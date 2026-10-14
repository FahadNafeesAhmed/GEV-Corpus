# Variation experiment — what is robust and what is framing

_V10_compare — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 01:58:37. Requests 16, input tokens 1188889, output tokens 18242._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV robustness audit: the nine V0x variants (V01–V09), as of 2026-09-30

Research input only. The team writes every memo sentence and picks every forecast number. I read all nine V0x outputs in full, including each FINAL_BLOCK. I checked one point of disagreement between variants against primary sources (the CFO on the January call).

**A caveat on independence.** All nine runs used the same model and the same corpus. Seven of them also read tonight's D01–D04 outputs. So when a finding recurs across variants, that shows it survives different framings. It does not show independent confirmation. V05 (no brief, no prior research) and V09 (no web) are the least dependent runs, so findings they reach on their own count most.

---

## 1. Bottom line

- **The FY27 EBITDA estimate is robust; the direction call is not.** FY27 adj. EBITDA base: median $8,800M, range $8,700–8,900M across all nine, about −8% vs MarketScreener's $9,574M. Direction splits 3 long / 6 short. p_long: median 0.46, range 0.43–0.55. [V01–V09 FINAL_BLOCKs; consensus per MarketScreener, cross-checked against the GLJ-cited $9,450M in V01/V04/V06/V08]
- **Anchoring moved the answer by more than the noise band.**
  - Noise (V01 vs V02, identical prompts) was 0.03 on p_long.
  - Anchoring (V03 told long vs V04 told short) was 0.07, and the direction flipped.
  - FY27 EBITDA did not move with the anchor (Δ$100M).
  - On the brief's own criterion, the evidence does not settle the direction question.
- **Horizon explains most of the split in direction.**
  - Every variant with a 4–5-month horizon is short: V04, V06, V07, V08, V09. Median p_long 0.45.
  - Of the four 12-month horizons, three are long (V01, V02, V03) and one is short (V05).
  - Where a variant gave a 12-month probability in its body text, the median is about 0.51 (§4).
  - V08 states the split explicitly: about 0.45 at 4 months, about 0.57 at 12 months.
  - Framing mostly worked by pushing the model toward a shorter horizon.
- **Every short target embeds a de-rating.** The short targets (V06–V09) put about 24–26x on FY27 in a January-2027 frame, against 28.2x NTM today.
  - At a constant 28.2x on the research path, January value is about $991 (V04 A3).
  - About $100–110 per share of each short target comes from the assumed multiple cut, not from the estimate gap (A4).
- **One brief premise is technically true but misleading.** The "first FY27 guide under the new CFO" framing:
  - McDonough becomes CFO on 2027-01-01 [8-K 0001996810-26-000153, Item 5.02].
  - But GEV's own release says Parks stays through "the third and fourth quarter earnings calls and the publishing of the 2026 10-K" [gevernova.com CFO-transition release, 2026-08-27; eletric-vehicles.com 2026-08-27; CFO Dive 2026-08-28 via D04].
  - The two variants without that web evidence (V05, V09) kept the "new CFO" angle. The other seven dropped it.
- **The research's own confidence never moved.** All nine rate confidence 2/5. Eight of nine name the multiple, not EBITDA, as the biggest uncertainty (V09 names management behaviour).

---

## 2. Answers to the assignment

### Q1. FINAL_BLOCK table

| Var | Framing | Dir | p_long | FY27 low / base / high ($M) | FY28 base ($M) | Target range (base) | Horizon | Conf | Top reason (condensed) |
|---|---|---|---|---|---|---|---|---|---|
| V01 | neutral A | long | 0.52 | 7,900 / 8,800 / 9,600 | 12,000 | $875–1,086 ($1,001) | 12m | 2 | ~8% FY27 gap cancelled by the NTM roll; CMD and backlog-margin "floor" inside horizon |
| V02 | neutral B | long | 0.55 | 7,900 / 8,800 / 9,600 | 11,500 | $930–1,090 ($1,010) | 12m | 2 | Plan-path roll needs only ~23x to hold; guide days historically positive |
| V03 | told long | long | 0.53 | 8,200 / 8,900 / 9,600 | 11,600 | $880–1,090 ($1,004) | 12m | 2 | ~25% NTM roll even on below-consensus numbers; market rewards orders/cash over margin |
| V04 | told short | short | 0.46 | 8,000 / 8,800 / 9,600 | 11,600 | $815–915 (n/a) | 4m | 2 | FY27 consensus prices Power at 2028 target; CEO dates step '29–'30; thin because roll needs de-rating |
| V05 | cold start | short | 0.45 | 7,600 / 8,900 / 9,900 | 10,800 | $615–1,200 ($867) | 12m | 2 | ~22x mgmt FY28 / ~26x FY27; deposit-driven FCF; H2 commitments ~half H1; January guide likely below |
| V06 | PM persona | short | 0.43 | 8,000 / 8,700 / 9,600 | 11,200 | $840–915 ($851) | 4m | 2 | Street 9–17% ahead of mgmt plan; January guide without a December cushion |
| V07 | outside view | short | 0.47 | 8,000 / 8,900 / 9,700 | 11,600 | $836–937 ($870) | 5m | 2 | Street ahead of plan and CEO timing, offset by expensive-winner momentum and the raise record |
| V08 | pre-mortem | short | 0.46 | 8,000 / 8,800 / 9,600 | 11,500 | $827–893 (n/a) | 4m | 2 | Same as V06; edge fades after ~4m (body text: 12m P(above) ≈ 0.57) |
| V09 | no web | short | 0.45 | 8,400 / 8,700 / 9,300 | 11,500 | $760–913 ($818) | 4m | 2 | Consensus needs Power+Electrification at ~22% in 2027 (2028 target a year early); "new CFO" |

Summary statistics are computed in A1–A3. p_long: median 0.46, mean 0.48, range 0.43–0.55. FY27 base: median $8,800M, range $8,700–8,900M. FY27 low: median $8,000M (range $7,600–8,400M). FY27 high: median $9,600M (range $9,300–9,900M). FY28 base: median $11,500M, range $10,800–12,000M.

### Q2. Effect measurements

The neutral reference is the mean of V01 and V02: p_long 0.535, FY27 $8,800M.

| Test | Comparison | Δ p_long | Δ FY27 base | Δ FY28 base | Δ direction / horizon | Read |
|---|---|---|---|---|---|---|
| (a) Noise | V01 vs V02 | 0.03 | $0 | $500M (4%) | none; both long, 12m | Noise band ≈ ±0.03 on p_long and ±$0.5B on FY28. It rests on n=1 pair, so it is a weak estimate of noise. |
| (b) Anchoring | V03 vs V04 | **0.07 (≈2.3× noise)** | $100M | $0 | flip long→short; horizon 12m→4m | **Exceeds noise.** The effect is asymmetric: V03 sits within noise of neutral (−0.005), while V04 moved −0.075. The short anchor worked mainly by shortening the horizon. EBITDA did not move. |
| (c) Brief | V05 vs V01/V02 | −0.085 | +$100M | −$700M | long→short at the same 12m horizon | Without the brief and D01–D04, the answer came out more short, not more long. The brief did not pull variants toward its own short lean: brief-fed neutral runs went long. The difference comes from inputs: V05 lacked the D04 "4/4 guide days positive" and "Parks presents" evidence, used a 20x base multiple on FY28, and used GLJ-origin consensus ($9.45B, no FY28 consensus). FY27 EBITDA was unaffected. |
| (d) Persona | V06 | −0.105 | −$100M | −$800M | short, 4m | Largest single move. The PM framing "fund it or not" gave the lowest p_long and a 25x FY27 target with no roll. |
| (e) Base rates | V07 | −0.065 | +$100M | −$400M | short, 5m | The outside-view prior itself was 0.52 (long-leaning, from value×momentum); specific adjustments took it to 0.47. |
| (f) Pre-mortem | V08 | −0.075 (4m) / +0.035 (12m) | $0 | $0 | short at 4m, long at 12m | The clearest evidence that direction depends on horizon. |
| (g) Web | V09 vs V01/V02 | −0.085 | −$100M | −$0–500M | short, 4m | Without the web it lost the CFO-presenter correction and the peer/reaction evidence, and leaned short. FY27 range was narrower ($8.4–9.3B). The comparison is confounded, because V09 also did not use D04. |

Sources: FINAL_BLOCKs and §1/§7 of each output. V08's 12-month figure is from its A8. V05 input differences are from its R2/R11.

### Q3. Ladder rungs R1–R14 across variants

| Rung | Same everywhere? | What is common | What changed with framing |
|---|---|---|---|
| R1 price requires | **Yes (9/9)** | EV ≈ $247.2B; 25.8x FY27; 28.2x NTM; flat-price NTM multiple 20.3x on consensus / ~22.8–22.9x on plan; 20–22 GW in 2027, 24 GW in 2028; Power ~22% a year early | V05 frames it as 22.1x mgmt FY28 |
| R2 consensus vs plan | **Yes, 8/9 on numbers** | $9,574M / $13,064M (MarketScreener), FY28 +16.6% vs $11.2B; every variant flags single-vendor EBITDA | V05 used $9.45B (GLJ-origin) and found no FY28 consensus |
| R3 delivery record | **Yes (9/9)** | Revenue +1.3% / +4.3%; margin 5.83 vs 6.0 and 8.40 vs 8.5; FCF +89% / +65%; never cut | V04 adds that the FY26 margin guide was raised once (11–13% → 12–14%) |
| R4 variant line | **Mostly** | FY27 −6% to −9%, Power margin the driver | The "one number" was FY27 in 7 variants and FY28 in 2 (V03, V08) |
| R5 why unseen | **Yes (9/9)** | "Interpretation and timing, not information" | — |
| R6 long case | **Yes (core)** | Roll-forward; raise record; spring CMD; pricing (SRAs "10–20" / ">20%"); Siemens Energy sold out | V05 adds the services annuity; V07 adds momentum base rates |
| R7 short case | **Yes (core)** | Street ahead of plan; CEO '29–'30 timing; margin never above midpoint; H2'26 at 16.3% vs 15.0% | New per variant: V05 (deposit-funded FCF, H2 commitments ~20 GW vs 40 GW, MHI doubling capacity), V09 (P+E 22% needed), V06/V04 (hedge-fund holders 118→106) |
| R8 evidence quality | **Yes (9/9)** | Short is better on estimates; long is better on price mechanism | V07/V08/V09 call it roughly equal |
| R9 dated test | **Event yes; pass mark no** | Late-January FY27 guide; short fails at a margin guide ≥18% (9/9) | Short pass mark: ≤16.5% (V01), ≤17% (V02, V09), ≤17.5% (V04, V06, V07, V08), ≤$8.8B (V05). Presenter: Parks (7) vs new CFO (V05, V09) |
| R10 loss if wrong | **Yes** | Median drawdown −24.6%, max −38.3%; short risk +24% to the 52-week high and a +15.62% day | — |
| R11 Sep-2027 value | **Consensus row identical; the rest differs** | $950 / $1,041 / $1,179 at 20x / 22x / 25x | Plan-path NTM input ranges $10,548–10,925M; probability-weighted values $905–987 (A5) |
| R12 analog | **Yes (9/9)** | The busts started with orders turning, earnings lag orders, no order turn is visible, so the analogs do not support a 3–12m bust short | V05 reads the H2 commitment slowdown as an early second-derivative warning. The 2017–19 case was not researched in V03, V05, V06, V08 |
| R13 flip | **To long: yes** | A low end ≥18% or a framework raise flips the view long (9/9) | Flip-to-short thresholds vary |
| R14 confidence | **Yes** | 2/5 in all nine; the multiple dominates (8/9) | V09 names management behaviour |

**Citation recurrence.** Robust means recurring across framings, not independent.

- **Strong:** cited by at least 6 variants, including at least one of V05 or V09.
  - 8-K -26-000012 (2028 framework) and 8-K -26-000147 (FY26 guide): 9/9.
  - GLJ-cited Street $9.45B: 9/9.
  - MarketScreener $9,574M: 8/9.
  - Margin-vs-midpoint rows (facts BR-23 / 10-Q -25-000133): 8/9.
  - Drawdown series (BX-03..08): 8/9.
  - Laguna p.10 "'29 and '30": 8/9. V06 and V09 could not verify it verbatim, and V09 tags it single-source.
  - GE 2002 release on the "80% or more" order decline: 5 variants, V05 among them.
- **Recurring but single-source underneath:**
  - Laguna p.3 "H2 commitments below H1's 40 GW": V02, V03, V05, V08, all tagged single-source.
  - D04's "4/4 guide days positive": 7 variants, but all trace to D04's price table.
  - GE Power Systems "+29% in 2002": V03, V05, V06, V07; the underlying documents all come from GE itself.
- **Appears once (weak):**
  - McKinsey analyst bias and Asness value×momentum (V07).
  - 247wallst revision count (V04).
  - CNBC AI-slowdown cause of 9/14 (V08).
  - Goldman "~21x 2028E" (V05).
  - FY26 MarketScreener EPS including the Prolec gain (V06).
  - P+E 22% arithmetic and the YF debt reconciliation (V09).
  - Jones & Tuzel order/shipment ratio (V07).

### Q4. Robust vs framing-driven

**ROBUST.** These held across all nine framings and beyond noise:
1. FY27 adj. EBITDA base ≈ $8.7–8.9B, about −7% to −9% vs consensus.
2. Street FY28 is +16.6% above management's $11.2B plan.
3. The margin record: revenue and cash beat; margin lands inside the range, below the midpoint.
4. The gap is interpretation/timing, not information.
5. The late-January FY27 guide is the reveal, and a low end ≥18% kills the short.
6. The price mechanism dominates the estimate gap. A 12-month short needs a de-rating to about 20–23x NTM.
7. The gas-turbine bust analogs do not support an in-horizon bust.
8. Confidence is 2/5.

**FRAMING-DRIVEN:**
1. **Direction.** p_long median 0.46, range 0.43–0.55. The anchoring swing (0.07) is more than twice the noise swing (0.03).
2. **Horizon choice.** It fully sorts direction among the brief-fed runs.
3. **Target ranges.** Short targets depend on an unstated de-rating; long targets on a ~23x hold.
4. **FY28 base** ($10.8–12.0B).
5. **The short pass mark** in January (16.5–17.5%).
6. **The CFO-presenter angle.** It depends on whether the variant saw the 2026-08-27 release.

**Is the direction call robust?** No. It is robust only when conditioned on horizon:
- At 4–5 months (through the January guide), 5/5 variants lean short at about 0.45.
- At 12 months, the framings split, and the median is about 0.51.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | Neutral-run p_long | 0.52 / 0.55 | V01 FINAL_BLOCK | V02 FINAL_BLOCK | close (Δ0.03) | H |
| 2 | Anchored p_long | 0.53 / 0.46 | V03 FINAL_BLOCK | V04 FINAL_BLOCK | conflict (Δ0.07, direction flips) | H |
| 3 | FY27 base across variants | $8.7–8.9B | V01–V09 FINAL_BLOCKs | D01 base $8.7B (cited in V04/V07) | close | H |
| 4 | FY27 consensus | $9,574M | MarketScreener (V01–V04, V06–V09) | GLJ-cited $9,450M (Yahoo/GuruFocus via V05, V08) | close (−1.3%) | M (single vendor) |
| 5 | McDonough CFO effective 2027-01-01 | date | 8-K 0001996810-26-000153 Item 5.02 (read this session) | eletric-vehicles.com 2026-08-27 | exact | H |
| 6 | Parks presents the Q4'26 call and 10-K | presenter | GEV release 2026-08-27, gevernova.com (search snippet this session) | CFO Dive 2026-08-28 (via D04); vocal.media repeat | exact | H |
| 7 | V08 12m vs 4m probability | 0.57 / 0.45 | V08 A8 | V08 §1 bullet 4 | exact (internal) | M |
| 8 | Jan-2027 value at constant 28.2x on $8.8B path | $991 | V04 A3 | recomputed in A4 below | exact | H |
| 9 | Guide days positive 4/4 | +5.01%, +15.62% (framework days) | D04 (corpus price table) | Proactive 2025-12-10 (via D04) | close | M |
| 10 | Brief's $10,794M NTM uses consensus FY27 | 0.25×9,574 + 0.75×11,200 | V02 §4 | V06 §7; V08 A6 | exact | H |

---

## 4. Arithmetic

- **A1. p_long.** Sorted: 0.43, 0.45, 0.45, 0.46, 0.46, 0.47, 0.52, 0.53, 0.55. Median 0.46 (5th value). Mean 4.32 / 9 = 0.480. Range 0.12.
- **A2. FY27 base.** Sorted: 8,700 ×2; 8,800 ×4; 8,900 ×3. Median $8,800M. Mean 79,200 / 9 = $8,800M. Spread $200M (2.3%). 8,800 / 9,574 − 1 = −8.1%.
- **A3. FY28 base.** Sorted: 10,800; 11,200; 11,500 ×3; 11,600 ×3; 12,000. Median $11,500M, which is 11,500 / 11,200 − 1 = +2.7% vs the plan and 11,500 / 13,064 − 1 = −12.0% vs consensus.
- **A4. De-rating embedded in the short targets** (January frame; NTM = 11/12 × FY27 + 1/12 × FY28 = 11/12 × 8,800 + 1/12 × 11,600 = $9,033M, per V04 A3):
  - At 28.2x: (254,731 + 9,113) / 266.33 = $991.
  - At 25x: (225,825 + 9,113) / 266.33 = $882.
  - De-rating component = $109 a share. The estimate component (consensus NTM $9,865M vs $9,033M at 28.2x) = $1,079 − $991 = $88.
  - Net cash $9,113M and 266.33M shares are from 10-Q -26-000148 per brief §2 and V09 row 2–3.
- **A5. Probability-weighted Sep-2027 values stated in the variants:** V01 $979, V03 $983, V06 $954, V05 $905–924, V08 ≈ +2.5% ≈ $987. Median ≈ $979, about +1.7% vs $962.49.
- **A6. 12-month p_long where stated or implied:**

  | Variant | 12m p_long |
  |---|---|
  | V01 | 0.52 |
  | V02 | 0.55 |
  | V03 | 0.53 |
  | V05 | 0.45 |
  | V06 | ~0.445 (R11 "0.43–0.46") |
  | V08 | 0.57 |
  | V09 | ~0.50 ("about neutral") |
  | V04 | ~0.50 ("close to a coin flip") |

  Median = (0.50 + 0.52) / 2 = **0.51**.
  - 4–5-month group (V04, V06, V07, V08, V09): 0.46, 0.43, 0.47, 0.45, 0.45. Median **0.45**.
  - The 12-month mapping for V04, V06 and V09 is my reading of their prose. It is not a stated number.

---

## 5. General question bank items answered

- **G5 (flat for 12 months):**
  - All variants agree that a flat price implies NTM EV/EBITDA falls from 28.2x to about 20.3x on the consensus path or about 22.9x on the plan path (V07 §4; V08 A6).
- **G8 (does the gap matter after the multiple):**
  - The −8% FY27 gap is about $60–90 a share (V03 R14; A4).
  - One turn of multiple is worth about $40–46 a share (V02 R14; V06 R14).
  - Every variant finds the multiple dominates.
- **G14 (could the reveal slip past the horizon):**
  - Yes, if no FY27 margin guide is given, or if a December event pulls a framework raise forward (V07, V08).
- **G17 (what management controls):**
  - Guide style: "do better internally relative to what we commit to you externally" (Strazik, Laguna, per V04/V08 via D04).
  - Buyback: $3.0B left on the authorization (V04 R6).
- **G20 (single-source and definition traps):**
  - EBITDA consensus comes from one vendor.
  - FY27 FCF consensus is single-source.
  - MarketScreener FY26 EPS includes the Prolec gain (V06).
  - YF TTM EBITDA of $3,927M is not company-adjusted TTM EBITDA of $4,115M (V09).
- **G25 (what was verified by hand vs by tools/AI):**
  - This audit verified the CFO documents by hand against the 8-K text and the GEV release.
  - Every other figure here is a FINAL_BLOCK or body value transcribed from V01–V09.

---

## 6. What would change these findings

- **"Direction not robust" would be overturned by:**
  - a second noise pair showing noise of 0.07 or more (then anchoring would sit inside noise); or
  - re-runs of V03 and V04 held to a fixed 12-month horizon that converge.
- **"FY27 estimate robust" would be overturned by:**
  - a second consensus vendor well below $9.5B (the gap shrinks); or
  - a disclosed Power equipment/services margin split that moves the Power 2027 path.
- **"Horizon sorts direction" would be overturned by:**
  - a 12-month-fixed rerun of V06 or V09 that still comes out short above noise. V05 already partly contradicts it, but its 20x base multiple explains the difference.

---

## 7. Disagreements with the master brief

1. **The research lean is horizon-specific, not a clean 55–60% short.**
   - Across nine framings: median p_long 0.46, about 54% short.
   - That holds only for a 4–5-month window. At 12 months the median is about 0.51.
   - The brief's §8 lean survives only if the team's horizon ends at the January guide.
2. **"First under the new CFO" is misleading.**
   - The title changes 2027-01-01 [8-K -26-000153].
   - But Parks presents the Q4 call and signs off the 10-K [GEV release 2026-08-27; CFO Dive 2026-08-28].
3. **The §7 "management plan" NTM of $10,794M uses consensus FY27.** On a plan-consistent FY27 it is $10,548–10,625M (V02, V06, V08).
4. **The §8 short range (−9% to −14% at 25x) values on FY27 without the four-month roll.**
   - At a constant 28.2x NTM the January value is about $991 on the research path.
   - So the short needs an explicit de-rating assumption (A4; V04 §7).
5. **The FY26 margin guide was raised once** (11–13% → 12–14%) (V04, V05). The "never beat the first margin guide" claim still holds for FY24 and FY25.

---

## 8. Open items

- **A second noise pair.** One pair (V01/V02) is too few to set a noise band. Rerun V01 twice more, and rerun V03/V04 with the horizon fixed at 12 months, to separate anchoring from horizon choice.
- **A second EBITDA consensus vendor** (Visible Alpha / LSEG / FactSet). This was flagged in 9/9 variants and is still unresolved.
- **The verbatim Laguna p.10 quote from a second source.** V06 and V09 could not confirm it. Read the GEV-hosted transcript PDF directly.
- **The Laguna p.3 remark on H2'26 commitments** is single-source in every variant that used it. The Q3 call on 2026-10-28 will confirm or refute it.
- **The 2017–19 GE Power de-rating path** was not researched in four variants. Source: GE 10-Ks 2018–19, CIK 40545.
- **Who actually speaks on the January call.** Confirm when GEV posts the Q4'26 date and speaker list on its IR events page.
