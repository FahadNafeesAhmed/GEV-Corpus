"""Unattended overnight corpus build. Local GPU only, no external services.

    python overnight.py --hours 8

Designed to be launched and left alone on a machine nobody is watching:

  * Keeps Windows awake for the duration (SetThreadExecutionState), and releases
    that request on exit so the laptop can sleep normally afterwards.
  * Works through phases in value order against a global deadline. Each phase
    gets its own budget; when the clock runs out mid-phase it stops cleanly at a
    chunk boundary rather than being killed halfway through a write.
  * Survives Ollama dying: every phase is retried, and the model is re-warmed
    before each one. A phase that fails outright is logged and skipped, never
    fatal.
  * Commits continuously, so a hard power loss costs seconds of work, not hours.
  * Writes data/NIGHT_REPORT.md at the end - read that in the morning instead of
    the log.
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import sys
import time
import traceback
import urllib.request
from pathlib import Path

from common import DATA, connect, load_universe, log

import build_index          # noqa: F401  (imported for completeness of the pipeline)
import embed
import extract

STOP = False
REPORT = DATA / "NIGHT_REPORT.md"
PIDFILE = DATA / "overnight.pid"


def _sig(_signum, _frame):
    global STOP
    STOP = True
    log("signal received - finishing current batch then stopping")


# ----------------------------------------------------------------- power

class KeepAwake:
    """Stop Windows sleeping while the job runs, without touching power plans."""
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_AWAYMODE_REQUIRED = 0x00000040

    def __enter__(self):
        self.ok = False
        if os.name == "nt":
            try:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(
                    self.ES_CONTINUOUS | self.ES_SYSTEM_REQUIRED | self.ES_AWAYMODE_REQUIRED)
                self.ok = True
                log("sleep suppressed for the duration of this run")
            except Exception as exc:
                log(f"WARNING could not suppress sleep ({exc}); the run may be cut short")
        return self

    def __exit__(self, *exc):
        if self.ok:
            try:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(self.ES_CONTINUOUS)
                log("sleep suppression released")
            except Exception:
                pass


# ----------------------------------------------------------------- ollama

def ollama_up(timeout: int = 5) -> bool:
    try:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def wait_for_ollama(max_wait: int = 600) -> bool:
    """Ollama can be restarted by Windows update or crash; wait it out."""
    if ollama_up():
        return True
    log("ollama not responding - waiting for it to come back")
    start = time.time()
    while time.time() - start < max_wait:
        if STOP:
            return False
        time.sleep(15)
        if ollama_up():
            log(f"ollama back after {time.time()-start:.0f}s")
            return True
    log("ollama did not return")
    return False


def warm(model: str) -> None:
    """Load the model so the first real call is not paying a ~50s cold start."""
    try:
        body = json.dumps({"model": model, "prompt": "ok", "stream": False,
                           "think": False, "keep_alive": "60m",
                           "options": {"num_predict": 1}}).encode()
        req = urllib.request.Request("http://localhost:11434/api/generate", data=body,
                                     headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=300).read()
    except Exception as exc:
        log(f"  warm-up failed ({type(exc).__name__}) - continuing anyway")


# ----------------------------------------------------------------- phases

def phase_extract(con, name, ticker, deadline, model, limit=None):
    spec = extract.EXTRACTORS[name]
    rows = extract.pick_chunks(con, name, spec, ticker, limit)
    if not rows:
        return 0
    log(f"  {len(rows):,} chunks queued")
    done = found = 0
    t0 = time.time()
    for cid, text, acc, form, fdate, section, tick in rows:
        if STOP or time.time() > deadline:
            log(f"  stopping phase at {done}/{len(rows)} (deadline or signal)")
            break
        payload, ms = extract.ollama(spec["prompt"].format(chunk=text[:4000]),
                                     spec["schema"], model,
                                     num_predict=spec.get("num_predict", 900))
        ok = payload is not None
        con.execute(
            """INSERT OR REPLACE INTO extractions
               (ticker, chunk_id, extractor, model, ok, payload, elapsed_ms, ts)
               VALUES (?,?,?,?,?,?,?,?)""",
            (tick, cid, name, model, int(ok), json.dumps(payload or {}), ms,
             time.strftime("%Y-%m-%dT%H:%M:%S")))
        if ok:
            found += extract.flatten(con, name, (cid, acc, form, fdate, tick), payload)
        done += 1
        if done % 25 == 0:
            con.commit()
            rate = done / max(time.time() - t0, 1)
            log(f"    {done}/{len(rows)}  {found} items  {rate*60:.0f}/min  "
                f"ETA {(len(rows)-done)/max(rate,1e-6)/60:.0f}m")
    con.commit()
    log(f"  phase done: {done} chunks, {found} items, {(time.time()-t0)/60:.1f} min")
    return found


def phase_embed(con, ticker, deadline, batch=64):
    return embed.run(con, ticker, batch, embed.MODEL, deadline=deadline)


def phase_web(con, deadline, kinds):
    """Pull every angle from arXiv / OpenAlex / DDG / YouTube / RSS, then chunk it
    into the shared corpus and rebuild the search index. Network-bound, so it
    runs while the GPU is idle at the start of the night."""
    import ingest_web
    totals = ingest_web.run(con, ingest_web.load_angles(), None, kinds, deadline)
    log("  web totals: " + "  ".join(f"{k}={v}" for k, v in totals.items()))
    build_index.build_sources(con, __import__("common").load_config())
    build_index.rebuild_fts(con)
    return sum(totals.values())


def phase_module(con, deadline, fn):
    """Run one of the ingest/analysis modules under the phase deadline, then fold
    anything new into chunks + the search index. The filing re-chunk is skipped
    when no document changed - it is 215k upserts for nothing otherwise."""
    cfg = __import__("common").load_config()
    before = con.execute("SELECT COUNT(*), COALESCE(MAX(id),0) FROM documents").fetchone()
    src_before = con.execute("SELECT COUNT(*), COALESCE(MAX(version),1) FROM sources").fetchone()
    fn(con, deadline)
    after = con.execute("SELECT COUNT(*), COALESCE(MAX(id),0) FROM documents").fetchone()
    src_after = con.execute("SELECT COUNT(*), COALESCE(MAX(version),1) FROM sources").fetchone()
    changed = False
    if src_after != src_before:
        build_index.build_sources(con, cfg)
        changed = True
    if after != before:
        build_index.build(con, cfg)
        changed = True
    if changed:
        build_index.rebuild_fts(con)
    else:
        log("  no new documents - index unchanged")


def _derive(con, deadline):
    import derive
    derive.derive_mgmt_guidance(con)
    derive.derive_comps(con)
    derive.derive_backlog_spine(con)
    derive.derive_catalysts(con)
    derive.validation_sample(con)


def _primary(groups):
    def fn(con, deadline):
        import ingest_primary
        ingest_primary.run(con, groups, False, deadline)
    return fn


def _tabular(con, deadline):
    import ingest_tabular
    ingest_tabular.run(con, "2023-01", False, False, deadline)


def _thesis(con, deadline):
    import thesis
    thesis.run(con, thesis.candidate_claims(con, 16), extract.DEFAULT_MODEL, deadline)


def build_plan(gen_model):
    """Phases in the order the audit set: repairs run before launch (night2.cmd),
    then primary documents, customer/operator datasets, structured extraction,
    disagreement testing. Network-bound phases go first while the GPU is idle."""
    comp = [t["ticker"] for t in load_universe() if t["tier"] == "B"]
    peers = [t["ticker"] for t in load_universe() if t["tier"] == "C"]
    plan = [
        # --- primary documents -------------------------------------------
        ("primary: GEV IR transcripts, decks, investor days", "module", (_primary(["ir"]),), 0.75, None),
        ("primary: competitor reports (Siemens Energy, MHI, Vestas, Hitachi)", "module", (_primary(["competitors"]),), 0.75, None),
        # --- customer / operator datasets --------------------------------
        ("primary: grid-operator forecasts (PJM, ERCOT, NERC), all vintages", "module", (_primary(["operators"]),), 0.5, None),
        ("datasets: EIA-860M vintages, EIA-923, LBNL queue", "module", (_tabular,), 0.75, None),
        ("primary: named-customer SEC filings", "module", (_primary(["customers"]),), 1.0, None),
        ("web: refresh + all angles (versioned, arXiv fixed)", "web",
                 (["rss", "arxiv", "openalex", "web", "news", "youtube"],), 1.0, None),
        ("embeddings: everything new", "embed", ("ALL",), 1.5, None),
        # --- structured extraction ---------------------------------------
        ("retry the 85 failed extractions + remaining GEV guidance", "extract", ("guidance", "GEV"), 0.5, gen_model),
        ("GEV backlog / deposits / cash-timing series", "extract", ("backlog", "GEV"), 0.75, gen_model),
        ("GEV transcript language, quarter by quarter", "extract", ("transcript", "GEV"), 0.75, gen_model),
        ("competitor segment figures", "extract", ("competitor", "GEV"), 0.5, gen_model),
        # GEV-tagged chunks (its own filings, IR, and all web sources) first: a
        # project cited in GE Vernova's own release is the highest-value row.
        ("customer project facts - GEV-tagged sources first", "extract", ("project", "GEV"), 0.5, gen_model),
        ("customer project facts - all customers and peers", "extract", ("project", "ALL"), 1.0, gen_model),
        ("grid-operator forecast figures (vintage vs target year)", "extract", ("operator", "GEV"), 0.5, gen_model),
        ("attributed analyst calls (dated)", "extract", ("analyst", "GEV"), 0.5, gen_model),
        ("claims from papers/articles (continue)", "extract", ("claims", "GEV"), 1.5, gen_model),
        # --- derived tables (seconds, no GPU) then disagreement testing ----
        ("derive: guidance revisions, comps inputs, XBRL backlog spine, catalysts, validation CSV",
                 "module", (_derive,), 0.1, None),
        ("insight cards: disagreement testing", "module", (_thesis,), 1.0, None),
    ]
    for t in comp:
        plan.append((f"{t} guidance (continue)", "extract", ("guidance", t), 0.4, gen_model))
    plan.append(("all embeddings (continue)", "embed", ("ALL",), 3.0, None))
    for t in peers:
        plan.append((f"{t} guidance", "extract", ("guidance", t), 0.4, gen_model))
    for t in comp + peers:
        plan.append((f"{t} risk factors", "extract", ("risk", t), 0.4, gen_model))
    return plan


def write_report(con, started, phases_done, phases_failed):
    def one(sql, default=0):
        try:
            return con.execute(sql).fetchone()[0]
        except Exception:
            return default

    hrs = (time.time() - started) / 3600
    lines = [
        "# Overnight corpus build", "",
        f"Started {time.strftime('%Y-%m-%d %H:%M', time.localtime(started))}, "
        f"ran {hrs:.1f} hours, finished {time.strftime('%Y-%m-%d %H:%M')}.", "",
        "## Totals", "",
        "| | |", "|---|---|",
        f"| Tickers | {one('SELECT COUNT(DISTINCT ticker) FROM documents')} |",
        f"| Documents | {one('SELECT COUNT(*) FROM documents'):,} |",
        f"| Characters | {one('SELECT COALESCE(SUM(n_chars),0) FROM documents'):,} |",
        f"| Chunks | {one('SELECT COUNT(*) FROM chunks'):,} |",
        f"| **Embedded chunks** | **{one('SELECT COUNT(*) FROM embeddings'):,}** |",
        f"| **Chunks extracted** | **{one('SELECT COUNT(*) FROM extractions'):,}** |",
        f"| **Guidance items** | **{one('SELECT COUNT(*) FROM guidance'):,}** |",
        f"| **Risk items** | **{one('SELECT COUNT(*) FROM risk_items'):,}** |",
        f"| XBRL facts | {one('SELECT COUNT(*) FROM xbrl_facts'):,} |",
        f"| Extraction failures | {one('SELECT COUNT(*) FROM extractions WHERE ok=0'):,} |",
        f"| **Claims (web tier)** | **{one('SELECT COUNT(*) FROM claims'):,}** |",
        f"| Backlog series rows | {one('SELECT COUNT(*) FROM backlog_quarterly'):,} |",
        f"| Transcript statements | {one('SELECT COUNT(*) FROM transcript_statements'):,} |",
        f"| Customer projects | {one('SELECT COUNT(*) FROM projects'):,} |",
        f"| Analyst calls (attributed) | {one('SELECT COUNT(*) FROM analyst_calls'):,} |",
        f"| Competitor segment figures | {one('SELECT COUNT(*) FROM competitor_financials'):,} |",
        f"| EIA generator rows (all vintages) | {one('SELECT COUNT(*) FROM generators'):,} |",
        f"| Web sources / versions | {one('SELECT COUNT(*) FROM sources'):,} / {one('SELECT COUNT(*) FROM source_versions'):,} |",
        f"| **Insight cards** | **{one('SELECT COUNT(*) FROM insights'):,}** |",
        f"| Orphaned guidance rows (should be 0) | {one('SELECT COUNT(*) FROM guidance g LEFT JOIN chunks c ON c.id=g.chunk_id WHERE c.id IS NULL OR c.accession != g.accession'):,} |",
        "", "## Phases completed", "",
    ]
    lines += [f"- {p}" for p in phases_done] or ["- (none)"]
    if phases_failed:
        lines += ["", "## Phases that failed or were skipped", ""]
        lines += [f"- {p}" for p in phases_failed]

    lines += ["", "## Guidance found, by ticker", "", "| ticker | items |", "|---|---|"]
    try:
        for t, c in con.execute(
                "SELECT ticker, COUNT(*) c FROM guidance GROUP BY ticker ORDER BY c DESC"):
            lines.append(f"| {t} | {c:,} |")
    except Exception:
        pass

    lines += [
        "", "## Next", "",
        "```bash",
        'python src/ask.py search "backlog" --form 10-K',
        'python src/embed.py --search "pricing power in gas turbines" --ticker GEV',
        "python src/extract.py --status",
        "python src/backtest.py --ticker GEV",
        "```", "",
        "Quote fidelity was not re-checked automatically. Before using any extracted",
        "figure, confirm its `quote` appears in the source chunk (whitespace-insensitive)",
        "and take the number itself from `xbrl_facts`, never from the model.", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    log(f"report written to {REPORT}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--hours", type=float, default=8.0)
    p.add_argument("--model", default=extract.DEFAULT_MODEL)
    a = p.parse_args()

    signal.signal(signal.SIGINT, _sig)
    signal.signal(signal.SIGTERM, _sig)

    started = time.time()
    end = started + a.hours * 3600
    PIDFILE.parent.mkdir(parents=True, exist_ok=True)
    PIDFILE.write_text(str(os.getpid()), encoding="utf-8")

    log("=" * 68)
    log(f"OVERNIGHT RUN - budget {a.hours}h, ends "
        f"{time.strftime('%H:%M', time.localtime(end))}, pid {os.getpid()}")
    log("=" * 68)

    done_list, failed_list = [], []
    with KeepAwake():
        con = connect()
        if not wait_for_ollama():
            log("ollama unavailable at start - aborting")
            write_report(con, started, done_list, ["ollama unavailable"])
            return
        warm(a.model)

        for label, kind, args, budget_h, model in build_plan(a.model):
            if STOP or time.time() >= end:
                failed_list.append(f"{label} (out of time)")
                continue
            phase_end = min(time.time() + budget_h * 3600, end)
            log("-" * 68)
            log(f"PHASE: {label}   budget {budget_h}h, "
                f"until {time.strftime('%H:%M', time.localtime(phase_end))}")
            try:
                if not ollama_up() and not wait_for_ollama():
                    failed_list.append(f"{label} (ollama down)")
                    continue
                if kind == "extract":
                    name, ticker = args
                    warm(model)
                    phase_extract(con, name, ticker, phase_end, model)
                elif kind == "web":
                    phase_web(con, phase_end, args[0])
                elif kind == "module":
                    phase_module(con, phase_end, args[0])
                else:
                    phase_embed(con, args[0], phase_end)
                done_list.append(label)
            except Exception:
                log(f"PHASE FAILED: {label}\n{traceback.format_exc()}")
                failed_list.append(f"{label} (error)")
                time.sleep(20)

        write_report(con, started, done_list, failed_list)
        con.close()

    try:
        PIDFILE.unlink()
    except Exception:
        pass
    log(f"OVERNIGHT RUN COMPLETE - {(time.time()-started)/3600:.1f}h")


if __name__ == "__main__":
    main()
