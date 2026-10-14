"""Charts of the research corpus itself (data/gev.db): what it holds, and what it found.
Used by financials_charts.py to append a corpus section to the page. Read-only on the DB.
"""
import re
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "gev.db"
C = ["#1d4e89", "#e8a33d", "#2a9d8f", "#d95d39", "#7b6d8d", "#9aa5b1", "#4f81bd", "#f2c98a"]

INTRO = ("Everything above came from GE Vernova's own filings. This section is the wider research corpus the team built: "
         "34 companies' filings, competitor and customer reports, grid-operator studies, government generator data, academic papers "
         "and dated commentary, stored in one 4 GB database and read by local models. First what it contains, then what it found.")

# Curated results of the multi-agent sweep (2026-09-21). status: verified / refuted / unverified / dead-end
FINDINGS = [
    ("Service-contract profit revisions -$218M in H1 2026, five times H1 2025", "short", "verified", "10-Q Note 9; reproduced exactly; not published anywhere we could find"),
    ("CEO's own HA services math is about $25M per GW-year; the $70M bull figure is one Jefferies projection for the 2030s", "short", "unverified", "Laguna conference Sep 16 2026 coverage; today's yield about $15M per GW-year"),
    ("HA units shipped fell 38% in H1 2026 (8 vs 13); Q2 shipped 3 HA plus 16 aeroderivatives", "short", "refuted as thesis", "Numbers reproduce, but trailing-4Q GW is flat and revenue is booked on cost, not shipment"),
    ("First-in-first-out check: 2024-priced orders are mostly shipped by H2 2026, so 2027 ships 2025 orders", "long", "unverified", "Challenges the GLJ vintage-margin timing; revenue is over-time so directional only"),
    ("Deposits convert to revenue slower: 29% of opening balance in H1 2026 vs 40% in 2025; deposits are 43% of equipment backlog", "long", "unverified", "XBRL ContractWithCustomerLiabilityRevenueRecognized; cash reversal unlikely inside 12 months"),
    ("Equipment backlog due within 12 months fell from 46% to 36% of the total since 2024; the dollar amount still rose", "either", "unverified", "RPO timing footnote across eight filings"),
    ("Entergy holds an exclusive supply deal with Mitsubishi for a minimum of 27 large power-island sets, ratcheted up four times", "short", "unverified", "Entergy 10-Q text; none of the biggest US utility build is GEV"),
    ("The March 2026 jump in EIA planned gas units is 65% one speculative Siemens-supplied campus (Fermi America, Texas)", "neutral", "unverified", "EIA-860M vintage diff; ex-Fermi, new planning shrank vs March 2025"),
    ("No US combustion turbine of 300 MW or more entered service in 2024, 2025 or 2026 to date; only 2.3 of 15.3 GW planned is under construction", "either", "verified", "EIA-860M Operating and Planned sheets"),
    ("60% of planned US gas capacity for 2026-27 is simple-cycle peakers that run about 10% of hours", "short", "unverified", "EIA-860M and EIA-923 join; services scale with hours, not GW"),
    ("GEV converts about 20% of its reservation pool per quarter; Siemens Energy converted 44% in the same quarter", "short", "unverified", "GEV press releases vs Siemens Q3 FY26 presentation"),
    ("Wind FY26 guide implies a +$257M second half; the best Wind quarter since the spin was +$19M", "short", "unverified", "8-K reconciliations; the Sep 16 Vineyard settlement is the swing item"),
    ("Rate filings show all-in combined-cycle plant cost rising from $988/kW (2021) to $2,700/kW (2026); GE blocks price no higher than Mitsubishi's", "either", "unverified", "Entergy and Oglethorpe filings; turbine is about 30% of plant cost per the CEO"),
    ("The December investor update, not earnings, is GEV's largest scheduled move (+15.6% in 2025, fully reversed in five days)", "either", "verified", "prices table; missing from most catalyst calendars"),
    ("Earnings-day returns since Q1 2025 follow the sign of the EPS surprise every time; GW announcements do not move the stock", "neutral", "verified", "Refutes the 'orders saturated' story; the stock trades on EPS and guidance"),
    ("The June-to-September drawdown is mostly GEV-specific once the regression includes an intercept (about -23% vs peers)", "neutral", "verified", "Corrects the first-pass 'half beta' reading"),
    ("'$3,000 per kW' and 'prices up 300%' are whole-plant costs; GEV's own turbine scope is about $740/kW, up 54% in five quarters", "neutral", "verified", "Q3 2025 call, Q2 2026 call, RPO tables"),
    ("The $0.3B per year 'availability shortfall' is a Wind farm guarantee charge, not an HA gas-fleet number", "neutral", "verified", "Correction to an earlier internal note"),
    ("Tariff cost estimate cut from $250-350M to $100-200M between Q1 and Q2 10-Qs", "neutral", "refuted as insight", "Real, but a macro legal event, not execution"),
    ("Insider selling: five small open-market sales in 18 months, none large", "neutral", "dead-end", "Form 4 table; no signal"),
    ("No filing anywhere discloses reservation deposit percentage or refund terms", "neutral", "dead-end", "SEC full-text search across all filers; the one open question that decides the reservations point"),
]

GUIDE = (
    "A corpus is not a thesis. It is a place where a thesis can be tested cheaply. The way to use it: start from something "
    "the market believes, write the sentence down, then look for the table or filing that would prove it wrong. Most beliefs "
    "survive. The few that do not are the memo.",
    [
        "Primary sources beat commentary. When a news story and a 10-Q disagree, the 10-Q wins and the story tells you what the crowd thinks.",
        "Series beat snapshots. One footnote number across ten quarters is worth more than ten numbers from one quarter.",
        "Joins beat reading. The findings came from putting two tables next to each other, not from reading either one.",
        "Verification kills half of everything. Of the sweep's findings, about half were reproduced and not refuted. The refuted half is still useful as a list of traps.",
        "Absence is information. No filing gives the deposit terms. That gap is itself the most important fact about the reservations debate.",
    ],
    [
        "Which of these findings changes a number in the model, and by how much?",
        "For each finding, what is the single check on October 22 that confirms or kills it?",
        "Which findings point the same direction, and is that direction the one the team wants, or the one the data wants?",
        "What would a Citadel analyst with expert calls know that this corpus cannot tell us, and how do we hedge that gap?",
        "Which dead ends should we stop spending time on?",
    ],
)


def _con():
    return sqlite3.connect(DB) if DB.exists() else None


def _fig(w=10, h=4.4):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.grid(axis="y", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    return fig, ax


def corpus_composition(con):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1, 1.4]})
    t = pd.read_sql("SELECT tier, COUNT(*) n FROM chunks GROUP BY tier", con)
    a1.pie(t["n"], labels=["%s\n%s" % (r.tier, format(r.n, ",")) for r in t.itertuples()], colors=C[:3], startangle=90, wedgeprops={"width": 0.45})
    a1.set_title("469k text chunks by source tier", loc="left", fontweight="bold")
    k = pd.read_sql("SELECT kind, COUNT(*) n FROM chunks GROUP BY kind ORDER BY n", con)
    a2.barh(k["kind"], k["n"], color=C[0]); a2.set_xscale("log"); a2.set_title("Chunks by source type (log scale)", loc="left", fontweight="bold")
    a2.spines[["top", "right"]].set_visible(False)
    for i, v in enumerate(k["n"]):
        a2.text(v, i, " " + format(v, ","), va="center", fontsize=8)
    return fig


def corpus_by_company(con):
    fig, ax = _fig(10, 5)
    t = pd.read_sql("SELECT ticker, COUNT(*) n FROM chunks WHERE ticker IS NOT NULL AND ticker<>'' GROUP BY ticker ORDER BY n DESC LIMIT 24", con)
    ax.bar(t["ticker"], t["n"] / 1e3, color=[C[3] if x == "GEV" else C[0] for x in t["ticker"]])
    ax.set_ylabel("thousand chunks"); ax.set_title("Filing text by company (GEV in red)", loc="left", fontweight="bold")
    ax.tick_params(axis="x", rotation=60, labelsize=8); return fig


def angle_radar(con):
    t = pd.read_sql("SELECT angle, COUNT(*) n FROM sources WHERE angle NOT IN ('feed','ir','hitachi','mhi','siemens_energy','vestas') GROUP BY angle ORDER BY n DESC LIMIT 14", con)
    labels = [a.replace("_", " ") for a in t["angle"]]; vals = t["n"].tolist()
    ang = np.linspace(0, 2 * np.pi, len(vals), endpoint=False).tolist(); vals2 = vals + vals[:1]; ang2 = ang + ang[:1]
    fig = plt.figure(figsize=(7.5, 7)); ax = plt.subplot(111, polar=True)
    ax.plot(ang2, vals2, color=C[0], linewidth=2); ax.fill(ang2, vals2, color=C[0], alpha=0.2)
    ax.set_xticks(ang); ax.set_xticklabels(labels, fontsize=8); ax.set_yticklabels([]); ax.set_title("Web and academic sources per research angle", loc="left", fontweight="bold", pad=18)
    return fig


def extracted_facts(con):
    fig, ax = _fig(10, 4)
    rows = []
    for t, lab in (("guidance", "Guidance statements"), ("claims", "Claims"), ("risk_items", "Risk items"), ("backlog_quarterly", "Backlog rows"),
                   ("projects", "Customer projects"), ("analyst_calls", "Analyst calls"), ("transcript_statements", "Transcript statements"), ("competitor_financials", "Competitor figures")):
        cols = [x[1] for x in con.execute("PRAGMA table_info(%s)" % t)]
        allc = con.execute("SELECT COUNT(*) FROM %s" % t).fetchone()[0]
        gev = con.execute("SELECT COUNT(*) FROM %s WHERE ticker='GEV'" % t).fetchone()[0] if "ticker" in cols else allc
        rows.append((lab, allc, gev))
    d = pd.DataFrame(rows, columns=["table", "all", "gev"]); x = range(len(d))
    ax.bar(x, d["all"], color=C[5], label="All companies"); ax.bar(x, d["gev"], color=C[3], label="GEV only", width=0.5)
    ax.set_xticks(list(x)); ax.set_xticklabels(d["table"], rotation=30, ha="right", fontsize=9); ax.set_yscale("log")
    ax.set_title("Facts the local model extracted, with verbatim quotes (log scale)", loc="left", fontweight="bold"); ax.legend(frameon=False); return fig


def eia_planned(con):
    fig, ax = _fig()
    t = pd.read_sql("""SELECT vintage, CASE WHEN status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%' THEN 'Under construction or complete' ELSE 'Planned, not under construction' END s, SUM(mw)/1000.0 gw
        FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','GT','CS','CA','CC') GROUP BY vintage, s ORDER BY vintage""", con)
    p = t.pivot(index="vintage", columns="s", values="gw").fillna(0)
    ax.stackplot(range(len(p)), p["Under construction or complete"], p["Planned, not under construction"],
                 labels=["Under construction or complete", "Planned, not under construction"], colors=[C[0], C[5]], alpha=0.9)
    ax.set_xticks(range(0, len(p), 3)); ax.set_xticklabels(p.index[::3], rotation=45, ha="right", fontsize=8); ax.set_ylabel("GW")
    ax.set_title("Planned US gas turbine capacity in every monthly EIA snapshot, 2023 to 2026", loc="left", fontweight="bold"); ax.legend(frameon=False, loc="upper left"); return fig


def eia_generation(con):
    fig, ax = _fig()
    t = pd.read_sql("""SELECT year, CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN 'Combined cycle' WHEN prime_mover='GT' THEN 'Simple cycle' ELSE 'Steam and other' END pm,
        SUM(net_generation_mwh)/1e6 twh FROM generation WHERE fuel_type='NG' AND year<=2025 GROUP BY year, pm""", con)
    p = t.pivot(index="year", columns="pm", values="twh").fillna(0)[["Combined cycle", "Simple cycle", "Steam and other"]]
    bottom = np.zeros(len(p))
    for i, c in enumerate(p.columns):
        ax.bar(p.index.astype(str), p[c], bottom=bottom, label=c, color=C[i]); bottom += p[c].values
    ax.set_ylabel("TWh"); ax.set_title("US gas-fired generation by plant type (EIA-923)", loc="left", fontweight="bold"); ax.legend(frameon=False)
    for i, v in enumerate(bottom):
        ax.text(i, v, format(int(v), ","), ha="center", va="bottom", fontsize=9)
    return fig


def eia_unit_size(con):
    fig, ax = _fig()
    t = pd.read_sql("""SELECT vintage, mw FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover='CT'
        AND substr(vintage,6,2) IN ('01','07') AND plant_name NOT LIKE '%Matador%'""", con)
    g = t.groupby("vintage")["mw"].agg(["median", "count"])
    ax.bar(g.index, g["median"], color=C[0])
    for i, (m, n) in enumerate(zip(g["median"], g["count"])):
        ax.text(i, m, "%.0f MW\nn=%d" % (m, n), ha="center", va="bottom", fontsize=8)
    ax.set_ylabel("median MW per planned unit"); ax.set_title("Planned combined-cycle turbines are getting bigger (H/J-class sized)", loc="left", fontweight="bold"); return fig


def narrative_gap(con):
    fig, ax = _fig()
    t = pd.read_sql("""SELECT substr(filing_date,1,4)||'-Q'||((CAST(substr(filing_date,6,2) AS INT)+2)/3) q, tier, COUNT(*) n,
        SUM(CASE WHEN lower(text) LIKE '%data center%' OR lower(text) LIKE '%hyperscale%' THEN 1 ELSE 0 END) dc
        FROM chunks WHERE ticker='GEV' AND filing_date BETWEEN '2025-01' AND '2026-12' AND tier IN ('primary','commentary') GROUP BY q, tier""", con)
    t["rate"] = 1000 * t["dc"] / t["n"]
    p = t.pivot(index="q", columns="tier", values="rate")
    for c, col in (("commentary", C[3]), ("primary", C[0])):
        if c in p:
            ax.plot(range(len(p)), p[c].values, marker="o", linewidth=2, color=col, label="Commentary about GEV" if c == "commentary" else "GEV's own filings")
    ax.set_xticks(range(len(p))); ax.set_xticklabels(p.index, rotation=45, ha="right", fontsize=9); ax.set_ylabel("'data center' mentions per 1,000 chunks")
    ax.set_title("The narrative gap: how often 'data center' appears", loc="left", fontweight="bold"); ax.legend(frameon=False); return fig


def projects_status(con):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1, 1.3]})
    t = pd.read_sql("SELECT commitment_status s, COUNT(*) n FROM projects WHERE lower(oem) LIKE '%ge%' OR lower(oem) LIKE '%vernova%' GROUP BY s ORDER BY n DESC", con)
    a1.bar(t["s"], t["n"], color=C[0]); a1.tick_params(axis="x", rotation=45, labelsize=8); a1.set_title("GE-linked customer projects by status", loc="left", fontweight="bold")
    a1.spines[["top", "right"]].set_visible(False)
    o = pd.read_sql("""SELECT owner, MAX(CAST(capacity_mw AS REAL)) mw FROM projects WHERE (lower(oem) LIKE '%ge%' OR lower(oem) LIKE '%vernova%')
        AND capacity_mw<>'' AND CAST(capacity_mw AS REAL) BETWEEN 50 AND 20000 AND owner NOT LIKE 'GE Vernova%' GROUP BY owner ORDER BY mw DESC LIMIT 12""", con)
    a2.barh(o["owner"].str.slice(0, 28)[::-1], o["mw"][::-1] / 1000, color=C[1]); a2.set_xlabel("GW (largest single project per owner)")
    a2.set_title("Biggest named projects tied to GE turbines", loc="left", fontweight="bold"); a2.spines[["top", "right"]].set_visible(False); return fig


def analyst_targets(con):
    fig, ax = _fig()
    t = pd.read_sql("SELECT published, firm, value FROM analyst_calls WHERE ticker='GEV' AND metric='price_target' AND value LIKE '$%' AND value NOT LIKE '%/kW%'", con)
    t["v"] = t["value"].str.replace(r"[^\d.]", "", regex=True).astype(float); t = t[(t["v"] > 300) & (t["v"] < 2000)]
    t["d"] = pd.to_datetime(t["published"], errors="coerce"); t = t.dropna(subset=["d"])
    px = pd.read_sql("SELECT date, close FROM prices WHERE ticker='GEV' AND date>='2026-01-01' ORDER BY date", con); px["d"] = pd.to_datetime(px["date"])
    ax.plot(px["d"], px["close"], color=C[5], linewidth=1.5, label="GEV share price")
    ax.scatter(t["d"], t["v"], color=C[3], s=28, zorder=3, label="Published price targets (attributed)")
    for r in t.sort_values("v").drop_duplicates("firm").itertuples():
        ax.annotate(r.firm[:14], (r.d, r.v), fontsize=7, xytext=(3, 2), textcoords="offset points")
    ax.set_title("Price targets in the corpus versus the share price (not a consensus)", loc="left", fontweight="bold"); ax.legend(frameon=False); return fig


def price_vs_peers(con):
    fig, ax = _fig()
    for tk, col in (("GEV", C[3]), ("VRT", C[0]), ("ETN", C[2]), ("PWR", C[1]), ("SPY", C[5])):
        p = pd.read_sql("SELECT date, close FROM prices WHERE ticker=? AND date>='2024-04-01' ORDER BY date", con, params=(tk,))
        if len(p):
            ax.plot(pd.to_datetime(p["date"]), p["close"] / p["close"].iloc[0] * 100, label=tk, color=col, linewidth=2 if tk == "GEV" else 1.2)
    ax.set_ylabel("indexed to 100 at Apr 2024"); ax.set_title("GEV versus the AI-power peer group and the S&P 500 since the spin-off", loc="left", fontweight="bold"); ax.legend(frameon=False); return fig


def insider_sales(con):
    fig, ax = _fig(10, 3.6)
    t = pd.read_sql("SELECT substr(tx_date,1,7) m, SUM(shares*price)/1e6 usd FROM insider_tx WHERE ticker='GEV' AND code='S' GROUP BY m ORDER BY m", con)
    ax.bar(t["m"], t["usd"], color=C[4]); ax.set_ylabel("$ millions sold"); ax.set_title("Insider open-market sales by month (Form 4)", loc="left", fontweight="bold"); return fig


def oem_radar():
    axes = ["Firm backlog GW", "Reservations GW", "Q2 firm orders GW", "Q2 shipped GW", "Backlog / quarterly shipments"]
    data = {"GE Vernova": [53, 63, 12, 3, 53 / 3], "Siemens Energy": [69, 26, 15, 6, 69 / 6], "Mitsubishi Power": [35, 0, 4, 2, 35 / 2]}
    mx = np.array([max(v[i] for v in data.values()) for i in range(len(axes))])
    ang = np.linspace(0, 2 * np.pi, len(axes), endpoint=False).tolist(); ang2 = ang + ang[:1]
    fig = plt.figure(figsize=(7.5, 7)); ax = plt.subplot(111, polar=True)
    for (name, v), col in zip(data.items(), C):
        n = (np.array(v) / mx).tolist(); ax.plot(ang2, n + n[:1], linewidth=2, label=name, color=col); ax.fill(ang2, n + n[:1], alpha=0.12, color=col)
    ax.set_xticks(ang); ax.set_xticklabels(axes, fontsize=8); ax.set_yticklabels([])
    ax.set_title("Three factories, one market: Q2 2026 as read from each company's report (scaled to the largest)", loc="left", fontweight="bold", pad=18, fontsize=10)
    ax.legend(loc="lower right", bbox_to_anchor=(1.2, -0.08), frameon=False, fontsize=9); return fig


CHARTS = [
    ("corpus_composition", "What the corpus is made of", corpus_composition),
    ("corpus_by_company", "Whose filings are in it", corpus_by_company),
    ("angle_radar", "Coverage by research angle", angle_radar),
    ("extracted_facts", "What the local model extracted", extracted_facts),
    ("price_vs_peers", "The stock against its peers", price_vs_peers),
    ("analyst_targets", "Price targets in the corpus", analyst_targets),
    ("narrative_gap", "The narrative gap", narrative_gap),
    ("eia_planned", "Planned US gas capacity, month by month", eia_planned),
    ("eia_generation", "How hard the US gas fleet runs", eia_generation),
    ("eia_unit_size", "Planned turbines are getting bigger", eia_unit_size),
    ("projects_status", "Customer projects tied to GE", projects_status),
    ("oem_radar", "GEV vs Siemens vs Mitsubishi", oem_radar),
    ("insider_sales", "Insider selling", insider_sales),
]


def render(fig_b64, out_dir):
    """Return HTML for the corpus section; fig_b64(fig, path) saves and encodes a figure."""
    con = _con()
    if con is None:
        return ""
    cards = []
    for name, title, fn in CHARTS:
        try:
            fig = fn(con) if fn.__code__.co_argcount else fn()
            cards.append('<div class="card"><h3>%s</h3><img alt="%s" src="data:image/png;base64,%s"></div>' % (title, title, fig_b64(fig, out_dir / ("corpus_%s.png" % name))))
        except Exception as e:
            print("corpus chart %s failed: %s" % (name, e))
    colors = {"verified": "#2a9d8f", "unverified": "#e8a33d", "refuted as thesis": "#d95d39", "refuted as insight": "#d95d39", "dead-end": "#9aa5b1"}
    rows = "".join('<tr><td>%s</td><td><span class="pill" style="background:%s">%s</span></td><td>%s</td><td>%s</td></tr>'
                   % (f, colors.get(st, "#9aa5b1"), st, d, note) for f, d, st, note in FINDINGS)
    board = ('<div class="card"><h3>Findings board from the multi-agent sweep</h3><p class="note">Twelve finder agents searched the corpus and the web with different lenses; '
             'each finding was re-run by a second agent and attacked by a third. Green survived both. Orange was not re-checked. Red reproduced but the conclusion failed.</p>'
             '<div class="scroll"><table class="grid board"><tr><th>Finding</th><th>Status</th><th>Leans</th><th>Source and note</th></tr>%s</table></div></div>' % rows)
    think, intu, qs = GUIDE
    guide = ('<div class="guide"><div class="think"><b>How to think about this</b><p>%s</p></div><div class="intu"><b>Research intuitions</b><ul>%s</ul></div>'
             '<div class="ask"><b>Questions to ask of the corpus</b><ol>%s</ol></div></div>' % (think, "".join("<li>%s</li>" % i for i in intu), "".join("<li>%s</li>" % q for q in qs)))
    return '<h2 id="corpus">The research corpus: what we built and what it found</h2><p class="note">%s</p>%s%s%s' % (INTRO, guide, board, "\n".join(cards))
