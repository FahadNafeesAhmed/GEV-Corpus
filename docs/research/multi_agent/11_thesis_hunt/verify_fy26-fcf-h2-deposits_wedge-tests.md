# Verify: fy26-fcf-h2-deposits against the wedge tests

_Checker working. Research input only: facts, arithmetic, tables, sources. No memo sentences, no forecast choices (ranges and methods only). Bloomberg figures: "Bloomberg, 2026-10-01", academic licence, keep inside the project folder._

Units: $M unless stated. "CL" = contract liabilities and deferred income. "SRA" = slot reservation agreement.

## 0. Verdict

**Does not survive.** It fails 7 of the 13 tests, including the error-band test, and the distance test is only marginal. The rule was: no more than two fails, and line-item, distance, error-band and reveal-date must all pass.

| # | Test | Result | One-line reason |
|---|---|---|---|
| 1 | Line-item | Pass | FY26 FCF vs $12,196M (Bloomberg BEst), with Q3 CL balance as a named test line |
| 2 | Consensus-side | Pass, weak | FCF consensus is the real consensus; but the "+10.4% vs mean" CL figure is one outlier broker, and the stock is not valued on FY26 FCF |
| 3 | Distance | Marginal | No single gap. Like-for-like guide record +2.5% to +4.9%; deposit method +12% to +19%. The 19% rests on a median taken only from the guides that were beaten |
| 4 | Ratio | Fail | The gap is one-time cash: $2.3B = $8.6 a share = 0.9% of the price. Any target return is a multiple call |
| 5 | Physical quantity | Pass, with a caveat | Street H2 FCF implies CL growth of about $2.8-3.4B, or roughly 10-20 GW signed; company says about 20 GW is "likely conservative". Needs the k assumption |
| 6 | Rival explanation | Fail | Year-end receivables, cash taxes, inventory for the 5 GW a quarter ramp, deposits passed on to suppliers, and conversions that bring little new cash all explain a low H2 without the Street being wrong |
| 7 | Error band | **Fail** | Back-test error is as large as or larger than the gap at every step (section 3) |
| 8 | Why missed | Fail, partly | The structural gap is real, but every key input is in public remarks, and the quarter-building analysts already sit above the top of the guide |
| 9 | Already priced | Fail | Three guide raises on deposits in 2026; on the last one (+$5B) the stock fell 8.7% |
| 10 | Cash | Pass | Moves reported FCF. Timing only; no EBITDA effect; may pull from FY27 |
| 11 | Reveal date | Pass, with caveats | 2026-10-28 (company events page) and late January 2027. Pass mark must be one number, and Q3 is a weak read on the full-year claim |
| 12 | Counter-move | Fail | Management says it aligns "the timing of inflows and outflows"; FY24 landed on the top of the guide to the dollar, twice |
| 13 | Multiple consistency | Fail | No exit or bear multiple given; a deposit-driven cash beat does not support 28.5x EV/EBITDA |

The playbook also lists a kill test (pass: balance at or below $39.9B on Oct 28; FY26 at or below $12.5B) and a noise test (not addressed).

## 1. What was reproduced from the primary files

| Claim in the candidate | Recomputed | Source | Match |
|---|---|---|---|
| Street FY26 FCF $12,196M | 12,196.26 | `GEV_bloomberg_pull_filled_2026-10-01.xlsx`, Consensus, BEST_ESTIMATE_FCF 1FY | Yes |
| Street Q3 $1,502M, Q4 $1,148M, 15 analysts each | 1,502.2 (15), 1,148.5 (15) | `01_eeo_annual.xlsx` row 27 | Yes |
| Q3 FCF range -$1,622M to +$7,062M, median 1,482 | same | `06_modl.xlsx` row 229 | Yes |
| Q3 current CL: mean 37,492 / median 39,944 / low 19,487 / high 41,817 | same | `06_modl.xlsx` row 172 | Yes |
| Q3 change in CL: mean -1,402 / median -50 / low -8,795 / high +1,873 | same | `06_modl.xlsx` row 205 | Yes |
| H1'26 FCF $9,897M | 10,680 - 783 = 9,897 | XBRL: NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquireProductiveAssets | Yes |
| CL up in 10 of 10 quarters, smallest +379 | +868, +613, +379, +637, +1,107, +900, +553, +5,646, +5,999, +8,088 | `gev_quarterly.csv` ContractLiabilities | Yes |
| Median = reported 6/30/26 current balance | 40,037 - 93 = 39,944 | `gev_quarterly.csv` | Yes |
| Segment CL: Power 12,645 / 16,547 / 20,400 / 27,685 etc. | same | `gev_segments.csv` | Yes |
| Guide levels: 3.0-3.5 (Jul-25), 11.5-12.5 from 6.5-7.5 (Jul-26) | same | 8-K EX-99 0001996810-25-000132, 0001996810-26-000147 | Yes |
| Six guide remainders, five above the top | 1.02-1.52 vs 2.73; 1.83-2.33 vs 2.54; 1.10-1.60 vs 1.81; 1.60-2.10 vs 1.81; FY26 5.0-5.5 vs 9.90 in H1; 1.71-2.71 vs 5.11 in Q2 | XBRL cumulative FCF | Yes |
| k = 0.48 / 0.36 / 0.32 / 0.75 | same from the candidate's own inputs | section 3.3 of `propose_winners-pattern.md` | Yes |
| Q3 build +571 / -291 / +1,601 | 570.8 / -290.9 / 1,601.1 | `segment_quarterly.json` Orders and Revenue, 2026 Q3 | Yes |
| Stock -8.7% on 2026-07-22 | 1,078.81 to 985.03 = -8.7% | PricePositioning sheet | Yes |
| CFO: H1 FCF "substantially higher than the second half, as many of these slot reservations convert to orders" | verbatim | Q2'26 call transcript, corpus `sources` id 3161 | Yes |
| Reveal 2026-10-28 | company events page per `E07_catalyst_calendar.md` line 13; the corpus `catalyst_calendar` table still shows an estimated 10-21 | | Yes (E07 governs) |

Errors and gaps found in the candidate:

1. **H2 Street on two bases.** Annual BEst implies H2 of 12,196 - 9,897 = **$2,299M**. The quarterly sum is $2,651M, which gives FY26 of **$12,548M, above the $12.5B top of the guide**. The 15 analysts who build quarters already assume a small beat. Against 12,548 every gap is about 3 points smaller (14.5 is +15.6%, not +19%).
2. **The 1.79x multiplier is a selected median.** It is the median of the five guides that were beaten (79, 9, 13, 80, 88), two of which are not finished. The median of all six in the candidate's list is 46%. Adding the three 2024 guides the candidate left out (+34%, 0%, 0%) the median of the eight finished cases is **+11%**.
3. **The low end of the Power deposit range drops the 1.12 fit factor.** 18 x 0.95 x 25% x 1.12 - 0.4 = 4.4, not 3.9. The stated 3.9 is 18 x 0.95 x 25% - 0.4.
4. **"+10.4% vs the mean" is one broker.** See section 2.
5. **"Five of six" is two fiscal years**, not six trials: four guides are scored against FY25 and two against H1'26.

## 2. What the Street's contract-liability rows really say

Contributor count is hidden. The four statistics (mean 37,492; median 39,944; low 19,487; high 41,817) are only arithmetically possible with **7 or more brokers** (n = 3 to 6 is infeasible).

| Brokers assumed | Mean balance without the 19,487 entry | Mean change in CL without the -8,795 entry |
|---|---|---|
| 7 | 40,493 | -170 |
| 8 | 40,064 | -346 |
| 10 | 39,493 | -581 |
| 12 | 39,129 | -730 |

- Without the one low entry the Street's balance is $39.1-40.5B, i.e. flat on the reported $39,944M. The usable comparison is the median only.
- The 19,487 entry is not consistent with its own -8,795 change (39,944 - 19,487 = 20,457), so that broker probably defines the line differently.
- Sign convention across brokers on these MODL working-capital rows is not verifiable (inventories +947 mean and contract assets -1,280 mean cannot both be cash-flow signs).

## 3. Error-band test (the decisive one)

### 3.1 Deposit models against reported quarters

Lens A (winners-pattern): SRA GW signed x $/kW x 25% vs change in Power product CL.

| Quarter | Model | Actual | Error |
|---|---|---|---|
| Q2'25 | 1,050 | 930 | +120 (+13%) |
| Q3'25 | 1,950 | 923 | +1,027 (+111%) |
| Q4'25 | 3,938 | 3,933 | +4 (0%) |
| Q1'26 | 4,275 | 3,929 | +346 (+9%) |
| Q2'26 | 4,050 | 7,320 | -3,270 (-45%) |

RMS error **$1,542M a quarter**; mean absolute error 36%.

Lens B (fcf-deposits), fixed parameters as used for Q3'26: 22.5% x change in Electrification equipment RPO + 35% x Wind + 30% x Power + 20% x change in SRA GW x price, vs change in total CL.

| Quarter | Model | Actual | Error |
|---|---|---|---|
| Q2'25 | 1,603 | 900 | +703 (+78%) |
| Q3'25 | 1,605 | 553 | +1,052 (+190%) |
| Q4'25 | 4,846 | 5,646 | -800 (-14%) |
| Q1'26 | 5,235 | 5,999 | -764 (-13%), Prolec in the quarter |
| Q2'26 | 4,749 | 8,088 | -3,339 (-41%) |

RMS error **$1,829M a quarter** (four quarters without Q1'26); mean absolute error 81%.

- Claimed Q3'26 gap: +1,500 central vs Street median -50 = 1,550. Gap / RMS error = **0.85 (lens B), 1.0 (lens A)**. The model cannot tell +$1.5B from zero.
- Both lenses over-predicted the two low-signing quarters most like Q3'26 (Q2'25 and Q3'25) by $0.7-1.05B.
- Inputs: segment equipment RPO and SRA GW as tabulated in `propose_fcf-deposits.md` section 2.1 (10-Q MD&A and releases); CL from `gev_segments.csv`.

### 3.2 Cash kept per dollar of deposit growth (k)

One step ahead, using the prior period's k and the ACTUAL deposit change (perfect foresight of deposits):

| Period | Predicted FCF | Actual | Error |
|---|---|---|---|
| H1'25 (k from FY24, 0.48) | 1,394 | 1,169 | +19% |
| H2'25 (k from H1'25, 0.36) | 2,779 | 2,541 | +9% |
| H1'26 (k from H2'25, 0.32) | 3,972 | 9,897 | -60% |

Mean absolute error 29% of the period's FCF before any error in the deposit forecast.

### 3.3 Combined band

H2'26 FCF = cash before working capital + k x change in CL, candidate's own input ranges (1.0-2.1; k 0.32-0.75; change 3.0-8.0): **$2.0B to $8.1B**, so FY26 **$11.9B to $18.0B = -3% to +48%** vs $12,196M.

Candidate's own stated band: $11.6B to $16.4B = -4.9% to +34.5%; half-width $2.4B = **20% of the Street** against a central gap of 19% (16% on the quarterly-sum Street).

Result: the back-test error is not smaller than the claimed variance at the deposit step, at the k step, or in total. **Fail.**

## 4. Distance test: the gap by method

| Method | H2'26 FCF $B | FY26 $B | vs 12,196 | vs 12,548 (quarterly sum) | Back-test |
|---|---|---|---|---|---|
| Guide top | 2.60 | 12.50 | +2.5% | -0.4% | |
| July guides for H2 only (2024: 0%; 2025: +9%) | 2.60-2.84 | 12.50-12.73 | +2.5% to +4.4% | -0.4% to +1.5% | n = 2 |
| Guides with two quarters or fewer left (0, 0, +9, +13, -14%) | 2.60 (median 0%) | 12.50 | +2.5% | -0.4% | n = 5 |
| All eight finished guides, median +11% | 2.89 | 12.79 | +4.9% | +1.9% | n = 8 |
| Candidate's six, median of all six (+46%) | 3.80 | 13.70 | +12% | +9% | 2 fiscal years |
| Deposit analog, k = 0.32 (H2'25) on $6.4-6.5B | 3.7-3.8 | 13.6-13.7 | +12% | +9% | section 3 |
| Candidate central (1.79x, or k = 0.45) | 4.6 | 14.5 | +19% | +16% | selected median |
| Candidate adverse | 1.7-2.2 | 11.6-12.1 | -5% to -1% | -8% to -4% | |

- The only like-for-like history (a July guide for the second half) gives a gap under 5%, below the 7% floor.
- A gap of 12% or more needs the deposit model, whose error band is wider than the gap.
- No method gives a gap of 7% or more with an error band smaller than the gap. Distance and error-band cannot both pass.

## 5. Evidence for the other tests

**Ratio.** Extra cash per share: $0.6B = $2.3 (0.23% of $987.45); $1.5B = $5.6 (0.57%); $2.3B = $8.6 (0.87%); $4.2B = $15.8 (1.6%). Street FY26 FCF yield on market cap 4.6%, FY27 2.9%. The candidate gives no price target; `BLOOMBERG_VERDICT.md` section 5 scenarios (+6% to +31% at 23x to 28.5x) come from EBITDA and the multiple.

**Physical quantity.** The guide holds if k x change in CL is at most $0.9B, i.e. CL growth of at most $2.8B at k = 0.32 (candidate) or about $3.4B on the bridge in `propose_fcf-deposits.md` section 4.6. Net Power product CL per GW signed: $71-103M (Q2-Q3'25), $164M (Q4'25), $187M (Q1'26), $366M (Q2'26). At $165-281M per GW, $2.8-3.4B is 10-20 GW. Company: about 20 GW in H2, "likely to prove to be conservative", Q4 above Q3 (conference 2026-09-16, corpus src:681). So the guide is consistent with about 20 GW at the Q4'25 rate; upside needs more GW or the H1'26 rate.

**Rival explanations (each can produce a low H2 with deposits still rising).**

| Variable | Evidence | Size |
|---|---|---|
| Year-end receivables | Q4'25 receivables +$2.4B while CL +$5.6B; working capital other than CL -$3,630M in H2'25 | k = 0.32 |
| Cash taxes | H1'26 $1,258M vs $363M in H1'25; cause not disclosed | $0.5-1.0B |
| Inventory for the 5 GW a quarter ramp | Inventories +$1,744M in H1'26 on the cash-flow statement (10,429 to 12,692 on the balance sheet, including Prolec) | $1-2B |
| Deposits passed to suppliers | CEO, Q2'26 call: supply-chain capacity "all funded by customer down payments" | not sized |
| Conversions bring little new cash | CFO, Q2'26 call (quote above) | the stated reason for H1 above H2 |
| Capex phasing | Street FY26 capex 1,706 less H1 783 = 923 in H2 | +$0.14B vs H1 |
| Wind deliveries | 70% of 2025 Wind equipment orders deliver in H2'26; Wind product CL fell $582M and $903M in the last two third quarters | -$0.3B to -$0.6B |

**Why missed.** Verifiable gap: SRA GW is in neither orders nor RPO; the deposit share is in no filing. Against it: "20% to 25%" is in news of 2026-06-22 (src:2674); "like, 25% down" and the 20 GW H2 figure are in the 2026-09-16 conference transcript on the company site; the H1-above-H2 cash profile is in the Q2 call; the highest Q3 FCF estimate is $7.1B; the quarterly-sum Street is above the guide top. Sell-side notes not checked.

**Already priced.** Earnings-day moves on FCF guide raises: 2025-07-23 +14.6%; 2025-12-10 +15.6%; 2026-04-22 +13.7%; 2026-07-22 -8.7% (largest raise, +$5B, margin guide unchanged). Price is 16% below the 2026-06-30 high of $1,174.86. Management's standard sentence "we also expect to deliver positive free cash flow ... down payments, which correlate with the timing of orders" was used word for word for Q1'26 (which printed $4.8B) and again for Q3'26, so it carries no information either way.

**Reveal date.** Q3 analog (Q2'25 and Q3'25 scaled for price, 7-10 GW signed): change in CL about +$0.3B to +$3.4B, centre near +$1.5B; Q3 FCF about $1.1-2.0B against the Street's $1,502M. Q3 FCF shows no gap; most of any H2 upside sits in Q4 ("most contracted in Q4"). A Q3 balance of about $41.4B would beat the median by 3.6% and sit below the highest broker ($41.8B). The two lenses' pass marks ($41.0B and $43B) must be merged into one before use. The print is on the same day as the FOMC decision (`E07_catalyst_calendar.md`).

**Counter-move.** FY24: H2 and Q4 actuals equalled the top of the implied range exactly ($1.54B and $0.57B). Levers visible in H1'26: $0.5B voluntary pension contribution and supplier commitments. Customer side: a December signing can be billed and not collected (k).

**Multiple consistency.** Forward EV/EBITDA 28.5x, 6th percentile of 12 months; peers 11-22x. $2.3B of extra cash lowers enterprise value by 0.9%. Nothing in the candidate ties the cash line to the exit multiple or sets a bear multiple.

## 6. What survives as usable input (not as the wedge)

- Fact, checkable in seconds: CL rose in 10 of 10 quarters and the Street median for 9/30/26 is the 6/30/26 balance to the dollar. Supports a Q3 cash-quality line; gap 3.6% vs the median, inside the model error.
- Fact: the FY26 guide leaves $1.60-2.60B for H2 after $9.9B in H1; the guide would hold only if CL growth slows to about $2.8-3.4B from $13.7B.
- Range only: FY26 FCF $12.5-12.8B on the guide record, $13.6-14.5B on the deposit method, full band $11.6-16.4B (or $11.9-18.0B on the input grid).

## 7. Reproduce

Scripts (session scratchpad): `verify_fcf.py` (guide record, CL history, broker-count feasibility), `verify_bt.py` (both deposit back-tests, k test, band, per-share). Inputs: `GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus, PricePositioning); `GEV_Pull_2026-10-01/06_modl.xlsx`, `01_eeo_annual.xlsx`, `segment_quarterly.json`; `data/financials/gev_quarterly.csv`, `gev_segments.csv`; `gev.db` (xbrl_facts, mgmt_guidance, chunks_fts, sources 3161 and 681); `propose_fcf-deposits.md`, `propose_winners-pattern.md`; `PLAYBOOK.md` "Tests a wedge must pass".
