# Variation: told the team leans LONG (anchoring test)

_V03_anchor_long — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 01:22:12. Requests 20, input tokens 863586, output tokens 19012._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): long or short over 3–12 months from $962.49 (research input, as of 2026-09-30)

*This is research input only. Every range is a research estimate, and the team chooses its own numbers.*

**Source key:**
- **REL-2Q26**: 8-K 0001996810-26-000147, press release, 2026-07-22
- **10Q-2Q26**: 0001996810-26-000148
- **REL-4Q25**: 8-K 0001996810-26-000012, press release, 2026-01-28
- **10K-25**: 0001996810-26-000015
- **MS**: MarketScreener finances page, fetched 2026-09-29 (facts CT-01/02/04/06)
- **FS**: FactSet survey relayed by cnyes 6544296, 2026-07-23 (CT-10/11)
- **LAG**: GEV's own Morgan Stanley Laguna transcript PDF, 2026-09-16
- **MB-LAG**: MarketBeat write-up of Laguna, 2026-09-18 (corpus src:681)
- **CALL-4Q25**: Q4'25 call, corpus src:2660
- **BX**: Yahoo chart API / Nasdaq historical closes (facts BX-03..08)
- **D01 / D02 / D03 / D04**: tonight's outputs (segment build, long steelman, short steelman, January-guide study)

## 1. Bottom line

- **Direction: a thin LONG. p_long ≈ 0.53, confidence 2/5.** This goes against the brief's modest short lean. My FY27 EBITDA estimate is *below* consensus: base $8.9B vs $9,574M [MS; GLJ puts the Street at $9,450M, via facts GLJ rows]. So a long here has no estimate edge. It is a bet on how the market reacts to guides plus the roll-forward.
- **The estimate gap is real but moderate.**
  - FY27 base is ~7% below consensus.
  - FY28 base of $11.6B is ~11% below consensus $13,064M [MS]. That is close to management's own $11.2B (20% × $56B) [REL-4Q25; corpus src:27 news 2026-01-23].
- **The short's catalyst has not worked at GEV before.** Every new-guide or framework day was positive (4 of 4) [D04, from corpus price table plus Proactive/Reuters]. The January 2026 day, when the margin guide was not raised and Q4 EBITDA missed ($1.16B vs $1.29B), closed +2.73% [D04; StockStory src:3787, single price dataset]. The two sharp down days (−8.69% on Q2'26, −8.6% on the GLJ day) reversed within 1 and 11 sessions respectively [D04; evidence brief Test 6].
- **The roll-forward absorbs the gap.** Even on my below-consensus path, NTM EBITDA grows ~25% by Sep-2027 ($8,755M → $10,925M) [computed]. The stock is roughly flat at ~22x and +4% at 23x, against 28.2x NTM today [computed; facts VF-08].
- **The outcome is close to a coin flip.** The Sep-2027 value range is $880–$1,090 at 20–25x [computed]. The main swing factor is the multiple, not the estimate. The brief's argument about where the Street sits relative to management's plan is correct, but it is interpretation the market already knows, not new information.

## 2. The ladder, R1–R14

**R1. What $962.49 requires.**
- Market cap is $256.3B (962.49 × 266.33M) [yfinance quote 2026-09-30; P3 provider mkt cap $256.34B]. EV is ~$247.2B after $9,113M of net cash [10Q-2Q26 balance sheet; facts BX-26].
- To hold the price at Sep-2027 with today's net cash, the market needs either:
  - consensus NTM EBITDA of $12,191M at ~20x, or
  - management's plan path of ~$10.8B at ~23x [computed; MS; REL-4Q25].
- In physical terms:
  - Gas shipments of ~20–22 GW in 2027 and 24 GW in 2028 [REL-2Q26/CALL-2Q26 "at least 30 GW" over Q3'26–Q4'27; LAG p.4 via D01].
  - Power margin reaching ~22% by 2028 [REL-4Q25; Dec-2025 release src:2711].
  - New orders keep pricing well above the existing backlog: ">20%" [CALL-2Q26] and "10 to 20 points" [CALL-4Q25].
  - The 125 GW YE2026 contracted target is met [REL-2Q26; src:2685].

**R2. Consensus vs management's plan.**
- FY27: EBITDA $9,574M at 18.15% on revenue of $52,740M [MS]. The second source is revenue only: FS $52,632M [FS]. **No second EBITDA vendor was found.** GLJ's quoted Street figure of $9,450M is the only cross-check (−1.3%, close).
- FY28: EBITDA $13,064M at 21.6% on $60,500M [MS] (FS revenue $60,511M). Management's plan is $56B, 20%, $11.2B [REL-4Q25; src:27]. Street FY28 EBITDA is therefore **+16.6%** above the plan [computed].
- FY27 EPS: $24.85 [MS]. Second sources: FactSet mean $24.78 [FS] and Barchart $24.24 (2026-08-04).
- The straight line from the FY26 guide to the plan puts FY27 at $8.2–8.8B [D03, using REL-2Q26 and REL-4Q25].

**R3. Delivery vs guidance since the spin.**
- Guidance was never cut; it was raised or reaffirmed at every report [REL-2Q26; D04 guide table].
- Revenue beat the first numeric guide by +1.3% (FY24) and +4.3% (FY25). FCF beat by +89% and +65% [facts BR-21/24; 10K-25].
- Margin finished inside the range but below its midpoint: FY24 5.83% vs 6.0%, FY25 8.40% vs 8.5% [10Q-2Q25 non-GAAP table; Dec-2024 release src:2653; D03].
- FY26 consensus needs H2 at 16.3% vs H1 at 10.5% (+5.8 pts). Prior years added +2.2 pts in H2 [REL-2Q26 H1 10.5%; D03].
- 2025 bonus targets were beaten by a wide margin: EBITDA $3,196M vs a $2,900M target [DEF 14A 0001996810-26-000049; 10K-25]. The target itself is **[SINGLE-SOURCE]**.

**R4. Where the evidence differs from consensus.**
- **FY27 adjusted EBITDA: research base ~$8.9B vs $9,574M, about −$0.7B (−7%).** Research range $8.2–9.6B; the team chooses.
- FY28: base $11.6B vs $13,064M (−11%).
- The main line is the Power segment margin:
  - Consensus FY27 needs ~21.5–23.5%, i.e. its 2028 target a year early [D01 Q11; D02].
  - The CEO says the 2026 backlog-margin step "tells you the equipment margins for '29 and '30, largely" [LAG p.10; MB-LAG].

**R5. Why the market might not already know.**
- It largely does. Margin in backlog is published every January, and the Street-vs-plan gap has been visible since 2026-01-28 [CALL-4Q25; REL-4Q25].
- The Street is choosing to assume management sandbags, which is consistent with the bonus beats and two December framework raises [DEF 14A; D04].
- So the gap is **interpretation, not information**. That weakens the short: the market has to change its mind, not learn something new.

**R6. Strongest long argument.**
- The market rewards orders and cash over margin at GEV (4 of 4 guide days positive; January 2026 +2.73% despite an EBITDA miss) [D04].
- The spring-2027 Capital Markets Day with a 2030 outlook falls inside the horizon [LAG p.10–11; MB-LAG]. Prior framework events moved the stock +5.01% and +15.62% [D04; Proactive 2025-12-10].
- Power incremental margin was 44.4% from H1'25 to H1'26 [10Q-2Q26; CALL-2Q26].
- The stock is 19.5% below its 52-week high [P3 price block; BX-08 −18.1%]. NTM P/E is near the bottom of its post-spin range (min 33.8x) [facts BX-15, Chartloom, not point-in-time, SINGLE-VENDOR].

**R7. Strongest short argument.**
- Consensus FY27 already needs ~74% of the 13%→20% margin path covered in one year [D04, computed].
- P(January FY27 margin-guide midpoint < 18.15%) ≈ 85% [D04, research judgement].
- Street FY28 is 16.6% above the plan, while the CEO dates the next margin step to '29–'30 [LAG; MB-LAG].
- Deposit-funded cash is slowing: consensus FY27 FCF is −38% [MS, SINGLE-SOURCE]. The CEO said H2'26 commitments will be below H1's 40 GW [LAG p.3, SINGLE-SOURCE].
- The macro backdrop hurts long-duration multiples: 10-year yield at 5% and an AI-capex sentiment selloff on 2026-09-14 [evidence brief Test 6; Motley Fool 2026-09-14].

**R8. Evidence quality.**
- The short's *estimate* evidence is higher quality: primary filings and a CEO transcript, recent, cross-checked [LAG; REL-4Q25].
- The short's *price-mechanism* evidence is weak. There are only n=10 reaction days, and the analogues reversed quickly.
- The long's reaction-function evidence is also thin (n=4, all with framework raises except January 2026).
- Net: the estimate call goes to the short; the price-path call is roughly even to slightly long.

**R9. Dated events and pass marks.**

| Event | Date | Pass mark | Source |
|---|---|---|---|
| Q3'26 results | 2026-10-28 | Consensus EBITDA $1,706M, at the top of the guide-implied range | evidence brief; MS |
| FY27 outlook | Late January 2027 | Margin midpoint ≥18% (Street) vs ≤16.5% (bear) | LAG "'27 financial outlook in our January earnings call", facts; D04 |
| Capital Markets Day | Spring 2027 | 2030 outlook consistent with ≥$13B FY28 | LAG; MB-LAG |

- D04 corrects the brief on who presents the January call: Parks remains CFO through the Q4 call [GEV press release 2026-08-27; CFO Dive 2026-08-28].

**R10. Downside, judged by the stock's own history.**
- Five closing drawdowns of 15% or more since the spin: −38.3%, −17.5%, −15.0%, −24.6%, −25.5%. The median is −24.6% [BX-03..08; Nasdaq historical].
- A long that is wrong plausibly loses −15% to −25% (to ~$720–820), inside the stock's own history.
- A short that is wrong: the stock went from $270 (March 2025) to $1,175 (June 2026) [BX].

**R11. Value in Sep-2027 under each path** (net cash ~$16.2B including cash build; see §4).

| Path | NTM EBITDA | 20x | 23x | 25x |
|---|---|---|---|---|
| Consensus | $12,191M | $976 | $1,114 | $1,205 |
| Research base | $10,925M | $881 | $1,004 | $1,086 |
| Bear (FY27 $8.2B, FY28 $10.8B) | $10,150M | $823 | $937 | $1,014 |

- P/E cross-check: the stock's minimum post-spin NTM P/E of 33.8x × consensus Sep-2027 NTM EPS of $31.88 gives $1,078 [BX-15; VF-07]. On the haircut EPS of $28.57 it gives $966 [computed].

**R12. Historical analog.**
- The 2001–02 US gas-turbine bust:
  - ~46,000 MW of gas projects were shelved or cancelled after November 2001 [Power Engineering, 2002-09-01, power-eng.com].
  - GE planned for US gas-turbine orders and shipments to fall "80 percent or more over the next two years" [GE Power Systems release, 2002-07-23, ge.com].
  - Yet GE Power Systems' earnings still grew **+29% in 2002** and fell only in 2003 [GE 2003 annual report financial section, sec.gov 000079746304000012 ex99b]. The +29% figure is **[SINGLE-SOURCE]**. The GE 2003-07-11 release corroborates the 2003 "downturn in Power Systems' sales of large gas turbines".
- Lesson: in backlog businesses, profits lag orders by 1–2 years, so the cycle turns on orders and cancellations, not on near-year margins.
- Read-across:
  - GEV orders are still rising: a ≥125 GW target and a $200B backlog in 2027 [REL-2Q26; narrative-news 2026-09-24 citing the CEO].
  - The relevant short signal is an **orders or SRA-conversion slowdown** (H2'26 below H1's 40 GW [LAG, SINGLE-SOURCE]), not the FY27 margin.
  - The 2017–19 GE Power collapse was not researched (open item).

**R13. The single observation that would flip the view.**
- A January 2027 FY27 guide with a margin midpoint ≤16.5% **and** YE2026 contracted gas below 125 GW. Either one alone is survivable, based on the Q2'26 reversal [D04].

**R14. Confidence: 2/5.**
- The biggest uncertainty is the multiple: 20x vs 25x is ±$100 a share, larger than the whole estimate gap (~$0.7B × 23x / 266M ≈ $60 a share) [computed].
- Next are AI-capex sentiment and rates. Estimate risk comes third.

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Price at 2026-09-29 close | $962.49 | yfinance quote, 2026-09-30 | P3 price block (close 2026-09-29) | exact | H |
| 2 | FY26 guide | Revenue $45.5–46.5B, margin 12–14%, FCF $11.5–12.5B | REL-2Q26 "2026 Guidance" | 10Q-2Q26 / facts RQ rows | exact | H |
| 3 | 2028 plan | $56B, 20%, cumulative FCF ≥$24B | REL-4Q25 | News src:27, 2026-01-23 | exact | H |
| 4 | Consensus FY27 EBITDA | $9,574M | MS EBITDA row | GLJ's cited Street figure $9,450M | close (−1.3%) | M |
| 5 | Consensus FY27 revenue | $52,740M | MS | FS $52,632M | close | H |
| 6 | Consensus FY27 EPS | $24.85 | MS | FS $24.78; Barchart $24.24 | close | H |
| 7 | Consensus target | $1,237.34 | Yahoo Finance, 2026-09-21 | MarketBeat $1,145.83, 2026-09-21 | **conflict** (panel difference: 37 vs MarketBeat's own panel) | M |
| 8 | CEO dates backlog margin to '29–'30 | Quote | LAG p.10 | MB-LAG src:681 | exact | H |
| 9 | Higher-margin 2024–25 orders deliver "'27 and beyond" | Quote | CALL-4Q25 src:2660 | Trade press src:149/293 | exact | H |
| 10 | Margin finished below guide midpoint | FY24 5.83% vs 6.0%; FY25 8.40% vs 8.5% | 10Q-2Q25 / 10K-25 | Dec-2024 release src:2653; src:2711 | exact | H |
| 11 | Guide/framework days positive | 4/4; +5.01%, +15.62% | Corpus price table (D04) | Proactive / Reuters, 2025-12-10 | close | M |
| 12 | Drawdowns since spin | Median −24.6% | Yahoo closes | Nasdaq historical | exact | H |
| 13 | 2002 Power Systems earnings +29% before the 2003 drop | +29% | GE annual-report ex99b (sec.gov) | GE 2003-07-11 release (downturn only) | partial / SINGLE-SOURCE for +29% | M |
| 14 | 2001–02 cancellations | ~46,000 MW | Power Engineering, 2002-09 | Fortnightly, 2002-06 (shakeout; 380 GW of plans) | close | M |
| 15 | Consensus FY27 FCF | $7,417M | MS | none found | SINGLE-SOURCE | L |

## 4. Arithmetic

**Market cap and EV today**
- Market cap = 962.49 × 266.33 = $256,340M.
- EV = 256,340 − 9,113 = $247,227M.

**NTM EBITDA**
- Today: $8,755M [VF-08].
- Research path at Sep-2027 = 0.25 × 8,900 + 0.75 × 11,600 = **$10,925M**, i.e. +24.8% vs $8,755M.
- Research FY28 base = $56B × 1.035 (the historical revenue beat, taken between +1.3% and +4.3%) × 20% = $11.6B. This is a research estimate; the team chooses.

**Net cash at Sep-2027**
- 9,113 + H2'26 FCF (12,000 guide midpoint − 9,897 H1) + 0.75 × 7,417 (FY27 consensus FCF) − ~530 dividends ($2.00 × 266M; P3, period unverified) ≈ **$16.2B**.
- Buybacks are treated as neutral per share.
- Caveat: much of this cash is customer deposits (contract liabilities). Excluding the build, $9.1B of net cash lowers every value by ~$27 a share.

**Value per share**
- Formula: value = (multiple × NTM EBITDA + 16,200) / 266.33.
- Research base: 20x $881; 22x $963; 23x $1,004; 25x $1,086.
- Consensus path at 23x: (280,393 + 16,200) / 266.33 = $1,114.

**Price-flat multiples**
- On the plan path, price-flat needs 247,227 / 10,794 = 22.9x.
- On consensus, it needs 247,227 / 12,191 = 20.3x.

**Estimate gaps**
- FY27: 8,900 / 9,574 − 1 = −7.0%.
- FY28: 11,600 / 13,064 − 1 = −11.2%.

**Rough scenario expected value** (research judgement): 30% × $1,160 + 40% × $985 + 30% × $805 ≈ $983 before cash build, i.e. +2%. That is why p_long is only 0.53.

## 5. General question bank

- **G5 (stock flat for 12 months):** by construction, a flat price on the plan path means the multiple compresses to ~23x NTM [computed].
- **G7 (why the market hasn't seen it):** interpretation, not information (R5).
- **G19 (historical analog):** see R12.
- **G23 (why the price move is bigger or smaller than the estimate gap):** the multiple swing (±$100 a share) dominates the estimate gap (~$60 a share).

## 6. What would change this

- **Toward a short:**
  - The January guide midpoint ≤16.5%.
  - The ≥125 GW target missed.
  - Visible SRA cancellations or deferrals, which is the 2001–02 pattern.
  - An NTM multiple below 20x on unchanged numbers, driven by rates or AI-capex sentiment.
- **Toward a stronger long:**
  - A FY27 margin guide ≥18%.
  - The CMD's 2030 outlook implying FY28 of ≥$13B.
  - Q3 EBITDA at or above $1,706M with Power ≥19%.

## 7. Disagreements with the master brief

- **Direction.** The brief leans short at 55–60%. I lean a thin long at 0.53. The brief's estimate evidence is right, but its price mechanism (the January guide causing a de-rating) has no precedent at GEV. The evidence available shows cautious-margin days being bought back.
- **CFO.** The January call is presented with Parks still CFO, not McDonough alone [GEV release 2026-08-27; CFO Dive 2026-08-28]. The "new CFO resets expectations" angle is weaker than the brief says.
- **Consensus target.** $1,237.34 is panel-specific. MarketBeat shows $1,145.83.

## 8. Open items

- A second vendor for FY27/FY28 EBITDA consensus (try Visible Alpha, or the LSEG/Refinitiv panel via Reuters).
- GE Power's 2017–19 share-price path vs its orders, as a second analog.
- Peer forward EV/EBITDA for Siemens Energy and Vertiv, to anchor the 20–25x band (not found).
- H2'26 commitments vs H1's 40 GW needs a second source (the Q3 call on 2026-10-28).
- The dividend-per-share period for the net-cash bridge (10Q-2Q26 equity note).

```FINAL_BLOCK
{"direction": "long",
 "p_long": 0.53,
 "fy27_adj_ebitda_usd_m": {"low": 8200, "base": 8900, "high": 9600},
 "fy28_adj_ebitda_usd_m_base": 11600,
 "one_number": "FY28 adj EBITDA: research base ~$11.6B (near management's $11.2B 2028 framework) vs MarketScreener consensus $13,064M, about -11%; FY27 ~-7% ($8.9B vs $9,574M)",
 "target_price_range_usd": [880, 1090],
 "target_formula": "20x-25x (base 23x) x Sep-2027 NTM adj EBITDA $10,925M (0.25x$8.9B FY27 + 0.75x$11.6B FY28) + ~$16.2B projected net cash, / 266.33M shares = $881-$1,086 (base ~$1,004)",
 "horizon_months": 12,
 "kill_rule": "Late-Jan-2027 FY27 outlook with adj EBITDA margin guide midpoint <=16.5% AND YE2026 contracted gas (backlog+SRA) below 125 GW; or GEV closes below $780 (≈-19%) before the spring-2027 CMD",
 "top_reason": "Even on below-consensus estimates, NTM EBITDA rolls forward ~25% by Sep-2027, and GEV's market has so far rewarded orders and cash over margin shortfalls (4/4 guide days up, cautious-margin days reversed quickly), which outweighs a ~7-11% estimate gap that is interpretation rather than new information.",
 "confidence_1_to_5": 2}
```
