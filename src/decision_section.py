"""The decision section of the page: the market-side briefing and the long/short decision.

Renders the consensus baseline, the corrections, positioning, the sixteen cases and how each
died, the kill conditions, and the honest caveat on Pillar 1. Used by financials_charts.py.
"""
import html

import matplotlib.pyplot as plt
import numpy as np

C = ["#1d4e89", "#e8a33d", "#2a9d8f", "#d95d39", "#7b6d8d", "#9aa5b1", "#4f81bd", "#f2c98a"]
PRICE = 950.28

INTRO = (
    "Two further runs closed the research out: a 31-agent sweep of everything that is not a filing (what the Street expects, "
    "who owns the stock, what the bonds say, what suppliers say, what regulators are doing), and a 54-agent run that built the "
    "strongest possible long case and the strongest possible short case from sixteen independent angles, attacked every one twice, "
    "and put the survivors to a five-judge panel. <b>268 agents across five runs.</b>"
)

VERDICT = (
    "<b>Decision: LONG — defensive, modest target, both sides weak.</b> All sixteen cases were killed, but they died differently, "
    "and that asymmetry is the decision. The eight shorts died because their <i>mechanisms</i> were wrong. The eight longs died "
    "because they were <i>already priced</i>. “Your facts don't hold” is a worse verdict than “your facts hold but everyone "
    "knows them”: you can defend the second in a question-and-answer room. Panel voted 4 to 1 long on a forced choice."
)

CAVEAT = (
    "<b>The strongest available argument is a hypothesis, not a finding.</b> The rebuttal to the one published Sell note — that "
    "percentage-of-completion accounting already ran the cheap 2024 order vintage through 2025 and 2026 earnings — has a real flaw. "
    "Percentage-of-completion fixes the margin rate when the contract is signed and changes <i>when</i> margin is recognised, not "
    "<i>how much</i>. A turbine sold cheaply in 2024 recognises its thin margin across whatever years it is built in. The rebuttal only "
    "holds if those 2024 contracts are largely complete by the end of 2026, and nobody established that. The analyst who wrote the Sell "
    "note covers this company professionally and knows the accounting. <b>Establish the completion share from the filings before this "
    "goes anywhere near a memo.</b>"
)

CONSENSUS = [
    ("Revenue", "$46.28B", "$52.74B", "$60.50B", "Two sources agree to 0.004%, likely one feed"),
    ("Adjusted EBITDA", "$6.36B", "$9.57B", "$13.06B", "FY27 corroborated at $9.45B via the GLJ note"),
    ("Adjusted EPS", "$15.21", "$24.85-25.31", "$34.22", "FY26 excludes the Prolec gain; 31-37 analysts"),
    ("Free cash flow", "$12.02B", "$7.42B", "$9.25B", "Consensus itself models FY27 cash flow falling 38%"),
]

CORRECTIONS = [
    ("The market multiple", "S&amp;P 500 forward P/E is <b>~19.1-19.7x</b>, not ~22x", "GEV at 38.2x on FY27 trades at <b>~1.95x the market</b>, not 1.6x. The premium the memo must defend is far bigger than assumed."),
    ("Forward P/E", "<b>38.2x</b> on FY27, not ~35x", "The ~35x figure was stale."),
    ("The Prolec gain", "<b>$3,992M pre-tax</b>, not ~$4.4B", "2Q'26 press release. The wrong figure came from our own earlier brief."),
    ("Power guidance", "<b>18-20%</b> organic growth, not 16-18%", "Superseded; the older band was being quoted."),
    ("Tariff guidance", "The “$100-200M for 2026” figure is <b>unverified</b>", "The only tariff guidance on record is $300-400M for FY2025."),
    ("Vineyard Wind", "<b>&gt;$800M was claimed AGAINST GEV</b>", "GEV claimed &gt;$300M. Settled Sep 16, terms confidential, GEV withdrew its termination notice."),
    ("Entergy's commitment", "Started at <b>15</b> sets, not 21", "15 &rarr; 21 &rarr; 24 &rarr; 27, about 20 GW. The only Entergy contract naming a party names <b>Mitsubishi</b>."),
    ("Siemens gas services", "“+62% to &euro;10B” is <b>orders</b>, not revenue", "Revenue was &euro;3.8B. Quoting it wrong overstates by 2.6x."),
]

CASES_LONG = [
    ("Fleet services wave", "70% of it is just unit growth; the differentiated piece is ~$6/share and lands in 2028"),
    ("Deposit engine", "Values a customer liability at 100 cents as equity; the market marked the July cash-flow raise DOWN 8.7%"),
    ("Backlog conversion", "Model collapses to one input; the same method a year earlier claimed 98% visibility against 66-70% realised"),
    ("Vintage rebuttal", "Mechanism excellent, but its 44.5% drop-through contradicts its own build (31.2%) and the 10-K's 22.5%"),
    ("Electrification", "Compares GEV on 2028 estimates to peers on FY25 actuals; 43% of segment EBITDA cannot offset a Power de-rate"),
    ("De-rating mispricing", "Capitalises the price decline itself; the drawdown was a sector move (Vertiv -25.5%, Quanta -11.6%)"),
    ("Capacity execution", "The 400 installed machines are a company press release; 5.2 GW was already printed in Q2'25"),
    ("Demand durability", "Defends 2.6% of market cap against a duration problem"),
]
CASES_SHORT = [
    ("Conversion gap", "A denominator artifact. GEV converted 10 GW against Siemens' 12"),
    ("Services quality", "Divides a net backlog change by GW, ignoring $6.6B of run-off"),
    ("Wind bridge", "The miss is real ($480M) but sits inside the guided band with ~$560M of cushion; the market paid +13.75% on the worst Wind quarter in two years"),
    ("Margin vintage", "Dies to percentage-of-completion, and 82% of it was an unsourced multiple assertion"),
    ("Multiple compression", "Mixes guidance vintages; the “never raised” claim is false ($14B&rarr;$22B&rarr;$24B in 13 months)"),
    ("Share loss", "Assumes a demand-constrained market in a franchise sold out to 2031"),
    ("Cash normalisation", "Right observation, wrong forward model; the liquidation ratio double-counts deposits carrying no backlog"),
    ("Shipment stall", "Its trigger metric correlates <b>-0.31</b> with the revenue line it is supposed to drive"),
]

KILLS = [
    ("Q3 equipment gross margin below 9.0%", "FY25 was 10.39%, Q2'26 was 13.10%. Two consecutive quarters below 9% and the margin pillar is dead; flip to short."),
    ("Q3 Power segment EBITDA margin below 17.0%", "The floor of management's own guide, in the quarter the volume ramp is supposed to land."),
    ("Q3 gas turbine gigawatts below 4.5 with HA units at 4 or fewer", "Management committed to 5 GW a quarter from Q3'26. Ten straight quarters have printed 3 to 5, with nothing above 5.2."),
    ("January 2027: 2026 backlog margin change below +4 points", "2025 printed +6 points and “at least $8B”. Management committed on Sep 16 to disclose it. This is the direct scorecard."),
]

KILLER_Q = (
    "At $940 you are paying 21.4 times management's own 2028 EBITDA target. Capitalise a perfectly delivered 2028 at the 25 times "
    "you say is fair, discount it two years, and you get $877 — below where the stock trades today. That plan needs Power at 22% and "
    "Electrification at 22%, and neither segment has ever printed above 18.9% or 18.6% in any quarter, while Wind has had exactly one "
    "non-negative quarter in its history. So what am I being paid for the execution risk?"
)

OTHER_SIDE = (
    "<b>Earned free cash flow is approximately zero, and the market is calling it a 4.8% yield.</b> First-half operating cash flow of "
    "$10,680M contains a $14,087M increase in customer deposits, so operating cash <i>excluding</i> deposits was <b>-$3,407M</b>. FY25 was "
    "-$3,363M on the same basis. Since the spin, cumulative free cash flow of $15.3B sits on a $24.5B deposit build while $7.6B went back "
    "to shareholders. Deposits of $40,037M are 3.05x cash on hand and 3.35x book equity. And 40% of the annual bonus plus 50% of the "
    "long-term plan pay on this line, with no orders or backlog metric as a counterweight. <b>This survived every attack. It is the "
    "question a judge will ask.</b> Concede the quality point; reject the cliff — the deposits are non-refundable and are discharged by "
    "delivering turbines at a positive margin, not by wiring cash back."
)


def _fig(w=10, h=4.2):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.grid(axis="y", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    return fig, ax


def chart_multiple():
    fig, ax = _fig(10, 4.0)
    names = ["S&P 500\nforward", "GEV\nFY28", "GEV\nFY27", "GEV\nFY26 adj"]
    vals = [19.4, 27.8, 38.2, 62.5]
    cols = [C[5], C[2], C[3], C[3]]
    bars = ax.bar(names, vals, color=cols, width=0.55)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, "%.1fx" % v, ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.axhline(19.4, color=C[5], linestyle=":", linewidth=1.5)
    ax.set_ylabel("price / earnings (x)")
    ax.set_title("GEV trades at about twice the market multiple, not 1.6x as we had assumed", loc="left", fontweight="bold")
    return fig


def chart_fcf_target():
    fig, ax = _fig(10, 4.0)
    years = ["FY2025\nactual", "FY2026\nguide (mid)", "FY2027+28\nimplied, per year"]
    vals = [3.71, 12.0, 4.15]
    bars = ax.bar(years, vals, color=[C[5], C[2], C[3]], width=0.5)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, "$%.1fB" % v, ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.set_ylabel("free cash flow ($B)")
    ax.set_title("The January arithmetic: management's own $24B cumulative target leaves ~$4B a year", loc="left", fontweight="bold")
    ax.annotate("$24B cumulative 2025-2028, less FY25 actual, less the FY26 guide, leaves $7.8-8.8B for two years.\n"
                "An opening 2027 guide of $4-6B is the mechanical result and will read as a collapse.",
                (-0.42, -3.0), fontsize=9, annotation_clip=False)
    return fig


def chart_earned_cash():
    fig, ax = _fig(10, 4.0)
    labels = ["FY2025", "H1 2026"]
    reported = [4.99, 10.68]
    deposits = [8.35, 14.09]
    earned = [r - d for r, d in zip(reported, deposits)]
    x = np.arange(len(labels))
    ax.bar(x - 0.2, reported, width=0.38, label="Reported operating cash flow", color=C[0])
    ax.bar(x + 0.2, earned, width=0.38, label="Excluding the deposit increase", color=C[3])
    for i, (r, e) in enumerate(zip(reported, earned)):
        ax.text(i - 0.2, r, "$%.1fB" % r, ha="center", va="bottom", fontsize=10, fontweight="bold")
        ax.text(i + 0.2, e, "-$%.1fB" % abs(e), ha="center", va="top", fontsize=10, fontweight="bold")
    ax.axhline(0, color="black", linewidth=0.9)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("$ billions")
    ax.set_title("The other side's best argument: operating cash excluding customer deposits", loc="left", fontweight="bold")
    ax.legend(frameon=False)
    return fig


def chart_cases():
    fig, ax = _fig(10, 3.6)
    ax.barh([1], [8], color=C[2], height=0.5)
    ax.barh([0], [8], color=C[3], height=0.5)
    ax.set_yticks([0, 1]); ax.set_yticklabels(["8 SHORT cases\ndied on wrong mechanisms", "8 LONG cases\ndied on being already priced"], fontsize=10)
    ax.set_xlim(0, 10)
    ax.set_xlabel("cases built, attacked twice each")
    ax.set_title("All sixteen cases were killed — but how they died is the decision", loc="left", fontweight="bold")
    for i, t in enumerate(["denominator artifacts, mixed vintages, accounting errors", "every one produced a target below the $1,236 street average"]):
        ax.text(0.15, i, t, va="center", fontsize=9.5, color="white", fontweight="bold")
    return fig


def chart_margins():
    fig, ax = _fig(10, 4.2)
    yrs = ["FY22", "FY23", "FY24", "FY25", "Q2'26"]
    cons = [11.66, 14.50, 17.42, 19.79, 21.25]
    equip = [None, -2.45, 5.08, 10.39, 13.10]
    ax.plot(yrs, cons, marker="o", linewidth=2.5, color=C[0], label="Consolidated gross margin")
    ax.plot(yrs, equip, marker="o", linewidth=2.5, color=C[1], label="Equipment gross margin")
    for i, v in enumerate(cons):
        ax.annotate("%.1f%%" % v, (i, v), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=9, fontweight="bold")
    for i, v in enumerate(equip):
        if v is not None:
            ax.annotate("%.1f%%" % v, (i, v), textcoords="offset points", xytext=(0, -14), ha="center", fontsize=9, color=C[1], fontweight="bold")
    ax.axhline(3, color=C[3], linestyle="--", linewidth=1.5)
    ax.text(0.05, 3.4, "the Sell note says 2027 ships at ~3 points of equipment margin", fontsize=9, color=C[3])
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel("percent")
    ax.set_title("The margin ramp is being delivered in public", loc="left", fontweight="bold")
    ax.legend(frameon=False, loc="upper left")
    return fig


def render(fig_b64, out_dir):
    charts = [
        ("multiple", "What the stock actually costs", chart_multiple,
         "Correcting the market multiple changes the whole valuation argument. GEV is priced at roughly twice the S&amp;P 500, not 1.6 times."),
        ("cases", "Sixteen cases, sixteen deaths", chart_cases, None),
        ("margins", "The margin record", chart_margins,
         "The published Sell note argues 2027 ships at about three points of equipment margin. GEV has already printed 10.4% for a full year and 13.1% in a quarter."),
        ("earned_cash", "Cash, with the deposits taken out", chart_earned_cash,
         "This is the strongest argument against the long and it survived every attack. It belongs in the risk section, stated plainly."),
        ("fcf_target", "The January arithmetic", chart_fcf_target, None),
    ]
    cards = []
    for key, title, fn, note in charts:
        try:
            b64 = fig_b64(fn(), out_dir / ("decision_%s.png" % key))
            extra = ('<p class="note">%s</p>' % note) if note else ""
            cards.append('<div class="card"><h3>%s</h3><img alt="%s" src="data:image/png;base64,%s">%s</div>'
                         % (html.escape(title), html.escape(title), b64, extra))
        except Exception as e:
            print("decision chart %s failed: %s" % (key, e))

    cons_rows = "".join("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td class='note'>%s</td></tr>" % r for r in CONSENSUS)
    corr = "".join('<div class="killcard"><b>%s</b><p>%s</p><p class="why">%s</p></div>' % (html.escape(a), b, c) for a, b, c in CORRECTIONS)
    longs = "".join("<li><b>%s</b> — %s</li>" % (html.escape(a), b) for a, b in CASES_LONG)
    shorts = "".join("<li><b>%s</b> — %s</li>" % (html.escape(a), b) for a, b in CASES_SHORT)
    kills = "".join('<div class="survcard"><b>%s</b><p>%s</p></div>' % (html.escape(a), html.escape(b)) for a, b in KILLS)

    return """<h2 id="decision">The decision: what the Street expects, and which side to take</h2>
<p class="note">%s</p>
<div class="banner"><b>LONG, defensively.</b><p>%s</p></div>
<div class="killcard" style="border-left-color:#8a5a00;background:#fff8ec"><b>Read this before using the headline argument</b><p>%s</p></div>
%s
<h3>The consensus baseline</h3>
<p class="note">Assembled from three or more free sources with the spread reported. The GAAP-versus-adjusted confusion is resolved: sites showing FY26 earnings near $30.78 include the Prolec revaluation gain; $15.21 excludes it.</p>
<div class="scroll"><table class="grid board"><tr><th>Metric</th><th>FY2026</th><th>FY2027</th><th>FY2028</th><th>Note</th></tr>%s</table></div>
<p class="note"><b>What $950 requires:</b> about 5.2%% annual free-cash-flow growth for ten years if the guided FY26 figure is a run rate — or about <b>10.5%% if deposits are stripped out</b>. That single assumption doubles the answer, and consensus itself models FY27 cash flow falling 38%%.</p>
<h3>Eight corrections to facts we had been carrying</h3>
%s
<h3>How every case died</h3>
<div class="grid2">
<div><p><b>The eight long cases — already priced</b></p><ul class="findlist">%s</ul></div>
<div><p><b>The eight short cases — wrong mechanisms</b></p><ul class="findlist">%s</ul></div>
</div>
<h3>What kills the thesis</h3>
<p class="note">All four land at Q3 earnings on <b>October 28</b>, which falls after the October 22-24 finals. Say that from the podium rather than letting a judge point it out.</p>
%s
<h3>The question you have to answer on stage</h3>
<div class="killcard"><b>The red teams' killer question</b><p><i>%s</i></p><p class="why">The answer: nothing on 2028 — which is why the target is +12%% and not +25%%, and why we sit below the Street. You are paid for the next twelve months, in which the three arguments that took $256 off this stock each fail again on the record.</p></div>
<h3>The other side's best argument</h3>
<div class="killcard"><b>Put this in the risk section. Do not dodge it.</b><p>%s</p></div>
""" % (INTRO, VERDICT, CAVEAT, "\n".join(cards), cons_rows, corr, longs, shorts, kills, html.escape(KILLER_Q), OTHER_SIDE)
