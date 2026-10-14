# Horizon decision: short into January vs long over 12 months (expected value)

_E02_horizon_trade — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:17:39. Requests 14, input tokens 843417, output tokens 29878._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV pitch decision table: four candidate pitches (short into January, long 12 months, short 12 months, long into January)

*Research input only. Every probability is research judgement, every scenario EBITDA path is a research estimate, and the team picks its own numbers and writes every memo sentence.*

**Source key**
- **Q2REL** = 8-K 0001996810-26-000147 EX-99 (2026-07-22)
- **10Q** = 10-Q 0001996810-26-000148
- **Q4REL** = 8-K 0001996810-26-000012
- **DEC25** = Dec-2025 investor-update release
- **CFO-8K** = 8-K 0001996810-26-000153 Item 5.02
- **CFO-PR** = GEV CFO-transition release 2026-08-27
- **CFOD** = CFO Dive 2026-08-28
- **LAG-PDF** = GEV-hosted Laguna transcript 2026-09-16
- **LAG-SA** = stockanalysis.com Laguna transcript
- **MB** = MarketBeat Laguna write-up 2026-09-18
- **MS** = MarketScreener, fetched 2026-09-29
- **GF** = GuruFocus/Yahoo GLJ wire 2026-09-14/15
- **CL** = Chartloom NTM series
- **BX** = Yahoo chart API + Nasdaq closes (facts BX-01..13)
- **YF** = FinRobot yfinance quote, 2026-09-30 07:12 UTC
- **KAL** = Kalkine 2026-09-29
- **IR** = gevernova.com/investors/events (facts PP-01)
- D0x / V0x = tonight's outputs

---

## 1. Bottom line

- **Best evidence-backed reward/risk is (a), the short into the January guide, but the edge is thin and depends on the multiple.**
  - Central expected return is about **+4.3%** for the short. Across four multiple frames it runs from −0.6% to +12.1%.
  - Probability-weighted gain/loss is about **2.3x** in the central frame and 0.9x in the "sticky multiple" frame.
  - Worst plausible loss is about −23% ($1,181).
  - [computed §4-A; probabilities from D04A and D04B guide distributions; consensus S1 MS, S2 GF "Street $9.45B"]
- **The 12-month pitches are close to a coin-flip in expected value.**
  - (b) long: about **+1.8%** expected, P(up) ≈ 55%, worst about −33%.
  - (c) short: the mirror image, with a worst case of about +39% against it.
  - One turn of NTM multiple (~$43/share) or 5 points of probability moved from bull to bear flips the sign. [computed §4-B; bridge S1 10Q balance sheet, S2 stockanalysis EV $247.34B]
- **(d) the long into January has the worst expected value.** Central about −4.3%, worst about −29% ($687). It bets against the ~80–85% research probability that the FY27 margin midpoint lands below 18.15%. [S1: D04A; S2: D04B]
- **The price flat-lines only if the multiple compresses.**
  - To leave $962.49 unchanged by late January on unchanged consensus, NTM EV/EBITDA must fall from 28.2x to **25.1x**.
  - By Sep-2027 it must fall to **20.3x**.
  - A January short therefore needs a cut to FY27 that the market does not look through; it does not need a crash. [computed §4-A0; consensus S1 MS, S2 GF; multiple S1 MS-computed, S2 CL 27.7x]
- **Easiest to defend with Citadel PMs, in research ranking: (a) > (b) > (c) > (d).**
  - (a) is the only pitch where the model's one number, the dated event and the kill rule all point the same way.
  - Its weakest step, the de-rating, is exactly what PMs attack: about $100–110/share of typical short targets comes from a multiple cut [S1: V10 A4; S2: V04 A3 via D10 §1].
- **Q3'26 (2026-10-28) falls between the finals (10-23) and the January guide.**
  - A clean Q3 beat, modelled here as moving 15 points of probability toward the in-line and bull cases, cuts (a)'s expected value from +4.3% to about **+0.8%** from the original entry.
  - The team needs an explicit answer for this. [date S1: IR; S2: KAL]

---

## 2. Answers

### Q1. Scenarios, probabilities, prices, expected return and worst case

**Method.** Value = (m × NTM EBITDA + $9,113M) / 266.33M [bridge S1: 10Q balance sheet; S2: brief §7 / evidence_brief §C].
- January frame (late Jan-2027): NTM = 11/12 × FY27 + 1/12 × FY28 (the D10 convention).
- Sep-2027 frame: NTM = 0.25 × FY27 + 0.75 × FY28.
- Consensus inputs: FY27 $9,574M and FY28 $13,064M [S1: MS; S2: GF $9,450M for FY27; Motley Fool 60% CAGR → ~$13,091M for FY28 (D10 Q8)].
- Consensus FY27 revenue: $52,740M [S1: MS; S2: S&P/stockanalysis $52.74B].

#### January-horizon scenarios (used by pitches a and d)

The scenarios follow the FY27 margin-guide midpoint. The probabilities combine D04A's distribution (≥18.5%: 13%; 18.0%: 17%; 17.0–17.5%: 34%; ≤16.5%: 36%) with D04B's (P(<18.15%) ≈ 80%; P(≤17.5%) ≈ 65–70%), shaded to allow Q3 and backlog-page offsets.

| # | January outcome | P | FY27 / FY28 EBITDA after reset ($M) | NTM Jan ($M) | Multiple: central (sticky / harsh) | Price, central | vs $962.49 |
|---|---|---|---|---|---|---|---|
| J1 | Guide ≥18.5% midpoint (low end ≥18%), strong backlog page | 14% | 9,900 / 13,300 | 10,183 | 28x (29x / 27x) | **$1,105** ($1,143 / $1,067) | +14.8% |
| J2 | In line: 17–19% range, midpoint 18.0% | 20% | 9,493 / 12,800 | 9,769 | 27x (28.2x / 25x) | **$1,025** ($1,069 / $951) | +6.4% |
| J3 | Modest miss: midpoint 17.0–17.5% | 34% | 9,098 / 12,300 | 9,365 | 25x (26x / 23x) | **$913** ($948 / $843) | −5.1% |
| J4 | Large miss: midpoint ≤16.5% | 32% | 8,438 / 11,500 | 8,693 | 23x (25x / 20x) | **$785** ($850 / $687) | −18.4% |

Why the multiples look like this:
- The central multiples roughly equal "the market holds ~25.8x on FY27 and gives little FY28 roll credit inside four months".
- A constant 25.8x FY27 frame gives $993 / $954 / $916 / $852.
- The 2026 NTM EV/EBITDA troughs were 28.5x, 27.5x and 25.4x (the last on the GLJ day) [S1: CL via D05 Q1; S2: MS-computed 28.2x today].
- The one-day reaction ranges come from D04A Q9 and D04B §1: −6% to −12% for a guide at or below 17%, and −3% to +4% for an 18% guide.

**(a) Short into January (entry $962.49)**

| Multiple frame | E[price] | Short expected return | Probability-weighted gain / loss |
|---|---|---|---|
| Central | $921 | **+4.3%** | $73.6 / $32.3 = **2.28x** |
| Sticky NTM (roll credit) | $968 | −0.6% | 0.88x |
| Constant 25.8x FY27 | $914 | +5.1% | — |
| Harsh | $846 | +12.1% | ~9x |

- Worst plausible: J1 at 30x = **$1,181 (−22.7% to the short)**. The record close is $1,174.86 [S1: BX-08; S2: D08]; the intraday high is $1,195.94.
- Reward/risk (expected return ÷ worst loss) ≈ **0.19** in the central frame.

**(d) Long into January**
- Expected return is the negative of (a): central **−4.3%**; −5.1% to +0.6% across frames excluding the harsh one.
- Worst plausible: J4 at 20x = **$687 (−28.6%)**, in line with the median post-spin drawdown of −24.6% [S1: BX-07; S2: Nasdaq closes].
- Reward/risk is negative.

#### Sep-2027 scenarios (used by pitches b and c)

| # | 12-month outcome | P | FY27 / FY28 ($M) | NTM Sep-27 ($M) | Multiple | Price | vs today |
|---|---|---|---|---|---|---|---|
| T1 | Guide ≥18% and/or the spring CMD raises 2028 toward ~$13B | 25% | 9,700 / 13,300 | 12,400 | 25x (close to the consensus target's 26.3x) | **$1,198** | +24.5% |
| T2 | Consensus roughly holds (small trims) | 30% | 9,300 / 12,800 | 11,925 | 22x | **$1,019** | +5.9% |
| T3 | Management-plan path (V10 medians) | 30% | 8,800 / 11,500 | 10,825 | 21x | **$888** | −7.8% |
| T4 | Cut plus de-rating (AI-capex scare or order second derivative) | 15% | 8,300 / 10,800 | 10,175 | 18x | **$722** | −25.0% |

Basis for the probabilities:
- T1: P(guide ≥18%) ≈ 30% [D04A/B], and P(2028 raised toward ~$13B at the CMD) ≈ 40–50% [D02 via D10]; jointly with the multiple holding, research judgement gives 25%.
- T4: anchored on five ≥15% drawdowns since the spin (median −24.6%) [S1: BX-03..08; S2: Nasdaq].
- P(up) = 55%, consistent with V08's 12-month ~0.57 and V10's ~0.51 [S1: V10 §1; S2: V08 A8].
- Multiples are from D05's anchors: consensus holds 22–28x, a 5–10% cut 20–25x, a 10–15% cut 16–22x.

**(b) Long 12 months**
- E[price] $980 → **+1.8%**. Probability-weighted gain/loss 1.30x.
- Worst plausible: T4 at 16x = **$646 (−32.9%)**. The maximum historical drawdown is −38.3% [S1: BX-03; S2: Nasdaq].
- Reward/risk ≈ 0.06.

**(c) Short 12 months**
- **−1.8%** expected. Gain/loss 0.77x.
- Worst plausible: T1 at 28x = **$1,338 (−39% to the short)**. Consensus at a constant 28.2x gives $1,325 (the +39% NTM roll).
- Reward/risk is negative.

### Q2. Dated events inside each horizon, and which way they push

| Date | Event | Direction / what to watch | S1 | S2 |
|---|---|---|---|---|
| 2026-10-23 | Finals (before any GEV print) | Judges see no new GEV data | brief §1 | IR (Q3 on 10-28) |
| 2026-10-28, 7:30 ET | Q3'26 + 10-Q | Two-way. Consensus EBITDA $1,706M (MS) / $1,728M (ChartMill). The past two Q3s only reaffirmed (+1.25%, −1.59%). The CEO pre-signalled "very strong" orders. The 10-Q updates RPO conversion percentages, buyback and Vineyard Wind. | IR; KAL | D07 (MS, ChartMill); LAG-PDF / MB |
| 2026-11-01 | McDonough joins as advisor | Neutral | CFO-8K | CFO-PR |
| YE2026 | Gas backlog + SRAs ≥125 GW (116 GW at Q2) | Long if met; CEO says H2 commitments "~20 GW… likely conservative" | Q2REL | LAG-PDF p.3 / LAG-SA |
| Dec-2026 | No investor event listed; past Decembers brought framework raises (+5.01%, +15.62%) | Absence is short-leaning; a surprise event is long | IR (BR-44) | D04A Q1 (Proactive / Reuters) |
| Late Jan-2027 (not yet announced; prior years 01-22, 01-28) | Q4 + **FY27 outlook** + 2026 backlog-margin change + likely CMD date | **Decisive for (a)/(d).** Short needs a midpoint ≤17.0–17.5%; long needs a low end ≥18%. Backlog page benchmarks: Power >+11 pts; ≥$8B margin added. | LAG-PDF p.10–11 | MB; LAG-SA |
| Late Jan-2027 | Presenter is Parks, not McDonough | Weakens any "new-CFO reset" leg | CFO-PR | CFOD |
| 2027-04-02 | Parks retires | Neutral | CFO-8K | Reuters (D03) |
| Late Apr-2027 | Q1'27 (Q1'26 raised the margin guide, +13.75%) | Long-skewed on precedent | BX-13 | TIKR 2026-04-23 (D07) |
| Spring 2027 | CMD with 2030 outlook | Long-skewed; a 2028 raise to ≥~$12.5B is a short kill | LAG-PDF p.11 | GuruFocus src:686 |
| Late Jul-2027 | Q2'27 | Two-way; the Q2'26 raise without a margin raise went −8.69% | BX-13 | stockanalysis (07-22) |
| Continuous | 10-year at 5.24% (highest since 2007); AI-capex sentiment (DeepSeek −21.5%; 09-14 −8.6%) | Multiple risk both ways | FRED / Investing.com (D05) | Motley Fool; BX-04 |

Two caveats:
- The earnings-day return series outside 07-22 is a single dataset (BX-13) [SINGLE-SOURCE].
- Hyperscaler capex-guide dates inside the window were **not researched** (open item).

### Q3. Reward/risk ranking and how sensitive it is

Ranking by central expected return:
1. **(a)** +4.3%
2. **(b)** +1.8%
3. **(c)** −1.8%
4. **(d)** −4.3%

Sensitivity of (a):
- Moving 12.9 points of probability from J4 to J1 (P(J1) ≈ 27%, P(J4) ≈ 19%) brings the expected return to zero.
- So does moving 17 points from J4 to J2.
- Switching from the central to the sticky-multiple frame (+1–2 turns per scenario) gives −0.6%. One turn on a ~9.4B NTM is about $35/share (3.7%).
- Conclusion: (a) survives moderate probability error but **not** a market that keeps paying 28x NTM through January.

Sensitivity of (b)/(c):
- ±1 turn on the probability-weighted NTM of $11,451M is about ±$43 (±4.5%). That is larger than the +1.8% expected return.
- Moving 5 points from T1 to T4 gives −0.7%.
- The 12-month sign is **not robust**. This matches D10 ("no edge at 12 months") and V10 (median p_long 0.46; horizon sorts direction).

Robust across frames:
- (a) weakly dominates (d) in every frame except the sticky one.
- (b) vs (c) is undetermined.
- (a) vs (b) depends on whether the team believes the multiple compresses before January.

### Q4. Short into January: target, stop/kill, and a Q3 beat

**Target (research range, team's choice).**
- Probability-weighted value given a miss: (0.34 × $913 + 0.32 × $785) / 0.66 ≈ **$851 (−11.6%)**.
- Range $785–913. At the harsh multiples: $687–843.

**Kill (event-based).** Any one of:
- FY27 guide low end ≥18%.
- 2028 framework raised to ≥~$12.5B.
- 2026 Power backlog-margin change well above +11 points **together with** a guide at or above 18%.

Sources: [S1: D10 Q6 kill table; S2: V10 R9/R13, where 9 of 9 variants agree on ≥18%].

**Stop (price-based, research options).**
- **$1,079 (+12.1%)**: consensus rolled at a constant 28.2x. If the stock trades there before January, the market is paying the roll with no de-rating, which is the short's mechanism failing.
- Wider: $1,175 (record close) or $1,181 (J1 at 30x).
- Unweighted payoff at the $851 target and $1,079 stop: +11.6% vs −12.1%, i.e. about 1:1. Taking the edge from probabilities (P(J3+J4) = 66%) is legitimate only if the team defends the 25.1x flat-price multiple.

**If Q3 beats on 10-28.**
- Definition used here: EBITDA well above $1,728M, Power ≥19%, Wind ≥ breakeven.
- Mechanism: a higher FY26 exit shrinks the step to 18.15%. D04A §6 flags that FY26 ≥14% with Q4 ≥17% makes +4 points "consistent with history".
- Research shift: 10 points from J4 to J2 and 5 from J3 to J1, giving 19 / 30 / 29 / 22.
- Result: E[January price] ≈ **$955**, i.e. about **+0.8%** to a short from $962.49, with the edge almost gone.
- If the stock also jumps (Q1'26 analogue: +13.75% when the margin guide was raised), the mark-to-market loss is realised before the guide.
- A Q3 print that only reaffirms (the past two Q3s: +1.25%, −1.59%) leaves the table roughly intact.
- The Q3 call may also "frame" 2027 early (as in Oct-2025, D04A G14). That shrinks the January surprise either way. A cautious framing on 10-28 would move part of the short's payoff into October.

### Q5. Fit to the 3–12-month horizon and "model and thesis alignment"

**(a)** Fits at about 4 months, the low end of the window.
- Alignment is the strongest of the four: the model's one number (FY27 adjusted EBITDA margin, research base $8.6–8.9B, −8% to −10% vs $9,574M) is tested by a dated company event with a pass mark and a kill rule [S1: D10 §1; S2: V10 Q4].
- The model must value on a January NTM (11/12 FY27 + 1/12 FY28) and state the multiple assumption. The playbook says to "Match the valuation date to the judging horizon" [S1: winners_playbook Step 10; S2: LSPD case, "the variance does not fit the horizon"].

**(b)** Fits at 12 months.
- The research's own FY27 is below consensus, so a long must rest on the roll-forward and the multiple. That is a multiple bet on consensus numbers, the Valvoline pattern [S1: brief §9; S2: V06 "no view that differs from the Street"].

**(c)** Fits at 12 months, but alignment is weakest.
- An about −8% estimate gap cannot beat a +39% roll unless the multiple falls to about 20x.
- The Deere winner lost exactly this way: earnings fell further than forecast, yet the stock rose on a higher multiple [S1: pitch corpus michigan-uic-2023-de; S2: winners playbook].

**(d)** Contradicts the research's own guide distribution. Not aligned.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Price | $962.49 (close 9/29) | YF 2026-09-30 | Zacks/Yahoo 9/29 (D08) | exact | H |
| 2 | Net cash bridge | $9,113M (13,120 − 2,849 − 1,158) | 10Q balance sheet | stockanalysis EV $247.34B (implied) | close; NCI filing-only | H/M |
| 3 | Shares outstanding | 266.33M | 10Q balance sheet | MS 266,334K | exact | H |
| 4 | FY27 consensus EBITDA | $9,574M | MS | GF "Street $9,450M" | close (1.3%) | M |
| 5 | FY28 consensus EBITDA | $13,064M | MS | Motley Fool CAGR → ~$13,091M | close | M |
| 6 | FY27 consensus revenue | $52,740M | MS | S&P/stockanalysis $52.74B | exact | H |
| 7 | NTM EV/EBITDA today | 28.2x / 27.7x | MS-computed | CL | close | M |
| 8 | 2026 NTM troughs | 28.5x, 27.5x, 25.4x | CL (D05) | — | SINGLE-SOURCE (P/E cross-checked vs Yahoo/TIKR) | M |
| 9 | P(FY27 midpoint < 18.15%) | ~85% / ~80% | D04A | D04B | close (same model; weak independence) | M |
| 10 | Parks presents the Q4 call | "inclusive of third and fourth quarter" | CFO-PR | CFOD | exact | H |
| 11 | FY27 outlook on the January call | "We'll also provide you a '27 financial outlook" | LAG-PDF p.10–11 | MB 2026-09-18 | exact | H |
| 12 | Q3 date | 2026-10-28, 7:30 EDT | IR (PP-01) | KAL 2026-09-29 | exact | H |
| 13 | Q3 EBITDA consensus | $1,706M / $1,728M | MS | ChartMill | close | M |
| 14 | Earnings-day moves | 10 days, mean +2.48%, mean absolute 5.42% | BX-13 | stockanalysis (07-22 only) | partial | M |
| 15 | Drawdowns ≥15% | 5; median −24.6%; max −38.3% | Yahoo chart API | Nasdaq closes | exact | H |
| 16 | Record close / intraday high | $1,174.86 / $1,195.94 | BX-08 | D08 | exact | H |
| 17 | 2028 framework | $56B, 20%, $11.2B | Q4REL | DEC25 / Prolec news src:3806 | exact | H |
| 18 | CMD spring 2027 with 2030 outlook | — | LAG-PDF p.11 | GuruFocus src:686 | exact | M |
| 19 | 12-month p_long | ~0.51 median; V08 0.57 | V10 §1 | V08 A8 | close (same model) | L/M |
| 20 | December events drove the first-guide days | +5.01%, +15.62% | BX / BR-38 | Proactive / Reuters (D04A) | close | H |
| 21 | Deere short lost on multiple expansion | — | pitch corpus DE outcome | winners playbook | exact | M |

---

## 4. Arithmetic

**A0. Flat-price multiples.**
- EV = 962.49 × 266.33 − 9,113 = 256,340 − 9,113 = $247,227M.
- January consensus NTM = 11/12 × 9,574 + 1/12 × 13,064 = 8,776.2 + 1,088.7 = $9,865M → 247,227 / 9,865 = **25.06x**.
- At a constant 28.2x: (28.2 × 9,865 + 9,113) / 266.33 = **$1,079**.
- Sep-2027 consensus NTM = 0.25 × 9,574 + 0.75 × 13,064 = $12,191M → **20.3x** holds the price.

**A1. January scenarios.** Price = (m × NTM + 9,113) / 266.33.
- J1: NTM 9,075 + 1,108.3 = 10,183.3 → 28x $1,104.8 | 29x $1,143.0 | 27x $1,066.6 | 30x $1,181.3 | 25.8x on FY27 $993.3.
- J2: FY27 = 18.0% × 52,740 = 9,493; NTM 8,701.9 + 1,066.7 = 9,768.6 → 27x $1,024.5 | 28.2x $1,068.5 | 25x $951.2 | 25.8x FY27 $953.8.
- J3: FY27 = 17.25% × 52,740 = 9,098; NTM 8,339.8 + 1,025 = 9,364.8 → 25x $913.3 | 26x $948.4 | 23x $842.9 | 25.8x FY27 $915.6.
- J4: FY27 = 16.0% × 52,740 = 8,438; NTM 7,734.8 + 958.3 = 8,693.2 → 23x $784.9 | 25x $850.2 | 20x $687.0 | 25.8x FY27 $851.6.
- FY28 resets (13,300 / 12,800 / 12,300 / 11,500) are research estimates, team's choice.

**A2. January expected values.**
- Central: 0.14 × 1,104.8 + 0.20 × 1,024.5 + 0.34 × 913.3 + 0.32 × 784.9 = 154.7 + 204.9 + 310.5 + 251.2 = **$921.3 (−4.28%)**.
- Sticky: 160.0 + 213.7 + 322.5 + 272.1 = **$968.2 (+0.60%)**.
- Constant 25.8x FY27: 139.1 + 190.8 + 311.3 + 272.5 = **$913.6 (−5.1%)**.
- Harsh: 149.3 + 190.2 + 286.6 + 219.8 = **$846.0 (−12.1%)**.

**A3. Short gain/loss, central frame.**
- Losses: 0.14 × 142.3 + 0.20 × 62.0 = 32.3.
- Gains: 0.34 × 49.2 + 0.32 × 177.6 = 73.6.
- Ratio 2.28. Sticky frame: 40.7 / 46.5 = 0.88.

**A4. Breakeven probability shifts.**
- J4 → J1: 41.2 / (1,104.8 − 784.9) = 12.9 points.
- J4 → J2: 41.2 / 239.6 = 17.2 points.

**A5. After a Q3 beat.** 0.19 × 1,104.8 + 0.30 × 1,024.5 + 0.29 × 913.3 + 0.22 × 784.9 = 209.9 + 307.4 + 264.9 + 172.7 = **$954.8**.

**A6. Short target.** (0.34 × 913.3 + 0.32 × 784.9) / 0.66 = **$851.0**.

**B1. Sep-2027 scenarios.**
- T1: NTM 2,425 + 9,975 = 12,400 → 25x $1,198.2; 28x $1,337.9.
- T2: 2,325 + 9,600 = 11,925 → 22x $1,019.3.
- T3: 2,200 + 8,625 = 10,825 → 21x $887.8; at 23x $969.1 (≈ today).
- T4: 2,075 + 8,100 = 10,175 → 18x $721.9; 16x $645.5.
- Consensus at 28.2x: (28.2 × 12,191 + 9,113) / 266.33 = $1,325.

**B2. 12-month expected value.**
- 0.25 × 1,198.2 + 0.30 × 1,019.3 + 0.30 × 887.8 + 0.15 × 721.9 = 299.6 + 305.8 + 266.3 + 108.3 = **$980.0 (+1.82%)**.
- Long gain/loss: 75.97 / 58.50 = 1.30.
- One turn = 11,451 / 266.33 = $43.0.
- Moving 5 points from T1 to T4: −0.05 × 476.3 = −$23.8 → $956.2.

---

## 5. General question bank answers

- **G1 / G5:** The price holds only if NTM EV/EBITDA falls to 25.1x by January or 20.3x by Sep-2027 on unchanged consensus (A0). If the stock goes nowhere for 12 months, either estimates held and the multiple fell about 28%, or estimates were cut about 12.5% and the multiple fell to about 23x [S1: D05 §1; S2: D03 §1].
- **G8 / G23:** An estimate gap of about −8% is worth about $60–90/share. The roll-forward is worth about +$218/share over Jan→Sep at 25x. The short's upside beyond the gap is a multiple assumption [S1: D10 §1; S2: V10 A4].
- **G13 / G18:** The late-January guide is the test. The short passes at a midpoint ≤17.0–17.5% and is killed by a low end ≥18% or a 2028 raise to ≥~$12.5B [S1: D10 Q6; S2: V10 R9].
- **G14:** Q3 framing on 10-28, a surprise December event, or the January date slipping into February could each move or shrink the reveal [S1: D04A G14; S2: IR, no December event].
- **G15:** Worst plausible outcomes: −23% (Jan short) to −39% (12-month short); −29% (Jan long) to −33% (12-month long). History: median drawdown −24.6%, maximum −38.3% [S1: BX; S2: Nasdaq].

---

## 6. What would change this

- **(a) ranked first:**
  - The stock trading above ~$1,079 before January (the market paying the roll).
  - A Q3 beat accompanied by an FY26 margin-guide raise.
  - A December 2026 event being announced.
  - D04-type guide probabilities proving too bearish (for example, sell-side previews pointing to 18–19%).
- **12-month coin-flip:**
  - Evidence the multiple is sticky, for example a peer re-rating toward GEV's level. Current peers are about 21x US / 17.7x all-eight [D05].
  - The CMD date and content becoming known.
- **Q3-beat math:** my 15-point shift is research judgement. A larger shift (for example to 25 / 30 / 27 / 18) makes (a)'s expected value negative.

## 7. Disagreements with the master brief

1. **"First FY27 guide under the new CFO."** Parks presents the call [CFO-PR; CFOD]. Drop that leg.
2. **"Modest short, 55–60%."** This holds only for a horizon ending shortly after January, where it is about 55%, and the expected edge exists only if the multiple compresses below 25.1x. At 12 months there is no edge.
3. **Brief §7 "value today" formula.** It uses FY27 EBITDA. For a January target, the NTM should be 11/12 FY27 + 1/12 FY28. The difference is about +$30/share on consensus, since 9,865 vs 9,574 is worth 291 × m / 266.33.
4. **"Never cut."** Qualify it: Wind was cut, and the FY24 margin midpoint was narrowed down 25bp [D04A §7].
5. **$530.16 is an intraday low.** The closing low was $547.96 [evidence_brief].

## 8. Open items

- **Short borrow cost and GEV dividend carry:** not researched. Expected returns above are gross. Check a prime-broker or IBKR borrow rate; short interest is ~3.3%, which suggests general-collateral borrow, but that is unverified.
- **January earnings date:** not announced. Watch GEV IR.
- **Options-implied move** for the January and October expiries: not available through these tools. Use a university terminal.
- **Hyperscaler capex-guide dates** (late Oct / late Jan) as multiple catalysts: not researched.
- **Second vendor for FY27/FY28 EBITDA consensus** (FactSet, Bloomberg or Visible Alpha): every scenario rests on MS.
- **CL NTM EV/EBITDA trough series** is single-source.
- **Scenario probabilities** come from one model family (D04A/B, V01–V09 share the same model and corpus). Treat them as structured judgement, not independent estimates. The team should set its own and rerun §4 with the same formulas.
