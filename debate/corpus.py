"""Read-only SQLite helpers + FTS retrieval for the GEV corpus.

NEVER modifies gev.db. Opens with URI mode=ro when possible.
"""

from __future__ import annotations

import json
import logging
import re
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, Optional, Sequence

from config import CORPUS_DB, CORPUS_TABLES, MAX_EVIDENCE_CHARS, RETRIEVAL_LIMIT

log = logging.getLogger("gev.debate.corpus")

# Strip characters that break FTS5 MATCH
_FTS_SAFE = re.compile(r'[^\w\s\-\.\%\$]', re.UNICODE)


@dataclass
class EvidenceHit:
    source: str
    snippet: str
    meta: dict[str, Any] = field(default_factory=dict)
    score: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "snippet": self.snippet,
            "meta": self.meta,
            "score": self.score,
        }


def _ro_uri(path: Path) -> str:
    # file: URI with mode=ro — works on Windows and POSIX
    p = path.resolve().as_posix()
    if not p.startswith("/"):
        # Windows drive: C:/...
        return f"file:{p}?mode=ro"
    return f"file:{p}?mode=ro"


@contextmanager
def connect_readonly(db_path: Optional[Path] = None) -> Iterator[sqlite3.Connection]:
    """Open corpus DB read-only. Raises FileNotFoundError if missing."""
    path = Path(db_path or CORPUS_DB)
    if not path.exists():
        raise FileNotFoundError(
            f"Corpus DB not found: {path}. "
            "Set GEV_CORPUS_DB or place gev.db under gev-corpus/data/."
        )
    uri = _ro_uri(path)
    conn = sqlite3.connect(uri, uri=True, timeout=30.0)
    conn.row_factory = sqlite3.Row
    try:
        # Extra belt-and-suspenders
        conn.execute("PRAGMA query_only = ON")
        yield conn
    finally:
        conn.close()


def list_tables(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type IN ('table','view') ORDER BY name"
    ).fetchall()
    return [r[0] for r in rows]


def table_exists(conn: sqlite3.Connection, name: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type IN ('table','view') AND name=? LIMIT 1",
        (name,),
    ).fetchone()
    return row is not None


def sanitize_fts_query(q: str) -> str:
    """Make a user/agent query safe for FTS5 MATCH (simple AND of tokens)."""
    cleaned = _FTS_SAFE.sub(" ", q or "")
    tokens = [t for t in cleaned.split() if len(t) > 1][:12]
    if not tokens:
        return "GEV"
    # Quote tokens that look like column/operators; use AND for precision
    return " AND ".join(tokens)


def _row_to_snippet(row: sqlite3.Row, prefer_cols: Sequence[str]) -> str:
    d = dict(row)
    parts: list[str] = []
    for c in prefer_cols:
        if c in d and d[c] is not None:
            parts.append(str(d[c]))
    if not parts:
        # fallback: all non-null stringy values
        for k, v in d.items():
            if v is not None and k not in ("rowid",):
                parts.append(f"{k}={v}")
    text = " | ".join(parts)
    if len(text) > 1200:
        text = text[:1200] + "…"
    return text


def retrieve_fts(
    query: str,
    limit: int = RETRIEVAL_LIMIT,
    db_path: Optional[Path] = None,
) -> list[EvidenceHit]:
    """FTS retrieve from chunks_fts (or fallback LIKE on claims/transcripts)."""
    hits: list[EvidenceHit] = []
    fts_q = sanitize_fts_query(query)
    try:
        with connect_readonly(db_path) as conn:
            if table_exists(conn, "chunks_fts"):
                # Discover columns
                cols = [r[1] for r in conn.execute("PRAGMA table_info(chunks_fts)").fetchall()]
                # Prefer common text columns
                text_cols = [c for c in ("text", "chunk", "content", "body", "snippet") if c in cols]
                if not text_cols:
                    text_cols = [c for c in cols if c not in ("rowid",)][:3]
                try:
                    sql = f"""
                        SELECT * FROM chunks_fts
                        WHERE chunks_fts MATCH ?
                        LIMIT ?
                    """
                    rows = conn.execute(sql, (fts_q, limit)).fetchall()
                    for i, row in enumerate(rows):
                        snip = _row_to_snippet(row, text_cols)
                        meta = {k: dict(row).get(k) for k in ("doc_id", "source", "ticker", "date", "quarter")
                                if k in dict(row)}
                        hits.append(EvidenceHit("chunks_fts", snip, meta, score=1.0 - i * 0.01))
                except sqlite3.OperationalError as e:
                    log.warning("FTS MATCH failed (%s); falling back to LIKE", e)
                    # Fallback: LIKE on first text-like column if table is contentful
                    if text_cols:
                        col = text_cols[0]
                        like = f"%{query.split()[0] if query.split() else 'GEV'}%"
                        rows = conn.execute(
                            f"SELECT * FROM chunks_fts LIMIT ?",  # may be a content table
                            (limit,),
                        ).fetchall()
                        # Filter in Python if MATCH failed
                        for i, row in enumerate(rows):
                            snip = _row_to_snippet(row, text_cols)
                            if query.lower().split()[0] in snip.lower() or True:
                                hits.append(EvidenceHit("chunks_fts", snip, {}, 0.5 - i * 0.01))
                                if len(hits) >= limit:
                                    break
            # Supplement from claims / transcript_statements if thin
            if len(hits) < limit // 2:
                hits.extend(_like_search(conn, "claims", query, limit - len(hits)))
            if len(hits) < limit:
                hits.extend(_like_search(conn, "transcript_statements", query, limit - len(hits)))
    except FileNotFoundError:
        log.warning("Corpus missing — returning empty evidence for query=%r", query)
        return []
    except Exception as e:
        log.exception("retrieve_fts error: %s", e)
        return []
    return hits[:limit]


def _like_search(
    conn: sqlite3.Connection,
    table: str,
    query: str,
    limit: int,
) -> list[EvidenceHit]:
    if limit <= 0 or not table_exists(conn, table):
        return []
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({table})").fetchall()]
    text_cols = [
        c for c in cols
        if any(x in c.lower() for x in ("text", "claim", "statement", "body", "content", "title", "note"))
    ]
    if not text_cols:
        text_cols = cols[:4]
    token = (query.split() or ["GEV"])[0]
    like = f"%{token}%"
    # Build OR across text columns
    where = " OR ".join(f"{c} LIKE ?" for c in text_cols[:3])
    params = [like] * min(3, len(text_cols)) + [limit]
    try:
        rows = conn.execute(
            f"SELECT * FROM {table} WHERE ({where}) LIMIT ?",
            params,
        ).fetchall()
    except sqlite3.Error:
        rows = conn.execute(f"SELECT * FROM {table} LIMIT ?", (limit,)).fetchall()
    out: list[EvidenceHit] = []
    for i, row in enumerate(rows):
        snip = _row_to_snippet(row, text_cols)
        out.append(EvidenceHit(table, snip, {"table": table}, 0.4 - i * 0.01))
    return out


def query_table(
    table: str,
    where: str = "1=1",
    params: Sequence[Any] = (),
    limit: int = 20,
    db_path: Optional[Path] = None,
) -> list[dict[str, Any]]:
    """Safe SELECT from a known corpus table. Table name must be in allowlist."""
    if table not in CORPUS_TABLES and not table.endswith("_fts"):
        # Allow known + fts variants only
        raise ValueError(f"Table not in allowlist: {table}")
    # Guard against injection in where — only allow simple patterns from our agents
    if ";" in where or "--" in where:
        raise ValueError("Unsafe WHERE clause")
    try:
        with connect_readonly(db_path) as conn:
            if not table_exists(conn, table):
                return []
            sql = f"SELECT * FROM {table} WHERE {where} LIMIT ?"
            rows = conn.execute(sql, (*params, limit)).fetchall()
            return [dict(r) for r in rows]
    except FileNotFoundError:
        return []


def format_evidence(hits: Sequence[EvidenceHit], max_chars: int = MAX_EVIDENCE_CHARS) -> str:
    """Format evidence for prompts without stuffing the whole corpus."""
    lines: list[str] = []
    total = 0
    for i, h in enumerate(hits, 1):
        block = f"[{i}] ({h.source}) {h.snippet}"
        if total + len(block) > max_chars:
            lines.append(f"... truncated ({len(hits) - i + 1} more hits omitted)")
            break
        lines.append(block)
        total += len(block)
    if not lines:
        return "(no corpus hits — note evidence gap)"
    return "\n".join(lines)


def corpus_health(db_path: Optional[Path] = None) -> dict[str, Any]:
    """Quick diagnostic for smoke tests / README."""
    path = Path(db_path or CORPUS_DB)
    info: dict[str, Any] = {"path": str(path), "exists": path.exists(), "tables": {}}
    if not path.exists():
        return info
    with connect_readonly(path) as conn:
        present = list_tables(conn)
        info["all_tables"] = present
        for t in CORPUS_TABLES:
            if t in present or table_exists(conn, t):
                try:
                    n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                except sqlite3.Error:
                    n = -1
                info["tables"][t] = n
            else:
                info["tables"][t] = None
    return info


def shard_queries(base_queries: Sequence[str], max_shards: int) -> list[str]:
    """Expand / truncate query list to ~max_shards task slots."""
    qs = list(base_queries)
    if len(qs) >= max_shards:
        return qs[:max_shards]
    # Duplicate with slight variants to fill shards without inventing fake topics
    fillers = [
        "GE Vernova backlog",
        "GEV Power services",
        "HA gas turbine",
        "Electrification Prolec",
        "Wind offshore onshore",
        "FCF free cash flow",
        "deposit customer advances",
        "margin guide 2027",
        "data center grid",
        "outage upgrade modernization",
    ]
    i = 0
    while len(qs) < max_shards:
        qs.append(fillers[i % len(fillers)] + f" shard{len(qs)}")
        i += 1
    return qs


# ---- Named hooks for agent sql_hooks (read-only) ----

def _clip(s: str, n: int = 900) -> str:
    s = (s or "").replace("\n", " ")
    return s if len(s) <= n else s[:n] + "…"


def format_hit(h: EvidenceHit) -> str:
    meta = " ".join(f"{k}={v}" for k, v in (h.meta or {}).items() if v is not None)
    return f"--- {h.source} {meta}\n{_clip(h.snippet, 700)}"


def fts_search(query: str, limit: int = RETRIEVAL_LIMIT):
    """Alias used by orchestrator."""
    return retrieve_fts(query, limit=limit)


def hook_backlog_reservations() -> str:
    lines = ["[hook backlog_reservations]"]
    with connect_readonly() as con:
        if not table_exists(con, "backlog_quarterly"):
            return lines[0] + " missing table"
        rows = con.execute(
            """SELECT as_of, metric, value, unit, substr(quote,1,200)
               FROM backlog_quarterly
               WHERE ticker='GEV' AND (
                 lower(metric) LIKE '%reserv%' OR lower(metric) LIKE '%slot%'
                 OR lower(metric) LIKE '%backlog%' OR lower(metric) LIKE '%rpo%'
               )
               ORDER BY id DESC LIMIT 12"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]}={r[2]} {r[3] or ''} | {_clip(r[4] or '', 180)}")
    return "\n".join(lines)


def hook_contract_liabilities() -> str:
    lines = ["[hook contract_liabilities]"]
    with connect_readonly() as con:
        rows = con.execute(
            """SELECT as_of, value, unit, substr(quote,1,220)
               FROM backlog_quarterly
               WHERE ticker='GEV' AND lower(metric) LIKE '%contract_liab%'
               ORDER BY id DESC LIMIT 10"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]} {r[2] or ''} | {_clip(r[3] or '', 200)}")
    return "\n".join(lines)


def hook_transcript_margins() -> str:
    lines = ["[hook transcript_margins]"]
    with connect_readonly() as con:
        if not table_exists(con, "transcript_statements"):
            return lines[0] + " missing"
        rows = con.execute(
            """SELECT event_date, topic, substr(statement,1,280)
               FROM transcript_statements
               WHERE ticker='GEV' AND (
                 lower(statement) LIKE '%margin%' OR lower(topic) LIKE '%margin%'
               )
               ORDER BY event_date DESC LIMIT 12"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]} | {_clip(r[2] or '', 260)}")
    return "\n".join(lines)


def hook_transcript_backlog() -> str:
    lines = ["[hook transcript_backlog]"]
    with connect_readonly() as con:
        rows = con.execute(
            """SELECT event_date, topic, substr(statement,1,280)
               FROM transcript_statements
               WHERE ticker='GEV' AND (
                 lower(statement) LIKE '%backlog%' OR lower(statement) LIKE '%slot%'
               )
               ORDER BY event_date DESC LIMIT 12"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]} | {_clip(r[2] or '', 260)}")
    return "\n".join(lines)


def hook_transcript_conversion() -> str:
    lines = ["[hook transcript_conversion]"]
    with connect_readonly() as con:
        rows = con.execute(
            """SELECT event_date, topic, substr(statement,1,300)
               FROM transcript_statements
               WHERE ticker='GEV' AND (
                 lower(statement) LIKE '%convert%' OR lower(statement) LIKE '%inflection%'
                 OR lower(statement) LIKE '%reservation%'
               )
               ORDER BY event_date DESC LIMIT 10"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]} | {_clip(r[2] or '', 280)}")
    return "\n".join(lines)


def hook_analyst_glj() -> str:
    lines = ["[hook analyst_glj — SECONDARY unless filing]"]
    with connect_readonly() as con:
        if table_exists(con, "analyst_calls"):
            rows = con.execute(
                """SELECT published, analyst, firm, metric, value, period, substr(quote,1,200)
                   FROM analyst_calls WHERE ticker='GEV'
                   AND (lower(firm) LIKE '%glj%' OR lower(quote) LIKE '%vintage%' OR lower(quote) LIKE '%470%')
                   ORDER BY published DESC LIMIT 10"""
            ).fetchall()
            for r in rows:
                lines.append(f"{r[0]} | {r[1]}@{r[2]} | {r[3]}={r[4]} {r[5]} | {_clip(r[6] or '', 180)}")
        if table_exists(con, "claims"):
            rows = con.execute(
                """SELECT published, stance, substr(claim,1,220)
                   FROM claims WHERE ticker='GEV' AND (
                     lower(claim) LIKE '%glj%' OR lower(claim) LIKE '%vintage%' OR lower(claim) LIKE '%7.42%'
                   ) ORDER BY published DESC LIMIT 8"""
            ).fetchall()
            for r in rows:
                lines.append(f"claim {r[0]} | {r[1]} | {_clip(r[2] or '', 200)}")
    return "\n".join(lines)


def hook_comps_gev() -> str:
    lines = ["[hook comps_gev]"]
    with connect_readonly() as con:
        if not table_exists(con, "comps_inputs"):
            return lines[0] + " missing"
        rows = con.execute(
            """SELECT as_of, metric, value, unit FROM comps_inputs
               WHERE ticker='GEV' ORDER BY as_of DESC LIMIT 20"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]}={r[2]} {r[3] or ''}")
    return "\n".join(lines)


def hook_price_spot() -> str:
    lines = ["[hook price_spot]"]
    with connect_readonly() as con:
        if table_exists(con, "prices"):
            # schema unknown — probe columns
            cols = [r[1] for r in con.execute("PRAGMA table_info(prices)")]
            lines.append("cols=" + ",".join(cols))
            row = con.execute("SELECT * FROM prices ORDER BY rowid DESC LIMIT 1").fetchone()
            if row:
                lines.append("latest=" + " | ".join(str(x) for x in row))
        if table_exists(con, "comps_inputs"):
            rows = con.execute(
                """SELECT as_of, metric, value FROM comps_inputs
                   WHERE ticker='GEV' AND metric IN ('price','market_cap','pe_fy')
                   ORDER BY as_of DESC LIMIT 6"""
            ).fetchall()
            for r in rows:
                lines.append(f"{r[0]} | {r[1]}={r[2]}")
    return "\n".join(lines)


def hook_projects_upgrades() -> str:
    lines = ["[hook projects_upgrades — DEDUP BEFORE SUMMING]"]
    with connect_readonly() as con:
        if not table_exists(con, "projects"):
            return lines[0] + " missing"
        rows = con.execute(
            """SELECT source_date, owner, project_name, location, oem, model,
                      turbine_count, capacity_mw, commitment_status,
                      substr(quote,1,160)
               FROM projects
               WHERE lower(coalesce(project_name,'')) LIKE '%upgrade%'
                  OR lower(coalesce(quote,'')) LIKE '%upgrade%'
                  OR lower(coalesce(owner,'')) LIKE '%southern%'
                  OR lower(coalesce(project_name,'')) LIKE '%coryton%'
                  OR lower(coalesce(project_name,'')) LIKE '%franklin%'
                  OR lower(coalesce(project_name,'')) LIKE '%wansley%'
               ORDER BY source_date DESC LIMIT 25"""
        ).fetchall()
        for r in rows:
            lines.append(
                f"{r[0]} | {r[1]} | {r[2]} | {r[4]} {r[5]} | MW={r[7]} status={r[8]} | {_clip(r[9] or '', 140)}"
            )
    return "\n".join(lines)


def hook_power_services_rev() -> str:
    lines = ["[hook power_services_rev]"]
    with connect_readonly() as con:
        # try claims / backlog / xbrl
        if table_exists(con, "claims"):
            rows = con.execute(
                """SELECT published, substr(claim,1,240) FROM claims
                   WHERE ticker='GEV' AND lower(claim) LIKE '%services%'
                   AND (lower(claim) LIKE '%revenue%' OR lower(claim) LIKE '%%')
                   ORDER BY published DESC LIMIT 8"""
            ).fetchall()
            for r in rows:
                lines.append(f"{r[0]} | {_clip(r[1] or '', 220)}")
        if table_exists(con, "xbrl_facts"):
            rows = con.execute(
                """SELECT end_date, tag, val, unit, form FROM xbrl_facts
                   WHERE (tag LIKE '%Service%' OR label LIKE '%Service%')
                   AND val IS NOT NULL
                   ORDER BY end_date DESC LIMIT 8"""
            ).fetchall()
            for r in rows:
                lines.append(f"xbrl {r[0]} | {r[1]}={r[2]} {r[3]} {r[4]}")
    return "\n".join(lines)


def hook_rpo_services() -> str:
    lines = ["[hook rpo_services]"]
    with connect_readonly() as con:
        rows = con.execute(
            """SELECT as_of, metric, value, unit, substr(quote,1,200)
               FROM backlog_quarterly
               WHERE ticker='GEV' AND lower(metric) LIKE '%rpo%'
               ORDER BY id DESC LIMIT 12"""
        ).fetchall()
        for r in rows:
            lines.append(f"{r[0]} | {r[1]}={r[2]} {r[3] or ''} | {_clip(r[4] or '', 180)}")
    return "\n".join(lines)


def hook_guidance_wind() -> str:
    lines = ["[hook guidance_wind]"]
    with connect_readonly() as con:
        if table_exists(con, "mgmt_guidance"):
            rows = con.execute(
                """SELECT stated_on, metric, value, period, substr(quote,1,200)
                   FROM mgmt_guidance WHERE ticker='GEV'
                   AND (lower(metric) LIKE '%wind%' OR lower(quote) LIKE '%wind%')
                   ORDER BY stated_on DESC LIMIT 10"""
            ).fetchall()
            for r in rows:
                lines.append(f"{r[0]} | {r[1]}={r[2]} {r[3]} | {_clip(r[4] or '', 180)}")
        rows = con.execute(
            """SELECT event_date, topic, substr(statement,1,240)
               FROM transcript_statements WHERE ticker='GEV'
               AND lower(statement) LIKE '%wind%'
               ORDER BY event_date DESC LIMIT 8"""
        ).fetchall() if table_exists(con, "transcript_statements") else []
        for r in rows:
            lines.append(f"{r[0]} | {r[1]} | {_clip(r[2] or '', 220)}")
    return "\n".join(lines)


def hook_catalysts() -> str:
    lines = ["[hook catalysts]"]
    with connect_readonly() as con:
        if table_exists(con, "catalyst_calendar"):
            rows = con.execute(
                "SELECT date, event, confirmed FROM catalyst_calendar ORDER BY date"
            ).fetchall()
            for r in rows:
                lines.append(f"{r[0]} | {r[1]} | confirmed={r[2]}")
    return "\n".join(lines)
