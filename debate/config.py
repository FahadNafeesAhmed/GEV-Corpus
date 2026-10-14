"""Configuration for GEV debate system.

Paths default to Windows Citadel layout; override via env or CLI.
Hardware: RTX 5060 8GB VRAM, ~15GB RAM — concurrency MUST stay at 1.
"""

from __future__ import annotations

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (Windows-first; pathlib handles both platforms)
# ---------------------------------------------------------------------------
# Destination when copied: debate\
DEBATE_ROOT = Path(__file__).resolve().parent

# Corpus DB lives one level up from debate/ under gev-corpus/data/
_DEFAULT_CORPUS = DEBATE_ROOT.parent / "data" / "gev.db"
# Fallback for Linux box / smoke tests without the real DB
_FALLBACK_CORPUS = DEBATE_ROOT.parent / "data" / "gev.db"

CORPUS_DB = Path(os.environ.get("GEV_CORPUS_DB", str(_DEFAULT_CORPUS)))
if not CORPUS_DB.exists():
    alt = Path(os.environ.get("GEV_CORPUS_DB_FALLBACK", str(_FALLBACK_CORPUS)))
    if alt.exists():
        CORPUS_DB = alt

OUT_DIR = Path(os.environ.get("GEV_DEBATE_OUT", str(DEBATE_ROOT / "out")))
DEBATE_DB = Path(os.environ.get("GEV_DEBATE_DB", str(DEBATE_ROOT / "debate.db")))

# ---------------------------------------------------------------------------
# Ollama / model
# ---------------------------------------------------------------------------
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
# Official deepseek-r1:8b pull never finished — use distill only
MODEL_NAME = os.environ.get("GEV_DEBATE_MODEL", "deepseek-r1-distill:7b")
EMBED_MODEL = os.environ.get("GEV_EMBED_MODEL", "nomic-embed-text")
ALT_MODEL = os.environ.get("GEV_ALT_MODEL", "qwen3:8b")

# ---------------------------------------------------------------------------
# Hardware safety — NEVER raise concurrency without explicit override
# ---------------------------------------------------------------------------
# Single LLM worker queue. Optional 1 embed parallel is allowed separately.
LLM_CONCURRENCY = int(os.environ.get("GEV_LLM_CONCURRENCY", "1"))
EMBED_CONCURRENCY = int(os.environ.get("GEV_EMBED_CONCURRENCY", "1"))
assert LLM_CONCURRENCY == 1 or os.environ.get("GEV_ALLOW_MULTI_LLM") == "1", (
    "LLM_CONCURRENCY must be 1 on 8GB VRAM laptop (set GEV_ALLOW_MULTI_LLM=1 to override)"
)

# Generation limits (keep VRAM/RAM safe)
MAX_TOKENS = int(os.environ.get("GEV_MAX_TOKENS", "1024"))
TEMPERATURE = float(os.environ.get("GEV_TEMPERATURE", "0.3"))
REQUEST_TIMEOUT_S = int(os.environ.get("GEV_OLLAMA_TIMEOUT", "180"))
MAX_RETRIES = int(os.environ.get("GEV_OLLAMA_RETRIES", "2"))
RETRY_BACKOFF_S = float(os.environ.get("GEV_RETRY_BACKOFF", "3.0"))

# Context / retrieval
RETRIEVAL_LIMIT = int(os.environ.get("GEV_RETRIEVAL_LIMIT", "8"))
MAX_EVIDENCE_CHARS = int(os.environ.get("GEV_MAX_EVIDENCE_CHARS", "6000"))
MAX_PROMPT_CHARS = int(os.environ.get("GEV_MAX_PROMPT_CHARS", "14000"))

# Debate scale knobs
DEFAULT_ROUNDS = 1
DEFAULT_DEPTH = 2
DEFAULT_TASKS = 24  # smoke; production may use --tasks 200
MAX_AGENTS_DEFAULT = 40

# Kill-check keys that can spawn follow-up agents
KILL_CHECK_KEYS = (
    "deposit_terms",
    "vintage_primary_source",
    "upgrade_ebitda_bridge",
    "fcf_quality",
    "wind_drag_quantum",
    "prolec_quality",
    "ha_backlog_scarcity",
    "multiple_compression",
)

# Disclosure header stamped on every durable output
DISCLOSURE_HEADER = """\
# RESEARCH NOTES — NOT A COMPETITION SUBMISSION

**AI-research disclosure:** This document was produced by a local multi-agent
debate system (Ollama / deepseek-r1-distill:7b) retrieving from a private GEV
SQLite corpus. Outputs are **initial research notes only**, not investment
advice, and not a Citadel stock-pitch competition submission. Verify all
numbers against primary filings before use.

---
"""

# Known corpus tables (read-only; never ALTER gev.db)
CORPUS_TABLES = (
    "chunks_fts",
    "backlog_quarterly",
    "claims",
    "transcript_statements",
    "projects",
    "generation",
    "generators",
    "guidance",
    "mgmt_guidance",
    "xbrl_facts",
    "prices",
    "comps_inputs",
    "risk_items",
)
