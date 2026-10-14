"""Ingest GEV structured financials (SEC XBRL company facts) and daily price history."""
from __future__ import annotations

import csv
import io
import time

from common import CIK, Fetcher, connect, load_config, log, mark

FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
# Stooq now sits behind a JavaScript wall and returns a 796-byte stub, so use
# Yahoo's chart API, which needs a browser-style user agent.
YAHOO_URL = ("https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
             "?range=10y&interval=1d&events=div%2Csplit")
BROWSER_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch_xbrl(con, fetch: Fetcher, tk: dict) -> int:
    """Flatten one company's companyfacts JSON into tidy rows, one per fact."""
    cik, ticker = tk["cik"], tk["ticker"]
    r = fetch.get(FACTS_URL.format(cik=cik))
    if not r:
        log(f"  {ticker}: companyfacts unavailable")
        return 0
    try:
        doc = r.json()
    except Exception:
        log(f"  {ticker}: companyfacts unparseable")
        return 0
    n = 0
    for taxonomy, tags in doc.get("facts", {}).items():
        for tag, body in tags.items():
            label = body.get("label") or ""
            for unit, entries in body.get("units", {}).items():
                for e in entries:
                    try:
                        con.execute(
                            """INSERT OR IGNORE INTO xbrl_facts
                               (taxonomy, ticker, tag, label, unit, start_date, end_date,
                                fy, fp, form, accession, frame, val)
                               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (taxonomy, ticker, tag, label, unit, e.get("start"), e.get("end"),
                             e.get("fy"), e.get("fp"), e.get("form"), e.get("accn"),
                             e.get("frame"), e.get("val")))
                        n += 1
                    except Exception:
                        continue
    con.commit()
    tags = con.execute("SELECT COUNT(DISTINCT tag) FROM xbrl_facts WHERE ticker=?",
                       (ticker,)).fetchone()[0]
    log(f"  {ticker}: {n} xbrl facts across {tags} tags")
    mark(con, "xbrl", ticker, "ok", f"{n} facts / {tags} tags")
    return n


def fetch_prices(con, fetch: Fetcher, ticker: str = "GEV") -> int:
    """Daily OHLCV + adjusted close from Yahoo's chart API (no key required)."""
    r = fetch.get(YAHOO_URL.format(sym=ticker), headers=BROWSER_UA)
    if not r:
        log(f"  {ticker}: price history unavailable")
        mark(con, "prices", ticker, "fail", "no response")
        return 0
    try:
        res = r.json()["chart"]["result"][0]
        ts = res["timestamp"]
        q = res["indicators"]["quote"][0]
        adj = (res["indicators"].get("adjclose") or [{}])[0].get("adjclose") or [None] * len(ts)
    except Exception as exc:
        log(f"  {ticker}: price payload unparseable: {type(exc).__name__}")
        mark(con, "prices", ticker, "fail", str(exc)[:200])
        return 0

    n = 0
    for i, epoch in enumerate(ts):
        try:
            date = time.strftime("%Y-%m-%d", time.gmtime(epoch))
            if q["close"][i] is None:
                continue
            con.execute(
                """INSERT OR REPLACE INTO prices(ticker,date,open,high,low,close,volume,adjclose)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (ticker, date, q["open"][i], q["high"][i], q["low"][i], q["close"][i],
                 q["volume"][i], adj[i] if i < len(adj) else None))
            n += 1
        except Exception:
            continue
    con.commit()
    rng = con.execute("SELECT MIN(date), MAX(date), COUNT(*) FROM prices WHERE ticker=?",
                      (ticker,)).fetchone()
    log(f"  {ticker}: {n} price rows, {rng[0]} -> {rng[1]}")
    mark(con, "prices", ticker, "ok", f"{rng[2]} rows {rng[0]}..{rng[1]}")
    return n


def summarize(con) -> None:
    """Print the handful of facts most likely to anchor a memo."""
    headline = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "OperatingIncomeLoss", "NetIncomeLoss", "GrossProfit",
                "CashAndCashEquivalentsAtCarryingValue", "Assets", "Liabilities",
                "StockholdersEquity", "ResearchAndDevelopmentExpense",
                "EarningsPerShareDiluted", "CommonStockSharesOutstanding"]
    log("headline facts available:")
    for tag in headline:
        row = con.execute(
            """SELECT COUNT(*), MIN(end_date), MAX(end_date) FROM xbrl_facts
               WHERE tag=? AND val IS NOT NULL""", (tag,)).fetchone()
        if row and row[0]:
            log(f"    {tag:<58} {row[0]:>4} pts  {row[1]} -> {row[2]}")


def main():
    import argparse
    from common import load_universe
    p = argparse.ArgumentParser()
    p.add_argument("--tier", nargs="*", default=["A", "B", "C"])
    p.add_argument("--ticker")
    a = p.parse_args()

    cfg = load_config()
    con = connect()
    fetch = Fetcher(cfg)
    universe = [t for t in load_universe()
                if t["tier"] in a.tier and (not a.ticker or t["ticker"] == a.ticker)]
    log(f"structured data for {len(universe)} tickers")
    for tk in universe:
        try:
            fetch_xbrl(con, fetch, tk)
            fetch_prices(con, fetch, tk["ticker"])
        except Exception as exc:
            log(f"  {tk['ticker']} FAILED: {type(exc).__name__}: {exc}")
    con.close()


if __name__ == "__main__":
    main()
