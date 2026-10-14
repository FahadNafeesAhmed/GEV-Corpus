"""Chart definitions and plain-language notes for the GEV financials page.

Each chart is a function(ctx) -> matplotlib Figure. ctx has: q (quarterly metrics table),
s (segment table), ops (operational table), cols (quarter labels), helpers.
NOTES holds, per chart: what it is, why it matters, what to watch. Written for engineers,
not analysts. Every finance word is defined the first time it appears.
"""
import pandas as pd

BN = 1e9
C = {"Power": "#1d4e89", "Electrification": "#e8a33d", "Wind": "#2a9d8f",
     "Product": "#1d4e89", "Service": "#e8a33d", "a": "#1d4e89", "b": "#d95d39", "c": "#2a9d8f", "d": "#7b6d8d", "g": "#9aa5b1"}
SUBSEG_COLORS = {"GasPower": "#1d4e89", "NuclearPower": "#4f81bd", "HydroPower": "#8fb3e0", "SteamPower": "#bcd0ea",
                 "OnshoreWind": "#2a9d8f", "OffshoreWind": "#7fcdc3", "LMWindPower": "#bfe6e0",
                 "GridSolutions": "#e8a33d", "ElectrificationSoftware": "#f2c98a", "PowerConversionAndStorage": "#f7e0bc",
                 "PowerConversion": "#f7e0bc", "SolarAndStorageSolutions": "#fbeedb",
                 # Electrification was re-cut into these lines from 2026
                 "PowerTransmission": "#e8a33d", "GridSystemsIntegration": "#f2c98a", "GridAutomationAndSoftware": "#f7e0bc"}

SECTIONS = [
    ("How big is the business", ["revenue_mix", "segment_revenue", "subsegment_revenue"]),
    ("Is it making money", ["segment_ebitda", "segment_margin", "margins", "cost_structure", "below_the_line"]),
    ("Cash: what actually arrived", ["cash", "cash_sources", "deposits", "deposits_by_segment", "deposit_burn"]),
    ("The order book", ["rpo_split", "rpo_timing", "gas_gw", "gas_backlog"]),
    ("Quality signals", ["ltsa_revisions", "warranty", "working_capital", "restructuring"]),
    ("Balance sheet and shareholders", ["balance_sheet", "goodwill", "capital_return", "eps"]),
]

NOTES = {
    "revenue_mix": ("Revenue by quarter: equipment vs services ($B)",
        "Revenue is the money GEV bills customers in the quarter. Equipment is new turbines, transformers and grid gear. Services is maintaining the installed fleet: parts, repairs, upgrades.",
        "Services are steadier and carry higher margins. A company with half its revenue in services is less exposed to the boom-and-bust of new orders.",
        "Whether the services bar keeps growing while equipment ramps. If equipment grows and services stall, the mix gets riskier."),
    "segment_revenue": ("Revenue by segment ($B)",
        "GEV runs three segments. Power is gas, nuclear, hydro and steam turbines. Wind is onshore and offshore wind turbines. Electrification is transformers, switchgear, grid software and HVDC.",
        "Power is the profit engine and the AI story. Electrification is the fastest grower after the Prolec transformer deal. Wind loses money.",
        "The Electrification bar jumps in 2026 because Prolec was consolidated in February. Compare organic growth, not the reported jump."),
    "subsegment_revenue": ("Revenue by product line ($B)",
        "The same revenue cut one level finer, using the product lines GEV reports inside each segment.",
        "This shows what is actually growing. Gas Power is most of Power. Grid Solutions is most of Electrification. Offshore Wind is small but has produced most of the losses.",
        "Gas Power services versus Gas Power equipment, and whether Onshore Wind keeps shrinking."),
    "segment_ebitda": ("Segment EBITDA by quarter ($M)",
        "EBITDA is profit before interest, tax, depreciation and amortization. It is the closest thing to cash profit from operations. GEV reports it per segment.",
        "This is the number analysts model. Power and Electrification make money; Wind loses it every quarter.",
        "Wind must turn positive in the second half of 2026 for the company's guidance to hold. The first half lost $657M."),
    "segment_margin": ("Segment EBITDA margin (%)",
        "Margin is profit divided by revenue. A 20% margin means 20 cents of every revenue dollar is profit.",
        "Rising margin means price and volume are beating cost inflation. Falling margin during a ramp means the factory expansion is costing more than it earns yet.",
        "Power margin is guided to 17 to 19% for 2026. Whether it keeps expanding in 2027 is the central debate on the stock."),
    "margins": ("Company-wide margins (%)",
        "Gross margin is revenue minus the direct cost of making the product. Operating margin also subtracts sales, admin and R&D. Net margin is what is left after interest and tax.",
        "Three lines together show where the money goes. A wide gap between gross and operating margin means heavy overhead.",
        "Net margin spikes in Q4 2025 and Q1 2026 are one-offs: a tax benefit, and the accounting gain from revaluing GEV's old half of Prolec. Ignore them for the model."),
    "cost_structure": ("Where each revenue dollar goes (%)",
        "The cost of revenue, sales and admin, and research and development, each as a share of revenue.",
        "Operating leverage means costs grow slower than revenue, so margins expand. You can see it here directly.",
        "Cost of revenue falling as a share of revenue is the pricing story. Sales and admin should keep shrinking as a share."),
    "below_the_line": ("Interest, tax and one-offs ($M)",
        "Items between operating profit and net income: interest cost or income, income tax, restructuring charges, and income from joint ventures.",
        "These explain why net income and EBITDA move differently. GEV has net cash, so interest is income, not cost.",
        "The effective tax rate swings wildly because of one-off tax benefits. Do not use a single quarter's rate in the model."),
    "cash": ("Cash from operations, capex and free cash flow ($B)",
        "Cash from operations is real cash the business generated. Capex is cash spent on factories and equipment. Free cash flow is the difference, the cash left for shareholders.",
        "Profit is an opinion, cash is a fact. GEV's free cash flow in 2026 has been far above its profit because customers pay deposits up front.",
        "First-half 2026 free cash flow was about $9.9B. Full-year guidance is $11.5 to 12.5B, so the second half is guided to be small."),
    "cash_sources": ("Cash flow by activity ($B)",
        "The three sections of the cash flow statement: operating (the business), investing (factories and acquisitions), financing (debt, buybacks, dividends).",
        "Shows how the company uses the cash it makes. In Q1 2026 investing is deeply negative because GEV paid $5.3B for the rest of Prolec.",
        "Whether financing turns more negative as buybacks grow."),
    "deposits": ("Customer deposits vs backlog ($B)",
        "Contract liabilities are cash customers paid before GEV delivered, mostly deposits on turbine orders and slot reservations. RPO, remaining performance obligations, is the firm backlog: contracted work not yet delivered.",
        "Deposits are why cash flow is so strong right now. They are also an obligation: GEV must build what it was paid for. The percentage on each bar is deposits as a share of backlog.",
        "The ratio rising from 14% to 23% means customers are prepaying a larger slice of each order. That cash reverses only if orders get cancelled."),
    "deposits_by_segment": ("Customer deposits by segment ($B)",
        "The same deposits, split by which segment holds them.",
        "Almost all of the growth is Power, meaning gas turbine reservations and orders.",
        "Electrification deposits after Prolec, and whether Wind deposits keep shrinking."),
    "deposit_burn": ("Deposits turned into revenue each quarter ($B)",
        "Each quarter, some of the deposit balance is recognized as revenue as the work gets done. This is that amount.",
        "Compare it to the deposit inflow. When inflow is far larger than burn, the balance grows and cash flow looks great. When they converge, the cash tailwind fades.",
        "The burn rate has been about $3 to 4B per quarter while the balance grew by $8B per quarter in 2026."),
    "rpo_split": ("Backlog by type: equipment vs services ($B)",
        "RPO split into equipment (turbines and gear to build) and services (long-term maintenance contracts on the installed fleet).",
        "Services backlog is the most valuable half: long, high-margin, hard to cancel. It is also partly an estimate of future work under contracts.",
        "Equipment backlog has more than doubled in 18 months. Services backlog grows more slowly but is larger in absolute terms."),
    "rpo_timing": ("When the backlog turns into revenue (% within 1, 2, 5 years)",
        "GEV states what share of its backlog it expects to deliver within one, two and five years. Cumulative percentages, latest quarter.",
        "A backlog that is delivered later is worth less today, and it means near-term revenue is smaller than the headline suggests.",
        "The one-year share of equipment backlog has fallen from 46% to 36% since 2024. The dollar amount within one year still rose, because the total grew faster."),
    "gas_gw": ("Gas turbine gigawatts per quarter: signed, converted, shipped",
        "From the earnings press releases. Signed is new commitments, mostly slot reservations. Converted is reservations that became firm orders. Shipped is turbines that left the factory.",
        "This is the physical pipeline. Signing is easy; shipping is the constraint. GEV says annual output reaches 20 GW from the third quarter of 2026, which means about 5 GW a quarter.",
        "Shipped has been 3 to 5 GW for five quarters. The October 22 release shows whether the step to 5 GW happened."),
    "gas_backlog": ("Gas turbine backlog and slot reservations (GW)",
        "Backlog is firm gas turbine orders in gigawatts. Slot reservations are deposits that hold a place in the production line but are not yet firm orders.",
        "Together they are the '116 GW under contract' headline. Only the backlog is in RPO.",
        "Reservations are now larger than firm backlog. How fast they convert, and whether any lapse, decides how real the headline is."),
    "ltsa_revisions": ("Service-contract profit revisions ($M per quarter)",
        "GEV estimates the lifetime profit of each long-term service agreement. When it changes the estimate, the difference hits that quarter's revenue. Negative means it now expects less profit on existing contracts.",
        "This is the quality signal on the services half of the business. It sits in a footnote nobody quotes.",
        "First-half 2026 was about minus $218M, five times the first half of 2025. The nine-month number arrives around October 22."),
    "warranty": ("Warranty reserve ($B) and as % of quarterly revenue",
        "The warranty reserve is money set aside for expected repairs on products already sold.",
        "A reserve rising faster than revenue means quality problems or new products with unknown failure rates. Flat means the ramp is not hurting quality yet.",
        "The line, reserve as a share of revenue, is the one to watch during the factory ramp."),
    "working_capital": ("Inventory, receivables and contract assets ($B)",
        "Inventory is materials and unfinished turbines. Receivables is money customers owe. Contract assets is work done but not yet billable under the contract terms.",
        "Working capital is cash tied up in running the business. Inventory rising with revenue is normal; rising faster than revenue means slower turns or pre-building.",
        "Inventory has grown from about $9B to almost $13B as production ramps."),
    "restructuring": ("Restructuring charges ($M)",
        "One-off costs of closing sites, cutting jobs or exiting businesses.",
        "Large or repeated charges mean the 'one-off' is really recurring. Small and shrinking is healthy.",
        "Charges have shrunk to near zero in 2026."),
    "balance_sheet": ("Assets, liabilities and equity ($B)",
        "Total assets are everything the company owns. Total liabilities are what it owes, including customer deposits. Equity is the difference, the owners' stake.",
        "GEV's liabilities grow with deposits, which is not debt. Actual borrowing is small.",
        "Debt rose to about $2.9B in 2026 after a bond issue. Cash is larger than debt."),
    "goodwill": ("Goodwill and intangibles ($B)",
        "When a company buys another for more than the value of its physical assets, the excess is recorded as goodwill and intangibles. Intangibles are amortized, meaning expensed over years.",
        "The jump in Q1 2026 is the Prolec purchase. Amortization of Prolec intangibles is now about $180 to 240M per quarter of non-cash expense that lowers reported profit but not EBITDA.",
        "Any future write-down of goodwill would signal the acquisition underperformed."),
    "capital_return": ("Buybacks and dividends ($B)",
        "Cash returned to shareholders by buying back shares or paying dividends.",
        "Buybacks reduce the share count, which lifts earnings per share. GEV has been buying back more each quarter.",
        "Whether buybacks continue at $2B+ per quarter once the deposit cash tailwind fades."),
    "eps": ("Diluted earnings per share ($)",
        "Net income divided by the number of shares. Diluted means it includes shares that could be created by employee stock awards.",
        "This is the number the stock price is compared with. Forward P/E of about 35 means the price is 35 times next year's expected EPS.",
        "The Q1 2026 figure includes the Prolec revaluation gain and is not repeatable."),
}


def _series(ctx, metric):
    q, cols = ctx["q"], ctx["cols"]
    return pd.to_numeric(q.loc[metric, cols], errors="coerce") if metric in q.index else pd.Series([float("nan")] * len(cols), index=cols)


def _seg(ctx, concept_part, member_regex):
    s = ctx["s"]
    m = s[s["concept"].str.contains(concept_part) & s["member"].str.contains(member_regex, regex=True)]
    if not len(m):
        return pd.Series([float("nan")] * len(ctx["cols"]), index=ctx["cols"])
    return pd.to_numeric(m[ctx["cols"]].sum(min_count=1), errors="coerce")


def revenue_mix(ctx):
    fig, ax, bars = ctx["new"](); cols = ctx["cols"]
    p = _seg(ctx, "RevenueFromContract", r"^OperatingSegments;Product$") / BN
    sv = _seg(ctx, "RevenueFromContract", r"^OperatingSegments;Service$") / BN
    bars(ax, p, "Equipment", C["Product"]); bars(ax, sv, "Services", C["Service"], bottom=p.fillna(0))
    ctx["label_last"](ax, p + sv.fillna(0), "$%.1fB"); ax.legend(frameon=False); return fig


def segment_revenue(ctx):
    fig, ax, bars = ctx["new"](); bottom = pd.Series(0.0, index=ctx["cols"])
    for seg in ("Power", "Electrification", "Wind"):
        v = (_seg(ctx, "RevenueFromContract", r"^OperatingSegmentsExcludingIntersegmentElimination;%sSegment$" % seg) / BN).fillna(0)
        bars(ax, v, seg, C[seg], bottom=bottom); bottom = bottom + v
    ctx["label_last"](ax, bottom, "$%.1fB"); ax.legend(frameon=False); return fig


def subsegment_revenue(ctx):
    fig, ax, bars = ctx["new"](height=5.2); bottom = pd.Series(0.0, index=ctx["cols"])
    for name, color in SUBSEG_COLORS.items():
        v = (_seg(ctx, "RevenueFromContract", r"SubsegmentsAxis=%s$" % name) / BN).fillna(0)
        if v.sum() == 0:
            continue
        bars(ax, v, name, color, bottom=bottom); bottom = bottom + v
    ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0)); return fig


def segment_ebitda(ctx):
    fig, ax, _ = ctx["new"](); cols = ctx["cols"]; w = 0.26
    for i, seg in enumerate(("Power", "Electrification", "Wind")):
        v = _seg(ctx, "BeforeIncomeTaxesInterestAndDebtExpense", r"^OperatingSegments;%sSegment$" % seg) / 1e6
        ax.bar([j + (i - 1) * w for j in range(len(cols))], v.values, width=w, label=seg, color=C[seg])
    ctx["xticks"](ax); ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def segment_margin(ctx):
    fig, ax, _ = ctx["new"]()
    for seg in ("Power", "Electrification", "Wind"):
        e = _seg(ctx, "BeforeIncomeTaxesInterestAndDebtExpense", r"^OperatingSegments;%sSegment$" % seg)
        r = _seg(ctx, "RevenueFromContract", r"^OperatingSegmentsExcludingIntersegmentElimination;%sSegment$" % seg)
        ctx["line"](ax, e / r * 100, seg, C[seg])
    ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def margins(ctx):
    fig, ax, _ = ctx["new"](); rev = _series(ctx, "Revenues")
    for m, lab, c in (("GrossProfit", "Gross margin", C["a"]), ("OperatingIncome", "Operating margin", C["b"]), ("NetIncome", "Net margin", C["c"])):
        ctx["line"](ax, _series(ctx, m) / rev * 100, lab, c)
    ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def cost_structure(ctx):
    fig, ax, _ = ctx["new"](); rev = _series(ctx, "Revenues")
    for m, lab, c in (("CostOfRevenue", "Cost of revenue", C["a"]), ("SGA", "Sales and admin", C["b"]), ("R&D", "R&D", C["c"])):
        ctx["line"](ax, _series(ctx, m) / rev * 100, lab, c)
    ax.legend(frameon=False); return fig


def below_the_line(ctx):
    fig, ax, _ = ctx["new"]()
    for m, lab, c in (("InterestExpense", "Interest (negative = income)", C["a"]), ("IncomeTax", "Income tax", C["b"]),
                      ("RestructuringCharges", "Restructuring", C["d"]), ("EquityMethodIncome", "Joint-venture income", C["c"])):
        ctx["line"](ax, _series(ctx, m) / 1e6, lab, c)
    ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False, fontsize=8); return fig


def cash(ctx):
    fig, ax, bars = ctx["new"](); cfo = _series(ctx, "CashFromOps") / BN; capex = _series(ctx, "Capex") / BN
    bars(ax, cfo, "Cash from operations", C["a"]); bars(ax, -capex, "Capex", C["b"])
    ctx["line"](ax, cfo - capex, "Free cash flow", "black"); ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def cash_sources(ctx):
    fig, ax, _ = ctx["new"](); cols = ctx["cols"]; w = 0.26
    for i, (m, lab, c) in enumerate((("CashFromOps", "Operating", C["a"]), ("CashInvesting", "Investing", C["b"]), ("CashFinancing", "Financing", C["c"]))):
        ax.bar([j + (i - 1) * w for j in range(len(cols))], (_series(ctx, m) / BN).values, width=w, label=lab, color=c)
    ctx["xticks"](ax); ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def deposits(ctx):
    fig, ax, bars = ctx["new"](); cl = _series(ctx, "ContractLiabilities") / BN; rpo = _series(ctx, "RPO") / BN
    bars(ax, cl, "Customer deposits", C["a"]); ax2 = ax.twinx(); ax2.spines[["top"]].set_visible(False)
    ax2.plot(range(len(cl)), rpo.values, marker="o", color=C["b"], label="Backlog, RPO (right axis)"); ax2.set_ylabel("RPO $B")
    for i, (v, r) in enumerate(zip(cl.values, rpo.values)):
        if pd.notna(v) and pd.notna(r):
            ax.annotate("%.0f%%" % (v / r * 100), (i, v), ha="center", va="bottom", fontsize=8)
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1 + h2, l1 + l2, frameon=False, loc="upper left"); return fig


def deposits_by_segment(ctx):
    fig, ax, bars = ctx["new"](); bottom = pd.Series(0.0, index=ctx["cols"])
    for seg in ("Power", "Electrification", "Wind"):
        v = (_seg(ctx, "^ContractWithCustomerLiability$", r"^%sSegment$" % seg) / BN).fillna(0)
        bars(ax, v, seg, C[seg], bottom=bottom); bottom = bottom + v
    ax.legend(frameon=False); return fig


def deposit_burn(ctx):
    fig, ax, bars = ctx["new"](); bars(ax, _series(ctx, "DepositsRecognizedAsRevenue") / BN, "Deposits recognized as revenue", C["a"])
    cl = _series(ctx, "ContractLiabilities") / BN
    ctx["line"](ax, cl.diff(), "Change in deposit balance", C["b"]); ax.axhline(0, color="black", linewidth=0.8); ax.legend(frameon=False); return fig


def rpo_split(ctx):
    fig, ax, bars = ctx["new"](); p = _seg(ctx, "RemainingPerformance", r"^Product$") / BN; sv = _seg(ctx, "RemainingPerformance", r"^Service$") / BN
    bars(ax, p, "Equipment backlog", C["Product"]); bars(ax, sv, "Services backlog", C["Service"], bottom=p.fillna(0))
    ctx["label_last"](ax, p + sv.fillna(0), "$%.0fB"); ax.legend(frameon=False); return fig


def rpo_timing(ctx):
    fig, ax, _ = ctx["new"](); cols = ctx["cols"]; keys = (("One", "1 year"), ("Two", "2 years"), ("Three", "5 years"))
    for kind, c in (("Product", C["Product"]), ("Service", C["Service"])):
        for (k, lab), ls in zip(keys, ("-", "--", ":")):
            v = _seg(ctx, "RemainingPerformance", r"^%s;PerformanceObligationSatisfactionPeriodAxis=PerformanceObligationSatisfactionPeriod%s;" % (kind, k)) * 100
            ax.plot(range(len(cols)), v.values, marker="o", linestyle=ls, color=c, label="%s within %s" % ("Equipment" if kind == "Product" else "Services", lab))
    ctx["xticks"](ax); ax.set_ylim(0, 105); ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0)); return fig


def gas_gw(ctx):
    fig, ax, _ = ctx["new"](); ops = ctx["ops"]; cols = [c for c in ctx["cols"] if c in ops.columns]; w = 0.26
    for i, (m, lab, c) in enumerate((("gas_gw_signed", "Signed (mostly reservations)", C["g"]), ("gas_gw_converted", "Converted to firm orders", C["a"]), ("gas_gw_shipped", "Shipped", C["b"]))):
        v = pd.to_numeric(ops.loc[m, cols], errors="coerce") if m in ops.index else pd.Series(index=cols, dtype=float)
        ax.bar([j + (i - 1) * w for j in range(len(cols))], v.values, width=w, label=lab, color=c)
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=45, ha="right", fontsize=9); ax.axhline(5, color="black", linestyle=":", linewidth=1)
    ax.annotate("5 GW per quarter = the 20 GW/yr target", (len(cols) - 0.5, 5.15), fontsize=8, ha="right"); ax.legend(frameon=False); return fig


def gas_backlog(ctx):
    fig, ax, _ = ctx["new"](); ops = ctx["ops"]; cols = [c for c in ctx["cols"] if c in ops.columns]
    for m, lab, c in (("gas_backlog_gw_end", "Firm backlog (GW)", C["a"]), ("gas_sra_gw_end", "Slot reservations (GW)", C["g"])):
        v = pd.to_numeric(ops.loc[m, cols], errors="coerce") if m in ops.index else pd.Series(index=cols, dtype=float)
        ax.plot(range(len(cols)), v.values, marker="o", label=lab, color=c, linewidth=2)
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=45, ha="right", fontsize=9); ax.legend(frameon=False); return fig


def ltsa_revisions(ctx):
    fig, ax, bars = ctx["new"](); v = _series(ctx, "LTSA_ProfitRevision") / 1e6
    bars(ax, v, "Change in estimated service-contract profit", [C["b"] if x < 0 else C["c"] for x in v.fillna(0)])
    ax.axhline(0, color="black", linewidth=0.8); ctx["label_last"](ax, v, "%.0fM"); ax.legend(frameon=False); return fig


def warranty(ctx):
    fig, ax, bars = ctx["new"](); w = _series(ctx, "WarrantyAccrual") / BN; bars(ax, w, "Warranty reserve", C["a"])
    ax2 = ax.twinx(); ax2.spines[["top"]].set_visible(False)
    ax2.plot(range(len(w)), (w / (_series(ctx, "Revenues") / BN) * 100).values, marker="o", color=C["b"], label="% of quarterly revenue (right)"); ax2.set_ylabel("percent")
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1 + h2, l1 + l2, frameon=False, loc="upper left"); return fig


def working_capital(ctx):
    fig, ax, _ = ctx["new"]()
    for m, lab, c in (("Inventory", "Inventory", C["a"]), ("Receivables", "Receivables", C["b"]), ("ContractAssets", "Contract assets", C["c"])):
        ctx["line"](ax, _series(ctx, m) / BN, lab, c)
    ax.legend(frameon=False); return fig


def restructuring(ctx):
    fig, ax, bars = ctx["new"](); bars(ax, _series(ctx, "RestructuringCharges") / 1e6, "Restructuring charges", C["d"]); ax.axhline(0, color="black", linewidth=0.8); return fig


def balance_sheet(ctx):
    fig, ax, _ = ctx["new"]()
    for m, lab, c in (("TotalAssets", "Total assets", C["a"]), ("TotalLiabilities", "Total liabilities", C["b"]), ("Equity", "Equity", C["c"]), ("Cash", "Cash", C["d"]), ("DebtIncludingCurrent", "Debt", C["g"])):
        ctx["line"](ax, _series(ctx, m) / BN, lab, c)
    ax.legend(frameon=False, ncol=3, fontsize=8); return fig


def goodwill(ctx):
    fig, ax, bars = ctx["new"](); g = _series(ctx, "Goodwill") / BN; i = _series(ctx, "Intangibles") / BN
    bars(ax, g, "Goodwill", C["a"]); bars(ax, i, "Intangibles", C["b"], bottom=g.fillna(0)); ax.legend(frameon=False); return fig


def capital_return(ctx):
    fig, ax, bars = ctx["new"](); b = _series(ctx, "Buybacks") / BN; d = _series(ctx, "Dividends") / BN
    bars(ax, b, "Buybacks", C["a"]); bars(ax, d, "Dividends", C["c"], bottom=b.fillna(0)); ctx["label_last"](ax, b + d.fillna(0), "$%.1fB"); ax.legend(frameon=False); return fig


def eps(ctx):
    fig, ax, bars = ctx["new"](); bars(ax, _series(ctx, "EPS_diluted"), "Diluted EPS", C["a"]); ax.axhline(0, color="black", linewidth=0.8); return fig


CHARTS = {name: globals()[name] for section in SECTIONS for name in section[1]}
