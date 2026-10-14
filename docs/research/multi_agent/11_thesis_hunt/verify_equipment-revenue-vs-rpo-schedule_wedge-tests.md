# Checker working: 13 wedge tests on "equipment revenue vs RPO schedule"

_AI-assisted research input only. Facts, arithmetic, tables and sources. No memo sentences, no forecast chosen for the team. Bloomberg data: cite as "Bloomberg, 2026-10-01"; keep inside the project folder._

Working date 2026-10-01. All figures $M unless stated. Y1 = equipment RPO x the "within 1 year" share in the RPO note. Street = Bloomberg BEst mean.

## 0. Verdict

| Item | Result |
|---|---|
| Survives the 13 tests | **No** |
| Key numbers reproduced from primary files | Yes (every figure in proof A, B, C, E, F, H re-computed; two rounding slips, section 1) |
| Tests passed | 6 of 13: line-item, consensus-side, why-missed (weak), cash (weak), reveal-date, counter-move (weak) |
| Tests failed | 7 of 13: distance, ratio, physical-quantity, rival-explanation, error-band, already-priced, multiple-consistency |
| Required passes (line-item, distance, error-band, reveal-date) | 2 of 4 (distance and error-band fail) |
| Use that remains | A supporting fact for the revenue line of a model and a dated check (10-K schedule at 12/31/26 vs Street FY27 equipment $32,383M). Not a wedge by itself |

## 1. Reproduction (primary files)

Sources: RPO note sentences pulled from `gev.db` chunks for accessions 0001193125-24-063739, 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148; equipment revenue from XBRL `RevenueFromContractWithCustomerExcludingAssessedTax` / Product in `data/financials/gev_segments.csv`; Street from `GEV_Pull_2026-10-01/segment_quarterly.json` (Bloomberg, 2026-10-01).

| Check | Candidate | Re-computed | Match |
|---|---|---|---|
| 10-Q sentence, 6/30/26 | 87,821; 36% / 65% / 97% | same text found in 0001996810-26-000148 | yes |
| Y1 | 31,616 (31,176-32,055) | 31,615.6 (31,176.5-32,054.7) | yes |
| Street four-quarter equipment | 30,245 = 7,482 / 8,339 / 6,675 / 7,748 | 30,244.95, same quarters | yes |
| By division | Power 10,874, Wind 5,830, Electrification 13,541 | same | yes |
| Street total revenue, EBITDA, services | 50,019; 8,210; 19,790 | 50,019; 8,210; 19,790 | yes |
| Street / Y1 | 0.957 | 0.9566 | yes |
| Seven back-test ratios | 0.918, 1.028, 1.036, 1.076, 1.105, 1.052, 1.066 | 0.9180, 1.0283, 1.0358, 1.0760, 1.1052, 1.0516, 1.0658 | yes |
| Seven-window mean, sd | 1.040, 0.060 | 1.0401, 0.0597 | yes |
| Six post-spin mean, sd, min | 1.061, 0.028, 1.028 | 1.0605, 0.0283, 1.0283 | yes |
| Median | 1.050 | 1.0516 | slip of 0.002 |
| H1 2027 residual | 15,795 vs 14,424 = +9.5% | 15,794 vs 14,424 = +9.5% | yes |
| Total-revenue form | 45,770; Street 1.093; history mean 1.142 | 45,770; 1.0928; 1.1426 | yes |
| Division equipment RPO 6/30/26 | 39,261 / 8,197 / 40,589 | found in 10-Q MD&A segment tables | yes |
| Prolec equipment Q1, Q2 2026 | 469, 834 | 469 (Q1 organic reconciliation); 860 total acquisitions in Q2 | yes |
| Schedule-to-schedule change | +2,765 | +2,764 | slip of 1 |

Basis note: Bloomberg division equipment lines are on segment basis (Q2 2026 actuals 1,965 / 1,395 / 3,130 = 6,490 against consolidated equipment revenue 6,459). The Street sum therefore carries about $30M a quarter of intersegment sales; on consolidated basis the Street is about $30.1B.

## 2. New evidence found by this check

### 2a. The back-test ratio moves with how much growth the schedule demanded

Demanded growth = Y1 / trailing-four-quarter equipment revenue - 1. Realised growth = next-four-quarter equipment revenue (ex-Prolec) / trailing four quarters - 1.

| Backlog date | Y1 | Trailing 4Q equipment | Demanded growth | Realised growth | Ratio |
|---|---|---|---|---|---|
| 12/31/23 | 20,644 | 18,258 | +13.1% | +3.8% | 0.918 |
| 3/31/24 | 18,994 | 18,386 | +3.3% | +6.2% | 1.028 |
| 6/30/24 | 19,534 | 18,192 | +7.4% | +11.2% | 1.036 |
| 9/30/24 | 19,352 | 18,613 | +4.0% | +11.9% | 1.076 |
| 12/31/24 | 18,941 | 18,952 | -0.1% | +10.5% | 1.105 |
| 3/31/25 | 20,465 | 19,532 | +4.8% | +10.2% | 1.052 |
| 6/30/25 | 20,879 | 20,232 | +3.2% | +10.0% | 1.066 |
| 9/30/25 (open) | 22,178 | 20,822 | +6.5% | | |
| 12/31/25 (open) | 23,771 | 20,934 | +13.6% | | |
| 3/31/26 (open) | 28,851 | 21,991 | +31.2% | | |
| **6/30/26 (open)** | **31,616** | **23,556** | **+34.2%** (about +26% with Prolec taken out of both sides) | | Street 0.957 |

- Correlation between demanded growth and the ratio: **-0.93** (seven windows), **-0.74** (six post-spin windows).
- The six windows that beat the schedule are all windows where the schedule demanded -0.1% to +7.4% growth. The one window that demanded double-digit growth (+13.1%) missed by 8.2%.
- The current window demands +34% (+26% organic). No completed window is in that range. The 1.040 multiplier is being applied outside the sample it was measured on.
- Realised growth was steadier than the ratio: mean +9.1%, sd 3.0% (post-spin +10.0%, sd 2.0%), against a ratio sd of 6.0% (post-spin 2.8%).

### 2b. A naive model beat the schedule model in the same back-test

| Model for next-four-quarter equipment revenue | Leave-one-out RMSE, seven windows |
|---|---|
| Y1 x mean ratio (the candidate's method) | 6.4% (largest error 14.2%) |
| Trailing four quarters x (1 + mean growth) | 3.2% |

- Naive model applied today: (23,556 - 1,303) x 1.10 + about 3,500 Prolec = about $28.0B, which is 7.5% BELOW the Street. The Street (+28% reported, about +20% organic) already assumes twice the growth of any completed window.
- Fair reading: growth is accelerating (H1 2026 equipment +28.8% reported, +14.5% organic; guide-implied H2 2026 about +19% organic), so the naive model is breaking and the schedule may carry real information now. The back-test cannot show that, because it has no completed high-growth window.

### 2c. The 12/31/23 window, adjusted

The EDF disposal removed $3,708M of equipment RPO (investor-update reconciliation, corpus source 1844: adjusted equipment backlog $36,770M at 12/31/23). With that RPO taken out at a 25-51% one-year share and about $350M of pre-disposal revenue removed (assumed, not disclosed), the 12/31/23 ratio becomes about 0.94-0.99. Seven-window statistics with 0.97 in place of 0.918: mean 1.048, sd 0.043. The window is still at or below 1.00 and still the lowest.

### 2d. Open windows, reported quarters only

| Stage | Window | Share of Y1 reported so far (ex-Prolec) | Same stage in earlier windows | Those windows ended |
|---|---|---|---|---|
| After 3 quarters | 9/30/25 | 73.8% | 77.2% (9/30/24) | 1.076 |
| After 2 quarters | 12/31/25 | 43.8% | 48.0% (12/31/24); 37.8% (12/31/23) | 1.105; 0.918 |
| After 1 quarter | 3/31/26 | 22.4% | 22.1% (3/31/24); 23.9% (3/31/25) | 1.028; 1.052 |

Two of three open windows run 3-4 points of Y1 behind the 2025 windows. With guide-anchored H2 2026 they finish at about 1.00-1.04, not 1.06-1.10.

### 2e. The Street number on this sub-line is soft

From `06_modl.xlsx` (Bloomberg, 2026-10-01), Q3 2026:

| Line | Mean | Median | Low | High |
|---|---|---|---|---|
| Power equipment | 2,394 | 2,433 | 2,063 | 2,591 |
| Wind equipment | 1,789 | 1,813 | 1,274 | 2,244 |
| Electrification equipment | 3,299 | 3,369 | 2,301 | 3,849 |
| Sum | 7,482 | 7,615 (+1.8%) | 5,638 | 8,684 |
| Total revenue (28 analysts) | 11,993 | 11,972 | 11,469 | 12,384 |

- Broker-level cells for the equipment rows are masked on this export, so the number of contributors is not visible. The Electrification equipment low (2,301, against a segment total low of 2,995) looks like a model that does not yet include Prolec, which pulls the mean down.
- Headline revenue has 28 contributors and a 7.6% low-to-high spread. The equipment sum has a 41% low-to-high spread.

Street after each correction, and the gap:

| Street basis | Street | Schedule only | Schedule x 1.00 to 1.03 | Schedule x 1.040 | Schedule x 0.918 |
|---|---|---|---|---|---|
| Mean, segment basis (candidate) | 30,245 | +4.5% | +4.5% to +7.7% | +8.7% | -4.0% |
| Electrification services row corrected | 30,545-30,685 | +3.0% to +3.5% | +3.0% to +6.6% | +7.2% to +7.6% | -5.0% to -5.4% |
| Scaled to Q3 medians (x1.018) | 30,780 | +2.7% | +2.7% to +5.8% | +6.8% | -5.7% |
| Consolidated basis (less about 120 intersegment) | 30,125 | +4.9% | +4.9% to +8.1% | +9.1% | -3.7% |

### 2f. Physical cross-check (gas output)

- Management, Q2 2026 call (corpus source 3161): gas output moves from about 3 GW a quarter to 5 GW a quarter from Q3 2026; at least 30 GW over the next six quarters. Conference 2026-09-16 (source 681): 6 GW a quarter in H2 2027.
- 10-Q units table: gas turbine GW sold 3.3 in Q2 2026 (5.2 a year earlier), 7.5 in H1 2026 (8.2).
- Four-quarter window: 20 GW against 14.6 GW trailing = +37%. Street Power equipment 10,874 against 7,373 trailing = **+47%**. Street Power equipment per kW shipped: $544 against $505 trailing (+7.7%).
- If Power carried the whole floor gap (+1,371): $612 per kW, +21% on trailing.
- H1 2027: 10 GW against 7.5 GW (+33%); Street Power equipment 5,383 against 3,834 (+40%).
- Wind: H1 2026 orders 1.2 GW against 1.8 GW (-33%); Street H1 2027 wind equipment flat on H1 2026. Points below the Street for Wind (proposal file, section 6).
- Electrification: management's Q3 guide $3.8-4.0B against Street $3,881M.
- Reading: the physical count reproduces the Street (to about +5%), not the schedule. To hold the schedule with Power capped by output and Wind at or below Street, Electrification equipment in H1 2027 would need to be $1.4B to $2.2B (21-33%) above the Street's 6,763.
- Limit of this check: Power equipment revenue per GW is not stable ($351 per kW in H1 2025, $511 in H1 2026), so GW output is a loose ceiling on dollars, not a hard one.

### 2g. Price history against revisions (Bloomberg, 2026-10-01)

| Date | Price | Fwd EV/EBITDA | Street FY27 revenue | Street FY27 EBITDA |
|---|---|---|---|---|
| 2025-10-03 | 594.99 | 32.5x | 45,498 | 6,987 |
| 2026-01-02 | 679.55 | 32.6x | 48,075 | 8,003 |
| 2026-04-03 | 898.57 | 35.7x | 50,615 | 8,631 |
| 2026-07-03 | 1,113.11 | 37.2x | 51,919 | 9,273 |
| 2026-10-01 | 987.45 | 27.9x | 52,949 | 9,451 |

- Twelve months: FY27 revenue estimate +16.4%, FY27 EBITDA estimate +35%, multiple -14%.
- Since 2026-07-03: estimates +2%, price -11%, multiple -25%.
- Report-day moves: 2026-01-28 +2.7% (revenue about 7.5% above consensus); 2026-07-22 -8.7% (revenue about 2.9% above consensus, revenue guide raised, margin guide held).
- FY27 EBITDA estimates: mean 9,471, sd 917 (9.7% of mean), high 11,029 (+16.5%), 36 analysts.
- Sell-side stance: 32 Buy, 7 Hold, 2 Sell; mean target $1,225 (+24%).

## 3. The 13 tests

| # | Test | Result | Evidence |
|---|---|---|---|
| 1 | Line-item | **Pass**, with limits | Named line (consolidated equipment revenue), sourced consensus ($30,245M, Bloomberg division rows), named period (Q3 2026 to Q2 2027). Limits: the period straddles two fiscal years, which is not how consensus is published; contributor count on the sub-line is not visible; the Street sum is on segment basis |
| 2 | Consensus-side | **Pass** | The number rebutted is the mean of the division consensus, which ties to the 28-analyst headline within $16M, not an outlier. Limit: the direction (long) is the same side as 32 of 41 ratings |
| 3 | Distance | **Fail** | Checkable floor +4.5% (+2.7% to +3.5% after the Street corrections in 2e). The 8.7% needs the full seven-window multiplier, which 2a and 2d do not support for this window; at the 1.00-1.03 the open windows point to, the gap is +3.0% to +7.7%. Total revenue +2.7% to +5.3%. EBITDA +1.5% to +6.6%. Only the uncorrected sub-line at the full multiplier clears 7% |
| 4 | Ratio | **Fail** | No target given. EBITDA gap about +2% to +6%; any long target near the sell-side mean (+24%) is 4x to 12x the gap, so the return would be multiple. The price-implied lens says the gap offsets a multiple drift (28.5x to 24.6x), not adds return |
| 5 | Physical quantity | **Fail** | The one physical quantity (gas GW shipped, guided 5 GW a quarter) is already covered by the Street (Power equipment +47% against GW +37%). Wind GW orders point below Street. "Share of backlog converted" is not a physical quantity and has no ceiling. See 2f |
| 6 | Rival explanation | **Fail** | Not excluded: (a) the schedule is more back-loaded or slips, as in the one double-digit-demand window; (b) rounding of 36% is worth +/-$439M (1.4%); (c) Street sub-line measurement (mean vs median, services row, a stale contributor) is worth 1.0-1.8 points; (d) the past uplift is explained by steady 10% growth against a noisy schedule (correlation -0.93). The split between Power and Electrification is not identified |
| 7 | Error band | **Fail** | Back-test error: sd 6.0%, leave-one-out RMSE 6.4%, largest error 14.2%; with about two independent years the predictive sd is about 7.3% (about 5.3% using the adjusted 12/31/23 window). Gap claimed 8.7% (6.8-7.6% on corrected Street): 1.1 to 1.6 predictive sd. Floor gap 4.5% is smaller than the error. A naive model has half the error (3.2%) and gives a figure below the Street. Current window is outside the sampled range of demanded growth |
| 8 | Why missed | **Pass**, weak | Footnote only, rounded percentage, no dollar figure, no division split, no Bloomberg field. Corpus and web search: the 36% is quoted in press (2026-07-23, 2026-08-21/22) as a visibility or slow-conversion point; no piece found that multiplies it out or sets it against consensus; not discussed on the Q2 2026 call. Sell-side notes could not be checked |
| 9 | Already priced | **Fail** | Street FY27 revenue has risen 16% and FY27 EBITDA 35% in twelve months while the multiple fell 14%; a further +3% to +5% on revenue is one to two quarters of the normal drift. Revenue beats of 3-7% drew +2.7% and -8.7% on the day. Price-implied lens: a flat price already needs NTM EBITDA 5.4-6.4% above Street (that regression was not re-run in this check). See 2g |
| 10 | Cash | **Pass**, weak | Reported revenue and EBITDA dollars do move: +$0.14B to +$0.54B on a $8,210M base (+1.5% to +6.6%). Limits: that is 0.2 to 0.7 of one standard deviation of FY27 EBITDA estimates; margin percentage falls 0.2-0.6 point; nets to about zero if Street services are 2-6% high; no free-cash-flow effect shown |
| 11 | Reveal date | **Pass** | Company-reported equipment revenue and a new schedule on 2026-10-28, late January 2027 (10-K schedule at 12/31/26 vs Street FY27 equipment $32,383M; FY27 guide vs $53,029M), late April 2027, late July 2027; all inside 3-12 months. Limits: the pass marks offered differ between lenses and none is fixed yet; the October check is weak because management's Q3 guide equals the Street |
| 12 | Counter-move | **Pass**, weak | Management cannot withhold reported revenue; a cautious January guide would delay the market's reaction, not the print. Customer deferrals are the live risk (one window in seven). Competitors are not relevant inside twelve months. The candidate lists these but does not stress each one |
| 13 | Multiple consistency | **Fail** | No exit multiple or bear-case multiple is given. Available anchors (twelve-month floor 27.3x, peer regression 24.6x, peers 11-22x) all sit at or below the current 27.9-28.5x |

Tests 14 and 15 in the playbook (kill rule, noise): a measurable kill rule is stated (four-quarter equipment revenue at or below Street, or a new one-year amount that falls to the Street). The noise test is not done.

## 4. Corrected figures (ranges and methods only)

| Item | Value | Method |
|---|---|---|
| Street, as given | $30,245M | Mean, segment basis; reproduced |
| Street, corrected range | $30.1B to $30.8B | Consolidated basis (-120); services-row correction (+300 to +440); Q3 median scaling (+535) |
| Schedule | $31,616M ($31,176M to $32,055M) | 36% (35.5% to 36.5%) x 87,821 |
| Uplift multiplier supported by this check | 1.00 to 1.03 | Open windows on reported quarters and guide (2d); decay as demanded growth rises (2a) |
| Value range | $31.2B to $32.6B; $32.9B only at the full 1.040; $29.0B on a repeat of 0.918 | Schedule x multiplier |
| Gap, centre | about +5.5% (range +3% to +9%) | Mid-range value against Street mean and corrected Street |
| Error band on the value | about +/-7% (one predictive sd; +/-5% with the adjusted 12/31/23 window) | sd 6.0%, about two independent years |
| Total revenue gap | +2.7% to +5.3% | Equipment gap carried to the $50,019M total |
| EBITDA gap | +1.5% to +6.6% | 13% to 20.5% drop-through |

## 5. What would change this verdict

| Observation | Date | Effect |
|---|---|---|
| Q3 2026 10-Q: one-year amount at 9/30/26 at least 5% above Street Q4 2026 to Q3 2027 equipment ($31,314M) AND Q3 equipment revenue above about $7.6B | 2026-10-28 | First completed data point with demanded growth above 6%; would start to answer 2a |
| 10-K schedule at 12/31/26 of $34B or more against Street FY27 equipment $32,383M, with FY26 equipment landing at or above the 12/31/25 schedule x 1.03 | Late January 2027 | Turns the claim into a fiscal-year line (FY27 equipment) with a gap of 5% or more and a completed double-digit-demand window |
| Division one-year shares, or a broker note already using the schedule | Any | Settles tests 6 and 8 |

Scripts: scratchpad `wt_backtest.py` (re-computation of sections 1 and 2).
