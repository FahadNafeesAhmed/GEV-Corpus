#!/usr/bin/env python3
"""CLI for recursive GEV multi-agent pitch debate (local DeepSeek R1)."""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config
from orchestrator import DebateOrchestrator


def main() -> int:
    ap = argparse.ArgumentParser(description="GEV recursive multi-agent pitch debate")
    ap.add_argument("--tasks", type=int, default=config.DEFAULT_TASKS,
                    help="queued agent tasks (not concurrent LLMs)")
    ap.add_argument("--depth", type=int, default=config.DEFAULT_DEPTH)
    ap.add_argument("--rounds", type=int, default=1)
    ap.add_argument("--max-agents", type=int, default=None)
    ap.add_argument("--angles", type=str, default="all")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", type=str, default="")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    out = Path(args.out) if args.out else config.OUT_DIR
    print(f"model={config.MODEL_NAME} corpus={config.CORPUS_DB} out={out}")
    print(f"tasks={args.tasks} depth={args.depth} concurrency={config.LLM_CONCURRENCY}")

    orch = DebateOrchestrator(
        rounds=args.rounds,
        depth=args.depth,
        tasks_budget=args.tasks,
        max_agents=args.max_agents,
        angles=args.angles,
        out_dir=out,
        dry_run=args.dry_run,
    )
    summary = orch.run()
    print("DONE summary=", summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
