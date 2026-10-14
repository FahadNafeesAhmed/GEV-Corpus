# Why would the multiple fall by January, or not? Evidence on both sides

_S04_multiple_evidence — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 10:27:21. Requests 38, input tokens 3422799, output tokens 48021._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV: will the market still pay ~28x NTM EV/EBITDA by late January 2027? Evidence on both sides (research input only)

*The team chooses every number and writes every sentence. Nothing below is memo prose.*

**Source key**
- **NQ**: Nasdaq historical-price API for GEV, read 2026-09-30. Windows used: 2025-09-29→2025-12-31 and 2025-11-01→2026-05-29 (only ~66 rows came back for the Jul–Dec 2025 request), plus the latest rows 2026-08-12→09-29.
- **SAH**: stockanalysis.com GEV price history (S&P Global MI data), 2026-07-10→09-18, read 2026-09-30.
- **BX-01**: Yahoo and Nasdaq daily closes. Prior verifier: all 626 sessions agree within $0.02 (evidence_lanes_full).
- **SAR**: stockanalysis.com GEV quarterly ratios page, read 2026-09-30.
- **CL**: Chartloom NTM series (BX-14 to BX-18 and the verifier note in evidence_lanes_full). It is not point-in-time.
- **MS**: MarketScreener, 2026-09-29.
- **10Q2**: 0001996810-26-000148 (Q2'26 10-Q), MD&A chunk 5745. **10Q1**: 0001996810-26-000064, chunk 13710.
- **D04B, D05, R08, F01, R01, V07**: tonight's earlier outputs.

---

## 1. Bottom line

1. **Late January rolls the NTM window almost entirely onto FY27, so the price holds even if the multiple falls.** Late-Jan NTM EBITDA at consensus is $9,865M, so today's price equals **25.1x**.
   - At the research FY27 range ($8.6–8.9B), break-even is **27.9x / 27.0x**. The short needs roughly ≤26x to make money, not merely "below 28x".
   - Sources: [computed §4-A; inputs MS FY27 $9,574M / FY28 $13,064M; F01 §Q3; 10Q2 balance sheet via facts.csv].
2. **Over the last 12 months GEV's month-end NTM EV/EBITDA has not closed below ~25x, and no close has been at or below 23x.**
   - Today's 27.7x sits at about the 33rd–36th percentile of 12 month-ends and about the 17th percentile of the last 6.
   - Caveats: EV/EBITDA history is still **[SINGLE-SOURCE: CL]**, and the month-ends are my reconstruction from CL anchors (§4-B).
   - Sources: [S1: CL troughs] [S2: prices NQ / BX-01].
3. **The 25.5% fall from the June high to the September low was about all multiple.** On CL, the multiple went 37.9x→25.4x while CL-implied NTM EBITDA rose ~10%.
   - Point-in-time FY27 EPS rose only ~+2.5% over the same window (24.25→24.85).
   - Sources: [S1: CL / NQ, computed] [S2: R08 (YF "90 days ago" 24.25; MS 24.85)].
4. **Peer relative value is the best evidence for compression, but it has never bound in 2.5 years.**
   - GEV is at 28.2x against US electrical peers at ~21x and Siemens Energy at 12.6x.
   - Growth-adjusted, GEV (0.65) is priced about like Vertiv (0.64). The gap to Siemens Energy is not explained by growth: GEV trades at 2.2x SE's multiple but grows only ~1.2x faster.
   - Sources: [S1: MS, D05 §Q2] [S2: TIKR cross-checks for VRT/Schneider; peer EV/EBITDA otherwise **[SINGLE-SOURCE]**].
5. **Reference class: I could verify only 4 strict cases, not the 8 requested.** Three fell on the day (VRT 2025, ANET 2025, ETN 2026: −6% to −10% intraday) and one rose (PWR 2025, +5%).
   - GEV's own two December first guides were at or below consensus on revenue, yet rose +5.01% and +15.62%. Both came with framework raises, so they break the "long-term targets kept" condition.
   - Sources: §2 Q5 table (two sources per case where available).
6. **Near-term triggers for de-rating in-sample have been AI-capex risk-off days and "margin held" report days, not rates.**
   - AI-capex days: 2025-12-17 −10.50% (Oracle/Michigan data-center story); 2026-08-18 −6.90%; 2026-09-14 −8.62% alongside peers.
   - Margin-held report day: 2026-07-22 −8.69%, −12.55% over 5 days.
   - The 10-year yield rose 4.96%→5.24% (09-22 to 09-28) with GEV flat to up.
   - Sources: [S1: NQ] [S2: EnergyWatch 2025-12-18; Invezz 2025-12-18; D05 §Q6].

---

## 2. Answers

### Q1. Multiple history, percentiles, time at or below 26x / 25x / 23x

**Vendor coverage**
- **NTM EV/EBITDA:** only one free historical vendor, CL.
  - YCharts' forward EV/EBITDA is paywalled; the page shows "--".
  - TGMCharts, tickerleague, valueinvesting.io, Business Quant and SAR all publish *trailing* EV/EBITDA (62.99x on SAR today), which is useless here.
  - So the EV/EBITDA history stays **[SINGLE-SOURCE: CL]**.
  - Point cross-checks: today MS-computed 28.2x vs CL 27.70x. On 09-14, a computed 26.2x (from GLJ's "Street $9.45B" FY27) vs CL 25.44x (§4-C).
- **NTM P/E:** two vendors. CL daily (BX-15/16) and SAR quarter-end "Forward PE".

**P/E at quarter-ends, both vendors**

| Quarter-end | Close (NQ/BX-01; SAR) | SAR forward P/E | CL NTM P/E |
|---|---|---|---|
| Q2'24 | 170.79 | 40.70 | — |
| Q3'24 | 253.91 | 52.62 | — |
| Q4'24 | 327.79 | 51.96 | 49.85 |
| Q1'25 | 304.22 | 47.14 | — |
| Q2'25 | 527.72 | 69.08 | — |
| Q3'25 | 614.90 (SAR 613.51) | 60.34 | — |
| Q4'25 | 653.57 (SAR 652.36) | 59.60 | 42.17 |
| Q1'26 | 872.90 (SAR 872.45) | 60.74 | — |
| Q2'26 | 1,174.86 | 63.97 | 57.2 |
| 2026-09-29 | 962.49 | **45.71** | **46.85** |

- **Vendor conflict (a finding):** at 2025-12-31, SAR 59.60x vs CL 42.17x. The implied EPS is $10.97 vs $15.50. SAR's EPS basis is undisclosed. YF's 38.31x uses FY27 EPS of $25.13 (P4). Do not mix these bases in the memo.
- **P/E percentile:**
  - SAR quarter-ends: today's 45.71x is **below every quarter-end in the last 24 months** (0th percentile of 9 observations).
  - CL daily since the spin: p25 45.8x, median 50.85x, p10 40.9x (BX-15). Today's 46.85x is ≈ p27.
  - CL 2026 year-to-date: minimum 40.17x (01-09), median 51.91x (BX-16).

**EV/EBITDA peaks and troughs (CL):**
- Troughs: 15.55x (2025-04-04), 16.49x (03-10), 22.84x (01-27), 23.38x (11-04), 24.87x (12-17), 28.54x (2026-06-10), 27.54x (07-29), 25.44x (09-14).
- Peaks: 33.07x (2025-08-06), 40.39x (2026-04-23).
- Today: 27.70x.

**Reconstructed month-end NTM EV/EBITDA, last 12 months** [computed §4-B; CL anchors plus NQ closes]

| Month-end | Oct-25 | Nov-25 | Dec-25 | Jan-26 | Feb-26 | Mar-26 | Apr-26 | May-26 | Jun-26 | Jul-26 | Aug-26 | Sep-29 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Multiple | 25.1x | 25.1x | 26.0x | 27.9x | 32.6x | 31.3x | 37.7x | 32.5x | 37.9x | 30.3x | 26.5x | 27.7x |

**Percentile of today's 27.7x**
- 12 months: 4 of 12 month-ends are lower → ~33rd–36th percentile.
- 6 months (Apr–Sep): 1 of 6 is lower → ~17th percentile.
- 24 months: **cannot be computed.** CL anchors for Oct-24 to Sep-25 lack the matching EV. The 2025 troughs (15.6–22.8x) imply a higher percentile for today.

**Episodes at or below the threshold, last 12 months (closing basis; reconstruction; ±~1 turn of error)**

| Threshold | Episodes |
|---|---|
| ≤26x | (i) about 10-03 to 12-09-2025, ~9 weeks nearly continuous (Oct values are lower bounds; see §4-B). (ii) 12-17/18-2025, 2 sessions. (iii) 01-08 to 01-26-2026, ~12 sessions with gaps; low ≈24.4x on 01-09. (iv) 09-14/15-2026, 2 sessions. |
| ≤25x | (i) about 10-22 to 12-01-2025, ~6 weeks intermittent (low 23.38x on 11-04, CL). (ii) 12-17-2025, 1 session (24.87x, CL). (iii) 01-08/09-2026, ~2 sessions (≈24.4–24.7x). |
| ≤23x | **None.** The closest was 23.38x on 11-04-2025. The intraday low of $530.16 on 11-21-2025 would be ≈22.5x intraday only. |

- The January 2026 episode assumes linear estimate growth from 12-17 to 04-23. If the estimate step came at the 01-28 print, the January multiples are understated.

### Q2. Price change split into estimate and multiple

Method: ln(price) change ≈ ln(ΔNTM EBITDA) + ln(Δmultiple). The net-cash effect (~4% of EV) is ignored. Details in §4-D.

| Window | Price | NTM EBITDA change | Multiple change | Share of move | Sources |
|---|---|---|---|---|---|
| **52-week high → 09-14 low.** Intraday high **$1,195.94 on 2026-07-06**; closing high $1,174.86 on 06-30 | 1,174.86 → 874.76 = **−25.5%** | CL-implied 8,018 → 8,800 (+9.8%, 06-30 interpolated). Point-in-time FY27 EPS +2.5% (24.25 late-Jun YF → 24.85 MS) | 37.9x → 25.44x (**−32.9%**) | Multiple ≈ −130% of the move; estimates/roll ≈ +30%. CL P/E: 57.2x → 42.6x with NTM EPS unchanged (20.54 → 20.53) | [S1: Yahoo meta/BX-40 high date; NQ] [S2: SAH closes; CL BX-17/18; R08] |
| **2026-07-22 (Q2'26)** | 1,078.81 → 985.03 = **−8.69%** (5-day −12.55% to 943.38; 20-day −6.89% to 1,004.53) | FY27 EPS +1.7% to +4.3% (YF 24.36 / CN 04-25 23.76 → CN 07-23 24.78; revisions cluster at prints per R08) | ≈ **−10% to −12%** | ~all multiple | [S1: NQ/SAH] [S2: BX-13; R08 CN 6544296] |
| **2026-04-22 (Q1'26)** | 991.30 → 1,127.56 = **+13.75%** (5-day +9.85% to 1,088.93; 20-day +2.07% to 1,011.80) | FY27 EPS 23.27 → 23.76 (+2.1%) in 1–2 days; 21.81 (02-09) → 23.76 (+8.9%) quarter to quarter | ≈ **+11.4%** on the day; CL peak 40.39x on 04-23 | ~85% multiple on the day | [S1: NQ] [S2: BX-13; R08 CN 6430863 / 6432423] |
| **Dec-2025 investor update** (12-09 after close) | 621.90 (12-08) → 723.00 (12-10) = **+16.26%** over two days; 5-day +9.56% (681.35); 20-day +6.50% (662.32 on 01-07) | CL-implied ~6,136 → ~6,153 over two days (interpolated; the framework-driven revision is not observable point-in-time). Pre-event FY27 consensus **not found** | ≈ 25.5x → 29.8x (+16.8%) | ~all multiple on the day | [S1: NQ] [S2: BX-13; D04B (Barron's "jumped 16%")] |

- **Dec-2025 round trip (a finding):** by 12-17-2025 the close was **$614.19, below the pre-event $621.90**. That day was −10.50% on an Oracle / Michigan data-center financing story. The framework-raise multiple expansion was fully given back within 6 sessions.
  - Sources: [S1: NQ] [S2: EnergyWatch 2025-12-18, "fell 10.5%"; Invezz 2025-12-18, "bottomed at $614"].

### Q3. Peers, growth-adjusted premium, the Siemens Energy gap

**Peer multiples.** D05's table stands; I re-used it and did not re-pull.
- NTM EV/EBITDA (MS-computed): PWR 22.0x, ETN 21.3x, VRT 20.6x, HUBB 15.1x, ABB 19.0x, Schneider 16.4x, MHI 14.7x, Siemens Energy 12.6x. All-eight median ≈ 17.7x.
- P/E has two sources per name (MS/SA/ZK). EV/EBITDA is **[SINGLE-SOURCE: MS]** except VRT (~24x) and Schneider (~17x), which TIKR cross-checks (2026-08-25).
- **Not covered:** Hitachi and Baker Hughes. Neither this pass nor D05 pulled them. This is an open item.

**Growth-adjusted (EV/EBITDA ÷ two-year growth; mixed EPS/EBITDA bases, see BX-39)**

| Name | Ratio |
|---|---|
| GEV | 0.65 (28.2 / 43.3% EBITDA CAGR, MS) |
| VRT | 0.64 |
| Siemens Energy | 0.35 |
| Schneider | 0.88 |
| MHI | 0.90 |
| ETN | 1.23 |
| HUBB | 1.28 |
| PWR | 1.47 |
| ABB | 1.51 |

Source: [S1: MS] [S2: ZK/SA EPS growth, per D05].

**Siemens Energy gap, factor by factor**

| Factor | Evidence | Explains the gap? |
|---|---|---|
| Growth | EPS CAGR: SE 36% vs GEV 43–44% (ratio ~1.2x), against a multiple ratio of 28.2 / 12.6 = 2.24x [computed; D05] | Explains little |
| Fiscal year | SE's September year-end means its "NTM" is already FY27. Compared like-for-like on FY27, GEV is 25.8x vs SE 12.6x, still ~2x [MS] | Explains a small part |
| Margins | SE FY26 guide 9–11% profit margin before special items; FY28 target 14–16% [S1: SE Q4 FY25 presentation, MarketScreener 2025-11-13] [S2: SE press release 2025-11-14]. GEV 2028 framework: 20% adj EBITDA. Definitions differ (SE's is pre-special items, EBITA-type), so the margins are **not comparable at face value** | Partly; definition trap |
| Deposits, pensions, minorities | Not quantified for SE in this pass. GEV's fuller bridge (pension etc.) moves EV only $247.2B → $250.7B (brief) | Small for GEV; SE side open |
| Sentiment / listing | No direct evidence found. SE's own FY28 targets were raised twice and the stock "took off" (dpa-AFX via MarketScreener 2025-11-14) | Undetermined |

Verdict: the residual is sentiment or listing plus definitions. It is not growth. [research judgement]

### Q4. Event study: every report and investor event since the spin

1-day moves are verified (BX-13, D04B). 5- and 20-day moves are computed from NQ/SAH (day 1 = event day, measured against the prior close). Guide columns come from F01, R01, D04B and the brief. "Result vs consensus" was researched only where shown.

| Date | Event | Guides (Rev / margin / FCF / long-term) | Result vs consensus | 1d | 5d | 20d |
|---|---|---|---|---|---|---|
| 2024-04-25 | Q1'24 | first FY24 guide reaffirmed (margin qualitative) | not researched | +1.46% | n/a | n/a |
| 2024-07-24 | Q2'24 | raised (cash) | n/a | −4.45% | n/a | n/a |
| 2024-10-23 | Q3'24 | held / raised | n/a | +1.25% | n/a | n/a |
| 2024-12-10/11 | Dec-24 investor update | FY25 first guide, rev −2.0% vs $37.25B; margin "HSD"; LT raised to $45B / 14%; $6B buyback | below on revenue | −2.34% / **+5.01%** | n/a | n/a |
| 2025-01-22 | Q4'24 | reaffirm | n/a | +2.67% | n/a | n/a |
| 2025-04-23 | Q1'25 | held / raised | n/a | +3.07% | n/a | n/a |
| 2025-07-23 | Q2'25 | raised; first numeric margin 8–9% | n/a | **+14.58%** | n/a | n/a |
| 2025-10-22 | Q3'25 | **Wind cut** | n/a | −1.59% | −2.45% | −5.19% |
| 2025-12-09/10 | Dec-25 investor update | FY26 first guide, rev +0.5% vs $41.3B; margin 11–13%; LT +6 pts; buyback to $10B | at or slightly above | +0.55% / **+15.62%** | +9.56% | +6.50% |
| 2026-01-28 | Q4'25 | rev raised (Prolec); margin held; FCF raised; LT $56B (Prolec) | n/a | +2.73% | +12.64% | +26.46% |
| 2026-04-22 | Q1'26 | rev / margin / FCF raised | "exceeded consensus across every key metric" [SINGLE-SOURCE: corpus chunk 246495] | **+13.75%** | +9.85% | +2.07% |
| 2026-07-22 | Q2'26 | rev and FCF raised; **margin held** | adj EPS $2.47 miss; EBITDA −2.1% vs estimates [StockStory; Reuters, via R08] | **−8.69%** | −12.55% | −6.89% |
| 2026-09-16 | Laguna conference (CEO) | none | — | +4.79% | +7.64% | n/a |

**What the sample shows (n = 12–13, raw returns, no market adjustment)**
- The three largest up-days came on margin or long-term framework raises (+14.58%, +15.62%, +13.75%).
- The worst report day was the only one where company margin was held while other lines were raised (−8.69%).
- The January Q4 days have both been small positives (+2.67%, +2.73%). The 20-day drift after Jan-26 was +26.5%.
- No FY guide has ever been given first on a January call.
- The sample is too small to separate the effects of margin, framework, AI news and market beta.

### Q5. Reference class

**Selection rule, fixed before looking at outcomes:**
1. Large-cap capex-cycle equipment or infrastructure name.
2. First annual guide for the next fiscal year.
3. Midpoint at or below the published consensus on its headline metric.
4. Long-term targets not raised on the day.
5. Premium multiple (NTM EV/EBITDA ≥ ~25x).

Criterion 5 could **not** be verified historically for any peer case, so it is relaxed to "premium to sector". Criterion 3 was checked with two sources where possible.

| Case | Date | Guide vs consensus | 1-day | 1m / 3m | Multiple before / after | Sources | In class? |
|---|---|---|---|---|---|---|---|
| Vertiv | 2025-02-12 | FY25 adj EPS midpoint $3.55 vs $3.57 (−0.6%); Q1 guide below | "tumbled nearly 10%" (intraday) | not retrieved | not verified | Nasdaq/RTT; Investopedia; IBD | **Yes: down** |
| Quanta | 2025-02-20 | FY25 adj EPS midpoint $10.20 vs $10.25 (The Fly) / $10.22 (LSEG) | "jumped more than 5%" | not retrieved | not verified | Markets Insider; MarketScreener/Reuters; Zacks/Yahoo | **Yes: up** |
| Arista | 2025-02-18/19 | ~17% ($8.2B), raised from 15–17% but below "hopes"; the consensus gap is not quantified | −7.3% intraday | not retrieved | not verified | Barchart 02-19; Barchart 02-22 (same publisher) | Yes, weak (gap unquantified) |
| Eaton | 2026-02-03 | "2026 outlook trails estimates" (first guide $13.00–13.50) | −6.2% premarket | not retrieved | not verified | Seeking Alpha 02-03; Grafa 02-03; Smartkarma (prior range) | **Yes: down** |
| GEV | 2024-12-10 | revenue −2.0% | +5.01% (next day) | — | CL n/a | D04B; BX-13 | No (long-term raised) |
| GEV | 2025-12-09 | revenue +0.5% | +15.62% (next day) | 20d +6.5% | ~25.5x → 29.8x → 24.9x by 12-17 | D04B; NQ; CL | No (long-term raised) |
| ASML | 2024-10-15 | 2025 guide to lower half of €30–35B; bookings about half of expectations | "biggest one-day drop since 1998" | — | — | Reuters; CNBC; Bloomberg | No (mid-year cut, not a first guide) |

**Controls (guide above consensus)**

| Case | Guide vs consensus | Reaction | Sources |
|---|---|---|---|
| Eaton 2025-01-31 | $12.00 vs $11.95 | "stock up" | Reuters; RTT |
| Schneider 2025-02-20 | margin 19.2–19.5% vs 18.8% | +6.4% | Reuters; MarketScreener |
| Vertiv 2026-02-11 | EPS $5.97–6.07 vs $5.33 | ~+22% | Investing.com/Yahoo; Seeking Alpha; Finimize |
| Quanta 2026-02-19 | $12.65–13.35 vs $12.44 / $12.43 | move not retrieved | Reuters/MarketScreener; FactSet/MarketScreener |
| Siemens Energy 2025-11-13 | FY28 targets raised | "share price takes off" | SE release; dpa-AFX |

**Reading**
- Of 4 strict cases, 3 fell on the day and 1 rose.
- Every above-consensus control rose.
- Only 4 strict cases were verified, against the 8 requested, and none has a verified before/after multiple or 1- and 3-month path. **Treat this as anecdote, not a base rate.**

### Q6. What supports the multiple into January

- **Buyback.** $10.0B authorization; cumulative $7.0B repurchased at 6/30/26, so **$3.0B remains** [computed].
  - Sources: [S1: 10Q2 MD&A chunk 5745] [S2: 10Q1 chunk 13710, $4.6B cumulative at 3/31, so Q2 = $2.3B, consistent].
  - $3.0B is about 1.2% of the $256.3B market cap [computed].
  - Q2 average price ≈ $920 ($2.3B / 2.5M shares) [computed; 10Q2].
  - Cash $13.1B, of which $0.4B restricted; plus a $3.0B revolver [10Q2 chunk 5745; facts.csv cash $13,120M].
  - FY26 FCF guide $11.5–12.5B less H1 $9,897M leaves **$1.6–2.6B implied for H2** [computed; brief §4; 10Q2].
  - Precedent: authorizations were set or raised at both December events ($6B Dec-24, $10B Dec-25), and those days returned +5.01% and +15.62%. The buyback effect cannot be isolated from the framework raises.
- **Backlog-margin update (January) and ≥125 GW:** the prior January days carrying this disclosure were +2.67% and +2.73% (BX-13). The effect is not separable.
- **Spring-2027 CMD with a 2030 outlook:** no precedent CMD since the spin. The December investor updates are the nearest analogue (+5.01%, +15.62%) [D04B; BX-13]. Jefferies expects long-term guidance in March 2027 [R08, **SINGLE-SOURCE**].
- **Street not cutting:** FY27 EPS +0.3% since 07-23. Jefferies ($1,155→$1,185) and Bernstein ($1,206→$1,298) raised targets around GLJ [R08: StreetInsider; Zhitong].
- **Passive ownership:** top-4 holders ≈ 25.6% (BlackRock 8.17%, Vanguard 7.16%, FMR 6.05%, State Street 4.24%) [D05: MarketBeat; Longbridge].
- **AI-capex news** has in-sample been a *negative* shock channel (−21.5%, −10.5%, −6.9%). Positive AI-news days were not studied.

### Q7. What threatens it

- **FCF yield.**
  - FY26 consensus FCF $12,017M = 4.7% of market cap; FY27 $7,417M = **2.9%** [computed; MS **SINGLE-SOURCE** on FCF lines].
  - SAR trailing FCF yield is 4.85% and P/FCF 20.6x.
  - I found **no evidence** that holders anchor on FCF yield. Sell-side targets are EV/EBITDA- and P/E-based (consensus target ≈ 26.3x NTM, D05).
- **Rates and macro.**
  - 10-year 5.24% on 09-28 (5.27% intraday) [D05: FRED; Investing.com].
  - The FOMC date (10-28) and the dates of hyperscaler capex guides were **not verified** in this pass.
- **Peer events.** Siemens Energy holds an "Extended Q4 FY2026 Call" with a medium-term framework on **2026-11-11** [S1: PP-38 SE calendar] [S2: not found]. MHI date not verified.
- **Positioning.**
  - Hedge-fund holders fell 118→106 in Q2 [Insider Monkey, corpus chunk 235412; **SINGLE-SOURCE**].
  - Short interest 3.3% [MarketBeat; SA].
  - Options: IV rank 2 (cheap premium), put/call OI 1.48, 2-day expected move ±3.0% (09-23) [thetaOwl 09-23 and 09-16 snapshots; **SINGLE-SOURCE** publisher].
  - The **implied move through the January report was not found.**
  - Date conflict: TrendSpider shows "Next Earnings Oct 21, 2026" against the brief's 10-28. The company-confirmed date needs checking.

### Q8. Scorecard and break-even table

**Reasons the multiple compresses to ≤25–26x**
1. **Peer gap.** 28.2x vs US peers at ~21x and all peers at 17.7x [MS; TIKR].
2. **Mechanical.** At consensus, a flat price already means 25.1x by late January; the roll itself does it.
3. **In-sample triggers.** A margin-held report day (−8.69% / −12.55% over 5 days), plus AI risk-off days that took the multiple to 24.9x (12-17-25) and 25.4x (09-14-26) [NQ; EnergyWatch; BX-13].
   - Also: the 06-30→09-14 fall was ~all de-rating while estimates rose [CL; R08].

**Reasons it does not**
1. **The floor has risen.** 12-month closing floor ≈ 23.4x; month-ends ≥25.0x; 2026 troughs 25.4–28.5x [CL; NQ reconstruction].
2. **January and event record.** Both January days were positive, and framework or margin raises delivered +13.75% to +15.62% [BX-13; D04B/Barron's].
3. **Street and capital return.** No FY27 cuts; brokers raising targets; $3.0B authorization left, with a December pattern of re-ups [R08; 10Q2].

**Which side has the better evidence (research judgement):**
- The "does not compress" side has more direct, GEV-specific evidence: its own troughs and event days.
- The "compress" side rests on relative value, which has not bound since the spin, plus event risk that is real but undated.
- The short's arithmetic needs ≤~26x at the research FY27 number, which is near the observed 12-month floor band (25–26x).

**Break-even table: January-2027 price**
- Bridge: Price = (m × NTM + $9,113M) / 266.33M. NTM = 11/12·FY27 + 1/12·FY28, with FY28 = FY27 × 1.3645 (the consensus FY28/FY27 ratio), so NTM = FY27 × 1.03038.
- Net cash is held at the 6/30/26 level; each +$1B adds +$3.75/share.

| FY27 EBITDA | NTM | 23x | 25x | 26x | 28x | Break-even multiple |
|---|---|---|---|---|---|---|
| $8.6B | 8,861 | $800 (−16.9%) | $866 (−10.0%) | $899 (−6.6%) | $966 (+0.3%) | 27.9x |
| $8.9B | 9,170 | $826 (−14.2%) | $895 (−7.0%) | $930 (−3.4%) | $998 (+3.7%) | 27.0x |
| $9.3B | 9,583 | $862 (−10.5%) | $934 (−3.0%) | $970 (+0.7%) | $1,042 (+8.2%) | 25.8x |
| $9.6B | 9,892 | $888 (−7.7%) | $963 (0.0%) | $1,000 (+3.9%) | $1,074 (+11.6%) | 25.0x |

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | 52-week high | $1,195.94 intraday on 2026-07-06; close high $1,174.86 on 06-30 | Yahoo meta (BX-40) | Nasdaq (PP-37) | exact | H |
| 2 | Today's NTM EV/EBITDA | 27.7x / 28.2x | CL | MS-computed | close | H |
| 3 | EV/EBITDA troughs | 23.38x (11-04-25), 24.87x (12-17-25), 25.44x (09-14-26) | CL | computed 26.2x on 09-14 (GLJ Street) | close | M |
| 4 | Forward P/E quarter-ends | table in Q1 | SAR | CL | **conflict** at Q4'25 (59.6x vs 42.2x) | M |
| 5 | Event-day closes | Q1–Q2 tables | NQ | BX-01 / SAH | exact | H |
| 6 | 12-17-25 drop | −10.50% (Oracle story) | EnergyWatch | Invezz | exact | H |
| 7 | Buyback left | $3.0B | 10Q2 chunk 5745 | 10Q1 chunk 13710 (arithmetic check) | exact | H |
| 8 | VRT 2025 guide below consensus | $3.55 vs $3.57; ~−10% | Nasdaq/RTT | Investopedia / IBD | close | M |
| 9 | PWR 2025 guide | $10.20 vs $10.22–10.25; +5% | Markets Insider | MarketScreener/Reuters; Zacks | close | M |
| 10 | ETN 2026 guide trails | −6.2% premarket | Seeking Alpha | Grafa | close | M |
| 11 | SE FY26 / FY28 margins | 9–11% / 14–16% | SE presentation (MarketScreener) | SE press release | exact | H |
| 12 | Options positioning | IV rank 2; put/call OI 1.48 | thetaOwl 09-23 | thetaOwl 09-16 (same publisher) | [SINGLE-SOURCE] | L |
| 13 | FY27 EPS drift | +2.5% Jun→Sep | YF (R08) | MS | close | M |

---

## 4. Arithmetic

**A. Late-January bridge**
- NTM(cons) = 11/12 × 9,574 + 1/12 × 13,064 = 9,865.
- Flat-price multiple = (962.49 × 266.33 − 9,113) / NTM = 247,227 / 9,865 = 25.06x.
- Table cells: (m × FY27 × 1.03038 + 9,113) / 266.33. Example: 8.9B at 26x = (26 × 9,170 + 9,113) / 266.33 = $929.5.

**B. Reconstructed month-end multiples**
- CL-implied NTM EBITDA at each anchor: E = (P × 266.33 − 9,113) / m_CL.

| Anchor | Price | CL multiple | Implied E ($M) |
|---|---|---|---|
| 11-04-25 | 547.96 | 23.38x | 5,852 |
| 12-17-25 | 614.19 | 24.87x | 6,211 |
| 04-23-26 | 1,149.53 | 40.39x | 7,354 |
| 06-10-26 | 867.09 | 28.54x | 7,772 |
| 07-29-26 | 900.28 | 27.54x | 8,375 |
| 09-14-26 | 874.76 | 25.44x | 8,800 |
| 09-29-26 | 962.49 | 27.70x | 8,925 |

- E is interpolated linearly between anchors, and held at 5,852 before 11-04. Because E was probably lower before 11-04, the Oct-25 multiples are lower bounds.
- Month-end multiple = (P × 266.33 − 9,113) / E. Example: 08-31, E = 8,375 + 33 × 9.04 = 8,673, giving (898.53 × 266.33 − 9,113) / 8,673 = 26.54x.
- Caveats: today's share count and net cash are applied to all dates, and CL's EV definition is unknown. Error ≈ ±1x.
- Threshold price for 26x at 11-04 = (26 × 5,852 + 9,113) / 266.33 = $605.5.

**C. 09-14 cross-check**
- NTM = 0.296 × 6,359 + 0.704 × 9,450 = 8,535.
- EV = 874.76 × 266.33 − 9,113 = 223,862, so the multiple is 26.2x (CL: 25.44x).

**D. 52-week-high decomposition**
- E at 06-30 = 7,772 + 20 × 12.3 = 8,018; multiple = 303,788 / 8,018 = 37.9x.
- ln(8,800 / 8,018) = +0.093; ln(25.44 / 37.9) = −0.399; sum −0.306 vs ln(223,862 / 303,788) = −0.305. Ties.

**E. Other**
- Buyback remaining: 10.0 − 7.0 = $3.0B; 3.0 / 256.3 = 1.17%.
- FY27 FCF yield: 7,417 / 256,340 = 2.9%.
- Siemens Energy multiple ratio: 28.2 / 12.6 = 2.24; growth ratio: 43.3 / 36 = 1.20.
- Event returns, e.g. Jan-26 20-day: 876.01 / 692.70 − 1 = +26.46%.

---

## 5. General question bank

- **G5.** If the stock is flat to late January, the multiple becomes 25.1x at consensus; to Sep-27, 20.3x (§4-A; D05).
- **G15.** GEV's own de-ratings are fast: 40.4x→28.5x in 7 weeks (Apr→Jun-26); 37.9x→25.4x in 11 weeks (CL).
- **G16.** The dominant de-rating channel in-sample is AI-capex news, not rates (Q1–Q2, D05 §Q6).
- **G20.** Every historical EV/EBITDA number is single-vendor, and P/E vendors conflict by up to 17 turns on the same date.
- **G21.** If the short is wrong, the pattern would be the Jan-26 one: a January print, then a +26% 20-day drift.

## 6. What would change these findings

- **Floor and percentiles:** a point-in-time EV/EBITDA history (FactSet or Bloomberg) showing late-2025 troughs well below 23x would lower the floor. If it showed the Jan-26 dip above 26x, the "≤26x episodes" list shrinks.
- **Reference class:** verified 1- and 3-month paths for VRT-25, ETN-26 and PWR-25. If all recovered within a month, the "guide below consensus = de-rating" reading weakens.
- **Break-even table:** a December-2026 authorization re-up, or a larger H2 cash build, raises every cell by about $3.75 per $1B.

## 7. Disagreements with the master brief

1. The brief's premise that "the short loses ~3% if the multiple holds" is right only at 28x. The relevant break-even at FY27 $8.6–8.9B is **27.0–27.9x**, and at consensus it is 25.1x (§4-A).
2. "52-week range $530.16–$1,195.94" is intraday. On closes it is $547.96 (2025-11-04) to $1,174.86 (2026-06-30), as already flagged in prior work.
3. The earnings date may be in conflict (TrendSpider shows 10-21 vs the brief's 10-28). Verify on the GEV IR site.

## 8. Open items

- Point-in-time NTM EV/EBITDA history from a second vendor (YCharts is paywalled; Koyfin or Bloomberg are options). The 24-month percentile needs it.
- 5- and 20-day moves for the 2024 to mid-2025 events. Pull the Nasdaq API in windows of 60 rows or fewer, with `limit=700` and month-boundary dates.
- Reference class: 1- and 3-month moves and before/after multiples for VRT-25, PWR-25, ANET-25 and ETN-26; more cases to reach 8 (Hubbell, Rockwell FY25, Siemens Energy FY25, Rolls-Royce).
- Hitachi and Baker Hughes multiples.
- FOMC and hyperscaler dates; MHI November date; January implied move from the options chain.
- Pre-Dec-2025 FY27 consensus, to split the December estimate and multiple effects.
