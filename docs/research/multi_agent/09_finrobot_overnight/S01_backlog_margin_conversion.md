# Does the disclosed backlog support the Street's FY27 margin step, or only the plan's?

_S01_backlog_margin_conversion — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 09:57:58. Requests 50, input tokens 4595802, output tokens 59018._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV: does the disclosed backlog support the FY26→FY27 margin step the Street needs? Research note, 2026-09-30

Everything here is research input. Any range is a research estimate, and the team picks its own numbers. I have written no memo prose and chosen no forecasts.

**Short answer.** On GEV's own backlog numbers and management's own statements about timing, the order book supports roughly a straight-line step to the 2028 plan. That is slightly below the research base. It does **not** support the Street's step. To reach the Street, 2026 orders that ship in 2027 must already carry close to all of that year's price premium. The CEO says the 2026 premium lands mainly in 2029–30, which contradicts that. This conclusion rests on one uncertain link: how much of the backlog margin actually reaches the income statement. That ratio has ranged from about 0.2x to 1.6x a year (Q10 test 2).

**Source key**
- **K24**: FY24 10-K, 0001996810-25-000011
- **K25**: FY25 10-K, 0001996810-26-000015
- **10Q**: Q2'26 10-Q, 0001996810-26-000148
- **R4Q25**: Q4'25 release, 0001996810-26-000012 EX-99
- **T4Q25**: Q4'25 call, 2026-01-28. Corpus copy is src:2660 (chunks 246126–246128 and 246150). The GEV-hosted PDF gev_webcast_transcript_01282026.pdf was verified in earlier work (evidence_lanes PP-08/09/10, PMX-26/27).
- **FOOL**: Motley Fool Q4'25 transcript, fool.com/earnings/call-transcripts/2026/01/28/…
- **D4Q25**: Q4'25 deck slide 5 (gev_webcast_presentation_01282026.pdf), footnote b (evidence_lanes PMX-25)
- **D4Q24**: Q4'24 deck, p.6 and slide 25 "Adjusted equipment backlog" (PMX-25/29)
- **T4Q24**: Q4'24 call, 2025-01-22, roic.ai/quote/GEV/transcripts/2024-year/4-quarter
- **BOFA**: BofA Global Industrials transcript, 2026-03-18, earningscalls.dev. **BOFA-MS**: the MarketScreener transcript listing for the same event (paywalled; only title and date seen).
- **T1Q26**: Q1'26 call, 2026-04-22 (corpus src:3771, chunk 468309)
- **T2Q26**: Q2'26 call, 2026-07-22 (corpus src:3161)
- **LAG**: GEV-hosted Morgan Stanley Laguna transcript PDF, 2026-09-16 (verified earlier: evidence_lanes PP-04/05/06, POS-16/17). **MB-LAG**: MarketBeat write-up of Laguna (corpus src:681).
- **TP1**: trade press on the Q1'26 call (corpus chunk 217417). **TP2**: trade press on the Q2'25 call (chunk 236376). **X-SM**: Simon Mahan post on X (chunk 217497).
- **VM**: vintage_model_output.txt. **EL**: evidence_lanes_full.md. **D01A**: D01_fy27_build_A.md.

---

## 1. Bottom line

- **The backlog measure is a contribution margin, and no SEC filing defines it.** GEV defines "margin expansion" as the "increase or decrease in the average estimated contribution margin in backlog compared to prior year." It is a cost-as-known estimate and excludes future productivity.
  - Company increments: +7 / +5 / +6 pts (FY23/24/25). Power: +3 / +3 / +11. Power's YE22 starting point was "approximately breakeven." Dollars added: ">$6B" over 2023–24, "$8B" in 2025, and "at least $8B" in 2026.
  - [S1: D4Q25 slide 5 fn b; T4Q25 chunk 246127] [S2: R4Q25 "grew equipment margin in backlog by $8B, with 6 pts"; BOFA "in '24… 5 points. In '25… 6 points"]
- **Order-vintage margins backed out from these disclosures (points above each YE22 base) [computed]:**
  - Company: 2023 orders ≈ +9.6; 2024 ≈ +13.7 to +15.5; 2025 ≈ +20.3 to +21.6; 2026 ≈ +26 to +35 (depends on assumptions).
  - Power: 2023 ≈ +5.2 to +5.9; 2024 ≈ +5.5 to +7.5; 2025 ≈ +19.3 to +20.4; 2026 ≈ +34 to +40.
  - Inputs: [K24 and K25 RPO tables; D4Q24 slide 25 EDF adjustment; LAG p.5 "larger than… low double digits"]
- **Change in equipment contribution margin, FY26→FY27, weighting each vintage by the RPO conversion schedule [computed]:**
  - Under management's timing (2026 orders shipping in 2027 carry roughly 2025-vintage margins): company **+1.4 to +2.6 pts, $0.37–0.69B**; Power **+2.6 to +3.3 pts, $0.33–0.42B**.
  - If the full 2026 premium also lands in FY27: company +5.0 to +5.8 pts ($1.34–1.55B); Power +8.5 pts ($1.07B).
- **What each case needs:**
  - The research base's margin-rate gain (Power +688, Electrification +262 = **$950M**) needs 2026-vintage revenue in FY27 at about +25 to +26 pts. That is about one-third of the 2026 premium.
  - The Street (margin-rate gain of **$1,336–1,606M**) needs +31 to +36 pts (company) or +34 to +40 pts (Power). That is the *entire* estimated 2026 premium, on every 2026 dollar shipped in FY27. [computed §4]
- **Management's timing contradicts that requirement:**
  - 2025 margin reaches the income statement "starting 2 to 3 years from now, so call it '27, '28 and some… '29 and '30" [S1: BOFA #4] [S2: BOFA-MS listing, title only → effectively SINGLE-SOURCE on text].
  - The 2026 change "tells you the equipment margins for '29 and '30, largely" [S1: LAG p.10] [S2: EL PP-06 verification of the same PDF → SINGLE primary document].
  - Heavy-duty lead time is about 3 years [S1: TP1] [S2: X-SM / TP2, "2026 and 2027 largely sold out" as of July 2025].
- **The pass-through from backlog to the income statement is unstable, and the conclusion depends on it:**
  - Reported equipment gross-margin change divided by the change in vintage-weighted contribution points: FY24 ≈ 1.1–1.6x; FY25 ≈ 0.95–1.06x; H1'26 vs FY25 ≈ 0.2–0.35x.
  - For Power, the derived equipment EBITDA margin rose about +9 to +13 pts a year in FY24–25, several times the backlog arithmetic.
  - So non-backlog levers (execution, absorption, legacy losses running off) have at times been larger than the backlog effect. [S1: 10Q income statement; K25 via facts PMX-22] [S2: EL E01/D06 split, a derived and circular series per R01 #3]

---

## 2. Answers

### Q1. Every dated quantified "margin in backlog" statement found

| Date / venue | Speaker | Statement (verbatim, ≤40 words) | Figure | S1 | S2 |
|---|---|---|---|---|---|
| 2025-01-22, Q4'24 call | Strazik | "Over the past two years, we have added more than $6 billion of margin to our equipment backlog… as this backlog has grown over 50% to $43 billion." | 2023+24: >$6B | T4Q24 (roic.ai) | T1Q26 "the $6 billion margin growth in equipment backlog the prior 2 years" (chunk 468309) |
| 2025-01-22, Q4'24 deck p.6 | slide | Change in average contribution margin: Power +3 (FY23), +3 (FY24); company +7 / +5; Electrification +5 / +4; Wind +9 / +3 | pts | D4Q24 p.6 (EL PMX-25) | D4Q25 slide 5 repeats FY23/FY24 |
| 2025-03-28, proxy letter | shareholder letter | "grew our already healthy backlog to $119 billion while also expanding margins in the backlog" | qualitative | DEF 14A 0001996810-25-000049 (chunk 56977) | 424B3 -25-000052 (chunk 57172) |
| 2025 Q3 release (2025-10-22), Q2'26 release | Parks | "healthy equipment margin in backlog" | qualitative | 8-K -25-000159 (chunk 38446) | 10Q-era release -26-000147 (chunk 5623) |
| Dec-2024 / Dec-2025 investor updates | — | **No quantified backlog-margin statement found.** The Dec-25 Q&A says "orders we're taking today. We're shipping in '29 or '30. You'll like the equipment margins" (speaker and date not tagged) | — | corpus chunk 246346 (web copy) | not found. Searched: corpus "Investor Update" / "backlog margin(s)"; Exa for the Dec-25 transcript |
| 2026-01-28, Q4'25 release | Parks | "equipment margin in backlog expanding six points year-over-year"; bullet: "grew equipment margin in backlog by $8B, with 6 pts of accretion" | +6 pts; $8B | R4Q25 (chunk 30112) | FOOL; T4Q25 |
| 2026-01-28, Q4'25 deck slide 5 | slide | Power +11 (FY25); company +6; Electrification +3; Wind (2). Footnote b defines the measure | pts | D4Q25 (EL PMX-25) | T4Q25 chunk 246127 "11 points of growth in Power" |
| 2026-01-28, Q4'25 call (prepared) | Strazik | "adding $8 billion in equipment backlog margin dollars in '25, more than the prior 2 years combined… an incremental 6 points… This included 11 points of growth in Power" | $8B; +6; Power +11 | T4Q25 chunk 246127 | FOOL (same quote) |
| same | Strazik | "those 4 years will add at least $22 billion in equipment margin" ('23 to '26) | ≥$22B | T4Q25 chunk 246128 | trade press chunk 217531 |
| same, Q&A | Coe / Strazik | Coe: "17 points of improvement since year-end '22? The starting point would have been about a breakeven." Strazik: "directionally, the starting point is approximately breakeven… at least $8 billion, this year" | Power +17 from ~0; 2026 ≥$8B | T4Q25 chunk 246150 | GEV PDF p.12 (EL PP-10) |
| 2026-03-18, BofA | Strazik | "in '24, we accreted equipment margin by 5 points. In '25… 6 points… $8 billion… will come through to the P&L over really starting 2 to 3 years from now, so call it '27, '28" | 5 / 6 pts; $8B; timing | BOFA #4 | BOFA-MS listing (text not visible) → **[SINGLE-SOURCE on text]** |
| same | Strazik | SRAs "10 to 20 points higher in price than what's already in backlog… driving the incremental at least $8 billion" | 2026 driver | BOFA #6 | T4Q25 ("another 10 to 20 points of pricing strength", per brief §6) |
| 2026-04-22, Q1'26 call | Strazik | "$6 billion margin growth in equipment backlog the prior 2 years will be at least sequentially as large this year… a floor with an opportunity for it to be substantially higher" | ≥ floor | T1Q26 chunk 468309 | T4Q25 chunk 246150 (≥$8B) |
| 2026-09-16, Laguna | Strazik | "we expect the change in margin in backlog in '26 to be larger than… '25, and the change… in '25 was low double digits" (Power) | Power 2026 >11 | LAG p.5 | EL PP-04 (verified PDF) → **[SINGLE primary]**. MB-LAG covers Laguna, but this line was not re-checked there |
| same | Strazik | Electrification: "Last year, it was three points. It'll probably be something similar… maybe a little bit larger." Wind "healthy positive" | Electrification ~3+ | LAG p.5 | EL PP-05 → **[SINGLE primary]** |
| same | Strazik | "that really tells you the equipment margins for '29 and '30, largely" | timing | LAG p.10 | EL PP-06 → **[SINGLE primary]** |

**Consistency check [computed]:** $22B ≥ (>$6B for 2023–24) + $8B (2025) + ≥$8B (2026). This ties, and it confirms that the ">$6B over two years" refers to 2023–24.

### Q2. What the measure is, and how its level compares with reported margins

**Definition.**
- It is the "average estimated contribution margin in backlog," change versus the prior year, for equipment only [S1: D4Q25 fn b] [S2: T4Q25 "equipment backlog margin dollars"].
- Services backlog margin is discussed separately and only qualitatively [T4Q25 chunk 246150, Parks].
- It is a cost-as-known estimate. The CEO refers to "variable cost productivity not embedded in our backlog margins today" [S1: T4Q25 chunk 246128] [S2: EL PMX-28, GEV PDF].
- **No SEC filing defines it.** The term is absent from both 10-Ks (vintage_verification #15). This session's corpus hits were releases, calls and the proxy only.
- GEV does not say which costs count as variable, so fixed manufacturing overhead, D&A, SG&A, R&D and warranty treatment are **not disclosed**.

**Implied levels.** Two readings of the dollar statements fit the data:
- **(a) Stock reading.** "$ added" = change in (equipment RPO × average margin). With m24 = m25 − 6:
  - 8,000 = 64,245·m25 − 43,047·(m25 − 6%) → **m24 ≈ 19.6%, m25 ≈ 25.6%**.
  - Back-cast: m22 ≈ 7.6% on the EDF-adjusted $28,131M. That gives 2023–24 dollars added of $6.29B, consistent with ">$6B".
  - Rounding sensitivity (±$0.5B, ±0.5 pt): m25 ≈ 21.7–28.9%.
- **(b) Flow reading.** "$ added" = margin on the year's orders:
  - 2025: $8B / $42.1B of orders = 19.0%. 2023–24: >$6B / $52.1B = >11.5%.
  - Against the vintage points above, this implies a company base of about −1 to −2%, i.e. near breakeven like Power. That puts YE25 at about **16.5%**.
- Both readings fit. The data do not identify which one GEV uses.

**Against reported company equipment gross margin (GAAP; after D&A and fixed factory cost):**
- FY23 −2.4%, FY24 5.1%, FY25 10.4% (13.4% before the $637M Offshore Wind charge).
- H1'25 10.0%, **H1'26 11.8%** (11,713 − 10,328), Q2'26 13.1% (6,459 − 5,613).
- [S1: 10Q income statement] [S2: facts PMX-22 / K25 p.38; offshore charge from K25 revenue-recognition note]
- **The gap:** backlog contribution level 16–29% vs gross margin 11–13%, i.e. about 4–17 pts. GEV never reconciles the two. [computed]

**Power.**
- Backlog level YE25 ≈ **+17 pts** from a "breakeven" base [T4Q25 chunk 246150; D4Q25].
- Reported Power segment EBITDA margin (equipment and services combined): 14.68% FY25, 17.63% H1'26 [S1: 10Q Note 24] [S2: Q2 release].
- Derived Power equipment EBITDA margin: FY25 −8.5% to −4.8%; H1'26 0% to +3.6% [EL E01/D06; circular per R01 #3].
- So Power equipment EBITDA runs about 13–25 pts below the backlog contribution level. That is consistent with a large fixed-cost layer; the size of that layer is **not disclosed**.

### Q3. Each order vintage's own margin

**Method (pro-rata).** The old book runs off at its average margin:

v_t = [RPO_t·(L_{t−1}+Δ_t) − (RPO_{t−1} − Rev_t)·L_{t−1}] / [RPO_t − (RPO_{t−1} − Rev_t)]

where L is the average level in points above the base.
- **FIFO variant:** shipments draw from the oldest vintages first.
- **Curve variant:** the old book converts only its disclosed one-year percentage.

**Company.** The EDF-adjusted base is confirmed by Strazik's "grown over 50% to $43 billion": 43,047 / 28,131 = +53%, whereas the unadjusted +35% would not be "over 50%".

| Vintage | Pro-rata | FIFO | Curve variant | Inputs |
|---|---|---|---|---|
| 2023 | 9.57 | 9.57 | — | RPO22 adj 28,131; RPO23 adj 36,770; Rev23 18,258; Δ +7 |
| 2024 | 15.53 | 13.72 | — | RPO24 43,047; Rev24 18,952; Δ +5 |
| 2025 | 21.15 | 20.25 | 21.60 (old book converts 44%) | RPO25 64,245; Rev25 20,934; Δ +6 |
| 2026 | **26.4 / 28.1 / 31.4 / 34.8** for Δ26 = +5 / +6 / +8 / +10 | similar | — | RPO26 assumed $100B (team's choice); 2026 draw 23,771 |

**Power.** 2023–25 are from EL PMX-29 (corrected); 2026 is new.

| Vintage | Central | Range | Inputs |
|---|---|---|---|
| 2023 | 5.2 | 5.2–5.9 | adj RPO22 9,808, RPO23 9,928; Rev23 5,598; Δ +3 |
| 2024 | 7.5 | 5.5 (FIFO) – 7.6 | RPO24 12,461; Rev24 5,708; Δ +3 |
| 2025 | 20.4 | 19.3 (FIFO) – 20.4 | RPO25 24,707; Rev25 6,686; Δ +11 |
| 2026 | **~35–37** | **34–40** | Old book 15,565 (= 24,707 − 37% conversion) at 17; YE26 Power RPO 40–50B (6/30/26 already $39,261M); Δ26 = +12 to +15 (">11", LAG) |

**Independent price check on the 2026 Power vintage.** A price increase of p on unchanged cost moves margin to 1 − (1−m)/(1+p). Starting from about 20–25% (the 2025 vintage, and Q4'25 orders) with p = 20% (">20% above 4Q'25", T2Q26 chunk 251590), the result is **33.7–37.5%**. That agrees with 34–40 [computed].

**Unknowns that drive the ranges:**
- Rounding of the disclosed increments (±0.5 pt).
- Conversion order (pro-rata vs FIFO).
- The Power runoff curve, which borrows the blended curve (VM hole 1).
- YE26 RPO, including Prolec's acquired backlog, which enters RPO without being an order.
- FX and cancellations.

### Q4. FY26 and FY27 equipment margin by vintage (points above base)

**Company, organic (ex-Prolec).** FY26 revenue from the book is 23,771 (= 64,245 × 37%): pre-2025 10,762 (= 43,047 × 25%) and 2025-vintage 13,009. FY27 organic equipment revenue is taken as **$26,900M** (team's choice: VM central 30,325 less about 3.4B Prolec). Of that, 20,558 comes from the YE25 book (= 64,245 × (69 − 37)%) and **6,342 (23.6%) from 2026-or-later orders**.

| Case | FY26 pts | FY27 composition (pts) | FY27 pts | Δ pts | Δ$ on 26,900 |
|---|---|---|---|---|---|
| Low (pre-2025 heavy, FIFO, X = 21) | 17.3 | 5,682 @12; 14,876 @20.25; 6,342 @21 | 18.68 | +1.4 | **$0.37B** |
| Management timing (X = v25 21.2) | 17.3 | 4,133 @12.5; 16,425 @21.2; 6,342 @21.2 | 19.86 | +2.6 | **$0.69B** |
| Partial 2026 premium (X = 28) | 17.3 | same, X = 28 | 21.47 | +4.2 | $1.12B |
| Full 2026 premium (X = 31.4–34.8) | 17.3 | same | 22.27–23.07 | +5.0 to +5.8 | $1.34–1.55B |

FY26 is (10,762×12 + 13,009×21.6)/23,771 = 17.25 pro-rata, or 17.29 FIFO.

**Power.** FY26 equipment revenue is $9,774M (D01A §4). From the book: 9,142 (= 24,707 × 37%, borrowed curve), of which pre-2025 is 3,115 (= 12,461 × 25%). FY27 Power equipment revenue is **$12,680M** (D01A base). From the YE25 book: 7,906, of which pre-2025 is 748–1,645 (VM). So **2026-or-later orders supply 4,774 (37.6%)**.

| Case | FY26 pts | FY27 pts | Δ pts | Δ$ on 12,680 |
|---|---|---|---|---|
| Low (FIFO, pre-2025 1,645 @5.5, others @19.3) | 14.90 | 17.51 | +2.6 | **$331M** |
| Management timing (pre 1,200 @6.5; 2025 6,706 @20.4; X = 20.4) | 15.81 | 19.08 | +3.3 | **$415M** |
| Research-base requirement (X = 26.1) | 15.81 | 21.24 | +5.4 | $688M |
| Full 2026 premium (X = 37) | 16.88 | 25.33 | +8.5 | $1,071M |

**Sensitivity.** Each −5 pts on the 2025-vintage slice shipping in FY27 lowers FY27 Power by 6,706 × 5 / 12,680 = **−2.6 pts (−$335M)**. This matters because the 2025 orders shipping in 2027 are likely the shorter-cycle, less re-priced part of that vintage (Q6).

### Q5. Comparison with the research base, the Street and GLJ

**FY26→FY27 margin-rate dollars (excluding the volume effect at the FY26 margin):**

| | Power | Company (Power + Electrification, Wind excluded) | Implied X (2026-vintage pts in FY27) |
|---|---|---|---|
| GLJ (Power 18.5% vs 18.0% FY26 guide mid, on 27,503) | ~$138M | n/a | < v25 |
| **Backlog, management timing** | **$331–415M** | **$0.37–0.69B** | ≈ v25 (~20–21) |
| Research base (D01A §4) | $688M | $950M | Power 26.1 / company 25.3 |
| **Street** (MS +3,215 or FactSet +2,945, less research volume 1,211 and Wind 400) | +386 to +656 above base (if all in Power) | **$1,336–1,606M** | Power **34–40** / company **31.4–35.6** |

**Finding.**
- The backlog arithmetic, under management's own stated timing, supports a step **between GLJ and the research base**. It is closest to management's straight-line path: FY27 ≈ 16.5% × ~51–52.7B = $8.4–8.7B.
- **It does not support the Street.** The Street's bridge needs the 2026 vintage's full estimated premium on about 24–38% of FY27 equipment revenue, with no help from services. That contradicts "'29 and '30, largely" (LAG) and "'27, '28" for 2025 margins (BOFA).
- **The Street is reachable only through non-backlog levers** worth about $0.65–1.0B in Power (Street) or $0.27–0.36B (research base). These are productivity outside the backlog, absorption at 20→24 GW, and services pricing.
- **History of non-backlog levers [computed, low confidence].** Power segment margin-rate $ minus backlog $: FY24 ≈ 471 − (80 to 171) = **+$0.30–0.39B**; FY25 ≈ 435 − (200 to 261) = **+$0.17–0.24B**; FY26 guide ≈ 780 − (938 to 1,026) = **−$0.16 to −0.25B**.
  - So the research base's residual is within the historical range; the Street's is above anything seen.
- **GLJ correction.** The task text says the re-weighting closes "$0.6–1.3B" of GLJ's gap. That figure was superseded: the consistent ceiling is **$0.55–0.62B** (GLJ reaches $7.97–8.04B) [S1: EL line ~39920, "(3)"] [S2: master brief §5].
  - Rerun GLJ's increments-as-levels (pre-2025 at 3, 2025 at 10.5) through the Power shares (pre-2025 6–16%, 2025 49–56%, 2026+ ~38%). The result is a FY27 Power equipment level of about 10 pts, against 19 pts with the corrected vintage levels. GLJ's level is too low. But its implied *step* (+$0.14B) and the management-timing step (+$0.33–0.42B) differ by only about $0.2–0.3B.

### Q6. Timing by product

**Heavy-duty/HA gas**
- July 2025: "Sitting here today, 2026 and 2027 are largely sold out… approaching filling out '28" [S1: TP2 chunk 236376] [S2: X-SM chunk 217497]. Both report the Q2'25 call; primary transcript not opened.
- Q1'26: lead times "about three years"; about 10 GW left across 2029–30 [S1: TP1 chunk 217417] [S2: none found → **SINGLE-SOURCE**].
- 2032 slots sold only in single-digit GW [LAG, EL POS-18; SINGLE primary].
- **Timing statements have shifted one year out:**
  - Jan-2025: "won't begin delivering on the majority of the high-margin orders of 2023 and 2024 until 2026 and beyond" [S1: T4Q24] [S2: none].
  - Jan-2026: "the majority of the higher-margin orders placed in '24 and '25 until '27 and beyond" [S1: T4Q25 chunk 246127] [S2: EL PMX-27, GEV PDF].
  - This is a finding: the delivery window for the same 2024 vintage moved from 2026 to 2027.
- 2025 margin → "'27, '28 and some… '29 and '30" [BOFA]. 2026 → "'29 and '30, largely" [LAG].

**Aeroderivative**
- SRA-to-order conversion takes "6 to 18 months" [BOFA #8; SINGLE].
- H1'26 orders skewed to aero, with a higher $/kW [T2Q26 chunk 251590; 10Q unit table (16 aero of 29 units in Q2)].
- An aero delivery lead time was **not found**.

**Electrification (transformers, switchgear, HVDC)**
- Slowest converter: 36.9% of the YE24 book converted in 2025, against 53.7% for Power and 67.6% for Wind [S1: VM segment check using K24/K25 segment RPO] [S2: K25 segment RPO tables].
- Product-level lead times (transformers, HVDC) **not found** in this session. Look in the Dec-25 investor deck and Hitachi Energy / Siemens Energy grid decks.

**Wind**
- "70% of 2025 equipment orders were in the second half and will be delivered in the second half of 2026" [S1: T2Q26 chunk 251605] [S2: none → SINGLE]. Roughly a one-year cycle.

**Capacity**
- "70 to 80 heavy-duty gas turbines per year beginning in the second half of 2026, up from 48"; "approximately 20 gigawatts annually starting in 2027" [S1: T4Q24] [S2: brief §3 / Q2 release (20 GW run-rate from Q3'26; 24 GW in 2028)].

### Q7. What sits between backlog margin and reported EBITDA margin

- **Tariffs:** $100–200M in 2026, down from $250–350M guided at Q1; FY25 about $250M [S1: 10Q MD&A] [S2: 1Q26 10-Q via facts RQ-01].
- **Capacity and R&D cost in Power:** the Q2 Power margin moved "more than offsetting inflation, as well as additional expenses to support capacity investments at Gas along with R&D" [S1: T2Q26 chunk 251602] [S2: Q2 release driver text, per D01A]. No dollar figure is disclosed. **Under-absorption cost: not disclosed.**
- **R&D plus capex:** "at least $11 billion" over 2025–28 [S1: BOFA #2] [S2: T4Q25 ">$2 billion in R&D and CapEx" in 2025 (partial)].
- **G&A:** "$600 million G&A cost reduction target by 2028", a tailwind [S1: T2Q26 chunk 251607] [S2: none found → SINGLE].
- **CSA profitability revisions:** −$151M FY25, −$218M H1'26 [S1: 10Q Note 9] [S2: K25 Note 9, via D01A].
- **Wind:** FY26 about −$400M; the 2028 margin target was cut from 10% to 6%. Wind then missed the FY25 cut guide (−$598M actual vs about −$400M) [S1: T2Q26 chunk 251607] [S2: R4Q25 / K25 p.72].
- **Prolec:** loss before tax of −$166M from acquisition to 6/30/26 "includes the impact of inventory step-up amortization, intangible asset amortization, and integration costs" [S1: 10Q Note (acquisitions), p.14] [S2: none]. The step-up amount, and whether adjusted EBITDA excludes it, were **not found**.
- **Productivity outside the backlog** (an upside offset): "not embedded in our backlog margins today" [T4Q25 chunk 246128; EL PMX-28].
- **Warranty:** no figure found in this session.

### Q8. What management has said about the shape of the path

- **The only shape statement found:** "enough of that cutting in, in '27 and '28 to drive that shift from 8.5% to 20% at the company level" [S1: BOFA #4] [S2: text SINGLE]. It frames 2027–28 together and says nothing about linearity.
- **2026:** "more second-half weighted than 2025" [S1: T2Q26 chunk 251607] [S2: brief §4, H1 10.5% vs 12–14% guide].
- **No statement found** calling the path linear, back-half weighted or accelerating for 2027–28.
- **FY27-specific statements:**
  - "at least 30 GW" shipped over Q3'26–Q4'27 [T2Q26; D01A].
  - "In '27, we expect our combined gigawatts under contract to continue to grow" [T2Q26 chunk 251590].
  - $200B backlog "very early in 2027" [LAG, EL POS-18].
  - Wind "materially better in 2027" [MB-LAG; LAG].
  - FY27 outlook due on the January call [LAG; chunk 468154].
- **No FY27 margin, FCF or capex guidance exists.**

### Q9. Over-time vs point-in-time recognition

- **Over time (percentage of completion, cost-to-cost):** "customized goods including power generation equipment and long-term construction contracts" [S1: K25 revenue-recognition policy, p.44–45].
- **Point in time:** "non-customized equipment and other goods we manufacture on a standardized basis… generally no earlier than when the customer has physical possession" [S1: K25 p.45] [S2: VM hole 6, quoting the 10-K]. The same policy wording was not found verbatim in K24 → treat as **[SINGLE document]**.
- **Split: not disclosed.**
- **Mechanism:**
  - On over-time contracts, a vintage's margin reaches the income statement as costs are incurred, i.e. during manufacturing. That is ahead of shipment, so HA units shipping in 2029 start booking revenue and margin in 2027–28.
  - Estimate changes are recognised immediately as cumulative catch-up; Offshore Wind losses show the downside: $379M / $1,005M / $637M in FY23–25 [K25 p.44].
  - This is the main reason the RPO dollar curve, which is built on revenue recognition, and "ship year" (GLJ, and the CEO's "'29-'30") can disagree. The RPO curve already reflects over-time recognition. The CEO's year language may refer to deliveries.

### Q10. Three hand-checkable tests for the model

1. **Required-X test (Power and company).**
   - Formula: X_req = [Rev27 × (L26 + ΔL_needed) − pre × v_pre − s25 × v25] / s26.
   - Inputs: Q4 table plus the team's FY27 revenue; ΔL_needed = (bridge margin-rate $) / Rev27.
   - Readings: X_req ≤ ~21 means the 2025 vintage alone covers it. X_req about 25–28 needs part of the 2026 premium (research base). X_req ≥ 34 needs the whole 2026 premium in 2027, against the CEO's "'29–'30" (Street).
2. **Pass-through calibration.**
   - Formula: k = Δ(reported GAAP equipment GM) / Δ(vintage-weighted points).
   - History: FY24 +7.5 / (4.6–7.0) = 1.07–1.63; FY25 +5.3 / (5.0–5.6) = 0.95–1.06; H1'26 vs FY25 +1.4 / (5.3–7.1) = 0.20–0.26.
   - Update with the Q3'26 10-Q (10-28) and the FY26 10-K.
   - Readings: FY26 k back near 1 favours the Street's pace; k < 0.5 favours the research base or below.
3. **RPO-share test on the January disclosure.**
   - YE26 10-K Note 9: FY27 book slice = RPO26 × 1-yr%, split into pre-2026 (= 64,245 × 32% = 20,558) and 2026 orders.
   - If the 2026-order share of FY27 equipment revenue is ≤ ~25%, the Street's X_req rises above 35 (harder). If it is ≥ 40%, the required X falls toward 28.
   - Also compare the Power change in backlog margin against ">11" (LAG). A large number bears on 2029–30, not FY27 (CEO).

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Company equipment RPO | YE22 31,902; YE23 40,478; YE24 43,047 | K24 MD&A RPO table | K25 comparatives / VM step 5 | exact | H |
| 2 | Equipment RPO YE25 / 6/30/26 and conversion | 64,245 (37/69/97); 87,821 (36/65/97) | 10Q MD&A and Note 9 | K25 Note 9 via VM | exact | H |
| 3 | EDF equipment RPO removed | 3,771 (YE22), 3,708 (YE23) | D4Q24 slide 25 (EL PMX-29) | K24 "~$3.9B… sale… to EDF" | close | M |
| 4 | Power equipment RPO | 12,461 / 24,707 / 39,261 (6/30/26) | K25 p.26; 10Q MD&A | K24 p.38; VM | exact | H |
| 5 | Company increments | +7 / +5 / +6 | D4Q25 slide 5 | BOFA (5, 6) | exact | H |
| 6 | Power increments / base | +3 / +3 / +11; ~0 at YE22 | D4Q25 | T4Q25 chunk 246150 | exact | H |
| 7 | Dollars added | >$6B (23–24); $8B (25); ≥$8B (26); ≥$22B (23–26) | T4Q24; T4Q25 | R4Q25; T1Q26; FOOL | exact | H |
| 8 | Measure = average contribution margin | fn b | D4Q25 | EL PMX-25 verification (same deck) | exact | M (one primary doc) |
| 9 | Power 2026 change > 2025 | >11 | LAG p.5 | EL PP-04 | [SINGLE primary] | M |
| 10 | Timing: 2025 margin → '27–'28 | quote | BOFA #4 | — | [SINGLE-SOURCE] | M |
| 11 | Timing: 2026 → '29–'30 | quote | LAG p.10 | EL PP-06 | [SINGLE primary] | M |
| 12 | Timing: 2024 orders "'26 and beyond" (Jan-25) → "'27 and beyond" (Jan-26) | quotes | T4Q24 | T4Q25 chunk 246127 / FOOL | shift = finding | M |
| 13 | Equipment GM | H1'26 11.82%; H1'25 10.01%; Q2'26 13.10% | 10Q income statement | facts PMX-22 | exact | H |
| 14 | Pricing +20% vs 4Q'25 | quote | T2Q26 chunk 251590 | TP1 ("10 to 20 points") | close (different bases) | M |
| 15 | HD lead time ~3 yrs; '26–'27 sold out (Jul-25) | quotes | TP1; TP2 | X-SM | close | M |
| 16 | Recognition policy | over time vs point in time | K25 p.44–45 | VM hole 6 | exact | M |
| 17 | Tariffs 2026 | $100–200M | 10Q MD&A | 1Q26 10-Q (RQ-01) | close | H |
| 18 | Consensus FY27 EBITDA | 9,574 (MS) / 9,339 (FactSet via Boursorama) | MS (facts CT-02) | task brief (Boursorama; not re-verified) | conflict −2.5% = vendor dispersion | M |
| 19 | Research base bridge | +2,559 (Power margin +688, Electrification +262) | D01A §4 | F01 Q1 | exact | H (internal) |

---

## 4. Arithmetic (all [computed])

**A. Company levels (stock reading).**
- m24 = (8,000 − 64,245 × 0.06) / (64,245 − 43,047) = 4,145 / 21,198 = 19.56%. So m25 = 25.56%, m23 = 14.56%, m22 = 7.56%.
- Check: 43,047 × 0.1956 − 28,131 × 0.0756 = 8,420 − 2,127 = **6,293** (> $6B ✓).

**B. Vintages.** Company pro-rata:
- v23 = 36,770 × 7 / 26,897 = 9.57
- v24 = (516,564 − 17,818 × 7) / 25,229 = 15.53
- v25 = (1,156,410 − 22,113 × 12) / 42,132 = 21.15
- FIFO: v24 = (516,564 − 17,818 × 9.57) / 25,229 = 13.72; v25 = (1,156,410 − 22,113 × 13.72) / 42,132 = 20.25.
- Company 2026 (RPO26 = 100,000; old book 40,474 @18): v26 = (100,000 × (18 + Δ) − 728,532) / 59,526.
- Power 2026: v26 = (RPO26 × (17 + Δ) − 15,565 × 17) / (RPO26 − 15,565). For example 45,000 at Δ12 gives **35.3**.

**C. FY26 / FY27 weights.** As in the Q4 tables. For example, Power under management timing: (1,200 × 6.5 + 6,706 × 20.4 + 4,774 × 20.4) / 12,680 = 241,992 / 12,680 = 19.08.

**D. Street margin-rate requirement.**
- 3,215 − 694 − 517 − 400 = **1,604**. FactSet: 2,945 − 1,611 = **1,334**.
- Power X_req = (12,680 × (15.81 + 5.43 + 3.04 to 5.17) − 144,602) / 4,774 = **34.2–39.9**.
- Company X_req = (26,900 × (17.3 + 4.97 to 5.97) − 399,873) / 6,342 = **31.4–35.6**.

**E. Straight line to 2028.**
- FY26 guide mid 13% → 20% in FY28 gives a FY27 margin of 16.5%.
- On (46.0 + 56.0) / 2 = $51.0B of revenue that is $8.42B; on $52.74B it is $8.70B.
- Increment from 5,980 (13% × 46.0): **+$2.44B**, against research +2.56 and Street +2.95 to +3.22.

**F. Pass-through ratio k.** As in Q10 test 2.
- Predicted company points: FY24 4.58–7; FY25 10.19–12; FY26 17.3.
- FY24 FIFO = 9,079 × 9.57 / 18,952 = 4.58. FY25 FIFO = (17,818 × 9.57 + 3,116 × 13.72) / 20,934 = 10.19.

---

## 5. General question bank

- **G2:** The Street's FY27 needs 2026-vintage pricing in 2027. Before FY26, GEV's equipment gross margin never lagged the backlog arithmetic, but in H1'26 it did (k ≈ 0.2–0.35) [§4F].
- **G7:** This is interpretation plus timing, not new information. All inputs are public every January and quarter [EL Test 7].
- **G12:** Percentage of completion pulls a vintage's margin forward to the manufacturing period (Q9). That is a partial counter to "'29–'30".
- **G13 / G22:** YE26 RPO conversion percentages and the backlog-margin page arrive in late January alongside the FY27 guide. The Q3 10-Q equipment GM (10-28) gives an early k reading.
- **G20:** Traps are contribution vs gross vs EBITDA margin; the stock vs flow reading of "$ added"; EDF-adjusted vs reported RPO; segment-note vs MD&A Power equipment revenue (3,834 vs 3,851).
- **G21:** If this research is wrong, FY26 k should rebound toward 1: Q3'26 equipment GM ≥ ~14.5% with Wind excluded, or Q4 on a similar basis.

## 6. What would change this

- **FY26 k ≥ ~0.9** in the Q3 10-Q or the FY26 10-K. That would mean non-backlog levers are working, and it would favour the Street.
- **A statement at Q3 (10-28) or in January that 2026 orders are shipping in 2027 at new pricing.** It would contradict LAG p.10 and lower the weight on the timing constraint.
- **A YE26 two-year conversion percentage well above 69%**, i.e. the book shortening. A larger 2026 share in FY27 lowers X_req.
- **GEV clarifying that "$ added" is margin on orders (flow).** Levels would fall to about 16.5%; the point changes would not move.
- **FY27 guide with a low end ≥ 18%.** That would directly contradict the finding.

## 7. Disagreements with the master brief

1. The **"closes $0.6–1.3B of GLJ's gap"** figure in this task's text is superseded. The consistent figure is **$0.55–0.62B** [EL; brief §5].
2. The brief treats GEV's timing statements as a single "'27 and beyond" message. The Jan-25 wording for the 2024 vintage ("2026 and beyond") slid to "'27 and beyond" in Jan-26 [T4Q24; T4Q25].
3. The brief says the Dec-2024 and Dec-2025 investor updates quantified backlog margin. **I found no quantified backlog-margin statement at either event.** The quantified disclosures come from January calls and decks, BofA, the Q1'26 call and Laguna.

## 8. Open items

- **BofA text:** a second source (a MarketScreener or GEV-hosted transcript).
- **Laguna p.5/p.10:** a second copy, e.g. stockanalysis.com. It is cited as "LAG-SA" in F01, but the earningscalls.dev copy was truncated.
- **Dec-2024 and Dec-2025 investor-update transcripts and decks:** search for any backlog-margin page.
- **Power-only RPO runoff curve:** not disclosed. Ask IR; it is the main structural weakness in the Power split.
- **Over-time vs point-in-time revenue share:** not disclosed. Check the 10-K Note 9 disaggregation.
- **Prolec inventory step-up:** the amount, and whether adjusted EBITDA excludes it. Check the 10Q Note 2 and the Q2 non-GAAP reconciliation.
- **Transformer, switchgear and HVDC lead times:** not found. Check the Dec-25 deck and the Hitachi Energy and Siemens Energy grid decks.
- **FactSet $9,339M:** could not be re-verified this session (the data tool failed). Treat it as single-source.
