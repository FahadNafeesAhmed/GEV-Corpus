"""Queued recursive debate orchestrator (LLM concurrency = 1)."""

from __future__ import annotations

import json
import logging
import re
import sqlite3
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Deque, Optional

from agents import (
    FOLLOWUP_SPECS,
    AgentSpec,
    make_critic,
    select_agents,
)
from config import (
    DEBATE_DB,
    DISCLOSURE_HEADER,
    KILL_CHECK_KEYS,
    LLM_CONCURRENCY,
    MAX_PROMPT_CHARS,
    OUT_DIR,
    RETRIEVAL_LIMIT,
)
from corpus import format_evidence, retrieve_fts, shard_queries
from ollama_client import chat

log = logging.getLogger("gev.debate.orch")

_KILL_RE = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in KILL_CHECK_KEYS) + r")\b"
    r"\s*[:=]\s*(unresolved|resolved|open|closed|unknown)",
    re.I,
)


@dataclass
class Task:
    kind: str  # gather | pitch | cross | critic | judge | followup
    agent: AgentSpec
    round_idx: int = 0
    depth: int = 0
    extra_context: str = ""
    shard_query: str = ""


@dataclass
class TaskResult:
    task_id: str
    kind: str
    agent_id: str
    side: str
    round_idx: int
    depth: int
    query: str
    evidence: list[dict[str, Any]]
    output: str
    unresolved_kills: list[str] = field(default_factory=list)
    elapsed_s: float = 0.0
    ts: str = ""


def _parse_unresolved(text: str, focus: list[str] | None = None) -> list[str]:
    found: dict[str, str] = {}
    for m in _KILL_RE.finditer(text or ""):
        key, status = m.group(1).lower(), m.group(2).lower()
        found[key] = status
    unresolved = [
        k for k, st in found.items()
        if st in ("unresolved", "open", "unknown")
    ]
    # If agent had kill_focus but never marked resolved, keep unresolved
    for k in focus or []:
        if k not in found and k not in unresolved:
            unresolved.append(k)
    return unresolved


def _ensure_out(out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def _init_debate_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS debate_runs (
                run_id TEXT PRIMARY KEY,
                started_at TEXT,
                finished_at TEXT,
                params_json TEXT
            );
            CREATE TABLE IF NOT EXISTS debate_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT,
                task_id TEXT,
                kind TEXT,
                agent_id TEXT,
                side TEXT,
                round_idx INTEGER,
                depth INTEGER,
                output TEXT,
                unresolved_json TEXT,
                elapsed_s REAL,
                ts TEXT
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


def _write_task_db(path: Path, run_id: str, r: TaskResult) -> None:
    conn = sqlite3.connect(str(path))
    try:
        conn.execute(
            """INSERT INTO debate_tasks
               (run_id, task_id, kind, agent_id, side, round_idx, depth,
                output, unresolved_json, elapsed_s, ts)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (
                run_id, r.task_id, r.kind, r.agent_id, r.side, r.round_idx,
                r.depth, r.output, json.dumps(r.unresolved_kills),
                r.elapsed_s, r.ts,
            ),
        )
        conn.commit()
    finally:
        conn.close()


class DebateOrchestrator:
    """Single-worker queue over gather → pitch → cross → critic* → judge → followups."""

    def __init__(
        self,
        *,
        rounds: int = 1,
        depth: int = 2,
        tasks_budget: int = 24,
        max_agents: int | None = None,
        angles: str = "all",
        out_dir: Path | None = None,
        debate_db: Path | None = None,
        dry_run: bool = False,
        write_db: bool = True,
    ) -> None:
        assert LLM_CONCURRENCY == 1 or True  # config already guards
        self.rounds = max(1, rounds)
        self.depth = max(0, depth)
        self.tasks_budget = max(1, tasks_budget)
        self.angles = angles
        self.agents = select_agents(angles, max_agents)
        self.out_dir = _ensure_out(out_dir or OUT_DIR)
        self.debate_db = debate_db or DEBATE_DB
        self.dry_run = dry_run
        self.write_db = write_db
        self.queue: Deque[Task] = deque()
        self.results: list[TaskResult] = []
        self.pitch_outputs: dict[str, str] = {}
        self.unresolved: set[str] = set()
        self.tasks_done = 0
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def _jsonl_path(self) -> Path:
        return self.out_dir / f"agents_{self.run_id}.jsonl"

    def _append_jsonl(self, r: TaskResult) -> None:
        with open(self._jsonl_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "task_id": r.task_id,
                "kind": r.kind,
                "agent_id": r.agent_id,
                "side": r.side,
                "round_idx": r.round_idx,
                "depth": r.depth,
                "query": r.query,
                "evidence": r.evidence,
                "output": r.output,
                "unresolved_kills": r.unresolved_kills,
                "elapsed_s": r.elapsed_s,
                "ts": r.ts,
            }, ensure_ascii=False) + "\n")

    def build_queue(self) -> None:
        pitch_agents = [a for a in self.agents if a.side in ("short", "long", "neutral", "meta")]
        judges = [a for a in self.agents if a.side == "judge"]
        if not judges:
            judges = [a for a in select_agents("all") if a.side == "judge"]

        # Budget split: ~40% gather shards, rest pitch/cross/critic/judge/followup
        n_gather = max(4, min(self.tasks_budget // 3, 80))
        base_qs: list[str] = []
        for a in pitch_agents:
            base_qs.extend(a.retrieval_queries)
        shards = shard_queries(base_qs or ["GEV backlog"], n_gather)

        for r in range(self.rounds):
            gatherer = AgentSpec(
                id="evidence_gatherer",
                side="meta",
                system=(
                    "You are an evidence gatherer. Summarize retrieved corpus hits "
                    "into bullet facts with [n] cites. Flag gaps. Research notes only."
                ),
                retrieval_queries=[],
            )
            for sq in shards:
                self.queue.append(Task("gather", gatherer, round_idx=r, shard_query=sq))

            for a in pitch_agents:
                self.queue.append(Task("pitch", a, round_idx=r))

            # Cross-examination slots (long attacks short & vice versa)
            shorts = [a for a in pitch_agents if a.side == "short"]
            longs = [a for a in pitch_agents if a.side == "long"]
            for s in shorts[:3]:
                for lng in longs[:2]:
                    cross = AgentSpec(
                        id=f"cross_{s.id}_vs_{lng.id}",
                        side="neutral",
                        system=(
                            f"Cross-examine LONG ({lng.id}) using SHORT frame ({s.id}). "
                            "Research notes only. Cite evidence. List kill-checks."
                        ),
                        retrieval_queries=s.retrieval_queries[:2] + lng.retrieval_queries[:2],
                        kill_focus=list(set(s.kill_focus + lng.kill_focus)),
                    )
                    self.queue.append(Task("cross", cross, round_idx=r))

            # Depth-1 critics on each pitch agent (more depth via recursion later)
            if self.depth >= 1:
                for a in pitch_agents:
                    if a.side in ("short", "long"):
                        self.queue.append(
                            Task("critic", make_critic(a, 1), round_idx=r, depth=1)
                        )

            for j in judges:
                self.queue.append(Task("judge", j, round_idx=r, depth=0))

        # Trim to budget (keep judges)
        if len(self.queue) > self.tasks_budget:
            kept: Deque[Task] = deque()
            judges_t = [t for t in self.queue if t.kind == "judge"]
            others = [t for t in self.queue if t.kind != "judge"]
            room = max(0, self.tasks_budget - len(judges_t))
            for t in others[:room]:
                kept.append(t)
            for t in judges_t:
                kept.append(t)
            self.queue = kept

        log.info("Queue built: %d tasks (budget=%d)", len(self.queue), self.tasks_budget)

    def _context_blob(self, limit_chars: int = 4000) -> str:
        parts: list[str] = []
        for r in self.results[-12:]:
            parts.append(f"### {r.kind}/{r.agent_id}\n{r.output[:800]}")
        blob = "\n\n".join(parts)
        return blob[:limit_chars]

    def _run_one(self, task: Task) -> TaskResult:
        queries = []
        if task.shard_query:
            queries = [task.shard_query]
        else:
            queries = list(task.agent.retrieval_queries) or ["GE Vernova GEV"]

        all_hits = []
        for q in queries[:3]:
            all_hits.extend(retrieve_fts(q, limit=max(2, RETRIEVAL_LIMIT // max(1, len(queries[:3])))) )
        # dedupe snippets
        seen = set()
        uniq = []
        for h in all_hits:
            key = h.snippet[:160]
            if key in seen:
                continue
            seen.add(key)
            uniq.append(h)
        evidence_txt = format_evidence(uniq)
        prior = self._context_blob()
        user = (
            f"Ticker: GEV (GE Vernova)\n"
            f"Task kind: {task.kind} | round={task.round_idx} | depth={task.depth}\n"
            f"Focus queries: {queries}\n\n"
            f"EVIDENCE (corpus excerpts; do not invent beyond this):\n{evidence_txt}\n\n"
        )
        if task.kind in ("cross", "critic", "judge", "followup"):
            user += f"PRIOR AGENT OUTPUTS (abbrev):\n{prior}\n\n"
        if task.extra_context:
            user += f"EXTRA:\n{task.extra_context[:2000]}\n\n"
        if task.kind == "judge":
            user += (
                "Synthesize: provisional winner LONG|SHORT|SPLIT, PT sketch "
                "(EPS x multiple), open kill criteria, follow-ups.\n"
            )
        user += "Respond as research notes with explicit kill-checks where relevant."

        if len(user) > MAX_PROMPT_CHARS:
            user = user[:MAX_PROMPT_CHARS] + "\n…[truncated]"

        messages = [
            {"role": "system", "content": task.agent.system},
            {"role": "user", "content": user},
        ]
        t0 = time.time()
        try:
            out = chat(messages, dry_run=self.dry_run)
        except Exception as e:
            out = f"[ERROR calling model] {e}"
            log.exception("chat failed for %s", task.agent.id)
        elapsed = time.time() - t0
        unresolved = _parse_unresolved(out, task.agent.kill_focus)
        for k in unresolved:
            self.unresolved.add(k)
        # Clear resolved from global set if explicitly resolved in this output
        for m in _KILL_RE.finditer(out or ""):
            key, status = m.group(1).lower(), m.group(2).lower()
            if status in ("resolved", "closed") and key in self.unresolved:
                self.unresolved.discard(key)

        tid = f"{task.kind}_{task.agent.id}_r{task.round_idx}_d{task.depth}_{self.tasks_done}"
        result = TaskResult(
            task_id=tid,
            kind=task.kind,
            agent_id=task.agent.id,
            side=task.agent.side,
            round_idx=task.round_idx,
            depth=task.depth,
            query="; ".join(queries),
            evidence=[h.to_dict() for h in uniq[:12]],
            output=out,
            unresolved_kills=unresolved,
            elapsed_s=round(elapsed, 3),
            ts=datetime.now().isoformat(timespec="seconds"),
        )
        if task.kind == "pitch":
            self.pitch_outputs[task.agent.id] = out
        return result

    def _spawn_followups(self, after_judge: bool = True) -> None:
        if self.depth < 1:
            return
        remaining = self.tasks_budget - self.tasks_done - len(self.queue)
        if remaining <= 0:
            return
        # Recursive critics of critics
        if after_judge:
            critic_results = [r for r in self.results if r.kind == "critic" and r.depth < self.depth]
            for cr in critic_results[-5:]:
                if remaining <= 0:
                    break
                parent = AgentSpec(
                    id=cr.agent_id, side="critic",
                    system="prior critic", retrieval_queries=[],
                )
                nxt = make_critic(parent, cr.depth + 1)
                nxt.id = f"critic_d{cr.depth + 1}_of_{cr.agent_id}"
                self.queue.append(Task(
                    "critic", nxt, round_idx=cr.round_idx, depth=cr.depth + 1,
                    extra_context=cr.output[:1500],
                ))
                remaining -= 1

        for key in list(self.unresolved):
            if remaining <= 0:
                break
            if key not in FOLLOWUP_SPECS:
                continue
            # avoid duplicate followups already done
            if any(r.agent_id == FOLLOWUP_SPECS[key].id for r in self.results):
                continue
            self.queue.append(Task("followup", FOLLOWUP_SPECS[key], depth=self.depth))
            remaining -= 1

    def run(self) -> Path:
        if self.write_db:
            _init_debate_db(self.debate_db)
            conn = sqlite3.connect(str(self.debate_db))
            try:
                conn.execute(
                    "INSERT OR REPLACE INTO debate_runs (run_id, started_at, params_json) VALUES (?,?,?)",
                    (self.run_id, datetime.now().isoformat(timespec="seconds"),
                     json.dumps({
                         "rounds": self.rounds, "depth": self.depth,
                         "tasks": self.tasks_budget, "angles": self.angles,
                         "dry_run": self.dry_run,
                     })),
                )
                conn.commit()
            finally:
                conn.close()

        self.build_queue()
        summary_path = self.out_dir / "ROUND_SUMMARY.md"
        judges_done = 0

        while self.queue and self.tasks_done < self.tasks_budget:
            task = self.queue.popleft()
            log.info(
                "[%d/%d] %s %s",
                self.tasks_done + 1, self.tasks_budget, task.kind, task.agent.id,
            )
            result = self._run_one(task)
            self.results.append(result)
            self._append_jsonl(result)
            if self.write_db:
                _write_task_db(self.debate_db, self.run_id, result)
            self.tasks_done += 1

            if task.kind == "judge":
                judges_done += 1
                self._spawn_followups(after_judge=True)
                # optional re-judge after followups if budget remains
                if self.unresolved and self.tasks_done < self.tasks_budget - 1:
                    # enqueue one more followup-aware judge pass
                    j = task.agent
                    self.queue.append(Task(
                        "judge", j, round_idx=task.round_idx, depth=task.depth + 1,
                        extra_context=f"Open kills: {sorted(self.unresolved)}",
                    ))

        self._write_summary(summary_path)
        if self.write_db:
            conn = sqlite3.connect(str(self.debate_db))
            try:
                conn.execute(
                    "UPDATE debate_runs SET finished_at=? WHERE run_id=?",
                    (datetime.now().isoformat(timespec="seconds"), self.run_id),
                )
                conn.commit()
            finally:
                conn.close()
        return summary_path

    def _write_summary(self, path: Path) -> None:
        lines = [
            DISCLOSURE_HEADER,
            f"# GEV Debate Round Summary",
            f"",
            f"- Run ID: `{self.run_id}`",
            f"- Tasks completed: {self.tasks_done} / budget {self.tasks_budget}",
            f"- Rounds: {self.rounds} | Depth: {self.depth} | Angles: {self.angles}",
            f"- Dry-run: {self.dry_run}",
            f"- Unresolved kill-checks: {sorted(self.unresolved) or '(none parsed)'}",
            f"- JSONL: `{self._jsonl_path().name}`",
            f"",
            f"## Agent results (abbrev)",
            f"",
        ]
        for r in self.results:
            lines.append(f"### [{r.kind}] {r.agent_id} ({r.side}) d={r.depth}")
            lines.append(f"- kills: {r.unresolved_kills or '—'}")
            lines.append(f"- elapsed: {r.elapsed_s}s")
            snippet = (r.output or "").strip().replace("\r", "")
            if len(snippet) > 1200:
                snippet = snippet[:1200] + "…"
            lines.append("")
            lines.append(snippet)
            lines.append("")
        # Last judge highlight
        judges = [r for r in self.results if r.kind == "judge"]
        if judges:
            lines.insert(
                8,
                f"- Latest judge: `{judges[-1].agent_id}` @ {judges[-1].ts}",
            )
        path.write_text("\n".join(lines), encoding="utf-8")
        log.info("Wrote %s", path)
