# Red-team: why the 12-month LONG thesis fails

_E06_redteam_long — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:37:21. Requests 29, input tokens 1476025, output tokens 22715._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV: red-team of the 12-month long ($962.49, 2026-09-29 close)

*This is research input only. Every probability is a research judgement, and every forecast is a research estimate. The team chooses its own numbers and writes its own prose.*

**Source key**
- **10Q** = 10-Q 0001996810-26-000148 (2026-07-22)
- **PR2Q / PR1Q / PR4Q / PR3Q25** = GEV earnings releases (8-K exhibits) -26-000147, -26-000063, -26-000012, -25-000159
- **10K** = 10-K 0001996810-26-000015
- **T2Q** = Q2'26 call transcript (corpus src:3161)
- **D02 / D05 / V07 / V08** = earlier outputs tonight, which carry their own primary citations
- **FACTS** = facts.csv

---

## 1. Bottom line

- **The multiple drives the result, and peer multiples take away most of the gain from rolling forward to Sep-2027 estimates.**
  - At the US grid-peer median of ~21x NTM EV/EBITDA on consensus NTM EBITDA of $12,191M, the stock is worth about $995 (+3%). At the all-peer median of ~17.7x it is worth about $844 (−12%).
  - On management's own plan path (NTM $10,794M), the same two multiples give about $885 (−8%) and about $752 (−22%) [computed, §4-A].
  - Sources: peer multiples [S1: MarketScreener valuation pages 2026-09-29, via D05] [S2: TIKR cross-checks on Vertiv and Schneider, 2026-08-25, via D05]. Most peer EV/EBITDA figures are **[SINGLE-SOURCE: MarketScreener]**.
- **The +39% roll-forward rests on the least reliable number in the model.** That number is consensus FY28 EBITDA of $13,064M, which is 16.6% above management's own 2028 plan of $11.2B.
  - Consensus [S1: MarketScreener, FACTS CT-02] [S2: stockanalysis, per V07]. Plan [S1: PR4Q] [S2: news source N27, per V08].
  - On the plan path the roll-forward is +23%, not +39% [computed].
- **The GE precedent shows the pattern the long cannot rule out: gas-turbine earnings kept rising while the multiple halved.**
  - GE's P/E went from 42.6x to 21.1x while EPS rose 19% [S1: GE 2000 and 2002 ex-99b on SEC] [S2: NY Post 2002-04-16; Blackwell case, via D05].
  - Power Systems earnings rose 29% in 2002 and fell only in 2003: "The subsequent 2003 decline in shipments was reflected in the $0.14 per share drop" [S1: GE 2003 10-K ex13, sec.gov/…/000004054504000013/ex13.htm] [S2: GE dex99b, sec.gov/…/000119312504053388].
- **Research probabilities for the long over 12 months:**

  | Outcome | Probability |
  |---|---|
  | Return > +10% | ~22% |
  | Return < −10% | ~25% |
  | Return > 0 | ~55–64% |
  | Probability-weighted return | about +1% before net-cash build, about +4% after |

  - Computed from a 3×3 estimate × multiple grid (§4-B). The result is near market-like with a fatter left tail. On the evidence the long is a poor risk/reward rather than a broken thesis. The team should not claim it has been "destroyed".
- **Most likely failure (single largest grid cell, ~18%): the business delivers and the stock goes nowhere.**
  - The FY27 outlook lands below Street's 18.15% margin (a mild cut), and the multiple settles at 21–23x. Result: roughly −4% to +3% after 12 months.
  - This matches how the stock has reacted to raises that came without a margin raise: −8.69% on Q2'26 and −4.45% on Q2'24 [S1: Yahoo/Nasdaq closes, FACTS BX-13] [S2: D05 event table].
- **Several of the listed attack lines are weak as FY27 EBITDA arguments.**
  - Tariffs are small: $100–200M in 2026 [S1: 10Q MD&A] [S2: Reuters 2026-07-22].
  - SRAs mostly deliver in 2029 and later, so SRA conversion is a multiple/narrative risk, not a FY27 EBITDA risk.
  - The strong attack lines are the multiple, the plan-vs-Street gap, AI-capex sentiment, and FCF normalisation.

---

## 2. Answers

### Q1. De-rating to peer multiples

Formula: price = (multiple × NTM EBITDA + $9,113M net cash) / 266.33M shares. Net cash is held at the Q2'26 level; see Q7 for the build.

| Sep-27 NTM EBITDA | 25x | 22x | 21x (US grid) | 17.7x (all-peer) | 15.6x (GEV Apr-25 trough) | 12.6x (Siemens Energy) |
|---|---|---|---|---|---|---|
| $12,191M consensus | $1,179 (+22%) | $1,041 (+8%) | $995 (+3%) | $844 (−12%) | $748 (−22%) | $611 (−37%) |
| $11,277M (−7.5%) | $1,093 (+14%) | $966 (0%) | $923 (−4%) | $784 (−19%) | — | — |
| $10,794M plan path | $1,047 (+9%) | $926 (−4%) | $885 (−8%) | $752 (−22%) | — | — |

- Today's multiple is 28.2x NTM (MarketScreener-based) or 27.7x (Chartloom) [D05].
- Peer medians: US grid ≈21x (PWR 22.0x, ETN 21.3x, VRT 20.6x, HUBB 15.1x); all eight peers ≈17.7x [S1: MarketScreener] [S2: TIKR for VRT (~24x) and Schneider (~17x) only]. **[SINGLE-SOURCE]** for the others.
- **Counter-point:** GEV has the highest 2-year EBITDA CAGR in the set (43.3%, MarketScreener). On EV/EBITDA-to-growth it is 0.65, about the same as Vertiv at 0.64 [D05]. So a de-rating to peer median needs a story change, not just mean reversion.
- **Evidence that a story change can happen fast:** the NTM EV/EBITDA went from 33x to 15.6x between Jan and Apr 2025 [S1: Chartloom, **SINGLE-SOURCE** for the series] [S2: price closes via Yahoo/Nasdaq, FACTS BX-04].

### Q2. The GE 2000–02 precedent

- GE peaked at $60 in Aug-2000, which was 42.6x FY01 EPS of $1.41. It traded at $31.85 on 2002-04-15, which was 21.1x FY02 EPS of $1.51 [sources as in the bottom line, via D05].
- GE Power Systems was 16% of three-year revenue and 21% of earnings. It was hit by "the U.S. power bubble… peaking during 2002" [S1: GE 2003 10-K ex13] [S2: GE 2004 dex99b, same wording].
- In Q1 2003, GE revenue was down 1%, "reflecting lower U.S. gas turbine sales at Power Systems" [S1: GE Q1'03 release, ge.com] [S2: GE ex99a, sec.gov/…/000004054503000056].
- **Sequence:**
  1. Multiple compressed from Aug-2000.
  2. Segment earnings peaked in 2002 (+29%).
  3. Earnings fell in 2003.

  The de-rating ran roughly 1.5–2 years ahead of the earnings decline.
- **Caveat:** the de-rating also reflected the conglomerate, Enron-era trust and the "Welch premium" [D05, NY Post; Inc. 2002-10-01]. It is not a clean gas-cycle test.
- **Scale then vs now:** GE shipped ">60 GW" in 2001 [SINGLE-SOURCE: web analysis, corpus src:296]. GEV targets 20–24 GW, rising toward 30 GW by 2030 [S1: PR2Q] [S2: T2Q]. Today's capacity discipline is tighter, which works against the bust analogy.

### Q3. AI-capex sentiment

- **GEV's direct exposure is 20% of GW under contract** ("~80% are traditional customers and 20% are for data centers") [S1: T2Q p.3] [S2: web analysis, corpus src:238]. Indirect exposure through utility load forecasts is larger but not quantified.
- **2026-09-14 had a co-driver the GLJ framing leaves out.** The heads of the model provider, OpenAI and xAI called for slowing AI development. Chip stocks fell 3–7%, and a Reuters source said: "Markets are punishing the picks-and-shovels layer harder" [S1: Reuters via KRRO 2026-09-15] [S2: Gate News 2026-09-14; CNBC 2026-09-14 via V08].
- **Other shocks since mid-August:**
  - WSJ report of ~$3T in off-balance-sheet AI commitments; GEV, Vertiv and Bloom all fell [S1: Startup Fortune 2026-09-03] [S2: 24/7 Wall St, via D05 (GEV −6% on 08-18)].
  - Three data-center-related IPOs were delayed [S1: Bisnow 2026-09-22, citing the NYT] [S2: NYT, not read directly].
- **Hyperscaler capex is still rising:** ~$795B in 2026 and ~$1.08T in 2027 (BofA) [S1: Reuters 2026-09-15] [S2: Gate News (~$700B figure; definitions differ)].
- **Precedent:** the DeepSeek sell-off (−21.5% in one day) "proved to be a short-lived hiccup" [S1: Reuters 2026-09-15] [S2: Chartloom trough-to-peak recovery by Aug-25, D05].
- **Takeaway:** sentiment shocks are frequent and large, but so far they have reversed.

### Q4. Gas-turbine cycle history

- **1997–2002:** orders peaked in 2002, then about 46 GW was cancelled between Nov-2001 and Aug-2002 [V07: Power Engineering 2002-09; PEi 2002].
- **2006–16:** GE averaged about 20 GW a year [SINGLE-SOURCE: src:296].
- **2017–18:** GE Power profit fell 45% after a bullish guide against flat demand [V07: Reuters 2018-02-23; POWER 2018-02-28].
- **In both busts, earnings broke only after orders turned.** No order turn is visible yet: the CEO says 2031 slots are more than half sold by year-end [T2Q p.3] [S2: Laguna via MarketBeat, V07].
- **The one early warning:** H2'26 signings are set to roughly halve (Q5).

### Q5. SRA conversion (54% of GW is reservations)

**Quarterly roll** [S1: PR3Q25, PR4Q, PR1Q, PR2Q bullets] [S2: T2Q p.3 for Q2]:

| Quarter | SRA opening | New SRAs | Converted | SRA closing | Conversion % of opening | Firm new orders | Shipped | Backlog |
|---|---|---|---|---|---|---|---|---|
| Q3'25 | 25 | 12 | 7 | 29 | 28% | 1 | 4 | 29→33 |
| Q4'25 | 29 | 21 | 8 | 43 | 28% | 3 | 3 | 33→40 |
| Q1'26 | 43 | 19 | 6 | 56 | 14% | 2 | 4 | 40→44 |
| Q2'26 | 56 | 18 | 10 | 63 | 18% | 2 | 3 | 44→53 |

**Findings:**
- **No SRA cancellations are visible.** The roll residuals (−1, +1, 0, −1 GW) look like rounding.
- **Nearly all new demand enters as SRAs.** Firm direct orders were 8 GW over four quarters, against 70 GW of new SRAs [computed].
- **The 10-K flags conversion as a risk:**
  - "slot reservation agreements may not result in orders" (10K Item 1A, offset ~65k).
  - "some counterparties… may not place orders equal to the value of their reservation amount or at all" (10K Item 1A, offset ~80.8k).
  - Both quotes are from the same filing, so they are one source. The SRA-share comparison is confirmed by Siemens Energy's Q3 FY26 presentation p.6 (GEV 54.3% of GW vs Siemens Energy 27.4%) [FACTS RQ-16].
- **Deposit terms:** the deposit is "non-refundable… credited toward the final purchase price" [SINGLE-SOURCE: web analysis src:238]. A second example is Maxim Power's 7HA.02 reservation with a non-refundable deposit (web, src:3490). No GEV filing states the deposit size or its refundability.
- **Dated test:** the CEO says H2'26 will be the point "where orders in backlog will be greater than gigawatts on slot reservation agreement" [T2Q, Strazik, 2026-07-22].
  - Meeting ≥125 GW with backlog above SRAs needs backlog ≥62.5 GW.
  - Assuming ~10 GW shipped in H2 (research assumption from the 20 GW run-rate), that needs ~19.5 GW of H2 conversions plus orders. H1 delivered 20 GW.
  - Gross H2 signings implied by 125 GW are only ~19 GW, against 41 GW in H1 [computed]. The "peak orders" headline risk is real.
  - **Timing:** the Q3 print on 2026-10-28 is after the finals.
- **FY27 impact is limited.** SRAs mostly deliver in 2029 and later, so conversion misses hit the multiple and the orders narrative, not FY27 EBITDA (research inference).

### Q6. Fixed-price contracts, no escalation

- **Equipment is fixed-price.** The filing says GEV enters "contracts that commit to a fixed price well before project completion." In the FY25 10-K, "escalation" appears only in the lease note [S1: 10K Item 1A] [S2: FY24 10-K -25-000011, same language, via D02].
- **Customer evidence:** a $25M LG&E/KU reservation was paid "to lock in firm pricing" [S1: KY PSC order 2025-10-28] [S2: evidence brief].
- **Services escalate only at a fixed rate:** "annual 2.5% escalation" in a 2019 CSA [SINGLE-SOURCE: Talen 8-K/EX 0001622536-25-000013].
- **Implication:** margin on the older backlog cannot be repaired by escalation clauses. This supports GLJ's view on timing.

### Q7. Deposit-funded cash

- **Balances at 6/30/26** [S1: 10Q balance sheet] [S2: 10Q Note 9 table; IR deck src:3159 repeats it]:
  - Contract liabilities $39,944M (Power $27,679M, of which $25,799M is equipment).
  - Cash $13,120M; equity $13,115M.
  - Contract liabilities are about 3.0x cash [computed].
- **H1'26 cash:**
  - The deposit line was $13,695M of $10,680M operating cash flow. OCF excluding it was −$3.0B [FACTS; brief §3].
  - Treasury stock rose from $3,385M to $7,057M, i.e. **~$3.67B of H1 buybacks funded while OCF excluding deposits was negative** [computed from 10Q balance sheet; average price $854.43, FACTS].
- **FY27 consensus FCF is $7,417M, down 38%** [SINGLE-SOURCE: MarketScreener].
- **Offset the long can claim:** net cash still builds. Implied H2'26 FCF is about $2.1B at the guide midpoint, and FY27 Q1–Q3 is about $5.6B at consensus. That is ~$7.7B, or +$29/share (+3%), by Sep-2027 [computed].

### Q8. Services profit revisions

- Net unfavourable CSA profitability changes:

  | Period | Change |
  |---|---|
  | FY24 | −$319M |
  | FY25 | −$151M |
  | H1'26 | −$218M |

  Sources: [S1: 10Q Note 9] [S2: 10K Note 9 (FY25 −$151M); FACTS RQ-13].
- **Trend:** H1'26 alone already exceeds the whole of FY25. This cuts against the services-pricing narrative.
- **Scale:** it is small against $9.6B of EBITDA. It works as a quality signal more than an estimate driver.

### Q9. Wind

- Q2'26 Wind orders were −40% organic, and losses widened [S1: PR2Q via MarketScreener] [S2: Utility Dive 2026-07-23].
- Q2 adjusted EBITDA was $1.25B against a $1.28B estimate, a miss driven by Wind [S1: Reuters 2026-07-22] [S2: Investing.com, FACTS RQ-32].
- The ~−$400M FY26 Wind guide needs a +$257M H2 improvement [FACTS RQ-10]. Wind missed its final FY25 guide by $198M [FACTS BR-42; PR4Q].
- Vineyard Wind settled on confidential terms [FACTS RQ-11: GEV release; Boston Globe].
- **Takeaway:** repeated Wind misses are a credible Q3/Q4 risk. Company-level guidance has absorbed them before.

### Q10. Tariffs

- 2026 tariff cost is $100–200M, down from $250–350M, with FY25 actual ~$250M [S1: 10Q MD&A] [S2: Reuters 2026-07-22].
- That is ≤2% of FY27 consensus EBITDA. **Tariffs are noise for this thesis.**
- The Q2 call noted that pre-tariff onshore orders "had fewer contractual protections" [D02, T2Q; single-source inference].

### Q11. Rebutting the long's other pillars

- **Competitors are "sold out", but capacity is rising.**
  - Siemens Energy goes from ~110 to ~160 units a year and reaches 210–230 in FY28–30 [S1: SE CFO deck src:3179] [S2: trade press src:1699, via D02].
  - MHI is doubling capacity [S1: Utility Dive 2026-08-13] [S2: MHI Q&A, via D02].
  - GEV's firm backlog (53 GW) is below Siemens Energy's (69 GW) [FACTS RQ-16].
- **Electrification is strong but slowing at the margin.**
  - Book-to-bill fell from ~2.5 in Q1 to ~1.7 in Q2, and organic order growth from +86% to +66% [S1: PR1Q] [S2: PR2Q].
  - The H1 margin of 18.2% flatters: it is ~16.3% excluding Prolec, which runs at ~25% [D02].
- **The spring-2027 CMD has a high bar.**
  - It needs a 2028 raise of about 17% just to reach Street.
  - A raise below Street repeats the Q2'26 pattern (−8.69%).
  - Framework-raise days were +5.01% and +15.62%, but those raised the plan above where Street stood [D05; FACTS BR-38].
- **Correction:** Ken Parks, not the new CFO, presents the Jan-2027 guide [S1: GEV release 2026-08-27] [S2: MarketScreener/CFO Dive 2026-08-28, via V07/V08].

### Q12. Probabilities and the most likely failure

- **Headline probabilities** are in §4-B. The most likely single cell is (mild cut, 21–23x) at ~18%, giving about 0% before cash and +3% after.
- **Most likely failure: "dead money."**
  1. The Jan-2027 FY27 outlook lands around 16.5–17% margin against Street at 18.15% (straight-line to plan, per D04).
  2. Street trims.
  3. The multiple drifts to the grid-peer range.
- **Tail failure (~25%):** an AI-sentiment shock pushes the multiple to 15–18x.
- **Drawdown frequency:** GEV has had five closing drawdowns of 15%+ in about 2.5 years since the spin (median −24.6%) [FACTS BX]. At that rate (~2 a year), the chance of at least one ≥15% drawdown within 12 months is about 86% [computed, Poisson]. Even a winning long probably has to sit through one.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | SRA roll Q2'26 | 56+18−10→63; backlog 44→53 | PR2Q | T2Q p.3 | exact | H |
| 2 | Conversion rates | 28/28/14/18% | PR3Q25–PR2Q | T2Q | computed | H |
| 3 | Data-center share of GW | 20% | T2Q p.3 | web src:238 | exact | M |
| 4 | SRA risk language | "may not result in orders" | 10K 1A ~65k | 10K 1A ~80.8k (same doc) | — | M [single issuer] |
| 5 | Contract liabilities | $39,944M | 10Q balance sheet | 10Q Note 9 / src:3159 | exact | H |
| 6 | H1 buyback (treasury change) | ~$3,672M | 10Q balance sheet | FACTS buyback row | close | M |
| 7 | CSA revisions | −319/−151/−218 | 10Q Note 9 | 10K Note 9 | exact | H |
| 8 | Tariff cost 2026 | $100–200M | 10Q MD&A | Reuters 07-22 | exact | H |
| 9 | Q2 EBITDA vs estimate | $1.25B vs $1.28B | Investing.com | Reuters "missed" | close | M |
| 10 | Wind orders Q2 | −40% organic | PR2Q (MarketScreener) | Utility Dive | exact | H |
| 11 | GE Power earnings | 2002 +29%, 2003 −$0.14/share | GE 2003 ex13 | GE dex99b 2004 | exact | H |
| 12 | GE P/E 42.6x→21.1x | EPS +19% | GE SEC ex-99b | NY Post / Blackwell | computed | M |
| 13 | 09-14 AI-slowdown co-driver | CEO calls; chips −3 to −7% | Reuters/KRRO 09-15 | Gate News 09-14 | close | H |
| 14 | Hyperscaler capex | $795B '26, $1.08T '27 | Reuters (BofA) | Gate (~$700B) | conflict (definitions) | M |
| 15 | Peer multiples | 21x / 17.7x | MarketScreener | TIKR (2 names) | partial | M |
| 16 | Electrification book-to-bill | 2.5 → 1.7 | PR1Q | PR2Q | exact | H |
| 17 | GE 2001 shipments | >60 GW | src:296 | — | [SINGLE-SOURCE] | L |

---

## 4. Arithmetic

**A. Price grid.** P = (m × E + 9,113) / 266.33, with net cash and shares taken from the 10Q.
- Example: 21 × 12,191 = 256,011; plus 9,113 = 265,124; divided by 266.33 = **$995**.
- NTM definitions:
  - Today: 0.25 × 6,359 + 0.75 × 9,574 = **8,770**.
  - Sep-27: 0.25 × 9,574 + 0.75 × 13,064 = **12,191**, i.e. +39%.
  - Plan path: 10,794 (brief §7), i.e. +23% on 8,770.

**B. Probability grid** (research judgement; estimates and multiple treated as independent, which understates the tail because the two are positively correlated):
- Estimate rows: consensus 0.35 / −7.5% 0.40 / plan path 0.25.
- Multiple columns: 25x 0.30 / 22x 0.45 / 17.7x 0.25.
- Row returns (25x, 22x, 17.7x):
  - Consensus: +22.4%, +8.2%, −12.3%
  - −7.5% cut: +13.5%, +0.3%, −18.6%
  - Plan path: +8.8%, −3.8%, −21.9%
- Expected return: 0.35 × 7.34 + 0.40 × (−0.47) + 0.25 × (−4.55) = **+1.25%**. Adding ~+3.0% for the net-cash build gives **≈ +4%**.
- P(> +10%) = 0.105 + 0.12 = **0.225**.
- P(< −10%) = 0.0875 + 0.10 + 0.0625 = **0.25**.

**C. H2 SRA test.**
- Needed backlog: 125 / 2 = 62.5 GW.
- 62.5 − 53 + 10 (shipped) = **19.5 GW** of conversions plus orders.
- Gross signings: 125 − 116 + 10 = **~19 GW** in H2, against 41 GW in H1.

**D. Cash build to Sep-27.**
- H2'26 FCF: 12,000 (guide midpoint) − 9,897 (H1) = ~2.1B.
- FY27 Q1–Q3: 0.75 × 7,417 = ~5.6B.
- Total ≈ 7.7B / 266.33 = **$29/share**.

**E. Drawdown frequency.** λ = 5 / 2.5 years = 2 per year; P(at least one in 12 months) = 1 − e^−2 = **0.86**.

---

## 5. General question bank

- **G1:** holding $962.49 in Sep-2027 needs 20.3x on consensus or ~22.9x on the plan path [D05/V07].
- **G5:** a flat stock with consensus intact means de-rating to ~20x.
- **G9:** the other side's best answer is growth-adjusted parity with Vertiv and no order turn yet.
- **G14:** the Q3 print (10-28) falls after the finals. The Jan-2027 guide is ~4 months out.
- **G15:** see the drawdown stats in Q12 and §4-E.
- **G16:** AI-sentiment shocks, three to four of them since August.
- **G17:** buybacks funded by deposits (Q7).
- **G19:** see Q2 and Q4.

---

## 6. What would make the long robust (and overturn this critique)

1. The FY27 outlook (late Jan 2027) has a margin midpoint ≥18% and EBITDA ≥ ~$9.5B.
2. The 2028 framework is raised to ≥$13B EBITDA, or a 2030 outlook at the spring CMD implies it.
3. YE26 backlog GW exceeds SRA GW, and the ≥125 GW target is met, confirming conversion.
4. The Q3/Q4 CSA profitability revision turns favourable, and Wind hits ~−$400M.
5. Peer multiples re-rate: the US grid median rises above 24x.
6. AI-capex guides for 2027 are confirmed at ≥$1T with no cancellations.

---

## 7. Disagreements with the master brief

- **Jan-2027 guide presenter:** Ken Parks, not Claire McDonough, presents the guide (per V07/V08 sources).
- **GLJ-day drop:** the brief attributes the Sep-14 fall to GLJ plus the 10-year yield, but the AI-lab slowdown call was a third, and probably larger, co-driver.
- **Tariffs and SRAs:** they appear on the brief's attack list but carry little FY27 EBITDA weight.

---

## 8. Open items

- **SRA economics:** deposit size and refundability are not stated in any GEV filing. Look in utility dockets (KY PSC, Georgia PSC) for SRA contract terms.
- **Peer EV/EBITDA:** needs a second vendor (Koyfin, FactSet).
- **Hyperscaler capex:** reconcile the $700B vs $795B definitions.
- **H2 signings:** confirm the "H2 signings below H1" statement against the Laguna transcript. It is currently single-source.
- **GE 2001 shipments:** confirm ">60 GW" against the GE 2001 annual report.
