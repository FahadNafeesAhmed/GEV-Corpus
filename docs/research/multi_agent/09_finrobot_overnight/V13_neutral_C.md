# Variation: neutral framing (C — third sample, noise check)

_V13_neutral_C — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:56:22. Requests 36, input tokens 2178129, output tokens 21592._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): long or short over 3–12 months from $962.49 (2026-09-29 close)

Research input only. The team writes every memo sentence and picks every forecast number. All probabilities are research judgement, and all ranges are research estimates.

**Source key**
- **Q2REL** = 8-K 0001996810-26-000147 EX-99 (2026-07-22)
- **10Q** = 10-Q 0001996810-26-000148 (2026-07-22)
- **10K** = 10-K 0001996810-26-000015
- **Q1REL** = 8-K 0001996810-26-000063 (2026-04-22)
- **Q4REL** = 8-K 0001996810-26-000012 (2026-01-28)
- **Q4T** = Q4'25 call transcript (corpus src:2660, 2026-01-23)
- **DEC25-QA** = Dec-2025 Investor Update Q&A web transcript excerpt (corpus src:2686, undated; the content refers to the "2035 milestone" and "the page that Scott showed")
- **LAG-PDF** = GEV-hosted Morgan Stanley Laguna transcript (2026-09-16)
- **LAG-SA** = stockanalysis.com copy of the same transcript
- **MS** = MarketScreener (fetched 2026-09-29)
- **GF** = GuruFocus GLJ wire (2026-09-15)
- **BX** = Yahoo chart API and Nasdaq closes
- **YF** = FinRobot yfinance quote (2026-09-30 07:52 UTC)
- **D0x/E0x** = earlier outputs tonight; they carry their own primary citations. I did not read any V-output.

---

## 1. Bottom line

- **The gap to consensus is in the estimates.** Every build tonight puts FY27 adjusted EBITDA at about $8.6–8.8B, against consensus of $9,574M (−8% to −10%). The line that decides it is the FY27 Power segment margin. To reach consensus, Power needs about 21.7–23.5%. The FY26 guide midpoint is 18%, and the fastest annual step so far was +3.3 points.
  - Consensus: [S1: MS] [S2: GF "Street $9.45B"]
  - Builds: [S1: D01A] [S2: D01B]
  - Power history: [S1: 10K/Q2REL segment tables] [S2: 10Q MD&A]
- **Management's own timing supports the lag.**
  - Q4'25 call: the majority of the higher-margin '24–'25 orders do not *begin* delivering "until '27 and beyond" [S1: Q4T chunk 246127] [S2: trade press, corpus src:149].
  - Dec-2025 Q&A: "orders we're taking today. We're shipping in '29 or '30" [S1: DEC25-QA chunk 246346]. At Laguna, the CEO said the 2026 backlog-margin change "tells you the equipment margins for '29 and '30, largely" [S2: LAG-PDF p.10].
  - These are two different events, so the timing leg is less single-sourced than D08 judged.
- **Over 12 months, the price mechanics go the other way.** At a constant multiple, the NTM roll-forward to Sep-2027 is +39% on consensus and +23% on management's plan path. That is larger than the ~8% estimate gap.
  - The breakeven multiple in Sep-2027 is 20.3x consensus NTM, or about 22x the plan path (computed A2).
  - Consensus: [S1: MS] [S2: GF]. Plan: [S1: Q4REL] [S2: news src:27].
- **How the reveal tends to trade.** Guide and framework days have all closed up (+2.7% to +15.6%). Raises that held margin flat traded down (Q2'26 −8.69%). GEV's first guides are beatable: the FY26 first guide of 11–13% was raised to 12–14% in April.
  - Event returns: [S1: BX-13] [S2: Barron's/Proactive for 2025-12-10 "+16%"]
  - Raise: [S1: Q1REL] [S2: web copy src:2708]
- **Research lean: a short into the January FY27 outlook has the better, though thin, edge.** E02 computes a central expected return of about +4.3%, ranging −0.6% to +12.1% by multiple frame. At 12 months there is no edge (±2%). P(long works) ≈ 0.45. Confidence 2/5.

---

## 2. The ladder (R1–R14)

**R1. What today's price requires**
- The market sets EV at $247,227M: market cap $256,340M (962.49 × 266.33M) less net cash of $9,113M.
  - Price: [S1: YF] [S2: Zacks/Yahoo 9/29]
  - Shares and net cash: [S1: 10Q balance sheet] [S2: stockanalysis EV $247.34B]
- **In financial terms:**
  - At 25x in January 2027, the price needs NTM EBITDA of $9,889M. Consensus Jan-frame NTM is $9,865M, so **today's price is consensus at ~25x**.
  - At Sep-2027, it needs $11,238M at 22x (≈ management's 2028 plan of $11.2B) or $12,361M at 20x (A1).
- **In physical terms:**
  - Gas output runs at 5 GW/quarter now, reaching 6 GW/quarter in H2'27 (≤~22 GW in calendar 2027) and 24 GW in 2028 [S1: LAG-PDF p.4] [S2: LAG-SA].
  - Power margin must reach the 2028 target of 22% about a year early [S1: Q4REL] [S2: Dec-25 release].
  - The margin has to come from pricing on backlog that is still converting. Equipment RPO is $87,821M; 36% converts within 1 year and 65% within 2 years [S1: 10Q Note 9] [S2: GEV IR deck copy src:3159 — same publisher, weak].

**R2. Consensus vs management's plan**

| | FY27 consensus | FY28 consensus | 2028 plan | FY28 gap to plan |
|---|---|---|---|---|
| Revenue | $52,740M | $60,500M | $56B | +8.0% |
| Adj EBITDA | $9,574M (18.15%) | $13,064M (21.6%) | $11,200M (20%) | +16.6% |

- FY27 consensus: [S1: MS] [S2: GF $9.45B; S&P/stockanalysis revenue $52.74B]
- FY28 consensus: [S1: MS] [S2: Motley Fool 60% CAGR → ~$13.09B]
- Plan: [S1: Q4REL] [S2: Q4T "at least $56 billion… 20%"]
- A straight line from the FY26 midpoint (13%) to the 2028 plan (20%) gives FY27 at 16.5%, or $8,702M on consensus revenue. Consensus sits 10% above that (A3).
- There is no FY27 guidance yet.

**R3. Delivery record since the spin**

| Metric | Record |
|---|---|
| Revenue vs first numeric guide midpoint | +1.26% (FY24), +4.30% (FY25) |
| Adj EBITDA margin vs mid-year raised midpoints | Finished slightly below: 5.83% vs 6.0%; 8.40% vs 8.5% |
| First (qualitative) margin guides | Met |
| FCF vs initial guide | +89%, +65% |
| FY26 margin guide | Raised from 11–13% to 12–14% at Q1'26, then held at Q2 |
| Wind | Cut at Q3'25; 2028 Wind margin target lowered from 10% to 6% |

- Revenue, margin and FCF record: [S1: facts BR-21/23/24, built from Q4REL and the FY24 release] [S2: MS actuals]
- FY26 raise: [S1: Q1REL] [S2: Q2REL]
- Wind cut: [S1: 8-K -25-000159] [S2: Dec-25 release]
- Pattern: revenue and cash beat by a lot; margin lands inside the range.

**R4. Where the evidence differs most from consensus**
- **FY27 Power segment EBITDA margin.** Consensus-implied is 21.7–23.5%; research base is 20.0–20.5%, a gap of about 2–3 points. At ~$275M per point, that flows to FY27 adj EBITDA of $8.6–8.8B vs $9,574M (−8% to −10%) [S1: D01A Q11] [S2: D01B §4-L].
- **Pace test (A4).** Annual Power margin steps have been +2.63 points (FY24), +2.17 (FY25) and +3.32 (FY26 guide midpoint of 18%). Consensus needs +3.7 to +5.5 points in FY27.
  - Segment history: [S1: 10K] [S2: Q2REL]
  - FY26 Power guide of 17–19%: [S1: Q2REL] [S2: Q1REL]
- **FY28 is the larger gap:** +16.6% vs plan.

**R5. Why the market might not already know this**
- The gap is interpretation and timing, not new information. GEV publishes margin-in-backlog every January, and GLJ published the idea on 2026-09-14. The stock then recovered 106% of the 8.6% drop [S1: BX] [S2: GF/TIKR 2026-09-27].
- **What the market underweights:** a dollar share of 2027 revenue is not a margin share. The price uplift sits in heavy-duty gas with the longest lead times [Q4T; LAG-PDF].
- **Honest caveat:** this is a known debate. The edge is not information. The edge would be the January guide landing where the timing implies.

**R6. Strongest long argument**
- **Roll-forward plus capacity scarcity.**
  - Consensus NTM EBITDA rises 39% by Sep-2027, and even on the plan path the Sep-2027 NTM is +23% vs Jan (A2).
  - Siemens Energy is "sold-out until FY28" [S1: SE CFO deck src:3179] [S2: trade press src:1699].
  - GEV is selling 2032 delivery slots [S1: TIKR 2026-09-27] [S2: MarketBeat src:681].
- **Beatable internal targets.** The 2025 bonus paid 130% on EBITDA [S1: DEF 14A -26-000049] [S2: actuals from Q4REL].
- **Upside not in backlog margins.** Management says backlog margins exclude "variable cost productivity versus known cost today" [S1: Q4T chunk 246128] [S2: Dec-2025 release, "incremental opportunity… not projected in our backlog", per Q4T].
- **Management does not describe 2024 orders as cheap.** The CEO calls both "'24 and '25" orders "higher-margin" [S1: Q4T] [S2: src:149]. That weakens GLJ's premise of a cheap 2024 book.

**R7. Strongest short argument**
- Consensus FY27 needs Power near its 2028 target a year early, at a pace 1.1–1.7x the fastest step so far (A4).
- Management maps margin to 3–4 years after order ['29/'30: DEC25-QA; LAG-PDF].
- The equipment RPO 1-year share fell from 45–47% (2024 10-Qs) to 36% (6/30/26). Backlog is lengthening, so new pricing lands later [S1: 10-Q 0001996810-24-000008 / -24-000067] [S2: 10Q Note 9].
- The stock has punished flat margin guides: Q2'26 −8.69%, with William Blair noting investors "had expected… margin expansion" [S1: BX-13] [S2: Marketscold 2026-07-25 citing Reuters].
- The multiple is 28.2x NTM EV/EBITDA with the 10-year near 5% [S1: MS-computed] [S2: Chartloom 27.7x].

**R8. Which side's evidence is better**
- **On the estimate line, the short is better.** It rests on primary filings, two consensus vendors within 1.3%, and two independent management statements on timing.
- **On the price line, the long is better.** The roll-forward is arithmetic on the same consensus inputs, and there are strong reaction base rates on framework and guide days.
- The long's weakest input is FY28 consensus, 16.6% above plan and effectively single-vendor for the full row.
- The short's weakest step is the de-rating it needs. About $100–110/share of typical short targets comes from the multiple [S1: V10 A4 as cited in D10] [S2: E02].

**R9. The dated reveal and pass marks**
- **Event:** the late-January 2027 Q4'26 call with the FY27 outlook. The date is not yet announced; prior years were 01-22 and 01-28. Ken Parks, not the new CFO, likely presents [S1: CFO-PR] [S2: CFO Dive].
- **Short pass mark:** margin-guide midpoint ≤17.0%, which is ≈$8,966M on consensus revenue (−6.4%), with 2028 held at 20%.
- **Long pass mark / short kill:** low end ≥18%.
- **Research odds:** P(midpoint <18.15%) ≈ 80–85%; P(≤17.5%) ≈ 65–68% [S1: D04A] [S2: D04B].
- **Interim events:**
  - Q3'26 on 2026-10-28, after the finals. Consensus EBITDA is $1,706M (MS) / $1,728M (ChartMill).
  - YE2026 gas backlog + SRAs ≥125 GW.

**R10. How much can be lost**

| Position | Adverse case | Loss |
|---|---|---|
| Short | Record close $1,174.86 | +22% against |
| Short | Bull January case at 30x ($1,181) | −23% |
| Short, 12 months | Consensus at constant 28x ($1,338) | −39% |
| Long | Median post-spin drawdown | −24.6% |
| Long | Maximum post-spin drawdown | −38.3% |

- Daily σ ≈ 3.3%, so the ~4-month horizon carries about 30% of noise against a ~5% expected edge.
- Record close: [S1: BX-08] [S2: D08]
- Drawdowns: [S1: BX-03..08] [S2: Nasdaq closes; the −38.3% peak is not re-found]
- σ: [S1: BX] [S2: evidence_lanes verifier re-check]

**R11. What the market would pay a year out**
- Formula: (multiple × NTM + $9,113M) / 266.33M.

| Sep-27 NTM EBITDA | 20x | 22x | 25x |
|---|---|---|---|
| $12,191M (consensus) | $950 | $1,041 | $1,179 |
| $10,794M (plan path) | $845 | $926 | $1,047 |
| $10,500M (research path) | $823 | $902 | $1,020 |

- **January frame on the research path** (FY27 $8,800M, FY28 $11,300M; NTM $9,008M): 23x $812, 25x $880, 26x $914.
- **Probability-weighted 12-month return:** about +1–2% [S1: E02 §Q1] [S2: E06 §1].

**R12. Historical analog**
- **GE 2000–02 fits best.** GE's P/E halved from 42.6x to 21.1x while EPS rose 19%. GE Power Systems earnings peaked in 2002 (+29%), and U.S. gas turbine sales were lower in Q1 2003 [S1: GE 2003 10-K ex13 on sec.gov] [S2: NY Post 2002-04-16 / GE dex99b].
- **Lesson:** de-rating can come two years before the earnings peak. That supports multiple risk more than an earnings bust inside the horizon.
- **GEV's own Jan–Apr 2025 swing:** 33x to 15.6x NTM [SINGLE-SOURCE: Chartloom; prices via BX].

**R13. The single observation that would flip the view**
- A FY27 adj EBITDA margin guide with a **low end ≥18%**.
- Or, before 2027-04-30, a 2028 framework raised to **≥$12.5B EBITDA**.

**R14. Confidence and what drives the uncertainty**
- **Confidence: 2/5.**
- The biggest driver is the multiple: one NTM turn ≈ $35–43/share, which is about the size of the whole expected edge.
- The second is GEV's guiding style, whether it sandbags a low first guide that the market then looks through. Precedent: FY26 was guided at 11–13% and raised to 12–14%, and the stock rose on the December 2025 guide day (+15.6%, with a framework raise and buyback).
- The third is Q3'26 (10-28). A beat-and-raise would move the short about 10% under water before January (E05).
- Direction depends on horizon. Short-leaning through January (p_long ≈ 0.45); a coin-flip at 12 months (≈0.50–0.52).

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | Close | $962.49 | YF 2026-09-30 | Zacks/Yahoo 9/29 | exact | H |
| 2 | Shares / net cash | 266.33M / $9,113M | 10Q balance sheet | stockanalysis EV $247.34B | close | H (NCI single) |
| 3 | FY27 consensus EBITDA | $9,574M | MS 9/29 | GF $9.45B | close (−1.3%) | M–H |
| 4 | FY28 consensus vs plan | $13,064M vs $11,200M | MS / Q4REL | Motley Fool / Q4T | close | M |
| 5 | FY26 margin guide raised | 11–13% → 12–14% | Q1REL | src:2708 web / Q2REL held | exact | H |
| 6 | Power margin path | 9.88 / 12.51 / 14.68 / 17.63% | 10K | Q2REL, 10Q | exact (company-only) | M–H |
| 7 | Consensus-implied FY27 Power margin | 21.7–23.5% | D01A | D01B | close (derived) | M |
| 8 | "higher-margin orders '24–'25… '27 and beyond" | quote | Q4T chunk 246127 | src:149 trade press | exact | H |
| 9 | Orders today ship '29–'30 | quote | DEC25-QA chunk 246346 | LAG-PDF p.10 (different event) | consistent | M |
| 10 | Equipment RPO 1-year share | 45–47% (2024) → 36% (6/30/26) | 10Qs -24-000008/-24-000067 | 10Q Note 9 | exact | H |
| 11 | Q2'26 reaction | −8.69% | BX-13 | Reuters via Marketscold | close | H |
| 12 | Guide/framework-day returns | +2.7% to +15.6% | BX-13 | Proactive/Benzinga 2025-12-10 | close | H |
| 13 | Drawdowns | median −24.6%, max −38.3% | BX | Nasdaq | close (peak not re-found) | M |
| 14 | Analyst count | 0 Sell | 24/7 Wall St 9/16 (6 SB/24 B/7 H) | MarketBeat-syndicated feed: MS Underweight on 8/3 | **conflict** | L |
| 15 | Consensus target | $1,237 | TIKR / biggo | MarketBeat $1,145.83 | **conflict** (vendor basis) | M |
| 16 | FY26 FCF guide | $11.5–12.5B | Q2REL | Kalkine 9/29; Lark says $11.5–13.5B | conflict: Lark wrong | H |

---

## 4. Arithmetic

- **A1. EV and required NTM EBITDA**
  - EV = 962.49 × 266.33 = $256,340M; less $9,113M = $247,227M.
  - Required NTM: ÷25 = $9,889M; ÷22 = $11,238M; ÷20 = $12,361M.
- **A2. January-frame consensus NTM and roll-forward**
  - Jan NTM = 11/12 × 9,574 + 1/12 × 13,064 = $9,865M.
  - Consensus roll-forward: $12,191M / 8,776 − 1 ≈ +39% vs FY27.
  - Plan path: $10,794M / $8,776M ≈ +23%.
  - Breakeven multiple, Sep-2027: 247,227 / 12,191 = 20.3x (consensus); 247,227 / 10,794 = 22.9x (plan).
- **A3. Straight-line FY27 margin**
  - (13% + 20%) / 2 = 16.5%; × $52,740M = $8,702M.
  - $9,574M / $8,702M = +10.0%.
- **A4. Power margin steps**
  - Steps: 12.51 − 9.88 = 2.63; 14.68 − 12.51 = 2.17; 18.0 − 14.68 = 3.32.
  - Consensus needs 21.7 to 23.5 − 18.0 = +3.7 to +5.5 points.
- **A5. Research January target**
  - NTM = 11/12 × 8,800 + 1/12 × 11,300 = $9,008M.
  - 23x: (207,184 + 9,113) / 266.33 = $812.
  - 26x: (234,208 + 9,113) / 266.33 = $914.
  - 25x on FY27 of $8,800M: $860 (−10.6%).
- **A6. Guide translation on consensus revenue $52,740M**
  - 17.0% → $8,966M; 18.0% → $9,493M.

---

## 5. General question bank (answered along the way)

- **G1:** see R1.
- **G2:** consensus Power pace exceeds any prior annual step (A4).
- **G5:** a flat stock needs NTM EV/EBITDA to fall to 25.1x by January and 20.3x by Sep-2027 (E02).
- **G7:** interpretation and timing, not information (R5).
- **G13:** see R9.
- **G15:** see R10.
- **G17:** buybacks (Q2'26: $3,037M left at 6/30 [S1: 10Q Part II Item 2] [S2: 10-Q -26-000064 via VF-13]) and the guide style are the tools that could break a short.
- **G19:** see R12.
- **G21:** evidence that would say the thesis is wrong is a guide with a low end ≥18%; nothing observable yet.

---

## 6. What would change these findings

| Finding | What would overturn it |
|---|---|
| Estimate gap | Q3'26 Power margin ≥19–20% with Wind at or above breakeven. Or a January guide low end ≥18% |
| Timing leg | A full Laguna p.10 context showing the '29/'30 line applies only to SRAs. Or a Q3 10-Q showing the equipment RPO 1-year share rising back above 40% |
| Price-line favours long at 12 months | NTM multiple falling to ≤20x, or FY28 consensus converging down to about $11.2B before the CMD |

---

## 7. Disagreements with the master brief

1. **"Never beat its first margin guide" is outdated.** The FY26 first guide of 11–13% was raised to 12–14% [Q1REL; src:2708]. The FY24 and FY25 shortfalls were against mid-year raised guides.
2. **"First call under the new CFO" is wrong.** Parks presents in January [CFO-PR; CFO Dive via D10].
3. **The timing leg is better sourced than D08 judged.** A second, different-event source exists: the Dec-2025 Q&A "orders we're taking today. We're shipping in '29 or '30" (src:2686, undated web excerpt). Also, the Q4'25 quote calls **2024** orders "higher-margin" too, which cuts against GLJ's "cheap 2024 book".
4. **"0 Sell" and the $1,237 target vary by vendor.** MarketBeat shows $1,145.83 and a Morgan Stanley Underweight on 8/3. That is unverified and contradicted by 24/7 Wall St's 0-Sell count.

---

## 8. Open items

- **Morgan Stanley rating:** confirm on a terminal. The 7/23 target raise to $1,350 Overweight makes an 8/3 Underweight look like a data error.
- **Laguna PDF pp.9–11:** read in full for context. Also find the date and source document behind src:2686.
- **Second full-row EBITDA vendor** for FY27/FY28 consensus (FactSet or Bloomberg).
- **Q3'26 10-Q (10-28):** updated RPO 1-year share, the pace of CSA revisions, and buybacks.
- **Hyperscaler capex-guide dates** inside the window: not researched.

```FINAL_BLOCK
{"direction": "short",
 "p_long": 0.45,
 "fy27_adj_ebitda_usd_m": {"low": 7900, "base": 8800, "high": 9700},
 "fy28_adj_ebitda_usd_m_base": 11300,
 "one_number": "FY27 adj EBITDA: research base ~$8.8B vs MarketScreener consensus $9,574M (-8%), driven by FY27 Power segment margin ~20-20.5% vs ~21.7-23.5% implied by consensus",
 "target_price_range_usd": [810, 915],
 "target_formula": "(23x-26x) x Jan-2027 NTM EBITDA $9,008M (11/12 x FY27 $8,800M + 1/12 x FY28 $11,300M) + $9,113M net cash, / 266.33M shares = $812-$914",
 "horizon_months": 4,
 "kill_rule": "Late-Jan-2027 Q4'26 call guides FY27 adj EBITDA margin with low end >=18% (>= ~$9.5B), or 2028 framework raised to >= $12.5B EBITDA before 2027-04-30; hard stop on a close above the $1,174.86 record",
 "top_reason": "Consensus FY27 needs Power margin near its 2028 target a year early at 1.1-1.7x the fastest step GEV has delivered, while management's own statements place the high-margin deliveries mostly in 2029-30, and the January FY27 guide falls inside a 4-month horizon before the 12-month roll-forward can offset it.",
 "confidence_1_to_5": 2}
```
