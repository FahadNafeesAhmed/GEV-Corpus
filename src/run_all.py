"""Orchestrator: run every ingest stage in order. Resumable - safe to re-run."""
from __future__ import annotations

import sys
import time
import traceback

import build_index
import ingest_market
import ingest_sec
from common import Fetcher, connect, load_config, log, write_default_config

STAGES = [
    ("sec_index", lambda con, f, cfg: ingest_sec.fetch_index(con, f)),
    ("sec_documents", lambda con, f, cfg: ingest_sec.fetch_documents(con, f, cfg)),
    ("xbrl_facts", lambda con, f, cfg: ingest_market.fetch_xbrl(con, f)),
    ("prices", lambda con, f, cfg: ingest_market.fetch_prices(con, f)),
    ("insiders", lambda con, f, cfg: ingest_sec.fetch_insiders(con, f)),
    ("chunk_and_index", lambda con, f, cfg: build_index.build(con, cfg)),
]


def report(con) -> None:
    log("=" * 68)
    log("CORPUS SUMMARY")
    for label, sql in [
        ("filings indexed", "SELECT COUNT(*) FROM filings"),
        ("documents (full text)", "SELECT COUNT(*) FROM documents"),
        ("characters of text", "SELECT COALESCE(SUM(n_chars),0) FROM documents"),
        ("searchable chunks", "SELECT COUNT(*) FROM chunks"),
        ("xbrl facts", "SELECT COUNT(*) FROM xbrl_facts"),
        ("distinct xbrl tags", "SELECT COUNT(DISTINCT tag) FROM xbrl_facts"),
        ("price days", "SELECT COUNT(*) FROM prices"),
        ("insider transactions", "SELECT COUNT(*) FROM insider_tx"),
        ("news articles", "SELECT COUNT(*) FROM news"),
    ]:
        try:
            log(f"  {label:<24} {con.execute(sql).fetchone()[0]:,}")
        except Exception:
            log(f"  {label:<24} -")
    log("=" * 68)


def main():
    started = time.time()
    write_default_config()
    cfg = load_config()
    con = connect()
    fetch = Fetcher(cfg)

    only = sys.argv[1:] or None
    for name, fn in STAGES:
        if only and name not in only:
            continue
        log("-" * 68)
        log(f"STAGE: {name}")
        t0 = time.time()
        try:
            fn(con, fetch, cfg)
            log(f"STAGE {name} done in {time.time() - t0:.1f}s")
        except Exception:
            # One bad stage must not abort an overnight run.
            log(f"STAGE {name} FAILED:\n{traceback.format_exc()}")

    report(con)
    log(f"total elapsed {time.time() - started:.1f}s")
    con.close()


if __name__ == "__main__":
    main()
