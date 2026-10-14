# What multiple will the market pay, and how does it move?

_D05_multiple — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 02:06:22. Requests 44, input tokens 3496636, output tokens 33217._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV: range for the Sep-2027 forward EV/EBITDA multiple, with implied prices

*Research input only. Every grid cell is a research range; the team picks its own multiple and estimate path.*

**Source key:**
- **CL** = Chartloom GEV series (evEbitdaNtm and peRatioNtm, not point-in-time), as reproduced in evidence_lanes_full.md rows BX-14 to BX-18 and the verifier note at offset ~143.8k.
- **MS** = MarketScreener valuation pages, 2026-09-29 (BX-27 to BX-36).
- **SA** = stockanalysis.com.
- **ZK** = Zacks/Nasdaq estimates API.
- **YF** = FinRobot yfinance pull, 2026-09-30. YF forward EPS matches SA to the cent (PWR 19.77394 in both), so YF and SA are **one feed**, not two independent sources.
- **10Q** = 0001996810-26-000148.

---

## 1. Bottom line

- **Where the stock breaks even in Sep-2027 depends on the estimate path.** Holding $962.49 needs 20.3x NTM EV/EBITDA if consensus holds, 21.9x after a 7.5% cut, and 23.2x after a 12.5% cut [computed; bridge from 10Q balance sheet and MS; NTM $12,191M from MS FY27 $9,574M and FY28 $13,064M].
  - Today's multiple is 28.2x (MS-based) or 27.7x (CL).
  - The consensus target of $1,237 equals about 26.3x [evidence_brief.md §C; TIKR 2026-09-21].
- **GEV's own multiple floor has risen, but it only reflects 2025-26 regimes.**
  - CL NTM EV/EBITDA troughs: 15.6x (2025-04-04), 16.5x (2025-03-10), 22.8x (2025-01-27), 23.4x (2025-11-04), 24.9x (2025-12-17), 28.5x (2026-06-10), 27.5x (2026-07-29), 25.4x (2026-09-14). Peaks: 33.1x and 40.4x.
  - NTM EV/EBITDA history is **[SINGLE-SOURCE]** (CL). The P/E history does cross-check against Yahoo (point-in-time) and TIKR (below).
- **Peers today are well below GEV (calendar-weighted NTM EV/EBITDA, computed from MS):**

  | Group | Names and multiples |
  |---|---|
  | US electrical/grid | PWR 22.0x, ETN 21.3x, VRT 20.6x, HUBB 15.1x (median ≈21x) |
  | Europe/Japan | ABB 19.0x, Schneider 16.4x, MHI 14.7x, Siemens Energy 12.6x |
  | All eight | Median ≈17.7x |

  - GEV has the highest two-year growth in the set: EBITDA CAGR 43.3% (MS) and EPS CAGR 44.3% (ZK; inflated by a low FY26 base).
  - TIKR independently puts VRT near 24x and Schneider near 17x forward EV/EBITDA (2026-08-25).
- **History says a premium multiple can halve while earnings still rise.**
  - GE: $60 peak in Aug-2000 = 42.6x FY2001 EPS of $1.41. By 2002-04-15, $31.85 = 21.1x FY2002 EPS of $1.51. EPS rose 19% from 2000 to 2002 [GE 2000 ex-99b and 2002 ex99b on SEC; GE 2002 press release; Blackwell GE case; NY Post 2002-04-16].
  - Cisco is **not** a "multiple fell while earnings rose" case. FY2001 pro forma EPS fell 23% ($0.53 to $0.41) on revenue +18% [Cisco FY01 release 2001-08-07; Cisco 2001-04-16 update].
- **Rates: the latest yield spike did not de-rate GEV.** The 10-year went from 4.96% (09-22) to 5.24% (09-28), with an intraday 5.27%, the highest since 2007 [FRED series via Exa library; Investing.com 2026-09-29; Seoul Economic Daily 2026-09-30]. GEV rose from $874.76 (09-14) to $962.49 (09-29) over the same stretch [BX-01, two feeds]. The earlier Aug-Sep leg (GEV −18.9%) had AI-capex and GLJ co-drivers, so rate sensitivity cannot be isolated.
- **Ownership is index-heavy at the top; the marginal holder is active and thinning.**
  - Top four holders ≈25.6%: BlackRock 8.17%, Vanguard 7.16%, FMR 6.05%, State Street 4.24% [Longbridge; MarketBeat 13F alert 2026-08-23; Investing.com as of 3/31].
  - Hedge-fund holders fell from 118 to 106 in Q2 [SINGLE-SOURCE: Insider Monkey].
  - Hazeltree places GEV in the "AI theme" short basket [TIKR citing Hazeltree].
  - Goldman's AI data-center long-crowding reading is 0.74 [Tickmill summary of the GS monitor, Aug-2026].

---

## 2. Answers

### Q1. GEV's forward multiples since the spin, around each event

The series is CL's daily NTM series. Within a calendar quarter CL holds estimates fixed, so any price move within the quarter shows up as a multiple move. Point-in-time checks are marked PIT.

| Date | Event | Day move | NTM EV/EBITDA (CL) | NTM P/E (CL) |
|---|---|---|---|---|
| 2024-04-05 | Post-spin low | — | n/a | 33.75x (series minimum) |
| 2024-07-24 | Q2'24 raise | −4.45% | — | — |
| 2024-11-11 | 2024 peak | — | — | 59.2x |
| 2024-12-10/11 | Dec-24 investor update, 2028 target to ~$45B / 14% | +5.01% | — | — |
| 2025-01-23 | Peak | — | — | 66.3x |
| 2025-01-27 | DeepSeek day | −21.5% | 22.84x | 50.0x (PIT 49.4x) |
| 2025-03-10 | Trough | — | 16.49x | 40.9x (PIT 40.4x) |
| 2025-04-04 | Tariff trough | — | **15.55x** | 33.8x |
| 2025-07-23 | Q2'25 raise | +14.58% | — | — |
| 2025-08-06 | Peak | — | 33.07x | 68.9x |
| 2025-10-22 | Q3'25 (Wind guide cut) | −1.59% | — | — |
| 2025-11-04 | Trough | — | 23.38x | 45.6x |
| 2025-12-09/10 | Dec-25 update, $52B / 20% | +15.62% | — | 60.2x |
| 2025-12-17 | Trough | — | 24.87x | 51.1x |
| 2026-01-28 | Q4'25, framework to $56B (Prolec) | +2.73% | — | — |
| 2026-04-22/23 | Q1'26 raise; peak | +13.75% | **40.39x** | 63.5x |
| 2026-06-10 | Trough | — | 28.54x | 47.9x (PIT 43.0x) |
| 2026-07-22 | Q2'26 raise, margin held | −8.69% | — | — |
| 2026-07-29 | Trough | — | 27.54x | 43.8x |
| 2026-09-14 | GLJ initiation; 10-year at 5% | −8.62% | 25.44x | 42.6x |
| 2026-09-29 | Today | — | 27.70x (MS-computed 28.2x) | 46.85x (SA 45.91x; TIKR 44.7x on 09-18) |

Sources:
- Prices and event returns: BX-01 and BX-13 (Yahoo and Nasdaq feeds agree on all 626 sessions).
- Multiples: BX-15 to BX-18, plus the verifier's evEbitdaNtm list (CL).
- PIT checks: BX-19 (Wayback capture of Yahoo) and BX-20 (Yahoo article dated 2026-06-22).
- Second source for the P/E range: TIKR 2026-09-21 gives a 12-month average of 56.3x and a spring peak near 70x.
- Event dates: BR-44 (GEV IR events page) and the 8-K filing dates.

Findings:
1. The big up-moves came on margin or framework raises (+14.6%, +15.6%, +13.75%). Raises without margin news did not protect the stock (Q2'26 −8.69%; Q2'24 −4.45%) [BR-38; BX-13].
2. EV/EBITDA troughs stepped up from 15.6x (Apr-25) to 23-25x (late 2025) to 25-28.5x (2026). Today's 27.7x sits in the lower half of the 2026 range.
3. CL reads high at troughs, so the trough values are an upper bound [evidence_brief.md §2].

### Q2. Peers today (prices as of 2026-09-29)

"NTM" EV/EBITDA below is computed as 1/(0.25/FY26 + 0.75/FY27), using MS multiples. Siemens Energy (Sep year-end) uses FY27 as NTM; MHI uses the average of FYMar27 and FYMar28.

| Ticker | EV/EBITDA FY26 / FY27 (MS) | NTM EV/EBITDA (computed) | FY27 P/E: S1 / S2 | 2-yr EPS CAGR |
|---|---|---|---|---|
| GEV | 38.9 / 25.8 (MS own: 38.4 / 25.0) | 28.2 | MS 38.7 / ZK 40.0 / SA 38.3 | 44.3% (ZK), EBITDA 43.3% (MS) |
| VRT | 27.2 / 19.1 | 20.6 (TIKR ~24 at $254.97 on 08-24) | SA/YF 27.1 / ZK 27.7 | 32.3% |
| ETN | 24.0 / 20.5 | 21.3 | SA/YF 26.8-26.9 / ZK 27.2 | 17.3% |
| PWR | 24.8 / 21.2 | 22.0 | SA/YF 33.0 / ZK 36.2 | 15.0% (ZK) / 21.5% (MS GAAP) |
| HUBB | 17.0 / 14.6 | 15.1 | SA/YF 20.0 / ZK 20.4 | 11.8% |
| ABB | 21.0 / 18.4 | 19.0 | SA 27.1 (ABBNY) / MS 27.5 | ~12.6% (12.1% then 13.0%) |
| Schneider | 18.4 / 15.8 | 16.4 (TIKR ~17) | SA 24.4 / MS 25.8 | 18.6% |
| Siemens Energy | 17.0 / 12.6 | 12.6 | MS 23.5 / SA 23.6 | 36.0% |
| MHI | 15.9 / 13.6 | 14.7 | MS FYMar28 25.0 / SA forward 30.8 | 16.4% |

Sources: BX-29 to BX-36 (MS, SA, ZK); FinRobot YF pull 2026-09-30; TIKR Vertiv note 2026-08-25.

- Peer EV/EBITDA rests on MS alone, apart from the two TIKR cross-checks: **[SINGLE-SOURCE]** for ETN, PWR, HUBB, ABB, MHI and Siemens Energy. The YF data is trailing and cannot serve as a check.
- **On growth, GEV is the fastest in the set.** Siemens Energy (36%) and Vertiv (32%) are closest, and they trade at 12.6x and 20.6x.
- A rough EV/EBITDA-to-growth ratio gives GEV 0.65, VRT 0.64, Siemens Energy 0.35, Schneider 0.88, MHI 0.90, ETN 1.23, HUBB 1.28, PWR 1.47, ABB 1.51. This mixes EPS and EBITDA growth bases (definition mismatch; see BX-39).
- On growth-adjusted terms GEV is priced like Vertiv, not at an outlier premium.

### Q3. GE at the 1999-2001 gas-turbine boom peak, and after

- **Earnings:** GE diluted EPS was $1.27 (2000), $1.41 (2001), $1.51 (2002, before accounting changes) [S1: GE 2000 financials ex-99b, SEC 797463/000079746301500003; S2: GE 2000 annual report] [S1: GE 2002 ex99b, SEC 0000040545-03-000021; S2: GE 2002 earnings press release].
- **Price:** $60 peak in Aug-2000 [Blackwell "GE: Life after Jack" case]. $31.85 on 2002-04-15 [NY Post 2002-04-16]; below $33 on 2002-04-24 [Blackwell].
- **Multiple:**
  - At the peak: 47.2x FY2000 EPS and 42.6x FY2001 EPS [computed]. "Around 40x" [jayvas.com; **[SINGLE-SOURCE]** for the qualitative figure].
  - By 2002-04: 21.1x FY2002 EPS [computed].
  - Result: P/E halved while EPS grew 19%.
- **Power Systems** grew from 11.4% to 16.1% to 17.4% of GE revenue across 2000-2002 [GE 2002 10-K via EDGAR Online]. Power Systems earnings rose 29% in 2002 before falling in 2003 [V07, citing GE 10-K 2003 ex13 and the 2002-07-23 release].
- **Not found:** a standalone multiple for GE Power, which was never separately traded.
- **Caveat:** GE's 2001-02 de-rating was driven largely by the conglomerate and accounting ("Welch premium", Enron-era trust) [NY Post; Inc. 2002-10-01]. It is not a clean gas-cycle test.

### Q4. "Picks and shovels" suppliers

- **Cisco:** traded at 220x GAAP EPS of $0.36 on 2000-03-27 [Kingswell], cited elsewhere as about 200x [Yahoo Finance/Cisco-25-years article]. That is about 151x FY2000 pro forma EPS of $0.53 [computed].
  - The stock de-rated before earnings fell. FY2001 revenue was +18% but pro forma EPS −23%, with a GAAP loss of $1.01B [Cisco FY01 release; Cisco 2001-04-16 update]. The shares fell 83-86% [Standard Chartered; ProfitByFriday].
  - So the premise "earnings kept rising" fails for Cisco.
- **GE 2000-02** (Q3) is the cleaner case of earnings rising while the multiple halved.
- **Caterpillar:** record 2012 EPS of $8.48, up 15% [CAT Q4'12 release; Equipment World 2013-01-28]. The price path and multiple were **not verified** here, so do not cite CAT's multiple.

### Q5. Premium-industrial de-ratings on growth deceleration or guides

| Name | Date | Trigger | Move | Sources |
|---|---|---|---|---|
| Siemens Energy | 2023-06-23 | Guidance withdrawn (Gamesa quality) | −37% | CNBC; Reuters; SE ad-hoc 2023-06-22 |
| GEV | 2025-01-27 | DeepSeek | −21.5% (1d); NTM EV/EBITDA 33→16x by Apr | BX-04; CL |
| GEV | 2026-07-22 | Raise without margin raise | −8.69% | BX-13; BR-38 |
| Vertiv | 2026-07-29 | Beat and raise, revenue −3% vs consensus | −17% | CNBC 2026-07-29; Economic Times; Motley Fool |
| Vertiv | through 2026-08-24 | Yields and multiple | −33% from $379.94 high | TIKR 2026-08-25 **[SINGLE-SOURCE]** |
| Rockwell | 2026-08-04 | Raise only matched consensus | −7.2% (intraday −10%) | Weiss Ratings; Seeking Alpha |
| Siemens AG | 2026-08-06 | Raise short of hopes | −4% to −6% intraday | AFP; MarketScreener/Dow Jones |
| GE (Power) | 2017-18 | Bullish guide on flat demand | Power profit −45%; shares −50%+ | V07: Reuters 2018-02-23; POWER 2018-02-28 |

The 2026 pattern: in this group, a raise that is merely "in line" is punished 4-17% in one day.

### Q6. Moves on large 10-year yield changes, 2025-26

| Window | 10-year yield | GEV and peers | Sources |
|---|---|---|---|
| Week to 2025-04-11 | +~50bp to 4.49% (biggest weekly rise since 2001) | GEV trough $271.48 on 04-04 (15.6x); 04-11 close **not retrieved** | Bloomberg; Syz |
| 2026-08-18 | 10-year 4.68%; 30-year at a 19-year high | GEV −6%, CAT −4-5%, VRT −7% (same day as WSJ hyperscaler-debt report) | 24/7 Wall St; Foreign Policy Journal |
| Week of ~08-17 to 08-21 | Long yields spiked | VRT ≈−11% | TIKR **[SINGLE-SOURCE]** |
| 2026-09-14 | Hit 5% | GEV −8.6%; VRT, ETN, Siemens Energy −7.6% to −8.0% | TipRanks; BX-09; POS-06 |
| 09-22 to 09-28 | 4.96% to 5.24% | GEV 09-23 $951.82, 09-28 $949.77, 09-29 $962.49: flat to up | FRED via Exa library; Investing.com; BX-01 / P3 |

No regression was possible because no yield series was accessible. Rate shocks hit GEV mainly when they coincided with AI-capex risk-off.

### Q7. What 28x and 20x each require in Sep-2027

**28x (implies $1,316, +36.7% on consensus, above the $1,237 target):**
- Estimates hold. That needs a January-2027 FY27 guide margin of at least ~18%, versus the 18.15% consensus [MS; master brief kill rule].
- The market keeps a ≈1.3x premium to the best US peer (PWR at 22x today).
- Next-year growth at Sep-2027 still looks like today's +39% NTM roll-forward. That depends on FY29 consensus, which is not available and which the spring-2027 Capital Markets Day 2030 outlook would set.
- Precedent: GEV's multiple has held at 25x or more at every trough since Dec-2025 (CL).

**20x (implies $950, the consensus breakeven):**
- Roughly today's US-peer median (≈21x).
- Needs the market to price GEV's FY28-29 growth like ETN or PWR (15-20%) rather than Siemens Energy or VRT. The GE 2000-02 analog shows a halving is possible even with earnings rising.
- GEV's own 2025 troughs (15.6-16.5x) and GLJ's ≈15.6x mark the floor below that.

### Q8. Who owns GEV, and what crowding does to downside

| Holder | Stake | Sources |
|---|---|---|
| BlackRock | 8.17% (21.76M) | MarketBeat; Longbridge |
| Vanguard | 7.16% | Longbridge (conflicting figures; see note) |
| FMR | 6.05% / 6.00% | Longbridge / Investing.com |
| State Street | 4.24% | **[SINGLE-SOURCE]** |
| Capital Research | 2.26% | **[SINGLE-SOURCE]** |

- **Vanguard conflict:** Longbridge shows 19.07M shares but dates it 3/31, while Investing.com shows 17.52M (6.52%) at 3/31.
- Institutions hold 81.69% [Longbridge, **[SINGLE-SOURCE]**]. There are 3,624 13F holders [13finsight].
- **13F aggregates are unreliable:** 13f.info shows 696M shares held, more than the 266M outstanding.
- **Crowding:**
  - Hedge-fund holders fell from 118 to 106 [Insider Monkey].
  - Hazeltree lists GEV among the most-shorted large names for 10 consecutive months; this is a dollar ranking [TIKR].
  - Short interest is only 3.3% of float [MarketBeat; SA].
  - Goldman's VIP basket had its worst month against the S&P in 20+ years in July 2026 [Evidence Investor citing CNBC 2026-08-21]. GEV fell −23.4% from 06-30 to 07-29 in the same window, but GEV's membership in the VIP list was **not verified**.
- **Implication (inference):** index holders are not the marginal seller. A de-rating would run through active and hedge-fund exits (FMR and Capital Research are the large active holders). The −23% July episode is the in-sample template for de-grossing.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | GEV NTM EV/EBITDA today | 28.2x / 27.7x | MS via BX-27 | CL | close | H |
| 2 | EV/EBITDA troughs | 15.55x to 28.54x | CL (verifier note) | none — [SINGLE-SOURCE] | — | M |
| 3 | NTM P/E range | 33.8x to 68.9x; TIKR 12-mo average 56.3x | CL, BX-15 | TIKR 2026-09-21 | close | M |
| 4 | Consensus NTM EBITDA Sep-27 | $12,191M | MS | GLJ FY27 $9.45B cross-check | close | M |
| 5 | Peer multiples | table in Q2 | MS | SA / ZK / TIKR | close for P/E; EBITDA mostly single | M |
| 6 | GE EPS 2000-02 | $1.27 / $1.41 / $1.51 | SEC ex-99b | GE annual report / press release | exact | H |
| 7 | GE peak price | $60, Aug-2000 | Blackwell case | NY Post (context) | close | M |
| 8 | Cisco FY01 EPS | pro forma −23%; GAAP loss $1.01B | Cisco release | SEC 10-K text | exact | H |
| 9 | Siemens Energy one-day drop | −37% | CNBC | Reuters | exact | H |
| 10 | Vertiv one-day drop | −17% | CNBC | Motley Fool | close | H |
| 11 | Rockwell drop | −7.2% | Weiss | Seeking Alpha | close | M |
| 12 | 10-year yield | 5.24% (09-28) | FRED via Exa library | Seoul Economic Daily (5.27% intraday) | close | H |
| 13 | BlackRock stake | 8.17% | MarketBeat | Longbridge | exact | H |
| 14 | Hedge-fund holder count | 118 → 106 | Insider Monkey | none — [SINGLE-SOURCE] | — | L |

---

## 4. Arithmetic

- **Formulas:** price = (M × E + 9,113) / 266.33. Breakeven multiple = (962.49 × 266.33 − 9,113) / E = 247,227 / E.
- **Estimate paths:**
  - Consensus: E = $12,191M.
  - −7.5%: E = $11,277M (band −5% to −10% = $11,581M to $10,972M).
  - −12.5%: E = $10,667M (band −10% to −15% = $10,972M to $10,362M).

**Grid: Sep-2027 price by NTM EV/EBITDA and estimate path (change vs $962.49)**

| Path | 16x | 18x | 20x | 22x | 24x | 25x | 26x | 28x |
|---|---|---|---|---|---|---|---|---|
| Consensus | 767 (−20%) | 858 (−11%) | 950 (−1%) | 1,041 (+8%) | 1,133 (+18%) | 1,179 (+22%) | 1,224 (+27%) | 1,316 (+37%) |
| −7.5% | 712 (−26%) | 796 (−17%) | 881 (−8%) | 966 (0%) | 1,050 (+9%) | 1,093 (+14%) | 1,135 (+18%) | 1,220 (+27%) |
| −12.5% | 675 (−30%) | 755 (−22%) | 835 (−13%) | 915 (−5%) | 996 (+3%) | 1,036 (+8%) | 1,076 (+12%) | 1,156 (+20%) |

Edge values: at −5%, 20x = $904 and 25x = $1,121. At −10%, 20x = $858 and 25x = $1,064. At −15%, 16x = $657 and 22x = $890.

**Research ranges for the plausible multiple on each path (the team chooses):**

| Path | Multiple range | Anchors | Implied price |
|---|---|---|---|
| Consensus holds | 22-28x | 2026 CL trough band 25.4-28.5x; consensus target 26.3x; best US peer 22x | $1,041-1,316 |
| Cut 5-10% | 20-25x | A cut breaks the "never cut" record; −8.7% reaction to a margin-flat raise; Nov-25 trough 23.4x; US-peer median ≈21x | $858-1,121 |
| Cut 10-15% | 16-22x | 2025 troughs 15.6-16.5x; GLJ ≈15.6x; all-peer median 17.7x; GE 2000-02 halving | $657-940 |

**Other computations:**
- Peer NTM example: ETN = 1/(0.25/24.0 + 0.75/20.5) = 21.3x; the same formula gives every row in Q2.
- GEV EBITDA CAGR = (13,064 / 6,359)^0.5 − 1 = 43.3%.
- GE multiples: 60/1.41 = 42.6x; 60/1.27 = 47.2x; 31.85/1.51 = 21.1x.
- Top-four holders: 8.17 + 7.16 + 6.05 + 4.24 = 25.6%.
- Net-cash sensitivity: the bridge holds today's net cash of $9,113M. Consensus FCF to Sep-2027 would add several $B before buybacks. Each +$1B of net cash adds $3.75 per share.

---

## 5. General question bank

- **G1 / G5:** If the stock is flat for 12 months at consensus, the multiple compresses to 20.3x.
- **G15:** Implied downside cells run from −13% to −30% on the cut paths at 16-20x. GEV's own median drawdown is −24.6% [BX-03 to BX-08].
- **G16:** Rates are the risk most often dismissed, and the latest spike did not move GEV. The more dangerous co-driver is AI-capex risk-off, which featured on 08-18 and 09-14.
- **G19:** See Q3 and Q4.
- **G20:** EV/EBITDA history and peer EBITDA multiples are thinly sourced. YF and SA are one feed.

## 6. What would change these findings

- **Floor moves up:** PIT EV/EBITDA history showing troughs above 25x would raise the cut-path floors.
- **Floor moves down:** US peers re-rating toward 15-17x would drag the "consensus holds" band down.
- **Ceiling moves up:** a spring-2027 Capital Markets Day 2030 outlook implying FY28-29 growth above 30% would support the 28x case.
- **Rate view changes:** evidence that GEV fell on a pure-rate day with no AI news would overturn the Q6 read.

## 7. Disagreements with the master brief

1. **"Never cut"** holds for company revenue and FCF only. Wind guidance was cut at Q3'25, and the Wind 2028 margin target went from 10% to 6% [BR-11: 8-K 0001996810-25-000159; Dec-25 PDF].
2. **The 10-year yield is now 5.24%**, not the 5% the brief cites for 09-14, and GEV's multiple held through the rise.
3. **Who presents the January 2027 call:** V07 reports Ken Parks presents it, not the new CFO. This is unverified here.
4. **The +39% roll-forward** does absorb de-rating, but only down to 20.3x. That is the US-peer median, not a stretched assumption.

## 8. Open items

- A point-in-time GEV NTM EV/EBITDA series, from FactSet/Bloomberg or Wayback captures of MS.
- A second source for peer forward EBITDA (Koyfin or TIKR).
- GEV's close on 2025-04-11.
- Whether GEV is in the Goldman VIP list, and Q3'26 13Fs (due mid-November).
- FY29 consensus.
- CAT's 2011-12 multiple path.
- GE Power's 2003 profit decline, from the primary GE 10-K.
