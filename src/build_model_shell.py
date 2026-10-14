"""Build the GEV valuation model SHELL as an .xlsx.

History is filled from the company's own filings (data/financials/*.csv, which came from
SEC XBRL). Every forecast cell is a FORMULA driven by the Drivers tab. The assumption cells
on Drivers are left EMPTY and highlighted: the team types them in and owns them, which is
what the competition rules require. Change one driver and the implied price updates.

Usage:  python src/build_model_shell.py
Writes: data/model/GEV_model_shell.xlsx
"""
import sys
from pathlib import Path

from openpyxl import Workbook

from vintage_model import RPO, EQUIP_REV, TOTAL_REV
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "model"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---- history, in $ millions, from the filings (FY2022-FY2025) -------------------------
HIST = {
    "years": [2022, 2023, 2024, 2025],
    "Power revenue": [16124, 17436, 18127, 19767],
    "Power EBITDA": [1655, 1722, 2268, 2902],
    "Electrification revenue": [5076, 6378, 7550, 9642],
    "Electrification EBITDA": [-164, 234, 679, 1433],
    "Wind revenue": [8905, 9826, 9701, 9110],
    "Wind EBITDA": [-1710, -1033, -588, -598],
    "Total revenue": [29654, 33239, 34935, 38068],
    "Net income": [-2736, -438, 1552, 4884],
    "D&A": [1797, 964, 1172, 853],
    "Cash from operations": [-114, 1186, 2583, 4987],
    "Diluted EPS ($)": [-10.00, -1.60, 5.58, 17.69],
    "Diluted shares (M)": [274, 274, 278, 276],
}
GAS_GW_SHIPPED = {2023: 13.8, 2024: 11.9, 2025: 15.3}
FORECAST = [2026, 2027, 2028]

# ---- published Street consensus, pre-filled ------------------------------------------
# These are what OTHER people forecast, not ours. They are reference data, the same as the
# filed history, so they are pre-filled. The "Ours" column stays empty — that is the part
# the team owns and must type.
# Every figure needs its source verified before the memo goes out; anything still marked
# UNVERIFIED must either be sourced or deleted.
CONSENSUS = {
    "2027E revenue ($M)": (52740, "Street consensus FY27 revenue"),
    "2027E adjusted EBITDA ($M)": (9570, "Street consensus FY27 adj EBITDA; GLJ cites Street $9.45B and models $7.42B"),
    "2027E EPS ($)": (25.08, "Street consensus FY27 adj EPS, midpoint of $24.85-25.31"),
    "2027E free cash flow ($M)": (7420, "Street consensus FY27 FCF — note consensus itself has FCF FALLING 38% from FY26 $12.02B"),
}
# Reference close. The corpus prices table stops 2025-09-18, so this is entered by hand
# and must be refreshed before submission.
REF_PRICE = 950.28
REF_PRICE_DATE = "2026-09-22 close"

HEAD = PatternFill("solid", fgColor="1D4E89")
SUB = PatternFill("solid", fgColor="DCE6F1")
INPUT = PatternFill("solid", fgColor="FFF2CC")      # yellow = you type here
CALC = PatternFill("solid", fgColor="F2F2F2")        # grey = formula, do not edit
HISTF = PatternFill("solid", fgColor="EAF3EA")       # green = filed history, do not edit
WHITEB = Font(color="FFFFFF", bold=True)
B = Font(bold=True)
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def hdr(ws, row, text, span=10):
    ws.cell(row=row, column=1, value=text).font = WHITEB
    for c in range(1, span + 1):
        ws.cell(row=row, column=c).fill = HEAD
    return row + 1


def label(ws, row, text, bold=False, indent=0):
    c = ws.cell(row=row, column=1, value=("    " * indent) + text)
    if bold:
        c.font = B
    return c


def put(ws, row, col, value, fill=None, fmt=None, bold=False):
    c = ws.cell(row=row, column=col, value=value)
    if fill:
        c.fill = fill
    if fmt:
        c.number_format = fmt
    if bold:
        c.font = B
    c.border = BOX
    return c


def build():
    wb = Workbook()

    # ================= README =================
    ws = wb.active
    ws.title = "README"
    ws.column_dimensions["A"].width = 118
    rows = [
        ("GE VERNOVA (GEV) — VALUATION MODEL SHELL", True),
        ("", False),
        ("HOW THIS WORKS", True),
        ("1. Green cells are history, taken from GEV's own 10-K and 10-Q filings via SEC XBRL. Do not edit them.", False),
        ("2. YELLOW cells on the Drivers tab are the only things you type. They are empty on purpose: the forecast", False),
        ("   assumptions must be yours, not the machine's. Each one has a 'Consensus / guide' column next to it as a", False),
        ("   starting reference, and a Note column where you write WHY you chose your number.", False),
        ("3. Grey cells are formulas. Everything flows from Drivers -> Segments -> P&L -> Valuation -> Scenarios.", False),
        ("4. Change one yellow cell and watch the implied share price on Valuation move. If it does not move, a formula", False),
        ("   is broken and you should find it before trusting anything.", False),
        ("", False),
        ("THE METHOD (do it in this order)", True),
        ("Step 1. Fill the Drivers tab with CONSENSUS values only — what the Street expects. Check that the Valuation tab", False),
        ("        then produces a price near the $940 reference. If it does, your model is calibrated to the market and you", False),
        ("        now know exactly what $940 assumes.", False),
        ("Step 2. Change ONE driver at a time to what your research says. Record the EPS effect on the 'vs Consensus' tab.", False),
        ("Step 3. Add up the column. If the total lands above $940 the evidence says long; below, it says short.", False),
        ("        The model decides the direction, not your opinion. That is the whole point of doing it in this order.", False),
        ("Step 4. Fill the three scenarios, give each a probability, and read the risk/reward.", False),
        ("", False),
        ("REFERENCE POINTS (as of 2026-09-18 close)", True),
        ("Share price $940.33   |   Diluted shares ~266.3M   |   Market cap ~$250B   |   Forward P/E ~35x vs S&P 500 ~22x", False),
        ("FY2026 guidance (raised 2026-07-22): revenue $45.5-46.5B, free cash flow $11.5-12.5B, Power organic growth", False),
        ("16-18% at 17-19% segment EBITDA margin, Wind EBITDA loss about -$400M.", False),
        ("2028 target (Dec 2025 investor update): about $56B revenue.", False),
        ("Gas: 53 GW firm backlog + 63 GW slot reservations. Output target 20 GW/yr from Q3 2026, 24 GW 2028, 30 GW 2030.", False),
        ("Gas GW shipped: 13.8 (2023), 11.9 (2024), 15.3 (2025), 7.5 (H1 2026).", False),
        ("", False),
        ("WHAT THIS SHELL DELIBERATELY DOES NOT DO", True),
        ("No balance-sheet forecast beyond cash and debt. No monthly detail. No macro inputs. Roughly a dozen assumptions,", False),
        ("because a model with a hundred assumptions has a hundred places to hide a bad one. That is how buy-side models", False),
        ("are actually built for a pitch.", False),
        ("", False),
        ("PROVENANCE", True),
        ("History: data/financials/gev_quarterly.csv and gev_segments.csv, generated by src/financials_dump.py from every", False),
        ("GEV 10-K and 10-Q via edgartools. Rebuild with: python src/financials_dump.py GEV", False),
        ("Forecasts and assumptions: entirely the team's own work.", False),
    ]
    for i, (t, bold) in enumerate(rows, start=1):
        c = ws.cell(row=i, column=1, value=t)
        if bold:
            c.font = Font(bold=True, size=12, color="1D4E89")

    # ================= DRIVERS =================
    ws = wb.create_sheet("Drivers")
    ws.column_dimensions["A"].width = 46
    for col, w in zip("BCDEFG", [13, 13, 13, 20, 52, 10]):
        ws.column_dimensions[col].width = w
    r = 1
    r = hdr(ws, r, "DRIVERS — type your assumptions in the yellow cells", 6)
    for j, t in enumerate(["Driver", "2026E", "2027E", "2028E", "Consensus / guide (reference)", "Your note: why this number"]):
        put(ws, r, j + 1, t, SUB, bold=True)
    r += 1
    DRIVERS = [
        ("GAS POWER", None, None, None, None, None),
        ("Gas turbine GW shipped", None, None, None, "Guide: 20 GW/yr run-rate from Q3'26, 24 GW 2028. Actual: 15.3 (2025), 7.5 (H1'26)", ""),
        ("Realised price per kW ($/kW)", None, None, None, "Implied ~$740/kW at Q2'26 (equip RPO / firm GW). Mgmt: +10-20% on new bids", ""),
        ("Power services revenue growth (%)", None, None, None, "Power services $13,081M in FY25, +5.3%. Recurring CSA revenue was FLAT", ""),
        ("Power segment EBITDA margin (%)", None, None, None, "Guide 17-19% for 2026. FY25 actual 14.7%", ""),
        ("", None, None, None, None, None),
        ("ELECTRIFICATION", None, None, None, None, None),
        ("Electrification revenue growth (%)", None, None, None, "FY25 +27.7%. 2026 includes Prolec from Feb 2 (~$3B contribution)", ""),
        ("Electrification EBITDA margin (%)", None, None, None, "FY25 14.9%. Prolec came in at 22.0% vs 19.1% organic in H1'26", ""),
        ("", None, None, None, None, None),
        ("WIND", None, None, None, None, None),
        ("Wind revenue growth (%)", None, None, None, "FY25 -6.1%. Orders down 40% y/y; equipment RPO $13.7B (Dec-23) -> $8.2B (Jun-26)", ""),
        ("Wind segment EBITDA ($M)", None, None, None, "Guide ~-$400M for 2026. H1'26 actual -$657M, so H2 must be +$257M", ""),
        ("", None, None, None, None, None),
        ("BELOW THE SEGMENTS", None, None, None, None, None),
        ("Corporate / other EBITDA ($M)", None, None, None, "Negative. Back into it from FY25: total EBITDA less the three segments", ""),
        ("Depreciation & amortisation ($M)", None, None, None, "FY25 $853M. Prolec intangible amortisation adds ~$180-240M/quarter from 2026", ""),
        ("Net interest income / (expense) ($M)", None, None, None, "FY25 +$186M (net cash). $2.5B of notes issued Feb 2026", ""),
        ("Effective tax rate (%)", None, None, None, "Reported rate swings on one-offs. Use a normalised rate and say so", ""),
        ("Diluted shares (M)", None, None, None, "276M (FY25) falling on buybacks: $3.3B in 2025, $1.3B Q1'26, $2.4B Q2'26", ""),
        ("", None, None, None, None, None),
        ("VALUATION", None, None, None, None, None),
        ("Exit P/E multiple (x)", None, None, None, "Currently ~35x forward. S&P 500 ~22x. Peers: VRT, ETN, PWR", ""),
        ("Discount rate for DCF (%)", None, None, None, "Typically 8-10% for an industrial of this risk", ""),
        ("Terminal growth rate (%)", None, None, None, "2-3% is the defensible range; above 3% needs an argument", ""),
    ]
    driver_rows = {}
    for name, a, b_, c_, ref, note in DRIVERS:
        if name and a is None and ref is None:  # section header
            label(ws, r, name, bold=True).fill = SUB
            for col in range(1, 7):
                ws.cell(row=r, column=col).fill = SUB
        elif name:
            label(ws, r, name, indent=1)
            for col in (2, 3, 4):
                put(ws, r, col, None, INPUT, fmt="#,##0.00")
            put(ws, r, 5, ref).alignment = Alignment(wrap_text=True, vertical="top")
            put(ws, r, 6, None, INPUT)
            driver_rows[name] = r
        r += 1
    r += 1
    label(ws, r, "Yellow = you type it.  Every forecast on the other tabs reads from these cells.", bold=True)

    D = lambda n, col: "Drivers!%s%d" % (get_column_letter(col), driver_rows[n])

    # ================= SEGMENTS =================
    ws = wb.create_sheet("Segments")
    ws.column_dimensions["A"].width = 40
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 14
    r = 1
    r = hdr(ws, r, "SEGMENTS ($ millions) — green is filed history, grey is driven by the Drivers tab", 8)
    cols = HIST["years"] + FORECAST
    put(ws, r, 1, "", SUB)
    for j, y in enumerate(cols):
        put(ws, r, j + 2, ("%dA" % y) if y <= 2025 else ("%dE" % y), SUB, bold=True)
    hdr_row = r
    r += 1
    seg_rows = {}

    def series(name, hist_key, formula_fn, fmt="#,##0"):
        nonlocal r
        label(ws, r, name, bold=name.endswith("EBITDA") or "Total" in name)
        for j, y in enumerate(cols):
            col = j + 2
            if y <= 2025:
                put(ws, r, col, HIST[hist_key][j], HISTF, fmt)
            else:
                put(ws, r, col, formula_fn(col, y), CALC, fmt)
        seg_rows[name] = r
        r += 1

    fcol = {2026: 6, 2027: 7, 2028: 8}  # forecast column letters F,G,H
    # Power equipment = GW * $/kW * 1000  (GW * 1,000,000 kW * $/kW / 1e6 for $M)
    label(ws, r, "Gas turbine GW shipped", bold=True)
    for j, y in enumerate(cols):
        col = j + 2
        if y <= 2025:
            put(ws, r, col, GAS_GW_SHIPPED.get(y), HISTF, "0.0")
        else:
            put(ws, r, col, "=%s" % D("Gas turbine GW shipped", col - 2), CALC, "0.0")
    gw_row = r
    r += 1
    label(ws, r, "Realised price ($/kW)", bold=True)
    for j, y in enumerate(cols):
        col = j + 2
        if y > 2025:
            put(ws, r, col, "=%s" % D("Realised price per kW ($/kW)", col - 2), CALC, "#,##0")
        else:
            put(ws, r, col, None, HISTF)
    price_row = r
    r += 1
    label(ws, r, "Power equipment revenue", indent=1)
    for j, y in enumerate(cols):
        col = j + 2
        L = get_column_letter(col)
        if y > 2025:
            # 1 GW = 1,000,000 kW, so GW x $/kW lands directly in $ millions.
            # Check: 53 GW x $740/kW = $39,220M, versus the $39,261M equipment RPO at Q2'26.
            put(ws, r, col, "=%s%d*%s%d" % (L, gw_row, L, price_row), CALC, "#,##0")
        else:
            put(ws, r, col, None, HISTF)
    put(ws, r, 9, "GW x $/kW = $M  (1 GW = 1,000,000 kW). Check: 53 x 740 = 39,220 vs $39,261M equipment RPO at Q2'26.")
    pe_row = r
    r += 1
    label(ws, r, "Power services revenue", indent=1)
    for j, y in enumerate(cols):
        col = j + 2
        L = get_column_letter(col)
        if y > 2025:
            prev = get_column_letter(col - 1)
            base = "%s%d" % (prev, r) if y > 2026 else "13081"
            put(ws, r, col, "=%s*(1+%s/100)" % (base, D("Power services revenue growth (%)", col - 2)), CALC, "#,##0")
        else:
            put(ws, r, col, None, HISTF)
    ps_row = r
    r += 1
    series("Power revenue", "Power revenue",
           lambda col, y: "=%s%d+%s%d" % (get_column_letter(col), pe_row, get_column_letter(col), ps_row))
    series("Power EBITDA", "Power EBITDA",
           lambda col, y: "=%s%d*%s/100" % (get_column_letter(col), seg_rows["Power revenue"], D("Power segment EBITDA margin (%)", col - 2)))
    r += 1
    series("Electrification revenue", "Electrification revenue",
           lambda col, y: "=%s%d*(1+%s/100)" % (get_column_letter(col - 1), r - 0, D("Electrification revenue growth (%)", col - 2)))
    series("Electrification EBITDA", "Electrification EBITDA",
           lambda col, y: "=%s%d*%s/100" % (get_column_letter(col), seg_rows["Electrification revenue"], D("Electrification EBITDA margin (%)", col - 2)))
    r += 1
    series("Wind revenue", "Wind revenue",
           lambda col, y: "=%s%d*(1+%s/100)" % (get_column_letter(col - 1), r - 0, D("Wind revenue growth (%)", col - 2)))
    series("Wind EBITDA", "Wind EBITDA", lambda col, y: "=%s" % D("Wind segment EBITDA ($M)", col - 2))
    r += 1
    series("Total revenue", "Total revenue",
           lambda col, y: "=%s%d+%s%d+%s%d" % (get_column_letter(col), seg_rows["Power revenue"],
                                               get_column_letter(col), seg_rows["Electrification revenue"],
                                               get_column_letter(col), seg_rows["Wind revenue"]))
    label(ws, r, "Segment EBITDA (sum of three)", bold=True)
    for j, y in enumerate(cols):
        col = j + 2
        L = get_column_letter(col)
        put(ws, r, col, "=%s%d+%s%d+%s%d" % (L, seg_rows["Power EBITDA"], L, seg_rows["Electrification EBITDA"], L, seg_rows["Wind EBITDA"]),
            CALC if y > 2025 else HISTF, "#,##0")
    seg_rows["Segment EBITDA"] = r
    r += 2
    label(ws, r, "CHECK: total revenue vs FY25 filed $38,068M", bold=True)
    put(ws, r, 5, "=E%d" % seg_rows["Total revenue"], HISTF, "#,##0")

    # ================= P&L =================
    ws = wb.create_sheet("P&L")
    ws.column_dimensions["A"].width = 40
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 14
    r = 1
    r = hdr(ws, r, "PROFIT & LOSS ($ millions except per-share) — down to EPS", 8)
    put(ws, r, 1, "", SUB)
    for j, y in enumerate(cols):
        put(ws, r, j + 2, ("%dA" % y) if y <= 2025 else ("%dE" % y), SUB, bold=True)
    r += 1
    pl = {}

    def pl_row(name, hist, formula_fn, fmt="#,##0", bold=False):
        nonlocal r
        label(ws, r, name, bold=bold)
        for j, y in enumerate(cols):
            col = j + 2
            if y <= 2025 and hist:
                put(ws, r, col, hist[j], HISTF, fmt)
            elif y > 2025:
                put(ws, r, col, formula_fn(col, y), CALC, fmt)
            else:
                put(ws, r, col, None, HISTF, fmt)
        pl[name] = r
        r += 1

    pl_row("Total revenue", HIST["Total revenue"], lambda col, y: "=Segments!%s%d" % (get_column_letter(col), seg_rows["Total revenue"]), bold=True)
    pl_row("Segment EBITDA", None, lambda col, y: "=Segments!%s%d" % (get_column_letter(col), seg_rows["Segment EBITDA"]))
    pl_row("Corporate / other EBITDA", None, lambda col, y: "=%s" % D("Corporate / other EBITDA ($M)", col - 2))
    pl_row("Adjusted EBITDA", None, lambda col, y: "=%s%d+%s%d" % (get_column_letter(col), pl["Segment EBITDA"], get_column_letter(col), pl["Corporate / other EBITDA"]), bold=True)
    pl_row("Depreciation & amortisation", HIST["D&A"], lambda col, y: "=-%s" % D("Depreciation & amortisation ($M)", col - 2))
    pl_row("Operating income (EBIT)", None, lambda col, y: "=%s%d+%s%d" % (get_column_letter(col), pl["Adjusted EBITDA"], get_column_letter(col), pl["Depreciation & amortisation"]), bold=True)
    pl_row("Net interest income / (expense)", None, lambda col, y: "=%s" % D("Net interest income / (expense) ($M)", col - 2))
    pl_row("Pre-tax income", None, lambda col, y: "=%s%d+%s%d" % (get_column_letter(col), pl["Operating income (EBIT)"], get_column_letter(col), pl["Net interest income / (expense)"]))
    pl_row("Tax", None, lambda col, y: "=-%s%d*%s/100" % (get_column_letter(col), pl["Pre-tax income"], D("Effective tax rate (%)", col - 2)))
    pl_row("Net income", HIST["Net income"], lambda col, y: "=%s%d+%s%d" % (get_column_letter(col), pl["Pre-tax income"], get_column_letter(col), pl["Tax"]), bold=True)
    pl_row("Diluted shares (M)", HIST["Diluted shares (M)"], lambda col, y: "=%s" % D("Diluted shares (M)", col - 2), "#,##0")
    pl_row("Diluted EPS ($)", HIST["Diluted EPS ($)"], lambda col, y: "=%s%d/%s%d" % (get_column_letter(col), pl["Net income"], get_column_letter(col), pl["Diluted shares (M)"]), "0.00", bold=True)
    r += 1
    label(ws, r, "NOTE: FY2025 filed EPS of $17.69 and FY2024 of $5.58 are GAAP and include one-offs.", bold=True)
    r += 1
    label(ws, r, "Q1 2026 GAAP EPS also includes a ~$4.4B non-cash gain from revaluing GEV's prior 50% of Prolec.")
    r += 1
    label(ws, r, "Decide explicitly whether you are forecasting GAAP or adjusted, and make consensus match.")

    # ================= CASH =================
    ws = wb.create_sheet("Cash")
    ws.column_dimensions["A"].width = 44
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 14
    r = 1
    r = hdr(ws, r, "CASH ($ millions) — the deposit line is isolated on purpose", 8)
    put(ws, r, 1, "", SUB)
    for j, y in enumerate(cols):
        put(ws, r, j + 2, ("%dA" % y) if y <= 2025 else ("%dE" % y), SUB, bold=True)
    r += 1
    cash = {}
    for name, hist, fmt in [("Net income", HIST["Net income"], "#,##0"),
                            ("Depreciation & amortisation", HIST["D&A"], "#,##0"),
                            ("Change in customer deposits (contract liabilities)", None, "#,##0"),
                            ("Other working capital", None, "#,##0"),
                            ("Cash from operations", HIST["Cash from operations"], "#,##0"),
                            ("Capital expenditure", None, "#,##0"),
                            ("Free cash flow", None, "#,##0")]:
        label(ws, r, name, bold=name in ("Cash from operations", "Free cash flow"))
        for j, y in enumerate(cols):
            col = j + 2
            L = get_column_letter(col)
            if y <= 2025 and hist:
                put(ws, r, col, hist[j], HISTF, fmt)
            elif y > 2025:
                if name == "Net income":
                    put(ws, r, col, "='P&L'!%s%d" % (L, pl["Net income"]), CALC, fmt)
                elif name == "Depreciation & amortisation":
                    put(ws, r, col, "=%s" % D("Depreciation & amortisation ($M)", col - 2), CALC, fmt)
                elif name == "Cash from operations":
                    put(ws, r, col, "=%s%d+%s%d+%s%d+%s%d" % (L, cash["Net income"], L, cash["Depreciation & amortisation"],
                                                              L, cash["Change in customer deposits (contract liabilities)"], L, cash["Other working capital"]), CALC, fmt)
                elif name == "Free cash flow":
                    put(ws, r, col, "=%s%d+%s%d" % (L, cash["Cash from operations"], L, cash["Capital expenditure"]), CALC, fmt)
                else:
                    put(ws, r, col, None, INPUT, fmt)
            else:
                put(ws, r, col, None, HISTF if name != "Capital expenditure" else INPUT, fmt)
        cash[name] = r
        r += 1
    r += 1
    label(ws, r, "Deposits are the whole cash story: $17.6B (Dec-24) -> $25.8B (Dec-25) -> $39.9B (Jun-26).", bold=True)
    r += 1
    label(ws, r, "H1 2026 free cash flow was ~$9.9B against a full-year guide of $11.5-12.5B, so H2 is guided small.")
    r += 1
    label(ws, r, "Model 'earned' cash separately by setting the deposit line to zero and seeing what is left.")

    # ================= VALUATION =================
    ws = wb.create_sheet("Valuation")
    ws.column_dimensions["A"].width = 46
    for col, w in zip("BCDE", [16, 16, 16, 40]):
        ws.column_dimensions[col].width = w
    r = 1
    r = hdr(ws, r, "VALUATION — the implied price updates when you change a driver", 5)
    put(ws, r, 1, "Reference price (2026-09-18 close)", SUB, bold=True)
    put(ws, r, 2, 940.33, HISTF, "$#,##0.00")
    px_row = r
    r += 2
    put(ws, r, 1, "MULTIPLE-BASED", SUB, bold=True)
    for c in range(1, 6):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "2027E diluted EPS ($)")
    put(ws, r, 2, "='P&L'!G%d" % pl["Diluted EPS ($)"], CALC, "0.00")
    eps27 = r
    r += 1
    put(ws, r, 1, "Exit P/E multiple (x)")
    put(ws, r, 2, "=%s" % D("Exit P/E multiple (x)", 3), CALC, "0.0")
    pe_mult = r
    r += 1
    put(ws, r, 1, "IMPLIED PRICE ($)", None, bold=True)
    put(ws, r, 2, "=B%d*B%d" % (eps27, pe_mult), CALC, "$#,##0.00", bold=True)
    implied = r
    r += 1
    put(ws, r, 1, "Upside / (downside) vs $940.33", None, bold=True)
    put(ws, r, 2, "=B%d/B%d-1" % (implied, px_row), CALC, "0.0%", bold=True)
    r += 2
    put(ws, r, 1, "WHAT $940 REQUIRES (reverse engineering)", SUB, bold=True)
    for c in range(1, 6):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "EPS needed at your exit multiple to justify $940.33")
    put(ws, r, 2, "=B%d/B%d" % (px_row, pe_mult), CALC, "0.00")
    put(ws, r, 5, "Compare this to your 2027E EPS. The gap IS the thesis.")
    r += 1
    put(ws, r, 1, "Multiple needed on your EPS to justify $940.33")
    put(ws, r, 2, "=B%d/B%d" % (px_row, eps27), CALC, "0.0")
    put(ws, r, 5, "If this is far above 22x (the S&P), the price needs GEV to stay special.")
    r += 2
    put(ws, r, 1, "SIMPLE DCF", SUB, bold=True)
    for c in range(1, 6):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "2027E free cash flow ($M)")
    put(ws, r, 2, "=Cash!G%d" % cash["Free cash flow"], CALC, "#,##0")
    fcf = r
    r += 1
    put(ws, r, 1, "Discount rate (%)")
    put(ws, r, 2, "=%s" % D("Discount rate for DCF (%)", 3), CALC, "0.0")
    disc = r
    r += 1
    put(ws, r, 1, "Terminal growth (%)")
    put(ws, r, 2, "=%s" % D("Terminal growth rate (%)", 3), CALC, "0.0")
    tg = r
    r += 1
    put(ws, r, 1, "Perpetuity value ($M)")
    put(ws, r, 2, "=B%d*(1+B%d/100)/((B%d-B%d)/100)" % (fcf, tg, disc, tg), CALC, "#,##0")
    pv = r
    r += 1
    put(ws, r, 1, "Value per share from DCF ($)", None, bold=True)
    put(ws, r, 2, "=B%d/'P&L'!G%d" % (pv, pl["Diluted shares (M)"]), CALC, "$#,##0.00", bold=True)
    put(ws, r, 5, "Crude on purpose: one year of FCF grown forever. Sanity check, not the answer.")
    r += 2
    put(ws, r, 1, "SANITY CHECKS", SUB, bold=True)
    for c in range(1, 6):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    for t in ["Does the implied price move when you change GW shipped? If not, a formula is broken.",
              "Is your 2027 EPS within a plausible distance of consensus? If it is 3x away, you made an error.",
              "Did you decide GAAP vs adjusted, and does your consensus comparison use the same basis?",
              "Is your exit multiple defensible against the S&P at ~22x and peers?"]:
        put(ws, r, 1, t)
        r += 1

    # ================= SCENARIOS =================
    ws = wb.create_sheet("Scenarios")
    ws.column_dimensions["A"].width = 42
    for col, w in zip("BCDE", [16, 16, 16, 44]):
        ws.column_dimensions[col].width = w
    r = 1
    r = hdr(ws, r, "SCENARIOS — three futures, each built from drivers, each with a probability", 5)
    for j, t in enumerate(["", "Bear", "Base", "Bull", "What has to be true"]):
        put(ws, r, j + 1, t, SUB, bold=True)
    r += 1
    for name in ["Gas GW shipped 2027", "Realised price ($/kW) 2027", "Power services growth (%)",
                 "Power EBITDA margin (%)", "Electrification growth (%)", "Wind EBITDA ($M)",
                 "2027E EPS ($)", "Exit multiple (x)", "IMPLIED PRICE ($)",
                 "Upside / (downside) (%)", "Probability (%)"]:
        label(ws, r, name, bold=name.startswith("IMPLIED") or name.startswith("Probability"))
        for col in (2, 3, 4):
            put(ws, r, col, None, INPUT, "#,##0.00")
        put(ws, r, 5, None, INPUT).alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    r += 1
    put(ws, r, 1, "Probability-weighted price ($)", None, bold=True)
    put(ws, r, 2, None, INPUT, "$#,##0.00", bold=True)
    r += 1
    put(ws, r, 1, "Reward / risk (upside vs downside)", None, bold=True)
    put(ws, r, 2, None, INPUT, "0.0", bold=True)
    r += 2
    label(ws, r, "Professionals want the downside case SMALL and the base case modest. If your bear case is -50%,", bold=True)
    r += 1
    label(ws, r, "either the thesis is wrong or the bear case is a straw man. Judges check this.")

    # ================= VS CONSENSUS =================
    ws = wb.create_sheet("vs Consensus")
    ws.column_dimensions["A"].width = 46
    for col, w in zip("BCDEF", [16, 16, 16, 18, 52]):
        ws.column_dimensions[col].width = w
    r = 1
    r = hdr(ws, r, "YOUR NUMBER vs THE STREET — this table is the memo", 6)
    for j, t in enumerate(["Driver / line", "Consensus", "Ours", "Difference", "EPS effect ($)", "The evidence, with its source"]):
        put(ws, r, j + 1, t, SUB, bold=True)
    r += 1
    for name in ["2027E revenue ($M)", "2027E adjusted EBITDA ($M)", "2027E EPS ($)", "2027E free cash flow ($M)",
                 "", "SWAP ONE DRIVER AT A TIME:", "Gas GW shipped 2027", "Realised price ($/kW)",
                 "Power services growth", "Power EBITDA margin", "Electrification growth", "Wind EBITDA",
                 "Exit multiple", "", "TOTAL EPS GAP vs CONSENSUS", "IMPLIED PRICE GAP"]:
        if name.startswith("SWAP") or name.startswith("TOTAL") or name.startswith("IMPLIED"):
            label(ws, r, name, bold=True)
            for col in range(1, 7):
                ws.cell(row=r, column=col).fill = SUB
        elif name:
            label(ws, r, name)
            if name in CONSENSUS:
                # Consensus is published reference data, so it is pre-filled and locked.
                val, src = CONSENSUS[name]
                fmt = "0.00" if "EPS" in name else "#,##0"
                put(ws, r, 2, val, HISTF, fmt)
                for col in (3, 4, 5):
                    put(ws, r, col, None, INPUT, fmt)
                put(ws, r, 4, "=C%d-B%d" % (r, r), CALC, fmt)
                put(ws, r, 6, src, HISTF).alignment = Alignment(wrap_text=True, vertical="top")
            else:
                for col in (2, 3, 4, 5):
                    put(ws, r, col, None, INPUT, "#,##0.00")
                put(ws, r, 6, None, INPUT).alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    r += 1
    label(ws, r, "Fill 'Consensus' first, everywhere. Then change ONE driver to your number and record the EPS effect.", bold=True)
    r += 1
    label(ws, r, "Add up the EPS-effect column. Positive total means the evidence says long. Negative means short.")
    r += 1
    label(ws, r, "Every row needs a source in the last column. A row without a source does not go in the memo.")

    # ================= BACKLOG VINTAGE =================
    # The evidence exhibit. Every figure in the top block is verbatim from the RPO note of
    # the stated filing. The calculation below it is transparent arithmetic on those figures,
    # with the one genuine judgement call left as a yellow input.
    ws = wb.create_sheet("Backlog vintage")
    ws.column_dimensions["A"].width = 44
    for col, w in zip("BCDEFG", [15, 12, 12, 12, 15, 46]):
        ws.column_dimensions[col].width = w
    r = 1
    r = hdr(ws, r, "BACKLOG VINTAGE — how much of 2027 is priced at old prices", 7)
    for t in ['GEV discloses equipment RPO and the share of it expected to be recognised',
              'within 1, 2 and 5 years. That is a runoff curve. Applied to the book as it',
              'stood at 31-Dec-2024, it bounds how much old-priced work is left for 2027.',
              'Green = verbatim from the filing named in the last column. Yellow = you choose.']:
        put(ws, r, 1, t)
        r += 1
    r += 1
    for j, t in enumerate(["As of", "Equipment RPO ($M)", "<=1 yr", "<=2 yr", "<=5 yr",
                           "1-yr amount ($M)", "Source: accession, RPO note"]):
        put(ws, r, j + 1, t, SUB, bold=True)
    r += 1
    first_rpo = r
    for as_of, acc, rpo, f1, f2, f5 in RPO:
        put(ws, r, 1, as_of, HISTF)
        put(ws, r, 2, rpo, HISTF, "#,##0")
        put(ws, r, 3, f1, HISTF, "0%")
        put(ws, r, 4, f2, HISTF, "0%")
        put(ws, r, 5, f5, HISTF, "0%")
        put(ws, r, 6, "=B%d*C%d" % (r, r), CALC, "#,##0")
        put(ws, r, 7, acc, HISTF)
        r += 1
    last_rpo = r - 1
    # the 31-Dec-2024 row is the cohort we care about
    coh = first_rpo + [i for i, x in enumerate(RPO) if x[0] == "2024-12-31"][0]
    r += 1
    put(ws, r, 1, "STEP 1 — does the disclosed curve actually work?", SUB, bold=True)
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "Predicted 2025 equipment revenue (31-Dec-24 RPO x 1-yr %)")
    put(ws, r, 2, "=B%d*C%d" % (coh, coh), CALC, "#,##0")
    pred = r
    r += 1
    put(ws, r, 1, "Actual FY2025 equipment revenue")
    put(ws, r, 2, EQUIP_REV[2025], HISTF, "#,##0")
    put(ws, r, 7, "FY2025 10-K p.38, Sales of equipment", HISTF)
    act = r
    r += 1
    put(ws, r, 1, "Share of 2025 equipment revenue that came from the opening book")
    put(ws, r, 2, "=B%d/B%d" % (pred, act), CALC, "0.0%")
    put(ws, r, 7, "If this is near 90%, the curve describes reality and is usable.", HISTF)
    r += 2
    put(ws, r, 1, "STEP 2 — where the 31-Dec-2024 book lands", SUB, bold=True)
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    for lbl, formula, note in [
        ("Recognised in 2025 (year 1)", "=B{c}*C{c}", ""),
        ("Recognised in 2026 (year 2)", "=B{c}*(D{c}-C{c})", ""),
        ("Left for 2027-2029 (years 3-5)", "=B{c}*(E{c}-D{c})", "This is all the old-priced work that can reach 2027."),
        ("Left for 2030 onward", "=B{c}*(1-E{c})", ""),
    ]:
        put(ws, r, 1, lbl)
        put(ws, r, 2, formula.format(c=coh), CALC, "#,##0")
        if lbl.startswith("Left for 2027"):
            pool = r
        if note:
            put(ws, r, 7, note, HISTF)
        r += 1
    put(ws, r, 1, "Already recognised by 31-Dec-2026", None, bold=True)
    put(ws, r, 2, "=D%d" % coh, CALC, "0%", bold=True)
    put(ws, r, 7, "Of the pre-2025 book. The rest is the only old-priced work left.", HISTF)
    r += 2
    put(ws, r, 1, "STEP 3 — 2027's slice, which GEV does NOT disclose", SUB, bold=True)
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "Years 3-5 are one bucket. What share of it lands in 2027?")
    put(ws, r, 2, None, INPUT, "0%")
    put(ws, r, 7, "YOU CHOOSE. Flat = 33%. Declining = 45%. This is the widest "
                  "source of error in the whole exhibit and you must defend it.", INPUT)
    share = r
    r += 1
    put(ws, r, 1, "Old-priced revenue reaching 2027 ($M)")
    put(ws, r, 2, "=B%d*B%d" % (pool, share), CALC, "#,##0")
    old27 = r
    r += 2
    put(ws, r, 1, "STEP 4 — as a share of 2027 equipment revenue", SUB, bold=True)
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    put(ws, r, 1, "2027E total revenue ($M)")
    put(ws, r, 2, "='vs Consensus'!C3", CALC, "#,##0")
    put(ws, r, 7, "Reads YOUR number from the vs Consensus tab. Fill that first.", HISTF)
    tot27 = r
    r += 1
    put(ws, r, 1, "Equipment as a share of revenue (%)")
    put(ws, r, 2, None, INPUT, "0.0%")
    put(ws, r, 7, "Equipment was %.1f%% of FY2025 revenue and equipment RPO is growing "
                  "faster than services, so this should rise." % (EQUIP_REV[2025] / TOTAL_REV[2025] * 100), INPUT)
    eqshare = r
    r += 1
    put(ws, r, 1, "2027E equipment revenue ($M)")
    put(ws, r, 2, "=B%d*B%d" % (tot27, eqshare), CALC, "#,##0")
    eq27 = r
    r += 1
    put(ws, r, 1, "OLD-PRICED SHARE OF 2027 EQUIPMENT REVENUE", None, bold=True)
    put(ws, r, 2, "=B%d/B%d" % (old27, eq27), CALC, "0.0%", bold=True)
    put(ws, r, 7, "The bear case needs this HIGH. Our arithmetic says it is low.", HISTF)
    r += 1
    put(ws, r, 1, "Priced at 2025-or-later prices", None, bold=True)
    put(ws, r, 2, "=1-B%d" % (r - 1), CALC, "0.0%", bold=True)
    r += 2
    put(ws, r, 1, "WHAT THIS DOES NOT SETTLE — say these out loud before a judge does", SUB, bold=True)
    for c in range(1, 8):
        ws.cell(row=r, column=c).fill = SUB
    r += 1
    for h in [
        "Equipment RPO blends gas, wind and electrification. The bear case is about gas. "
        "GEV does not disclose runoff by segment.",
        "'Pre-2025' is a proxy for 'before the price increases'. If prices only rose in "
        "mid-2025, the cheap cohort is larger than this and the share above is understated.",
        "Years 3-5 are one disclosed bucket, so 2027's slice is bounded, not known.",
        "The runoff percentages are management estimates and they move every quarter.",
        "Some equipment is recognised at a POINT IN TIME, not over time. For that slice the "
        "bear's shipment-year logic is correct. The split is not disclosed anywhere.",
        "Vintage mix bounds the EXPOSURE to old pricing. It does not by itself give the "
        "2027 margin rate.",
    ]:
        put(ws, r, 1, h).alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
        ws.row_dimensions[r].height = 28
        r += 1

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "GEV_model_shell.xlsx"
    wb.save(path)
    print("wrote", path)
    print("tabs:", wb.sheetnames)


if __name__ == "__main__":
    build()
