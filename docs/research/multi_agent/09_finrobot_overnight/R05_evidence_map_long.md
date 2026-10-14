# Evidence map: LONG over 12 months (elements only)

_R05_evidence_map_long — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:45:13. Requests 17, input tokens 1016727, output tokens 17409._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV 12-month LONG from $962.49 (to about Sep-2027, covering the spring-2027 CMD): evidence map, elements only

This is research input. The team writes every sentence and picks every forecast; grids are labelled "team's choice."

**Source key**

| Key | Document |
|---|---|
| 10Q | 0001996810-26-000148 |
| 10K | 0001996810-26-000015 |
| Q2REL | 8-K -26-000147 EX-99 |
| Q4REL | 8-K -26-000012 EX-99 |
| Q1REL | 8-K -26-000063 EX-99 |
| DEF14A | 0001996810-26-000049 |
| LAG-PDF | GEV-hosted Morgan Stanley Laguna transcript, 2026-09-16 |
| LAG-ECD | earningscalls.dev copy of the Laguna transcript (read this session; I used only the verbatim speaker text, not the site's auto-summary, which mislabels the event as "Q3 earnings") |
| LAG-SA | stockanalysis.com Laguna transcript (Exa highlight this session) |
| TD | Transcript Daily, 2026-09-21 (Exa highlight this session) |
| MB | MarketBeat Laguna write-up, corpus src:681, chunks 223192/223197, 2026-09-18 |
| 247 | 24/7 Wall St, 2026-09-16 |
| MS | MarketScreener, 2026-09-29 |
| GF | GuruFocus GLJ wire |
| BX | Yahoo/Nasdaq closes |
| yf | FinRobot yfinance quote, 2026-09-30 08:42 UTC |
| FACTS | facts.csv |

Tonight's outputs cited: F01, E06, D02, D03, V03, V12, E02, R04.

---

## 1. Bottom line

- **The long has no estimate edge.** Every build tonight has FY27 adjusted EBITDA *below* consensus: $8.6–8.9B vs $9,574M. Over 12 months the return is roll-forward plus multiple.
  - Sources: [S1: F01 §1, from D01A/D01B] [S2: V03 R4 ($8.9B base); V12 R4 ($8.8B)]. Consensus: [S1: MS] [S2: GF "Street $9.45B"].
- **What the price needs in Sep-2027.** Holding $962.49 needs about 20.3x NTM EV/EBITDA on consensus ($12,191M), or about 22.8–22.9x on the research/plan path ($10.8B). Today it trades at 28.2x.
  - Getting +15% ($1,107) needs 23.4x on consensus, or 26.5x on the plan path [computed §4-A; matches D02 §1 and V12 A6].
- **The spring-2027 CMD (2030 outlook) falls inside the window.** Strazik said "in the spring, before summer."
  - [S1: LAG-PDF, FACTS CT-39] [S2: MB chunk 223197].
  - Both earlier framework resets were raises: +4 margin points (Dec-24) and +6 points (Dec-25). Those days closed +5.01% and +15.62% [S1: FACTS BR-28/BR-38] [S2: Proactive / Reuters 2025-12-10, via D02 Q6].
- **Demand evidence is now double-sourced (new this session):**
  - Slots sold for 2032 deliveries since Q2.
  - 12 GW of added 2030–31 supply is "in some form of contracting" at premium pricing.
  - The H2'26 guide of "20 gigawatts is likely to prove to be conservative."
  - [S1: LAG-ECD, Strazik segment #6] [S2: MB chunk 223192].
- **Research probabilities for the 12-month long:**

  | Source | Result |
  |---|---|
  | E06 | E[r] ≈ +1% before net-cash build, about +4% after; P(>+10%) ≈ 22%; P(<−10%) ≈ 25% |
  | E02 | +1.8% |
  | V12 | p_long 0.52 |
  | V03 | p_long 0.53 |

  Across these the long is close to a coin flip, not a broken case. Sources: [S1: E06 §4-B] [S2: E02 via F01 Q3; V12 §1; V03 §1].
- **The biggest structural weakness.** The +39% NTM roll-forward rests on FY28 consensus of $13,064M, which is 16.6% above management's own $11.2B plan. On the plan path the roll is +23%.
  - [S1: MS, FY28 EBITDA SINGLE-SOURCE] [S2: Q4REL for the plan; computed].

---

## 2. Answers

### Q1. Evidence mapped to each memo element (12-month long)

**E1. Header / setup**

| Element | Fact | S1 | S2 | Note |
|---|---|---|---|---|
| Price | $962.49 (09-29 close; unchanged in the 09-30 quote) | yf 2026-09-30 | Zacks/Yahoo close (D08 #1, via R04) | |
| Shares | 266.33M outstanding; 270M diluted WA | 10Q balance sheet | MS 266,334K | The formula uses shares outstanding. The model must say so |
| Net cash | $9,113M (13,120 incl. restricted − 2,849 − 1,158 NCI) | 10Q balance sheet | 10Q Note 14 | |
| EV / NTM multiple | $247.2B; 28.2x NTM $8,770M | computed | stockanalysis EV $247.34B; Chartloom 27.7x | |
| Horizon events | Q3 10-28 (after finals); FY27 outlook late Jan-27 (Parks presents); CMD spring-27 "before summer" | GEV events page (PP-01); CFO-PR 08-27 | MB chunk 223197; 8-K -26-000153 | CMD date not fixed |
| Target formula | P = (m × NTM EBITDA + 9,113) / 266.33 | E06 §4-A | V12 A6 | m is the team's choice |

**E2. "The one number" (a long has to pick one)**

| Candidate | Fact | S1 | S2 | Strength for a long |
|---|---|---|---|---|
| (a) FY27 EBITDA vs consensus | Research $8.6–8.9B < consensus $9,574M | F01/D01 | V12, V03 | **Negative.** No beat to claim |
| (b) FY28 / 2028 plan raise at the CMD | Plan $11.2B vs Street $13,064M; past resets +4 and +6 pts | Q4REL | FACTS BR-28; Dec releases | The long needs a raise of about 17% just to match the Street. The pass mark sits at the Street, not above it |
| (c) Contracted services annuity (HA) | HA services ~$1B of Power's ~$24B revenue. 130 units running, 195 on contract, ≥400 by end-2027 (~200 GW). About $0.5B of services revenue per GW over 20 years, so "$100 billion" contracted by end-2027 | LAG-ECD #4 | LAG-SA; TD 2026-09-21 | New and double-sourced. A long-duration element; no FY27 EBITDA effect |
| (d) Backlog to $200B "very early in 2027" (from $176B) | | LAG-ECD #4 | 247 2026-09-16; MB | Dated, inside the window, but a volume metric |

**E3. Pillars with their top facts**

**P1. Power operating leverage and pricing**

| Fact | S1 | S2 |
|---|---|---|
| Power margin 9.88% → 12.51% → 14.68% → 17.63% (H1'26); Q2 18.82% | 10Q Note 24 | Q2REL segment table |
| H1 incremental margin 44.4% (+$1,215M revenue / +$539M EBITDA) | 10Q MD&A | Q2'26 call "+320 bp" (D02) |
| SRA pricing "10 to 20 points" vs backlog (Q4'25); ">20%" (07-22) | Q4'25 call | Q2'26 call (brief §6) |
| LG&E/KU same-site plant cost +53–57% | KY PSC order 2025-10-28 | evidence brief test (VF-03) |
| Competitors sold out: Siemens Energy "sold-out until FY28"; MHI backlog 35 GW | SE CFO deck src:3179 | Utility Dive 2026-08-13 |

- Counter-fact to carry: equipment is fixed-price with no escalation (10K 1A) [S2: FY24 10-K, same language].

**P2. Electrification**

| Fact | S1 | S2 |
|---|---|---|
| H1 revenue $6,597M; EBITDA 18.2% (13.0% a year earlier); ex-Prolec ~16.3% (computed) | 10Q MD&A | Q2'26 call |
| Equipment RPO $40,589M (+69% y/y) | 10Q | Q2'26 call |
| Electrification backlog $45B (from $6B at launch) | LAG-ECD #4 | D02 Q4 |

- Counter-fact: book-to-bill fell from ~2.5 to ~1.7 [S1: Q1REL] [S2: Q2REL].

**P3. Wind loss run-off**

| Fact | S1 | S2 |
|---|---|---|
| H1'26 −$657M; FY26 guide ~−$400M; "'27 will be much better than '26" | 10Q | LAG-ECD #4; MB |
| 2028 target 6%: 6% × ~$6.4B ≈ +$385M, a +$785M swing vs FY26 | Q4REL | D02 Q5 (computed) |

- Counter-fact: Wind missed its FY24 and FY25 guides and was cut at Q3'25 [S1: 8-K -25-000159] [S2: FACTS BR-42].

**P4. Guidance culture, bonus cushion and the CMD**

| Fact | S1 | S2 |
|---|---|---|
| 2025 bonus targets EBITDA $2.9B / FCF $2.5B vs actual $3,196M / $3,710M | DEF14A p.~47 (targets SINGLE-SOURCE) | 10K / Q4REL actuals |
| FY26 margin guide raised 11–13% → 12–14% | Q1REL | Q2REL |
| Strazik: "I always have an expectation that we do better internally relative to what we commit to you externally" | LAG-PDF p.4 | MB src:681 |

**E4. Valuation bridge (the gate judges ask for; winners' playbook, winners_playbook.md offset ~9.3k)**

Split of the return from $962.49 to Sep-2027 (§4-B):

| Path, exit multiple | Roll-forward at 28.2x | Multiple change | Estimate vs consensus | Value |
|---|---|---|---|---|
| Consensus NTM, 22x | +$362 | −$283 | $0 | $1,041 (+8%) |
| Research NTM $10,825M, 22x | +$362 | −$283 | −$113 | $928 (−4%) |

- Net-cash build adds about $29/share (+3%) [E06 §4-D; FY27 FCF SINGLE-SOURCE, MS].
- One turn of multiple is worth $45.8/share, which is more than the whole FY27 estimate gap [computed].

**E5. Catalysts and pass marks (research proposal; the team sets its own)**

| Date | Event | Long passes if | Long fails if | S1 | S2 |
|---|---|---|---|---|---|
| 10-28 | Q3'26 | EBITDA ≥ $1,706M (MS) / $1,728M (ChartMill); FY26 margin guide raised | Miss; Power < 17% | MS VF-10 | ChartMill (D07) |
| YE26 | Gas contracted ≥ 125 GW; backlog GW > SRA GW | Both | < 125 GW | Q2REL | Q2'26 call chunk 251595 |
| Early 2027 | Backlog ≥ $200B | Hit "very early" | Slips | LAG-ECD | 247 |
| Late Jan-27 | FY27 outlook + 2026 backlog-margin change (> +11 pts per CEO) | Low end ≥ 18%, or dollars ≥ ~$9.5B; margin change > 11 pts | Midpoint ≤ 17% with 2028 held | LAG-PDF p.5 (PP-04) | E06 §6 |
| Spring-27 | CMD, 2030 outlook | 2028 ≥ ~$12.5–13B, or 2030 implies Power ≥ 24% | 2028 held at $11.2B | V12 R9 | E06 §6 |

**E6. Kill rule (research proposal)**
- FY27 guide midpoint ≤ 17% with the 2028 plan held; or NTM EV/EBITDA ≤ 20x [F01 Q5] [V12 R9].
- Orders tell: H2 commitments < ~20 GW, or any disclosed SRA cancellation [V12 R13] [E06 Q5].

**E7. Downside anchor**
- Five closing drawdowns of 15% or more since the spin (median −24.6%, max −38.3%). A median drawdown takes the stock to about $725 [S1: BX Yahoo] [S2: Nasdaq closes; FACTS BX-03].
- P(at least one ≥15% drawdown within 12 months) ≈ 86% (Poisson, λ = 2 per year) [E06 §4-E].
- Bear-grid values: 17.7x all-peer median on consensus gives $844 (−12%); on the plan path $752 (−22%) [E06 Q1].

**E8. SBC, deposits, cash (G24)**
- SBC: $257M in FY25, $135M in H1'26, about 2.7% of FY27 consensus EBITDA [S1: 10K equity statement] [S2: 10Q equity statement, FACTS RV-35].
- Contract liabilities $39,944M, about 3.0x cash [S1: 10Q balance sheet] [S2: 10Q Note 9].
- H1 buyback: $3,645M, average $854.43; $3,037M authorisation left at 6/30 [S1: 10-Q -26-000064 Part II Item 2] [S2: 10Q Part II Item 2, FACTS VF-13].
- Insiders: 3 sales in 2026, no purchases [FACTS; Form 4s].

### Q2. The five strongest counter-arguments to the long, and the facts that answer them

**CA1. De-rating to peers; the roll-forward rests on a FY28 consensus that sits above plan (E06 Q1; D03 §1)**
- Attack:
  - US grid-peer median ~21x gives $995 (+3%); all-peer 17.7x gives $844.
  - Plan path at 21x gives $885 (−8%).
  - Peer multiples are mostly SINGLE-SOURCE (MS).
- Answer facts:
  - GEV has the highest 2-year EBITDA CAGR in the set (43.3%). EV/EBITDA-to-growth is 0.65 vs Vertiv 0.64 [D05 via E06].
  - NTM P/E is near the bottom of its own post-spin range (33.8x–68.9x) [Chartloom, SINGLE-VENDOR, BX-15].
  - Both framework events were raises [BR-28].
- Residual (unanswered): +15% on the plan path needs 26.5x. The long depends on the Street being right where it exceeds management.

**CA2. The January FY27 guide probably lands below the Street's 18.15%, P ≈ 80–85% (D03, D04 via V12 R7)**
- Answer facts:
  - Guide and framework days were 4 of 4 positive. Jan-2026 closed +2.73% despite an EBITDA miss ($1.16B vs $1.29B) [D04; StockStory src:3787, via V03 R3].
  - A midpoint of 16.5–17.8% is consistent with consensus still being met, given the bonus cushion [E04 via F01 §1; DEF14A].
  - January bundles the backlog-margin change (> +11 pts), the ≥125 GW target and the $200B backlog [LAG-PDF p.5] [LAG-ECD].
- Residual: Q2'26 held its margin guide and fell −8.69% [BX-13; Reuters 07-22].

**CA3. Timing: old fixed-price book; the CEO puts the next margin step in '29–'30 (D03 Q1; E06 Q6)**
- Answer facts:
  - The 2025 step (+6 pts, $8B) flows "'27, '28" and drives 8.5% → 20% by 2028 [S1: BofA transcript 2026-03-18 p.2, via R04] [S2: Q4'25 call chunk 246127].
  - At a 12-month horizon the NTM is 75% FY28, and the CMD prices 2029–30. That is where the CEO's timing *lands*, so the timing argument cuts toward the long over 12 months [V12 R8].
  - GLJ also places high-premium deliveries in 2029 [TIKR, via R04].
- Residual: consensus FY27 Power of ~21.7–23.5% (derived, not published) is above trend [F01 Q1].

**CA4. Deposit-funded cash and peaking orders (E06 Q5/Q7; D03)**
- Attack:
  - OCF excluding contract liabilities was −$3.0B in H1 while ~$3.67B was bought back.
  - FY27 FCF −38% (MS, SINGLE-SOURCE).
  - H2 commitments are below H1's 40 GW.
  - SRAs are 54% of GW vs 27% at Siemens Energy.
- Answer facts:
  - "20 gigawatts is likely to prove to be conservative for the second half of the year, but we also aren't going to be at a 40 gigawatt run rate every 6 months" (Strazik, Laguna, 2026-09-16) [S1: LAG-ECD #6] [S2: LAG-PDF p.3 via D03]. This second source clears the earlier E06 open item.
  - 2032 slots sold "with cash committed"; 12 GW of 2030–31 supply in contracting at premium pricing [S1: LAG-ECD #6/#8] [S2: MB chunk 223192].
  - The SRA roll shows no visible cancellations (residuals ±1 GW) [E06 Q5, from Q3'25–Q2'26 releases].
  - Net cash still builds by about $29/share [E06 §4-D].
- Residual: SRA deposit size and refundability are not disclosed in any GEV filing.

**CA5. AI-sentiment and rates shocks; the GE 2000–02 analogue (E06 Q2–Q4; D03; V12 R12)**
- Attack:
  - GE's P/E halved (42.6x → 21.1x) while EPS rose 19%.
  - Three to four AI shocks since August.
  - 10-yr yield 5.24% on 09-28 [FACTS RQ-28, FRED].
- Answer facts:
  - Data centres are ~20% of contracted GW [S1: Q2'26 call p.3] [S2: src:238].
  - Hyperscaler capex ~$795B in 2026 → ~$1.08T in 2027 (BofA) [S1: Reuters 09-15; S2: Gate, ~$700B, definitional conflict].
  - DeepSeek (−21.5%) reversed by Aug-25 [Reuters; Chartloom].
  - Capacity is disciplined: 20–24 GW now vs ">60 GW" shipped in 2001 (the latter SINGLE-SOURCE).
  - The GE 2002 bust signal was orders (−80%), and Power orders were +134% organic in Q2 [S1: Q2REL] [S2: Q2'26 call].
- Residual: the GE de-rating ran 1.5–2 years *ahead* of the earnings decline, so the analogue gives no reassurance on timing.

**Also noted (not top five):**
- CSA revisions are worsening: −$218M in H1'26 vs −$151M for FY25 [10Q Note 9; 10K Note 9]. A quality flag.
- Electrification book-to-bill is falling.

### Q3. Which elements are thin (honest list)

1. **Variant view / estimate edge: absent.** Research builds sit below consensus. Judges' likely question: "why is the upside bigger than the beat?" The honest answer is roll-forward plus multiple, which is time, not insight [winners_playbook ratio test].
2. **"Why the market hasn't seen it":** there is no information edge. The CMD-raise and services-annuity arguments are public (Laguna was webcast).
3. **Multiple evidence:**
   - Peer EV/EBITDA is SINGLE-SOURCE (MS).
   - The GEV multiple history (Chartloom) is not point-in-time.
   - There is no trigger evidence for a hold at ≥22x.
4. **FY28 consensus EBITDA ($13,064M): SINGLE-SOURCE.** It carries the whole roll-forward.
5. **CMD:** no fixed date, and the content of the 2030 outlook is unknown. The pass mark (2028 ≥ ~$12.5–13B) needs a +12–17% plan raise. Past raises (n=2) were +4 and +6 margin points.
6. **HA services annuity:** it is a management claim. The $0.5B/GW over 20 years is not in any filing I found, and it has no 12-month EBITDA effect.
7. **Bonus-target cushion:** SINGLE-SOURCE (proxy only).
8. **No in-horizon proof point before the finals.** Q3 reports 10-28, five days after the finals.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Price | $962.49 | yf 09-30 | Zacks/Yahoo (D08) | exact | H |
| 2 | Net cash | $9,113M | 10Q balance sheet | 10Q Note 14 | exact | H |
| 3 | Consensus FY27 EBITDA | $9,574M | MS | GF $9.45B | close (−1.3%) | M |
| 4 | Consensus FY28 EBITDA | $13,064M | MS | Motley Fool CAGR ≈ $13.09B (derived) | close | L–M |
| 5 | 2028 plan | $56B / 20% / $11.2B | Q4REL | BofA "20% by 2028"; src:27 | exact | H |
| 6 | CMD spring-27, 2030 outlook | "spring, before summer" | LAG-PDF (CT-39) | MB chunk 223197 | exact | H |
| 7 | Framework raises | +4 / +6 pts; +5.01% / +15.62% | BR-28 | Proactive / Reuters | exact | M–H |
| 8 | HA services economics | $1B today; 130 + 195 units; ≥400; ~$0.5B per GW over 20 years; $100B | LAG-ECD #4 | LAG-SA; TD | exact | M (management claim) |
| 9 | $200B backlog "very early in 2027" | | LAG-ECD #4 | 247 | exact | H |
| 10 | H2 commitments ~20 GW "conservative"; below 40 | | LAG-ECD #6 | LAG-PDF p.3 (D03) | exact | H |
| 11 | 2032 slots; 12 GW of 2030–31 at premium | | LAG-ECD #6 | MB chunk 223192 | exact | H |
| 12 | Power incremental margin H1 | 44.4% | 10Q MD&A | Q2'26 call | computed | H |
| 13 | Power margin path | 9.88 → 17.63% | 10Q Note 24 | Q2REL | exact | H |
| 14 | Bonus targets vs actuals | $2.9B vs $3,196M | DEF14A | 10K (actuals only) | SINGLE for targets | M |
| 15 | Drawdowns ≥ 15% | 5; median −24.6% | Yahoo | Nasdaq | exact | H |
| 16 | SBC | FY25 $257M; H1'26 $135M | 10K | 10Q | exact | H |
| 17 | H1 buyback | $3,645M at $854.43; $3,037M left | 10-Q -26-000064 | 10Q Part II | exact | H |
| 18 | Peer multiples | ~21x US grid / 17.7x all | MS | TIKR (2 names only) | partial | L–M |
| 19 | CSA revisions | −319 / −151 / −218 | 10Q Note 9 | 10K Note 9 | exact | H |
| 20 | Power orders Q2 | +134% organic | Q2REL | Q2'26 call | exact | H |

---

## 4. Arithmetic

**A. Required multiples.** m = (P × 266.33 − 9,113) / NTM.
- Hold: 256,340 − 9,113 = 247,227; ÷ 12,191 = 20.3x; ÷ 10,825 = 22.8x.
- +15%: 1,107 × 266.33 = 294,827; − 9,113 = 285,714; ÷ 12,191 = 23.4x; ÷ 10,794 = 26.5x.
- NTM definitions:
  - Today: 0.25 × 6,359 + 0.75 × 9,574 = 8,770.
  - Sep-27, consensus: 0.25 × 9,574 + 0.75 × 13,064 = 12,191 (+39%).
  - Sep-27, research: 0.25 × 8,800 + 0.75 × 11,500 = 10,825 (V12 A6).
  - Inputs: MS, and Q4REL for the plan.

**B. Bridge.** Today's multiple = 247,227 / 8,770 = 28.19x.
- Roll at constant multiple: (28.19 × 12,191 + 9,113) / 266.33 = $1,324.6, i.e. +$362.1.
- Multiple change: (22 − 28.19) × 12,191 / 266.33 = −$283.3.
- Gives $1,041.3 (+8.2%).
- Research-path estimate effect: (10,825 − 12,191) × 22 / 266.33 = −$112.8, giving $928.5 (−3.5%).
- One turn of multiple = 12,191 / 266.33 = $45.8.

**C. HA annuity (research inference, lifetime not annual).** 200 GW × $0.5B = $100B over ~20 years, or about $5B a year at maturity vs ~$1B today. The phase-in timing is not disclosed.

**D. SBC share.** 257 / 9,574 = 2.7%.

**E. Drawdown probability.** λ = 5 / 2.5 = 2; 1 − e^−2 = 0.86 (E06).

---

## 5. General question bank

- **G1:** holding the price needs 20.3x (consensus) or 22.8x (research) in Sep-27. In physical terms: 20–22 GW in 2027, 24 GW in 2028, and Power reaching ~22% by 2028 (§4-A; V12 R1).
- **G5:** a flat stock with consensus intact implies a de-rating to ~20x.
- **G8/G23:** one turn of multiple ($46) is more than the FY27 gap ($60–90 per share, V12). For a long, the upside is not an estimate beat.
- **G13:** the only dated tests before Sep-27 are the Jan-27 guide and the spring CMD. Q3 is after the finals.
- **G14:** the CMD could slip into summer ("before summer" is a soft commitment).
- **G17:** buybacks ($3,037M authorisation remaining), M&A optionality ("play offense" with $13B cash, LAG-ECD #4 / MB), and guidance style under the new CFO from Jan-27.
- **G21:** evidence that would show the long is wrong: H2 commitments < 20 GW, SRA cancellations, a CMD with 2028 held. None has been observed yet.
- **G24:** see E8.

---

## 6. What would change this

| Finding | What would overturn it |
|---|---|
| "Roll-forward carries the long" | FY28 consensus revised toward $11.2B after January (the roll drops to about +23%) |
| "CMD raises" | 2028 reaffirmed with only a 2030 range that implies ≤ 22% Power |
| Demand pillar | Q3/Q4 10-Q shows SRA cancellations, or YE26 < 125 GW |
| Multiple support | The US grid-peer median falls below 20x, or an AI-capex guide-down in 2027 |
| "No estimate edge" | January guide low end ≥ 18% (the long would gain an estimate leg) |

---

## 7. Disagreements with the master brief

- **January presenter:** the January 2027 guide is presented by Parks, not as McDonough's first call [S1: CFO-PR 08-27] [S2: 8-K -26-000153] (F01).
- **Margin-guide history:** the FY26 first margin guide was 11–13%, raised to 12–14% [Q1REL; Q2REL]. "Never cut" excludes Wind [8-K -25-000159].
- **H2 commitments:** the H2 < H1 statement is now double-sourced [LAG-ECD #6; LAG-PDF p.3]. It was previously flagged single-source in E06/D03. Strazik also calls the 20 GW H2 guide "conservative", which softens the "orders halving" reading.

---

## 8. Open items

1. **Second vendor for FY28 EBITDA and peer EV/EBITDA:** Koyfin, FactSet, or LSEG via the university terminal.
2. **CMD exact date:** watch the GEV events page and the 10-28 call.
3. **HA $0.5B/GW over 20 years:** look for it in any GEV filing or IR deck (not found in the corpus search this session).
4. **SRA deposit size and refundability:** KY PSC / Georgia PSC dockets.
5. **Whether a December 2026 investor event is announced on 10-28.** It is not listed today.
6. **Laguna p.10 "'29 and '30" line:** a second verbatim copy may exist in LAG-ECD beyond the first 12k characters I read. Worth reading further.
