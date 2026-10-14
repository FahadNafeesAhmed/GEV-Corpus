"""The technical research section of the page: what the arXiv/IEEE sweep looked for,
what it found, what it killed, and why none of it cleared the materiality bar.

Reads docs/research/multi_agent/03_technical_wedge_hunt/agents.json (91 agents) plus the
two earlier runs, and renders charts + a full written record. Used by financials_charts.py.
"""
import html
import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "docs" / "research" / "multi_agent"
C = ["#1d4e89", "#e8a33d", "#2a9d8f", "#d95d39", "#7b6d8d", "#9aa5b1", "#4f81bd", "#f2c98a"]
PRICE = 940.33

INTRO = (
    "Three multi-agent runs searched for a mispricing: a broad corpus sweep, a wedge-selection tournament, and this one, "
    "a technical sweep across arXiv, IEEE, OpenAlex and the corpus academic tier. Sixteen research lenses read 212 papers and "
    "produced 38 findings. Every finding was then attacked by a physics skeptic who re-derived the central number from a second "
    "source, and independently re-priced by a quantifier who rebuilt the dollars-per-share arithmetic from scratch. "
    "<b>Zero findings survived both checks.</b> That is the result, and it is worth more than a weak yes: it says the debate about "
    "this stock is not a hidden technical fact, it is the multiple. What follows is the complete record, including the nine "
    "popular bear arguments the physics killed."
)

RULE = (
    "Every finding had to clear four bars: a quantified physical fact from a citable paper; a mechanism reaching a named GEV "
    "financial line; <b>materiality in dollars per share</b> (EBITDA impact x 25 multiple / 266.3M shares, against the $940.33 "
    "reference price); and a testable prediction with a date and a kill condition. Anything worth under about $10 a share, "
    "roughly 1%, is not a wedge no matter how elegant the physics."
)

# The physics that actually matters, extracted and verified across three independent agents.
GER3620 = [
    # model, combustion/HGP hours, HGP starts, major hours, major starts
    ("7HA.01 / 9HA.01", 25000, 900, 50000, 1800),
    ("7HA.02 / 9HA.02", 25000, 720, 50000, 1440),
]
FLEET = [  # (label, hours accumulated per unit, source)
    ("Average installed HA unit today", 28571),
    ("First hot-gas-path inspection", 25000),
    ("First major inspection", 50000),
]
DUTY = [  # (duty type, hours per start, note)
    ("New US simple-cycle peaker", 6, "3-8 hour blocks, ~987 equivalent full-load hours/yr"),
    ("Crossover: starts vs hours govern", 34.7, "25,000 factored hours / 720 factored starts"),
    ("Installed HA fleet today", 147, "3.0M fired hours / 20,400 fired starts"),
]
REVISIONS = [("FY2024", -319, 5473), ("FY2025", -151, 5412), ("H1 2026", -218, 2689)]

KILLED = [
    ("Part-load operation wears turbines faster",
     "GE's own GER-3620 Rev P sets the hours-based load severity factor at <b>1.0 all the way down to base load</b>, and in combined-cycle mode firing temperature does not drop until below ~80% of rated output. Part-load start cycles below 60% carry a factor of <b>0.5</b> and therefore <i>extend</i> the interval.",
     "Never say this on stage. It is the most intuitive bear argument and it is false."),
    ("Batteries are eating the peaker market",
     "Operating US battery capacity went from <b>8.9 GW to 53.3 GW</b> (+499%) between January 2023 and July 2026, while simple-cycle gas utilization went <b>up</b>. PJM accredits a 4-hour battery below a simple-cycle peaker for capacity value.",
     "Storage contests energy, not firm capacity. The GW are not at risk."),
    ("Reciprocating engines are taking turbine share",
     "Planned US reciprocating-engine capacity is flat at ~1.0 GW while planned turbine capacity went from <b>11.3 GW to 44.1 GW</b>. Recip share of planned gas collapsed from ~8% to <b>2.2%</b>.",
     "The bridge-power narrative is real but tiny in the data."),
    ("Hydrogen blending changes the economics",
     "EIA's planned-generator file contains exactly <b>one</b> hydrogen unit nationally, 50 MW, and it is a fusion pilot that has been miscoded.",
     "Hydrogen optionality in a US-driven story is worth approximately zero."),
    ("Liquid cooling shrinks the power that was contracted",
     "Uptime Institute puts industry average PUE at <b>1.52, flat for seven years</b>. Campuses sanctioned in 2026 are designed at 1.1-1.25 and the contract embeds that number, not a survey mean of a legacy fleet. Rack density rising 135 to 230 to 600 kW swamps the gain.",
     "Priced at $76/share by the researcher; correctly scoped it is under $4."),
    ("AI needs less power than people think, so orders fall",
     "GEV has <b>116 GW under contract against 20 GW/yr of output</b> rising to 30 GW/yr by 2030, roughly five years oversubscribed in an industry-wide shortage. Equipment revenue is recognized over time on costs incurred against contracts already signed.",
     "Demand haircuts trim the back of the queue, not this year's revenue. Every efficiency-driven bear thesis dies here."),
    ("Grid-enhancing technologies displace new gas",
     "FERC excluded dynamic line ratings from Order 2023's alternative-technologies list; reconductoring programs run on a 2035 horizon.",
     "Cannot touch a 3-12 month thesis."),
    ("The SMR option is a big part of the story",
     "Four independent sources put realized BWRX-300 capex at <b>US$12,530-17,949/kW</b>, which is 2.5-3.6x the ~$5,000/kWe viability threshold in the published literature. Total nuclear/SMR option value bounds at <b>$15-32/share</b> (1.6-3.4%).",
     "Real, small, and far out of the money. The licensing leg is de-risking, which kills the obvious bear catalyst too."),
    ("The corpus academic tier holds the AI-hardware answer",
     "It is a power-systems and wind library. Zero hits for “energy per token”, “roofline”, “arithmetic intensity” or “factored fired hours”. The signal sits in 42 arXiv data-center papers from 2025-26, which were genuinely unmined.",
     "Go to arXiv directly; do not mine the corpus for chip physics."),
]

SURVIVING_PHYSICS = [
    ("The starts-versus-hours crossover is real, and the fleet is on the safe side of it",
     "GER-3620 Rev P sets the 7HA.02 hot-gas-path inspection at 25,000 factored fired hours <i>or</i> 720 factored starts, whichever comes first. Divide and the crossover is <b>34.7 fired hours per start</b>. New simple-cycle peakers run 4-8 hours per start, five times below it, so starts would govern. But the installed HA fleet runs <b>147 hours per start</b> (3.0M hours / 20,400 starts), 4.2x clear on the hours side. The fleet that generates services revenue today is hours-limited, not starts-limited."),
    ("The average HA turbine has not reached its first major overhaul",
     "The fleet averages <b>28,571 operating hours per unit</b> (3.6M hours / 126 units, FY25 10-K) against a 50,000-hour major inspection. At the measured ~6,000 hours/year run rate the first major arrives in about <b>3.6 years</b>. This single disclosed fact explains the gap between management's $25M/GW-year services target and today's realised ~$15M with zero duty-cycle content. It is a tailwind, not a headwind."),
    ("The services accounting breaks the duty-cycle chain anyway",
     "GEV recognises service-contract revenue on cost-to-cost percentage of completion, and the FY25 10-K says billing happens “per hour of usage <b>and upon the occurrence of a major maintenance event</b>.” Several researchers quoted only the first half. A harsher duty cycle that pulls maintenance forward pulls billings forward with it, so the sign may be positive."),
    ("Nobody could establish how the contracts actually bill",
     "Neither the researchers nor the skeptics could determine from public sources whether GEV's service agreements bill on <i>actual</i> or <i>factored</i> fired hours. If factored, GE's own severity formula already prices duty cycle and the effect is zero. <b>This one question flips the sign on roughly a third of the technical work</b> and is the highest-value thing to ask investor relations."),
]

PAPERS = [
    ("GE Vernova, GER-3620 Rev P (2021), 60pp, free on gevernova.com",
     "Figures 36, 40, 42 and Appendix A. The single most important document in this whole file. Three separate agents misread Figure 36 in three different ways, so read it yourself."),
    ("GE Vernova FY2025 Form 10-K, Note 9 and critical accounting estimates",
     "Net long-term service agreement balance $3.4B is about 4% of life-of-contract billings, implying ~$85B; contracts ~29% complete; one percentage point of lifetime profitability equals $0.2B of contract asset. This is the sizing lever for any services thesis."),
    ("Huber, Wallmeier, Pieper, Schafmeister & Kolar, IPEC 2022 (ECCE Asia), open access from ETH",
     "The 800VDC efficiency ladder. Shows a conventional transformer plus central rectifier reaches 97.9% against the solid-state-transformer path's 97.7%, so 800VDC does not require an SST."),
    ("Li, She & Zhang, arXiv:2608.10999 (Aug 2026)",
     "SMR-versus-grid economics for hyperscale data centers, and the source of the ~$5,000/kWe viability threshold. Note its own caveat that the threshold is specific to the 2023 price year."),
    ("Norris et al., “Rethinking Load Growth”, Duke Nicholas Institute (2025)",
     "The flexible-load headroom numbers that everyone cites when arguing new data centers need less firm generation."),
]


def _fig(w=10, h=4.4):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.grid(axis="y", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    return fig, ax


def _load(run="03_technical_wedge_hunt"):
    p = RUNS / run / "agents.json"
    if not p.exists():
        return []
    return json.load(open(p, encoding="utf-8", errors="replace"))


def _research(data):
    out = {}
    for d in data:
        if d.get("phase") != "Research":
            continue
        r = d.get("result")
        if isinstance(r, str):
            try:
                r = json.loads(r)
            except Exception:
                continue
        if isinstance(r, dict):
            out[d.get("label", "").replace("research:", "")] = r
    return out


def chart_crossover():
    """The single most important physical chart: where starts overtake hours."""
    fig, ax = _fig(10, 4.0)
    duty = [d for d in DUTY if "Crossover" not in d[0]]
    labels = [d[0] for d in duty]
    vals = [d[1] for d in duty]
    notes = [d[2] for d in duty]
    ax.barh(range(len(vals)), vals, color=[C[3], C[2]], height=0.42)
    ax.set_yticks(range(len(vals)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xscale("log")
    ax.set_xlim(2, 900)
    ax.set_ylim(-0.6, 1.6)
    ax.set_xlabel("fired hours per start (log scale)")
    ax.set_title("The 34.7-hour rule: which maintenance clock governs", loc="left", fontweight="bold")
    ax.axvline(34.7, color="black", linestyle=":", linewidth=1.8)
    ax.text(3.0, 0.5, "STARTS govern this side\nmaintenance arrives early", fontsize=9.5, va="center",
            color=C[3], fontweight="bold")
    ax.text(40, 0.5, "crossover\n34.7 h/start", fontsize=9.5, va="center", fontweight="bold")
    ax.text(230, 0.5, "HOURS govern\nthis side", fontsize=9.5, va="center", color=C[2], fontweight="bold")
    for i, (v, n) in enumerate(zip(vals, notes)):
        ax.text(v * 1.18, i - 0.07, "%.0f h/start" % v, va="center", fontsize=10, fontweight="bold")
        ax.text(v * 1.18, i + 0.17, n, va="center", fontsize=8, color="#52606d")
    ax.invert_yaxis()
    return fig


def chart_fleet_maturity():
    fig, ax = _fig(10, 4.0)
    ax.barh([0], [28571], color=C[0], height=0.45)
    ax.axvline(25000, color=C[1], linestyle="--", linewidth=2)
    ax.axvline(50000, color=C[3], linestyle="--", linewidth=2)
    ax.text(25000, 0.42, " first hot-gas-path\n 25,000 h", color=C[1], fontsize=9, va="bottom", fontweight="bold")
    ax.text(50000, 0.42, " first major\n 50,000 h", color=C[3], fontsize=9, va="bottom", fontweight="bold")
    ax.text(28571, 0, "  28,571 h average", va="center", fontsize=10, fontweight="bold", color="white")
    ax.set_yticks([])
    ax.set_xlim(0, 58000)
    ax.set_xlabel("operating hours per installed HA unit")
    ax.set_title("The HA fleet has passed its first inspection and has not reached its first major overhaul",
                 loc="left", fontweight="bold")
    ax.annotate("126 units, 3.6M hours (FY25 10-K). At ~6,000 h/yr the first major wave lands in ~3.6 years.",
                (500, -0.38), fontsize=9)
    return fig


def chart_intervals():
    fig, ax = _fig(10, 4.0)
    models = [g[0] for g in GER3620]
    x = np.arange(len(models))
    w = 0.35
    ax.bar(x - w / 2, [g[2] for g in GER3620], width=w, label="Hot-gas-path: factored starts", color=C[0])
    ax.bar(x + w / 2, [g[4] for g in GER3620], width=w, label="Major: factored starts", color=C[3])
    for i, g in enumerate(GER3620):
        ax.text(i - w / 2, g[2], str(g[2]), ha="center", va="bottom", fontsize=9, fontweight="bold")
        ax.text(i + w / 2, g[4], str(g[4]), ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.set_ylabel("factored starts before inspection")
    ax.set_title("The newer machine has the tighter starts budget (GER-3620 Rev P)", loc="left", fontweight="bold")
    ax.annotate("Hours budget is 25,000 (hot-gas-path) and 50,000 (major) for both. Whichever limit arrives first governs.",
                (-0.45, -260), fontsize=9, annotation_clip=False)
    ax.legend(frameon=False)
    return fig


def chart_revisions():
    fig, ax = _fig(10, 4.0)
    labels = [r[0] for r in REVISIONS]
    pct = [abs(r[1]) / r[2] * 100 for r in REVISIONS]
    bars = ax.bar(labels, pct, color=[C[5], C[5], C[3]], width=0.5)
    for b, p, r in zip(bars, pct, REVISIONS):
        ax.text(b.get_x() + b.get_width() / 2, p, "%.2f%%\n(%s$%dM)" % (p, "-", abs(r[1])), ha="center", va="bottom", fontsize=9)
    ax.set_ylabel("unfavourable revision as % of contract revenue")
    ax.set_title("The service-revision line is not a clean escalation: FY24 breaks the AI story",
                 loc="left", fontweight="bold")
    ax.annotate("FY24 ran at more than double the FY25 rate, with essentially zero data-center HA capacity operating.",
                (-0.45, -1.5), fontsize=9, annotation_clip=False)
    return fig


def chart_materiality(data):
    """Every finding's independent per-share value against the price."""
    fig, ax = _fig(10, 4.2)
    bands = [("Best technical finding\n(sign unresolved)", 2.65, 17.49),
             ("Service-revision line\n(existing angle)", 8.0, 17.0),
             ("SMR option value", 15.0, 32.0),
             ("800VDC content shortfall\n(not in the price)", 0.0, 27.0)]
    y = np.arange(len(bands))
    for i, (lab, lo, hi) in enumerate(bands):
        ax.barh(i, hi - lo, left=lo, height=0.45, color=C[0] if i else C[3])
        ax.text(hi + 4, i, "$%.0f-%.0f" % (lo, hi), va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels([b[0] for b in bands], fontsize=9)
    ax.set_xlim(0, 200)
    ax.axvline(PRICE * 0.20, color="black", linestyle=":", linewidth=1.5)
    ax.text(PRICE * 0.20, len(bands) - 0.3, " 20% of the share price ($188)", fontsize=9, va="top")
    ax.set_xlabel("dollars per share, independently re-derived")
    ax.set_title("Nothing the physics found is big enough to be the thesis", loc="left", fontweight="bold")
    ax.invert_yaxis()
    return fig


def chart_lens_scores(data):
    res = _research(data)
    fig, ax = _fig(10, 5.0)
    xs, ys, ss, cs, labels = [], [], [], [], []
    for lens, r in res.items():
        short = re.split(r"[—:.]", lens)[0].strip()[:28]
        for f in r.get("findings", []):
            xs.append(f.get("novelty", 0) + np.random.RandomState(abs(hash(f.get("title", ""))) % 2**31).uniform(-0.12, 0.12))
            ys.append(f.get("materiality", 0) + np.random.RandomState((abs(hash(f.get("title", ""))) + 7) % 2**31).uniform(-0.12, 0.12))
            ss.append(30 + 40 * f.get("confidence", 1))
            d = f.get("direction", "")
            cs.append({"short": C[3], "long": C[2], "kills-an-existing-angle": C[5], "either": C[1], "neutral": C[4]}.get(d, C[0]))
            labels.append(short)
    ax.scatter(xs, ys, s=ss, c=cs, alpha=0.75, edgecolors="white", linewidth=0.8)
    ax.set_xlabel("novelty, as scored by the researcher (1-5)")
    ax.set_ylabel("materiality, as scored by the researcher (1-5)")
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_title("All 38 findings: self-scored before verification (bubble size = confidence)", loc="left", fontweight="bold")
    from matplotlib.lines import Line2D
    keys = [("short", C[3]), ("long", C[2]), ("kills an angle", C[5]), ("either", C[1]), ("neutral", C[4])]
    ax.legend(handles=[Line2D([], [], marker="o", linestyle="", color=c, label=k, markersize=8) for k, c in keys],
              frameon=False, ncol=5, fontsize=9, loc="lower left")
    ax.annotate("Every one of these was refuted on verification, or re-priced as immaterial. Self-scores run hot; that is the lesson.",
                (0.6, 0.15), fontsize=9, annotation_clip=False)
    return fig


def chart_run_sizes():
    fig, ax = _fig(10, 3.8)
    runs = [("Run 1\nCorpus sweep", 46, 0), ("Run 2\nWedge selection", 46, 0), ("Run 3\nTechnical sweep", 91, 212)]
    x = np.arange(len(runs))
    ax.bar(x - 0.2, [r[1] for r in runs], width=0.4, label="agents", color=C[0])
    ax.bar(x + 0.2, [r[2] for r in runs], width=0.4, label="papers read", color=C[1])
    for i, r in enumerate(runs):
        ax.text(i - 0.2, r[1], str(r[1]), ha="center", va="bottom", fontsize=9, fontweight="bold")
        if r[2]:
            ax.text(i + 0.2, r[2], str(r[2]), ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([r[0] for r in runs])
    ax.set_title("Three multi-agent runs: 183 agents, 212 papers, one negative result", loc="left", fontweight="bold")
    ax.legend(frameon=False)
    return fig


def render(fig_b64, out_dir):
    data = _load()
    if not data:
        return ""
    res = _research(data)
    charts = [
        ("run_sizes", "The research effort", chart_run_sizes, None),
        ("crossover", "The one piece of physics that matters", chart_crossover,
         "GE's own maintenance manual sets two clocks on a turbine: fired hours and starts. Whichever fills first triggers an "
         "expensive inspection. Divide the two limits and you get 34.7 hours per start. A machine that runs long shifts is "
         "limited by hours. A machine that starts and stops all day is limited by starts, and needs an overhaul far sooner "
         "than an hours-based cost model expects. New peakers sit well left of the line. The installed fleet sits well right of it."),
        ("fleet_maturity", "The fleet is younger than the story assumes", chart_fleet_maturity,
         "This is disclosed-number arithmetic with no assumption chain, and it is the strongest defensible claim in the file, "
         "in either direction. It also explains why services earn about $15M per gigawatt-year today against a $25M target, "
         "with no need for any AI or duty-cycle story at all."),
        ("intervals", "The newer machine is tighter on starts", chart_intervals, None),
        ("revisions", "The number that breaks the AI framing", chart_revisions,
         "Service-contract profit estimates are being cut, and that is real. But fiscal 2024 ran at more than double the "
         "fiscal 2025 rate, at a time when essentially no data-center-linked H-class capacity was operating. A judge holding "
         "the FY24 filing ends an 'AI duty cycles are eating the annuity' pitch with one question."),
        ("materiality", "Everything, priced", chart_materiality,
         "Each bar is an independent re-derivation of what the finding is worth per share, not the researcher's own estimate. "
         "The dotted line is a 20% move. Nothing comes close."),
        ("lens_scores", "How the findings scored themselves", chart_lens_scores, None),
    ]
    cards = []
    for key, title, fn, note in charts:
        try:
            fig = fn(data) if fn.__code__.co_argcount else fn()
            b64 = fig_b64(fig, out_dir / ("research_%s.png" % key))
            extra = ('<p class="note">%s</p>' % note) if note else ""
            cards.append('<div class="card"><h3>%s</h3><img alt="%s" src="data:image/png;base64,%s">%s</div>'
                         % (html.escape(title), html.escape(title), b64, extra))
        except Exception as e:  # a broken chart must not take the page down
            print("research chart %s failed: %s" % (key, e))

    killed = "".join(
        '<div class="killcard"><b>%s</b><p>%s</p><p class="why">%s</p></div>' % (html.escape(t), body, html.escape(why))
        for t, body, why in KILLED)

    surviving = "".join('<div class="survcard"><b>%s</b><p>%s</p></div>' % (html.escape(t), body)
                        for t, body in SURVIVING_PHYSICS)

    papers = "".join('<li><b>%s</b><br><span class="note">%s</span></li>' % (html.escape(t), html.escape(d))
                     for t, d in PAPERS)

    # Full lens-by-lens record
    rows = []
    for lens, r in sorted(res.items()):
        name = re.split(r"[—:.]", lens)[0].strip()
        fs = r.get("findings", [])
        items = "".join(
            '<li><span class="tag tag-%s">%s</span> %s<br><span class="note">%s</span></li>'
            % (html.escape(f.get("direction", "neutral")), html.escape(f.get("direction", "")),
               html.escape(f.get("title", "")), html.escape((f.get("physical_fact", "") or "")[:400]))
            for f in fs)
        rows.append('<details><summary><b>%s</b> &mdash; %d findings, %d papers</summary><ul class="findlist">%s</ul></details>'
                    % (html.escape(name), len(fs), len(r.get("papers_read", [])), items))

    dead = []
    for lens, r in res.items():
        name = re.split(r"[—:.]", lens)[0].strip()[:34]
        for d in r.get("dead_ends", [])[:6]:
            dead.append("<li><b>%s</b>: %s</li>" % (html.escape(name), html.escape(d[:300])))

    style = """
<style>
.killcard,.survcard{background:#fff;border:1px solid #e1e6ec;border-radius:10px;padding:12px 14px;margin:8px 0;font-size:13.5px;line-height:1.5}
.killcard{border-left:4px solid #d95d39}.survcard{border-left:4px solid #2a9d8f}
.killcard b,.survcard b{display:block;margin-bottom:4px;color:#1f2933}
.killcard p,.survcard p{margin:4px 0}
.killcard .why{color:#8a3a20;font-size:12.5px;font-style:italic}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:800px){.grid2{grid-template-columns:1fr}}
details{background:#fff;border:1px solid #e1e6ec;border-radius:8px;padding:8px 12px;margin:6px 0;font-size:13px}
details summary{cursor:pointer;color:#1d4e89}
.findlist{margin:8px 0 0;padding-left:16px}.findlist li{margin:8px 0;line-height:1.45}
.tag{display:inline-block;border-radius:999px;padding:1px 7px;font-size:10.5px;color:#fff;margin-right:5px;text-transform:uppercase;letter-spacing:.03em}
.tag-short{background:#d95d39}.tag-long{background:#2a9d8f}.tag-either{background:#e8a33d}
.tag-neutral{background:#7b6d8d}.tag-kills-an-existing-angle{background:#9aa5b1}
.banner{background:#1d4e89;color:#fff;border-radius:12px;padding:16px 18px;margin:14px 0}
.banner b{font-size:17px}.banner p{margin:6px 0 0;font-size:13.5px;line-height:1.55;opacity:.95}
</style>"""

    return """%s<h2 id="research">The technical research: arXiv, IEEE and the physics</h2>
<p class="note">%s</p>
<div class="banner"><b>Result: no technical wedge.</b><p>%s</p></div>
%s
<h3>The physics that survived, and the question that decides it</h3>
%s
<h3>Nine arguments the physics killed</h3>
<p class="note">This is the most useful part of the section. Each of these is an intuitive bear argument that other teams may pitch, and each is contradicted by a hard number.</p>
%s
<h3>Every lens, every finding</h3>
<p class="note">Sixteen lenses, 38 findings. Direction tags are the researcher's own. Expand any lens to see what it found and the physical fact behind it.</p>
%s
<h3>Papers worth reading</h3>
<ul class="findlist">%s</ul>
<h3>Dead ends</h3>
<p class="note">Closed with evidence, so nobody repeats them.</p>
<ul class="findlist">%s</ul>
""" % (style, INTRO, RULE, "\n".join(cards), surviving, killed, "\n".join(rows), papers, "\n".join(dead[:40]))
