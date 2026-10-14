# Red-team the 12-month LONG: does earnings growth outrun multiple compression?

_S07_redteam_long — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 10:53:31. Requests 35, input tokens 3025565, output tokens 50356._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV 12-month long from $962.49: red-team research pack (research input only; the team writes all prose and picks every number)

## Source key
| Key | Document |
|---|---|
| 10Q | GEV Q2'26 10-Q, 0001996810-26-000148 |
| 10K | FY25 10-K, 0001996810-26-000015 |
| PR4Q | Q4'25 release, 0001996810-26-000012 EX-99 |
| PR2Q | Q2'26 release, -26-000147 |
| PR4Q24 | Q4'24 release, -25-000004 |
| SPIN8K | Spin-date 8-K, 0001193125-24-084048 EX-99.1 |
| MS | MarketScreener, 2026-09-29 (FACTS CT-01/02) |
| SA | stockanalysis.com forecast page, read 2026-09-30 (S&P Global MI data, updated 09-22) |
| CL | Chartloom NTM series (via D05 / S04) |
| TIKR-a/b/c/d | TIKR blog posts dated 2026-03-29, 06-24, 07-01, 05-06 |
| LAG | GEV-hosted Morgan Stanley Laguna transcript, 2026-09-16 |
| FACTS | facts.csv |

Earlier outputs from tonight are cited by file name (S01, S04, D05, E06, R05, R07, R08, ROB = ROBUSTNESS_PACK). Each carries its own primary sources.

---

## 1. Bottom line

- **The point-1 arithmetic is correct to the dollar, but three inputs need labels.**
  - The "plan path" FY27 ($8,590M) is a dollar midpoint and is not guidance. Other straight-line methods give $8,184–8,415M.
  - The master brief's "$10,794M plan NTM" is consensus FY27 blended with plan FY28, so it is not the plan path.
  - On the true plan path ($10,548M) the break-even multiple is **23.4x, not 22.9x**.
  - [computed; inputs 10Q balance sheet, MS, PR4Q; S2: ROB T1, E06 §4-A]
- **Point 2 is half right.**
  - The Jun→Sep 2026 fall was all multiple. But the ~10% rise in NTM EBITDA was the calendar roll, not upgrades: FY27 EPS moved +0.3% from Jul-23 to Sep-29.
  - "No month-end below ~25x" holds only on one vendor's reconstructed series. Intra-month closes reached 23.4x.
  - A second vendor (TIKR) confirms the shape of the history but reads 4–10 turns higher. The 25x "floor" is vendor-specific.
  - [S1: S04 §Q1–Q2; S2: R08 §1; TIKR-a/b/c]
- **Growth-based methods put the September-2027 multiple at about 17–24x. The long needs ≥23.4x on the plan path, or ≥20.3x on consensus.**
  - The peer cross-section (ex-Siemens Energy) fits about 18–21x at the growth GEV will show in Sep-2027. Keeping today's +28% premium to that fit gives about 23–27x.
  - Implied prices: $817–1,261 on consensus, $711–1,096 on plan [computed §4; peer data S1: MS via D05, S2: TIKR for VRT/Schneider only].
- **Base rate (Q3).** Under a strict rule (12-month loss while forward estimates rose), I verified only one clean case (GE 2000–02) and one partial case (ASML 2024–25). Vertiv 2025 and GEV 2025 are counter-cases: a sharp de-rating followed by a positive 12 months. n is too small for a frequency. That is an open item for a terminal screen [D05; Motley Fool 2025-07-21 and 2026-01-15].
- **Q6: no published FY29/FY30 broker consensus was found on free sources.**
  - SA shows FY28 as the last year, and even that is paywalled.
  - A backlog-vintage build (S01 margins × RPO schedule × GW path) gives 2029 company EBITDA of about **$10.8B / $15.4B / $20.4B** (low / base, the team's choice / high). The base is +18% on consensus FY28.
  - That is the only place a number above consensus could sit, and it is assumption-dominated [computed §4-F].
- **January (Q7).** On the long side, the dollar thresholds that separate "wrong" from "early" are:
  - FY27 guide midpoint **≤ ~$7.7B**: below the plan straight line even after GEV's largest observed cushion.
  - 2026 Power backlog-margin change **≤ +11 pts**: contradicts the CEO's Laguna statement.
  - 2028 framework margin **cut below 20%**.
  - [computed from R07 cushions; LAG p.5 via S01; PR4Q]

---

## 2. Answers

### Q1. Arithmetic and inputs (point 1); multiple history (point 2)

**Inputs**

| Input | Value | S1 | S2 | Status |
|---|---|---|---|---|
| Shares | 266.33M outstanding (270M diluted weighted average) | 10Q cover / balance sheet | MS 266,334K (R05 E1) | exact |
| Net cash | $9,113M = 13,120 − 2,849 − 1,158 NCI | 10Q balance sheet | 10Q Note 14 (R05 E1) | exact |
| Consensus FY27 EBITDA | $9,574M | MS | GLJ "Street $9.45B" (edgex 2026-09-15; FACTS GLJ-04); FactSet $9,339M (ROB T1) | close; **vendor spread $9,339–9,574M** |
| Consensus FY28 EBITDA | $13,064M | MS | none found | **[SINGLE-SOURCE]**. SA FY28 is paywalled (page read this session); E06 says the same |
| Plan FY28 | $56B × 20% = $11,200M | PR4Q (chunk 30113) | news corpus chunk 215481 (2026-01-23) and web chunk 223054 | exact |
| FY26 guide midpoint | $46.0B × 13% = $5,980M | PR2Q | Lark Research 2026-08-04 ($45.5–46.5B, 12–14%) | exact |

**Recomputation [computed]**
- Formula: P = (m × NTM + 9,113) / 266.33.
- Plan path NTM = 0.25 × 8,590 + 0.75 × 11,200 = **10,547.5**.
  - 21x: $866 (−10.0%). 23x: $945 (−1.8%). 25x: $1,024 (+6.4%). 28.2x: $1,151 (+19.6%).
- Consensus NTM = 0.25 × 9,574 + 0.75 × 13,064 = **12,191.5**.
  - 21x: $996 (+3.4%). 23x: $1,087 (+12.9%). 25x: $1,179 (+22.5%). 28.2x: $1,325 (+37.7%).
- **Every figure in point 1 ties.**

**Caveats that change numbers**
1. **"Straight line" is ambiguous.**

   | Method | FY27 | Plan NTM | Break-even multiple |
   |---|---|---|---|
   | Dollar midpoint (thesis) | $8,590M | 10,548 | 23.4x |
   | Revenue/margin midpoint: $51.0B × 16.5% | $8,415M | 10,504 | 23.5x |
   | Geometric: √(5,980 × 11,200) | $8,184M | 10,446 | 23.7x |

   The effect is small (≤$9/share at 23x) but should be labelled.
2. **Break-even multiples.** (962.49 × 266.33 − 9,113) = 247,227. That is 20.3x on consensus NTM and **23.4x on the plan NTM**. R05's "22.8–22.9x" used the brief's $10,794M, which is consensus FY27 + plan FY28. That is a blended path, not the plan.
3. **Diluted shares.** Using 270M instead of 266.33M lowers every price by 1.36% (e.g. plan 25x becomes $1,010).
4. **Static bridge.** Net-cash build to Sep-2027 adds about $29/share (+3%) [E06 §4-D; FY27 FCF consensus $7,417M is SINGLE-SOURCE, MS]. The fuller bridge (pension etc., EV $250.7B) takes off about $13/share (brief §2).
5. **Seasonality (a definitional note, not an error).** Q4 was 55% of FY24 adj EBITDA ($1.1B of $2.0B) and about 37.5% of FY25 ($1.2B of $3,196M) [S1: PR4Q24 chunk 69971; S2: PR4Q chunk 30106].
   - A quarter-sum NTM for Sep-2027 would be about 3% below the 25/75 calendar weighting.
   - Vendors' NTM multiples (MS-computed 28.2x, CL) use calendar weighting, so the thesis is internally consistent. The team must not mix the two conventions.

**Point 2: multiple history**

- **Second source for the forward EV/EBITDA history.** TIKR publishes point readings:

  | Date | Price | TIKR NTM EV/EBITDA | CL basis |
  |---|---|---|---|
  | 2026-03-29 | ~$900 | 41.47x | Mar month-end 31.3x at $872.90 |
  | 2026-05-06 | — | ~40x | 04-23 peak 40.39x |
  | 2026-06-24 | $1,034.98 | ~37.5x | ≈33.3x, scaling 06-30 by EV |
  | 2026-07-01 | $1,174.86 | ~43x | 37.9x on 06-30 |

  - TIKR also reports "EBITDA $5.75B in 2025", against adjusted EBITDA of $3,196M. It uses a different EBITDA definition, and its multiples do not reconcile with its own EBITDA figures.
  - **Finding: the two vendors agree on direction (peak Apr–Jul 2026, compression since) and disagree on level by about 4–10 turns.** "25x" is a CL-basis number.
- **Check at the September trough.**
  - My MS-basis estimate for 09-14 ($874.76): EV = 874.76 × 266.33 − 9,113 = $223,862M. NTM ≈ 0.29 × 6,359 + 0.71 × 9,574 = $8,642M. Result: **25.9x**, against CL 25.44x (close) [computed].
  - GLJ's "roughly 26 times projected 2027 EBITDA" [S1: edgex 2026-09-15; S2: business-news-today 2026-09-16] matches the NTM basis. On pure FY27 ($9,450M) my bridge gives 23.7x. Small conflict; likely an EV-definition difference.
- **"No month-end below ~25x in 12 months" is confirmed only as written.**
  - Lowest reconstructed month-ends: Oct-25 and Nov-25 at 25.1x (Oct is a lower bound).
  - But closes were ≤25x for about 6 weeks in Oct–Dec 2025 (low 23.38x on 2025-11-04), on 2025-12-17 (24.87x) and on 2026-01-08/09 (≈24.4x).
  - [S1: S04 §Q1 (CL + Nasdaq closes); S2: D05 trough table]. All CL-basis, ±~1 turn.
- **April-2025 trough.** CL gives 15.55x on 2025-04-04 **[SINGLE-SOURCE vendor]**.
  - Price conflict: D05 has "trough $271.48 on 04-04"; Investorsobserver (2025-04-07) says GEV "dropped 8.8% to close at $261.48". One of them is wrong; check against Nasdaq history.
  - I could not find a point-in-time FY25/FY26 EBITDA consensus from April 2025 to re-derive the multiple.
- **"While estimates rose" needs a qualifier.**
  - Late-June to September FY27 EPS moved +2.5% (24.25 → 24.85), and +0.3% from Jul-23 to Sep-29 [S1: R08 §1 (CN FactSet 07-23; MS); S2: S04 §Q2 (YF)].
  - The ~10% rise in NTM EBITDA is the window rolling: (0.5 FY26 + 0.5 FY27) → (0.25 FY26 + 0.75 FY27) = +$804M on about $7,967M = +10.1% [computed].

### Q2. What multiple for September 2027?

**(a) Cross-section today** (NTM EV/EBITDA against 2-year growth; peer growth is EPS CAGR, a definition mismatch per D05/BX-39)

| Name | NTM EV/EBITDA | 2-yr growth |
|---|---|---|
| VRT | 20.6x | 32.3% |
| ETN | 21.3x | 17.3% |
| PWR | 22.0x | 15.0% |
| HUBB | 15.1x | 11.8% |
| ABB | 19.0x | 12.6% |
| Schneider | 16.4x | 18.6% |
| Siemens Energy | 12.6x | 36.0% |
| MHI | 14.7x | 16.4% |
| GEV | 28.2x | 43.3% (EBITDA) |

[S1: MS via D05 §Q2; S2: ZK/SA growth; TIKR cross-checks VRT ~24x and Schneider ~17x only. Peer EV/EBITDA is otherwise **[SINGLE-SOURCE]**.]

OLS regression [computed §4-C]:
- **All 8 peers:** slope −0.09 turns per growth point. There is no positive growth–multiple relationship, because Siemens Energy dominates.
- **Ex-Siemens Energy (7 peers):** m = 15.9 + 0.143 × g, R² ≈ 0.11 (weak).
  - At GEV's current 43.3%, the fit is 22.1x. GEV trades 6.1 turns (+28%) above its own fitted value.

**(b) GEV's own multiple against forward growth.**
- One-year NTM roll (NTM+1 / NTM): about +42% in late June (7,967 → 11,319) and +39% in late September (8,770 → 12,192) [computed from MS].
- Over the same window the multiple went 37.9x → 27.7x (CL).
- **Forward growth barely moved while the multiple fell 27%.** In-sample, GEV's multiple is sentiment-driven, not growth-driven. The ratio of multiple to one-year growth was 0.90 in June and 0.71 in September. GEV's multiple history has not been regressed against its forward growth: a point-in-time growth series is not available.

**(c) Growth once the window rolls.**
- Consensus FY26→27 is +50.6% and FY27→28 is +36.5%; the plan path FY27→28 is +30.4%.
- FY28→29 has no published consensus (Q6). My research range for FY28→29 EBITDA growth is about +15% to +35% (team's choice). On the §4-F base, the Sep-27 NTM roll is +21% on the consensus path and +36% on the plan path.

**Implied multiples and prices**

| Method (research) | Multiple | Consensus NTM $12,191M | Plan NTM $10,548M |
|---|---|---|---|
| Ex-SE fit at g = 15% / 25% / 35% | 18.1x / 19.5x / 20.9x | ≈$862 / $925 / $991 | ≈$751 / $806 / $862 |
| Ex-SE fit + today's +28% GEV premium kept | ≈23.2x / 25.0x / 26.8x | ≈$1,096 / $1,179 / $1,261 | ≈$953 / $1,024 / $1,096 |
| All-peer fit (incl. SE) at GEV's growth | 15.6x | $748 (−22%) | $652 (−32%) |
| Ratio 0.71 × roll of 19–33% (range) | 13.5–23.4x | $652–1,105 | ~$569–961 |
| US-grid median (unchanged) | ~21x | $996 (+3%) | $866 (−10%) |

**Finding.** Every growth-based method sits below today's 28.2x. Holding the price on the plan path needs GEV to keep most of its current premium over a regression fitted at slower growth. The winners' model lens makes the same point: "a lower growth rate must also cut a 28x multiple" [S1: pitch-winners model lens (bam-2025-frpt); S2: D05 Q7].

### Q3. Base rate for the failure mode

**Selection rule (fixed first).**
- Large-cap capex-cycle equipment or "bottleneck" leaders.
- Starting forward P/E ≥ ~25x, or EV/EBITDA ≥ ~20x.
- Forward (next-FY) consensus estimates rose over the 12 months.
- Outcome: 12-month price return.
- Cases where estimates fell are excluded: that is a different failure mode.

| Case | Start multiple | Change in estimates | Change in multiple | Return | Trigger | Passes rule? | Sources |
|---|---|---|---|---|---|---|---|
| GE, Aug-2000 → Apr-2002 (~20 months, not 12) | 42.6x FY01 EPS | EPS $1.27 → $1.41 → $1.51 (+19%) | → 21.1x (−50%) | $60 → $31.85 (−47%) | Conglomerate/accounting trust, power bubble peak | Yes (window longer than 12m) | D05 (SEC ex-99b 2000 and 2002; NY Post 2002-04-16) |
| Cisco 2000–01 | ~151x pro forma | FY01 pro forma EPS **−23%** | collapsed | −83 to −86% | Demand bust | **No:** estimates fell | D05 (Cisco FY01 release; 2001-04-16 update) |
| ASML, Jul-2024 → Jul-2025 | not verified | 2025 growth guide ~15% held, but the Oct-2024 bookings miss cut near-term expectations | → 26–27x forward (Whispertick 2025-07-21; Zacks 2025-08-18: 26.1x) | "about 30% over the past year" | China/bookings, no 2026 guide | **Partial:** estimate direction ambiguous | Motley Fool 2025-07-21; Whispertick 2025-07-21 |
| Vertiv, Jan–Apr 2025 | high (not verified) | rose; FY25 adj EPS +47% | DeepSeek/tariff de-rating | **CY2025 +42.6%** | DeepSeek, tariffs | Counter-case: de-rated but no 12m loss | Fool 2026-01-15; VRT 8-K 2026-02-11 |
| GEV, Jan–Apr 2025 | CL 33x → 15.6x | rose | −53% at trough | Q4'24 close $327.79 → Q4'25 $653.57 (+99%) | DeepSeek, tariffs | Counter-case | S04 table (Nasdaq/SAR); D05 |
| Vestas 2008–09; GE Power 2017–18; Siemens Energy 2023 | — | estimates fell | — | large losses | Overcapacity, guidance withdrawn | **No** | V07; D05 |
| Vertiv mid-2026 | ~24x (TIKR) | rose | — | −33% from $379.94 to 2026-08-24 | Yields, beat-and-raise −17% | In progress | D05 (TIKR SINGLE-SOURCE; CNBC 2026-07-29) |

**Frequency ("~28x with 25–40% growth losing money over 12 months").**
- **Cannot be computed from free data.** Under the rule I have 1 clean hit and 1 partial, against 2 counter-cases. That is anecdote, not a base rate.
- Nearest systematic evidence (V07):
  - Only about 25% of the highest-multiple buckets beat the S&P over 12 months [WisdomTree/Siegel 2023, **SINGLE-SOURCE**].
  - Momentum is strongest among expensive winners [Asness FAJ 1997].
  - The two point in opposite directions.
- **Terminal screen to run:**
  - Universe: MSCI World industrials/tech hardware, 1995–2025.
  - Conditions: fwd EV/EBITDA 25–32x, 2-yr fwd EBITDA CAGR 25–40%, and next-FY consensus up over the next 12 months.
  - Measure: the share with a negative 12-month return, and the median multiple change.

### Q4. Five strongest PM objections

| # | Objection | Best evidence for | Best evidence against | Which wins |
|---|---|---|---|---|
| 1 | "The roll-forward is in every model. Where is the edge?" | Consensus target $1,237 ≈ 26.3x Sep-27 NTM, so the roll is already priced [D05; brief §2]. Jun–Sep 2026 NTM rose +10% on roll and the stock fell 25% [S04; R08]. No build tonight has FY27 above consensus [R05 §1] | Rolling estimates carried GEV +99% in 2025 [S04]. Momentum among expensive winners [V07] | **Objection.** The long is a multiple call with no information edge |
| 2 | "Growth halves as the window rolls, so 28x must fall" | Ex-SE fit 18–21x at 15–35% growth (§4-C). Consensus growth falls from +50.6% to +36.5%. GE 2000–02 P/E halved as EPS rose 19% [D05] | CEO dates the equipment-margin step to '29–'30 [LAG p.10; S01], which could re-accelerate FY29 (§4-F base +18% on FY28 consensus). GEV's premium over the fit has held all year | **Undetermined.** It turns on FY29 numbers that are not public; the spring CMD sets them |
| 3 | "January will read as a cut" | Street above management at every horizon: FY27 +9–12%, FY28 +16.6% [ROB T1]. 3 of 4 similar first guides fell 6–10% on the day [S04 §1.5]. Q2'26 margin-held day −8.69% [BX-13] | Cushions: bonus targets beaten by +1.75% / +10.2%; FY26 guide +12% from first guide [R07 §1]. Research P(guide ≥ $9.4B) ≈ 35% [R07] | **Objection on the day; neutral over 12 months** |
| 4 | "It trades as AI-beta; drawdowns dominate" | Five closing drawdowns ≥15% since spin (median −24.6%) [brief §6]. Stops between −15% and −30% hit 45–76% of the time on noise alone [R07]. 09-14 co-driver: an AI slow-down call [E06 Q3]. New signals this week, all adjacent to GEV rather than GEV orders: Crusoe cancelled a $1.25B turbine deal with Boom [valueaddvc 2026-09-25, SINGLE-SOURCE]; Oracle sent a force-majeure notice on Project Jupiter [mgrid 2026-09-26, SINGLE-SOURCE] | Direct data-center share is 20% of GW [E06 Q3]. Hyperscaler capex ~$795B → ~$1.08T [Reuters 2026-09-15 via E06]. Every drawdown so far has recovered | **Objection for path; long for endpoint.** E06 probability-weighted return +1% to +4% |
| 5 | "Cash is customer-funded and FY27 FCF falls 38%" | OCF ex-deposits −$3.0B in H1'26 [brief §3]. H1 buybacks ~$3.67B while deposits were $13.7B [E06 Q7; 10Q MD&A offset ~120k]. FY27 FCF consensus −38% [MS, SINGLE-SOURCE] | The valuation is EBITDA-based. Deposits are non-refundable (web, SINGLE-SOURCE). The fall is already in consensus | **Objection in Q&A; weak as a 12-month price driver** |

### Q5. "The price only needs the plan": is that fair?

**It is not fair as stated.** On the plan path the stock needs ≥23.4x in Sep-2027 just to hold (Q1). That is above the US-grid median (~21x) and above every growth fit (Q2). It is a claim about the multiple as well as the plan.

**Framework and guide record**

| Date | Framework / guide | Outcome | S1 | S2 |
|---|---|---|---|---|
| Apr-2024 (spin) | By 2028: mid-single-digit organic growth, 10% adj EBITDA margin, 90–110% FCF conversion | Raised twice | SPIN8K chunk 94232 | FACTS BR-28 |
| Dec-2024 | ~$45B, 14% | Raised | web chunk 246507 ("Up from $45 billion… Up from 14%") | FACTS BR-28 |
| Dec-2025 | $52B, 20% (+15.6% revenue, +6 pts) | Revenue raised with Prolec | web chunk 246507 | PR4Q |
| Jan-2026 | $56B, 20%, cumulative FCF ≥ $24B (up from ≥ $22B) | Current | PR4Q chunk 30113 | news chunk 215481 |
| FY24 and FY25 first guides | Revenue beat by +1.26% / +4.30%. Margin 5.83% vs 6.0% and 8.40% vs 8.5% (mid-year guides). FCF +89% / +65% | Margin never beaten | FACTS BR-21/23/24 | PR4Q24; PR4Q |
| Segment level | **Wind FY25 guide cut (Q3'25); Wind 2028 margin cut 10% → 6% (Dec-25)** | Cuts exist below company level | FACTS BR-11 | 8-K -25-000159 (via R05 P3) |
| FY26 | Margin guide 11–13% → 12–14% | Raised | PR2Q | Lark 2026-08-04 |

**What would take FY28 below the framework** (dollar sensitivities are research estimates):
- **Wind:** a 6% × ~$6.4B = +$385M target, against a record of misses [D02 Q5 via R05; FACTS BR-11].
- **Tariffs:** $100–200M in 2026 [10Q MD&A; Reuters 2026-07-22 via E06]. Small.
- **Capacity ramp:** 24 GW in 2028 is a management target [FACTS RV-26; PR2Q].
- **SRA book:** 54% of GW is reservations. The 10-K says reservations "may not result in orders" [10K Item 1A chunk 29660; E06 Q5, same filing, so one source].
- **Services:** margins not disclosed; derived band 18–32% [D06].
- **Fixed pricing:** equipment is fixed-price with no escalation [10K 1A; FY24 10-K, same language].

**Slot cancellations or deferrals: none found at GEV.**
- The SRA roll residuals are −1 / +1 / 0 / −1 GW, i.e. rounding [S1: PR3Q25–PR2Q bullets via E06 Q5; S2: Q2'26 call].
- The Q2'26 10-Q MD&A cites deposits "on orders and slot reservation agreements at Power" as the H1 inflow and discloses no cancellation [10Q offsets 118.5k/120.2k, read this session].
- The only adjacent signals are the Crusoe/Boom and Oracle items in Q4 (both SINGLE-SOURCE, neither involves a GEV order).
- The dated test is backlog GW > SRA GW in H2'26 [T2Q via E06].

**The framework is stale on cash.** FY25 FCF $3.71B plus the FY26 guide of $11.5–12.5B leaves only ~$8.3B for 2027–28 inside the "≥ $24B" figure. FY27 consensus alone is $7.4B [computed; PR4Q; MS]. That does not show the plan is weak, but it does show the framework is not a tight constraint.

### Q6. Searching for a number above consensus

**(a) Published long-dated figures**

| Figure | Value | Source | Second source |
|---|---|---|---|
| Broker FY29/FY30 consensus | **not found** | SA stops at FY28 (paywalled, read this session). The FinRobot forward_estimates tool failed | — |
| Simply Wall St FCF 2030 | $12.4B, *extrapolated beyond analyst years* (not a broker number) | Yahoo/SWS article | [SINGLE-SOURCE] |
| Seeking Alpha author (May-2026) | 2028 Power EBITDA $8B + Electrification $6.1B = $14.1B segment EBITDA, above FY28 consensus of $13,064M before Wind and corporate | SA 2026-05-14 | [SINGLE-SOURCE; not a broker] |
| Lark Research FY27 | Revenue $54.5B; non-GAAP EPS $21.21 (vs consensus $52.74B / $24.85) | Lark 2026-08-04 | [SINGLE-SOURCE] |
| TIKR model | ~$3,390 mid target "through 2030" | TIKR-b/c | TIKR only |
| Company: equipment margin added to backlog | "at least $22 billion" over 2023–26 | T4Q25 chunk 246128 | trade press chunk 217531 (S01) |
| Company: gas capacity | Actions toward 30 GW by 2030; 2029 capacity sold out | FACTS RV-26 | Capital Whispers 2026-07-25 (MS note; slots ~$3,000/kW plant-implied) |
| Company: HA services | ~$100B contracted services by end-2027 | LAG | Transcript Daily 2026-09-21 (R05 E2) |

**(b) Vintage build for 2029 and 2030** (research estimate, team's choice; §4-F)

| $B | 2029 low | 2029 base | 2029 high | 2030 low | 2030 base | 2030 high |
|---|---|---|---|---|---|---|
| Power equipment revenue | 15.6 | 20.3 | 26.1 | 15.6 | 22.5 | 27.0 |
| Power equipment EBITDA margin | 21.7% | 30.3% | 37.1% | 24.6% | 32.8% | 40.0% |
| Power EBITDA | 7.3 | 10.9 | 15.4 | 8.1 | 12.7 | 17.3 |
| Company EBITDA | 10.8 | 15.4 | 20.4 | — | ~17.3 | — |

- Calibration: the same base inputs give Power 2028 ≈ $7.35B (~20.9%), slightly **below** the 22% framework margin. The method is not biased high at 2028.

**(c) Comparison.** There is no FY29 figure to compare against. The base is +18% over FY28 consensus and +37% over the FY28 plan. Holding the multiple steady would therefore need FY29 consensus of about ≥$15B (research inference).

**Pull list for a Bloomberg terminal:**
- EE/BEst: FY29 and FY30 EBITDA, EPS and revenue, with the number of contributors.
- BEST_EV_TO_BEST_EBITDA with BF override: point-in-time daily history for GEV and the 8 peers.
- Visible Alpha: segment consensus for Power revenue, EBITDA and gas GW for FY27–30.
- Revision history for FY27/FY28 EBITDA.

### Q7. The January call for a 12-month holder

**What to expect.**
- Research zones for the FY27 dollar guide: ≥$9.4B about 35%, $8.55–9.4B about 45%, ≤$8.55B about 20% [R07 §1].
- Reference class: 3 of 4 similar first guides fell 6–10% on the day [S04].
- GEV's own January calls: +2.67% (2025) and +2.73% (2026), but those were not first guides [S04 table].
- There is **no December event this year**, so the guide arrives without a framework raise [FACTS BR-44; R07].
- Presenter conflict: Parks presents per R05 and V07 (GEV release 2026-08-27), while McDonough becomes CFO on 2027-01-01 [FACTS PP-32].

**Proposed long kill rule** (research proposal; the team sets its own thresholds)

| Line | Wrong | Early / ambiguous | Pass |
|---|---|---|---|
| FY27 adj EBITDA guide midpoint (revenue midpoint × margin midpoint) | **≤ ~$7.7B** (= 8,590 / 1.12, the largest cushion) | $7.7–8.44B | ≥ $8.44B (plan on the smallest cushion, 8,590 / 1.0175); ≥ $9.4B consensus |
| 2026 Power backlog-margin change | **≤ +11 pts** (CEO said "larger than" 2025's low double digits) [LAG p.5; S01 Q1, single primary] | — | ≥ +12 pts |
| 2026 equipment margin added to backlog | **< $8B** ("at least $8B") [FACTS PP-09; T1Q26] | $8–10B | > $10B |
| 2028 framework | **margin < 20%**, or revenue cut excluding FX/portfolio | held | raised |
| FY26 Wind (Q4 print) | ≤ −$600M (i.e. H2 < +$57M; research line) | −$600M to −$400M | ≥ guide of ~−$400M |
| YE26 gas | < 125 GW, or backlog GW ≤ SRA GW | — | both met [PR2Q; T2Q] |

- No price stop: noise alone hits stops between −15% and −30% 45–76% of the time [R07].

### Q8. What the team can state, qualify, or drop

**No qualifier needed:**
- The price formula and its inputs (266.33M outstanding shares, $9,113M net cash).
- The 2028 framework of $56B / 20%.
- The framework was raised organically at both December events.
- Street FY28 is +16.6% above the framework.
- The Jun–Sep 2026 fall was multiple, not estimates.
- No GEV slot cancellation has been disclosed.

**Needs a qualifier:**

| Statement | Qualifier |
|---|---|
| Consensus FY27 | Name the vendor: $9,339–9,574M across vendors |
| Consensus FY28 | Single-source (MS) |
| "Estimates rose" | Via the calendar roll; FY27 EPS +0.3% since July |
| "No month-end below ~25x" | Chartloom reconstruction; closes reached 23.4x; TIKR reads 4–10 turns higher |
| "~16x in April 2025" | Chartloom only; the price is disputed ($261.48 vs $271.48) |
| Vintage margins +7.5 / +20 / +35–40 | Derived; assumes a ~breakeven YE22 base; the 2026 figure rests on one conference statement. **S01 concludes the vintage math supports the plan's FY27 step, not the Street's** |
| Siemens Energy 17.3% / 19.9% | "Profit margin before special items", fiscal Q3 (Apr–Jun 2026), not EBITDA [chunk 235541; SE analyst-call chunk 251677] |
| Plan path | The framework is an outlook, not guidance |

**Drop:**
- "The price only needs the plan", unless the multiple is also stated (≥23.4x).
- The brief's "$10,794M plan NTM".
- Any FY29 or FY30 "consensus" figure: none exists publicly.

**The single check that would most change confidence either way:** Bloomberg BEst FY29 EBITDA consensus with point-in-time NTM EV/EBITDA history.
- FY29 ≥ ~$15B would support 23–25x on growth (long side).
- FY29 ≈ $14B or below (≤ +7% on FY28) implies ≤ ~19x by the fit (short side).

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Shares outstanding | 266.33M | 10Q | MS | exact | H |
| 2 | Net cash | $9,113M | 10Q balance sheet | 10Q Note 14 | exact | H |
| 3 | FY27 consensus EBITDA | $9,574M | MS | GLJ/edgex $9.45B; FactSet $9,339M | close (spread) | M |
| 4 | FY28 consensus EBITDA | $13,064M | MS | none | single | L-M |
| 5 | 2028 framework | $56B / 20% | PR4Q | news chunk 215481 | exact | H |
| 6 | Spin framework | MSD growth / 10% | SPIN8K | FACTS BR-28 | exact | H |
| 7 | Jul→Sep FY27 EPS drift | +0.3% | R08 (CN) | MS | close | M |
| 8 | CL troughs 23.38x / 25.44x | — | S04/CL | MS-basis computed 25.9x (09-14) | close | M |
| 9 | TIKR NTM EV/EBITDA | 41.47x (03-29), 37.5x (06-24), ~43x (07-01) | TIKR-a/b/c | CL | **conflict (level)** | M |
| 10 | Apr-4-2025 close | $261.48 vs $271.48 | Investorsobserver | D05 | **conflict** | L |
| 11 | Vertiv CY2025 return | +42.6% | Fool 2026-01-15 | VRT 8-K (EPS +47%) | partial | M |
| 12 | ASML 1-year return to Jul-2025 | ~−30% | Fool 2025-07-21 | Whispertick (fwd P/E 27.35) | close | M |
| 13 | GE P/E 42.6x → 21.1x | EPS +19% | D05 (SEC ex-99b) | NY Post 2002 | exact | H |
| 14 | Q4 share of adj EBITDA | 55% (FY24), ~37.5% (FY25) | PR4Q24 | PR4Q | computed | H |
| 15 | SE Gas Services 17.3%, Grid 19.9% | Q3 FY26 | web chunk 235541 | SE analyst-call chunk 251677 | exact | H |
| 16 | No SRA cancellation disclosed | roll residuals ±1 GW | E06 (releases) | 10Q MD&A | consistent | M |
| 17 | FY27 independent estimate below consensus | Lark EPS $21.21 | Lark 2026-08-04 | — | single | L |

---

## 4. Arithmetic

- **A. Prices.** P = (m × NTM + 9,113) / 266.33.
  - Plan NTM = 0.25 × 8,590 + 0.75 × 11,200 = 10,547.5.
  - Consensus NTM = 0.25 × 9,574 + 0.75 × 13,064 = 12,191.5.
  - The full grid is in Q1 and Q2.
  - Extra points on consensus: 17.1x $817, 19.8x $941, 23.4x $1,105, 26.8x $1,261.
  - Extra points on plan: 17.1x $711, 19.8x $818, 23.4x $961, 26.8x $1,096.
- **B. Break-even.** 247,227 / 12,191.5 = 20.28x; 247,227 / 10,547.5 = 23.44x.
- **C. Regression (ex-SE).**
  - Mean g = 17.71, mean m = 18.44.
  - Σ(dg·dm) = 40.65, Σdg² = 283.9, so slope = 0.1432 and intercept = 15.91.
  - R² = 5.82 / 55.14 = 0.106.
  - With SE included: slope = −52.83 / 576.5 = −0.092.
- **D. Cushions** (R07): 8,590 / 1.0175 = 8,442; 8,590 / 1.102 = 7,795; 8,590 / 1.12 = 7,670.
- **E. Roll.** NTM(Jun) = 0.5 × 6,359 + 0.5 × 9,574 = 7,966.5. NTM(Sep) = 8,770. That is +10.1%.
- **F. Vintage build (research, team's choice).**
  - GW shipped:

    | | Low | Base | High |
    |---|---|---|---|
    | 2029 | 24 | 27 | 29 |
    | 2030 | 24 | 30 | 30 |

    [FACTS RV-26: 24 GW in 2028, toward 30 GW by 2030]
  - Price: $/kW 650 / 750 / 900 (Q2'26 RPO ÷ GW = $741, FACTS RV-25).
  - Vintage margins: 2025 ≈ 19.3–20.4 pts; 2026 ≈ 34–40 [S01]. 2027 vintage set equal to 2026 (assumption).
  - Mix in 2029: 50/50, 25/75, 15/85 (2025 / 2026+ vintages). Mix in 2030: 30/70, 10/90, 0/100.
  - Contribution-to-EBITDA haircut d = 5 / 2.5 / 0 pts. Calibrated to H1'26: central equipment EBITDA +3.6% while shipping ~5–7.5-pt vintages [D06].
  - Power services: FY25 $13,081M [D06 grid; 10K Note 24], growing 8 / 10 / 12% a year at margins of 22 / 25 / 28% [D06 band 18–32%].
  - Other segments: Electrification about $4.0 / 4.55 / 5.0B; Wind 0 / 0.38 / 0.5B; corporate −0.5B.
  - Results: 2029 company EBITDA 10.8 / 15.4 / 20.4.
  - Sep-28 NTM on the base: consensus path 0.25 × 13.064 + 0.75 × 15.36 = 14.79 (+21%); plan path 14.32 (+36%).

---

## 5. General question bank

| Question | Answer |
|---|---|
| G1 | The stock holds with ≥23.4x on the plan path, or ≥20.3x on consensus (Q1) |
| G5 | Flat for 12 months ≈ estimates delivered with the multiple at 20–23x. E06's modal cell is −4% to +3% |
| G7 | The roll-forward is public information. The only candidate edge is FY29, where no consensus is public |
| G8 | One turn of multiple is worth $45.8/share, more than the FY27 estimate gap [R05 E4] |
| G14 | The CMD date is not fixed ("spring, before summer") [LAG; MarketBeat chunk 223197] |
| G19 | GE 2000–02: the multiple halved while earnings rose; the earnings break came 1.5–2 years later [D05; E06] |
| G20 | FY28 consensus, peer EV/EBITDA and CL history are all single-vendor |

---

## 6. What would change this

| Finding | What would overturn it |
|---|---|
| 1. Break-even of 23.4x on the plan path | An upward revision to the framework (FY28 > $11.2B) moves the break-even down roughly one-for-one |
| 2. Growth fits at 17–24x | FY29 consensus ≥ ~$15B, or a spring CMD 2030 outlook implying FY28→30 EBITDA CAGR ≥ 25% |
| 3. "25x floor" is vendor-specific | A point-in-time Bloomberg series showing no close below 25x |
| 4. No slot cancellations | Any quarter with an SRA roll residual ≤ −3 GW, or backlog GW < SRA GW at YE26 |

---

## 7. Disagreements with the master brief

1. The brief's "plan NTM $10,794M" is consensus FY27 plus plan FY28. The pure plan path is $10,548M, and the break-even is 23.4x, not ~23x.
2. "Never cut" is true at company level only. Wind's FY25 guide and its 2028 margin target were both cut [FACTS BR-11].
3. The Jun–Sep NTM rise came from the calendar roll, not upgrades [R08].
4. Who presents in January is disputed. The brief says the new CFO; R05 and V07 say Parks presents (GEV release 2026-08-27); McDonough becomes CFO on 2027-01-01 [PP-32].
5. The April-2025 trough price is disputed ($261.48 vs $271.48).

---

## 8. Open items

1. FY29/FY30 BEst consensus and a point-in-time NTM EV/EBITDA history (Bloomberg; see the Q6 pull list).
2. The Q3 base-rate screen described in Q3.
3. The 2025-04-04 close, to be resolved from Nasdaq history.
4. ASML July-2024 starting multiple and the direction of its estimates (FactSet revision history).
5. Why TIKR's multiple sits 4–10 turns above CL (EBITDA definition in S&P Capital IQ).
6. A second source for FY28 consensus EBITDA (FactSet/Visible Alpha).
7. The date of the spring CMD.
