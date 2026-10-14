# Red-team the refined thesis and the robustness pack

_S06_redteam_robustness — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 10:42:12. Requests 37, input tokens 2733991, output tokens 29548._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV refined short thesis: last-check audit (research input only; the team writes every sentence and picks every number)

## 1. Bottom line

- **Every number in the premium-to-plan ladder is arithmetically correct. The framing "consensus above management at every horizon" does not hold at the two near rungs.**
  - At Q3'26, consensus of $1,706M sits *inside* a range the research rebuilt from segment guides ($1,535–1,716M). Management gave no company-level Q3 number.
  - At FY26, consensus ($6,359M / $6,394M) sits inside the guided dollar range ($5,460–6,510M). It is only +3.2% to +3.8% above the sum of management's own **segment**-guide midpoints (~$6,162M) [computed §4-A]. So management's 12–14% company margin guide sits *below* its own segment guides.
  - Sources: [S1: Q2'26 release 0001996810-26-000147 guidance section] [S2: Q2'26 call transcript, corpus chunks 251602/251604/251606/251607]
- **The FY27 rung compares consensus with a research construct, not a management number.** The $8,590M straight line is the *highest* of four reasonable ways to interpolate from FY26 to 2028 ($8,184–8,681M) [computed §4-B]. So the +8.7% to +11.5% premium is, if anything, understated. But the team cannot call $8,590M "management's number": no FY27 guidance exists.
  - Sources: [S1: Q4'25 release -26-000012, "outlook by 2028… $56 billion… 20%"] [S2: Laguna recap, MarketBeat 2026-09-18, corpus 223197: "2027 financial outlook… during its January earnings call"]
- **The strongest attack is a precedent: the ladder pattern has existed before, and it resolved in the longs' favour.**
  - Dec-2024: JPMorgan wrote that GEV's FY25 guide and its raised long-term targets were both "slightly below consensus".
  - Twelve months later (Dec-2025), management moved the 2028 margin from 14% to 20%. Morningstar said that "surpassed our and the market's expectations".
  - The stock went from $327.79 at YE24 to $653.57 at YE25.
  - Sources: [S1: TipRanks/Markets Insider 2024-12-11] [S2: Yahoo Finance 2024-12-14 (same JPM note, so same originator)] [S3: Morningstar 2025-12-10] [prices: S04 table, from Nasdaq and stockanalysis]
- **The multiple leg is the binding constraint.**
  - At today's price, the late-January NTM consensus already equals 25.1x.
  - On the research FY27 path ($8.6–8.9B), the break-even multiple is 27–28x.
  - The month-end multiple has not closed below ~25x in 12 months. This rests on one vendor (Chartloom) and is a reconstruction.
  - Sources: [S1: S04 §1 (CL, NQ)] [S2: ROBUSTNESS_PACK T8, recomputed §4-D]
- **Signs the raise cycle is slowing are real but small:**
  - the FY26 margin guide was held in July;
  - Q2 adj EBITDA was about $1.25B, below LSEG estimates;
  - FY27 EPS revisions went +11.0% (Jan–Apr), then +6.5% (Apr–Jul), then +0.3% (Jul–Sep);
  - Mizuho cut FY27 from $9.4B to $9.3B.
  - Against that, Mizuho *raised* FY28 from $12.8B to $13.0B, and no major broker cut after GLJ.
  - Sources: [S1: Q2REL "remains 12%-14%"; R08 §1 (FactSet via cnyes, then MarketScreener)] [S2: Reuters 2026-07-22 via R08; Investing.com Mizuho 2026-09-30 via S02 (SINGLE-SOURCE for the estimates)]
- **"Largest premium in its peer group" holds only as stated for the chosen eight names.**
  - Growth-adjusted, GEV (0.65) is priced like Vertiv (0.64).
  - Bloom Energy, the closest AI-power name, trades far above GEV: ~446x TTM EV/EBITDA and ~20x EV/Sales [SINGLE-SOURCE: EveryTicker 2026-09-05].
  - The peer multiples themselves are mostly MarketScreener-only.
  - Sources: [S1: S04 §1 item 4] [S2: D05 §Q2]

---

## 2. Answers

### Q1. The ladder and the peer table, re-opened

| Rung / item | Pack value | Primary check | Verdict |
|---|---|---|---|
| Q3'26 management number | $1,535–1,716M "rebuilt from segment guides" | Management gave company Q3 only as "continued year-over-year revenue growth and adjusted EBITDA margin expansion" (Q3'25: 8.1%). The segment inputs are verified: Power revenue +17–19%, margin "approximately 17% to 18%"; Electrification $3.8–4.0B, margin "modestly above 2Q" (18.4%); Wind "approximately break-even". My rebuild gives ~$1,533M low and ~$1,676M high with Electrification ≤19%; the top of $1,716M needs a higher Electrification margin or positive Wind [§4-C] | **MISLEADING.** The arithmetic is fine, but it is a research rebuild, not a management number. The top end depends on assumptions |
| Q3 consensus | $1,706M, +5.0% vs midpoint | MarketScreener $1,706M; ChartMill $1,728M (its history is on a different basis). $1,706M is 0.6% *below* the rebuilt top | **CORRECT number, MISLEADING framing.** It sits inside the range, not above management |
| H2'26 | 3,834 vs MS 4,241 (+10.6%) | 5,980 − H1 2,146 = 3,834 ✓. MS 4,241 = MS Q3 1,706 + Q4 2,535 (the quarterly sum). The annual figure less H1 gives 6,359 − 2,146 = 4,213 (+9.9%) | **CLOSE.** MS quarters and annual do not tie (S02) |
| FY26 management number | $5,980M | $46.0B × 13% ✓ | **CORRECT** |
| FY26 consensus | $6,359M MS / $6,394M FactSet (Boursorama) | Both confirmed in S02 | **CORRECT number, MISLEADING framing.** It is inside the guided range ($5,460–6,510M) and only +3.2–3.8% above the segment-guide sum of ~$6,162M |
| FY27 management number | $8,590M "straight line" | (5,980 + 11,200) / 2 = 8,590 ✓. Other interpolations give 8,184 (geometric), 8,415 (revenue and margin interpolated separately) and 8,681 (from the segment-sum base) | **MISLEADING as a label.** It is not guidance; it is the top end of the interpolation choices |
| FY27 consensus | $9,574M / $9,339M | The vendor band is $9.34–9.65B. Mizuho is at $9.3B | **CORRECT.** Present it as a band |
| FY28 management number | $11,200M | "$56 billion… adjusted EBITDA margin of 20%", "by 2028" | **CORRECT.** "By 2028" is the wording. Morningstar paraphrased the Dec-25 margin as "at least 20%"; the primary release says 20% |
| FY28 consensus | $13,064M, +16.6% | MS $13,064M; ChartMill $13,184M; Mizuho $13.0B | **CORRECT number, MISLEADING without context.** The revenue anchor is stale: the FY26 revenue guide is +$1.5B since the framework was set, and that alone explains about a quarter of the premium (§4-E) |
| Peer NTM EV/EBITDA (Quanta 22.0x … Siemens Energy 12.6x; median 17.7x) | — | Computed from MS FY26/FY27 multiples (D05 §Q2). The only independent cross-check is TIKR's VRT at ~24x (08-25), against the MS-computed 20.6x | **CORRECT as MS-computed, SINGLE-SOURCE.** VRT conflicts across vendors |
| GEV 28.2x | — | EV 247.2B / 8,767 ✓. Using MS's own GEV multiples (38.4 / 25.0) gives 27.4x | **CORRECT.** State it as 27.4–28.2x |
| GEV troughs 23.4 / 24.9 / 27.5 / 25.4x | — | Chartloom only; not point-in-time | **SINGLE-SOURCE** |

Sources: [Q2REL; T2Q26 chunks 251602/04/06/07; Q3'25 release -25-000159 (8.1%, $4.8B Power revenue); S02 vendor table; D07 Q1; D05 §Q2; S04]

### Q2. Five PM objections

1. **"A consensus above guidance is the signature of a serial raiser (sandbagging), not a Street that is too high."**
   - *For the objection:*
     - FY26 went from the Jan guide midpoint of $5,340M to the current $5,980M (+12%), with consensus at $6,359M (+19%) [R07 §1].
     - In Dec-24, the targets "slightly lagged consensus", and a year later the new framework surpassed the market (JPM via TipRanks and Yahoo; Morningstar).
     - FCF beats of 65–89% (brief).
   - *Against:*
     - The margin has never finished above its first numeric guide: FY25 came in at 8.40% vs an 8.5% midpoint [R01 #8].
     - The margin guide was held in July, when Q2 missed.
     - Wind was cut and then missed: −$598M against "~$400M" [Q3'25 release; 10-K p.72].
   - *Winner:* **the objection, for the Q3 and FY26 rungs** (consensus is inside the ranges). **Undetermined for FY27–28.**
2. **"Your management anchors are stale or constructed, so the ladder widens by construction."**
   - *For:*
     - The FY27 comparison point is interpolated.
     - The FY28 framework dates from January 2026, and the FY26 revenue guide has risen $1.5B since.
     - The pack's own T4: management's plan implies a 52.2% incremental margin from FY26 to 2028, *above* the Street's FY27 45–50%.
     - T3: the Street's FY27 step (+3.9 to +4.4 pts) is *smaller* than the guided FY26 step (+4.6).
   - *Against:* the Street's FY28 margin (21.6%) is 1.6 pts above the plan, and revenue staleness does not explain that.
   - *Winner:* **the objection, largely.** The widening is partly an artefact of timing.
3. **"The multiple has a floor you need to break."**
   - *For:* no month-end close below ~25x in the last 12 months, and troughs have stepped up from 15.6x to 23–25x to 25–28.5x [S04; D05].
   - *Against:* the 2025 troughs were 15.6–16.5x; the peer median is 17.7x; GE's P/E halved between 2000 and 2002 while EPS rose 19% [D05].
   - *Winner:* **the objection, over the January horizon.** 25–26x is at the floor, not inside the range.
4. **"January will not settle it, and it comes bundled with positives."**
   - *For:*
     - R07 zones: ~35% thesis-wrong, ~45% ambiguous, ~20% thesis-right.
     - Both prior first guides were at or below consensus, and the stock still rose (+5.01% and +15.62% next day) because frameworks were raised alongside.
     - The CEO has pre-flagged a backlog-margin change "larger" than low double digits, $200B backlog and ≥125 GW [S04; D07; LAG].
   - *Against:* no framework event is scheduled for January (the CMD is in spring). Q2'26, a hold with no margin raise, fell 8.69%.
   - *Winner:* **the objection.**
5. **"There is no information edge: GLJ published it, the backlog margin is disclosed, and the premium is growth-justified."**
   - *For:*
     - PEG 0.65 vs VRT 0.64.
     - Two-year EBITDA CAGR of 43.3% is the highest in the set.
     - GLJ's note made the same point on 09-14.
     - Revisions since then are flat.
     - Sources: [S04; D05; R08]
   - *Against:* the gap to Siemens Energy is not explained by growth (2.2x its multiple for 1.2x its growth), and the Street's +4.4-pt step sits at the 88th percentile of peer segment steps [S05].
   - *Winner:* **roughly even.**

### Q3. The long holder's best fact against each rung

| Rung | Long's best fact | Sources |
|---|---|---|
| Q3'26 | Consensus is inside management's own segment-implied range. At Laguna the CEO said Q3 orders were "very strong" and H2 gas commitments are "likely to prove to be conservative" | T2Q26 chunks; Laguna PDF / MarketBeat 09-18 (D07) |
| FY26 | Consensus is +3.2% above the sum of management's *segment* midpoints. Ex-Wind seasonality gives $6.37–6.60B if Wind delivers its guide | Q2REL; S03 §1 |
| FY27 | Management's plan implies a steeper incremental margin (52%) than the Street's FY27 (45–50%). The Street step (+4.4) is smaller than the guided FY26 step (+4.6). Peer SE Gas Services was +4.2 pts year on year in Q3 FY26 | Pack T3/T4; S05 (SE Q3 release and deck, same publisher) |
| FY28 | The last time the Street sat above the plan (Dec-24), management later leapfrogged it (14% → 20%). Since the framework was set, the FY26 revenue guide is +$1.5B | TipRanks/Yahoo 2024-12; Morningstar 2025-12-10; R08 guide path (Reuters/TipRanks) |
| Peer premium | Growth-adjusted it is in line with VRT. Bloom trades far higher | S04; EveryTicker [single] |

### Q4. Facts in S01–S05 that contradict the thesis

- **S03:** "Seasonality in Power and Electrification supports consensus FY26… Consensus ($6,359M) sits exactly on 'Wind delivers.'" This directly undercuts the FY26 rung, which S03 read as consensus = management's segment guides delivered [S03 §1, from releases Q2'24–Q2'26].
- **S04:** "Late January rolls the NTM window almost entirely onto FY27, so the price holds even if the multiple falls… today's price equals 25.1x." Also: "GEV's month-end NTM EV/EBITDA has not closed below ~25x" in the last 12 months [S04 §1 items 1–2].
- **S05:** "GEV's own Electrification already beats the peer base rate… [it] needs only about +1–2 pts a year." Also: "No sign of heavy-duty pricing flattening was found." [S05 §1]
- **S01, partial:** it concludes the backlog does "not support the Street's step", which supports the thesis. But it adds that the pass-through ranged "0.2x to 1.6x" and that "non-backlog levers… have at times been larger than the backlog effect". That weakens how precise the thesis can claim to be [S01 §1].
- **S02, both ways:** Mizuho "raised FY28 from $12.8B to $13.0B". One broker is moving FY28 *away* from the plan even as it cuts FY27.

Nothing is an outright falsification. The S03 and S04 lines are the closest.

### Q5. Base rate for another raise, and signs of slowing

- **Base rate.** No clean academic base rate for "raise after N raises" was found.
  - Myers, Myers & Skinner (2007) find 746 firms with EPS-increase strings of 20+ quarters, "much larger than would be expected by chance". Strings persist more than chance would predict, which the authors read as partly managed [S1: SSRN 741244] [S2: Exa library record of the same paper; one study → effectively SINGLE-SOURCE].
  - Guidance practice is sticky: past guidance predicts current guidance [NYU Stern working paper on guidance consistency, abstract only].
  - A naive Laplace estimate on 11 post-spin report/event days with no company revenue or FCF cut gives (11+1)/(11+2) ≈ 92% "no cut" next time [computed; the count is from R01 #5]. But the thesis does not need a cut.
- **The relevant base rate is first guides versus consensus.** It is 2 of 2 at or below consensus (FY25: JPM "slightly below"; FY26: at or below on revenue). **In both cases the stock rose**, because frameworks were raised at the same event [TipRanks 2024-12-11; S04 §1 item 5].
- **Evidence of slowing:**
  - The margin guide was held in July after the April raise [Q2REL; T2Q26 chunk 251606].
  - Q2 adj EBITDA was ~$1,255M (11.3% × $11,104M), below LSEG and StockStory estimates (−2.1%) [Q2REL; Reuters/StockStory via R08].
  - FY27 EPS revisions decelerated: +11.0%, then +6.5%, then +0.3% [R08: cnyes/FactSet → MS].
  - Q3 EPS revisions: −1.5% over 1 month and −2.1% over 3 months (ChartMill); −2.9% over 30 days (Zacks) [D07].
  - Mizuho cut FY27 [Investing.com; SINGLE].
- **Evidence against slowing:**
  - The FY26 revenue-guide increments *accelerated*: +$0.5B, then +$1.0B [R08: TipRanks/TheFly; Reuters].
  - Yahoo counts 18 up / 3 down FY27 revisions over 30 days.
  - Jefferies (→$1,185) and Bernstein (→$1,298) raised targets after GLJ [R08].

### Q6. The residual: what the team can say

**Can state with no qualifier:**
- FY28 consensus $13,064M (MS) is 16.6% above $56B × 20% = $11.2B.
- FY26 consensus ($6,359M / $6,394M) is above the company guide midpoint ($5,980M).
- There is no FY27 guidance; it comes on the January call.
- The FY26 margin guide was held at 12–14% in July.
- GEV trades at 27.4–28.2x NTM EV/EBITDA, against a median of 17.7x for the eight named peers (MS-computed).

**Needs a qualifier:**

| Statement | Qualifier to add |
|---|---|
| "Consensus above management at every horizon" | "above the midpoint. At Q3 and FY26, consensus is inside management's (rebuilt or guided) ranges." |
| "Widening" | "partly because the management anchors are older and the FY27 anchor is interpolated." |
| "Largest premium in the peer group" | "among these eight names; growth-adjusted it is in line with VRT." |
| "Needs 25–26x" | "On the research FY27 path, break-even is ~27–28x. About −10% needs ~25x." |
| "January call" | "presented by Parks; McDonough holds the CFO title from 1 Jan 2027" [8-K -26-000153; GEV PR 2026-08-27] |

**Drop:**
- "Consensus implies FY27 Power 21.7–23.5%": this is a back-solve (R01 #2).
- "Never beaten its first margin guide": FY24 had a qualitative guide, and FY26 was raised.
- "Q3 consensus above management's guide".
- "0 Sell ratings": GLJ's Sell exists.
- Any single "$9,574M" presented without the vendor band.

### Q7. The one extra check

**Back-test the ladder.** Rebuild Street-vs-plan at the equivalent points: Oct-2024 (vs the Mar-24 targets) and Oct-2025 (vs the Dec-24 targets), and at each horizon. Then record what the next first guide and framework did to estimates and to the stock.
- If the Street sat above the plan by a similar margin both times and management leapfrogged (Dec-24 and Dec-25 point that way), the ladder is not a signal, and confidence in the short falls sharply.
- If the premium today is materially larger than at those points, the thesis gains a real historical test.
- Where to look: the cnyes/FactSet archives (R08 URLs), Wayback captures of MarketScreener, and JPM/Morningstar event notes.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY26 guide | Revenue $45.5–46.5B; margin 12–14% held | Q2REL -26-000147 guidance | T2Q26 chunk 251606 | exact | H |
| 2 | Segment FY26 guides | Power +18–20% organic, 17–19%; Electrification $14.5–15.0B, 18–20%; Wind ~−$400M | Q2REL | T2Q26 chunk 251607 | exact | H |
| 3 | Q3 Power guide | Revenue +17–19%; margin ~17–18% | T2Q26 chunk 251602 | D07 citing Reuters 07-22 | close | M |
| 4 | Q3 Electrification guide | $3.8–4.0B; margin modestly above 18.4% | T2Q26 chunk 251604 | chunk 251603 (same transcript) | SINGLE-SOURCE | M |
| 5 | Q3'25 base | Adj EBITDA margin 8.1%; Power revenue $4.8B | Q3'25 release -25-000159 | S03 table | exact | H |
| 6 | 2028 framework | $56B, 20%, "by 2028" | Q4'25 release -26-000012 | News 2026-01-23, chunk 215481 | exact | H |
| 7 | Dec-24: targets below consensus | "slightly below consensus" | TipRanks / Markets Insider 2024-12-11 | Yahoo 2024-12-14 (same JPM note) | exact (same originator) | M |
| 8 | Dec-25 framework beat the market | "surpassed our and the market's expectations" | Morningstar 2025-12-10 | Reuters 2025-12-10 (record high) | close | M |
| 9 | Spring CMD, not December | "capital markets day in the spring" | MarketBeat 09-18, chunk 223197 | chunk 468155 | exact. **Conflict:** a 07-22 article (chunk 468970) says December; it predates Laguna | M |
| 10 | FY27 consensus band | $9.34–9.65B | Boursorama/FactSet 09-26 | MS 09-29 | close | H |
| 11 | Q2 adj EBITDA below estimates | ~$1,255M | Q2REL (11.3% × 11,104) | Reuters 07-22 via R08 | close | H |
| 12 | Revision deceleration | +11.0 / +6.5 / +0.3% | cnyes/FactSet (R08) | MS 09-29 | close | M |
| 13 | Bloom multiple | ~446x TTM EV/EBITDA | EveryTicker 2026-09-05 | — | SINGLE-SOURCE | L |
| 14 | Month-end multiple ≥ ~25x | 12 months | Chartloom (S04) | Nasdaq prices (inputs only) | SINGLE-SOURCE | L-M |

## 4. Arithmetic [computed]

**A. FY26 segment-guide sum.** Inputs: FY25 Power revenue $19,767M (brief/10-K p.72); Q2REL segment guides; corporate $450–500M (T2Q26 chunk 251608 via S03). I assume organic ≈ reported for Power.

| Line | Low | Mid | High |
|---|---|---|---|
| Power revenue | 23,325 | 23,523 | 23,720 |
| Power EBITDA | 3,965 | 4,234 | 4,507 |
| Electrification EBITDA | 2,610 | 2,803 | 3,000 |
| Wind | −400 | −400 | −400 |
| Corporate | −500 | −475 | −450 |
| **Total** | **5,675** | **6,162** | **6,657** |

- Consensus premium to the midpoint: 6,359 / 6,162 − 1 = **+3.2%**; FactSet 6,394 gives **+3.8%**.
- Guided dollar range: 45.5 × 12% = 5,460 to 46.5 × 14% = 6,510.

**B. FY27 interpolations**

| Method | FY27 value | MS premium | FactSet premium |
|---|---|---|---|
| Arithmetic: (5,980 + 11,200) / 2 | 8,590 | +11.5% | +8.7% |
| Geometric: √(5,980 × 11,200) | 8,184 | +17.0% | +14.1% |
| Revenue and margin separately: 51.0B × 16.5% | 8,415 | +13.8% | +11.0% |
| Arithmetic from segment-sum base: (6,162 + 11,200) / 2 | 8,681 | +10.3% | +7.6% |

**C. Q3 rebuild**
- Power: 4.8B × 1.17–1.19 = 5.62–5.71B, × 17–18% = 955–1,028.
- Electrification: 3.8–4.0B × 18.5–19% = 703–760.
- Wind: 0.
- Corporate: −112 to −125.
- Total ≈ **1,533–1,676**. The pack's 1,716 needs Electrification at ~20% or positive Wind.
- Consensus premium to the rebuild midpoint: 1,706 / 1,625.5 = +5.0%.

**D. Multiples**
- January NTM EBITDA = 11/12 × 9,574 + 1/12 × 13,064 = 9,865.
- Price at 25x: (25 × 9,865 + 9,113) / 266.33 = **$960**.
- Today: 247.2B / 8,767 = 28.2x.
- Using MS's own GEV multiples: 1 / (0.25/38.4 + 0.75/25.0) = 27.4x.

**E. Stale revenue anchor**
- FY26 revenue guide: 44.5 → 46.0 = +3.4%.
- Scaled framework: 56 × 1.034 × 20% = 11,580.
- Consensus 13,064 is then +12.8% above it, not +16.6%. About a quarter of the premium comes from the stale anchor (illustrative).

**F. H2'26**
- 6,359 − 2,146 = 4,213, which is +9.9% vs 3,834.
- The MS quarterly sum is 4,241 (+10.6%).

## 5. General question bank

- **G2:** the Street's FY27 step (+3.9 to +4.4) sits below the guided FY26 step (+4.6) but at the ~88th percentile of peer segment steps [Pack T3; S05].
- **G7 (information, interpretation or timing?):** there is no information edge. GLJ published on 09-14 and the backlog-margin data is disclosed. If an edge exists, it is interpretation plus timing [S02; S01].
- **G14:** the spring CMD with a 2030 outlook could re-anchor after January [MarketBeat 09-18].
- **G19:** the Dec-24 → Dec-25 cycle is the in-company analog, and it resolved long (Q2 answer, objection 1).
- **G21:** "if we were wrong, we'd see the Street above plan followed by a leapfrog". That has already happened once (Dec-24).

## 6. What would change this

- The Oct-24 / Oct-25 back-test (Q7) shows smaller premia then → the ladder becomes a signal.
- The Q3 print (10-28) takes the FY26 margin guide to the low half → the FY26 rung becomes real.
- January gives a dollar midpoint ≤ ~$8.55B with no framework raise → the thesis is confirmed. A midpoint ≥ ~$9.4B kills it.
- A second vendor for the multiple history showing sub-25x month-ends → the multiple floor weakens.

## 7. Disagreements with the master brief

- **Brief §4 ("Street FY28 16.6% above plan")** is correct, but the brief omits that the Street sat above the plan in Dec-2024 too, and management later leapfrogged it.
- **Brief §4:** "first under the new CFO" should read "presented by Parks, with McDonough as CFO from 1 Jan".
- **Brief §4 ("no December event")** is supported by the Laguna statement. One July article says a December analyst day is planned; treat that as superseded.
- **FY26 framing:** consensus sits inside management's range and close to its segment-guide sum. It is not simply "above management".

## 8. Open items

- The Q7 back-test: cnyes/FactSet archives, Wayback captures of MarketScreener, JPM Dec-24 and Morningstar Dec-25 notes.
- An independent historical source for NTM EV/EBITDA (Bloomberg, FactSet, CapIQ).
- A second source for the peer multiples. The VRT figure conflicts: 20.6x (MS-computed) vs ~24x (TIKR).
- Mizuho's full note (StreetInsider paywall).
- Any published expectation for the FY27 guide before January (the whisper number): not found.
