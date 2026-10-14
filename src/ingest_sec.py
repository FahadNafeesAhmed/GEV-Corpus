"""Ingest SEC filings for every ticker in the universe: index, full text,
8-K exhibits, insider Form 4s.

    python ingest_sec.py                 # whole universe
    python ingest_sec.py --tier A B      # only these tiers
    python ingest_sec.py --ticker GEV
"""
from __future__ import annotations

import argparse
import json
import re
import time

from common import (RAW, Fetcher, already, connect, filing_url, html_to_text,
                    load_config, load_universe, log, mark)

# Narrative forms worth pulling full text for. 20-F/40-F/6-K cover foreign issuers.
NARRATIVE = ("10-K", "10-Q", "8-K", "DEF 14A", "DEFA14A", "S-1", "S-1/A", "424B3",
             "424B5", "10-12B", "10-12B/A", "ARS", "11-K", "SD", "20-F", "40-F", "6-K")

# An 8-K's primary document is a two-page cover sheet; the earnings release with
# segment results and guidance is an exhibit. Without these the corpus has no
# guidance at all between 10-Qs.
#
# Do NOT select exhibits by filename. Across 17 issuers the filing agents name
# them inconsistently - GE Vernova files its earnings release as
# "gevpressrelease2q26.htm", not "ex-99.1.htm", so an /ex-?99/ pattern silently
# misses every one. Instead take every document in the filing directory except
# the things we know are not exhibits.
EXHIBIT_FORMS = ("8-K", "6-K", "10-K", "10-Q")
NOT_AN_EXHIBIT = re.compile(
    r"(-index|index-headers|^R\d+\.htm|FilingSummary|^0\d{9}-\d\d-\d{6}\.txt$)", re.I)
# Item 2.02 is "Results of Operations and Financial Condition" - the 8-Ks that
# actually carry earnings releases and guidance.
EARNINGS_ITEM = "2.02"


def fetch_index(con, fetch: Fetcher, tk: dict) -> int:
    """Pull the filing index for one ticker, including older paginated batches."""
    cik, ticker, since = tk["cik"], tk["ticker"], tk.get("since", "2000-01-01")
    r = fetch.get(f"https://data.sec.gov/submissions/CIK{cik}.json")
    if not r:
        log(f"  {ticker}: submissions index unavailable")
        return 0
    doc = r.json()
    batches = [doc["filings"]["recent"]]
    for extra in doc["filings"].get("files", []):
        rr = fetch.get(f"https://data.sec.gov/submissions/{extra['name']}")
        if rr:
            batches.append(rr.json())

    n = 0
    for rec in batches:
        count = len(rec.get("accessionNumber", []))
        for i in range(count):
            if rec["filingDate"][i] < since:
                continue
            acc = rec["accessionNumber"][i]
            doc_name = rec["primaryDocument"][i]
            con.execute(
                """INSERT OR REPLACE INTO filings
                   (accession, ticker, form, filing_date, report_date, primary_doc,
                    url, items, size, fetched_at)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (acc, ticker, rec["form"][i], rec["filingDate"][i],
                 rec.get("reportDate", [""] * count)[i], doc_name,
                 filing_url(acc, doc_name, cik) if doc_name else "",
                 rec.get("items", [""] * count)[i], rec.get("size", [0] * count)[i],
                 time.strftime("%Y-%m-%dT%H:%M:%S")))
            n += 1
    con.commit()
    log(f"  {ticker}: {n} filings indexed (since {since})")
    return n


_PARSE_FAIL_SHOWN = 0


def _store_doc(con, ticker, acc, form, fdate, url, raw) -> int:
    global _PARSE_FAIL_SHOWN
    try:
        text = html_to_text(raw)
    except Exception as exc:
        # ~8% of Duke/Dominion exhibits failed with a bare AttributeError on run 2;
        # show where for the first few so it can actually be fixed
        _PARSE_FAIL_SHOWN += 1
        if _PARSE_FAIL_SHOWN <= 3:
            import traceback
            tail = " | ".join(traceback.format_exc().strip().splitlines()[-3:])
            log(f"    parse failed {acc}: {type(exc).__name__}: {tail[:220]}")
        else:
            log(f"    parse failed {acc}: {type(exc).__name__}")
        return 0
    if len(text) < 200:
        return 0
    con.execute(
        """INSERT OR REPLACE INTO documents
           (accession, ticker, form, filing_date, url, n_chars, text)
           VALUES (?,?,?,?,?,?,?)""",
        (acc, ticker, form, fdate, url, len(text), text))
    return len(text)


def fetch_documents(con, fetch: Fetcher, cfg: dict, tk: dict) -> int:
    """Download primary documents, plus EX-99 exhibits for 8-K/6-K filings."""
    cik, ticker = tk["cik"], tk["ticker"]
    rows = con.execute(
        f"""SELECT accession, form, filing_date, primary_doc, url FROM filings
            WHERE ticker=? AND form IN ({','.join('?' * len(NARRATIVE))})
              AND primary_doc != '' ORDER BY filing_date DESC""",
        [ticker, *NARRATIVE]).fetchall()

    done = exhibits = 0
    for acc, form, fdate, doc_name, url in rows:
        if already(con, "sec_doc", f"{ticker}:{acc}"):
            continue
        cache = RAW / f"{acc}_{doc_name}".replace("/", "_")
        if cache.exists():
            raw = cache.read_bytes()
        else:
            r = fetch.get(url)
            if not r:
                mark(con, "sec_doc", f"{ticker}:{acc}", "fail", url)
                continue
            raw = r.content
            if len(raw) <= cfg["max_filing_bytes"]:
                cache.write_bytes(raw)
        if _store_doc(con, ticker, acc, form, fdate, url, raw):
            done += 1

        # Exhibits: the earnings release lives here, not in the cover sheet.
        if form in EXHIBIT_FORMS:
            accn = acc.replace("-", "")
            idx = fetch.get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/index.json")
            if idx:
                try:
                    items = idx.json().get("directory", {}).get("item", [])
                except Exception:
                    items = []
                for it in items:
                    nm = it.get("name", "")
                    if not nm.lower().endswith((".htm", ".html")):
                        continue
                    if NOT_AN_EXHIBIT.search(nm) or nm == doc_name:
                        continue           # index pages, XBRL renders, primary doc
                    ex_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{nm}"
                    rr = fetch.get(ex_url)
                    if rr and _store_doc(con, ticker, f"{acc}#{nm}", form + "/EX",
                                         fdate, ex_url, rr.content):
                        exhibits += 1
        mark(con, "sec_doc", f"{ticker}:{acc}", "ok", f"{form} {fdate}")
        if done % 25 == 0 and done:
            con.commit()
            log(f"    {ticker}: {done} docs, {exhibits} exhibits")
    con.commit()
    log(f"  {ticker}: {done} documents + {exhibits} exhibits")
    return done


def _t(node, name):
    el = node.find(name)
    return el.get_text(strip=True) if el else ""


def fetch_insiders(con, fetch: Fetcher, tk: dict, max_filings: int | None = None) -> int:
    """Parse Form 4 ownership XML into structured transactions."""
    from bs4 import BeautifulSoup
    cik, ticker = tk["cik"], tk["ticker"]
    rows = con.execute(
        """SELECT accession, filing_date, primary_doc FROM filings
           WHERE ticker=? AND form IN ('4','4/A') ORDER BY filing_date DESC""",
        (ticker,)).fetchall()
    if max_filings:
        rows = rows[:max_filings]

    n = 0
    for acc, fdate, primary in rows:
        key = f"{ticker}:{acc}"
        if already(con, "sec_form4", key):
            continue
        accn = acc.replace("-", "")
        # The primary document is usually the rendered xslF345X05/*.xml; the raw
        # ownership XML sits beside it under the same base name.
        candidates = []
        if primary:
            base = primary.split("/")[-1]
            candidates.append(base if base.endswith(".xml") else base.rsplit(".", 1)[0] + ".xml")
        soup = None
        for cand in candidates:
            rr = fetch.get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{cand}")
            if rr and b"ownershipDocument" in rr.content:
                soup = BeautifulSoup(rr.content, "xml")
                break
        if soup is None:
            mark(con, "sec_form4", key, "skip", "no ownership xml")
            continue

        owner = _t(soup, "rptOwnerName")
        flags = {t.name for t in soup.find_all(["isDirector", "isOfficer", "isTenPercentOwner"])
                 if t.get_text(strip=True) in ("1", "true")}
        role = (",".join(sorted(flags)) + " " + _t(soup, "officerTitle")).strip()

        added = 0
        for tx in soup.find_all(["nonDerivativeTransaction", "derivativeTransaction"]):
            try:
                con.execute(
                    """INSERT OR IGNORE INTO insider_tx
                       (accession, ticker, filed_date, owner, role, tx_date, security,
                        code, acq_disp, shares, price, shares_after)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (acc, ticker, fdate, owner, role, _t(tx, "transactionDate"),
                     _t(tx, "securityTitle"), _t(tx, "transactionCode"),
                     _t(tx, "transactionAcquiredDisposedCode"),
                     float(_t(tx, "transactionShares") or 0) or None,
                     float(_t(tx, "transactionPricePerShare") or 0) or None,
                     float(_t(tx, "sharesOwnedFollowingTransaction") or 0) or None))
                added += 1
            except Exception:
                continue
        mark(con, "sec_form4", key, "ok", f"{owner} {added}")
        n += added
        if n % 200 == 0 and n:
            con.commit()
    con.commit()
    log(f"  {ticker}: {n} insider transactions")
    return n


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--tier", nargs="*", default=["A", "B", "C"])
    p.add_argument("--ticker")
    p.add_argument("--skip-insiders", action="store_true")
    p.add_argument("--max-form4", type=int, default=250,
                   help="cap Form 4 filings per ticker (they are 2 requests each)")
    a = p.parse_args()

    cfg = load_config()
    con = connect()
    fetch = Fetcher(cfg)
    universe = [t for t in load_universe()
                if t["tier"] in a.tier and (not a.ticker or t["ticker"] == a.ticker)]
    log(f"ingesting {len(universe)} tickers: {', '.join(t['ticker'] for t in universe)}")

    for tk in universe:
        log("-" * 60)
        log(f"TICKER {tk['ticker']} ({tk['tier']}) - {tk['name']}")
        try:
            fetch_index(con, fetch, tk)
            fetch_documents(con, fetch, cfg, tk)
            if not a.skip_insiders:
                fetch_insiders(con, fetch, tk, a.max_form4)
        except Exception as exc:
            log(f"  {tk['ticker']} FAILED: {type(exc).__name__}: {exc}")
    con.close()


if __name__ == "__main__":
    main()
