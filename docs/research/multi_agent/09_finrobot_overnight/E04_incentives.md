# Executive incentives and guidance behaviour (proxy deep dive)

_E04_incentives — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:43:46. Requests 47, input tokens 3035163, output tokens 30788._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): how bonus and PSU targets compare with public guidance, from the 2025 and 2026 proxies (research input only, not memo text)

## 1. Bottom line

- **The annual bonus targets were set at public guidance, not below it.** The adjusted EBITDA bonus target was about the guide midpoint in both years: FY24 target $2,000M against "mid-single digits toward the higher end" on $34–35B revenue; FY25 target $2,900M, 0.7% under the $2,920M mid-case of "high-single digits" on $36–37B. The free cash flow (FCF) target sat at the top of the guide both years, 11.1% above the midpoint ($1,000M vs $0.7–1.1B; $2,500M vs $2.0–2.5B). The organic-growth target (5.0%, 5.2%) sat in the upper half of the growth the revenue guide implied. [S1: DEF 14A 0001996810-25-000049, p.54 table] [S1: DEF 14A 0001996810-26-000049, p.50 table] [guides S2: GE 8-K 0000040545-24-000024 (2024-01-23); GEV 1Q24 8-K 0001996810-24-000004; Dec-2024 investor update PDF; Reuters 2024-12-11]
- **Payouts beat target both years, and the size of each leg's beat mirrors the guidance pattern.**
  - FCF paid 170% in 2024 and 200% (above maximum) in 2025. Actuals were +70% and +48% over target.
  - Adjusted EBITDA paid only 104% and 130%, on actuals +1.75% and +10.2% over target.
  - Organic growth paid 131% and 178%.
  - This is the brief's "beats are cash and revenue, not margin" pattern, now in the pay record. [S1: proxy tables above] [S2: 4Q24 release 0001996810-25-000004; 4Q25 release 0001996810-26-000012]
- **Payouts to the executives:** the business-performance factor was 136% (2024) and 157% after a −10pt safety modifier (2025). The CEO was paid 164% of target in 2024 and was capped at 200% in 2025. [S1: 2025 proxy p.55; 2026 proxy p.53] [S2: AFL-CIO Paywatch, 2024 incentive $3,206,385; Creately/SEC extract, 2025 incentive $4.50M]
- **The bonus targets were not easy against the prior year.**
  - FY24 targets were 2.5x FY23 adjusted EBITDA ($807M) and 2.3x FY23 FCF ($442M).
  - FY25 thresholds were about 18% above FY24 actuals.
  - So the slack comes from the guidance itself, not from targets set below guidance. [computed §4]
- **No 2026 targets are disclosed.**
  - The 2026 bonus and 2026–28 PSU values are not in the 2026 proxy (searched "2026 AIP", "2026 PSU", "2026-2028", "for 2026"; only 2026 peer-group changes appear).
  - PSU targets for 2024–26 and 2025–27 are withheld until each period ends. The 2024–26 targets should appear in the spring-2027 proxy, after the January 2027 guide. [S1: 2025 proxy p.55; 2026 proxy p.53] [SINGLE-SOURCE per document; checked both proxies and the 10-K Note 17, which gives no targets]
- **What this means for reading the FY27 guide** (arithmetic, not a forecast):
  - If the FY27 guide carries the same cushion as FY24–25 (actual EBITDA 1.8–10.2% above the bonus target), a guide midpoint of **$8.69–9.41B, or 16.5–17.8% margin** on consensus revenue, is consistent with consensus $9,574M still being hit.
  - A sub-18% FY27 margin guide therefore does not by itself show consensus is too high. This bears directly on the brief's proposed kill rule (FY27 guide margin at or above ~18%). [computed §4]

## 2. Answers to the assignment

**Q1. 2024 annual incentive (AEIP; renamed "AIP" in the 2026 proxy)**

Design:
- The GE compensation committee approved the goals before the spin, and GEV's own compensation committee (CHCC) ratified them in early 2024.
- Payout is 50% at threshold, 100% at target and 200% at maximum, linearly interpolated.
- A safety and sustainability modifier adds or subtracts up to 10pts; it is applied additively. An individual performance factor (IPF) ranges 0–150%. Total payout is capped at 200%. [S1: 2025 proxy pp.49–50] [S2: 2025 proxy p.3 program summary, a separate section of the same document; also 424B3 0001996810-25-000052]

| Metric (weight) | Threshold | Target | Max | Result | Payout |
|---|---|---|---|---|---|
| FCF (40%) | $500M | $1,000M | $2,000M | $1,701M | 170% |
| Adj EBITDA (40%) | $1,500M | $2,000M | $3,000M | $2,035M | 104% |
| Organic revenue growth (20%) | 2.5% | 5% | 10% | "7%" (actually 6.56%) | 131% |

- Business-performance factor 136%; modifier −10% (three fatalities); CEO IPF 130%; CEO payout $3,206,385 (164%). Other NEOs were paid 126–134%.
- The Power segment leader was weighted 80% on Power: payouts 118% / 135% / 134%, Power EBITDA $2,268M. Segment targets were withheld as competitively sensitive. [S1: 2025 proxy pp.54–55] [S2: results match the 4Q24 release: adjusted EBITDA $2,035M, FCF $1,701M, organic revenue $34,771M vs $32,630M]
- The proxy's "7%" is rounded. The 131% payout only reconciles with 6.56% growth (computed §4).

**Q2. 2025 annual incentive**

Same weights and payout curve. Goals were approved by the CHCC in early 2025. [S1: 2026 proxy p.46]

| Metric (weight) | Threshold | Target | Max | Result | Payout |
|---|---|---|---|---|---|
| FCF (40%) | $2,000M | $2,500M | $3,500M | $3,710M | 200% |
| Adj EBITDA (40%) | $2,400M | $2,900M | $3,900M | $3,196M | 130% |
| Organic revenue growth (20%) | 2.6% | 5.2% | 10.4% | 9.3% | 178% |

- Business-performance factor 157% including the −10% modifier (four fatalities). CEO: target 150% of $1.5M salary, IPF 130%, calculated $4.59M, capped at $4.50M (200%). Other payouts: CFO 181%, Power leader 191%, Electrification Systems leader 200%, CHRO 196%.
- Segment leg payouts: Power 200% / 146% / 199%; Electrification Systems 200% / 170% / 200%. [S1: 2026 proxy pp.50–53] [S2: 4Q25 release: adjusted EBITDA $3,196M, FCF $3,710M, organic revenue $37,818M vs $34,608M = +9.28%]
- The metric definitions match the reported non-GAAP figures exactly in both years, so there is no compensation-only adjustment.

**Q3. PSUs**
- **2024 PSUs (2024–26):**
  - Metrics: 50% cumulative adjusted EBITDA, 50% cumulative FCF, with a relative-TSR modifier of ±20% against the S&P 500 Industrials. The modifier cuts below the 20th percentile and adds above the 80th; TSR is measured from the spin.
  - Payout 50/100/200%. Targets are not disclosed until the period ends. [S1: 2025 proxy pp.51, 55] [S2: 2025 proxy p.3 summary]
- **2025 PSUs (2025–27):**
  - Same metrics, but the relative-TSR bands moved to at/below the 25th and at/above the 75th percentile. Both bands are now easier to trigger.
  - Targets are not disclosed. [S1: 2026 proxy pp.46, 53] [S2: 2026 proxy p.39 summary]
- **FY27 sits inside the 2025–27 PSU window**, and presumably the 2026–28 window, although that grant's terms are not disclosed.
- **Pay mix:** long-term incentive (LTI) grants are 50% PSU / 30% RSU / 20% options. The CEO's target LTI rose from $9.5M to $11M in 2025. [S1: 2026 proxy p.53–54] [S2: 10-K 0001996810-26-000015 Note 17 confirms PSUs, RSUs and options under the 2024 LTIP]
- **Pre-spin reference point:** GE's 2023 PSUs were certified 175% for 2023 and at target for 2024–25, times a 1.2x TSR factor, for 150% overall. [S1: 2025 proxy p.56] [SINGLE-SOURCE]

**Q4. 2026 targets.** None are disclosed. The only forward-looking item is the 2026 peer group: Halliburton, Honeywell and Vestas out; RTX, IBM, Cisco and NextEra in. [S1: 2026 proxy p.48] [SINGLE-SOURCE]

**Q5. Bonus targets vs guidance issued around the same time**

Timing:
- FY24: the GE guide came out on 2024-01-23 and the bonus goals were approved pre-spin, i.e. at about the same time.
- FY25: the guide came out on 2024-12-10, was reaffirmed on 2025-01-22, and the goals were approved in early 2025, i.e. after the guide.

| Year / metric | Guide at the time | Bonus target | Target vs guide |
|---|---|---|---|
| FY24 FCF | $0.7–1.1B | $1,000M | +11.1% vs midpoint; 9% below top; threshold ($500M) under the low end |
| FY24 adj EBITDA | Mid-single-digit margin, "toward the higher end", on $34–35B | $2,000M (5.80% on $34.5B) | In the upper part of a $1.70–2.10B grid; matches the later 5.5–6% narrowed guide (midpoint ≈ $2.0B) |
| FY24 organic growth | $34–35B implies +2.3% to +5.3% reported | 5.0% | Upper end |
| FY25 FCF | $2.0–2.5B | $2,500M | At the top (+11.1% vs midpoint); threshold = low end |
| FY25 adj EBITDA | High-single-digit margin on $36–37B | $2,900M (7.95%) | 0.7% below the 8% mid-case ($2,920M); grid $2.52–3.33B |
| FY25 organic growth | $36–37B implies +3.0% to +5.9% | 5.2% | Upper half (midpoint 4.5%) |

[guide S1: GE 8-K EX-99 0000040545-24-000024; S2: GEV 1Q24 release 0001996810-24-000004 ("reaffirmed … $34-35 billion … high end of mid-single digits … $0.7-1.1 billion"). FY25 S1: Dec-2024 investor-update PDF; S2: 4Q24 release 0001996810-25-000004 ("$36-$37 billion, high-single digits … $2.0-$2.5 billion"); Reuters 2024-12-11 for revenue]

- **Verdict: targets are at guidance.** EBITDA targets are at about the midpoint; FCF targets are at the top; thresholds are at or below the low end. No year shows a target below guidance.
- **Caveat:** the qualitative margin guides ("MSD", "HSD") need a numeric interpretation, so the EBITDA comparison is a grid, not an exact figure.

**Q6. What the pay design implies for the late-January 2027 FY27 guide (evidence, not a forecast)**
1. **Guides and bonus targets are set in the same window.** The FY27 guide will be the first annual guide issued in January rather than at a December event, and the CHCC approves goals "in early" the year. [S1: 2026 proxy p.46] [S2: master brief / BR-44; D04_jan_guide_A]
2. **In both years the target equalled the guide, and actuals beat the target:** EBITDA by 1.8% and 10.2%, FCF by 48–70%. A guide that consensus beats by a similar amount would reproduce the FY24–25 payouts.
3. **The payout curve is steep and capped.** Each $100M of adjusted EBITDA above the FY25 target added 10pts on that metric, or 4pts to the business-performance factor. The CEO hit the 200% cap in 2025, so beyond a certain point the benefit is in setting a beatable target, not in beating it further.
4. **The outgoing CFO has no stake in FY27 results.**
   - Parks retires on 2027-04-02 and gets a prorated 2027 bonus "at target performance".
   - McDonough's 2027 target LTI grant ($5.225M) is "expected in 2027", so its targets will be set around the time of the guide. Her make-whole package is $14.5M, half in PSUs (grant timing not stated). [S1: 8-K 0001996810-26-000153] [S2: CFO Dive 2026-08-28; Reuters 2026-08-27]
   - D04 cites GEV's release saying Parks runs the calls through the 2026 10-K, i.e. he presents the January call.
5. **Counter-evidence:** the EBITDA leg paid near target in 2024 (104%), so margin guides have not been heavily lowballed. The margin, not the dollars, is where the guide sits closest to the outcome. That is consistent with the brief's finding that margin ended slightly below the mid-year raised guides.

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY24 bonus goals (FCF, adj EBITDA, organic growth) | $500/1,000/2,000M; $1,500/2,000/3,000M; 2.5/5/10% | 2025 DEF 14A p.54 | none independent; internal check: the 136% factor and $3,206,385 CEO payout reconcile exactly | [SINGLE-SOURCE] (also searched StockTitan and Exa) | H |
| 2 | FY25 bonus goals | $2,000/2,500/3,500M; $2,400/2,900/3,900M; 2.6/5.2/10.4% | 2026 DEF 14A p.50 | internal: 157% factor and $1,805,500 CFO payout reconcile | [SINGLE-SOURCE] | H |
| 3 | FY24 actuals | Adj EBITDA $2,035M; FCF $1,701M; organic +6.56% | 4Q24 8-K 0001996810-25-000004 | 4Q25 8-K 0001996810-26-000012 (prior-year column) | exact | H |
| 4 | FY25 actuals | $3,196M; $3,710M; +9.28% | 4Q25 8-K | 2026 proxy p.50; CEO shareholder letter ("$3.2B … $3.7B") | exact | H |
| 5 | FY24 first guide | $34–35B; margin mid-single digits toward higher end; FCF $0.7–1.1B | GE 8-K 0000040545-24-000024 | GEV 1Q24 8-K 0001996810-24-000004 | exact | H |
| 6 | FY25 first guide | $36–37B; high-single-digit margin; FCF $2.0–2.5B | Dec-2024 investor-update PDF | 4Q24 8-K; Reuters 2024-12-11 (revenue) | exact | H |
| 7 | CEO bonus payouts | $3,206,385 (164%); $4,500,000 (200%, capped) | 2025/2026 proxies | AFL-CIO Paywatch; Creately | exact | H |
| 8 | PSU design | 50/50 adj EBITDA/FCF, ±20% relative TSR, cap 200%; bands 20/80 (2024) → 25/75 (2025) | 2025 proxy p.51; 2026 proxy p.46 | proxy summary pages; 10-K Note 17 (PSUs exist, no terms) | exact on design | M–H |
| 9 | PSU targets undisclosed until period end | — | 2025 proxy p.55 | 2026 proxy p.53 | exact | H |
| 10 | CFO transition terms | $1M salary, 100% bonus target, $5.225M LTI in 2027, $14.5M make-whole, $5M sign-on; Parks' 2027 bonus at target | 8-K 0001996810-26-000153 | CFO Dive 2026-08-28; Reuters 2026-08-27 | exact | H |

## 4. Arithmetic

**Payout interpolation**
- Payout = 100 + (actual − target)/(max − target) × 100 above target.
- FY24 FCF: 100 + 701/1,000 × 100 = 170.1%.
- FY24 EBITDA: 100 + 35/1,000 × 100 = 103.5%.
- FY24 organic growth: 34,771/32,630 − 1 = 6.561%, so 100 + 1.561/5 × 100 = 131.2%.
- FY25 FCF: $3,710M is above the $3,500M maximum, so 200%.
- FY25 EBITDA: 100 + 296/1,000 × 100 = 129.6%.
- FY25 organic growth: 37,818/34,608 − 1 = 9.275%, so 100 + 4.075/5.2 × 100 = 178.4%.

**Business-performance factor**
- FY24: 0.4×170 + 0.4×104 + 0.2×131 = 135.8%.
  - CEO: 1,957,500 × (1.36 − 0.10) × 1.30 = $3,206,385 ✓.
- FY25: 0.4×200 + 0.4×130 + 0.2×178 = 167.6%; less 10 = 157.6%.
  - CEO: 2,250,000 × 1.57 × 1.30 = $4,592,250, capped at $4,500,000 ✓.

**Targets vs guide**
- FCF: 1,000/900 = 1.111; 2,500/2,250 = 1.111.
- FY24 EBITDA grid (5–6% × $34–35B): $1,700–2,100M. Target margin 2,000/34,500 = 5.80%.
- FY25 EBITDA grid (7–9% × $36–37B): $2,520–3,330M. Mid-case 8% × 36.5 = $2,920M; target/mid = 0.993.
- Implied revenue growth: FY24 34/33.239 = +2.29% to 35/33.239 = +5.30%. FY25 36/34.935 = +3.05% to 37/34.935 = +5.91%.

**Targets vs prior-year actuals**
- FY24 targets: 2,000/807 = 2.48x; 1,000/442 = 2.26x.
- FY25 thresholds: 2,400/2,035 = +17.9%; 2,000/1,701 = +17.6%.
- FY25 targets: +42.5% (EBITDA), +47.0% (FCF).

**Actual vs target**
- EBITDA: 2,035/2,000 = +1.75%; 3,196/2,900 = +10.2%.
- FCF: +70.1%; +48.4%.

**FY27 cushion grid**
- Implied guide midpoint = consensus $9,574M / (1 + cushion).
- 1.75% cushion → $9,409M = 17.84% of $52,740M consensus revenue.
- 10.2% cushion → $8,688M = 16.47%.

**PSU context (inference; targets undisclosed)**
- 2025–27 cumulative FCF before FY27 = 3,710 + 11,500–12,500 = $15.2–16.2B. That already exceeds the Dec-2024 framework of at least $14B for all four years 2025–28, the plan in force when the 2025 PSU targets were set.
- 2024–26 cumulative FCF = 1,701 + 3,710 + 11,500–12,500 = $16.9–17.9B.
- 2024–26 cumulative adj EBITDA = 2,035 + 3,196 + (12% × 45.5 = 5,460 to 14% × 46.5 = 6,510) = $10.7–11.7B.

## 5. General question bank items answered

- **G17 (what management controls):** guidance is set in the same window as the bonus targets, and both years paid above target. Management and the board control both the guide level and the bonus goals.
- **G22 (what has to change in guidance):** the pass mark for the January 2027 guide needs to allow for a typical 2–10% EBITDA cushion (§4 grid).
- **G24 (SBC and cash):** bonus and PSU FCF are reported FCF, so the deposit-driven FCF counts fully toward pay. FCF paid 170–200%.
- **G20 (definition traps):**
  - The proxy's "7%" organic growth was 6.56%.
  - Segment "EBITDA" in the bonus is not the company adjusted EBITDA.
  - "AEIP" (2025 proxy) and "AIP" (2026 proxy) are the same plan.

## 6. What would change this

- If the 2027 proxy shows a FY26 bonus EBITDA or FCF target materially above the Jan-2026 guide (FY26 guide at the time: 12–14% margin; first FCF guide $4.5–5.0B), the "targets are set at guidance" pattern breaks.
- If the January 2027 guide comes with an explicit statement that it is set at the Street's level, or if the FY27 bonus is re-weighted toward margin, the cushion reading weakens.
- If the 2024–26 PSU targets, to be disclosed in spring 2027, turn out to be close to actuals rather than far below them, the reading of multi-year plans as conservative weakens.

## 7. Disagreements with the master brief

- **"First under the new CFO":** McDonough becomes CFO on 2027-01-01, but per D04 (citing the GEV release and CFO Dive), Parks presents the Q4'26 call. Parks' 2027 bonus is fixed at target, so he has no stake in FY27 results.
- **Kill rule "FY27 guide margin ≥ ~18%":** the pay record implies the guide is normally set 2–10% below the eventual actual. A 16.5–17.8% guide is consistent with the Street being right. The team may want the pass mark to reflect this.

## 8. Open items

- The FY26 bonus goals and the 2026–28 PSU targets. Look in the spring-2027 DEF 14A and in any 8-K on 2027 grants.
- Street consensus at the time each bonus target was set (Jan-2024, Jan-2025), to test target vs consensus. Needs point-in-time consensus from FactSet or Visible Alpha.
- Segment-level bonus targets are withheld in both proxies.
- Say-on-pay vote results. Look in the 8-K Item 5.07 filings from May 2025 and May 2026.
- The grant date and performance period of McDonough's make-whole PSUs. The offer letter is to be filed with the Q3'26 10-Q.
