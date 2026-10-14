"""Sections 12 to 17 of the thesis file, and the reference list."""

S = []

S.append(("12. Questions a judge is likely to ask, with the facts", [
    ("note", "**Use.** These are the facts for each answer. The words of the answer are the team's."),
    ("md", "Eight questions, each with the facts that answer it."),
    ("wide", """
| Question | Facts to answer with |
|---|---|
| Why 25x, when the direct rivals trade at 12.7x and 15.1x? | Every week of the last 12 months was above 27x. Howmet and GE Aerospace trade at 25.7x and 25.0x with a third of the growth. The case still returns -3.7% at 21x on base EBITDA and breaks even at 21.8x. It is an assumption, and the file says so. |
| Last quarter was 3.3 GW. Why will it be 5? | The company shipped 5.2 GW in Q2 2025. 325 machines are installed and about 400 will be by year end. The blade maker's turbine sales grew 38%. The first reading is 28 October. |
| Power equipment is a quarter of revenue. Why build the thesis on it? | It is where the growth is: analysts have it rising from $9,342M to $15,888M between 2026 and 2028. Each turbine shipped adds decades of service revenue. Power is about 62% of analysts' 2028 EBITDA. |
| If you agree with analysts' earnings, what do you know that the market does not? | Nothing about earnings, and the file does not claim to. The view is about the hurdle: the multiple can fall 26% before the position loses, and in the stock's history it has not fallen that much over any 8 to 12 month window. |
| Why 12 months and not 3 or 6? | The break-even multiple is 27.2x at 3 months, 25.1x at 6 and 21.8x at 12. The return builds evenly, at a little over 1% a month. Safety is what grows with time. |
| Why not short? | The short's best window is 3 months, and it needs the multiple below 27.2x. Company guidance has been raised or held at every report. Nine bear arguments failed their checks. |
| Is the Sell note right? | For the largest turbines its premise is contradicted: 62 to 70 of the 70 HA units in backlog were ordered in 2025 or later. |
| How much of the $741 per kW will actually be realised? | Over five yearly windows, revenue per kW shipped ran at 78% to 94% of the backlog average, 87% on average. On $741 that is $578 to $697. Analysts need $579 in 2027 and $662 in 2028. |
| What happens to cash flow when the deposits stop growing? | Analysts have free cash flow falling from $12.2B to $7.7B in 2027 while EBITDA rises; that already assumes deposit growth slows from $15.7B to about $5.5B. The company's own floor of at least $24B for 2025 to 2028 sits below analysts for 2027 and 2028. The valuation rests on EBITDA, not cash. |
| What makes you sell? | Section 11. |
"""),
]))

S.append(("13. What the research does not support", [
    ("note", "**Why list these.** A judge who finds one claim that does not hold will doubt the rest. These are the claims to leave out."),
    ("md", """
- That analysts are too low, or too high, by any stated percent.
- That the H1 2027 Power equipment figure will beat by 14 to 17%. The sign held in every variant; the size did not.
- That the 21 GW (2027) and 26 GW (2029) output figures are company numbers. They are readings of the plan.
- That world capacity will rise from 67 to 102 GW a year. One source.
- The details of the Sell note. It is known only from press summaries.
- That past price behaviour predicts the next year. The history is two and a half years long and covers one long rise.
- Howmet's call remarks on capacity and market share, which come from a transcript site. Its dollar figures ($321M in Q2 2026, $605M in H1 2026, $944M in FY2025) are from its own filings and can be cited.
"""),
]))

S.append(("14. Starting the model", [
    ("note", "**The model is the team's.** This section lists the inputs, where each comes from, and the totals your own workbook should reach. It does not lay out cells or formulas."),
    ("md", """
**What the rules ask of the model:** clearly formatted, easy to follow, with the assumptions shown and justified, and consistent with the thesis. Judging looks at how well the model and the thesis fit together. [R37]

### What a valuation model of this kind usually shows

1. An inputs page. Every typed number appears once, with its unit, date and source.
2. Reported history by segment (section 3).
3. The forecast by year: analysts' figures, the company plan path, and any view of your own (sections 7 and 8).
4. The gigawatt exhibit: output and price per kW against analysts' Power equipment revenue (section 5).
5. The valuation: forward profit, multiple, net cash, diluted shares, price (section 8).
6. The three cases side by side, and the weighted value.
7. A sensitivity grid: price at each multiple and each profit case.
8. A row of checks that should all read zero or "OK".

### Totals your own workbook should reach

| Check | Value |
|---|---|
| Diluted shares | 269.334M |
| Net cash | 8,713 |
| Forward EBITDA at 30 September 2027: bear / base / bull | 10,547.5 / 11,782.5 / 12,371.6 |
| Price: bear / base / bull | $855 / $1,126 / $1,341 |
| Weighted price | $1,112 |
| Break-even multiple | 21.8x |
| Multiple today on the same basis | 29.6x |
| Price if the multiple held at 29.6x | $1,328 |

### Traps that moved the answer during research

- Basic shares instead of diluted shares.
- Leaving restricted cash and noncontrolling interests in net cash.
- Mixing Bloomberg's 28.5x with a forward profit built another way. Section 8 explains the two bases.
- Prices from different dates. Keep 1 October 2026 throughout.
- Two segment EBITDA series on Bloomberg. The tables here use the adjusted series, which matches the company's own measure.
- H1 2025 figures: use the ones restated to the 2026 segments.
"""),
    ("md", """
### Where the facts for each part of the memo are

| Memo part | Sections of this file |
|---|---|
| Recommendation, price, target, return | 1, 8 |
| Thesis points | 5 and 6 (gigawatts and the factory); 1 and 8 (profit growth against the multiple) |
| Market view | 7 |
| Company and industry | 3, 4 |
| Valuation and scenarios | 8 |
| Catalysts | 10 |
| Risks and mitigants | 11 |
| Sources | 16 |
"""),
]))

S.append(("15. The Bloomberg work: what was pulled and how to cite it", [
    ("note", "**How the pulls worked.** A workbook of Bloomberg formulas was prepared in advance. Opened on a terminal, it filled itself with live data. Screens that formulas cannot reach were exported by hand."),
    ("md", "Two full pulls were made on a Bloomberg terminal, on 1 and 2 October 2026. A third, short workbook is waiting to be filled. The table lists what each one holds."),
    ("wide", """
| Pull | What it holds | Bloomberg fields or screens | Main result | File |
|---|---|---|---|---|
| 1 October, workbook | Price and value, analysts' forecasts for four years, their weekly history, the multiple and its history, ratings, short interest | PX_LAST, CUR_MKT_CAP, CURR_ENTP_VAL, BEST_EV_TO_BEST_EBITDA, BEST_SALES, BEST_EBITDA with median, high, low and count, BEST_ESTIMATE_FCF, BEST_TARGET_PRICE, TOT_BUY_REC, SI_PERCENT_EQUITY_FLOAT | Analysts' EBITDA 6,334 / 9,471 / 12,553 / 16,496; multiple 28.5x; no gap against research either way | GEV_bloomberg_pull_filled_2026-10-01.xlsx |
| 1 October, 20 screen exports | Forecasts to 2030, forecasts by segment, each broker's model for Q3 2026, valuation against history and peers, holders, customers | EEO, EEO Company Specific, MODL, EEG, EQRV, RV, HDS, SPLC, DDM | Segment forecasts by quarter and year; premium to the benchmark at its two-year average | GEV_Pull_2026-10-01 folder |
| 2 October, workbook | 14 suppliers and rivals, 28 customers, options, estimate changes | CHG_PCT_3M, SALES_REV_TURN, BEST_CAPEX, implied-volatility fields, the 4-week and 3-month change fields, SUPPLY_CHAIN_SUPPLIERS | Sections 7 to 9: group-wide fall, fair options, Howmet's growth, slower customer spending in 2028 | GEV_bloomberg_pull_2_filled_2026-10-02.xlsx |
| 2 October, third workbook | Howmet's quarterly outlook; supply-chain links in dollars | BEST_SALES by quarter; RELATIONSHIP_AMOUNT (untested) | Not yet returned | GEV_bloomberg_pull_3.xlsx |

All files are in `gev-corpus/data/bloomberg/`.
"""),
    ("md", """
- **How to cite:** "Bloomberg, 2026-10-01" or "Bloomberg, 2026-10-02", with the measure named, for example "Bloomberg consensus adjusted EBITDA, 36 estimates".
- **Licence:** the data is for academic use. Keep the files inside the team. Do not post them.
- **One caution on the multiple:** Bloomberg's 28.5x uses its own blend of forecast years. A simple model cannot reproduce it, which is why this file also gives 29.6x on the model's basis.
- **One caution on segments:** segment forecasts come from fewer brokers than company totals. The export hides most broker names, so the count behind each segment line is not known.
"""),
]))

REFS = [
    ("R1", "GE Vernova, Form 10-K for FY2025, filed 29 January 2026 (accession 0001996810-26-000015)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm"),
    ("R2", "GE Vernova, Form 10-K for FY2024, filed 6 February 2025 (0001996810-25-000011)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681025000011/gev-20241231.htm"),
    ("R3", "GE Vernova, Form 10-Q for Q2 2026, filed 22 July 2026 (0001996810-26-000148)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm"),
    ("R4", "GE Vernova, Form 10-Q for Q1 2026, filed 22 April 2026 (0001996810-26-000064)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000064/gev-20260331.htm"),
    ("R5", "GE Vernova, Form 10-Q for Q3 2025, filed 22 October 2025 (0001996810-25-000160)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681025000160/gev-20250930.htm"),
    ("R6", "GE Vernova, Q2 2026 earnings release, 22 July 2026 (8-K 0001996810-26-000147)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gev-20260722.htm"),
    ("R7", "GE Vernova, Q4 2025 earnings release, 28 January 2026 (8-K 0001996810-26-000012)", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000012/gev-20260128.htm"),
    ("R8", "GE Vernova, Q1 2026 earnings release, 22 April 2026 (8-K 0001996810-26-000063); Q3 2025 release (8-K 0001996810-25-000159); 2025 Investor Update press release, 9 December 2025", "https://www.sec.gov/Archives/edgar/data/1996810/000199681026000063/gev-20260422.htm"),
    ("R9", "GE Vernova, Q2 2026 earnings call transcript, 22 July 2026", "https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf"),
    ("R10", "GE Vernova at the Morgan Stanley Laguna conference, transcript, 16 September 2026 (gevernova.com investor pages; read 1 October 2026)", None),
    ("R11", "Earlier filings used for the back-tests: Forms 10-Q for Q1 to Q3 2024 and Q1 to Q2 2025; Form S-1/A of 2024", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1996810&type=10-Q"),
    ("R12", "Bloomberg, 2026-10-01: consensus (BEst), segment consensus (EEO Company Specific), broker models (MODL), multiples and their weekly history, ratings, peers (RV, EQRV). Academic licence; no public link", None),
    ("R13", "Bloomberg, 2026-10-02: suppliers and rivals, customers' capital spending, implied volatility, estimate changes, supply-chain lists. Academic licence; no public link", None),
    ("R14", "Daily closing prices in the research database, 27 March 2024 to 18 September 2026", None),
    ("R15", "Mitsubishi Heavy Industries, FY2025 fourth-quarter results, questions and answers", "https://www.mhi.com/finance/library/result/pdf/fy20254q/qa_20254q.pdf"),
    ("R16", "Wood Mackenzie, press release: gas turbine prices soar 195% as market faces supply-demand crisis", "https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/"),
    ("R17", "Utility Dive: GE Vernova gas turbine backlog climbs to 116 GW", "https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/"),
    ("R18", "Trade article: Gas Turbine Orders 2025-26: Backlog, Price and Lead-Time Data (secondwatt.com)", "https://secondwatt.com/resources/gas-turbine-orders-2025-backlog-lead-times-buyer-guide"),
    ("R19", "News: The Gas Turbine Shortage Just Became AI's Biggest Constraint (Yahoo Finance)", "https://finance.yahoo.com/energy/articles/gas-turbine-shortage-just-became-210000180.html"),
    ("R20", "News on the SpaceX blade foundry, 30 August and 2 September 2026 (Yahoo Finance)", "https://finance.yahoo.com/technology/ai/articles/elon-musk-trying-break-ge-141624492.html"),
    ("R21", "News on GE Aerospace buying Consolidated Precision Products, September 2026 (Yahoo Finance)", "https://finance.yahoo.com/economy/policy/articles/good-ge-aerospace-may-not-154622399.html"),
    ("R22", "Press summary of the GLJ Research Sell initiation, September 2026 (Yahoo Finance)", "https://finance.yahoo.com/markets/stocks/articles/glj-starts-ge-vernova-sell-122234358.html"),
    ("R23", "Press summary of the Jefferies note of 12 September 2026 (Blockonomi)", "https://blockonomi.com/ge-vernova-gev-stock-jefferies-says-recent-23-decline-creates-entry-point/"),
    ("R24", "Enverus Intelligence Research post citing BloombergNEF capacity data (LinkedIn). One source", "https://www.linkedin.com/posts/enverus-intelligence-research_gas-turbine-manufacturing-capacity-not-demand-activity-7500600955910959104-osJ0"),
    ("R25", "SemiAnalysis: How AI Labs Are Solving the Power Crisis", "https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power"),
    ("R26", "Earnings call highlight articles for Q1 and Q2 2026 (Yahoo Finance)", "https://finance.yahoo.com/sectors/energy/articles/ge-vernova-q1-earnings-call-030652565.html"),
    ("R27", "Clean Air Task Force, report on hydrogen in heavy-duty gas turbines (blade casting cost and yield)", "https://cdn.catf.us/wp-content/uploads/2023/07/13144950/emissions-performance-implications-hydrogen-fuel-heavy-duty-gas-turbines.pdf"),
    ("R28", "Howmet Aerospace, second quarter 2026 results, press release of 6 August 2026", "https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/"),
    ("R29", "Howmet Aerospace, Q2 2026 earnings call transcript (Motley Fool). Secondary", "https://www.fool.com/earnings/call-transcripts/2026/08/13/howmet-aerospace-hwm-q2-2026-earnings-call-transcript/"),
    ("R30", "Zacks Equity Research on Howmet's Q2 2026 results (via Yahoo Finance). Secondary", "https://finance.yahoo.com/markets/stocks/articles/hwm-q2-earnings-beat-estimates-164300840.html"),
    ("R31", "TheStreet: report of the chief executive's remarks on the $200 billion backlog, the January outlook and the spring 2027 investor day", "https://www.thestreet.com/investing/stocks/gev-ge-vernova-ceo-strazik-says-200b-backlog-target-on-track-very-early-2027"),
    ("R32", "Power Engineering: first US construction permit for the BWRX-300 small reactor, 29 September 2026", "https://www.power-eng.com/nuclear/smrs/tennessee-clinch-river-bwrx-300-smr-nrc-construction-permit/"),
    ("R33", "NRG, market update on the PJM auction for 2028/29, July 2026; PJM auction schedule", "https://www.nrg.com/assets/documents/insights/white-papers-and-webinars/pjm-bra-results-july2026.pdf"),
    ("R34", "Siemens Energy, investor relations: results calendar and Q3 FY2026 earnings release", "https://www.siemens-energy.com/global/en/home/investor-relations.html"),
    ("R35", "Investing.com: Evercore ISI reiterates its GE Vernova rating on raised estimates", "https://www.investing.com/news/analyst-ratings/evercore-isi-reiterates-ge-vernova-stock-rating-on-raised-estimates-93CH-4926745"),
    ("R36", "GE Vernova, press release: fourth quarter 2026 dividend, 30 September 2026", "https://www.gevernova.com/news/press-releases/ge-vernova-declares-fourth-quarter-2026-dividend"),
    ("R37", "Citadel Fall 2026 Pitch Competition, Official Rules", "https://www.citadel.com/wp-content/uploads/2026/06/Citadel-Fall-2026-Pitch-Competition-Official-Rules.pdf"),
    ("R38", "GE Vernova, 2025 Investor Update: press release and presentation, 9 December 2025", "https://www.gevernova.com/sites/default/files/gev_webcast_pressrelease_12092025.pdf"),
    ("R39", "Team research files in gev-corpus/docs/research/multi_agent/: 03 technical wedge hunt; 07 pitch winners; 09 overnight run (ROBUSTNESS_PACK, BLOOMBERG_VERDICT, D04 January guide); 11 thesis hunt (THESIS_HUNT, GIGAWATT_ANGLE); 12 team brief; 13 thesis dossier", None),
    ("R41", "Supplier filings on SEC EDGAR, read by the second-opinion check: Howmet 10-K FY2025 and 10-Q Q2 2026 (end-market revenue table); Carpenter Technology 10-K FY2026; ATI 10-Q Q2 2026; Woodward 10-Q June 2026", "https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm"),
    ("R42", "News reports of the Vineyard Wind settlement, 16 to 18 September 2026 (in the research corpus)", None),
    ("R40", "NRG Energy filings: Q4 2024 results release (February 2025), Form 10-Q for Q1 2025, Form 10-K for FY2025 (filed 24 February 2026)", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1013871&type=10-K"),
]

S_END = [("17. Limits of this file", [
    ("note", "**Bottom line.** The call is a 12-month long that rests on arithmetic and on one assumption, the 25x multiple. Everything else in this file is there so the team can check it."),
    ("md", """
- This is a research file made with AI assistance. Under rule 10 that use has to be disclosed, and the memo and the model have to be the team's own work. [R37]
- It contains no private information. Every source is a public filing, a public release or call, a licensed Bloomberg figure, or a published article.
- News items and transcript sites are marked as secondary. Check them before citing.
- Figures are as of 1 and 2 October 2026. Results on 28 October will date them.
- Charts for the memo should be remade by the team from its own model.
- An independent second AI (Grok) read the corpus and the suppliers' filings on the evening of 2 October 2026, in two passes, and found no number against the call. Its findings are in section 9 (rows 23 to 25), sections 5 and 6, and section 11. Disclose its use with the rest.
"""),
])]
