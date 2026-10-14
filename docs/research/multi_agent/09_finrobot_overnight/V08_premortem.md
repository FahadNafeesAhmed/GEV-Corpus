# Variation: pre-mortem on both directions

_V08_premortem — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 01:50:33. Requests 18, input tokens 853462, output tokens 27109._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): long vs short failure stories and the R1–R14 ladder (research input only, as of 2026-09-30)

**Research input only.** The team writes every memo sentence and chooses every forecast. All ranges and probabilities below are research estimates or research judgement.

**Source key (used throughout)**
- **10Q-2Q26** = 10-Q 0001996810-26-000148 (2026-07-22)
- **REL-2Q26** = 8-K 0001996810-26-000147, press release (2026-07-22)
- **REL-4Q25** = 8-K 0001996810-26-000012, press release (2026-01-28)
- **CALL-4Q25** = Q4'25 transcript, corpus src:2660
- **N27** = news on the Q4'25 outlook, corpus src:27 (2026-01-23)
- **N354** = news on the Q2'26 guide, corpus src:354 (2026-07-23)
- **MS** = MarketScreener finances page, fetched 2026-09-29 (facts CT-01/02/04/06)
- **YF-GLJ** = Yahoo/GuruFocus, "GLJ Starts GE Vernova at Sell…", 2026-09-15
- **LAG** = GEV-hosted Morgan Stanley Laguna transcript PDF, 2026-09-16 (facts VF-02)
- **MB-LAG** = MarketBeat write-up of Laguna, corpus src:681
- **BX** = Yahoo chart API and Nasdaq historical closes (facts BX-03..08)
- **D03 / D04** = tonight's short-steelman and January-guide outputs. Their primary citations are carried through.

---

## 1. Bottom line

- **Consensus FY27 adjusted EBITDA is about $9.45–9.57B. It sits 9–11% above a straight line from the FY26 guide to management's 2028 plan ($8.59–8.78B).**
  - Consensus: $9,574M [S1: MS] vs $9.45B as cited by GLJ [S2: YF-GLJ]. Only one vendor publishes the full number, so this is close to single-source.
  - Plan: 2028 is $56B × 20% = $11.2B [S1: REL-4Q25] [S2: N27]. The FY26 guide is 12–14% on $45.5–46.5B [S1: REL-2Q26] [S2: N354].
- **Consensus FY28 of $13,064M is 16.6% above the 2028 plan.** The CEO says the next backlog-margin step "tells you the equipment margins for '29 and '30, largely" [S1: LAG p.10] [S2: MB-LAG].
- **The short needs two things at once: an estimate cut and a de-rating. The long needs only the multiple to hold.**
  - At Sep-2027, the breakeven NTM EV/EBITDA is 20.3x on consensus and 22.8x on a plan-path research base. Today it is ~28.2x [computed, A6].
  - Peer anchors on FY27 EV/EBITDA: Siemens Energy 12.6x and Vertiv 19.1x [S1: MarketScreener valuation pages] [S2: stockanalysis.com; facts BX-29/31].
- **Which failure is more likely depends on the horizon.**
  - Through the late-January 2027 FY27 guide (about 4 months), a long loses more often than a short (research judgement ~55/45).
  - Over 12 months, the NTM roll-forward and the spring-2027 Capital Markets Day (CMD) tilt it the other way (~45/55).
- **The "new CFO kitchen-sinks the guide" angle is weaker than the master brief says.** Ken Parks presents through the Q4 call and the 10-K [S1: GEV release 2026-08-27] [S2: CFO Dive 2026-08-28] (via D04).
- **The Sep-14 drop was an AI-sentiment event, not a thesis event.** Anthropic and OpenAI leaders called for an AI slowdown on the same day GLJ initiated [S1: CNBC 2026-09-14] [S2: Recharge 2026-09-14; Motley Fool 2026-09-14]. That sentiment channel is the long's biggest risk and the short's best tailwind.

---

## 2. Failure stories and the ladder

### (a) October 2027: the team pitched LONG and lost

**Most likely chain (stock ~$780–880, −9% to −19%):**
1. **Q3 print (2026-10-28).** It lands near a consensus EBITDA of $1,706M, which sits at the top of the guide-implied range (facts). The CEO had already said H2'26 commitments would run below H1's ~40 GW [LAG p.3; **SINGLE-SOURCE**, D03]. "Peak orders" becomes the story.
2. **Late-January 2027 FY27 guide.** The margin midpoint comes in around 16.5–17.5% vs a Street 18.15%.
   - For the first time, no framework raise cushions it. Both prior first guides came at December events alongside raises (+5.01% and +15.62% reaction days) [S1: D04, corpus price table] [S2: Proactive 2025-12-10; Morningstar 2025-12-10].
   - The Street cuts FY27 to ~$8.8–9.0B and pulls FY28 toward $12B.
3. **Multiple compression.** AI-capex sentiment shocks compress the multiple toward capex-supplier peers. The pattern is the Sep-14 day (−8.6% [S1: Motley Fool] [S2: BX]) and the DeepSeek day (−21.5% [S1: D03, Motley Fool] [S2: BX]).
4. **Outcome.** 21x on ~$10.8B NTM EBITDA ≈ $888; 20x ≈ $847 [computed].

**Why it is plausible today:**
- The stock is at ~2x the S&P on P/E (38.7x vs ~19.2x; brief §2).
- Five drawdowns of 15% or more since the spin, median −24.6%, three of them while the S&P rose [S1: BX] [S2: Nasdaq closes].

**Probability (research judgement):** ~45% that the stock is below $962.49 in Oct-2027; ~25% that it is below $850.

### (b) October 2027: the team pitched SHORT and lost

**Most likely chain (stock ~$1,050–1,200):**
1. **Q3.** The 125 GW target is reached and the $200B backlog is pulled into early 2027 [S1: corpus src:3750 Laguna coverage] [S2: Quartr summary].
2. **January guide.** The margin guide is 17–19% (midpoint 18.0%, −$79M vs consensus on consensus revenue; D04). It reads as in line.
3. **Spring 2027 CMD.** The 2030 outlook comes out and the 2028 plan is raised, matching the pattern at every prior investor event: Dec-24 +4 points, Dec-25 +6 points and +15.6% revenue [S1: REL-4Q25/Dec-25 release] [S2: Reuters 2025-12-09 via D04]. The Street's FY28 is validated.
4. **Outcome.** The +39% NTM roll at 22–25x gives $1,041–1,179 [computed, A6].

**Why it is plausible today:**
- Guidance has never been cut since the spin (facts BR series).
- Pricing is rising at all three OEMs; SRAs are priced ">20%" above backlog [S1: CALL-2Q26] [S2: LG&E/KU plant cost +53–57%, KY PSC 2025-00045].
- 2025 bonus targets were beaten at 130–200% payout [S1: DEF 14A -26-000049] [S2: 10-K -26-000015 actuals] (via D02).
- The stock recovered 106% of the GLJ-day drop in 11 sessions.

**Probability (research judgement):** ~55% over 12 months. It falls to ~45% if the short is closed after the January guide.

### Ladder R1–R14

**R1. What the price requires.**
- Enterprise value is about $247.2B (A1): 25.8x FY27 consensus EBITDA and ~18.9x FY28 consensus.
- To hold $962 in Sep-2027 at a peer-like ~20x, NTM EBITDA must be about $12.2B, i.e. FY28 ≈ $13B. That is the Street's number, 16.6% above plan [MS; REL-4Q25].
- In physical terms: about 20–22 GW of gas shipped in 2027 and 24 GW in 2028.
  - "At least 30 gigawatts" over Q3'26–Q4'27 [S1: CALL-2Q26] [S2: LAG p.4, facts PP-22].
  - Power margin around 22% a year early (D01, computed from MS).

**R2. Consensus vs management's plan.**

| | Revenue | Adj. EBITDA | Margin | Sources |
|---|---|---|---|---|
| Consensus FY27 | $52,740M | $9,574M | 18.15% | [S1: MS] [S2: YF-GLJ, Street $9.45B] |
| Consensus FY28 | $60,500M | $13,064M | 21.6% | [S1: MS] |
| Management 2028 plan | $56B | $11.2B | 20% | [S1: REL-4Q25] [S2: N27] |
| Straight-line FY27 | | $8.59–8.78B | | computed (A3) |

- Consensus FY28 is +16.6% vs the plan.
- Consensus FY27 is 9–11% above the straight line.
- FY27 EPS consensus: $24.85 (MS), $24.78 (FactSet via cnyes), $24.24 (Barchart 2026-08-04). These are close.

**R3. Delivery vs guidance since the spin.**
- **Revenue** beat the first numeric guide by +1.26% (FY24) and +4.30% (FY25).
- **Margin** landed inside the range but below the midpoint both years: 5.83% vs 6.0% and 8.40% vs 8.5%. That is small, about $40–61M.
  - [S1: 10-Q 0001996810-25-000133 non-GAAP table] [S2: 10Q-2Q26 comparative; Dec-24 release] (facts BR-21/23; D03).
- **FCF** beat by +89% and +65%, driven by deposits (facts BR-24).
- The pattern is beats on revenue and cash, not on margin (n=2).

**R4. The sharpest difference from consensus.**
- It is FY28 adjusted EBITDA: $13,064M vs a plan-anchored ~$11.2–11.5B, i.e. −12% to −14%.
- On FY27, the difference is −6% to −9% (research base $8.8B vs $9.57B).
- GLJ's Power gap (18.5% vs a "consensus 20.7%") is worth only ~$0.55–0.62B [S1: YF-GLJ] [S2: brief §5 / facts GLJ-27].
  - GLJ's 18.5% for 2027 sits inside the FY26 Power guide (17–19%) and below Q2'26's 18.82% [S1: REL-2Q26] [S2: 10Q-2Q26 segment table].
  - So GLJ assumes almost no Power expansion in 2027, which looks too bearish.

**R5. Why the market might not know.** This is not an information edge; everything is public.
- It is interpretation and timing: the Street builds past management's "grounded" framework, expecting another raise.
  - CEO: "we don't put it in our external financial outlook until it's proven" [S1: Dec-2025 transcript PDF] [S2: Bastion Fiduciary 2026-01-15] (via D04).
- Management itself signals conservatism, so the gap may be deliberate on the Street's part rather than an error.

**R6. Strongest long argument.**
- The +39% NTM roll-forward plus a record of raising plans at every investor event, with a spring-2027 CMD inside the horizon.
- Power incremental margin was 44.4% from H1'25 to H1'26 [S1: 10Q-2Q26 MD&A] [S2: CALL-2Q26 "+320 bps to 18.8%"] (via D02).
- Competitors are capacity-constrained: Siemens Energy is "sold-out until FY28" [S1: SE CFO deck, src:3179] [S2: src:1699].

**R7. Strongest short argument.**
- FY28 consensus exceeds the plan by $1.86B, and the CEO dates the next margin step to 2029–30 [LAG; MB-LAG].
- The FY27 guide lands without a framework cushion for the first time.
- The multiple carries a large premium to peers: 25.8x vs Siemens Energy 12.6x and Vertiv 19.1x on FY27 EV/EBITDA (facts BX-29/31).

**R8. Evidence quality.**
- The short's estimate evidence is primary but interpretive: straight lines and a CEO quote, not a disclosed split.
- The long's evidence is primary and backward-looking: the raise record and incrementals.
- The consensus EBITDA line is effectively single-vendor on both sides.
- Net: roughly equal quality. The short leans more on inference about the future path, the long more on extrapolating the past.

**R9. The dated event and its pass mark.**
- **Event:** the late-January 2027 FY27 outlook (the date is not yet announced; last year's was 2026-01-28 [REL-4Q25]).
- **Short pass mark:** a margin midpoint ≤17.5% (≥~$340M below consensus on consensus revenue) and the 2028 plan not raised. D04 puts the probability at ~66%.
- **Kill:** low end ≥18%, or implied EBITDA midpoint ≥$9.4B.
- **Interim:** Q3 on 2026-10-28, with consensus EBITDA at $1,706M.

**R10. How much can be lost, on the stock's own history.**
- **Long:** median drawdown −24.6%, maximum −38.3% [S1: BX] [S2: Nasdaq closes].
- **Short:**
  - The 52-week high of $1,195.94 is +24% from here [S1: Motley Fool quote box] [S2: yfinance via P3].
  - A single-day +15.62% happened on a framework raise (D04).
  - The stock recovered 106% of the GLJ-day drop in 11 sessions.

**R11. What the market would pay in Sep-2027.** Consensus path, NTM $12,191M:

| NTM EV/EBITDA | Value | vs $962.49 |
|---|---|---|
| 20x | $950 | −1% |
| 22x | $1,041 | +8% |
| 25x | $1,179 | +22% |

- Plan-path research base, NTM $10,825M: 20x $847 / 23x $969 / 25x $1,050.
- Bear path, NTM $9,875M: 20x $776 (−19%).
- See A6.

**R12. Historical analog.** The 1999–2002 merchant gas boom:
- Plans for 380,000 MW were set against a 750,000 MW base [S1: Fortnightly, June 2002].
- About 46,000 MW was shelved from Nov-2001 [S2: Power Engineering, Sep 2002]; Calpine halted 15,100 MW [NGI 2002-01-21].
- **Lesson:** the bust arrived through the customers' financing and cancellations, not the OEM's reported revenue, and it showed up in orders first.
- For a 12-month GEV view, the relevant channel is sentiment around the customers' capex (the AI debate) plus SRA conversion. SRAs are 54% of GW, a softer commitment than firm orders.
- GE Power 2017–19: not re-researched here (open item).

**R13. The single observation that would flip the view.** The FY27 margin guide at ≥18% low end, or a raise of the 2028 plan. Either would flip the lean to long.

**R14. Confidence:** 2/5.
- The biggest uncertainty is the multiple, driven by AI-capex sentiment, not the estimate gap.
- The estimate gap is small (−6% to −9% on FY27) relative to the +39% roll-forward.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Price at 2026-09-29 close | $962.49 | yfinance quote 2026-09-30 | Motley Fool quote box 2026-09-14 page | exact | H |
| 2 | 2028 plan | $56B, 20%, FCF ≥$24B | REL-4Q25 | N27 (2026-01-23) | exact | H |
| 3 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B | REL-2Q26 | N354 | exact | H |
| 4 | Consensus FY27 EBITDA | $9,574M vs $9.45B | MS 2026-09-29 | YF-GLJ 2026-09-15 | close (−1.3%) | M |
| 5 | Consensus FY27 EPS | $24.85 / $24.78 / $24.24 | MS | FactSet via cnyes; Barchart 2026-08-04 | close | M |
| 6 | Consensus target | $1,237.34 vs $1,145.83 | MS / Yahoo 2026-09-21 | MarketBeat 2026-09-21 | **conflict** (different panels) | M |
| 7 | CEO dates the margin step to '29–'30 | quote | LAG p.10 | MB-LAG src:681 | exact | H |
| 8 | GLJ FY27 view | $7.42B; Power 18.5% vs "20.7%" | YF-GLJ | Motley Fool 2026-09-21 ($470 PT) | close | M (the "20.7%" is single-source) |
| 9 | Margin vs guide midpoint | 5.83/6.0; 8.40/8.5 | 10-Q -25-000133 | 10Q-2Q26; Dec-24 release | exact | H |
| 10 | Sep-14 cause | AI-slowdown call; GEV −8.6% | CNBC 2026-09-14 | Recharge; Motley Fool 2026-09-14 | exact | H |
| 11 | Drawdowns | median −24.6%, max −38.3% | Yahoo chart API | Nasdaq historical | exact | H |
| 12 | Jan-2027 presenter | Parks through Q4 and the 10-K | GEV release 2026-08-27 | CFO Dive 2026-08-28 | exact | H |
| 13 | Peer FY27 EV/EBITDA | SE 12.6x; VRT 19.1x | MarketScreener | stockanalysis.com | close | M |
| 14 | 2001–02 gas bust | 46 GW shelved; Calpine 15.1 GW halted | Power Eng. 2002-09 | NGI 2002-01-21 | consistent | M |
| 15 | H2'26 commitments below H1 | qualitative | LAG p.3 | — **[SINGLE-SOURCE]**; searched corpus and MB-LAG | — | L |

---

## 4. Arithmetic

**A1. Enterprise value.**
- Market cap: 962.49 × 266.33M = $256,340M.
- Less net cash of $9,113M (brief §2, from 10Q-2Q26): EV = $247,227M.

**A2. Current multiples.**
- 247,227 / 9,574 = 25.8x FY27 consensus.
- 247,227 / 13,064 = 18.9x FY28 consensus.
- 247,227 / 8,800 = 28.1x on the research-base FY27.

**A3. Straight-line FY27.**
- (46.0B × 13% = 5,980 + 11,200) / 2 = $8,590M.
- From FY26 consensus: (6,359 + 11,200) / 2 = $8,780M.
- Consensus of $9,574M is +9.0% to +11.5% above these.

**A4. FY27 margin grid on consensus revenue of $52,740M.**

| Margin | FY27 EBITDA |
|---|---|
| 16.5% | $8,702M |
| 17.0% | $8,966M |
| 17.5% | $9,230M |
| 18.0% | $9,493M |

- On $54B revenue, 17.5% gives $9,450M. A revenue beat can erase most of a margin miss.

**A5. Value in Jan-2027 (FY27 frame).** Formula: (multiple × EBITDA + 9,113) / 266.33.

| FY27 EBITDA | Multiple | Value | vs $962.49 |
|---|---|---|---|
| $8,800M | 24x | $827 | −14% |
| $8,800M | 25.8x | $887 | −8% |
| $8,800M | 26x | $893 | −7% |
| $8,000M | 25x | $785 | −18% |
| $8,000M | 22x | $695 | −28% |
| $9,574M | 25.8x | $962 | 0% |
| $9,600M | 27x | $1,007 | +5% |

**A6. Value in Sep-2027.** NTM = 0.25 × FY27 + 0.75 × FY28.

| Path | FY27 / FY28 | NTM EBITDA | Values | Breakeven multiple |
|---|---|---|---|---|
| Consensus | 9,574 / 13,064 | $12,191M | 20x $950; 22x $1,041; 25x $1,179 | 20.3x |
| Research base | 8,800 / 11,500 | $10,825M | 20x $847; 23x $969; 25x $1,050 | 22.8x |
| Bear | 8,000 / 10,500 | $9,875M | 20x $776; 25x $961 | 25.0x |

- The master brief's "$10,794M on management's plan" implicitly uses consensus FY27 ($9,576M) with FY28 at the plan.
- Net cash builds by Sep-2027 (FY27 FCF less buybacks and dividends). That would add roughly $20–28 per share and is not included.

**A7. GLJ's Power gap.**
- (20.7% − 18.5%) × FY27 Power revenue of ~$25–28B = $0.55–0.62B.
- Total gap: 9.45 − 7.42 = $2.03B, leaving $1.41–1.48B unexplained.
- The ~$27B Power revenue comes from FY25 $19,767M × 1.18–1.20 (FY26 guide) × ~1.15. That is research judgement.

**A8. Scenario tree, Sep-2027 (research judgement).**

| Scenario | Probability | Range | Midpoint |
|---|---|---|---|
| Street right | 30% | +8% to +22% | +15% |
| Plan path | 40% | −5% to +11% | +3% |
| Bear / de-rate | 25% | −14% to −27% | −20% |
| Blue sky | 5% | | +35% |

- Expected return ≈ +2.5%.
- P(stock above $962) ≈ 0.30 + 0.22 + 0.05 = 0.57 at 12 months. The 0.22 assumes ~55% of the plan-path outcomes finish above $962.
- At 4 months, with the January guide as the dominant event: ≈ 0.45.

---

## 5. General question bank answers

- **G1 / G4:** see R1. The number that would falsify the market's story is the FY28 EBITDA path. The plan at $11.2B vs the Street at $13.1B is the test.
- **G5:** if the stock goes nowhere for 12 months, consensus NTM EBITDA rises ~39% and the multiple compresses from ~28x to ~20x [A6].
- **G7:** the gap is interpretation and timing, not information (R5).
- **G8:** the FY27 estimate gap (−6% to −9%) is smaller than the NTM roll (+39%). A short needs de-rating.
- **G13:** see R9.
- **G14:** the reveal slips past the horizon if GEV holds a December 2026 event (none listed; D04) or folds FY27 into the CMD.
- **G15:** see R10.
- **G16:** AI-capex sentiment. It is the single largest one-day driver (−21.5% and −8.6%).
- **G17:**
  - Framework timing: the spring CMD.
  - Buybacks: the $6B authorization dates from Dec-2024, via D04; the Dec-2025 release announced an increase.
  - Guidance style: "grounded"; the CEO expects to "do better internally relative to what we commit to you externally" [LAG; earningscalls.dev] (via D04).
- **G19:** see R12.
- **G20:** consensus EBITDA (effectively single vendor); GLJ's "20.7%" (single-source); the H2 commitments remark (single-source).

---

## 6. What would change this

- **FY27 guide midpoint ≥18%, or 2028 plan raised to ≥$12.5B** → the short's estimate leg is dead; the lean flips to long.
- **Q3 (2026-10-28) shows contracted GW growth stalling below the 125 GW path, or SRA conversions falling** → strengthens the long-failure chain; the 12-month lean moves to short.
- **Street FY27 drifts down to ≤$9.0B before January** → the surprise is already priced and the short's catalyst weakens.
- **Another AI-capex shock with peers down ≥15%** → de-rating risk dominates; a long fails regardless of estimates.

---

## 7. Disagreements with the master brief

1. **January presenter.** It is Parks's team, not a new CFO (row 12). The "new-CFO reset" is weaker.
2. **"Never beaten its first margin guide."** The first guides were qualitative and were met. The numeric-midpoint misses were ~$40–61M (D03). The pattern holds but is small.
3. **GLJ's Power 18.5% for FY27** is at or below the current run-rate (Q2'26 at 18.82%). GLJ is too bearish on Power level, not only "right about when".
4. **"At management's plan the stock is about fairly priced."** The brief's $10,794M NTM uses consensus FY27. On a straight-line FY27 the breakeven is 22.8x NTM (A6).
5. **Lean.** I rate it closer to a coin flip. The short is favoured only on a ≤4-month horizon through the January guide; at 12 months there is a slight long edge (P ≈ 0.55–0.57 above entry).
6. **Consensus target** conflicts by panel: $1,237 (MarketScreener) vs $1,146 (MarketBeat). State the source.

---

## 8. Open items

- A second independent FY27/FY28 EBITDA consensus (Visible Alpha, FactSet or LSEG via a broker note).
- GLJ's full note: segment build and the source of "20.7%".
- A second source for the H2'26 commitments remark: the Laguna transcript on earningscalls.dev.
- GE Power 2017–19 de-rating path. Search the corpus for GE 10-K 2018 / 2019 Power segment orders and price history.
- The January 2027 call date and whether a December 2026 event gets added: GEV IR events page.

```FINAL_BLOCK
{"direction": "short",
 "p_long": 0.46,
 "fy27_adj_ebitda_usd_m": {"low": 8000, "base": 8800, "high": 9600},
 "fy28_adj_ebitda_usd_m_base": 11500,
 "one_number": "FY28 adj EBITDA: research base ~$11.5B vs MarketScreener consensus $13,064M (about -12%); FY27 base $8.8B vs $9,574M (-8%)",
 "target_price_range_usd": [827, 893],
 "target_formula": "24-26x FY27 adj EBITDA $8,800M + net cash $9,113M, / 266.33M shares = $827-$893 (Jan-2027 frame)",
 "horizon_months": 4,
 "kill_rule": "Late-Jan 2027 FY27 guide with adj EBITDA margin low end >=18% or implied EBITDA midpoint >=$9.4B, or 2028 framework raised to >=$12.5B EBITDA before the spring-2027 CMD",
 "top_reason": "Consensus FY27-28 EBITDA runs 9-17% above management's own straight-line path and 2028 plan, and the FY27 guide arrives in January without a framework raise to cushion it; the edge is thin and fades beyond ~4 months as the +39% NTM roll-forward and the spring CMD favour the long.",
 "confidence_1_to_5": 2}
```
