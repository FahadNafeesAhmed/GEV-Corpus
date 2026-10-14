"""Derived tables that need no model - pure SQL over what is already extracted.
Fast (seconds), idempotent, safe to run any time.

    python derive.py

  mgmt_guidance      dated guidance revisions: each forward guidance row with the
                     prior value for the same metric, so a raise/lower is visible
  comps_inputs       dated valuation inputs per ticker from XBRL + prices
                     (market cap, P/E, P/S, EV/EBIT) - observation dates kept
  backlog_quarterly  XBRL spine: contract liabilities, RPO, customer advances,
                     capex as filed, status='xbrl', so the LLM-extracted series
                     can be checked against the authoritative numbers
  catalyst_calendar  next earnings estimated from the 8-K item 2.02 cadence
  validation CSV     random sample of extracted rows with a verbatim check, for
                     a human pass on units, dates, and forward-vs-historical
"""
from __future__ import annotations

import csv
import time

from common import DATA, connect, log

ANNUAL_TAGS = {
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"],
    "operating_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss"],
    "eps_diluted": ["EarningsPerShareDiluted"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"],
    "d_and_a": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
                "DepreciationAmortizationAndAccretionNet"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
}
INSTANT_TAGS = {
    "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "debt": ["LongTermDebt", "LongTermDebtNoncurrent", "DebtLongtermAndShorttermCombinedAmount",
             "LongTermDebtAndCapitalLeaseObligations"],
    "shares": ["EntityCommonStockSharesOutstanding", "CommonStockSharesOutstanding"],
    "contract_liabilities": ["ContractWithCustomerLiability", "ContractWithCustomerLiabilityCurrent"],
    "rpo": ["RevenueRemainingPerformanceObligation"],
}
# XBRL tags that belong in the backlog/deposit/cash series as an authoritative spine.
BACKLOG_XBRL = {
    "contract_liabilities": ["ContractWithCustomerLiability", "ContractWithCustomerLiabilityCurrent",
                             "ContractWithCustomerLiabilityNoncurrent"],
    "rpo_total": ["RevenueRemainingPerformanceObligation"],
    "customer_advances": ["CustomerAdvancesCurrent", "CustomerAdvancesAndDeposits",
                          "CustomerAdvancesAndDepositsCurrent"],
    "deferred_revenue": ["DeferredRevenue", "DeferredRevenueCurrent", "ContractWithCustomerLiabilityCurrent"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"],
    "free_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
}


def latest_annual(con, ticker, tags):
    for t in tags:
        r = con.execute(
            """SELECT val, end_date FROM xbrl_facts
               WHERE ticker=? AND tag=? AND val IS NOT NULL AND form IN ('10-K','20-F','40-F')
                 AND start_date IS NOT NULL
                 AND julianday(end_date) - julianday(start_date) > 300
               ORDER BY end_date DESC LIMIT 1""", (ticker, t)).fetchone()
        if r:
            return r[0], r[1], t
    return None, None, None


def latest_instant(con, ticker, tags):
    for t in tags:
        r = con.execute(
            """SELECT val, end_date FROM xbrl_facts
               WHERE ticker=? AND tag=? AND val IS NOT NULL AND start_date IS NULL
               ORDER BY end_date DESC LIMIT 1""", (ticker, t)).fetchone()
        if r:
            return r[0], r[1], t
    return None, None, None


def derive_comps(con) -> int:
    tickers = [r[0] for r in con.execute("SELECT DISTINCT ticker FROM xbrl_facts WHERE ticker IS NOT NULL")]
    n = 0

    def put(ticker, as_of, metric, value, unit, source):
        nonlocal n
        if value is None or as_of is None:
            return
        con.execute("""INSERT OR REPLACE INTO comps_inputs (ticker, as_of, metric, value, unit, source)
                       VALUES (?,?,?,?,?,?)""", (ticker, as_of, metric, float(value), unit, source))
        n += 1

    for tk in tickers:
        px = con.execute("SELECT date, close FROM prices WHERE ticker=? ORDER BY date DESC LIMIT 1",
                         (tk,)).fetchone()
        a = {k: latest_annual(con, tk, v) for k, v in ANNUAL_TAGS.items()}
        i = {k: latest_instant(con, tk, v) for k, v in INSTANT_TAGS.items()}
        for k, (val, d, tag) in a.items():
            put(tk, d, k + "_fy", val, "USD" if k != "eps_diluted" else "USD/share", "xbrl:" + (tag or ""))
        for k, (val, d, tag) in i.items():
            put(tk, d, k, val, "shares" if k == "shares" else "USD", "xbrl:" + (tag or ""))
        if not px:
            continue
        pdate, price = px
        put(tk, pdate, "price", price, "USD", "yahoo")
        shares = i["shares"][0]
        rev, oi, ni, eps = a["revenue"][0], a["operating_income"][0], a["net_income"][0], a["eps_diluted"][0]
        da = a["d_and_a"][0]
        cash, debt = i["cash"][0] or 0.0, i["debt"][0] or 0.0
        if shares:
            mcap = price * shares
            put(tk, pdate, "market_cap", mcap, "USD", "derived: price x shares")
            ev = mcap + debt - cash
            put(tk, pdate, "enterprise_value", ev, "USD", "derived: mcap + debt - cash (latest instants)")
            if rev:
                put(tk, pdate, "ps_fy", mcap / rev, "x", "derived: mcap / FY revenue")
                put(tk, pdate, "ev_sales_fy", ev / rev, "x", "derived")
            if oi and oi > 0:
                put(tk, pdate, "ev_ebit_fy", ev / oi, "x", "derived: EV / FY operating income")
            if oi is not None and da and (oi + da) > 0:
                put(tk, pdate, "ev_ebitda_fy", ev / (oi + da), "x", "derived: EV / (FY op income + D&A)")
        if eps and eps > 0:
            put(tk, pdate, "pe_fy", price / eps, "x", "derived: price / FY diluted EPS")
    con.commit()
    log(f"comps_inputs: {n} dated rows across {len(tickers)} tickers")
    return n


FWD_CUES = ("expect", "outlook", "guidance", "target", "anticipate", "will be", "on track",
            "forecast", "project")
HIST_CUES = ("were $", "was $", "reclassified", "recognized during",
             "for the three months ended", "for the year ended")


def backfill_is_forward(con) -> int:
    """Rows extracted before the is_forward column existed are NULL; apply the
    same heuristic the extractor now applies, so mgmt_guidance is not empty."""
    rows = con.execute("SELECT id, quote FROM guidance WHERE is_forward IS NULL").fetchall()
    for gid, quote in rows:
        ql = (quote or "").lower()
        fwd = int(any(c in ql for c in FWD_CUES) and not any(c in ql for c in HIST_CUES))
        con.execute("UPDATE guidance SET is_forward=? WHERE id=?", (fwd, gid))
    con.commit()
    if rows:
        log(f"is_forward backfilled on {len(rows):,} guidance rows")
    return len(rows)


def derive_mgmt_guidance(con) -> int:
    backfill_is_forward(con)
    con.execute("DELETE FROM mgmt_guidance")
    rows = con.execute(
        """SELECT id, ticker, filing_date, metric, value, period, direction, quote FROM guidance
           WHERE is_forward=1 AND metric IS NOT NULL
           ORDER BY ticker, LOWER(metric), filing_date, id""").fetchall()
    prev = {}
    n = 0
    for gid, tk, fdate, metric, value, period, direction, quote in rows:
        key = (tk, (metric or "").lower().strip())
        prior = prev.get(key)
        con.execute(
            """INSERT INTO mgmt_guidance (ticker, stated_on, metric, value, period, direction,
                                          prior_value, guidance_id, quote)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (tk, fdate, metric, value, period, direction, prior, gid, (quote or "")[:600]))
        prev[key] = value
        n += 1
    con.commit()
    log(f"mgmt_guidance: {n} dated rows (forward-flagged guidance with prior value)")
    return n


def derive_backlog_spine(con) -> int:
    con.execute("DELETE FROM backlog_quarterly WHERE status='xbrl'")
    n = 0
    for metric, tags in BACKLOG_XBRL.items():
        for tag in tags:
            for tk, val, start, end, form, acc in con.execute(
                    """SELECT ticker, val, start_date, end_date, form, accession FROM xbrl_facts
                       WHERE tag=? AND val IS NOT NULL AND ticker IS NOT NULL
                       ORDER BY ticker, end_date""", (tag,)):
                period = f"{start} .. {end}" if start else end
                con.execute(
                    """INSERT INTO backlog_quarterly (ticker, chunk_id, accession, form, filing_date,
                                                      as_of, metric, value, unit, period, status, quote)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (tk, None, acc, form, end, end, metric, str(val), "USD", period, "xbrl",
                     "xbrl tag " + tag))
                n += 1
    con.commit()
    log(f"backlog_quarterly: {n} XBRL spine rows (status='xbrl')")
    return n


def derive_catalysts(con) -> int:
    n = 0
    for tk, in con.execute("SELECT DISTINCT ticker FROM filings WHERE ticker IS NOT NULL"):
        dates = [r[0] for r in con.execute(
            """SELECT filing_date FROM filings WHERE ticker=? AND form='8-K' AND items LIKE '%2.02%'
               ORDER BY filing_date DESC LIMIT 8""", (tk,))]
        if len(dates) < 2:
            continue
        # median gap between the last few earnings 8-Ks, projected forward from the latest
        import datetime as dt
        ds = [dt.date.fromisoformat(d) for d in dates]
        gaps = sorted((ds[i] - ds[i + 1]).days for i in range(len(ds) - 1))
        gap = gaps[len(gaps) // 2]
        nxt = ds[0] + dt.timedelta(days=gap)
        while nxt < dt.date.today():
            nxt += dt.timedelta(days=gap)
        con.execute("""INSERT OR IGNORE INTO catalyst_calendar (date, event, ticker, source, confirmed)
                       VALUES (?,?,?,?,0)""",
                    (nxt.isoformat(), "earnings release (estimated from 8-K item 2.02 cadence)",
                     tk, f"last {dates[0]}, median gap {gap}d", ))
        n += 1
    con.commit()
    log(f"catalyst_calendar: {n} estimated earnings dates (confirmed=0 until a source confirms)")
    return n


def validation_sample(con, path=None, per_table: int = 150) -> str:
    path = path or (DATA / "validation_sample.csv")

    def squash(s):
        return "".join((s or "").split()).lower()

    rows = []
    # each column list is exactly 7 wide: ticker, date, a, b, c, flag, quote
    for table, cols in (("guidance", "ticker, filing_date, metric, value, period, is_forward, quote"),
                        ("risk_items", "ticker, filing_date, category, summary, severity, '', quote"),
                        ("claims", "ticker, published, topic, claim, stance, has_number, quote")):
        # prefix every column with t. - chunks also has ticker/filing_date, so bare
        # names would be ambiguous in the join
        sel = ", ".join(("t." + c.strip()) if c.strip() != "''" else "''" for c in cols.split(","))
        for r in con.execute(f"""SELECT t.id, {sel}, c.text, c.form
                                  FROM {table} t JOIN chunks c ON c.id=t.chunk_id
                                  ORDER BY RANDOM() LIMIT {int(per_table)}""").fetchall():
            tid, tk, d, a, b, cc, flag, quote, text, form = r
            rows.append([table, tid, tk, d, form, a, b, cc, flag,
                         "verbatim" if squash(quote) in squash(text) else "NOT VERBATIM",
                         (quote or "")[:300]])
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["table", "id", "ticker", "date", "form", "field_a", "field_b", "field_c",
                    "flag(is_forward/severity/has_number)", "quote_check", "quote",
                    "HUMAN: unit ok?", "HUMAN: date ok?", "HUMAN: forward vs historical?", "notes"])
        w.writerows(rows)
    log(f"validation sample: {len(rows)} rows -> {path}")
    return str(path)


def backfill_insights_verdict(con) -> int:
    """Cards built before the `verdict` column existed stored the verdict in `stance`."""
    n = con.execute("""UPDATE insights SET verdict = stance
                       WHERE verdict IS NULL
                         AND stance IN ('supported','contested','refuted','insufficient')""").rowcount
    con.commit()
    if n:
        log(f"insights: verdict backfilled on {n} cards")
    return n


def main():
    con = connect()
    t0 = time.time()
    backfill_insights_verdict(con)
    derive_mgmt_guidance(con)
    derive_comps(con)
    derive_backlog_spine(con)
    derive_catalysts(con)
    validation_sample(con)
    log(f"derive done in {time.time()-t0:.1f}s")
    con.close()


if __name__ == "__main__":
    main()
