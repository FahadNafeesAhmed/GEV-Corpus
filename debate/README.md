# GEV recursive multi-agent pitch debate

**Research notes only — not a Citadel submission.** Local Ollama `deepseek-r1-distill:7b` debates long/short angles against `data/gev.db`.

## Hardware
RTX 5060 8GB: **one** LLM at a time. `--tasks 200` means 200 queued agent roles/shards, not 200 simultaneous models.

## Run
```bat
cd "debate"
python run_debate.py --tasks 48 --depth 2 -v
python run_debate.py --tasks 200 --depth 3
```

Outputs: `out/ROUND_SUMMARY.md`, `out/tasks_run*.jsonl`, `debate.db`.

## Disclosure
Stamp AI-research use if any notes feed the memo. Final memo/model must be human-written per competition rules.
