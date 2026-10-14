#!/usr/bin/env python3
"""Narrow, quote-locked local research jobs against gev.db.

Architecture: question lock → SQL/FTS retrieve → qwen extract (JSON) →
quote-must-match audit → durable JSON/MD notes. Not a competition submission.

Examples:
  python research_job.py --question deposit_terms
  python research_job.py --question upgrade_bridge --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]  # gev-corpus/
if Path(__file__).parent.name == "research":
    ROOT = Path(__file__).resolve().parents[1]
else:
    # if script lives in research/, parent is gev-corpus
    ROOT = Path(__file__).resolve().parent.parent if (Path(__file__).parent / "out").exists() or Path(__file__).parent.name == "research" else Path(__file__).resolve().parent

# Prefer layout: gev-corpus/research/research_job.py
SCRIPT_DIR = Path(__file__).resolve().parent
if SCRIPT_DIR.name == "research":
    CORPUS_ROOT = SCRIPT_DIR.parent
    OUT_DIR = SCRIPT_DIR / "out"
else:
    CORPUS_ROOT = SCRIPT_DIR
    OUT_DIR = SCRIPT_DIR / "research" / "out"

DB_PATH = CORPUS_ROOT / "data" / "gev.db"
MODEL = "qwen3:8b"
OLLAMA = "http://127.0.0.1:11434"
MAX_CHUNKS = 12
MAX_CHUNK_CHARS = 1800

DISCLOSURE = (
    "# RESEARCH NOTES — NOT A COMPETITION SUBMISSION\n\n"
    "**AI-research disclosure:** Local Ollama extraction (qwen3:8b) over private "
    "GEV corpus with quote-must-match verification. Initial research only; "
    "verify against primary filings before any memo use.\n\n---\n\n"
)

QUESTIONS: dict[str, dict[str, Any]] = {
    "deposit_terms": {
        "title": "SRA / deposit / refund terms (primary filings)",
        "forms": ("10-Q", "10-K", "8-K"),
        "like_any": (
            "%slot reservation%",
            "%down payment%",
            "%customer deposit%",
            "%refund%",
            "%non-refund%",
            "%nonrefund%",
            "%contract liabilities%",
            "%advances from customer%",
        ),
        "fts": 'slot OR reservation OR deposit OR "down payment" OR refundable OR refund',
        "extract_prompt": (
            "You extract ONLY facts about GE Vernova (GEV) customer deposits, "
            "down payments, slot reservation agreement (SRA) cash terms, "
            "refundability, forfeiture, and contract liabilities from the EVIDENCE. "
            "Do not discuss other companies. Do not invent numbers. "
            "If the evidence does not state refundability, say so explicitly.\n"
            "Return STRICT JSON (no markdown) with shape:\n"
            "{"
            '"claims":[{"claim":str,"quote":str,"supports":str,'
            '"confidence":0-100}],'
            '"unresolved":[str],'
            '"summary":str'
            "}\n"
            "Every quote MUST be a verbatim substring of the evidence. "
            "If you cannot quote, omit the claim."
        ),
    },
    "upgrade_bridge": {
        "title": "Existing-fleet upgrade scope → 2027 EBITDA bridge inputs",
        "forms": ("10-Q", "10-K", "8-K", "NEWS"),
        "like_any": (
            "%upgrade%",
            "%7F%",
            "%modernization%",
            "%Coryton%",
            "%Franklin%",
            "%Wansley%",
            "%transactional%",
        ),
        "fts": "upgrade OR modernization OR 7F OR Coryton OR transactional",
        "extract_prompt": (
            "Extract ONLY facts about GE Vernova gas fleet upgrades / modernization "
            "(scope, MW added, customer, timing, GEV revenue if stated). "
            "Never treat customer construction cost as GEV revenue unless the text says GEV was awarded that amount. "
            "Return STRICT JSON: "
            '{"claims":[{"claim":str,"quote":str,"supports":str,"confidence":0-100}],'
            '"projects":[{"name":str,"mw":str|null,"timing":str|null,"gev_scope":str|null}],'
            '"unresolved":[str],"summary":str}. '
            "Quotes must be verbatim substrings of evidence."
        ),
    },
}


def connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise SystemExit(f"DB missing: {DB_PATH}")
    uri = DB_PATH.resolve().as_posix()
    if not uri.startswith("/"):
        conn = sqlite3.connect(f"file:{uri}?mode=ro", uri=True)
    else:
        conn = sqlite3.connect(f"file:{uri}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def retrieve(question: str) -> list[dict[str, Any]]:
    q = QUESTIONS[question]
    con = connect()
    hits: list[dict[str, Any]] = []
    seen: set[int] = set()

    # Primary: LIKE on GEV filing chunks
    clauses = " OR ".join(["lower(text) LIKE ?"] * len(q["like_any"]))
    params: list[Any] = [p.lower() if False else p for p in q["like_any"]]
    # SQLite LIKE is case-insensitive for ASCII by default with NOCASE sometimes — use lower()
    params = [pat.lower().replace("%", "%") for pat in q["like_any"]]
    # rebuild with lower(text) LIKE lower patterns — patterns already have %
    sql = f"""
        SELECT id, accession, form, filing_date, section, substr(text,1,?) AS text
        FROM chunks
        WHERE ticker='GEV' AND form IN ({",".join("?" * len(q["forms"]))})
          AND ({" OR ".join(["lower(text) LIKE ?" for _ in q["like_any"]])})
        ORDER BY filing_date DESC, id DESC
        LIMIT ?
    """
    bind = [MAX_CHUNK_CHARS, *q["forms"], *[pat for pat in q["like_any"]], MAX_CHUNKS]
    # fix: LIKE patterns should stay as given; lower(text) LIKE '%slot%' works if pattern lowercased
    bind = [MAX_CHUNK_CHARS, *q["forms"], *[p.lower() for p in q["like_any"]], MAX_CHUNKS]
    try:
        rows = con.execute(sql, bind).fetchall()
    except sqlite3.Error as e:
        print("LIKE query failed:", e, file=sys.stderr)
        rows = []

    for r in rows:
        if r["id"] in seen:
            continue
        seen.add(r["id"])
        hits.append(
            {
                "id": r["id"],
                "accession": r["accession"],
                "form": r["form"],
                "filing_date": r["filing_date"],
                "section": (r["section"] or "")[:120],
                "text": r["text"] or "",
                "source": "chunks_like",
            }
        )

    # Supplement: backlog_quarterly contract liabilities / reservations
    try:
        brows = con.execute(
            """
            SELECT id, as_of, metric, value, unit, substr(quote,1,500) AS quote, filing_date, form
            FROM backlog_quarterly
            WHERE ticker='GEV' AND (
              lower(metric) LIKE '%reserv%' OR lower(metric) LIKE '%deposit%'
              OR lower(metric) LIKE '%contract_liab%' OR lower(metric) LIKE '%slot%'
              OR lower(quote) LIKE '%down payment%' OR lower(quote) LIKE '%slot reservation%'
            )
            ORDER BY id DESC LIMIT 15
            """
        ).fetchall()
        for r in brows:
            hits.append(
                {
                    "id": f"bq-{r['id']}",
                    "accession": "",
                    "form": r["form"] or "backlog_quarterly",
                    "filing_date": r["filing_date"] or r["as_of"],
                    "section": r["metric"],
                    "text": f"{r['as_of']} | {r['metric']}={r['value']} {r['unit'] or ''}\n{r['quote'] or ''}",
                    "source": "backlog_quarterly",
                }
            )
    except sqlite3.Error as e:
        print("backlog hook failed:", e, file=sys.stderr)

    # Risk factor explicit SRA language
    try:
        rrows = con.execute(
            """
            SELECT id, accession, form, filing_date, section, substr(text,1,?) AS text
            FROM chunks
            WHERE ticker='GEV' AND form IN ('10-K','10-Q')
              AND lower(text) LIKE '%slot reservation%'
              AND (lower(text) LIKE '%deposit%' OR lower(text) LIKE '%cancel%'
                   OR lower(text) LIKE '%may not%' OR lower(text) LIKE '%refund%')
            ORDER BY filing_date DESC LIMIT 8
            """,
            (MAX_CHUNK_CHARS,),
        ).fetchall()
        for r in rrows:
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            hits.append(
                {
                    "id": r["id"],
                    "accession": r["accession"],
                    "form": r["form"],
                    "filing_date": r["filing_date"],
                    "section": (r["section"] or "")[:120],
                    "text": r["text"] or "",
                    "source": "risk_sra",
                }
            )
    except sqlite3.Error:
        pass

    # Projects table for upgrade / modernization jobs
    if question == "upgrade_bridge":
        try:
            prows = con.execute(
                """
                SELECT id, source_date, owner, project_name, location, oem, model,
                       turbine_count, capacity_mw, commitment_status,
                       equipment_delivery_date, commercial_operation_date,
                       substr(quote,1,700) AS quote
                FROM projects
                WHERE lower(coalesce(project_name,'')) LIKE '%upgrade%'
                   OR lower(coalesce(quote,'')) LIKE '%upgrade%'
                   OR lower(coalesce(project_name,'')) LIKE '%modern%'
                   OR lower(coalesce(quote,'')) LIKE '%7f%'
                   OR lower(coalesce(project_name,'')) LIKE '%coryton%'
                   OR lower(coalesce(project_name,'')) LIKE '%franklin%'
                   OR lower(coalesce(project_name,'')) LIKE '%wansley%'
                   OR lower(coalesce(owner,'')) LIKE '%southern%'
                   OR lower(coalesce(quote,'')) LIKE '%gt26%'
                ORDER BY source_date DESC LIMIT 30
                """
            ).fetchall()
            for r in prows:
                text = (
                    f"owner={r['owner']} project={r['project_name']} loc={r['location']} "
                    f"oem={r['oem']} model={r['model']} turbines={r['turbine_count']} "
                    f"MW={r['capacity_mw']} status={r['commitment_status']} "
                    f"delivery={r['equipment_delivery_date']} COD={r['commercial_operation_date']}\n"
                    f"{r['quote'] or ''}"
                )
                hits.insert(
                    0,
                    {
                        "id": f"proj-{r['id']}",
                        "accession": "",
                        "form": "projects",
                        "filing_date": r["source_date"],
                        "section": r["project_name"],
                        "text": text,
                        "source": "projects",
                    },
                )
        except sqlite3.Error as e:
            print("projects hook failed:", e, file=sys.stderr)

        # Prefer Power services / transactional language from transcripts
        try:
            trows = con.execute(
                """
                SELECT id, event_date, topic, substr(statement,1,?) AS text
                FROM transcript_statements
                WHERE ticker='GEV' AND (
                  lower(statement) LIKE '%upgrade%'
                  OR lower(statement) LIKE '%transactional%'
                  OR lower(statement) LIKE '%modern%'
                  OR lower(statement) LIKE '%outage%'
                )
                ORDER BY event_date DESC LIMIT 10
                """,
                (MAX_CHUNK_CHARS,),
            ).fetchall()
            for r in trows:
                hits.insert(
                    0,
                    {
                        "id": f"tr-{r['id']}",
                        "accession": "",
                        "form": "transcript",
                        "filing_date": r["event_date"],
                        "section": r["topic"],
                        "text": r["text"] or "",
                        "source": "transcript",
                    },
                )
        except sqlite3.Error:
            pass

    con.close()
    # For upgrade_bridge, keep project/transcript hits first, cap noise
    if question == "upgrade_bridge":
        primary = [h for h in hits if h.get("source") in ("projects", "transcript")]
        other = [h for h in hits if h.get("source") not in ("projects", "transcript")]
        hits = (primary + other)[:40]
        return hits
    return hits[: MAX_CHUNKS + 15]


def format_evidence(hits: list[dict[str, Any]]) -> str:
    blocks = []
    for i, h in enumerate(hits, 1):
        blocks.append(
            f"[{i}] form={h.get('form')} date={h.get('filing_date')} "
            f"section={h.get('section')} accession={h.get('accession')} id={h.get('id')}\n"
            f"{h.get('text', '')}"
        )
    return "\n\n".join(blocks)


def strip_think(text: str) -> str:
    text = re.sub(r"<think>[\s\S]*?</think>", "", text or "", flags=re.I)
    text = re.sub(r"<thinking>[\s\S]*?</thinking>", "", text, flags=re.I)
    return text.strip()


def ollama_chat(system: str, user: str, *, dry_run: bool = False) -> str:
    if dry_run:
        return json.dumps(
            {
                "claims": [],
                "unresolved": ["dry_run"],
                "summary": "dry_run",
            }
        )
    payload = {
        "model": MODEL,
        "stream": False,
        "options": {"temperature": 0.1, "num_ctx": 8192},
        "messages": [
            {"role": "system", "content": system + "\n/no_think"},
            {"role": "user", "content": user},
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA}/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return strip_think(body.get("message", {}).get("content") or body.get("response") or "")


def parse_json_loose(text: str) -> dict[str, Any]:
    text = strip_think(text)
    text = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", text)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {"claims": [], "unresolved": ["json_parse_failed"], "summary": text[:500], "raw": text}


def normalize(s: str) -> str:
    s = (s or "").replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def quote_in_evidence(quote: str, evidence: str) -> bool:
    if not quote or len(quote) < 12:
        return False
    return normalize(quote) in normalize(evidence)


def audit(extracted: dict[str, Any], evidence: str) -> dict[str, Any]:
    kept = []
    rejected = []
    for c in extracted.get("claims") or []:
        if not isinstance(c, dict):
            continue
        q = c.get("quote") or ""
        if quote_in_evidence(q, evidence):
            c["verified"] = True
            kept.append(c)
        else:
            c["verified"] = False
            c["reject_reason"] = "quote_not_in_evidence"
            rejected.append(c)
    out = dict(extracted)
    out["claims_verified"] = kept
    out["claims_rejected"] = rejected
    out["audit"] = {
        "n_claims_in": len(extracted.get("claims") or []),
        "n_verified": len(kept),
        "n_rejected": len(rejected),
    }
    return out


def deterministic_deposit_flags(hits: list[dict[str, Any]]) -> dict[str, Any]:
    """Rule-based scan — no LLM — for refund/deposit language."""
    blob = "\n".join(h.get("text") or "" for h in hits).lower()
    flags = {
        "mentions_slot_reservation": "slot reservation" in blob,
        "mentions_down_payment": "down payment" in blob or "down payments" in blob,
        "mentions_deposit": "deposit" in blob,
        "mentions_refund": "refund" in blob,
        "mentions_nonrefundable": ("non-refund" in blob) or ("nonrefund" in blob) or ("non refundable" in blob),
        "mentions_may_not_place_orders": "may not place orders" in blob or "may fail to materialize" in blob or "may not result in orders" in blob,
    }
    return flags


def run(question: str, *, dry_run: bool = False) -> Path:
    if question not in QUESTIONS:
        raise SystemExit(f"Unknown question {question}; choose from {list(QUESTIONS)}")
    spec = QUESTIONS[question]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    hits = retrieve(question)
    evidence = format_evidence(hits)
    flags = deterministic_deposit_flags(hits) if question == "deposit_terms" else {}

    system = spec["extract_prompt"]
    user = f"QUESTION: {spec['title']}\n\nEVIDENCE:\n{evidence}\n\nReturn JSON now."
    t0 = time.time()
    raw = ollama_chat(system, user, dry_run=dry_run)
    elapsed = round(time.time() - t0, 2)
    parsed = parse_json_loose(raw)
    audited = audit(parsed, evidence)

    report = {
        "disclaimer": "AI initial research notes only — not a competition submission",
        "question": question,
        "title": spec["title"],
        "model": MODEL,
        "db": str(DB_PATH),
        "ts": datetime.now(timezone.utc).isoformat(),
        "elapsed_s": elapsed,
        "n_evidence_hits": len(hits),
        "deterministic_flags": flags,
        "extraction": audited,
        "evidence_index": [
            {
                "i": i + 1,
                "id": h.get("id"),
                "form": h.get("form"),
                "filing_date": h.get("filing_date"),
                "section": h.get("section"),
                "accession": h.get("accession"),
                "source": h.get("source"),
                "chars": len(h.get("text") or ""),
            }
            for i, h in enumerate(hits)
        ],
    }

    # Human verdict stub from flags for deposit_terms
    if question == "deposit_terms":
        if flags.get("mentions_nonrefundable"):
            verdict = "Filings mention non-refundable language — verify quote in claims_verified."
        elif flags.get("mentions_down_payment") and flags.get("mentions_slot_reservation"):
            verdict = (
                "PRIMARY: down payments on orders AND slot reservations drive contract liabilities / FCF. "
                "NON-REFUNDABLE terms NOT found in this retrieval. "
                "Risk factor: SRAs may not convert to orders."
            )
        else:
            verdict = "Insufficient primary language in retrieval."
        report["working_verdict"] = verdict

    json_path = OUT_DIR / f"{question}.json"
    md_path = OUT_DIR / f"{question}.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    md = [DISCLOSURE, f"# {spec['title']}\n"]
    md.append(f"- Model: `{MODEL}`")
    md.append(f"- Evidence hits: **{len(hits)}**")
    md.append(f"- Verified claims: **{audited.get('audit', {}).get('n_verified', 0)}** "
              f"(rejected {audited.get('audit', {}).get('n_rejected', 0)})")
    md.append(f"- Elapsed: {elapsed}s\n")
    if report.get("working_verdict"):
        md.append(f"## Working verdict\n\n{report['working_verdict']}\n")
    if flags:
        md.append("## Deterministic flags\n")
        for k, v in flags.items():
            md.append(f"- `{k}`: **{v}**")
        md.append("")
    md.append("## Verified claims\n")
    for c in audited.get("claims_verified") or []:
        md.append(f"- **{c.get('claim')}**")
        md.append(f"  - quote: “{(c.get('quote') or '')[:300]}”")
        md.append(f"  - confidence: {c.get('confidence')}")
    if not audited.get("claims_verified"):
        md.append("_None passed quote-must-match._\n")
    md.append("\n## Unresolved\n")
    for u in audited.get("unresolved") or []:
        md.append(f"- {u}")
    md.append("\n## Rejected claims (failed quote check)\n")
    for c in audited.get("claims_rejected") or []:
        md.append(f"- {c.get('claim')} —_{c.get('reject_reason')}_")
    md.append("\n## Evidence index\n")
    for e in report["evidence_index"]:
        md.append(
            f"- [{e['i']}] {e['form']} {e['filing_date']} | {e['section']} | {e['source']} | id={e['id']}"
        )
    md.append(f"\n## Summary (model)\n\n{audited.get('summary') or ''}\n")
    md_path.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return md_path


def main() -> int:
    global MODEL
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", required=True, choices=list(QUESTIONS))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=MODEL)
    args = ap.parse_args()
    MODEL = args.model
    run(args.question, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
