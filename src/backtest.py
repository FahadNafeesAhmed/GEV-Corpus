"""Event study over corpus-derived signals.

    python backtest.py --signal filing --ticker GEV
    python backtest.py --signal insider_buy --ticker GEV
    python backtest.py --signal all

What this does: for each event date, measure the forward return over the next
1/5/21/63 trading days, market-adjusted against SPY, and report the distribution.

What this does NOT do: tell you a signal works. With one ticker and two years of
history you have roughly thirty events. Thirty is not a sample, it is an anecdote
with error bars. Every result below prints its own n and a verdict that says so.
"""
from __future__ import annotations

import argparse
import math
import statistics as stats

from common import Fetcher, connect, load_config, log

HORIZONS = [1, 5, 21, 63]
BENCH = "SPY"
YAHOO = ("https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
         "?range=10y&interval=1d")
BROWSER_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Below this many events, report the distribution but refuse to call it a result.
MIN_N_FOR_A_CLAIM = 30


def ensure_benchmark(con, fetch: Fetcher) -> bool:
    have = con.execute("SELECT COUNT(*) FROM prices WHERE ticker=?", (BENCH,)).fetchone()[0]
    if have > 200:
        return True
    import time as _t
    r = fetch.get(YAHOO.format(sym=BENCH), headers=BROWSER_UA)
    if not r:
        log(f"could not fetch {BENCH}; falling back to raw (unadjusted) returns")
        return False
    try:
        res = r.json()["chart"]["result"][0]
        ts, q = res["timestamp"], res["indicators"]["quote"][0]
    except Exception:
        return False
    for i, epoch in enumerate(ts):
        if q["close"][i] is None:
            continue
        con.execute("INSERT OR REPLACE INTO prices(ticker,date,open,high,low,close,volume) "
                    "VALUES (?,?,?,?,?,?,?)",
                    (BENCH, _t.strftime("%Y-%m-%d", _t.gmtime(epoch)), q["open"][i],
                     q["high"][i], q["low"][i], q["close"][i], q["volume"][i]))
    con.commit()
    log(f"benchmark {BENCH}: {con.execute('SELECT COUNT(*) FROM prices WHERE ticker=?',(BENCH,)).fetchone()[0]} days")
    return True


def series(con, ticker: str):
    rows = con.execute("SELECT date, close FROM prices WHERE ticker=? ORDER BY date",
                       (ticker,)).fetchall()
    return [r[0] for r in rows], [r[1] for r in rows]


def fwd_return(dates, closes, idx_of, event_date, horizon):
    """Return over `horizon` trading days starting at the first session on/after the event."""
    i = idx_of.get(event_date)
    if i is None:                       # event fell on a non-trading day
        later = [d for d in dates if d >= event_date]
        if not later:
            return None
        i = idx_of[later[0]]
    j = i + horizon
    if j >= len(closes) or closes[i] in (None, 0):
        return None
    return closes[j] / closes[i] - 1.0


def collect_events(con, signal: str, ticker: str):
    if signal == "filing":
        return con.execute(
            """SELECT filing_date, form FROM filings
               WHERE ticker=? AND form IN ('10-K','10-Q','8-K') ORDER BY filing_date""",
            (ticker,)).fetchall()
    if signal == "earnings_8k":
        return con.execute(
            """SELECT filing_date, 'earnings-8K' FROM filings
               WHERE ticker=? AND form='8-K' ORDER BY filing_date""", (ticker,)).fetchall()
    if signal == "insider_buy":
        # Code 'P' is an open-market purchase - the only insider code with much signal.
        return con.execute(
            """SELECT tx_date, 'insider-buy' FROM insider_tx
               WHERE ticker=? AND code='P' AND shares > 0
               GROUP BY tx_date ORDER BY tx_date""", (ticker,)).fetchall()
    if signal == "insider_sell":
        return con.execute(
            """SELECT tx_date, 'insider-sell' FROM insider_tx
               WHERE ticker=? AND code='S' AND shares > 0
               GROUP BY tx_date ORDER BY tx_date""", (ticker,)).fetchall()
    if signal == "guidance":
        return con.execute(
            """SELECT DISTINCT filing_date, 'guidance-present' FROM guidance
               WHERE ticker=? ORDER BY filing_date""", (ticker,)).fetchall()
    raise SystemExit(f"unknown signal {signal!r}")


def describe(name: str, rets: list[float]) -> None:
    n = len(rets)
    if n == 0:
        print(f"    {name:<10}  no observations")
        return
    mean = stats.fmean(rets)
    med = stats.median(rets)
    sd = stats.stdev(rets) if n > 1 else 0.0
    hit = sum(1 for r in rets if r > 0) / n
    t = mean / (sd / math.sqrt(n)) if sd > 0 and n > 1 else float("nan")
    print(f"    {name:<10} n={n:<4} mean={mean*100:+6.2f}%  med={med*100:+6.2f}%  "
          f"sd={sd*100:5.2f}%  hit={hit*100:4.0f}%  t={t:+5.2f}")


def baseline(dates, closes, idx, bdates, bcloses, bidx, horizon, adjusted):
    """The null hypothesis: enter on EVERY trading day, hold the same horizon.

    Without this control an event study on a stock that trended hard will show a
    huge 'edge' for any event that happens regularly - you are measuring drift,
    not information. A signal only matters if it beats this.
    """
    out = []
    for d in dates:
        r = fwd_return(dates, closes, idx, d, horizon)
        if r is None:
            continue
        if adjusted:
            b = fwd_return(bdates, bcloses, bidx, d, horizon)
            if b is None:
                continue
            r -= b
        out.append(r)
    return out


def run_signal(con, signal: str, ticker: str, adjusted: bool):
    events = collect_events(con, signal, ticker)
    dates, closes = series(con, ticker)
    idx = {d: i for i, d in enumerate(dates)}
    bdates, bcloses = series(con, BENCH) if adjusted else ([], [])
    bidx = {d: i for i, d in enumerate(bdates)}

    print(f"\n  SIGNAL: {signal}   ticker={ticker}   events={len(events)}"
          f"   returns={'market-adjusted vs SPY' if adjusted else 'raw'}")
    if not events:
        print("    (no events)")
        return

    for h in HORIZONS:
        rets = []
        for edate, _label in events:
            r = fwd_return(dates, closes, idx, edate, h)
            if r is None:
                continue
            if adjusted:
                b = fwd_return(bdates, bcloses, bidx, edate, h)
                if b is None:
                    continue
                r -= b
            rets.append(r)
        describe(f"{h}d", rets)

        base = baseline(dates, closes, idx, bdates, bcloses, bidx, h, adjusted)
        describe(f"  base {h}d", base)
        if rets and base:
            edge = stats.fmean(rets) - stats.fmean(base)
            # Welch-style standard error on the difference of two means.
            sa = stats.stdev(rets) if len(rets) > 1 else 0.0
            sb = stats.stdev(base) if len(base) > 1 else 0.0
            se = math.sqrt(sa ** 2 / max(len(rets), 1) + sb ** 2 / max(len(base), 1))
            tt = edge / se if se > 0 else float("nan")
            verdict = "beats baseline" if abs(tt) > 2 else "indistinguishable from baseline"
            print(f"    {'EDGE':<10} {edge*100:+6.2f}% vs baseline   t={tt:+5.2f}   -> {verdict}")
        print()

    n = len(events)
    if n < MIN_N_FOR_A_CLAIM:
        print(f"    VERDICT: n={n} is too small to support any claim. Treat the numbers")
        print(f"             above as description, not evidence. Need n>={MIN_N_FOR_A_CLAIM}")
        print(f"             before a t-stat means anything - add tickers, not horizons.")
    else:
        print(f"    VERDICT: n={n} is a usable sample. A |t| above ~2 is worth a second look,")
        print(f"             but you are testing several horizons, so discount accordingly.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--signal", nargs="*",
                   default=["filing", "insider_buy", "insider_sell", "guidance"])
    p.add_argument("--ticker", default="GEV")
    a = p.parse_args()

    con = connect()
    fetch = Fetcher(load_config())
    adjusted = ensure_benchmark(con, fetch)

    print("=" * 78)
    print(f"EVENT STUDY  -  {a.ticker}")
    print("=" * 78)
    for sig in a.signal:
        run_signal(con, sig, a.ticker, adjusted)
    print("\n" + "=" * 78)
    con.close()


if __name__ == "__main__":
    main()
