"""Query the GEV corpus.

    python ask.py search "backlog"                 full-text search across filings
    python ask.py search "hydrogen" --form 10-K    restrict to a form
    python ask.py fact Revenues                    time series for an XBRL tag
    python ask.py tags revenue                     find XBRL tags by name
    python ask.py financials                       headline annual/quarterly summary
    python ask.py insiders                         recent insider transactions
    python ask.py price                            price summary and returns
    python ask.py stats                            what is in the corpus
"""
from __future__ import annotations

import argparse
import re
import sys

from common import connect


def _fmt(v, unit=""):
    if v is None:
        return "-"
    a = abs(v)
    if unit in ("USD",) or a >= 1_000_000:
        for div, suf in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
            if a >= div:
                return f"{v/div:,.2f}{suf}"
    return f"{v:,.2f}"


def cmd_search(con, args):
    q = args.query
    # Plain queries: quote each word so hyphens, slashes and apostrophes
    # ("heavy-duty", "$/kW") are matched literally instead of parsed as
    # FTS5 syntax. Queries that already use quotes or AND/OR/NOT/* pass through.
    if not any(tok in q for tok in ('"', ' AND ', ' OR ', ' NOT ', '*', '(')):
        q = " ".join('"%s"' % w for w in q.split())
    where, params = ["chunks_fts MATCH ?"], [q]
    if args.form:
        where.append("form = ?")
        params.append(args.form)
    sql = f"""
        SELECT form, filing_date, section, accession,
               snippet(chunks_fts, 0, '>>>', '<<<', ' ... ', 28) AS snip,
               bm25(chunks_fts) AS score
        FROM chunks_fts
        WHERE {' AND '.join(where)}
        ORDER BY score LIMIT ?"""
    params.append(args.limit)
    rows = con.execute(sql, params).fetchall()
    if not rows:
        print(f"no matches for {q!r}")
        return
    print(f"{len(rows)} match(es) for {q!r}\n")
    for form, date, section, acc, snip, score in rows:
        clean = re.sub(r"\s+", " ", snip)
        print(f"--- {form}  {date}  [{section}]  score {score:.2f}")
        print(f"    {clean}\n")


def cmd_tags(con, args):
    rows = con.execute(
        """SELECT tag, label, COUNT(*) n, MIN(end_date), MAX(end_date)
           FROM xbrl_facts WHERE tag LIKE ? OR label LIKE ?
           GROUP BY tag ORDER BY n DESC LIMIT ?""",
        (f"%{args.query}%", f"%{args.query}%", args.limit)).fetchall()
    for tag, label, n, lo, hi in rows:
        print(f"{tag:<58} {n:>4} pts  {lo} -> {hi}")
        if label and label.lower() != tag.lower():
            print(f"    {label}")


def cmd_fact(con, args):
    rows = con.execute(
        """SELECT DISTINCT end_date, start_date, val, unit, fy, fp, form
           FROM xbrl_facts WHERE tag = ? AND val IS NOT NULL
           ORDER BY end_date DESC, start_date DESC LIMIT ?""",
        (args.tag, args.limit)).fetchall()
    if not rows:
        print(f"no facts for tag {args.tag!r}  (try: python ask.py tags {args.tag})")
        return
    print(f"{args.tag}\n")
    print(f"{'period':<26}{'value':>16}  {'fy/fp':<10}{'form'}")
    for end, start, val, unit, fy, fp, form in rows:
        period = f"{start} .. {end}" if start else end
        print(f"{period:<26}{_fmt(val, unit):>16}  {str(fy) + ' ' + str(fp):<10}{form}")


def cmd_financials(con, args):
    tags = [
        ("Revenue", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"]),
        ("Gross profit", ["GrossProfit"]),
        ("Operating income", ["OperatingIncomeLoss"]),
        ("Net income", ["NetIncomeLoss"]),
        ("Diluted EPS", ["EarningsPerShareDiluted"]),
        ("R&D", ["ResearchAndDevelopmentExpense"]),
        ("Cash", ["CashAndCashEquivalentsAtCarryingValue"]),
        ("Total assets", ["Assets"]),
        ("Total equity", ["StockholdersEquity"]),
    ]
    print("Annual figures (form 10-K, full-year periods)\n")
    for label, candidates in tags:
        for tag in candidates:
            rows = con.execute(
                """SELECT DISTINCT end_date, val, unit FROM xbrl_facts
                   WHERE tag=? AND form='10-K' AND val IS NOT NULL
                     AND (start_date IS NULL OR
                          CAST(julianday(end_date)-julianday(start_date) AS INT) > 300)
                   ORDER BY end_date DESC LIMIT 4""", (tag,)).fetchall()
            if rows:
                series = "  ".join(f"{e[:4]}: {_fmt(v, u):>10}" for e, v, u in rows)
                print(f"  {label:<18} {series}")
                break


def cmd_insiders(con, args):
    rows = con.execute(
        """SELECT filed_date, owner, role, tx_date, code, acq_disp, shares, price, shares_after
           FROM insider_tx WHERE shares IS NOT NULL
           ORDER BY tx_date DESC LIMIT ?""", (args.limit,)).fetchall()
    if not rows:
        print("no insider transactions ingested yet")
        return
    print(f"{'tx date':<12}{'owner':<28}{'code':<6}{'A/D':<5}{'shares':>12}{'price':>10}")
    for f, owner, role, txd, code, ad, sh, px, after in rows:
        print(f"{txd:<12}{(owner or '')[:26]:<28}{code:<6}{ad or '':<5}"
              f"{sh:>12,.0f}{(px or 0):>10,.2f}")


def cmd_price(con, args):
    row = con.execute("SELECT COUNT(*), MIN(date), MAX(date) FROM prices").fetchone()
    if not row[0]:
        print("no price data")
        return
    print(f"{row[0]} trading days, {row[1]} -> {row[2]}")
    last = con.execute("SELECT date, close FROM prices ORDER BY date DESC LIMIT 1").fetchone()
    first = con.execute("SELECT date, close FROM prices ORDER BY date ASC LIMIT 1").fetchone()
    hi = con.execute("SELECT date, MAX(close) FROM prices").fetchone()
    lo = con.execute("SELECT date, MIN(close) FROM prices").fetchone()
    print(f"  latest close   {last[1]:,.2f}  ({last[0]})")
    print(f"  first close    {first[1]:,.2f}  ({first[0]})")
    print(f"  high / low     {hi[1]:,.2f} ({hi[0]})  /  {lo[1]:,.2f} ({lo[0]})")
    print(f"  since start    {(last[1]/first[1]-1)*100:+.1f}%")
    for label, n in (("1M", 21), ("3M", 63), ("6M", 126), ("12M", 252)):
        r = con.execute("SELECT close FROM prices ORDER BY date DESC LIMIT 1 OFFSET ?",
                        (n,)).fetchone()
        if r:
            print(f"  {label:<14} {(last[1]/r[0]-1)*100:+.1f}%")


def cmd_comps(con, args):
    """Dated valuation inputs per ticker, derived from XBRL + last price."""
    from collections import defaultdict
    t = defaultdict(dict)
    for tk, m, v, d in con.execute(
            "SELECT ticker, metric, value, as_of FROM comps_inputs ORDER BY ticker, metric"):
        t[tk][m] = v
        t[tk].setdefault("as_of", d)
    cols = [("pe_fy", "P/E"), ("ev_ebit_fy", "EV/EBIT"), ("ev_ebitda_fy", "EV/EBITDA"),
            ("ev_sales_fy", "EV/Sales"), ("ps_fy", "P/S"), ("market_cap", "Mkt cap")]
    print(f"{'tick':<6}" + "".join(f"{lbl:>11}" for _, lbl in cols) + "   price date")
    for tk in sorted(t):
        line = f"{tk:<6}"
        for key, _ in cols:
            v = t[tk].get(key)
            if v is None:
                line += f"{'-':>11}"
            elif key == "market_cap":
                line += f"{v/1e9:>10.1f}B"
            else:
                line += f"{v:>10.1f}x"
        pd_ = t[tk].get("price")
        pdate = con.execute("SELECT date FROM prices WHERE ticker=? ORDER BY date DESC LIMIT 1", (tk,)).fetchone()
        print(line + f"   {pdate[0] if pdate else '-'}")
    print("\nFY = latest fiscal-year XBRL values; instants (cash, debt, shares) are the latest reported.")
    print("Derived, not vendor-adjusted - EBITDA uses reported D&A where the tag exists, else '-'.")


def cmd_backlog(con, args):
    """Backlog / deposits / cash-timing series for a ticker, XBRL spine + extracted."""
    rows = con.execute(
        """SELECT metric, as_of, value, unit, status, form FROM backlog_quarterly
           WHERE ticker=? ORDER BY metric, as_of DESC""", (args.ticker,)).fetchall()
    if not rows:
        print("no backlog rows yet - run: python src/derive.py")
        return
    cur = None
    shown = 0
    for metric, as_of, value, unit, status, form in rows:
        if metric != cur:
            cur, shown = metric, 0
            print(f"\n{metric}")
        if shown >= args.limit:
            continue
        shown += 1
        try:
            v = float(str(value).replace(",", ""))
            vs = _fmt(v, unit or "")
        except Exception:
            vs = str(value)[:28]
        print(f"   {as_of or '-':<12}{vs:>16}  {unit or '':<6} {status:<12} {form or ''}")


def cmd_generators(con, args):
    """EIA-860M: planned gas generators and MW, by monthly vintage."""
    rows = con.execute(
        """SELECT vintage, COUNT(*), COALESCE(SUM(mw),0) FROM generators
           WHERE sheet='Planned' AND (technology LIKE '%Gas%' OR technology LIKE '%Combined Cycle%'
                                      OR technology LIKE '%Combustion Turbine%')
           GROUP BY vintage ORDER BY vintage""").fetchall()
    if not rows:
        print("no EIA-860M data yet")
        return
    print(f"{'vintage':<10}{'planned gas units':>18}{'planned MW':>14}")
    for v, n, mw in rows:
        print(f"{v:<10}{n:>18}{mw:>14,.0f}")
    slip = con.execute(
        """SELECT COUNT(DISTINCT plant_id || '-' || generator_id) FROM (
             SELECT plant_id, generator_id, COUNT(DISTINCT planned_year || '-' || planned_month) c
             FROM generators WHERE sheet='Planned' AND planned_year IS NOT NULL
             GROUP BY plant_id, generator_id HAVING c > 1)""").fetchone()[0]
    print(f"\nplanned units whose planned date changed across vintages: {slip:,}")


def cmd_insights(con, args):
    rows = con.execute(
        """SELECT claim, verdict, confidence, n_support, n_oppose, falsification, catalyst_date
           FROM insights ORDER BY CASE verdict WHEN 'contested' THEN 0 WHEN 'refuted' THEN 1
                                              WHEN 'supported' THEN 2 ELSE 3 END""").fetchall()
    if not rows:
        print("no insight cards yet - run: python src/thesis.py")
        return
    for claim, verdict, conf, ns, no, fals, cat in rows:
        verdict, conf = (verdict or "unverdicted"), (conf or "-")
        print(f"[{verdict:<12}] {conf:<6} {ns} for / {no} against")
        print(f"   {claim[:150]}")
        print(f"   falsified if: {(fals or '')[:160]}")
        if cat:
            print(f"   catalyst: {cat}")
        print()
    print(f"full cards: data/INSIGHTS.md")


def cmd_catalysts(con, args):
    rows = con.execute("SELECT date, ticker, event, confirmed, source FROM catalyst_calendar ORDER BY date").fetchall()
    if not rows:
        print("no catalysts yet - run: python src/derive.py")
        return
    for d, tk, ev, conf, src in rows:
        print(f"{d}  {tk:<6} {'confirmed' if conf else 'estimated':<10} {ev[:60]}   ({src[:40]})")


def cmd_stats(con, args):
    for label, sql in [
        ("filings indexed", "SELECT COUNT(*) FROM filings"),
        ("documents", "SELECT COUNT(*) FROM documents"),
        ("chars of text", "SELECT COALESCE(SUM(n_chars),0) FROM documents"),
        ("chunks", "SELECT COUNT(*) FROM chunks"),
        ("xbrl facts", "SELECT COUNT(*) FROM xbrl_facts"),
        ("xbrl tags", "SELECT COUNT(DISTINCT tag) FROM xbrl_facts"),
        ("price days", "SELECT COUNT(*) FROM prices"),
        ("insider tx", "SELECT COUNT(*) FROM insider_tx"),
        ("news", "SELECT COUNT(*) FROM news"),
    ]:
        try:
            print(f"  {label:<18} {con.execute(sql).fetchone()[0]:,}")
        except Exception:
            print(f"  {label:<18} -")
    print("\n  by form:")
    for form, n, lo, hi in con.execute(
            """SELECT form, COUNT(*), MIN(filing_date), MAX(filing_date)
               FROM documents GROUP BY form ORDER BY COUNT(*) DESC"""):
        print(f"    {form:<12}{n:>4}   {lo} -> {hi}")


def main():
    p = argparse.ArgumentParser(description="Query the GEV corpus")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--form")
    s.add_argument("--limit", type=int, default=8); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("tags"); s.add_argument("query")
    s.add_argument("--limit", type=int, default=25); s.set_defaults(fn=cmd_tags)
    s = sub.add_parser("fact"); s.add_argument("tag")
    s.add_argument("--limit", type=int, default=24); s.set_defaults(fn=cmd_fact)
    s = sub.add_parser("financials"); s.set_defaults(fn=cmd_financials)
    s = sub.add_parser("insiders"); s.add_argument("--limit", type=int, default=25)
    s.set_defaults(fn=cmd_insiders)
    s = sub.add_parser("price"); s.set_defaults(fn=cmd_price)
    s = sub.add_parser("stats"); s.set_defaults(fn=cmd_stats)
    s = sub.add_parser("comps"); s.set_defaults(fn=cmd_comps)
    s = sub.add_parser("backlog"); s.add_argument("--ticker", default="GEV")
    s.add_argument("--limit", type=int, default=8); s.set_defaults(fn=cmd_backlog)
    s = sub.add_parser("generators"); s.set_defaults(fn=cmd_generators)
    s = sub.add_parser("insights"); s.set_defaults(fn=cmd_insights)
    s = sub.add_parser("catalysts"); s.set_defaults(fn=cmd_catalysts)

    args = p.parse_args()
    con = connect()
    try:
        args.fn(con, args)
    finally:
        con.close()


if __name__ == "__main__":
    main()
