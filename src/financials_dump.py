"""Dump GE Vernova's reported financials from SEC XBRL into CSV via edgartools.

Walks every 10-K and 10-Q, reads the XBRL attached to each filing, and writes:
  data/financials/gev_facts_long.csv    one row per (concept, dimension, period)
  data/financials/gev_quarterly.csv     key metrics, one column per quarter
  data/financials/gev_segments.csv      segment revenue / EBITDA by quarter

Usage:  python src/financials_dump.py [TICKER]
"""
import json
import re
import sys
from pathlib import Path

import pandas as pd
from edgar import Company, set_identity

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "financials"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Concepts we want on the tidy quarterly sheet (us-gaap or GEV custom tags).
KEY = {
    "Revenues": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax", "us-gaap:Revenues"],
    "CostOfRevenue": ["us-gaap:CostOfRevenue", "us-gaap:CostOfGoodsAndServicesSold"],
    "GrossProfit": ["us-gaap:GrossProfit"],
    "SGA": ["us-gaap:SellingGeneralAndAdministrativeExpense"],
    "R&D": ["us-gaap:ResearchAndDevelopmentExpense"],
    "OperatingIncome": ["us-gaap:OperatingIncomeLoss"],
    "NetIncome": ["us-gaap:NetIncomeLoss", "us-gaap:ProfitLoss"],
    "EPS_diluted": ["us-gaap:EarningsPerShareDiluted"],
    "CashFromOps": ["us-gaap:NetCashProvidedByUsedInOperatingActivities"],
    "Capex": ["us-gaap:PaymentsToAcquirePropertyPlantAndEquipment"],
    "Cash": ["us-gaap:CashAndCashEquivalentsAtCarryingValue"],
    "Inventory": ["us-gaap:InventoryNet"],
    "Receivables": ["us-gaap:AccountsReceivableNetCurrent", "us-gaap:ReceivablesNetCurrent"],
    "ContractAssets": ["us-gaap:ContractWithCustomerAssetNetCurrent", "us-gaap:ContractWithCustomerAssetNet"],
    "ContractLiabilities": ["us-gaap:ContractWithCustomerLiabilityCurrent", "us-gaap:ContractWithCustomerLiability"],
    "ContractLiabilitiesNoncurrent": ["us-gaap:ContractWithCustomerLiabilityNoncurrent"],
    "WarrantyAccrual": ["us-gaap:StandardProductWarrantyAccrual"],
    "TotalAssets": ["us-gaap:Assets"],
    "TotalDebt": ["us-gaap:LongTermDebt", "us-gaap:LongTermDebtNoncurrent"],
    "Equity": ["us-gaap:StockholdersEquity"],
    "SharesDiluted": ["us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding"],
    "Buybacks": ["us-gaap:PaymentsForRepurchaseOfCommonStock"],
    "Dividends": ["us-gaap:PaymentsOfDividends", "us-gaap:PaymentsOfDividendsCommonStock"],
    "RPO": ["us-gaap:RevenueRemainingPerformanceObligation"],
    "InterestExpense": ["gev:InterestAndOtherFinancialCharges", "us-gaap:InterestExpense"],
    "PretaxIncome": ["us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"],
    "IncomeTax": ["us-gaap:IncomeTaxExpenseBenefit"],
    "EffectiveTaxRate": ["us-gaap:EffectiveIncomeTaxRateContinuingOperations"],
    "DepreciationAmortization": ["gev:DepreciationDepletionAndAmortizationIncludingImpairments", "us-gaap:DepreciationDepletionAndAmortization"],
    "IntangibleAmortization": ["us-gaap:AmortizationOfIntangibleAssets"],
    "Goodwill": ["us-gaap:Goodwill"],
    "Intangibles": ["us-gaap:IntangibleAssetsNetExcludingGoodwill"],
    "CurrentAssets": ["us-gaap:AssetsCurrent"],
    "CurrentLiabilities": ["us-gaap:LiabilitiesCurrent"],
    "TotalLiabilities": ["us-gaap:Liabilities"],
    "DebtIncludingCurrent": ["us-gaap:LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities"],
    "CashInvesting": ["us-gaap:NetCashProvidedByUsedInInvestingActivities"],
    "CashFinancing": ["us-gaap:NetCashProvidedByUsedInFinancingActivities"],
    "DebtIssued": ["us-gaap:ProceedsFromIssuanceOfLongTermDebt"],
    "RestructuringCharges": ["us-gaap:RestructuringCharges"],
    "EquityMethodIncome": ["us-gaap:IncomeLossFromEquityMethodInvestments"],
    "LTSA_ProfitRevision": ["gev:ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInEstimatedProfitability"],
    "LTSA_ProgressRevision": ["us-gaap:ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress"],
    "LTSA_Billings": ["gev:ContractWithCustomerAssetBillings"],
    "LTSA_RevenueRecognized": ["gev:ContractWithCustomerAssetRevenuesRecognized"],
    "DepositsRecognizedAsRevenue": ["us-gaap:ContractWithCustomerLiabilityRevenueRecognized"],
    "OperatingLeaseLiability": ["us-gaap:OperatingLeaseLiability"],
}
# Operational numbers GEV states only in words in its earnings press releases (8-K exhibits).
OPS_PATTERNS = {
    "gas_gw_shipped": r"shipped\s+(\d+(?:\.\d+)?)\s*(?:GW|gigawatts?)",
    "gas_gw_signed": r"[Ss]\s?igned\s+(?:just over\s+)?(\d+(?:\.\d+)?)\s*(?:GW|gigawatts?)",
    "gas_gw_converted": r"[Cc]onverted\s+(\d+(?:\.\d+)?)\s*(?:GW|gigawatts?)",
    "gas_backlog_gw_end": r"backlog\s+(?:growth|grew|remaining)?\s*(?:from\s+\d+\s*(?:GW\s*)?to\s+|at\s+)(\d+)\s*(?:GW|gigawatts?)",
    "gas_sra_gw_end": r"slot reservation agreements?\s+from\s+\d+\s*(?:GW\s*)?to\s+(\d+)\s*(?:GW|gigawatts?)",
}
SEG_AXES = ("StatementBusinessSegmentsAxis", "ProductOrServiceAxis")
# Per-share and share-count metrics are not additive: never difference YTD spans for them.
RATE_METRICS = {"EPS_diluted", "SharesDiluted"}


def load_identity():
    cfg = ROOT / "config" / "config.json"
    ua = json.load(open(cfg))["sec_user_agent"] if cfg.exists() else "research bot research@example.com"
    set_identity(ua)


def facts_for(filing):
    """All numeric facts in a filing's XBRL as a long dataframe."""
    xb = filing.xbrl()
    df = xb.facts.query().to_dataframe()
    keep = ["concept", "label", "numeric_value", "period_start", "period_end", "period_instant",
            "period_type", "is_dimensioned", "unit_ref", "fiscal_period", "fiscal_year", "context_ref"]
    df = df[[c for c in keep if c in df.columns]].copy()
    df = df[df["numeric_value"].notna()]
    # Dimension members live on the context; edgartools exposes them via xb.contexts
    dims = {}
    try:
        for cid, ctx in xb.contexts.items():
            d = getattr(ctx, "dimensions", None) or {}
            dims[cid] = ";".join("%s=%s" % (k.split(":")[-1], str(v).split(":")[-1]) for k, v in d.items())
    except Exception:
        pass
    df["dimension"] = df["context_ref"].map(dims).fillna("")
    df["form"] = filing.form
    df["filed"] = str(filing.filing_date)
    df["accession"] = filing.accession_no
    return df


def span(row):
    """Classify a fact's period: ('Q2 2026', 3) for a quarter, ('2026', 6/9/12) for YTD spans,
    or ('Q2 2026', 0) for an instant (balance-sheet) value."""
    if row["period_type"] == "instant":
        end = pd.Timestamp(row["period_instant"])
        return "Q%d %d" % ((end.month - 1) // 3 + 1, end.year), 0
    start, end = pd.Timestamp(row["period_start"]), pd.Timestamp(row["period_end"])
    months = round((end - start).days / 30.4)
    q = (end.month - 1) // 3 + 1
    if months == 3:
        return "Q%d %d" % (q, end.year), 3
    if months in (6, 9, 12) and q * 3 == months:
        return "Q%d %d" % (q, end.year), months
    return None, None


def period_label(row):
    return span(row)[0]


def tidy(long):
    """One column per quarter. Flow metrics that filings only report year-to-date
    (cash flow, Q4 of everything) are derived by differencing the YTD values."""
    rows = []
    for name, tags in KEY.items():
        sub = long[long["concept"].isin(tags) & (long["dimension"] == "")].copy()
        if sub.empty:
            continue
        sub[["period", "months"]] = sub.apply(lambda r: pd.Series(span(r)), axis=1)
        sub = sub.dropna(subset=["period"]).sort_values("filed")
        vals = {}  # (period, months) -> value, latest filing wins
        for _, r in sub.iterrows():
            vals[(r["period"], int(r["months"]))] = r["numeric_value"]
        if name in RATE_METRICS:
            vals = {k: v for k, v in vals.items() if k[1] in (0, 3, 12)}
            quarters = {p: v for p, v in quarterize(vals).items() if (p, 3) in vals or (p, 0) in vals or p.startswith("FY")}
        else:
            quarters = quarterize(vals)
        for p, v in quarters.items():
            rows.append({"metric": name, "period": p, "value": v})
    t = pd.DataFrame(rows)
    return t.pivot_table(index="metric", columns="period", values="value", aggfunc="last")


def quarterize(vals):
    """vals: {(period, months): value} -> {period_or_FY: quarterly value}, differencing YTD spans."""
    out = {}
    for p in sorted({p for p, _ in vals}, key=lambda p: (int(p[3:]), int(p[1]))):
        q, yr = int(p[1]), p[3:]
        if (p, 0) in vals:
            v = vals[(p, 0)]
        elif (p, 3) in vals:
            v = vals[(p, 3)]
        else:
            ytd = vals.get((p, q * 3))
            prev = vals.get(("Q%d %s" % (q - 1, yr), (q - 1) * 3)) if q > 1 else 0.0
            v = ytd - prev if ytd is not None and prev is not None else None
        if v is not None:
            out[p] = v
        if (p, 12) in vals:
            out["FY" + yr] = vals[(p, 12)]
    return out


def segments(long):
    sub = long[long["dimension"].str.contains("|".join(SEG_AXES), regex=True)].copy()
    # GEV tags segment EBITDA as IncomeLossFromContinuingOperationsBeforeIncomeTaxesInterestAndDebtExpense...
    sub = sub[sub["concept"].str.contains(
        "RevenueFromContract|BeforeIncomeTaxesInterestAndDebtExpense|ContractWithCustomerLiability|SegmentExpenditureAddition"
        "|RemainingPerformanceObligation|^us-gaap:Goodwill$", regex=True)]
    sub[["period", "months"]] = sub.apply(lambda r: pd.Series(span(r)), axis=1)
    sub = sub.dropna(subset=["period"]).sort_values("filed")
    sub["member"] = (sub["dimension"].str.replace("Member", "").str.replace("StatementBusinessSegmentsAxis=", "")
                     .str.replace("ProductOrServiceAxis=", "").str.replace("ConsolidationItemsAxis=", ""))
    rows = []
    for (concept, member), g in sub.groupby(["concept", "member"]):
        vals = {(r["period"], int(r["months"])): r["numeric_value"] for _, r in g.iterrows()}
        for p, v in quarterize(vals).items():
            rows.append({"concept": concept.split(":")[-1], "member": member, "period": p, "value": v})
    t = pd.DataFrame(rows)
    return t.pivot_table(index=["concept", "member"], columns="period", values="value", aggfunc="last")


def operational(ticker):
    """Regex the quarterly earnings press releases in the corpus for gas-turbine GW figures."""
    import sqlite3
    db = ROOT / "data" / "gev.db"
    if not db.exists():
        return pd.DataFrame()
    con = sqlite3.connect(db)
    rows = []
    q = """SELECT filing_date, text FROM documents WHERE ticker=? AND form='8-K/EX'
           AND (text LIKE '%shipped%GW%' OR text LIKE '%shipped%gigawatt%') ORDER BY filing_date"""
    for filing_date, text in con.execute(q, (ticker,)):
        d = pd.Timestamp(filing_date)
        # a release filed in month m reports the quarter that ended the month before
        qend = d - pd.offsets.MonthBegin(1) - pd.Timedelta(days=1)
        period = "Q%d %d" % ((qend.month - 1) // 3 + 1, qend.year)
        for name, pat in OPS_PATTERNS.items():
            m = re.search(pat, text)
            if m:
                rows.append({"metric": name, "period": period, "value": float(m.group(1)), "source": "8-K/EX " + filing_date})
    if not rows:
        return pd.DataFrame()
    t = pd.DataFrame(rows).drop_duplicates(["metric", "period"], keep="last")
    return t.pivot_table(index="metric", columns="period", values="value", aggfunc="last")


def order_cols(df):
    def key(c):
        m = re.match(r"Q(\d) (\d{4})", c)
        if m:
            return (int(m.group(2)), int(m.group(1)))
        m = re.match(r"FY(\d{4})", c)
        return (int(m.group(1)), 9) if m else (0, 0)
    return df[sorted(df.columns, key=key)]


def main(ticker="GEV"):
    load_identity()
    OUT.mkdir(parents=True, exist_ok=True)
    company = Company(ticker)
    filings = company.get_filings(form=["10-K", "10-Q"])
    frames = []
    for f in filings:
        try:
            df = facts_for(f)
            frames.append(df)
            print("ok   %s %s  %6d facts" % (f.form, f.filing_date, len(df)))
        except Exception as e:  # keep going; one bad filing must not kill the dump
            print("skip %s %s  %s" % (f.form, f.filing_date, str(e)[:120]))
    long = pd.concat(frames, ignore_index=True)
    long.to_csv(OUT / ("%s_facts_long.csv" % ticker.lower()), index=False)
    q = order_cols(tidy(long))
    q.to_csv(OUT / ("%s_quarterly.csv" % ticker.lower()))
    s = order_cols(segments(long))
    s.to_csv(OUT / ("%s_segments.csv" % ticker.lower()))
    ops = operational(ticker)
    if len(ops):
        ops = order_cols(ops)
        ops.to_csv(OUT / ("%s_operational.csv" % ticker.lower()))
        print("operational rows:", len(ops)); print(ops.to_string())
    print("\nwrote %d long rows, %d tidy metrics x %d periods, %d segment rows -> %s"
          % (len(long), len(q), len(q.columns), len(s), OUT))
    print(q.to_string(max_cols=12, float_format=lambda v: "%.3g" % v))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "GEV")
