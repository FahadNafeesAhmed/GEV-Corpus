"""Ollama chat client for deepseek-r1-distill:7b.

Single-worker friendly: callers serialize via orchestrator queue.
Strips <think>…</think> / reasoning tags when present.
"""

from __future__ import annotations

import json
import logging
import re
import time
import urllib.error
import urllib.request
from typing import Any, Optional

from config import (
    MAX_RETRIES,
    MAX_TOKENS,
    MODEL_NAME,
    OLLAMA_HOST,
    REQUEST_TIMEOUT_S,
    RETRY_BACKOFF_S,
    TEMPERATURE,
)

log = logging.getLogger("gev.debate.ollama")

# deepseek-r1 distill often emits thinking blocks
_THINK_RE = re.compile(
    r"<think>[\s\S]*?</think>|"
    r"<thinking>[\s\S]*?</thinking>|"
    r"<reasoning>[\s\S]*?</reasoning>",
    re.IGNORECASE,
)


def strip_thinking(text: str) -> str:
    if not text:
        return ""
    cleaned = _THINK_RE.sub("", text)
    # Also drop leading "Thinking Process:" style monologues if model leaks them
    lines = cleaned.splitlines()
    out: list[str] = []
    skip_preamble = True
    for line in lines:
        if skip_preamble and re.match(r"^(thinking|reasoning)\b", line.strip(), re.I):
            continue
        if skip_preamble and not line.strip():
            continue
        skip_preamble = False
        out.append(line)
    return "\n".join(out).strip()


def _post_json(url: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
    return json.loads(raw)


def chat(
    messages: list[dict[str, str]],
    *,
    model: Optional[str] = None,
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = REQUEST_TIMEOUT_S,
    dry_run: bool = False,
) -> str:
    """Chat completion via Ollama /api/chat. Returns stripped assistant text.

    dry_run: return a stub string without calling Ollama (smoke tests offline).
    """
    model = model or MODEL_NAME
    if dry_run:
        user = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
        preview = user[:200].replace("\n", " ")
        return (
            f"[DRY-RUN stub from {model}] Acknowledged task. "
            f"Evidence-aware note on: {preview}… "
            "Kill-checks: deposit_terms=unresolved; vintage_primary_source=unresolved; "
            "upgrade_ebitda_bridge=unresolved. Stance: NEUTRAL pending primary source."
        )

    url = f"{OLLAMA_HOST.rstrip('/')}/api/chat"
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        },
    }

    last_err: Optional[Exception] = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            result = _post_json(url, payload, timeout=timeout)
            msg = result.get("message") or {}
            content = msg.get("content") or result.get("response") or ""
            return strip_thinking(str(content))
        except urllib.error.HTTPError as e:
            last_err = e
            body = e.read().decode("utf-8", errors="replace") if e.fp else ""
            log.warning("Ollama HTTP %s attempt %s: %s", e.code, attempt, body[:300])
        except Exception as e:
            last_err = e
            log.warning("Ollama error attempt %s: %s", attempt, e)
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_BACKOFF_S * (attempt + 1))

    raise RuntimeError(f"Ollama chat failed after retries: {last_err}")


def ping(timeout: int = 5) -> bool:
    """Return True if Ollama is reachable."""
    try:
        url = f"{OLLAMA_HOST.rstrip('/')}/api/tags"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status == 200
    except Exception:
        return False
