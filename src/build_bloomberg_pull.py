"""
Build a Bloomberg data-pull workbook for GE Vernova.

The workbook holds only Bloomberg Excel add-in formulas (BDP / BDH / BDS). Opened on a terminal PC with the
Bloomberg tab in Excel, it fills itself in; saved and brought back, the cached values can be read with
openpyxl (data_only=True). Without the add-in every cell shows #NAME?, which is expected.

    python src/build_bloomberg_pull.py      ->  data/bloomberg/GEV_bloomberg_pull.xlsx

Field names follow Bloomberg's usual mnemonics. A few may differ on a given terminal; cells that error can be
fixed on the terminal with FLDS <GO>. This is a research data pull, not the model the team submits.
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parent.parent / "data" / "bloomberg" / "GEV_bloomberg_pull.xlsx"

GEV = "GEV US Equity"
PEERS = [("Siemens Energy", "ENR GY Equity", "FY ends September"),
         ("Mitsubishi Heavy", "7011 JT Equity", "FY ends March"),
         ("Eaton", "ETN US Equity", ""), ("Vertiv", "VRT US Equity", ""), ("Quanta", "PWR US Equity", ""),
         ("Hubbell", "HUBB US Equity", ""), ("ABB", "ABBN SW Equity", ""), ("Schneider", "SU FP Equity", ""),
         ("Hitachi", "6501 JT Equity", "FY ends March"), ("Baker Hughes", "BKR US Equity", ""),
         ("Bloom Energy", "BE US Equity", "")]
HYPERSCALERS = [("Microsoft", "MSFT US Equity", "FY ends June"), ("Alphabet", "GOOGL US Equity", ""),
                ("Amazon", "AMZN US Equity", ""), ("Meta", "META US Equity", ""), ("Oracle", "ORCL US Equity", "FY ends May")]
PERIODS = ["1FY", "2FY", "3FY", "4FY", "5FY"]
GEV_YEARS = {"1FY": "2026", "2FY": "2027", "3FY": "2028", "4FY": "2029", "5FY": "2030"}

HEAD = Font(bold=True, color="FFFFFF")
FILL = PatternFill("solid", fgColor="1F3A4D")
NOTE = Font(italic=True, color="666666")
BOLD = Font(bold=True)


def header(ws, row, values, col=1):
    for i, v in enumerate(values):
        c = ws.cell(row=row, column=col + i, value=v)
        c.font, c.fill = HEAD, FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")


def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w


def bdp(sec, field, period=None):
    if period:
        return '=BDP("%s","%s","BEST_FPERIOD_OVERRIDE=%s")' % (sec, field, period)
    return '=BDP("%s","%s")' % (sec, field)


def bdh(sec, field, start, period=None, per="W"):
    y, m, d = start
    extra = ',"BEST_FPERIOD_OVERRIDE=%s"' % period if period else ""
    return '=BDH("%s","%s",DATE(%d,%d,%d),TODAY()%s,"Per=%s","Days=A","Fill=P")' % (sec, field, y, m, d, extra, per)


def readme(wb):
    ws = wb.active
    ws.title = "README"
    lines = [
        ("GE Vernova Bloomberg data pull", BOLD),
        ("", None),
        ("How to use", BOLD),
        ("1. Open this file in Excel on a Bloomberg terminal PC. Excel must show a Bloomberg tab and you must be logged in to the terminal.", None),
        ("2. If cells show #NAME?, the add-in is not loaded: in Excel go to File > Options > Add-ins and enable Bloomberg, or ask the lab staff.", None),
        ("3. Wait until no cell says 'Requesting Data'. History sheets take a minute. Use the Bloomberg tab's Refresh Workbook button if needed.", None),
        ("4. Save As a new name with today's date. The values are stored in the file. Email it to yourself or put it on a USB stick.", None),
        ("5. Send the saved file back in the chat. Photos are not needed for anything in this workbook.", None),
        ("", None),
        ("If a cell shows #N/A", BOLD),
        ("#N/A Invalid Field: the field name differs on this terminal. Type FLDS <GO> on the terminal, search the description in column A, and replace the name.", None),
        ("#N/A N/A: Bloomberg has no data for that item, for example no 2030 estimates yet. That is itself an answer; leave it.", None),
        ("Overrides are written as \"BEST_FPERIOD_OVERRIDE=2FY\". If every estimate cell errors, try the two-argument form: \"BEST_FPERIOD_OVERRIDE\",\"2FY\".", None),
        ("", None),
        ("Period codes for GE Vernova (fiscal year ends December)", BOLD),
        ("1FY = 2026, 2FY = 2027, 3FY = 2028, 4FY = 2029, 5FY = 2030. 1BF = blended next twelve months.", None),
        ("For other companies 1FY is their own next unreported fiscal year; see the note beside each ticker.", None),
        ("", None),
        ("Limits", BOLD),
        ("University terminals cap how much data Excel can download. This workbook uses weekly history to stay small. Do not copy the sheets many times.", None),
        ("Bloomberg data is licensed for your own academic use. Keep the filled file within your team and cite figures as Bloomberg with the date.", None),
        ("", None),
        ("Still manual (screens, not Excel): see the Manual sheet. Use GRAB <GO> on any screen to email yourself a picture of it.", None),
    ]
    for i, (text, font) in enumerate(lines, 1):
        c = ws.cell(row=i, column=1, value=text)
        if font:
            c.font = font
        c.alignment = Alignment(wrap_text=True, vertical="top")
    widths(ws, {"A": 130})


def snapshot(wb):
    ws = wb.create_sheet("Snapshot")
    fields = [("Name", "NAME", None), ("Currency", "CRNCY", None), ("Last price", "PX_LAST", None),
              ("Market cap (M)", "CUR_MKT_CAP", None), ("Enterprise value (M)", "CURR_ENTP_VAL", None),
              ("Fwd EV/EBITDA (NTM)", "BEST_EV_TO_BEST_EBITDA", "1BF"), ("Fwd P/E (NTM)", "BEST_PE_RATIO", "1BF"),
              ("Trailing EV/EBITDA", "EV_TO_T12M_EBITDA", None), ("Avg price target", "BEST_TARGET_PRICE", None),
              ("Buy ratings", "TOT_BUY_REC", None), ("Hold ratings", "TOT_HOLD_REC", None), ("Sell ratings", "TOT_SELL_REC", None),
              ("Short interest ratio (days)", "SHORT_INT_RATIO", None), ("Short interest % float", "SI_PERCENT_EQUITY_FLOAT", None),
              ("30d implied vol", "30DAY_IMPVOL_100.0%MNY_DF", None), ("90d realised vol", "VOLATILITY_90D", None),
              ("Next report date", "EXPECTED_REPORT_DT", None), ("Shares out (M)", "EQY_SH_OUT", None)]
    header(ws, 1, ["Company", "Ticker", "Note"] + [f[0] for f in fields])
    header(ws, 2, ["Bloomberg field", "", ""] + [f[1] + (" [" + f[2] + "]" if f[2] else "") for f in fields])
    rows = [("GE Vernova", GEV, "")] + PEERS + HYPERSCALERS
    for r, (name, tic, note) in enumerate(rows, 3):
        ws.cell(row=r, column=1, value=name)
        ws.cell(row=r, column=2, value=tic)
        ws.cell(row=r, column=3, value=note).font = NOTE
        for j, (_, field, per) in enumerate(fields):
            ws.cell(row=r, column=4 + j, value=bdp(tic, field, per))
    widths(ws, {"A": 18, "B": 16, "C": 18})
    for j in range(len(fields)):
        ws.column_dimensions[get_column_letter(4 + j)].width = 15
    ws.freeze_panes = "D3"


def consensus(wb):
    ws = wb.create_sheet("Consensus")
    metrics = [("Revenue", "BEST_SALES"), ("EBITDA", "BEST_EBITDA"), ("EBITDA median", "BEST_EBITDA_MEDIAN"),
               ("EBITDA high", "BEST_EBITDA_HI"), ("EBITDA low", "BEST_EBITDA_LO"), ("EBITDA std dev", "BEST_EBITDA_STDDEV"),
               ("EBITDA number of estimates", "BEST_EBITDA_NUMEST"), ("EBIT", "BEST_EBIT"), ("Net income", "BEST_NET_INCOME"),
               ("EPS", "BEST_EPS"), ("EPS median", "BEST_EPS_MEDIAN"), ("EPS high", "BEST_EPS_HI"), ("EPS low", "BEST_EPS_LO"),
               ("EPS number of estimates", "BEST_EPS_NUMEST"), ("Free cash flow", "BEST_ESTIMATE_FCF"), ("Capex", "BEST_CAPEX"),
               ("Gross margin %", "BEST_GROSS_MARGIN")]
    row = 1
    for name, tic, note in [("GE Vernova", GEV, "1FY = 2026 ... 5FY = 2030")] + PEERS:
        header(ws, row, ["%s  (%s)  %s" % (name, tic, note), "Bloomberg field"] +
               ([p + " = " + GEV_YEARS[p] for p in PERIODS] if tic == GEV else PERIODS))
        for i, (label, field) in enumerate(metrics, 1):
            ws.cell(row=row + i, column=1, value=label)
            ws.cell(row=row + i, column=2, value=field).font = NOTE
            for j, p in enumerate(PERIODS):
                ws.cell(row=row + i, column=3 + j, value=bdp(tic, field, p))
        row += len(metrics) + 2
    widths(ws, {"A": 42, "B": 24, "C": 15, "D": 15, "E": 15, "F": 15, "G": 15})
    ws.freeze_panes = "C2"


def history_sheet(wb, title, series, note):
    """series: list of (label, formula). Each BDH spills two columns (date, value) downward from row 4."""
    ws = wb.create_sheet(title)
    ws.cell(row=1, column=1, value=note).font = NOTE
    col = 1
    for label, formula in series:
        c = ws.cell(row=2, column=col, value=label)
        c.font, c.fill = HEAD, FILL
        ws.cell(row=2, column=col + 1).fill = FILL
        ws.cell(row=3, column=col, value="date").font = NOTE
        ws.cell(row=3, column=col + 1, value="value").font = NOTE
        ws.cell(row=4, column=col, value=formula)
        ws.column_dimensions[get_column_letter(col)].width = 13
        ws.column_dimensions[get_column_letter(col + 1)].width = 13
        ws.column_dimensions[get_column_letter(col + 2)].width = 3
        col += 3
    ws.freeze_panes = "A4"


def histories(wb):
    start25, spin = (2025, 1, 3), (2024, 4, 5)
    cons = []
    for field, label in (("BEST_EBITDA", "EBITDA"), ("BEST_EPS", "EPS"), ("BEST_SALES", "Revenue")):
        for p in (("1FY", "2FY", "3FY", "4FY") if field == "BEST_EBITDA" else ("2FY", "3FY")):
            cons.append(("GEV %s %s (%s)" % (label, p, GEV_YEARS[p]), bdh(GEV, field, start25, p)))
    cons.append(("GEV EBITDA estimates count 2FY", bdh(GEV, "BEST_EBITDA_NUMEST", start25, "2FY")))
    history_sheet(wb, "ConsensusHistory", cons, "Weekly consensus since January 2025. Shows whether the Street is moving its numbers.")

    mult = [("GEV fwd EV/EBITDA (NTM)", bdh(GEV, "BEST_EV_TO_BEST_EBITDA", spin, "1BF")),
            ("GEV fwd P/E (NTM)", bdh(GEV, "BEST_PE_RATIO", spin, "1BF"))]
    for name, tic, _ in PEERS:
        mult.append(("%s fwd EV/EBITDA" % name, bdh(tic, "BEST_EV_TO_BEST_EBITDA", start25, "1BF")))
    history_sheet(wb, "Multiples", mult, "Weekly forward multiples. GEV since the April 2024 spin, peers since January 2025.")

    px = [("GEV price (daily)", bdh(GEV, "PX_LAST", (2024, 4, 2), None, "D")),
          ("GEV average price target (weekly)", bdh(GEV, "BEST_TARGET_PRICE", spin)),
          ("GEV buy ratings (weekly)", bdh(GEV, "TOT_BUY_REC", spin)),
          ("GEV short interest (shares)", bdh(GEV, "SHORT_INT", spin)),
          ("GEV 30d implied vol (weekly)", bdh(GEV, "30DAY_IMPVOL_100.0%MNY_DF", spin)),
          ("GEV put/call open interest (weekly)", bdh(GEV, "PUT_CALL_OPEN_INTEREST_RATIO", spin))]
    history_sheet(wb, "PricePositioning", px, "Price, targets, ratings, short interest and options since the spin.")

    macro = [("US 10-year yield", bdh("USGG10YR Index", "PX_LAST", start25)),
             ("Natural gas front month", bdh("NG1 Comdty", "PX_LAST", start25)),
             ("S&P 500", bdh("SPX Index", "PX_LAST", start25)),
             ("S&P 500 Industrials", bdh("S5INDU Index", "PX_LAST", start25))]
    for name, tic, _ in HYPERSCALERS:
        macro.append(("%s capex consensus 2FY" % name, bdh(tic, "BEST_CAPEX", start25, "2FY")))
    history_sheet(wb, "MacroDemand", macro, "Rates, gas, market and the data-centre builders' capex consensus (a demand read-through).")


def hyperscalers(wb):
    ws = wb.create_sheet("HyperscalerCapex")
    header(ws, 1, ["Company", "Ticker", "Note", "Capex 1FY", "Capex 2FY", "Capex 3FY", "Revenue 2FY"])
    for r, (name, tic, note) in enumerate(HYPERSCALERS, 2):
        ws.cell(row=r, column=1, value=name)
        ws.cell(row=r, column=2, value=tic)
        ws.cell(row=r, column=3, value=note).font = NOTE
        for j, p in enumerate(("1FY", "2FY", "3FY")):
            ws.cell(row=r, column=4 + j, value=bdp(tic, "BEST_CAPEX", p))
        ws.cell(row=r, column=7, value=bdp(tic, "BEST_SALES", "2FY"))
    widths(ws, {"A": 14, "B": 16, "C": 16, "D": 14, "E": 14, "F": 14, "G": 14})


def bulk(wb):
    ws = wb.create_sheet("Bulk")
    ws.cell(row=1, column=1, value="Each table spills down and to the right from its formula cell. If one shows #N/A, find the field with FLDS <GO>.").font = NOTE
    tables = [("Analyst ratings, targets and dates, by broker", "BEST_ANALYST_RECS_BULK"),
              ("Top 20 holders from public filings", "TOP_20_HOLDERS_PUBLIC_FILINGS"),
              ("Past report dates with EPS estimate and actual", "EARN_ANN_DT_TIME_HIST_WITH_EPS"),
              ("Largest customers (supply chain)", "SUPPLY_CHAIN_CUSTOMERS"),
              ("Largest suppliers (supply chain)", "SUPPLY_CHAIN_SUPPLIERS")]
    col = 1
    for label, field in tables:
        c = ws.cell(row=2, column=col, value="%s  [%s]" % (label, field))
        c.font, c.fill = HEAD, FILL
        ws.cell(row=3, column=col, value='=BDS("%s","%s")' % (GEV, field))
        for k in range(10):
            ws.column_dimensions[get_column_letter(col + k)].width = 16
        col += 11


def manual(wb):
    ws = wb.create_sheet("Manual")
    header(ws, 1, ["Screen", "Type this", "What to capture (use GRAB <GO> to email the screen to yourself)"])
    rows = [
        ("Broker estimates with dates", "GEV US Equity EEB <GO>", "EBITDA for 2027, 2028, 2029: every broker, value and estimate date. Use Actions > Export to Excel if offered. This tests whether the consensus is stale."),
        ("Estimates by segment", "GEV US Equity EE <GO>, Segments or KPI tab", "Power, Electrification and Wind revenue and margin for 2027-2029; gas turbine GW if shown."),
        ("Multiple chart and statistics", "GEV US Equity EQRV <GO>", "Forward EV/EBITDA: current, high, low, average and percentile."),
        ("Relative value", "GEV US Equity RV <GO>", "Custom peer set from the Snapshot sheet; export the table."),
        ("Bloomberg Intelligence", "BI <GO>", "GE Vernova page and the power or electrical equipment dashboard: forecasts to 2029-2030, any gas turbine order or price tracker."),
        ("Company models", "GEV US Equity MODL <GO>", "Any model with segment lines to 2029-2030; export if allowed."),
        ("BloombergNEF", "BNEF <GO>", "Gas plant project database (maker, MW, cost, in-service year); gas turbine orders and prices by maker."),
        ("Broker research", "GEV US Equity BRC <GO>", "Reports with 2029-2030 forecasts or 'margin in backlog'; title, broker, date, key numbers."),
        ("Valuation model", "GEV US Equity DDM <GO>", "The growth and margin at which model value equals today's price."),
        ("Events", "GEV US Equity EVTS <GO>", "Q3 date, any December event, January results date, spring investor day."),
        ("News screen", "GEV US Equity CN <GO>", "Last 60 days: cancel, defer, force majeure, slot, reservation."),
        ("Holders", "GEV US Equity HDS <GO>", "Top holders and the largest changes last quarter."),
        ("Options", "GEV US Equity OVDV <GO>", "Implied volatility for the expiry after the late-January report; put-call skew."),
        ("Peers by segment", "ENR GY Equity EE <GO>, then 7011 JT Equity EE <GO>", "Gas Services and Energy Systems margin consensus 2026-2028."),
    ]
    for r, row in enumerate(rows, 2):
        for c, v in enumerate(row, 1):
            ws.cell(row=r, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
    widths(ws, {"A": 30, "B": 44, "C": 110})


def main():
    wb = Workbook()
    readme(wb)
    snapshot(wb)
    consensus(wb)
    histories(wb)
    hyperscalers(wb)
    bulk(wb)
    manual(wb)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    n = sum(1 for ws in wb for row in ws.iter_rows() for c in row if isinstance(c.value, str) and c.value.startswith("="))
    print("wrote %s: %d sheets, %d Bloomberg formulas" % (OUT, len(wb.sheetnames), n))


if __name__ == "__main__":
    main()
