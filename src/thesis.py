"""Disagreement testing. Turns candidate claims into insight cards:

  claim · supporting evidence · opposing evidence · are both sides measuring the
  same thing? · which line item and how much · what the market expects (dated) ·
  a falsification condition observable within the competition horizon · catalyst

    python thesis.py                      seed hypotheses + top numeric claims
    python thesis.py --claim "..."        one card
    python thesis.py --limit 12

Nothing is written to INSIGHTS.md without a falsification condition. A card
that cannot say what would prove it wrong is a story, not a research lead.
"""
from __future__ import annotations

import argparse
import json
import time

import numpy as np

from common import DATA, connect, log
import embed
import extract

REPORT = DATA / "INSIGHTS.md"

# Starting hypotheses. Each is deliberately falsifiable and tied to a line item.
SEED_HYPOTHESES = [
    {"claim": "GE Vernova is priced as a data-center power play while its own filings frame demand as broad electrification; the AI/data-center narrative is ahead of what management commits to in writing.",
     "topic": "data-center-demand"},
    {"claim": "The $176B remaining performance obligation, with its published recognition schedule, supports the revenue trajectory embedded in the current valuation without requiring new orders.",
     "topic": "backlog"},
    {"claim": "Gas turbine scarcity pricing will persist through 2027 because competitor capacity additions (Siemens Energy, Mitsubishi Power) lag demand.",
     "topic": "pricing"},
    {"claim": "Customer-side project documents show delivery and commercial-operation dates slipping relative to the commitment language in GE Vernova's disclosures.",
     "topic": "gas-turbine-supply"},
    {"claim": "Offshore wind losses already recognized exceed the remaining cash exposure; the wind segment is no longer a source of negative surprises.",
     "topic": "wind"},
    {"claim": "Grid-operator load forecasts (PJM, ERCOT) have been revised upward each vintage and actual energized data-center load is tracking the forecasts.",
     "topic": "data-center-demand"},
    {"claim": "Services revenue on the installed gas fleet is growing faster than new-equipment revenue, driven by higher operating hours.",
     "topic": "financials"},
    {"claim": "Reservation agreements and slot deposits are converting into firm orders at a stable rate, with no double counting between reservation GW and backlog.",
     "topic": "backlog"},
    {"claim": "Electrification segment growth is predominantly organic; the Prolec GE consolidation and acquired backlog account for a minority of the reported increase.",
     "topic": "electrification"},
    {"claim": "Announced gas turbine output capacity (GW per year) is gated by a supplier bottleneck - castings, forgings or hot-gas-path components - that expands later than GE Vernova's own assembly capacity.",
     "topic": "gas-turbine-supply"},
    {"claim": "Management's language on pricing and delivery timing has become more qualified quarter over quarter in transcripts, even as headline guidance was raised.",
     "topic": "management"},
    {"claim": "Grid-operator forecast vintages show announced data-center load being counted more than once across utilities, so contracted or energized load is materially below the headline forecasts.",
     "topic": "data-center-demand"},
    {"claim": "Reciprocating engines, fuel cells and battery storage are winning a growing share of behind-the-meter data-center power that the gas-turbine narrative assumes belongs to GE Vernova.",
     "topic": "competition"},
    {"claim": "The next two quarters contain an observable catalyst - an earnings release, a capacity milestone, or an operator decision - that would move the stock if the backlog conversion rate disappoints.",
     "topic": "valuation"},
    {"claim": "Peer valuation inputs (Siemens Energy, Vertiv, Eaton) imply GE Vernova's multiple already discounts several years of scarcity pricing rather than a normal cycle.",
     "topic": "valuation"},
]

CARD_SCHEMA = {
    "type": "object",
    "properties": {
        "supporting": {"type": "array", "maxItems": 6, "items": {"type": "object", "properties": {
            "point": {"type": "string"}, "source_ref": {"type": "string"}, "tier": {"type": "string"}},
            "required": ["point", "source_ref", "tier"]}},
        "opposing": {"type": "array", "maxItems": 6, "items": {"type": "object", "properties": {
            "point": {"type": "string"}, "source_ref": {"type": "string"}, "tier": {"type": "string"}},
            "required": ["point", "source_ref", "tier"]}},
        "definitions": {"type": "string"},
        "financial_relevance": {"type": "string"},
        "market_expectation": {"type": "string"},
        "falsification_condition": {"type": "string"},
        "catalyst_date": {"type": "string"},
        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
        "verdict": {"type": "string", "enum": ["supported", "contested", "refuted", "insufficient"]},
    },
    "required": ["supporting", "opposing", "definitions", "financial_relevance",
                 "market_expectation", "falsification_condition", "catalyst_date",
                 "confidence", "verdict"],
}

QUERY_SCHEMA = {
    "type": "object",
    "properties": {"support_queries": {"type": "array", "items": {"type": "string"}},
                   "oppose_queries": {"type": "array", "items": {"type": "string"}}},
    "required": ["support_queries", "oppose_queries"],
}


_MATRIX_CACHE: dict = {}


def _matrix(con, tiers):
    """Load the embedding matrix for a tier set once per process. Each card runs
    a dozen retrievals; re-reading 700 MB of vectors from SQLite for every one
    would spend the phase budget on I/O."""
    key = tuple(tiers) if tiers else ("ALL",)
    if key in _MATRIX_CACHE:
        return _MATRIX_CACHE[key]
    sql = """SELECT e.chunk_id, c.tier, c.kind, c.form, c.filing_date, c.section, c.ticker,
                    substr(c.text, 1, 1200), e.vec
             FROM embeddings e JOIN chunks c ON c.id = e.chunk_id"""
    params: list = []
    if tiers:
        sql += " WHERE c.tier IN (%s)" % ",".join("?" * len(tiers))
        params += list(tiers)
    meta, blobs = [], []
    for r in con.execute(sql, params):
        meta.append(r[:8])
        blobs.append(r[8])
    if not meta:
        _MATRIX_CACHE[key] = (meta, None)
        return _MATRIX_CACHE[key]
    mat = np.frombuffer(b"".join(blobs), dtype=np.float32).reshape(len(meta), -1)
    mat = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
    _MATRIX_CACHE[key] = (meta, mat)
    log(f"    loaded {len(meta):,} vectors for tiers {key}")
    return _MATRIX_CACHE[key]


def retrieve(con, query: str, k: int, tiers: tuple[str, ...] | None = None):
    """Brute-force cosine over stored embeddings, optionally restricted by tier."""
    meta, mat = _matrix(con, tiers)
    if mat is None:
        return []
    qv = np.array(embed.embed_batch([query], embed.MODEL)[0], dtype=np.float32)
    qv /= (np.linalg.norm(qv) + 1e-9)
    scores = mat @ qv
    out = []
    for i in np.argsort(-scores)[:k]:
        cid, tier, kind, form, fdate, section, tick, text = meta[i]
        out.append({"chunk_id": cid, "score": float(scores[i]), "tier": tier, "kind": kind,
                    "form": form, "date": fdate, "section": section, "ticker": tick,
                    "text": " ".join((text or "").split())[:900]})
    return out


def expectations(con, topic: str) -> str:
    """Dated management guidance (with prior values where derived), attributed
    analyst calls, and comps inputs - three separate blocks on purpose."""
    g = con.execute("""SELECT stated_on, metric, value, prior_value, period FROM mgmt_guidance
                       WHERE ticker='GEV' ORDER BY stated_on DESC LIMIT 12""").fetchall()
    if not g:
        g = [(r[0], r[1], r[2], None, r[3]) for r in con.execute(
            """SELECT filing_date, metric, value, period FROM guidance
               WHERE ticker='GEV' AND is_forward=1 ORDER BY filing_date DESC LIMIT 12""").fetchall()]
    a = con.execute("""SELECT stated_on, analyst, firm, metric, value, period FROM analyst_calls
                       ORDER BY stated_on DESC LIMIT 12""").fetchall()
    c = con.execute("""SELECT ticker, as_of, metric, value FROM comps_inputs
                       WHERE metric IN ('pe_fy','ev_ebit_fy','ev_ebitda_fy','ev_sales_fy')
                       ORDER BY ticker, metric""").fetchall()
    lines = ["MANAGEMENT GUIDANCE (dated, from filings; prior value where known):"]
    lines += [f"  {r[0]} {r[1]}: {r[2]}" + (f" (prior {r[3]})" if r[3] else "") + f" [{r[4]}]" for r in g] \
        or ["  none extracted yet"]
    lines.append("ATTRIBUTED ANALYST CALLS (individual, not consensus):")
    lines += [f"  {r[0]} {r[1]} @ {r[2]}: {r[3]} {r[4]} ({r[5]})" for r in a] or ["  none extracted yet"]
    lines.append("COMPS INPUTS (derived from XBRL + price, with observation date):")
    lines += [f"  {r[0]} {r[2]}={r[3]:.1f}x as of {r[1]}" for r in c] or ["  none derived yet - run derive.py"]
    return "\n".join(lines)


def build_card(con, claim: str, topic: str, model: str, k: int = 8) -> dict | None:
    # 1. ask the model for search queries on both sides - opposing evidence is
    #    rarely found by searching for the claim itself
    qpayload, _ = extract.ollama(
        "For the following investment claim, write 3 short search queries that would find "
        "SUPPORTING evidence and 3 that would find OPPOSING evidence in company filings, "
        "academic papers and news. Queries should name concrete things (metrics, products, "
        "counterparties), not restate the claim.\n\nCLAIM: " + claim,
        QUERY_SCHEMA, model, num_predict=400)
    sq = (qpayload or {}).get("support_queries") or [claim]
    oq = (qpayload or {}).get("oppose_queries") or ["evidence against: " + claim]

    # 2. retrieve, primary and academic tiers first, then commentary
    def gather(queries, n, exclude=frozenset()):
        # The first 16 cards all quoted the same FCF/revenue boilerplate with an
        # empty opposing side: a handful of dense financial-statement chunks score
        # high on ANY finance query, and the "against" queries retrieved the same
        # bullish chunks as the "for" queries. Two fixes: at most 2 chunks per
        # source document, and the opposing set excludes everything already used
        # as support.
        seen, per_doc, out = set(), {}, []
        for q in queries[:3]:
            hits = (retrieve(con, q, n * 3, ("primary", "academic"))
                    + retrieve(con, q, max(2, n), ("commentary",)))
            for hit in sorted(hits, key=lambda h: -h["score"]):
                cid = hit["chunk_id"]
                if cid in seen or cid in exclude:
                    continue
                row = con.execute("SELECT accession FROM chunks WHERE id=?", (cid,)).fetchone()
                acc = row[0] if row else str(cid)
                if per_doc.get(acc, 0) >= 2:
                    continue
                per_doc[acc] = per_doc.get(acc, 0) + 1
                seen.add(cid)
                out.append(hit)
        return sorted(out, key=lambda h: -h["score"])[:k]

    sup = gather(sq, k)
    opp = gather(oq, k, exclude=frozenset(h["chunk_id"] for h in sup))

    def fmt(hits):
        return "\n\n".join(
            f"[chunk {h['chunk_id']} | {h['tier']} | {h['kind']} {h['form']} {h['date']} {h['ticker']}]\n{h['text']}"
            for h in hits) or "(nothing retrieved)"

    prompt = (
        "You are an equity research analyst testing a claim, not defending it.\n\n"
        f"CLAIM: {claim}\n\n"
        f"EVIDENCE RETRIEVED FOR THE CLAIM:\n{fmt(sup)}\n\n"
        f"EVIDENCE RETRIEVED AGAINST THE CLAIM:\n{fmt(opp)}\n\n"
        f"MARKET EXPECTATIONS ON FILE:\n{expectations(con, topic)}\n\n"
        "Produce the card. Rules:\n"
        "- Every supporting or opposing point must cite a chunk id from above in `source_ref` and its tier. "
        "Do not invent evidence. If a side has nothing, leave its list empty.\n"
        "- The MARKET EXPECTATIONS block is context for the `market_expectation` field only. Never copy it "
        "into supporting or opposing points, and never cite generic revenue/FCF guidance as evidence for a "
        "claim about something else.\n"
        "- Opposing points must genuinely cut against the claim. A supportive fact restated is not opposition.\n"
        "- `definitions`: state whether the two sides measure the same thing (e.g. backlog vs RPO vs "
        "reservations; announced vs energized load). Name any mismatch.\n"
        "- `financial_relevance`: which line item and roughly how much, or 'unclear'.\n"
        "- `market_expectation`: what the dated guidance/analyst rows imply is already expected. "
        "Never call a few analyst calls 'consensus'.\n"
        "- `falsification_condition`: one observable thing, within 3-12 months, that would prove the "
        "claim wrong. Be specific (a filing, a number, a date). This field is mandatory.\n"
        "- `catalyst_date`: the next date on which that observable arrives, if known.\n"
        "- Numbers must be copied from the evidence, never computed.")
    # A full card is ~3,000-4,500 tokens of JSON; the first attempt truncated at 2,200.
    card, ms = extract.ollama(prompt, CARD_SCHEMA, model, num_predict=4500, timeout=420)
    if not card:
        return None
    card.update({"claim": claim, "topic": topic, "n_support": len(sup), "n_oppose": len(opp),
                 "elapsed_ms": ms})
    return card


def candidate_claims(con, limit: int) -> list[dict]:
    out = list(SEED_HYPOTHESES)
    rows = con.execute("""SELECT claim, topic, stance, COUNT(*) c FROM claims
                          WHERE has_number=1 AND topic != 'other'
                          GROUP BY claim ORDER BY c DESC, LENGTH(claim) DESC LIMIT ?""",
                       (max(limit - len(out), 0),)).fetchall()
    out += [{"claim": r[0], "topic": r[1], "stance": r[2]} for r in rows]
    return out[:limit]


def write_report(con) -> None:
    rows = con.execute("""SELECT claim, topic, verdict, confidence, supporting, opposing, definitions,
                                 financial_relevance, market_expectation, falsification, catalyst_date,
                                 n_support, n_oppose, created_at
                          FROM insights ORDER BY
                            CASE verdict WHEN 'contested' THEN 0 WHEN 'refuted' THEN 1
                                         WHEN 'supported' THEN 2 ELSE 3 END, created_at DESC""").fetchall()
    lines = ["# Insight cards", "",
             f"{len(rows)} cards. Contested claims first - that is where an edge lives if one exists.",
             "A card without a falsification condition was not written.", ""]
    for r in rows:
        claim, topic, verdict, conf, sup, opp, defs, fin, mkt, fals, cat, ns, no, ts = r
        verdict, conf, ts = verdict or "unverdicted", conf or "-", ts or ""
        lines += [f"## {claim}", "",
                  f"**{verdict}** · confidence {conf} · topic {topic} · {ns} for / {no} against · {ts[:10]}", "",
                  "**Supporting**"]
        for p in json.loads(sup or "[]"):
            lines.append(f"- {p.get('point')}  _({p.get('tier')}, {p.get('source_ref')})_")
        lines += ["", "**Opposing**"]
        for p in json.loads(opp or "[]"):
            lines.append(f"- {p.get('point')}  _({p.get('tier')}, {p.get('source_ref')})_")
        lines += ["", f"**Same definitions?** {defs}", "",
                  f"**Financial relevance:** {fin}", "",
                  f"**Market expectation:** {mkt}", "",
                  f"**Falsification condition:** {fals}", "",
                  f"**Catalyst:** {cat or 'not identified'}", "", "---", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    log(f"insights report: {REPORT} ({len(rows)} cards)")


def run(con, claims: list[dict], model: str, deadline=None, refresh: bool = False) -> int:
    n = 0
    for c in claims:
        if deadline and time.time() > deadline:
            log("  thesis: deadline reached")
            break
        if con.execute("SELECT 1 FROM insights WHERE claim=?", (c["claim"],)).fetchone():
            if not refresh:
                continue
            con.execute("DELETE FROM insights WHERE claim=?", (c["claim"],))   # rebuild on newer evidence
        log(f"  card: {c['claim'][:80]}")
        try:
            card = build_card(con, c["claim"], c.get("topic", "other"), model)
        except Exception as exc:
            log(f"    failed: {type(exc).__name__}: {str(exc)[:100]}")
            continue
        if not card or not (card.get("falsification_condition") or "").strip():
            log("    no falsification condition - not written")
            continue
        con.execute(
            """INSERT INTO insights (claim, topic, stance, verdict, supporting, opposing, definitions,
                                     financial_relevance, market_expectation, falsification,
                                     catalyst_date, confidence, n_support, n_oppose, created_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (c["claim"], c.get("topic"), c.get("stance"), card.get("verdict"),
             json.dumps(card.get("supporting") or []), json.dumps(card.get("opposing") or []),
             card.get("definitions"), card.get("financial_relevance"), card.get("market_expectation"),
             card.get("falsification_condition"), card.get("catalyst_date"), card.get("confidence"),
             card.get("n_support"), card.get("n_oppose"), time.strftime("%Y-%m-%dT%H:%M:%S")))
        con.commit()
        n += 1
        log(f"    {card.get('verdict')} ({card.get('confidence')}) in {card.get('elapsed_ms',0)/1000:.0f}s")
    write_report(con)
    return n


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--claim")
    p.add_argument("--topic", default="other")
    p.add_argument("--limit", type=int, default=16)
    p.add_argument("--model", default=extract.DEFAULT_MODEL)
    p.add_argument("--refresh", action="store_true", help="rebuild cards that already exist")
    p.add_argument("--report-only", action="store_true",
                   help="write INSIGHTS.md from cards already in the database; no model calls")
    a = p.parse_args()
    con = connect()
    if a.report_only:
        write_report(con)
        con.close()
        return
    claims = [{"claim": a.claim, "topic": a.topic}] if a.claim else candidate_claims(con, a.limit)
    run(con, claims, a.model, refresh=a.refresh)
    con.close()


if __name__ == "__main__":
    main()
