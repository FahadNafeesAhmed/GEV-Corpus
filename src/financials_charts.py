"""Build the GE Vernova financials web page: every chart in financials_chart_defs.py,
each with a plain-language note, plus headline tiles and the data tables.

Reads  data/financials/<ticker>_quarterly.csv, _segments.csv, _operational.csv
Writes data/financials/charts/*.png and data/financials/index.html

Usage:  python src/financials_charts.py [TICKER]
"""
import base64
import html
import io
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

import financials_chart_defs as defs
import financials_intuition as guide
import corpus_charts
import research_section
import decision_section

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "financials"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BN = 1e9

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.titlesize": 12, "axes.titleweight": "bold",
                     "axes.edgecolor": "#888", "axes.labelcolor": "#333", "xtick.color": "#333", "ytick.color": "#333",
                     "figure.facecolor": "white", "axes.facecolor": "white"})


def quarter_cols(df, since=2024):
    cols = [c for c in df.columns if re.match(r"Q\d \d{4}", c) and int(c[3:]) >= since]
    return sorted(cols, key=lambda c: (int(c[3:]), int(c[1])))


def make_helpers(cols):
    def xticks(ax):
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols, rotation=45, ha="right", fontsize=9)

    def new(height=4.4):
        fig, ax = plt.subplots(figsize=(10, height))
        ax.grid(axis="y", alpha=0.3)
        ax.spines[["top", "right"]].set_visible(False)

        def bars(ax_, values, label, color, bottom=None, width=0.7):
            x = range(len(cols))
            ax_.bar(x, values.values, width=width, label=label, color=color, bottom=None if bottom is None else bottom.values)
            xticks(ax_)
        return fig, ax, bars

    def line(ax, values, label, color):
        ax.plot(range(len(cols)), values.values, marker="o", label=label, color=color, linewidth=2)
        xticks(ax)

    def label_last(ax, values, fmt):
        v = values.dropna()
        if len(v):
            i = list(values.index).index(v.index[-1])
            below = v.iloc[-1] < 0
            ax.annotate(fmt % v.iloc[-1], (i, v.iloc[-1]), ha="center", va="top" if below else "bottom",
                        xytext=(0, -3 if below else 3), textcoords="offset points", fontsize=9, fontweight="bold")
    return {"new": new, "line": line, "label_last": label_last, "xticks": xticks}


def fig_b64(fig, path):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=125, bbox_inches="tight")
    plt.close(fig)
    path.write_bytes(buf.getvalue())
    return base64.b64encode(buf.getvalue()).decode()


def last(q, metric, cols):
    if metric not in q.index:
        return None
    v = pd.to_numeric(q.loc[metric, cols], errors="coerce").dropna()
    return (v.index[-1], v.iloc[-1]) if len(v) else None


def tiles(q, cols):
    items = [("Revenue", "Revenues", "$%.1fB", BN), ("Operating income", "OperatingIncome", "$%.2fB", BN),
             ("Cash from operations", "CashFromOps", "$%.1fB", BN), ("Customer deposits", "ContractLiabilities", "$%.1fB", BN),
             ("Backlog (RPO)", "RPO", "$%.0fB", BN), ("Service-contract revision", "LTSA_ProfitRevision", "$%.0fM", 1e6)]
    out = []
    for label, metric, fmt, div in items:
        r = last(q, metric, cols)
        if r:
            out.append('<div class="tile"><div class="k">%s</div><div class="v">%s</div><div class="p">%s</div></div>' % (label, fmt % (r[1] / div), r[0]))
    return '<div class="tiles">%s</div>' % "".join(out)


def table_html(df, cols, scale=BN, fmt="%.2f"):
    t = df[cols].astype(object)
    for m in t.index:
        t.loc[m] = t.loc[m].map(lambda v: "" if pd.isna(v) else fmt % (v / scale))
    return t.to_html(border=0, classes="grid")


STYLE = """
body{font-family:Segoe UI,system-ui,Arial,sans-serif;margin:0;background:#f6f7f9;color:#1f2933}
.wrap{max-width:1100px;margin:0 auto;padding:24px 20px 60px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:20px;margin:40px 0 12px;padding-top:12px;border-top:2px solid #dde3ea}
h3{font-size:16px;margin:0 0 8px}.sub{color:#52606d;font-size:14px;margin-bottom:18px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin:18px 0 6px}
.tile{background:#fff;border:1px solid #e1e6ec;border-radius:10px;padding:12px 14px}
.tile .k{font-size:12px;color:#52606d}.tile .v{font-size:22px;font-weight:700;margin:2px 0}.tile .p{font-size:11px;color:#7b8794}
.toc{background:#fff;border:1px solid #e1e6ec;border-radius:10px;padding:12px 16px;font-size:13px;margin:16px 0}
.toc a{color:#1d4e89;text-decoration:none;margin-right:14px;white-space:nowrap;line-height:1.9}
.card{background:#fff;border:1px solid #e1e6ec;border-radius:12px;padding:16px 18px;margin:14px 0}
.card img{width:100%;height:auto;border-radius:6px}
.row{display:grid;grid-template-columns:minmax(0,3fr) minmax(220px,1fr);gap:14px;align-items:start}
@media(max-width:760px){.row{grid-template-columns:1fr}}
.askbox{background:#fff8ec;border:1px solid #f1dfb8;border-radius:8px;padding:10px 12px;font-size:13px;line-height:1.45}
.askbox b{display:block;color:#8a5a00;font-size:12px;text-transform:uppercase;letter-spacing:.04em;margin-bottom:4px}
.askbox ul{margin:0;padding-left:18px}.askbox li{margin:4px 0}
.guide{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:12px;margin:0 0 14px;font-size:13.5px;line-height:1.5}
@media(max-width:900px){.guide{grid-template-columns:1fr}}
.guide>div{background:#fff;border:1px solid #e1e6ec;border-radius:12px;padding:12px 14px}
.guide b{display:block;color:#1d4e89;font-size:12px;text-transform:uppercase;letter-spacing:.04em;margin-bottom:6px}
.guide .ask{background:#fff8ec;border-color:#f1dfb8}.guide .ask b{color:#8a5a00}
.guide p{margin:0}.guide ul,.guide ol{margin:0;padding-left:18px}.guide li{margin:4px 0}
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-top:12px;font-size:13.5px;line-height:1.5}
.notes div{background:#f6f7f9;border-radius:8px;padding:10px 12px}.notes b{display:block;color:#1d4e89;margin-bottom:3px;font-size:12px;text-transform:uppercase;letter-spacing:.04em}
table.grid{border-collapse:collapse;font-size:11.5px;width:100%;background:#fff}
table.grid th,table.grid td{border-bottom:1px solid #eceff3;padding:4px 7px;text-align:right;white-space:nowrap}
table.grid th:first-child,table.grid td:first-child{text-align:left;font-weight:600}
.scroll{overflow-x:auto;border:1px solid #e1e6ec;border-radius:10px;background:#fff}
p.note{color:#52606d;font-size:13px}
.pill{color:#fff;border-radius:999px;padding:2px 8px;font-size:11px;white-space:nowrap}
table.board td{white-space:normal;text-align:left;vertical-align:top;font-size:12px}table.board th{text-align:left}
"""


def main(ticker="GEV"):
    t = ticker.lower()
    q = pd.read_csv(OUT / ("%s_quarterly.csv" % t), index_col=0)
    s = pd.read_csv(OUT / ("%s_segments.csv" % t))
    ops_path = OUT / ("%s_operational.csv" % t)
    ops = pd.read_csv(ops_path, index_col=0) if ops_path.exists() else pd.DataFrame()
    cols = quarter_cols(q)
    ctx = {"q": q, "s": s, "ops": ops, "cols": cols, **make_helpers(cols)}
    (OUT / "charts").mkdir(exist_ok=True)
    body, toc, n = [], [], 0
    for section, names in defs.SECTIONS:
        anchor = re.sub(r"[^a-z]+", "-", section.lower())
        toc.append('<a href="#%s">%s</a>' % (anchor, html.escape(section)))
        body.append('<h2 id="%s">%s</h2>' % (anchor, html.escape(section)))
        if section in guide.SECTION_GUIDE:
            think, intuitions, questions = guide.SECTION_GUIDE[section]
            body.append('<div class="guide"><div class="think"><b>How to think about this</b><p>%s</p></div>'
                        '<div class="intu"><b>Market intuitions</b><ul>%s</ul></div>'
                        '<div class="ask"><b>Questions a top analyst asks</b><ol>%s</ol></div></div>'
                        % (html.escape(think), "".join("<li>%s</li>" % html.escape(i) for i in intuitions),
                           "".join("<li>%s</li>" % html.escape(qn) for qn in questions)))
        for name in names:
            title, what, why, watch = defs.NOTES[name]
            try:
                fig = defs.CHARTS[name](ctx)
                fig.axes[0].set_title(title, loc="left")
                b64 = fig_b64(fig, OUT / "charts" / ("%s.png" % name))
                n += 1
            except Exception as e:  # a missing metric should not kill the page
                print("chart %s failed: %s" % (name, e))
                continue
            qs = "".join("<li>%s</li>" % html.escape(x) for x in guide.CHART_QUESTIONS.get(name, []))
            body.append('<div class="card"><h3>%s</h3><div class="row"><img alt="%s" src="data:image/png;base64,%s">'
                        '<div class="askbox"><b>Ask yourself</b><ul>%s</ul></div></div>'
                        '<div class="notes"><div><b>What it is</b>%s</div><div><b>Why it matters</b>%s</div><div><b>What to watch</b>%s</div></div></div>'
                        % (html.escape(title), html.escape(title), b64, qs, html.escape(what), html.escape(why), html.escape(watch)))
    corpus_html = corpus_charts.render(fig_b64, OUT / "charts") if ticker.upper() == "GEV" else ""
    research_html = research_section.render(fig_b64, OUT / "charts") if ticker.upper() == "GEV" else ""
    decision_html = decision_section.render(fig_b64, OUT / "charts") if ticker.upper() == "GEV" else ""
    tables = '<h2 id="data">Data tables</h2><p class="note">Quarters since 2024. Dollar figures in $ billions unless noted. EPS in dollars, shares in millions.</p>'
    tables += '<h3>Company metrics</h3><div class="scroll">%s</div>' % table_html(q.drop(index=[m for m in ("EPS_diluted", "SharesDiluted", "EffectiveTaxRate") if m in q.index]), cols)
    for m, fmt, sc in (("EPS_diluted", "%.2f", 1.0), ("SharesDiluted", "%.0f", 1e6), ("EffectiveTaxRate", "%.1f%%", 0.01)):
        if m in q.index:
            tables += '<h3>%s</h3><div class="scroll">%s</div>' % (m, table_html(q.loc[[m]], cols, sc, fmt))
    seg = s.set_index(["concept", "member"])
    tables += '<h3>Segment data ($ billions)</h3><div class="scroll">%s</div>' % table_html(seg[[c for c in cols if c in seg.columns]], [c for c in cols if c in seg.columns])
    if len(ops):
        oc = [c for c in cols if c in ops.columns]
        tables += '<h3>Gas turbine gigawatts (from press releases)</h3><div class="scroll">%s</div>' % table_html(ops, oc, 1.0, "%.0f")
    page = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s reported financials</title><style>%s</style></head><body><div class="wrap">
<h1>%s: what the SEC filings say, in charts</h1>
<div class="sub">Every number comes from the company's own 10-K and 10-Q filings, read from the XBRL data attached to each one, plus its quarterly earnings press releases.
Q4 and cash-flow quarters are derived by subtracting year-to-date figures. Nothing here is a forecast. Rebuild with <code>python src/financials_dump.py</code> then <code>python src/financials_charts.py</code>.</div>
%s
<div class="toc">%s <a href="#corpus">Research corpus</a> <a href="#research">Technical research</a> <a href="#decision">The decision</a> <a href="#data">Data tables</a></div>
%s
%s
%s
%s
%s
</div></body></html>""" % (ticker, STYLE, ticker, tiles(q, cols), " ".join(toc), "\n".join(body), corpus_html, research_html, decision_html, tables)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    print("wrote %d charts -> %s" % (n, OUT / "index.html"))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "GEV")
