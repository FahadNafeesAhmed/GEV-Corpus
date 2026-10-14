"""Run local-LLM structured extraction over corpus chunks via Ollama.

    python extract.py --extractor guidance --ticker GEV --limit 50
    python extract.py --extractor guidance risk --ticker GEV --workers 3
    python extract.py --status

Design notes:
  * Schema-constrained decoding (Ollama `format`) rather than "reply in JSON" —
    the model cannot emit invalid JSON, so there is no parse-retry loop.
  * A cheap keyword prefilter runs before the model. Most chunks in a 10-K carry
    no guidance at all; paying 2.6s of GPU to learn that is the whole cost problem.
  * Resume is per (chunk, extractor), so a run that dies at hour 3 resumes at hour 3.
  * The model is never asked for a number it has to compute - only to locate and
    quote what the filing already states. Authoritative figures come from XBRL.
"""
from __future__ import annotations

import argparse
import json
import queue
import re
import threading
import time
import urllib.request

from common import connect, load_config, log

OLLAMA = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:8b"

# --------------------------------------------------------------- extractors

GUIDANCE_SCHEMA = {
    "type": "object",
    "properties": {
        "has_guidance": {"type": "boolean"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "metric": {"type": "string"},
                    "value": {"type": "string"},
                    "period": {"type": "string"},
                    "direction": {"type": "string",
                                  "enum": ["raise", "lower", "maintain", "initiate", "unclear"]},
                    "quote": {"type": "string"},
                },
                "required": ["metric", "value", "period", "direction", "quote"],
            },
        },
    },
    "required": ["has_guidance", "items"],
}

RISK_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "category": {"type": "string", "enum": [
                        "demand", "supply-chain", "pricing", "competition", "regulation",
                        "litigation", "technology", "execution", "financial", "macro",
                        "climate", "cyber", "labor", "other"]},
                    "summary": {"type": "string"},
                    "severity": {"type": "string", "enum": ["high", "medium", "low"]},
                    "quote": {"type": "string"},
                },
                "required": ["category", "summary", "severity", "quote"],
            },
        },
    },
    "required": ["items"],
}

CLAIMS_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "maxItems": 12,
            "items": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "enum": [
                        "backlog", "gas-turbine-supply", "pricing", "data-center-demand",
                        "wind", "electrification", "nuclear", "hydrogen", "competition",
                        "tariffs", "valuation", "management", "policy", "technology",
                        "financials", "other"]},
                    "claim": {"type": "string"},
                    "stance": {"type": "string", "enum": ["bullish", "bearish", "neutral"]},
                    "has_number": {"type": "boolean"},
                    "quote": {"type": "string"},
                },
                "required": ["topic", "claim", "stance", "has_number", "quote"],
            },
        },
    },
    "required": ["items"],
}

WEB_FORMS = ("ARXIV", "OPENALEX", "WEB", "NEWS", "YOUTUBE", "RSS", "IR")
PRIMARY_IR_FORMS = ("TRANSCRIPT", "DECK", "OPERATOR", "COMPETITOR")
CUSTOMER_FORMS = ("10-K", "10-Q", "8-K", "8-K/EX", "10-K/EX", "10-Q/EX", "CUSTOMER")

# --- quarterly backlog / deposits / cash timing ------------------------------
BACKLOG_SCHEMA = {
    "type": "object",
    "properties": {
        "as_of": {"type": "string"},
        "items": {"type": "array", "maxItems": 15, "items": {"type": "object", "properties": {
            "metric": {"type": "string", "enum": [
                "equipment_backlog", "services_backlog", "total_backlog", "rpo_total",
                "rpo_equipment", "rpo_services", "rpo_recognition_schedule",
                "reservation_gw", "slot_reservations", "firm_orders", "orders_value",
                "shipments_units", "customer_advances", "contract_liabilities",
                "deferred_revenue", "working_capital", "capex", "free_cash_flow",
                "other"]},
            "value": {"type": "string"},
            "unit": {"type": "string"},
            "period": {"type": "string"},
            "status": {"type": "string", "enum": ["reservation", "firm_order", "backlog",
                                                  "recognized", "cash", "unclear"]},
            "quote": {"type": "string"}},
            "required": ["metric", "value", "unit", "period", "status", "quote"]}}},
    "required": ["as_of", "items"],
}

# --- management language in transcripts, quarter by quarter -----------------
TRANSCRIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {"type": "object", "properties": {
            "topic": {"type": "string", "enum": [
                "pricing", "delivery_timing", "reservations", "deposits", "capacity",
                "margins", "backlog", "demand", "supply_chain", "wind", "guidance",
                "capital_allocation", "other"]},
            "speaker_role": {"type": "string", "enum": ["management", "analyst", "unclear"]},
            "statement": {"type": "string"},
            "is_analyst_followup": {"type": "boolean"},
            "qualification": {"type": "string"},
            "quote": {"type": "string"}},
            "required": ["topic", "speaker_role", "statement", "is_analyst_followup",
                         "qualification", "quote"]}}},
    "required": ["items"],
}

# --- customer-side project facts -------------------------------------------
PROJECT_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {"type": "object", "properties": {
            "owner": {"type": "string"},
            "project_name": {"type": "string"},
            "location": {"type": "string"},
            "oem": {"type": "string"},
            "model": {"type": "string"},
            "turbine_count": {"type": "string"},
            "capacity_mw": {"type": "string"},
            "commitment_status": {"type": "string", "enum": [
                "announced", "reservation", "order", "contract", "under_construction",
                "operating", "delayed", "cancelled", "disputed", "unclear"]},
            "financing_permits": {"type": "string"},
            "equipment_delivery_date": {"type": "string"},
            "commercial_operation_date": {"type": "string"},
            "date_revision": {"type": "string"},
            "cancellation_or_dispute": {"type": "string"},
            "quote": {"type": "string"}},
            "required": ["owner", "project_name", "location", "oem", "model", "turbine_count",
                         "capacity_mw", "commitment_status", "financing_permits",
                         "equipment_delivery_date", "commercial_operation_date",
                         "date_revision", "cancellation_or_dispute", "quote"]}}},
    "required": ["items"],
}

# --- dated, attributed analyst estimates (never called consensus) -----------
ANALYST_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {"type": "object", "properties": {
            "analyst": {"type": "string"},
            "firm": {"type": "string"},
            "metric": {"type": "string", "enum": [
                "price_target", "rating", "revenue", "ebitda", "eps", "margin",
                "backlog", "orders", "free_cash_flow", "other"]},
            "value": {"type": "string"},
            "period": {"type": "string"},
            "stated_on": {"type": "string"},
            "quote": {"type": "string"}},
            "required": ["analyst", "firm", "metric", "value", "period", "stated_on", "quote"]}}},
    "required": ["items"],
}

# --- grid-operator forecast figures, with the vintage that stated them --------
OPERATOR_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {"type": "object", "properties": {
            "operator": {"type": "string"},
            "report": {"type": "string"},
            "vintage": {"type": "string"},
            "region": {"type": "string"},
            "target_year": {"type": "string"},
            "metric": {"type": "string", "enum": [
                "summer_peak_load", "winter_peak_load", "annual_energy", "data_center_load",
                "large_load_additions", "load_growth_rate", "reserve_margin", "installed_capacity",
                "planned_capacity", "queue_capacity", "other"]},
            "value": {"type": "string"},
            "unit": {"type": "string"},
            "quote": {"type": "string"}},
            "required": ["operator", "report", "vintage", "region", "target_year", "metric",
                         "value", "unit", "quote"]}}},
    "required": ["items"],
}

# --- competitor segment figures from their own reports ---------------------
COMPETITOR_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "maxItems": 15, "items": {"type": "object", "properties": {
            "company": {"type": "string"},
            "segment": {"type": "string"},
            "metric": {"type": "string", "enum": [
                "orders", "revenue", "backlog", "profit", "margin", "capacity_expansion",
                "lead_time", "pricing", "headcount", "capex", "other"]},
            "value": {"type": "string"},
            "unit": {"type": "string"},
            "period": {"type": "string"},
            "quote": {"type": "string"}},
            "required": ["company", "segment", "metric", "value", "unit", "period", "quote"]}}},
    "required": ["items"],
}

EXTRACTORS = {
    "backlog": {
        "schema": BACKLOG_SCHEMA,
        "forms": ("10-K", "10-Q", "8-K", "8-K/EX", "10-K/EX", "10-Q/EX", "TRANSCRIPT", "DECK"),
        # Financial-table chunks yield 20-30 figures; at 2000 tokens ~7% still
        # truncated on run 2. Cap items and give more room.
        "num_predict": 3000,
        "prefilter": re.compile(
            r"\b(backlog|remaining performance obligation|RPO|reservation|slot|firm order|"
            r"customer advance|contract liabilit|deferred revenue|deposit|shipments?|"
            r"working capital|capital expenditure|free cash flow)\b", re.I),
        "prompt": (
            "You are reading an excerpt from a company's financial disclosure.\n"
            "Extract every backlog, order, reservation, deposit, contract-liability, working-capital, "
            "capex or free-cash-flow figure it STATES, with the period and the stage of commitment.\n"
            "Rules:\n"
            "- Copy each figure exactly as written, with its unit (e.g. '$ million', 'GW', 'units').\n"
            "- `status` is the stage: reservation < firm_order < backlog < recognized < cash. "
            "A reservation that later becomes an order must not be counted twice - tag each as stated.\n"
            "- `as_of` is the balance-sheet or period-end date the excerpt refers to, if stated.\n"
            "- `quote` must be verbatim. Never compute or infer a number.\n"
            "- Report at most 15 items: the most material figures first (totals before line items).\n"
            "- If nothing here is a backlog/deposit/cash-timing figure, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "transcript": {
        "schema": TRANSCRIPT_SCHEMA,
        "forms": ("TRANSCRIPT",),
        "num_predict": 2000,
        "prefilter": re.compile(
            r"\b(pric|deliver|slot|reserv|deposit|capacity|margin|backlog|lead time|"
            r"guidance|outlook|Haliade|offshore|Vineyard)\b", re.I),
        "prompt": (
            "You are reading an excerpt from an earnings-call or investor-event transcript.\n"
            "Extract each DISTINCT statement about pricing, delivery timing, reservations, deposits, "
            "capacity, margins, backlog, demand, supply chain, wind, or guidance.\n"
            "Rules:\n"
            "- `speaker_role`: management or analyst.\n"
            "- `is_analyst_followup` is true when an analyst pushes back or asks for clarification.\n"
            "- `qualification`: any hedge, caveat or condition attached to the statement "
            "('assuming', 'depending on', 'if', 'excluding'). Empty string if none.\n"
            "- `quote` must be verbatim from the excerpt.\n"
            "- If the excerpt is boilerplate or operator instructions, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "project": {
        "schema": PROJECT_SCHEMA,
        "forms": CUSTOMER_FORMS + PRIMARY_IR_FORMS + WEB_FORMS,
        "num_predict": 2000,
        # Run 2: "gas turbine" alone admitted 7,773 chunks at 0.2 projects each.
        # Require a turbine/OEM term AND a project cue (size, site, or schedule).
        "prefilter": re.compile(
            r"(?=.*\b(GE Vernova|Vernova|7HA|9HA|7F|9F|LM6000|LM2500|HA\.0[12]|combined[- ]cycle|"
            r"combustion turbine|gas turbine|simple[- ]cycle|peaker|CCGT)\b)"
            r"(?=.*\b(\d[\d,.]*\s?(MW|GW|megawatt|gigawatt)|plant|facility|station|project|"
            r"commercial operation|COD|in[- ]service|construction|permit|approved|"
            r"certificate of|IRP|resource plan|delivery)\b)", re.I | re.S),
        "prompt": (
            "You are reading an excerpt from a utility, developer, regulator or news document.\n"
            "Extract every SPECIFIC power-plant project it describes that involves gas turbines, "
            "one item per project. Leave a field as an empty string if the excerpt does not state it.\n"
            "Rules:\n"
            "- `oem` only if the excerpt names the turbine manufacturer. Do not assume GE Vernova.\n"
            "- `commitment_status` reflects what the excerpt says: announced < reservation < order < "
            "contract < under_construction < operating; or delayed / cancelled / disputed.\n"
            "- Record dates exactly as stated; put any change to a prior date in `date_revision`.\n"
            "- `quote` must be verbatim. A plant delay is not evidence of an equipment cancellation - "
            "report only what is written.\n"
            "- If no specific project is described, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "analyst": {
        "schema": ANALYST_SCHEMA,
        "forms": ("NEWS", "WEB", "RSS", "YOUTUBE"),
        "num_predict": 1500,
        "prefilter": re.compile(
            r"\b(price target|analyst|rating|upgrade|downgrade|overweight|underweight|"
            r"outperform|buy rating|sell rating|estimate|EPS|Goldman|Morgan Stanley|JPMorgan|"
            r"Jefferies|Barclays|UBS|Citi|Bernstein|Wolfe|Evercore|RBC|Mizuho|BofA)\b", re.I),
        "prompt": (
            "You are reading an excerpt from financial news or commentary.\n"
            "Extract each individual, ATTRIBUTED analyst estimate, rating or price target about "
            "GE Vernova (GEV): who said it, which firm, the figure, the period, and the date stated.\n"
            "Rules:\n"
            "- Only attributed estimates. 'Analysts expect' with no name or firm is NOT extractable.\n"
            "- Never describe anything as consensus. Each row is one analyst's view.\n"
            "- `quote` verbatim. Copy figures exactly.\n"
            "- If there is no attributed estimate, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "operator": {
        "schema": OPERATOR_SCHEMA,
        "forms": ("OPERATOR",),
        "num_predict": 2000,
        "prefilter": re.compile(
            r"\b(peak (?:load|demand)|load forecast|data cent|large load|GW|MW|reserve margin|"
            r"load growth|energy forecast|summer peak|winter peak)\b", re.I),
        "prompt": (
            "You are reading an excerpt from a grid operator's or reliability body's report "
            "(PJM, ERCOT, NERC, MISO, SPP, CAISO).\n"
            "Extract each forecast or capacity FIGURE it states: the operator, the report, the "
            "forecast vintage (the year the report was issued), the region/zone, the target year the "
            "figure applies to, the metric, the value and unit.\n"
            "Rules:\n"
            "- Copy figures exactly. Never convert MW to GW or vice versa.\n"
            "- `vintage` is when the forecast was MADE; `target_year` is the year it is ABOUT. "
            "Keeping these separate is the whole point.\n"
            "- `quote` verbatim.\n"
            "- If the excerpt is methodology text with no figure, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "competitor": {
        "schema": COMPETITOR_SCHEMA,
        "forms": ("COMPETITOR",),
        # Run 2: 81% of competitor chunks passed the old prefilter ("orders",
        # "capacity", "margin" match every page of a financial report) and 36% of
        # outputs truncated. Now: a segment/company term AND a currency-or-unit
        # figure must both be present, and output is capped.
        "num_predict": 3000,
        "prefilter": re.compile(
            r"(?=.*\b(Gas Services|Grid Technologies|Energy Systems|GTCC|Power Systems|"
            r"Power Grids|Service|order intake|order backlog|Siemens Energy|Mitsubishi Power|"
            r"Vestas|Hitachi Energy)\b)"
            r"(?=.*(€|\$|¥|EUR|USD|JPY|DKK|billion|million|bn|GW|MW|%))", re.I | re.S),
        "prompt": (
            "You are reading an excerpt from a competitor's financial report or presentation "
            "(Siemens Energy, Mitsubishi Heavy Industries / Mitsubishi Power, Hitachi Energy, Vestas).\n"
            "Extract each segment-level figure it STATES: orders, revenue, backlog, profit, margin, "
            "capacity expansion, lead times, pricing.\n"
            "Rules:\n"
            "- Name the company and the segment exactly as the document does.\n"
            "- Copy figures exactly with unit and currency. Never convert.\n"
            "- `quote` verbatim.\n"
            "- Report at most 15 items: segment totals first, then the most material line items.\n"
            "- If nothing is a segment figure, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    # For papers, articles and transcripts: pull out checkable claims about GE
    # Vernova or its markets. These are the raw material for the mismatch engine -
    # each claim gets compared against what the filings actually say.
    "claims": {
        "schema": CLAIMS_SCHEMA,
        "forms": WEB_FORMS,
        "num_predict": 3000,
        "prefilter": re.compile(
            r"\b(GE Vernova|GEV|Vernova|gas turbine|backlog|data cent|hyperscaler|"
            r"Haliade|offshore wind|HVDC|transformer|BWRX|Siemens Energy|Mitsubishi)\b", re.I),
        "prompt": (
            "You are reading an excerpt from a paper, article, or transcript.\n"
            "Extract each DISTINCT, CHECKABLE claim it makes about GE Vernova, its products "
            "(gas turbines, wind, grid equipment, nuclear), its competitors, or its end markets "
            "(data-center power demand, grid buildout, natural gas).\n"
            "Rules:\n"
            "- A claim is a statement that could be true or false. Opinions phrased as facts count. "
            "Pure sentiment ('great company') does not.\n"
            "- `quote` must be verbatim from the excerpt.\n"
            "- `stance` is the source's stance toward GEV's prospects, as conveyed by this claim.\n"
            "- `has_number` is true if the claim contains a specific figure, date, or quantity.\n"
            "- If there is nothing checkable about GEV or its markets, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "guidance": {
        "schema": GUIDANCE_SCHEMA,
        # The /EX forms are the exhibits - for an 8-K that is the earnings release
        # carrying segment results and guidance. Omitting them was silently
        # excluding the single richest source of forward-looking statements.
        "forms": ("10-K", "10-Q", "8-K", "ARS", "8-K/EX", "10-K/EX", "10-Q/EX", "6-K/EX",
                  "TRANSCRIPT", "DECK"),
        "num_predict": 2000,
        # Forward-looking cues. Cheap to run, and it is what keeps the job overnight-sized.
        "prefilter": re.compile(
            r"\b(guidance|outlook|we expect|we anticipate|we project|full[- ]year|"
            r"fiscal 20\d\d|targeting|on track to|we forecast|expects? to (?:be|deliver|generate|grow)|"
            r"free cash flow of|revenue of approximately|margin of approximately)\b", re.I),
        "prompt": (
            "You are reading an excerpt from an SEC filing.\n"
            "Extract ONLY explicit forward-looking guidance the company itself states: a metric, "
            "the value or range given, and the period it applies to.\n"
            "Rules:\n"
            "- Copy figures exactly as written. Never compute, convert or infer a number.\n"
            "- `quote` must be a verbatim span from the excerpt.\n"
            "- Historical results are NOT guidance. Boilerplate warnings are NOT guidance.\n"
            "- If there is no explicit guidance, return has_guidance=false with an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
    "risk": {
        "schema": RISK_SCHEMA,
        "forms": ("10-K", "10-Q"),
        "sections": ("1A",),
        "prefilter": None,
        "prompt": (
            "You are reading a risk-factor excerpt from an SEC filing.\n"
            "Identify each DISTINCT risk described. For each: categorize it, summarize it in one "
            "sentence, rate the severity the filing itself conveys, and quote the key span verbatim.\n"
            "Rules:\n"
            "- Only risks actually described here. Do not add risks you know from elsewhere.\n"
            "- `quote` must be verbatim from the excerpt.\n"
            "- Severity reflects the filing's own emphasis, not your market opinion.\n"
            "- If the excerpt is a heading or table of contents with no substance, return an empty list.\n\n"
            "EXCERPT:\n{chunk}"),
    },
}


# --------------------------------------------------------------- ollama

def ollama(prompt: str, schema: dict, model: str, timeout: int = 240,
           num_predict: int = 900) -> tuple[dict | None, int]:
    # Constrained decoding guarantees valid JSON only if generation finishes.
    # Dense chunks with many items were hitting a 900-token cap mid-output, so the
    # cap is now per extractor (see EXTRACTORS[...]["num_predict"]).
    body = json.dumps({
        "model": model, "prompt": prompt, "stream": False, "think": False,
        "format": schema, "keep_alive": "30m",
        "options": {"temperature": 0, "num_predict": num_predict},
    }).encode()
    t0 = time.time()
    try:
        req = urllib.request.Request(OLLAMA, data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            doc = json.loads(r.read())
        ms = int((time.time() - t0) * 1000)
        return json.loads(doc.get("response") or "{}"), ms
    except Exception as exc:
        log(f"    ollama error: {type(exc).__name__}: {str(exc)[:110]}")
        return None, int((time.time() - t0) * 1000)


def pick_chunks(con, name: str, spec: dict, ticker: str, limit: int | None):
    """Select candidate chunks: right form, right section, passing the prefilter,
    and not already extracted."""
    # A failed extraction (ok=0) still has a row, so `e.id IS NULL` alone would
    # exclude it from every future run. Include failures so they are retried.
    sql = ["""SELECT c.id, c.text, c.accession, c.form, c.filing_date, c.section, c.ticker
              FROM chunks c
              LEFT JOIN extractions e ON e.chunk_id = c.id AND e.extractor = ?
              WHERE (e.id IS NULL OR e.ok = 0)"""]
    params: list = [name]
    if ticker and ticker != "ALL":
        sql.append("AND c.ticker = ?"); params.append(ticker)
    if spec.get("forms"):
        sql.append(f"AND c.form IN ({','.join('?' * len(spec['forms']))})")
        params += list(spec["forms"])
    if spec.get("sections"):
        sql.append("AND (" + " OR ".join("c.section LIKE ?" for _ in spec["sections"]) + ")")
        params += [f"Item {s}%" for s in spec["sections"]]
    sql.append("ORDER BY c.filing_date DESC, c.id")
    rows = con.execute(" ".join(sql), params).fetchall()

    pf = spec.get("prefilter")
    if pf is not None:
        kept = [r for r in rows if pf.search(r[1])]
        log(f"  prefilter: {len(kept)}/{len(rows)} chunks carry candidate language "
            f"({100*len(kept)/max(len(rows),1):.0f}%)")
        rows = kept
    return rows[:limit] if limit else rows


# --------------------------------------------------------------- flattening

def flatten(con, name: str, chunk_meta: tuple, payload: dict) -> int:
    cid, acc, form, fdate, ticker = chunk_meta
    n = 0
    if name == "guidance":
        for it in (payload.get("items") or []):
            q = (it.get("quote") or "")
            ql = q.lower()
            # Cheap forward-vs-historical flag for the validation pass. The model
            # over-triggers on "expect"; this marks the rows a human should check.
            fwd_cues = ("expect", "outlook", "guidance", "target", "anticipate",
                        "will be", "on track", "forecast", "project")
            hist_cues = ("were $", "was $", "reclassified", "recognized during",
                         "for the three months ended", "for the year ended")
            is_forward = int(any(c in ql for c in fwd_cues) and not any(c in ql for c in hist_cues))
            con.execute(
                """INSERT INTO guidance (ticker, chunk_id, accession, form, filing_date,
                                         metric, value, period, direction, quote, is_forward)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, form, fdate, it.get("metric"), it.get("value"),
                 it.get("period"), it.get("direction"), q[:1200], is_forward))
            n += 1
    elif name == "backlog":
        as_of = payload.get("as_of") or ""
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO backlog_quarterly (ticker, chunk_id, accession, form, filing_date,
                                                  as_of, metric, value, unit, period, status, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, form, fdate, as_of, it.get("metric"), it.get("value"),
                 it.get("unit"), it.get("period"), it.get("status"),
                 (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "transcript":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO transcript_statements (ticker, chunk_id, accession, event_date,
                        topic, speaker_role, statement, is_analyst_followup, qualification, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, fdate, it.get("topic"), it.get("speaker_role"),
                 it.get("statement"), int(bool(it.get("is_analyst_followup"))),
                 it.get("qualification"), (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "project":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO projects (chunk_id, accession, source_kind, source_date, owner,
                        project_name, location, oem, model, turbine_count, capacity_mw,
                        commitment_status, financing_permits, equipment_delivery_date,
                        commercial_operation_date, date_revision, cancellation_or_dispute, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (cid, acc, form, fdate, it.get("owner"), it.get("project_name"),
                 it.get("location"), it.get("oem"), it.get("model"), it.get("turbine_count"),
                 it.get("capacity_mw"), it.get("commitment_status"), it.get("financing_permits"),
                 it.get("equipment_delivery_date"), it.get("commercial_operation_date"),
                 it.get("date_revision"), it.get("cancellation_or_dispute"),
                 (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "analyst":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO analyst_calls (ticker, chunk_id, accession, published, analyst,
                                              firm, metric, value, period, stated_on, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, fdate, it.get("analyst"), it.get("firm"), it.get("metric"),
                 it.get("value"), it.get("period"), it.get("stated_on"),
                 (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "operator":
        for it in (payload.get("items") or []):
            ty = "".join(ch for ch in str(it.get("target_year") or "") if ch.isdigit())[:4]
            con.execute(
                """INSERT INTO operator_forecasts (chunk_id, accession, operator, report, vintage,
                        region, target_year, metric, value, unit, source_url, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                (cid, acc, it.get("operator"), it.get("report"), it.get("vintage"), it.get("region"),
                 int(ty) if ty else None, it.get("metric"), it.get("value"), it.get("unit"), "",
                 (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "competitor":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO competitor_financials (chunk_id, accession, source_date, company,
                                                      segment, metric, value, unit, period, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (cid, acc, fdate, it.get("company"), it.get("segment"), it.get("metric"),
                 it.get("value"), it.get("unit"), it.get("period"),
                 (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "risk":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO risk_items (ticker, chunk_id, accession, form, filing_date,
                                           category, summary, severity, quote)
                   VALUES (?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, form, fdate, it.get("category"), it.get("summary"),
                 it.get("severity"), (it.get("quote") or "")[:1200]))
            n += 1
    elif name == "claims":
        for it in (payload.get("items") or []):
            con.execute(
                """INSERT INTO claims (ticker, chunk_id, accession, kind, published,
                                       topic, claim, stance, has_number, quote)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (ticker, cid, acc, form, fdate, it.get("topic"), it.get("claim"),
                 it.get("stance"), int(bool(it.get("has_number"))),
                 (it.get("quote") or "")[:1200]))
            n += 1
    return n


# --------------------------------------------------------------- runner

def run(con, name: str, ticker: str, limit: int | None, workers: int, model: str):
    spec = EXTRACTORS[name]
    rows = pick_chunks(con, name, spec, ticker, limit)
    if not rows:
        log(f"  nothing to do for {name}")
        return
    est = len(rows) * 2.6 / max(workers, 1) / 3600
    log(f"  {len(rows)} chunks queued for '{name}' "
        f"({workers} worker(s), est {est:.2f}h)")

    q: queue.Queue = queue.Queue()
    for r in rows:
        q.put(r)
    results: queue.Queue = queue.Queue()
    stop = threading.Event()

    def worker():
        while not stop.is_set():
            try:
                cid, text, acc, form, fdate, section, tick = q.get_nowait()
            except queue.Empty:
                return
            payload, ms = ollama(spec["prompt"].format(chunk=text[:4000]),
                                 spec["schema"], model,
                                 num_predict=spec.get("num_predict", 900))
            results.put((cid, acc, form, fdate, tick, payload, ms))
            q.task_done()

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(workers)]
    t0 = time.time()
    for t in threads:
        t.start()

    done = found = failed = 0
    total = len(rows)
    try:
        while done < total:
            cid, acc, form, fdate, tick, payload, ms = results.get(timeout=600)
            done += 1
            ok = payload is not None
            if not ok:
                failed += 1
            con.execute(
                """INSERT OR REPLACE INTO extractions
                   (ticker, chunk_id, extractor, model, ok, payload, elapsed_ms, ts)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (tick, cid, name, model, int(ok), json.dumps(payload or {}), ms,
                 time.strftime("%Y-%m-%dT%H:%M:%S")))
            if ok:
                found += flatten(con, name, (cid, acc, form, fdate, tick), payload)
            if done % 25 == 0 or done == total:
                con.commit()
                rate = done / max(time.time() - t0, 1)
                eta = (total - done) / max(rate, 1e-6) / 60
                log(f"    {done}/{total}  {found} items  {failed} failed  "
                    f"{rate*60:.0f}/min  ETA {eta:.0f}m")
    except queue.Empty:
        log("    timed out waiting on a worker; committing what we have")
    finally:
        stop.set()
        con.commit()
    log(f"  '{name}' done: {done} chunks, {found} items extracted, {failed} failures, "
        f"{(time.time()-t0)/60:.1f} min")


def status(con):
    log("extraction status:")
    rows = con.execute(
        """SELECT extractor, ticker, COUNT(*), SUM(ok), AVG(elapsed_ms)
           FROM extractions GROUP BY extractor, ticker""").fetchall()
    if not rows:
        log("  (nothing extracted yet)")
    for ex, tick, n, ok, ms in rows:
        log(f"  {ex:<10} {tick:<6} {n:>6} chunks  {ok} ok  avg {ms/1000:.1f}s")
    for table in ("guidance", "risk_items"):
        n = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        log(f"  -> {table:<12} {n:,} rows")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--extractor", nargs="*", default=["guidance"],
                   choices=list(EXTRACTORS) + ["all"])
    p.add_argument("--ticker", default="GEV")
    p.add_argument("--limit", type=int)
    p.add_argument("--workers", type=int, default=2)
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--status", action="store_true")
    a = p.parse_args()

    con = connect()
    if a.status:
        status(con); con.close(); return

    names = list(EXTRACTORS) if "all" in a.extractor else a.extractor
    for name in names:
        log("-" * 66)
        log(f"EXTRACTOR: {name}  ticker={a.ticker}  model={a.model}")
        run(con, name, a.ticker, a.limit, a.workers, a.model)
    status(con)
    con.close()


if __name__ == "__main__":
    main()
