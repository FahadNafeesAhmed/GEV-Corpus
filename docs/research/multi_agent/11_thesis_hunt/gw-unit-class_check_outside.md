# Check: ordinary explanation and already known — rebuild "gw-unit-class"

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Working date 2026-10-01. Money in $M unless stated. Checked file: `gw-unit-class.md`.

Words used here. **Layer** = the orders booked in one quarter (GW and dollars). **Conversion** = reported Power equipment revenue divided by the order dollars of the GW shipped, oldest layer first. **Price index** = the rebuild's heavy-duty-equivalent dollars per kW for one order quarter. **Guide-anchored** = scaled so that the model's H2 2026 equals the Street's H2 2026, which itself sits on company guidance. **Pooled** = several order quarters given one common price index, with total dollars unchanged.

## 0. Result

**Does not survive as a thesis.** The arithmetic reproduces and the unit facts are sound. The claim fails two of the three outside tests and passes the third only in form.

| Test | Result |
|---|---|
| Numbers reproduce from primary files | Yes (section 1) |
| No ordinary explanation removes the gap | Fails in part. Four-quarter window: the simple order-queue method gives the Street with a normal conversion (0.94 to 0.98), so no gap is needed. H1 2027: the Street is the guided H2 2026 run-rate held flat at the same output. The rebuild's +23% step between the two halves comes from one layer boundary (Q1 2025 to Q2 2025, index +50%), which management attributed to mix. With 2025 pooled and the model anchored on the guided half, the H1 2027 gap is +8% to +18% (section 2) |
| Street figure solid | Fails. No contributor count. Equipment + services is $269M below the Street's own Power total in H1 2027, which is 5% of the equipment line. One-model signature in 2027 (section 5) |
| Not already published | Mixed. The specific number is not found in print. The question "which order year ships in 2027" is a live public debate, with a Sell note and a company statement on opposite sides (section 4) |
| A company-reported number inside 12 months settles it | Yes in form (late April and late July 2027). In practice the January 2027 guide resets the Street first, and the rebuild needs Power growth of +27% to +40% in 2027 against a company framework of high teens (section 6) |
| **survives** | **false** |

Corrected H1 2027 gap: about **+17%** (range +3% to +28%). Corrected error band: about **+/-22%**. The gap is inside the band (section 7).

Usable as: **supporting evidence** (the HA unit count, the Street in physical terms, the class driver structure, a dated scorecard). Not a stand-alone claim that the Street is wrong.

## 1. What was recomputed

From `segment_quarterly.json`, `01-eeo-company-specific.xlsx`, `01_eeo_annual.xlsx`, `06_modl.xlsx`, the workbook sheets `Consensus`, `ConsensusHistory`, `Bulk`, the 10-Q / 10-K Power tables in `gev.db`, corpus sources 3161, 3796, 2660, 1844, and the company transcript of 2026-09-16 on gevernova.com.

| Item | Rebuild | Recomputed |
|---|---|---|
| Street Power equipment Q3 2026 to Q2 2027 | 2,394 / 3,097 / 2,585 / 2,798 | same (Bloomberg, 2026-10-01) |
| Street H2 2026; H1 2027; four quarters; FY2027; FY2028 | 5,491; 5,383; 10,874; 12,151; 15,888 | same |
| Units and GW ordered and sold by class, 14 quarters; equipment revenue; equipment RPO | section 2 of the rebuild | same in all ten filings (accessions in the rebuild's section 1) |
| HA units in RPO, disclosed | 29, 32, 36, 32, 51 | same (10-Q Q1 to Q3 2024, 10-K 2024, 10-K 2025). Not disclosed in any 2025 or 2026 10-Q |
| HA in RPO at 6/30/26 | 70 | 51 + 27 ordered - 8 sold = 70 |
| Base model (section 17 code) | bias 0.961; H2 2026 5,617; H1 2027 6,900; FY2027 15,394; FY2028 21,016 | same |
| Price index by order quarter | 431 ... 321, 482, 478, 594, 564, 751 | same |
| Q3 2026 Power equipment low / high | 2,063 / 2,591 | same; median 2,433 |
| Company statements: 5 GW in Q3 and Q4, 6 GW in H2 2027, 7 GW in 2028; 2026 backlog margin shows in 2029-30 | as paraphrased | confirmed in the company transcript |

The rebuild's claim "every HA in RPO was ordered in 2025 or later" assumes oldest-first shipping. Without that assumption the count still bounds it: 51 HA were in RPO at end-2025 and 43 were ordered in 2025, so at most 8 older units were left then, and 8 HA were sold in H1 2026. So **62 to 70 of the 70** were ordered in 2025 or later under any sequence, unless an HA ordered in 2025 shipped inside 2025. This fact holds.

## 2. Ordinary readings of the Street figure

### 2a. H1 2027 = the guided run-rate held flat

Street Power equipment revenue per kW at 5 GW a quarter (Bloomberg, 2026-10-01):

| | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 | H2 2026 | H1 2027 |
|---|---|---|---|---|---|---|
| Street $M | 2,394 | 3,097 | 2,585 | 2,798 | 5,491 | 5,383 |
| $/kW at 5 GW a quarter | 479 | 619 | 517 | 560 | 549 | 538 |
| Growth on a year earlier | +37% | +59% | +37% | +42% | +49% | +40% |

- H1 2027 is 2% below H2 2026 at the same output. Q4 is the seasonal high in every year since 2023.
- H1 2027 against H1 2026 actual (3,851 on 7.5 GW, $513/kW): GW +33%, revenue +40%, so revenue per kW +5%.
- Company, 2026-09-16: 5 GW in Q3 and in Q4, and "the beginning of next year will feel generally very similar". The step to 6 GW comes "sometime in the second half of next year".
- The Street's H2 2026 rests on guidance. Q3 2026 Power revenue guide: +17% to +19% (Q2 2026 call). Q3 2025 Power revenue was 4,838, so the guide is 5,660 to 5,757. Street 5,776 (low 5,684, high 5,960). FY2026 Power guide +18% to +20% gives H2 of 12,876 to 13,271. Street 13,160.
- So the plain reading of the Street's H1 2027 is: same output, same revenue per kW as the guided half. No broker has to hold any view on order vintages to get there.

### 2b. Four quarters = the order queue at a normal conversion

Simple method (the first build's): GW ship oldest layer first at the all-in order price of the layer. Opening backlog 21.7 GW at $446/kW (end-2022 RPO less the EDF item). Script `fifo.py`.

| Window | Reported or Street $M | Layer dollars shipped | Conversion |
|---|---|---|---|
| H1 2023 / H2 2023 | 2,327 / 3,271 | 2,632 / 3,524 | 0.88 / 0.93 |
| H1 2024 / H2 2024 | 2,486 / 3,222 | 1,695 / 4,341 | 1.47 / 0.74 |
| H1 2025 / H2 2025 | 2,996 / 3,690 | 4,183 / 2,941 | 0.72 / 1.26 |
| H1 2026 | 3,850 | 3,043 | 1.27 |
| Street H2 2026 | 5,491 | 4,317 (4,833 on the rebuild's pricing of the oldest 3.0 GW) | 1.27 (1.14) |
| Street H1 2027 | 5,383 | 6,736 | 0.80 |
| **Street Q3 2026 to Q2 2027** | **10,874** | **11,053 (11,569)** | **0.98 (0.94)** |
| Reported four-quarter windows (11) | | | 0.73 to 1.26, mean 0.97 |

- Over the four quarters the Street equals plan GW x order-queue prices x 0.94 to 0.98. That is at the historical mean (0.97 here; 0.90 to 0.92 in the earlier files). **On the method that produced the original claim, the four-quarter window has no gap.**
- The rebuild shows the two halves separately: layers x 0.90 "under-predicts the guided half by 21%" and gives "+13%" for H1 2027. Added together they are 10,412 against a Street of 10,874. The Street is 4% above.
- For H1 2027 alone the Street implies a conversion of 0.80. Two of seven reported half-years were lower (0.74, 0.72).
- The class model puts more dollars into the same four quarters: about $13.0B before bias against $11.1B to $11.6B of queue dollars (+13% to +18%). The larger items are aero taken deeper in the queue (20 units from Q4 2025 and Q1 2026 orders, about $1.1B, partly offset by less other heavy-duty), half of H2 2027's heavy-duty value recognised early (about +$0.9B net), and a non-gas base added on top (about +$0.4B net). Each is an assumption of the model, not a disclosed fact.

### 2c. Analysts following the company framework

| | Street (Bloomberg, 2026-10-01) | Company |
|---|---|---|
| Power revenue growth 2026 / 2027 / 2028 | +19.4% / +19.1% / +19.2% | "Revenue up high teens at Power" from 2025 to 2028, with "pricing reflecting recent orders" and 20 GW then about 24 GW (December 2025 update, corpus source 1844) |
| Power organic growth, each quarter of 2027 | exactly 18.0 (one contributor) | FY2026 guide +18% to +20% |
| Power H1 2027 on H1 2026 actual (10,449) | +23.9% (services +10.6%, equipment +39.8%) | - |
| Same with the rebuild's median (6,864 + Street services 7,294) | +35.5% | - |
| FY2027 Power growth on the rebuild | +27% to +40% (its section 11c) | - |

- Guide history. For 2025 the company still said +6% to +7% in December 2025 and reported +10% organic. For 2026 it said +16% to +18% and now says +18% to +20%. Guides have run 2 to 4 points low. The rebuild needs 8 to 21 points.
- The framework was set with 2027 slots already sold and with contract prices known to management slot by slot.

### 2d. Where the H1 2027 step comes from: one layer boundary

At flat output the model steps +23% from H2 2026 to H1 2027. The cause is the price index: 321 for Q1 2025 orders, 482 and 478 for Q2 and Q3 2025 orders (+50% in one quarter). H2 2026 ships Q1 2025 heavy-duty units. H1 2027 ships Q2 and Q3 2025 units.

What the company said about those two layers (Q3 2025 call, corpus source 3796):
- Q2 2025: "substantially more smaller gas turbines, more aeroderivatives that are higher priced per megawatt than the baseload units" (CEO).
- Q3 2025: back out "non-Gas Power orders that have really no gigawatts" and order dollars per GW are "relatively flat quarter-to-quarter" (CFO).
- "There can be more or less of the combined cycle that gets booked in that quarter, i.e., the steam turbines and generators" (CEO).
- 10-Q Q1, Q2 and Q3 2025 each list Hydro Power equipment as a driver of the rise in Power RPO. The rebuild holds non-gas orders flat at $300M a quarter.

This is kill reason 2 again, one layer earlier. The rebuild splits aero out with a fixed ratio. It does not treat small frames (Q2 2025 other heavy-duty averaged 78 MW a unit), added scope, or lumpy non-gas orders.

Test: give 2025 one common index (dollars unchanged). No unit ordered in 2025 has shipped, so the back-test cannot tell the two versions apart (worst half-year miss 19% against 20%). Script `variants.py`, July path, bias-corrected.

| Version | H2 2026 vs Street | H1 2027 vs Street | Step H2 to H1 | H1 2027 if anchored on the guided half | Four quarters |
|---|---|---|---|---|---|
| Rebuild base (index by quarter) | +2% | +28% | +23% | +25% | +15% |
| Q1 to Q3 2025 pooled | +4% | +24% | +17% | +19% | +13% |
| All of 2025 pooled | +13% | +22% | +6% | **+9%** | +17% |
| All of 2025 pooled, other recognition profiles (point / even / scope / late) | +17% / +10% / +10% / +8% | +29% / +19% / +25% / +27% | +7% / +6% / +11% / +16% | **+10% / +8% / +13% / +18%** | +23% / +15% / +17% / +17% |
| Q2 and Q3 2025 index 20% lower | -8% | +17% | +24% | +27% | +5% |
| Output 4.5 GW a quarter, 2025 pooled | +5% | +17% | +9% | +11% | +11% |

- "The model reproduces the guided half without being fitted to it" holds only with the index by quarter. With 2025 pooled the model is 8% to 17% above the guided half.
- Then one of two things is true. Either the guide is low and the surprise is in H2 2026 (reported late January 2027), or the model's level is high and the H1 2027 gap is +8% to +18%.
- The four-quarter gap stays at +11% to +23% in every pooled version. Its placement between the halves is what is not known. The earlier check of the RPO-schedule candidate reached the same point: the "gap sits in H1 2027" form was not supported.

### 2e. Price or scope: a check against the company's margin disclosure

- Rebuild's index, 2024 orders pooled to 2025 orders pooled: 294 to 483, **+64%**. All-in order dollars per kW: $417 to $635, +52%.
- Company (Q4 2025 call, corpus source 2660): margin in the Power equipment backlog rose 11 points in 2025 and 17 points since end-2022, from about breakeven.
- Arithmetic: RPO 12,461 to 24,707; orders 18,932; revenue 6,686. An 11-point rise needs the 2025 orders at about 17% to 22% margin against 4% to 8% for the opening backlog. At equal cost that is a like-for-like price ratio of **1.16 to 1.19**; with 5% to 10% cost inflation, 1.22 to 1.30.
- So about +20% to +30% of the +64% is price on like equipment. The rest is added scope, mix and non-gas orders. Those dollars are still revenue, but (a) scope and non-gas equipment follow their own delivery dates, and (b) they do not earn the 45% drop-through used in the rebuild's upper profit case. On a 15% to 25% drop-through the median H1 2027 case is +6% to +10% of the half's Street EBITDA, the same order as kill reason 6.

## 3. The first guided quarter (a test the rebuild does not list)

The company guided Q3 2026 Power revenue to +17% to +19%. With services up 6% to 11% on 3,094, that leaves Power equipment of **2,226 to 2,478** on about 5 GW ($445 to $496/kW, below the $516 of the last four quarters).

| | Q3 2026 Power equipment | Implied Power growth with Street services (3,389) |
|---|---|---|
| Company guide (implied) | 2,226 to 2,478 | +17% to +19% |
| Street mean (low / high) | 2,394 (2,063 / 2,591) | +19.0% |
| Rebuild base | 2,618 | +24.2% |
| Rebuild, five recognition profiles x three aero rates | 2,339 to 2,657 | +18.4% to +25.0% |

- In 14 of 15 versions the model implies Power growth above the top of the company's own Q3 guide (+19%). The base is above the highest broker.
- The model matches the guided half only by being low in Q4 (2,765 to 3,015 against 3,097).
- Candidate mark for 2026-10-28 (the team sets its own): with about 5 GW shipped, Q3 Power equipment revenue of $2.6B or more supports the model's level; $2.4B or less says the model starts high.

## 4. Already published

| Who / when | What is public | Source |
|---|---|---|
| Company, Q4 2025 call (2026-01) | "We will not begin delivering on the majority of the higher-margin orders placed in '24 and '25 until '27 and beyond" | corpus source 2660 |
| GLJ Research, Sell note (2026-09-14) | Turbines for 2027 delivery were ordered in 2024, before prices rose; about 3 points of backlog margin on that vintage against 10 to 11 on the 2025 vintage "shipping in 2028"; 2027 Power margin 18.5% against consensus 20.7%; 2027 EBITDA $7.42B against $9.45B. Stock -8.6% on the day | GuruFocus 2026-09-15; AInvest 2026-09-15; Seeking Alpha 2026-09-14 |
| Company, 2026-09-16 | 5 / 6 / 7 GW a quarter; start of 2027 "very similar" to H2 2026; 2026 backlog margin shows in 2029-30; FY27 outlook on the January call | gevernova.com transcript |
| BNP Paribas (2026-07-22) | About $790/kW heavy-duty, $950/kW HA with combined-cycle scope, $1,800/kW aero for Q2 2026 orders. The rebuild's class ratios come from this note | Utility Dive 2026-07-23 (corpus source 301) |
| Morgan Stanley (2026-07-23) | 30 GW in 2030 at about $900/kW; reservations near $3,000/kW of implied plant price | press copy dated 2026-07-25 |
| Company, Q3 2025 call | Order dollars per GW swing with aero mix, small turbines, combined-cycle scope and non-gas orders | corpus source 3796 |
| Company, December 2025 | Framework assumes pricing at recent orders; lists gas turbine pricing above current order levels as upside | corpus source 1844 |
| Bloomberg, 2026-10-01 | FY2027 EBITDA: 36 estimates, mean 9,471, high 11,029 (+16.5%), low 6,612, std dev 917 | workbook sheet Consensus |

- The vintage of 2027 deliveries is an open public argument. The Street mean sits between the two published sides.
- The HA count in section 1 contradicts the Sell note on units: at most 8 HA ordered before 2025 were left in RPO at mid-2026. That is a usable fact. It is the same point as the team's existing backlog-vintage work.
- Not found: any published figure for H1 2027 or FY2027 Power equipment revenue far above consensus, or the statement that all HA in RPO were ordered in 2025 or later.
- The rebuild's median FY2027 case adds $0.55B to $1.65B of EBITDA (15% to 45% drop-through). That is 0.6 to 1.8 standard deviations of the Street and, below 43% drop-through, under the highest existing estimate.
- The four-quarter version overlaps the RPO-schedule candidate already on file. Model Power plus Street Wind and Electrification is 0.98 to 1.04 times the filed schedule; the schedule file put total equipment at +5% to +7% over the Street. It is the same shortfall, assigned wholly to Power. It is not a second, independent finding.

## 5. How thin the Street line is for the periods used (Bloomberg, 2026-10-01)

| Check | Finding | File |
|---|---|---|
| Contributors to Power equipment, Q1 and Q2 2027 | Not shown. Mean only | `01-eeo-company-specific.xlsx` |
| Company-level quarterly revenue estimates | 28 for Q3 and Q4 2026; **22** for Q1 and Q2 2027. EBITDA 26 and 19. Division lines are a subset | `01_eeo_annual.xlsx` |
| Broker values on the division row | MODL (Q3 2026) lists 29 brokers. The Power equipment row shows no broker value. Three brokers show any value on the sheet | `06_modl.xlsx` |
| Spread one quarter out | Power equipment Q3 2026: mean 2,394, low -13.8%, high +8.3%. Power revenue: -1.6% / +3.2%. Services: -6.5% / +10.3% | `06_modl.xlsx` |
| Equipment + services against the Power total | Q3 2026 +7; Q4 2026 -16; **Q1 2027 -52; Q2 2027 -217**. H1 2027: 269 short, 5.0% of the equipment line | `segment_quarterly.json` |
| Gas + Nuclear + Hydro against the Power total | Q1 2027 -212; Q2 2027 -162 | same |
| One-model signature | Power organic growth exactly 18.0 in all four 2027 quarters, while the Power total grows +21.9% and +25.7% in Q1 and Q2 | same |
| History of the line | None. No way to see how it moved after July or September | - |
| Freshness | FY2027 revenue consensus 52,537 (2026-07-24) to 52,949 (2026-09-25): +0.8% in nine weeks. 12 of 45 rating rows are dated on or after 2026-09-17 | sheets ConsensusHistory, Bulk |

- If the missing 269 belongs to equipment, the Street's H1 2027 equipment figure is 5,652, not 5,383. Spread pro rata it is 5,497. The median gap moves from +28% to +21% or +25%.
- The rebuild itself reports the gap on broader lines: Power revenue +8% to +18%; company revenue (22 estimates) **+4% to +10%**.
- The +28% exists only on the line whose contributors cannot be seen.

## 6. Can a company-reported number inside 12 months settle it

| Date | Number | Comment |
|---|---|---|
| 2026-10-28 | Q3 units and GW sold by class; Q3 Power equipment revenue | Tests output and the model's level (section 3) |
| Late January 2027 | H2 2026 Power equipment revenue; FY2027 Power guide; HA in RPO (10-K) | The guide resets the Street's 2027 before any 2027 quarter prints. The rebuild's own mark calls a guide of +20% or less contrary. Guide history and the sibling rebuild (16% to 21%) point there |
| Late April 2027 | Q1 2027 Power equipment revenue | Inside 12 months |
| Late July 2027 | Six months to 30 June 2027 | Inside 12 months, near the end of the horizon |

- The line is company-reported and the dates fall inside 12 months. This test passes in form.
- The comparison is with the Street of 2026-10-01. By July 2027 that figure will have been replaced twice (January guide, April print).
- A revenue beat has not moved the stock by itself: Q2 2026 revenue was above consensus and the shares fell 8.7%.

## 7. Corrected gap and band (H1 2027)

| Step | H1 2027 gap |
|---|---|
| Rebuild median (with its H1 factor) | +28% |
| Street read as 5,497 to 5,652 (section 5) | +21% to +25% |
| 2025 pooled and anchored on the guided half (section 2d) | +8% to +18% |
| Both | +3% to +16% |
| Centre used here | **about +17%** (midpoint of +9% pooled and anchored and +28% unpooled is +18.5% on the printed Street line; +16% with the Street read pro rata) |

Band: the rebuild's back-test figure for a half-year (16.5%) with its own forward inputs (output 8%, aero 3%, price split 7%) plus the layer-placement uncertainty of section 2d (about 9.5 points, half the distance between +9% and +28%), combined in quadrature: **about +/-22%**. The p90 back-test miss alone is 24.6%.

Four-quarter window: gap +15% (+5% to +23% across the versions run here; +12% if the Street is read as 11,152). The rebuild compares it with the back-test band alone (9.5%). With the same forward inputs it adds for the half-year, the band is about +/-14.6%. Gap and band are about equal.

## 8. What can still be used

| Use | Status |
|---|---|
| HA unit count: 62 to 70 of the 70 HA in RPO at mid-2026 were ordered in 2025 or later | Solid. From filings. Answers the published claim that 2027 heavy-duty deliveries are 2024 orders |
| Exhibit: Street Power equipment in dollars per kW ($479 / $619 / $517 / $560 by quarter) beside the all-in order prices of the layers | Usable. Label the Street line as a division mean with hidden contributors |
| Driver structure by class with back-tested error | Usable as model structure. State that no 2025 order has shipped and that the index inside 2025 cannot be tested |
| Dated scorecard | Usable. Add Q3 2026 Power equipment revenue (section 3) |
| "Street H1 2027 Power equipment revenue is about 28% too low" | Not supported. About +17% against about +/-22%, on a line that cannot be verified |
| Four-quarter gap | Supporting evidence only, and not additional to the RPO-schedule fact |

What would change this result: a broker-level table for Power equipment in Q1 and Q2 2027 with 8 to 10 visible contributors; or a Q3 2026 print at about 5 GW with Power equipment revenue of $2.6B or more and HA units sold of 6 or more; or a company statement of delivery year by order year.

## 9. Sources and scripts

- Filings and transcripts: `data/gev.db` (read-only). 10-Q / 10-K Power tables (ten accessions listed in the rebuild); corpus sources 3161 (Q2 2026 call), 3796 (Q3 2025 call), 2660 (Q4 2025 call), 1844 (December 2025 deck), 301.
- Company transcript, 2026-09-16: https://www.gevernova.com/sites/default/files/ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf
- Sell note as reported: https://www.gurufocus.com/news/9079408/glj-starts-ge-vernova-at-sell-with-ebitda-22-below-consensus ; https://www.ainvest.com/news/ge-vernova-8-6-plunge-price-demand-2609/ ; https://seekingalpha.com/news/4642621-ge-vernova-sinks-9-as-glj-research-starts-with-sell-rating-street-high-470-pt
- Class prices: https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/
- 30 GW at about $900/kW: https://fancyhints.com/morgan-stanley-strongly-resets-ge-vernova-stock-target/
- Bloomberg, 2026-10-01: files named in the tables above.
- Scripts (scratchpad `uco/`): `base.py` (the rebuild's section 17 code with quarterly output), `fifo.py` (simple order-queue conversion by half-year and four quarters), `variants.py` (pooled 2025 index, guide anchoring, recognition profiles, Q3 2026 by profile).
- Web pages were read with the Exa search and fetch tools. The Firecrawl connector is not authorised in this session and was not used.

Core of the pooled test, to paste under the rebuild's section 17 code (replace the per-quarter `p` with `P[i]`):

```python
den = [RHA*MHA*ha + max(gw - MHA*ha - MAE*ae, 0.06*(hd-ha)) + RAE*MAE*ae for (hd, ha, ae, gw) in ORD]
P   = [(D[i] - NGO) / den[i] for i in range(14)]
idx = [Q.index(q) for q in ('2025Q1', '2025Q2', '2025Q3', '2025Q4')]
pp  = sum(D[i] - NGO for i in idx) / sum(den[i] for i in idx)      # one index for 2025: 483
for i in idx: P[i] = pp
# base: H2 2026 5,617 (+2%), H1 2027 6,900 (+28%), step +23%
# pooled: H2 2026 6,180 (+13%), H1 2027 6,577 (+22%), step +6%; anchored on 5,491: 5,843 (+9%)
```
