"""
Stress tests on the GEV short thesis that need no forecast: arithmetic on published numbers only.

Every input below is a published figure with its source tag (see docs/research/multi_agent/
09_finrobot_overnight/E03_model_inputs.md for page locators). Nothing here is a forecast by the team;
the "research base" rows are the overnight run's D01A build and are shown only for comparison.

    python src/robustness_tests.py            # prints the tables as markdown
"""

# ---------------------------------------------------------------- inputs ($M unless stated)
# Company actuals: revenue, adjusted EBITDA   [10-K25 p.26; releases; MarketScreener history ties]
ACT = {
    "FY23": (33239, 807), "FY24": (34935, 2035), "FY25": (38068, 3196),
    "H1'25": (17143, 1227), "H1'26": (20442, 2146),
    "Q3'24": (8913, 243), "Q4'24": (10559, 1077),      # Q3'24 2.7% and Q4'24 10.2% margins (releases)
    "Q3'25": (9969, 811), "Q4'25": (10956, 1158),
}
# FY26 guidance issued 2026-07-22   [Q2'26 release p.2; Reuters 2026-07-22]
GUIDE26_REV = (45500, 46500)
GUIDE26_MARGIN = (0.12, 0.14)
SEG_GUIDE26_EBITDA_MID = 6185          # segment-guide midpoints summed (D01A section 4) [computed]
Q3_GUIDE_IMPLIED = (1535, 1716)        # rebuilt from the Q3 segment guides (D07, R07) [computed]
# 2028 framework issued 2026-01-28   [Q4'25 release p.3]
FRAME28_REV, FRAME28_MARGIN = 56000, 0.20
SEG_TARGET28 = {"Power": 0.22, "Electrification": 0.22, "Wind": 0.06}
SEG_GUIDE26_MID = {"Power": 0.18, "Electrification": 0.19}      # Wind guided at about -$400M
# Consensus   [MarketScreener 2026-09-29]  and  [FactSet via Boursorama, 2026-09-30]
MS = {"FY26": (46282, 6359), "FY27": (52740, 9574), "FY28": (60500, 13064),
      "Q3'26": (12013, 1706), "Q4'26": (13905, 2535)}
FS = {"FY26": (46306, 6394), "FY27": (52888, 9339)}
# Research base, for comparison only   [D01_fy27_build_A.md section 4]
RES = {"FY26": (46049, 6185), "FY27": (52223, 8744)}
RES_SEG27_REV = {"Power": 27503, "Electrification": 17470, "Wind": 7700}
RES_CORP27 = -475
RES_WIND28_REV = 7000
# Valuation bridge   [10-Q2'26 cover and balance sheet; price 2026-09-29 close]
PRICE, SHARES_M, BRIDGE = 962.49, 266.333581, 9113
# Multiples   [D05_multiple.md: computed from MarketScreener; own history from one vendor]
GEV_NTM = 28.2
PEERS = {"Quanta": 22.0, "Eaton": 21.3, "Vertiv": 20.6, "ABB": 19.0, "Schneider": 16.4,
         "Hubbell": 15.1, "MHI": 14.7, "Siemens Energy": 12.6}
OWN_TROUGHS = [("2025-11-04", 23.4), ("2025-12-17", 24.9), ("2026-07-29", 27.5), ("2026-09-14", 25.4)]


def pct(a, b):
    return 100.0 * (a / b - 1.0)


def m(rev_ebitda):
    return 100.0 * rev_ebitda[1] / rev_ebitda[0]


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def guide_mid():
    rev = sum(GUIDE26_REV) / 2
    return rev, rev * sum(GUIDE26_MARGIN) / 2


def t1_ladder():
    """Street vs management's own number at each horizon."""
    rev26, e26 = guide_mid()
    frame28 = FRAME28_REV * FRAME28_MARGIN
    line27 = (e26 + frame28) / 2
    q3_mid = sum(Q3_GUIDE_IMPLIED) / 2
    h2_guide = e26 - ACT["H1'26"][1]
    h2_cons = MS["Q3'26"][1] + MS["Q4'26"][1]
    rows = [
        ["Q3'26", "%d-%d (rebuilt from segment guides)" % Q3_GUIDE_IMPLIED, MS["Q3'26"][1], "n/a",
         "%+.1f%% vs midpoint" % pct(MS["Q3'26"][1], q3_mid)],
        ["H2'26", "%.0f (guide midpoint less H1 actual)" % h2_guide, h2_cons, "n/a", "%+.1f%%" % pct(h2_cons, h2_guide)],
        ["FY26", "%.0f (guide midpoint: $46.0B x 13%%)" % e26, MS["FY26"][1], FS["FY26"][1],
         "%+.1f%% / %+.1f%%" % (pct(MS["FY26"][1], e26), pct(FS["FY26"][1], e26))],
        ["FY27", "%.0f (straight line FY26 guide to 2028; not guidance)" % line27, MS["FY27"][1], FS["FY27"][1],
         "%+.1f%% / %+.1f%%" % (pct(MS["FY27"][1], line27), pct(FS["FY27"][1], line27))],
        ["FY28", "%.0f (framework: $56B x 20%%)" % frame28, MS["FY28"][1], "n/f", "%+.1f%%" % pct(MS["FY28"][1], frame28)],
    ]
    return table(["Horizon", "Management's number", "MarketScreener", "FactSet", "Street above management"], rows)


def t2_distance_to_targets():
    """Where the Street's FY27 sits between a straight-line margin path and 2028 targets a year early."""
    wind26_margin = -400.0 / 8100.0
    lin = {"Power": (SEG_GUIDE26_MID["Power"] + SEG_TARGET28["Power"]) / 2,
           "Electrification": (SEG_GUIDE26_MID["Electrification"] + SEG_TARGET28["Electrification"]) / 2}
    wind_lin = (-400.0 + SEG_TARGET28["Wind"] * RES_WIND28_REV) / 2          # $M, midpoint of FY26 and 2028
    linear = sum(RES_SEG27_REV[s] * lin[s] for s in lin) + wind_lin + RES_CORP27
    early = sum(RES_SEG27_REV[s] * SEG_TARGET28[s] for s in SEG_TARGET28) + RES_CORP27
    rows = [["Straight-line margins (Power %.1f%%, Electrification %.2f%%, Wind %+.0f)" % (100 * lin["Power"], 100 * lin["Electrification"], wind_lin),
             "%.0f" % linear, "0%"],
            ["Research base (D01A)", RES["FY27"][1], "%.0f%%" % (100 * (RES["FY27"][1] - linear) / (early - linear))],
            ["FactSet consensus", FS["FY27"][1], "%.0f%%" % (100 * (FS["FY27"][1] - linear) / (early - linear))],
            ["MarketScreener consensus", MS["FY27"][1], "%.0f%%" % (100 * (MS["FY27"][1] - linear) / (early - linear))],
            ["Every segment at its 2028 target margin in 2027 (22% / 22% / 6%)", "%.0f" % early, "100%"]]
    return table(["FY27 case (research segment revenues, corporate -475)", "Adj. EBITDA", "Share of the way to targets-a-year-early"], rows), wind26_margin


def t3_steps():
    """Company margin step by year, in points."""
    rev26, e26 = guide_mid()
    rows = [["FY23 to FY24", "%.2f to %.2f" % (m(ACT["FY23"]), m(ACT["FY24"])), "%+.2f" % (m(ACT["FY24"]) - m(ACT["FY23"])), "delivered"],
            ["FY24 to FY25", "%.2f to %.2f" % (m(ACT["FY24"]), m(ACT["FY25"])), "%+.2f" % (m(ACT["FY25"]) - m(ACT["FY24"])), "delivered"],
            ["H1'25 to H1'26", "%.2f to %.2f" % (m(ACT["H1'25"]), m(ACT["H1'26"])), "%+.2f" % (m(ACT["H1'26"]) - m(ACT["H1'25"])), "delivered"],
            ["FY25 to FY26, guide midpoint", "%.2f to %.2f" % (m(ACT["FY25"]), 100 * e26 / rev26), "%+.2f" % (100 * e26 / rev26 - m(ACT["FY25"])), "guided"],
            ["FY25 to FY26, consensus", "%.2f to %.2f" % (m(ACT["FY25"]), m(MS["FY26"])), "%+.2f" % (m(MS["FY26"]) - m(ACT["FY25"])), "Street"],
            ["FY26 to FY27, MarketScreener", "%.2f to %.2f" % (m(MS["FY26"]), m(MS["FY27"])), "%+.2f" % (m(MS["FY27"]) - m(MS["FY26"])), "Street"],
            ["FY26 to FY27, FactSet", "%.2f to %.2f" % (m(FS["FY26"]), m(FS["FY27"])), "%+.2f" % (m(FS["FY27"]) - m(FS["FY26"])), "Street"],
            ["FY26 to FY27, research base", "%.2f to %.2f" % (m(RES["FY26"]), m(RES["FY27"])), "%+.2f" % (m(RES["FY27"]) - m(RES["FY26"])), "research"]]
    return table(["Period", "Adj. EBITDA margin (%)", "Step (points)", "Status"], rows)


def t4_incrementals():
    """Incremental margin: change in EBITDA divided by change in revenue."""
    rev26, e26 = guide_mid()
    frame28 = (FRAME28_REV, FRAME28_REV * FRAME28_MARGIN)

    def inc(a, b):
        return "%.1f%%" % (100.0 * (b[1] - a[1]) / (b[0] - a[0]))
    rows = [["FY24 to FY25", inc(ACT["FY24"], ACT["FY25"]), "delivered"],
            ["H1'25 to H1'26", inc(ACT["H1'25"], ACT["H1'26"]), "delivered (Wind loss widened by 345)"],
            ["FY25 to FY26, guide midpoint", inc(ACT["FY25"], (rev26, e26)), "guided (includes Prolec)"],
            ["FY25 to FY26, consensus", inc(ACT["FY25"], MS["FY26"]), "Street"],
            ["FY26 to FY27, MarketScreener", inc(MS["FY26"], MS["FY27"]), "Street"],
            ["FY26 to FY27, FactSet", inc(FS["FY26"], FS["FY27"]), "Street"],
            ["FY26 to FY27, research base", inc(RES["FY26"], RES["FY27"]), "research"],
            ["FY26 guide midpoint to the 2028 framework", inc((rev26, e26), frame28), "management's own plan, two years"]]
    return table(["Period", "Incremental margin", "Status"], rows)


def t5_exit_rate():
    """Next year's margin against this year's second half."""
    rev26, e26 = guide_mid()
    h2_24 = (ACT["Q3'24"][0] + ACT["Q4'24"][0], ACT["Q3'24"][1] + ACT["Q4'24"][1])
    h2_25 = (ACT["Q3'25"][0] + ACT["Q4'25"][0], ACT["Q3'25"][1] + ACT["Q4'25"][1])
    h2_26g = (rev26 - ACT["H1'26"][0], e26 - ACT["H1'26"][1])
    h2_26c = (MS["Q3'26"][0] + MS["Q4'26"][0], MS["Q3'26"][1] + MS["Q4'26"][1])
    rows = [["FY25 actual vs H2'24 actual", "%.2f" % m(h2_24), "%.2f" % m(ACT["FY25"]), "%+.2f" % (m(ACT["FY25"]) - m(h2_24))],
            ["FY26 guide midpoint vs H2'25 actual", "%.2f" % m(h2_25), "%.2f" % (100 * e26 / rev26), "%+.2f" % (100 * e26 / rev26 - m(h2_25))],
            ["FY26 consensus vs H2'25 actual", "%.2f" % m(h2_25), "%.2f" % m(MS["FY26"]), "%+.2f" % (m(MS["FY26"]) - m(h2_25))]]
    for name, h2 in (("H2'26 at the guide midpoint", h2_26g), ("H2'26 at consensus", h2_26c)):
        for lab, fy in (("MarketScreener FY27", MS["FY27"]), ("FactSet FY27", FS["FY27"]), ("Research base FY27", RES["FY27"])):
            rows.append(["%s vs %s" % (lab, name), "%.2f" % m(h2), "%.2f" % m(fy), "%+.2f" % (m(fy) - m(h2))])
    return table(["Comparison", "Prior second-half margin (%)", "Full-year margin (%)", "Difference (points)"], rows)


def t6_base_vs_bridge():
    """How much of the FY27 gap is the FY26 starting point and how much is the FY26-to-FY27 bridge."""
    res_bridge = RES["FY27"][1] - RES["FY26"][1]
    rows = []
    for lab, c in (("MarketScreener", MS), ("FactSet", FS)):
        gap = c["FY27"][1] - RES["FY27"][1]
        base = c["FY26"][1] - RES["FY26"][1]
        bridge = (c["FY27"][1] - c["FY26"][1]) - res_bridge
        rebased = c["FY26"][1] + res_bridge
        rows.append([lab, c["FY27"][1], gap, "%.1f%%" % (100.0 * gap / c["FY27"][1]), base, bridge,
                     rebased, "%.1f%%" % (100.0 * (c["FY27"][1] - rebased) / c["FY27"][1])])
    return table(["Vendor", "Street FY27", "Gap to research base (8,744)", "Gap %", "of which FY26 base", "of which bridge",
                  "Research bridge (+%d) on the Street's FY26" % res_bridge, "Gap % then"], rows)


def t7_wind():
    """Sensitivity of the research base to one line: FY27 Wind."""
    rows = []
    for margin in (0.0, 0.03, 0.06):
        wind = RES_SEG27_REV["Wind"] * margin
        total = RES["FY27"][1] + wind
        rows.append(["%.0f%%" % (100 * margin), "%.0f" % wind, "%.0f" % total,
                     "%.1f%%" % (100 * (1 - total / FS["FY27"][1])), "%.1f%%" % (100 * (1 - total / MS["FY27"][1]))])
    return table(["FY27 Wind margin on 7,700 revenue", "Wind EBITDA", "FY27 total", "Below FactSet", "Below MarketScreener"], rows)


def price_at(multiple, ntm_ebitda_m):
    return (multiple * ntm_ebitda_m + BRIDGE) / SHARES_M


def t8_multiple():
    """January price for combinations of FY27 EBITDA and the multiple (NTM = 11/12 FY27 + 1/12 FY28)."""
    mults = (23.0, 25.0, 26.0, 28.2)
    rows = []
    for fy27, fy28 in ((8600, 11200), (8900, 11500), (9339, 12500), (9574, 13064)):
        ntm = fy27 * 11 / 12 + fy28 / 12
        cells = ["%.0f / %.0f" % (fy27, fy28), "%.0f" % ntm]
        for k in mults:
            p = price_at(k, ntm)
            cells.append("$%.0f (%+.1f%%)" % (p, pct(p, PRICE)))
        rows.append(cells)
    head = ["FY27 / FY28 EBITDA", "NTM EBITDA in January"] + ["%.1fx" % k for k in mults]
    ntm_now = (PRICE * SHARES_M - BRIDGE) / GEV_NTM
    med = sorted(PEERS.values())
    median = (med[3] + med[4]) / 2
    peer_rows = [[n, "%.1fx" % v, "%.2fx" % (GEV_NTM / v)] for n, v in sorted(PEERS.items(), key=lambda kv: -kv[1])]
    peer_rows.append(["Median of the eight", "%.1fx" % median, "%.2fx" % (GEV_NTM / median)])
    return table(head, rows), table(["Peer", "NTM EV/EBITDA", "GEV multiple divided by peer"], peer_rows), ntm_now


def t9_twelve_months():
    """September-2027 price for combinations of the earnings path and the multiple (NTM = 1/4 FY27 + 3/4 FY28)."""
    rev26, e26 = guide_mid()
    frame28 = FRAME28_REV * FRAME28_MARGIN
    paths = [("Management path (straight line FY27, framework FY28)", (e26 + frame28) / 2, frame28),
             ("Research base (D01A)", RES["FY27"][1], 11190),
             ("MarketScreener consensus", MS["FY27"][1], MS["FY28"][1])]
    mults = (21.0, 23.0, 25.0, 28.2)
    rows = []
    for lab, fy27, fy28 in paths:
        ntm = 0.25 * fy27 + 0.75 * fy28
        breakeven = (PRICE * SHARES_M - BRIDGE) / ntm
        cells = [lab, "%.0f" % ntm]
        for k in mults:
            p = price_at(k, ntm)
            cells.append("$%.0f (%+.1f%%)" % (p, pct(p, PRICE)))
        cells.append("%.1fx" % breakeven)
        rows.append(cells)
    head = ["Earnings path", "NTM EBITDA in Sep-2027"] + ["%.1fx" % k for k in mults] + ["Multiple that holds $%.2f" % PRICE]
    ev = PRICE * SHARES_M - BRIDGE
    implied = [["%.0fx" % k, "%.0f" % (ev / k)] for k in (21, 23, 25)]
    return table(head, rows), table(["If the multiple in Sep-2027 is", "NTM EBITDA that today's price needs"], implied)


def main():
    print("## T1. Street against management's own number at each horizon\n")
    print(t1_ladder())
    print("\nFY26 against the sum of the segment-guide midpoints (%d): MarketScreener %+.1f%%, FactSet %+.1f%%. "
          "Consensus FY26 is inside the guided dollar range (%.0f-%.0f)."
          % (SEG_GUIDE26_EBITDA_MID, pct(MS["FY26"][1], SEG_GUIDE26_EBITDA_MID), pct(FS["FY26"][1], SEG_GUIDE26_EBITDA_MID),
             GUIDE26_REV[0] * GUIDE26_MARGIN[0], GUIDE26_REV[1] * GUIDE26_MARGIN[1]))
    t2, _ = t2_distance_to_targets()
    print("\n## T2. How far toward the 2028 targets the Street's FY27 already is\n")
    print(t2)
    print("\n## T3. Margin step by year\n")
    print(t3_steps())
    print("\n## T4. Incremental margin\n")
    print(t4_incrementals())
    print("\n## T5. Next year's margin against this year's second half\n")
    print(t5_exit_rate())
    print("\n## T6. Base effect against bridge effect\n")
    print(t6_base_vs_bridge())
    print("\n## T7. One-line sensitivity: FY27 Wind\n")
    print(t7_wind())
    grid, peers, ntm_now = t8_multiple()
    print("\n## T8. The multiple\n")
    print("NTM EBITDA implied by $%.2f at %.1fx: $%.0fM.\n" % (PRICE, GEV_NTM, ntm_now))
    print(grid)
    print()
    print(peers)
    print("\nGEV's own troughs (one vendor): " + ", ".join("%.1fx on %s" % (v, d) for d, v in OWN_TROUGHS) + ".")
    grid12, implied = t9_twelve_months()
    print("\n## T9. Twelve months out: earnings growth against multiple compression\n")
    print(grid12)
    print()
    print(implied)


if __name__ == "__main__":
    main()
