# Rebuild 2 of the gigawatts angle: Power equipment revenue from units by class

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team (ranges and methods only). Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Id: `gw-unit-class`. Working date 2026-10-01. Money in $M unless stated.

Terms used:
- **HA**: GEV's largest gas turbine class (about 430 MW each). **Other heavy-duty**: F, E and B class units (about 45 to 290 MW). **Aero**: aeroderivative units (about 30 to 115 MW).
- **RPO**: remaining performance obligations, i.e. signed orders not yet recognised as revenue. **SRA**: slot reservation agreement (a paid factory slot, not yet an order).
- **Vintage**: the quarter in which a unit was ordered. **Oldest first**: within each class, units ship in the order they were booked.
- **Price index**: heavy-duty-equivalent dollars per kW of one quarter's orders (section 4c).
- **Bias**: reported revenue divided by model revenue over 2023 to H1 2026. One number per parameter set, applied to every forward figure.
- **Street**: Bloomberg BEst mean, key `Total Revenue|Power|Equipment`.

## 0. Result

9,720 parameter sets were run (section 6). Columns show the 10th percentile, median and 90th percentile after bias correction.

| Window | Street | Model p10 / median / p90 | Gap p10 / median / p90 | Back-test band: worst miss, median of sets (p90) | Sets where gap > own worst miss | Company reports it |
|---|---|---|---|---|---|---|
| H2 2026 | 5,491 | 5,172 / 5,504 / 5,783 | -6% / 0% / +5% | half-year 16.5% (24.6%) | 0% | late Jan 2027 |
| **H1 2027** | **5,383** | 6,408 / 7,019 / 7,718; with the H1 factor 6,335 / 6,864 / 7,490 | +19% / +30% / +43%; with the H1 factor **+18% / +28% / +39%** | half-year 16.5% (24.6%) | 92% (89% with the H1 factor) | Q1: late Apr 2027. Six months: late Jul 2027 |
| Q3 2026 to Q2 2027 | 10,874 | 11,643 / 12,531 / 13,434 | +7% / +15% / +24% | rolling four quarters 9.5% (14.9%) | 76% | late Jul 2027 |
| FY2027 | 12,151 | 14,409 / 15,819 / 17,445 | +19% / +30% / +44% | annual 7.6% (13.3%) | 100% | late Jan 2028 (outside 12 months) |
| FY2028, output flat at 20 GW | 15,888 | 17,162 / 18,037 / 19,027 | +8% / +14% / +20% | annual 7.6% (13.3%) | 80% | Feb 2029 |
| FY2028, July plan 23 GW | 15,888 | 19,453 / 20,508 / 21,666 | +22% / +29% / +36% | same | 100% | Feb 2029 |
| FY2028, September ladder 25.5 GW | 15,888 | 21,299 / 22,482 / 23,777 | +34% / +41% / +50% | same | 100% | Feb 2029 |
| FY2029 | 19,256 | 16.4B to 28.5B (section 8c) | -15% to +48% | not usable | no call | Feb 2030 |
| FY2030 | 23,469 | 16.1B to 30.1B (section 8c) | -31% to +28% | not usable | no call | Feb 2031 |
| Cumulative H2 2026 to 2028 | 33,530 | flat 38,896; July 41,619; ladder 44,656 (medians) | +16% / +24% / +33% | annual | 91% / 100% / 100% | Feb 2029 |
| Cumulative 2027 to 2030 | 70,765 | flat 71,166; July 85,639; ladder 90,063 (medians) | +1% / +21% / +27% | annual | 15% / 97% / 100% | Feb 2031 |

Plain reading:
- One window clears the model's own back-tested error and is reported inside 12 months: **Power equipment revenue for the six months to 30 June 2027** (gap about +28%; band about +/-17% from the back-test, about +/-20% once input uncertainty is added, section 6e).
- The four-quarter version (Q3 2026 to Q2 2027) does not depend on which half the units land in. It clears more narrowly: +15% against +/-9.5%.
- FY2027 and FY2028 clear at the stated output plan but are reported after the 12-month horizon. FY2029 and FY2030 do not clear: they rest on SRA prices that are not disclosed and on aero orders not yet booked.
- The model matches the guided half (H2 2026) without being fitted to it. Two other methods (first-in-first-out GW layers x 0.90, and a unit regression) under-predict the guided half by 16% to 21%.
- Three things the back-test cannot cover: (1) no unit ordered in 2025 or later has shipped yet, so the higher price layers are untested; (2) output has to reach 5 GW a quarter; (3) half-year timing of the model has been off by about 20 points in sequential terms. Section 16 lists the rest.

## 1. Sources

| Key | What | Where |
|---|---|---|
| 10-Q / 10-K | Power tables: units and GW ordered and sold by class, equipment revenue, equipment RPO, HA units in RPO, sub-business revenue, revenue recognition note | `data/gev.db` (read-only), accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148 |
| Street | Quarterly consensus by division | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`; `01..05-eeo-company-specific.xlsx`; `06_modl.xlsx` (Q3 2026 low and high); `01_eeo_annual.xlsx` (estimate counts). Bloomberg, 2026-10-01 |
| Q2 2026 call and deck | Output path, aero and heavy-duty timing, order pricing, Power equipment orders in dollars | corpus sources 3161, 3157 |
| Q3 2025 call | Order dollars per GW: aero mix, combined-cycle scope, non-gas orders | corpus source 3796 |
| December 2025 investor update | 24 GW in 2028 including 90 to 100 heavy-duty units; class size ranges; 2028 framework | corpus source 1844 |
| Conference 2026-09-16 | 5, 6, 7 GW a quarter; aero size; timing of 2026 backlog margin | gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` (read 2026-10-01); summary in corpus source 681 |
| Per-class price estimate | One broker (BNP Paribas): about $790/kW heavy-duty, $950/kW HA combined-cycle scope, $1,800/kW aero, for Q2 2026 orders | Utility Dive 2026-07-22, corpus source 301 |
| Earlier work | First build and its three checks; RPO schedule candidate; sibling rebuild | `propose_power-equipment-physical.md`, `verify_power-equipment-fy28-fy29_*.md`, `candidate_equipment-revenue-vs-rpo-schedule.md`, `gw-guide-predictor.md` |

## 2. Units by class, quarter by quarter

Q4 values are the full year less nine months. HA is a subset of heavy-duty in the filings; "other HD" = heavy-duty less HA. Orders in dollars = change in Power equipment RPO + Power equipment revenue (the $3.9B EDF disposal is added back in Q2 2024). Deck values where published: Q2 2025 3,519; H1 2025 6,361; Q2 2026 12,650; H1 2026 18,261 (source 3157). Derived values are 0.4% to 5% above them.

| Quarter | Sold: HA / other HD / aero | GW sold | Ordered: HA / other HD / aero | GW ordered | Equipment revenue | Equipment RPO end | Orders $M (derived) | All-in $/kW |
|---|---|---|---|---|---|---|---|---|
| Q1 2023 | 4 / 14 / 5 | 3.6 | 4 / 2 / 7 | 2.3 | 1,180 | 13,992 | 1,593 | 693 |
| Q2 2023 | 3 / 6 / 5 | 2.3 | 0 / 14 / 12 | 2.1 | 1,147 | 13,980 | 1,135 | 540 |
| Q3 2023 | 2 / 10 / 7 | 2.7 | 4 / 8 / 8 | 3.1 | 1,291 | 13,865 | 1,176 | 379 |
| Q4 2023 | 5 / 14 / 16 | 5.2 | 0 / 9 / 25 | 2.1 | 1,980 | 13,636 | 1,751 | 834 |
| Q1 2024 | 1 / 9 / 7 | 2.3 | 8 / 8 / 18 | 4.9 | 1,201 | 14,394 | 1,959 | 400 |
| Q2 2024 | 1 / 7 / 7 | 1.5 | 4 / 10 / 1 | 4.1 | 1,285 | 10,978 | 1,769 | 431 |
| Q3 2024 | 5 / 8 / 5 | 3.3 | 9 / 5 / 15 | 5.1 | 1,426 | 11,392 | 1,840 | 361 |
| Q4 2024 | 8 / 9 / 8 | 4.8 | 4 / 20 / 10 | 6.1 | 1,796 | 12,461 | 2,865 | 470 |
| Q1 2025 | 5 / 7 / 7 | 3.0 | 8 / 21 / 9 | 7.1 | 1,491 | 13,920 | 2,950 | 415 |
| Q2 2025 | 8 / 10 / 3 | 5.2 | 7 / 13 / 27 | 5.1 | 1,505 | 16,133 | 3,718 | 729 |
| Q3 2025 | 6 / 8 / 6 | 4.0 | 13 / 7 / 9 | 7.4 | 1,744 | 18,977 | 4,588 | 620 |
| Q4 2025 | 5 / 5 / 11 | 3.1 | 15 / 26 / 18 | 10.2 | 1,946 | 24,707 | 7,676 | 753 |
| Q1 2026 | 5 / 10 / 10 | 4.2 | 12 / 16 / 9 | 8.1 | 1,885 | 28,530 | 5,708 | 705 |
| Q2 2026 | 3 / 10 / 16 | 3.3 | 15 / 37 / 61 | 12.1 | 1,965 | 39,261 | 12,696 | 1,049 |

Annual, 2022 (10-K 2024): ordered 9 HA / 21 other HD / 62 aero, 9.8 GW; sold 11 / 42 / 48, 11.1 GW; equipment revenue 4,896; RPO 13,579 at year end.

## 3. Unit backlog by class

Roll: backlog end = backlog start + orders - sales, by class. HA units are disclosed at five dates and the roll ties at each one. Other heavy-duty is carried in GW (GW of the quarter less 0.43 x HA units less 0.04 x aero units), because unit size in this class runs from 45 to 290 MW. Aero opening at end-2022 is an assumption (20 units; 14 to 30 tested). It has to be at least 14 if the end-2021 backlog was not negative.

| Date | HA units, roll (disclosed) | Other HD, GW | Other HD units, net change since end-2022 | Aero units | Total GW, roll (disclosed) |
|---|---|---|---|---|---|
| End 2022 | 28 | 8.9 | 0 | 20 | 21.7 |
| End 2023 | 22 | 6.5 | -11 | 39 | 17.5 |
| Q1 2024 | 29 (29) | 5.6 | -12 | 50 | 20.1 |
| Q2 2024 | 32 (32) | 7.2 | -9 | 44 | 22.7 |
| Q3 2024 | 36 (36) | 6.9 | -12 | 54 | 24.5 |
| End 2024 | 32 (32) | 9.8 | -1 | 56 | 25.8 |
| Q2 2025 | 34 | 11.9 | +16 | 82 | 29.8 (29) |
| Q3 2025 | 41 | 12.2 | +15 | 85 | 33.2 (33) |
| End 2025 | 51 (51) | 14.7 | +36 | 92 | 40.3 (40) |
| Q1 2026 | 58 | 15.6 | +42 | 91 | 44.2 (44) |
| **Q2 2026** | **70** | **17.5** | **+69** | **136** | **53.0 (53)** |

Facts that follow from the table:
- HA sold from 2023 to H1 2026 = 14 + 15 + 24 + 8 = 61 = opening 28 + 2023 orders 8 + 2024 orders 25. If units ship oldest first, every HA shipped so far was ordered before 2025.
- HA in RPO at 30 June 2026 = 70 = HA ordered since Q1 2025 (8 + 7 + 13 + 15 + 12 + 15). Every HA that ships from here was ordered in 2025 or later.
- Aero ordered since end-2022: 229. Aero sold: 113. The aero backlog is at least 116 units plus the opening. At the Q2 2026 pace (16 a quarter) that is seven to nine quarters of shipments.
- Company cross-checks: the CEO said 130 HA are running and 195 more are under contract (conference 2026-09-16); more than half of the 116 GW under contract is HA (Q2 2026 call). 195 less about 45 being installed leaves about 150 HA in RPO and SRAs, about 64 GW at 0.43.

## 4. Size and dollars per unit by class

### 4a. Size
Regression of GW on units (28 observations: orders and sales, Q1 2023 to Q2 2026, no constant): HA 435 MW a unit (s.e. 22), other heavy-duty 173 MW (s.e. 15), aero not identified (-3, s.e. 10). With aero fixed at 40 MW: HA 425, other heavy-duty 131. Company ranges (December 2025 deck): aero about 35 to 115 MW; B and E class 45 to 150; F class 90 to 290; HA 290 to 570. Used: HA 0.43 GW, aero 0.04 GW, other heavy-duty as the residual GW. Q2 2026 other heavy-duty orders: 3.2 GW for 37 units, about 87 MW each (the CEO cited demand for the 90 MW 7E).

### 4b. Revenue regression on units sold (same quarter, 14 quarters)

| Specification | Constant | HA $M a unit | Other HD | Aero $M a unit | Trend $M a quarter | R2 |
|---|---|---|---|---|---|---|
| Units only | 833 (117) | 86.7 (12.7) | -23 (11) | 69.4 (7.3) | | 0.92 |
| HA, aero, trend | 681 (61) | 63.5 (9.9) | | 55.1 (5.5) | 24.3 (5.5) | 0.96 |

- Out of sample, HA + aero + trend. Leave one period out: 2023 +4.4%, 2024 +0.4%, 2025 +0.5%, H1 2026 -5.7%; half-years -8.0% to +7.5%. Fitted only on earlier quarters: 2025 -0.4%, H1 2026 -5.7%, H2 2024 +10.8%, H1 2025 -5.0%, H2 2025 +7.0%.
- What it shows: (1) an HA adds $64M to $87M in its shipment quarter, about half the order value of the HA units then shipping ($117M to $222M, section 4c), so about half of HA value is recognised before the shipment quarter; (2) other heavy-duty has no same-quarter link, so its revenue is spread over time; (3) the constant ($2.7B to $3.3B a year) holds non-gas equipment (about $1.1B to $1.3B a year) plus gas revenue recognised away from the shipment quarter.
- Why it is not used forward: the constant does not scale with output and there is no price step. At guided units it gives $4.60B for H2 2026 (16% below the guide-anchored Street) and $4.91B for H1 2027.

### 4c. Dollars per unit by vintage (order side)
One price index per order quarter, solved so that the class values add up to that quarter's order dollars:

`p_q = (orders_q - non-gas orders) / (1.2 x 0.43 x HA units + other-HD GW + 2.28 x 0.04 x aero units)`

Then HA = p x 1.2 x 0.43 ($M a unit), other heavy-duty = p ($/kW), aero = p x 2.28 x 0.04 ($M a unit). The relativities 1.2 and 2.28 are the broker's $950 and $1,800 over $790. Non-gas orders: $300M a quarter (200 to 400 tested). Opening backlog priced at end-2022 RPO less the EDF item less $2.5B non-gas (2.0 to 3.0 tested): $286/kW.

| Order quarter | Index $/kW | HA $M a unit | Aero $M a unit |  | Order quarter | Index $/kW | HA $M a unit | Aero $M a unit |
|---|---|---|---|---|---|---|---|---|
| Opening (end 2022) | 286 | 148 | 26 |  | Q4 2024 | 369 | 190 | 34 |
| Q1 2023 | 431 | 222 | 39 |  | Q1 2025 | 321 | 166 | 29 |
| Q2 2023 | 308 | 159 | 28 |  | Q2 2025 | 482 | 249 | 44 |
| Q3 2023 | 227 | 117 | 21 |  | Q3 2025 | 478 | 246 | 44 |
| Q4 2023 | 429 | 222 | 39 |  | Q4 2025 | 594 | 307 | 54 |
| Q1 2024 | 255 | 132 | 23 |  | Q1 2026 | 564 | 291 | 51 |
| Q2 2024 | 327 | 169 | 30 |  | Q2 2026 | 751 | 387 | 69 |
| Q3 2024 | 232 | 120 | 21 |  | | | | |

- The index is rough quarter by quarter (it moves with non-gas orders and combined-cycle scope). It conserves dollars: the layers left at 30 June 2026 sum to $36,699M against reported RPO of $39,261M, which leaves $2,562M for the non-gas book net of work in progress.
- Sensitivity of the split: with an aero relativity of 3.0 or 4.0 the Q2 2025 HA value falls from $249M to $224M or $197M (Q3 2025: $246M to $240M or $231M) and the aero value rises. Dollars move between classes, not out of the backlog.
- **The Q2 2026 layer by class** ($12,696M, 12.1 GW, $1,049/kW all-in): aero 61 x $68.5M = $4,176M; HA 15 x $387M = $5,810M; other heavy-duty 3.21 GW x $751 = $2,410M; non-gas $300M. Aero relativity 3.0: aero $4,967M, HA $350M a unit. Relativity 4.0: aero $5,842M, HA $309M a unit. On the mix-adjusted index Q2 2026 is 33% above Q1 2026 (751 against 564); management attributes part of that to added combined-cycle equipment.

### 4d. Non-gas equipment base
Non-gas Power revenue (Nuclear + Hydro + Steam): 4,216 (2023), 3,663 (2024), 3,761 (2025), 1,955 (H1 2026). Equipment share is not disclosed; 30% assumed (25% to 35% tested): about $1.27B, $1.10B, $1.13B, $0.59B. Forward: 30% of Street Nuclear + Hydro revenue = $0.67B (H2 2026), $1.35B (2027), $1.44B (2028), $1.68B (2029), $1.98B (2030).

### 4e. Revenue recognised ahead of shipment
10-K 2025, revenue note: customised power generation equipment is recognised over time on cost incurred; standard goods at delivery. Profiles tested for heavy-duty value (aero at shipment in all):

| Profile | Share before shipment quarter | In shipment quarter | After | Median bias | Median worst annual miss | Median worst half-year miss |
|---|---|---|---|---|---|---|
| Point in time | 0 | 100% | 0 | 1.01 | 11.5% | 23.5% |
| Half (base) | 50% over three quarters | 50% | 0 | 0.97 | 7.1% | 18.3% |
| Even over four quarters | 75% | 25% | 0 | 0.95 | 9.8% | 19.2% |
| Scope | 25% over two quarters | 50% | 25% over four quarters | 1.02 | 4.3% | 12.3% |
| Late | 0 | 60% | 40% over four quarters | 1.05 | 5.2% | 10.3% |

The profiles with some revenue after shipment fit best. Filings mention project commissioning as a driver of Gas Power equipment revenue.

## 5. The model

`Revenue_t = non-gas_t + aero units shipped_t x vintage value + sum over k of w_k x (HA and other heavy-duty value shipped in quarter t+k)`

Units ship oldest first within each class. Value = the vintage's dollars per unit (HA, aero) or per kW (other heavy-duty). Forward output is split 60 / 40 between HA and other heavy-duty GW (32% to 46% other heavy-duty tested) after aero at 16 a quarter in H2 2026 and 18 a quarter from 2027 (14 and 22 tested). Check against the December 2025 statement of 90 to 100 heavy-duty units at 24 GW: the split gives about 28 to 32 HA and 55 to 65 other units in 2028. Orders after June 2026 enter at $700/kW heavy-duty and $60M an aero (620 / 50 and 800 / 70 tested).

Backlog at 30 June 2026 in the model (53.0 GW; $36,699M of gas layers):

| Vintage | HA units x $M | Other HD GW x $/kW | Aero units x $M |
|---|---|---|---|
| Q4 2024 | | 2.88 x 369 | 3 x 33.6 |
| Q1 2025 | 8 x 166 | 3.30 x 321 | 9 x 29.3 |
| Q2 2025 | 7 x 249 | 1.01 x 482 | 27 x 44.0 |
| Q3 2025 | 13 x 246 | 1.45 x 478 | 9 x 43.6 |
| Q4 2025 | 15 x 307 | 3.03 x 594 | 18 x 54.2 |
| Q1 2026 | 12 x 291 | 2.58 x 564 | 9 x 51.4 |
| Q2 2026 | 15 x 387 | 3.21 x 751 | 61 x 68.5 |
| Total | 70 units, $20,173M | 17.5 GW, $8,967M | 136 units, $7,559M |

## 6. Back-test

Reported units by class are used for 2023 to H1 2026. Parameters were set before the test; only the bias is measured from it.

### 6a. Base parameters (half profile, non-gas 30%, aero opening 20)

| Period | Reported | Model | Reported / model - 1 | After bias 0.961 |
|---|---|---|---|---|
| FY2023 | 5,598 | 5,858 | -4.4% | -0.5% |
| FY2024 | 5,708 | 6,218 | -8.2% | -4.5% |
| FY2025 | 6,686 | 6,581 | +1.6% | +5.7% |
| H1 2026 | 3,850 | 4,063 | -5.3% | -1.4% |
| H1 2023 | 2,327 | 2,672 | -12.9% | -9.4% |
| H2 2023 | 3,271 | 3,186 | +2.7% | +6.9% |
| H1 2024 | 2,486 | 2,531 | -1.8% | +2.2% |
| H2 2024 | 3,222 | 3,687 | -12.6% | -9.1% |
| H1 2025 | 2,996 | 3,380 | -11.3% | -7.7% |
| H2 2025 | 3,690 | 3,201 | +15.3% | +20.0% |

- Rolling four quarters (11 windows), before bias: -12.0% to +4.3%, s.d. 5.4%. After bias: -8.4% to +8.5%.
- Bias fitted on 2023-24 only (0.936), then applied forward: FY2025 6,161 against 6,686 reported (reported 8.5% higher); H1 2026 3,804 against 3,850 (1.2% higher).
- First build, same periods (checker's recomputation): annual 0.88 to 1.23; rolling four quarters 0.73 to 1.25, s.d. 14%.

### 6b. All parameter sets
9,720 sets = 5 recognition profiles x 3 non-gas shares x 3 aero openings x 2 aero relativities (2.28, 3.0) x 2 HA relativities (1.0, 1.2) x 2 opening non-gas RPO x 3 non-gas order levels x 3 output paths x 3 aero rates.

| Statistic (after each set's own bias) | p10 | Median | p90 | Max |
|---|---|---|---|---|
| Bias | 0.92 | 1.00 | 1.08 | 1.17 (min 0.86) |
| Worst annual miss (2023, 2024, 2025, H1 2026) | 3.3% | 7.6% | 13.3% | 17.7% |
| Worst half-year miss (seven half-years) | 9.5% | 16.5% | 24.6% | 36.8% |
| Worst rolling four-quarter miss | 5.9% | 9.5% | 14.9% | 19.7% |
| Pooled s.d. of misses: annual / half-year / rolling | 5.8% / 9.9% / 5.7% | | | |

### 6c. Half-year pattern
Reported H1 halves average 0.977 of the bias-corrected model (0.936 to 1.021 across sets); H2 halves 1.029. Applying 0.977 gives the "H1 factor" row in section 0.

### 6d. Sequential steps between half-years (base)
Model step against reported step: +19% / +41%; -21% / -24%; +46% / +30%; -8% / -7%; -5% / +23%; +27% / +4%. Differences: -21, +3, +16, -1, -28, +23 points; s.d. 20 points. The model's forward step from H2 2026 to H1 2027 is about +22% to +28%; the Street's is -2%. That difference is 1.2 to 1.5 times this s.d.

### 6e. Band used
- From the back-test alone: +/-17% for a half-year (median worst miss), +/-10% for four quarters, +/-8% for a year.
- Forward inputs the back-test did not have to guess: output (+/-10% is +/-8% on revenue), aero rate (+/-4 a quarter is +/-3%), price index split (+/-10% is +/-7%). Combined with the 17%: about **+/-20%** on the H1 2027 figure.

### 6f. What the back-test does not test
1. Price layers shipped in 2023 to H1 2026 had an index of 227 to 431. The layers that ship from H2 2026 carry 321 to 751. The higher layers have never been through the model.
2. The back-test uses reported units. Forward it uses guided GW and an assumed class split.
3. The regression in 4b back-tests about as well and points the other way (H1 2027 $4.9B). It is contradicted by the H2 2026 guide (section 11a), but it shows that back-test fit alone does not settle the forward regime.

## 7. Placing the backlog in years

Management statements (paraphrased; sources in section 1):
- Output: about 3 GW a quarter to 5 GW a quarter from Q3 2026; at least 30 GW over the six quarters from Q3 2026; the next step to 6 GW a quarter some time in H2 2027; 6 GW for part of 2028, then 7 GW a quarter; 24 GW annualised in 2028; actions toward 30 GW in 2030.
- Aero: complements heavy-duty and "comes first" (Q2 2026 call). Aero and heavy-duty shipments for the same customer can be about 24 months apart. Aero growth in orders and revenue expected through 2026, 2027 and beyond (Q3 2025 call). Small aero units are 30 to 35 MW.
- 2026 orders: the 2026 change in backlog margin points to 2029 and 2030, when most of that equipment delivers (conference). Contracts signed in Q2 2026 are for 2030 and 2031 slots (call). Sold out through 2028, under 10 GW left for 2029 (December 2025).

Unit arithmetic:
- HA needed at 5 GW a quarter = (5.0 - 0.64 aero - 1.74 other heavy-duty) / 0.43 = about 6 a quarter. H2 2026: 12. 2027: 24 to 26. 2028: 28 to 32. Cumulative to end-2028: 64 to 70, against 70 in RPO.
- H2 2026 and H1 2027 need 24 HA. 43 HA ordered in 2025 are in backlog. So all HA shipped in those four quarters carry 2025 order values under any sequence. Value of the 24 oldest: $5.3B, against $2.8B for the 19 HA shipped in the last four quarters (2024 vintages).
- 2028 HA shipments are mostly H1 2026 orders if oldest first (July plan: 7 from Q4 2025, 12 from Q1 2026, 9 from Q2 2026). Lower bound: if aero ships 22 a quarter and other heavy-duty 2.25 GW a quarter, HA shipped to end-2027 is 26, which leaves 17 pre-2026 HA for 2028 against 28 to 32 needed.
- This fits "mostly 2029-30" for 2026 orders: 27 HA ordered in H1 2026 plus about 30 to 40 expected from H2 conversions = 57 to 67; 21 to 27 of them (35% to 45%) ship in 2028 and the rest later. The Q2 2026 statement about 2030-31 slots refers to new signings (mostly SRAs), not to the SRA conversions booked as orders.

Vintage of what ships (July plan, oldest first, base aero rate):

| Period | HA units by vintage | Other HD GW by vintage | Aero units by vintage |
|---|---|---|---|
| H2 2026 | Q1'25 8.0; Q2'25 4.2 | Q4'24 2.9; Q1'25 0.6 | Q4'24 3; Q1'25 9; Q2'25 20 |
| H1 2027 | Q2'25 2.8; Q3'25 9.1 | Q1'25 2.7; Q2'25 0.7 | Q2'25 7; Q3'25 9; Q4'25 18; Q1'26 2 |
| H2 2027 | Q3'25 3.9; Q4'25 8.1 | Q2'25 0.3; Q3'25 1.5; Q4'25 1.7 | Q1'26 7; Q2'26 29 |
| FY2028 | Q4'25 6.9; Q1'26 12.0; Q2'26 9.1 | Q4'25 1.3; Q1'26 2.6; Q2'26 3.2; later orders 0.9 | Q2'26 32; later orders 40 |
| FY2029 | Q2'26 5.9; later orders 26.4 | later orders 9.2 | later orders 72 |

## 8. Forward results against the Street

### 8a. Base parameters by output path (bias 0.961)

| Period | Street | Flat 20 GW | July plan | September ladder | Parts on the July plan before bias: non-gas / HA / other HD / aero | Units on the July plan: HA / other HD GW / aero |
|---|---|---|---|---|---|---|
| H2 2026 | 5,491 | 5,617 (+2%) | 5,617 (+2%) | 5,670 (+3%) | 667 / 2,657 / 1,274 / 1,245 | 12.2 / 3.5 / 32 |
| H1 2027 | 5,383 | 6,847 (+27%) | 6,900 (+28%) | 7,263 (+35%) | 676 / 3,204 / 1,518 / 1,778 | 11.9 / 3.4 / 36 |
| H2 2027 | 6,768 | 8,140 (+20%) | 8,495 (+26%) | 9,446 (+40%) | 676 / 3,735 / 2,080 / 2,345 | 11.9 / 3.4 / 36 |
| FY2027 | 12,151 | 14,987 (+23%) | 15,394 (+27%) | 16,708 (+38%) | 1,352 / 6,939 / 3,598 / 4,124 | 23.9 / 6.8 / 72 |
| H1 2028 | 7,099 | 8,759 (+23%) | 9,888 (+39%) | 10,857 (+53%) | 719 / 4,552 / 2,583 / 2,431 | 13.3 / 3.8 / 36 |
| H2 2028 | 8,790 | 9,196 (+5%) | 11,128 (+27%) | 12,254 (+39%) | 719 / 5,538 / 3,159 / 2,160 | 14.7 / 4.2 / 36 |
| FY2028 | 15,888 | 17,955 (+13%) | 21,016 (+32%) | 23,111 (+45%) | 1,438 / 10,090 / 5,742 / 4,591 | 28.1 / 8.0 / 72 |
| FY2029 | 19,256 | 18,817 (-2%) | 24,017 (+25%) | 25,077 (+30%) | 1,676 / 12,233 / 6,754 / 4,320 | 32.3 / 9.2 / 72 |
| FY2030 | 23,469 | 18,956 (-19%) | 26,493 (+13%) | 26,493 (+13%) | 1,977 / 13,668 / 7,594 / 4,320 | 37.8 / 10.8 / 72 |
| Cum. H2 2026 to 2028 | 33,530 | 38,559 (+15%) | 42,027 (+25%) | 45,489 (+36%) | | 53 GW on the July plan |
| Cum. 2027 to 2030 | 70,765 | 70,717 (0%) | 86,921 (+23%) | 91,390 (+29%) | | |

Value shipped at vintage prices, last four quarters against next four (July plan): HA 19 units $2,775M to 24.1 units $5,314M; other heavy-duty 4.7 GW $1,479M to 6.9 GW $2,475M; aero 43 units $1,079M to 68 units $3,023M.

### 8b. All parameter sets
See the table in section 0. By recognition profile (all paths, medians): H1 2027 gap +27% (point in time), +34% (half), +37% (even), +29% (scope), +25% (late). H2 2026 gap 0%, +3%, +4%, -2%, -5%.

### 8c. FY2028 to FY2030 with the inputs that are not in backlog
FY2028 includes 40 aero units and 0.9 GW of other heavy-duty that are not yet ordered. From FY2029 nearly everything is from SRAs or future orders.

| Path | Future HD $/kW, aero $M | Aero a quarter from 2027 | FY2028 | FY2029 | FY2030 | Cum. 2027-30 |
|---|---|---|---|---|---|---|
| Flat | 620, 50 | 10 | 16,958 (+7%) | 16,435 (-15%) | 16,088 (-31%) | 63,277 (-11%) |
| Flat | 800, 70 | 18 | 18,572 (+17%) | 21,056 (+9%) | 21,492 (-8%) | 76,108 (+8%) |
| July | 620, 50 | 10 | 19,662 (+24%) | 20,967 (+9%) | 22,756 (-3%) | 77,614 (+10%) |
| July | 700, 60 | 18 | 21,016 (+32%) | 24,017 (+25%) | 26,493 (+13%) | 86,921 (+23%) |
| July | 800, 70 | 18 | 21,967 (+38%) | 27,160 (+41%) | 30,106 (+28%) | 94,627 (+34%) |
| Ladder | 620, 50 | 10 | 21,380 (+35%) | 21,893 (+14%) | 22,756 (-3%) | 81,562 (+15%) |
| Ladder | 800, 70 | 18 | 24,407 (+54%) | 28,521 (+48%) | 30,106 (+28%) | 99,742 (+41%) |

Management guided H2 2026 gas orders to the high end of 10 to 20 points above Q4 2025 in dollars per kW (all-in $838 to $904 on the derived $753; mix not stated). One broker already publishes 30 GW at about $900/kW for 2030 ($27.0B).

## 9. The Street in physical terms

| Period | Street $M | $/kW at flat or July GW | $/kW at ladder GW |
|---|---|---|---|
| H2 2026 | 5,491 | 549 (10 GW) | 549 |
| H1 2027 | 5,383 | 538 (10 GW) | 538 |
| H2 2027 | 6,768 | 677 (10 GW) | 588 (11.5 GW) |
| FY2027 | 12,151 | 608 (20 GW) | 565 (21.5 GW) |
| FY2028 | 15,888 | 691 (23 GW) | 623 (25.5 GW) |
| FY2029 | 19,256 | 741 (26 GW) | 688 (28 GW) |
| FY2030 | 23,469 | 782 (30 GW) | 782 |

- Realised: $365 (H1 2025), $520 (H2 2025), $437 (FY2025), $513 (H1 2026), $516 (last four quarters).
- All-in order price of the vintages: FY2024 $417; Q1 2025 $415; Q2 2025 $729; Q3 2025 $620; Q4 2025 $753; FY2025 $635 (deck basis $612); Q1 2026 $705; Q2 2026 $1,049.
- Ordinary reading of the Street's H1 2027: 10 GW x $538/kW = guided output at the trailing realised price plus 4%.
- In class terms. Street H1 2027 less non-gas 676 less 36 aero at $45M to $68M leaves $2.26B to $3.09B for 11.9 HA and 3.4 GW of other heavy-duty: $122M to $166M per HA. HA shipped in the last four quarters (2024 vintages): $120M to $190M. HA due in H1 2027 (Q2 and Q3 2025 vintages): about $246M ($197M to $240M with a higher aero relativity).
- Street FY2028 on the July plan, same method with 72 aero: $219M to $257M per HA. Vintages due: Q4 2025 $307M, Q1 2026 $291M, Q2 2026 $387M. With only the 32 aero already ordered, the Street leaves $281M to $298M per HA, which matches Q4 2025 to Q1 2026 values.

## 10. Stress tests (September ladder, base parameters, bias-corrected)

| Case | H2 2026 | H1 2027 | Q3'26-Q2'27 | FY2027 | FY2028 |
|---|---|---|---|---|---|
| Base | 5,670 (+3%) | 7,263 (+35%) | 12,932 (+19%) | 16,708 (+38%) | 23,111 (+45%) |
| Output flat at 20 GW | 5,617 (+2%) | 6,847 (+27%) | 12,464 (+15%) | 14,987 (+23%) | 17,955 (+13%) |
| 2025 vintages blended (no order inside 2025) | 6,241 (+14%) | 6,889 (+28%) | 13,130 (+21%) | 15,544 (+28%) | 22,543 (+42%) |
| Output 10% short (4.5 GW a quarter) | 5,104 (-7%) | 6,480 (+20%) | 11,584 (+7%) | 14,748 (+21%) | 20,843 (+31%) |
| Output 20% short (4 GW a quarter) | 4,576 (-17%) | 5,701 (+6%) | 10,277 (-5%) | 12,822 (+6%) | 18,352 (+16%) |
| Price index of 2025+ vintages 10% lower | 5,266 (-4%) | 6,641 (+23%) | 11,907 (+9%) | 15,259 (+26%) | 21,938 (+38%) |
| Price index 20% lower | 4,857 (-12%) | 6,012 (+12%) | 10,869 (0%) | 13,792 (+14%) | 20,751 (+31%) |
| Output 10% short and index 10% lower | 4,752 (-13%) | 5,928 (+10%) | 10,680 (-2%) | 13,474 (+11%) | 19,468 (+23%) |
| Same, plus point in time and aero 14 a quarter | 4,594 (-16%) | 5,144 (-4%) | 9,737 (-10%) | 12,108 (0%) | 18,210 (+15%) |
| Aero 12 a quarter | 5,531 (+1%) | 6,852 (+27%) | 12,383 (+14%) | 15,670 (+29%) | 22,571 (+42%) |
| 40% of heavy-duty value after shipment (late profile) | 5,238 (-5%) | 6,540 (+21%) | 11,778 (+8%) | 15,436 (+27%) | 22,262 (+40%) |
| Heavy-duty priced one year older (rival timing), July plan, before bias | 4,788 (-13%) | 5,826 (+8%) | 10,614 (-2%) | 12,995 (+7%) | 18,591 (+17%) |
| Same, output flat | 4,788 (-13%) | 5,786 (+7%) | 10,574 (-3%) | 12,699 (+5%) | 16,143 (+2%) |

- The H1 2027 gap goes to zero only when several adverse inputs are combined. Each of those cases also puts H2 2026 12% to 17% below the guide-anchored Street, so it would show first in the Q3 and Q4 2026 prints.
- The rival timing case prices HA at 2024-vintage values. Section 3 shows no HA ordered before 2025 is left in RPO, so this case conflicts with the unit count for HA. It remains possible for other heavy-duty (2.9 GW of Q4 2024 orders left) and aero.

## 11. Cross-checks on company-reported data

**(a) The guided half.** FY2026 Power revenue guide of +18% to +20% gives Power H2 2026 of $12.9B to $13.3B. Less services of $7.3B to $7.66B (H2 2025 6,896 x 1.06 to 1.11) leaves equipment of $5.2B to $6.0B. Street 5,491. Unit-class model 5,172 to 5,783. First-in-first-out GW layers: 4,833 x 0.90 = 4,350 (-21%). Regression: 4,604 (-16%).

**(b) The company's own schedule.** 10-Q Q2 2026 RPO note: 36% of $87,821M of equipment RPO, $31,616M, within one year (all segments). Street equipment revenue for the same four quarters: $30,245M (Power 10,874; Wind 5,830; Electrification 13,541). Model Power of 11.6B to 13.4B plus the Street's Wind and Electrification gives $31.0B to $32.8B, or 0.98 to 1.04 times the schedule. Reported windows since the spin: 0.92, then 1.03 to 1.11. The model's Power figure fits inside the filed schedule. The Street's total is below the schedule itself (see the RPO candidate file: checkers' centre +5% to +7%, band +/-4.5% to +/-7%).

**(c) The 2028 framework (December 2025).** Power revenue growing at a high-teens rate from 2025 gives $31.7B to $33.3B in 2028. Street 2027 Power: $28.1B (+19%). Model 2027 Power = Street services 15,675 + equipment 14.4B to 17.4B = $30.1B to $33.1B (+27% to +40% on about $23.6B in 2026). The model reaches the 2028 marker a year early. This is the main contrary evidence: the marker was set with 2027 and 2028 slots sold. Facts on the other side: the framework's stated assumption is pricing at recent orders; it lists turbine pricing above current order levels as upside; the 2028 revenue marker was raised from $45B to $52B in one year; the FY2026 guide was raised twice.

**(d) H1 2027 by five methods.**

| Method | H1 2027 | vs Street 5,383 |
|---|---|---|
| Regression on units with trend (4b) | 4,909 | -9% |
| 10 GW x FY2025 all-in order price ($612 deck, $635 derived) | 6,120 to 6,350 | +14% to +18% |
| First-in-first-out GW layers, positions 10 to 20 GW, x 0.90 | 6,736 x 0.90 = 6,062 | +13% |
| Same without the haircut | 6,736 | +25% |
| Unit-class model, all sets, with the H1 factor | 6,335 / 6,864 / 7,490 | +18% / +28% / +39% |

## 12. The six kill reasons

| # | Kill reason | What this rebuild shows |
|---|---|---|
| 1 | Rival explanation: Street FY2028 = 24 GW x about $735/kW x 0.90 | Still stands for FY2028 taken alone. In class terms the Street's FY2028 equals the July plan with HA at Q4 2025 to Q1 2026 values and only the aero already ordered (section 9). It cannot be rejected with disclosed data. For H1 2027 the matching rival is "guided GW at the trailing realised price" ($538 against $516). That needs HA shipped in H1 2027 to carry 2024-vintage dollars, and no HA ordered before 2025 is left in RPO (section 3). The 0.90 haircut is not supported at class level: bias is 0.92 to 1.08, median 1.00; past low conversion is explained by the non-gas book, estimated at about a quarter of RPO at end-2023 and about 7% now (neither is disclosed). |
| 2 | Gap sat in one order layer (Q2 2026), lifted by aero mix and combined-cycle scope; aero ships first; 2026 heavy-duty orders deliver 2029-31 | The layer is split by class (section 4c): aero $4.2B (61 units), HA $5.8B, other heavy-duty $2.4B. Aero is placed in H2 2027 and 2028, HA in H2 2028 to early 2029. The H1 2027 and four-quarter windows use no Q2 2026 dollars for heavy-duty: they rest on the Q1 to Q4 2025 layers ($18.9B derived, $18.2B deck). FY2028 still leans on the Q2 2026 layer (9 of 28 HA on the July plan) and on 40 aero units not yet ordered. |
| 3 | Error band: first-in-first-out layers miss four-quarter windows by -27% to +25% | Class model, same windows: -8% to +9% after bias (base); median worst miss across 9,720 sets 9.5% (four quarters), 16.5% (half-year), 7.6% (annual). Sequential half-year steps miss by 20 points (s.d.). Not tested: any price layer above an index of 431. |
| 4 | Reveal date: FY2028 prints February 2029 | H1 2027 is reported in the Q2 2027 10-Q (late July 2027) and Q1 2027 in late April 2027. FY2027 prints late January 2028 and FY2028 in February 2029, both outside 12 months. |
| 5 | Thin and partly stale Street data on the division line; one broker already at 30 GW x $900 for 2030 | Not fixed. No contributor count for the Power equipment line. Q3 2026 low / high is 2,063 / 2,591 around 2,394 (-14% / +8%). Street Power organic growth is a flat 18 in every 2027 quarter (one contributor). Headline quarterly revenue has 22 estimates for Q1 and Q2 2027. Lines with broader coverage that carry the same finding: Power revenue H1 2027 $12,946M (+8% to +18% on the model) and company revenue H1 2027 $24,111M (+4% to +10%). The 30 GW x $900 view concerns 2030, where this rebuild makes no call. |
| 6 | Small profit effect (+3% to +10% of 2028 EBITDA) | Section 13: H1 2027 +4% to +26% of the half's Street EBITDA (median case +6% to +18%); FY2027 +4% to +25%. Larger and earlier than before, but the drop-through is not disclosed and the Street's Power margin (21.0% in 2027 against 17.6% in H1 2026) may already hold part of it. |

## 13. Profit effect (ranges)

Street EBITDA: H1 2027 $4,038M (sum of quarters); FY2027 $9,391M (sum of quarters; annual consensus $9,471M). Street Power adjusted EBITDA: H1 2027 $2,639M; FY2027 $5,906M.

| Case | Extra revenue | EBITDA at 15% | at 25% | at 45% |
|---|---|---|---|---|
| H1 2027, p10 (6,408) | 1,025 | 154 (+3.8%) | 256 (+6.3%) | 461 (+11.4%) |
| H1 2027, median (7,019) | 1,636 | 245 (+6.1%) | 409 (+10.1%) | 736 (+18.2%) |
| H1 2027, p90 (7,718) | 2,335 | 350 (+8.7%) | 584 (+14.5%) | 1,051 (+26.0%) |
| FY2027, p10 (14,409) | 2,258 | 339 (+3.6%) | 565 (+6.0%) | 1,016 (+10.8%) |
| FY2027, median (15,819) | 3,668 | 550 (+5.9%) | 917 (+9.8%) | 1,651 (+17.6%) |
| FY2027, p90 (17,445) | 5,294 | 794 (+8.5%) | 1,324 (+14.1%) | 2,382 (+25.4%) |

Drop-through: 15% is about the equipment gross margin (13% in Q2 2026); 25% is an incremental volume rate; 45% applies if about half the extra revenue is price on units whose cost is unchanged. $1B of EBITDA at 25x is $94 a share (266.334M shares).

## 14. Dates and company-reported numbers (candidate marks; the team sets its own)

| Date | Number | Supports | Contradicts |
|---|---|---|---|
| 2026-10-28 (Q3 10-Q) | Gas GW sold in Q3; HA and aero units sold | 4.8 GW or more; 6 or more HA; 14 or more aero | 4.2 GW or less |
| Late January 2027 (Q4 release, 10-K) | H2 2026 Power equipment revenue (Street 5,491; model 5.2B to 5.8B) | 5.5B or more on 10 GW | 5.0B or less with 10 GW shipped (the price layers are not converting) |
| Same | FY2027 Power revenue guide (Street +19%; model +27% to +40%) | +25% or more | +20% or less (management does not see the step; the sibling rebuild `gw-guide-predictor` expects 16% to 21%) |
| Same | HA units in RPO at end-2026 (10-K) | Ties to 70 less H2 shipments plus H2 orders | |
| Late April 2027 (Q1 10-Q) | Q1 2027 Power equipment revenue (Street 2,585; model 3.1B to 3.7B at 49% of the half) | 3.0B or more | 2.7B or less |
| **Late July 2027 (Q2 10-Q)** | **Power equipment revenue, six months to 30 June 2027 (Street 5,383)** | **6.2B or more (Street +15%)** | **5.6B or less** |

## 15. What the angle is good for whatever the result

1. An exhibit of the Street in physical terms: revenue per kW held at $540 to $610 through 2027 while the vintages due to ship were ordered at $620 to $750 all-in (section 9).
2. A class table of the backlog: 70 HA, 17.5 GW of other heavy-duty, about 136 aero, with vintage dollars (section 5).
3. The driver structure for a Power equipment model: non-gas base + aero units x value + HA units x value + other heavy-duty GW x $/kW, with a recognition profile; back-tested error by horizon (section 6).
4. The Q2 2026 order split by class (section 4c).
5. A dated scorecard that separates three readings early: units sold by class on 28 October, H2 2026 revenue against 5.2B to 5.8B in January, and the two 2027 quarters.

## 16. Weak points

1. Untested regime: no unit ordered in 2025 or later has shipped. The step from 2024-vintage to 2025-vintage dollars is the whole H1 2027 gap.
2. Half-year timing: the model's sequential steps miss by 20 points. Revenue could arrive in Q4 2026 (then H2 2026 beats the guide) or slip to H2 2027.
3. Output: every forward figure assumes 5 GW a quarter from Q3 2026. H1 2026 shipped 7.5 GW; Q2 2026 3.3 GW. At 4 GW a quarter the H1 2027 gap is +6%.
4. Price index: one index per quarter, split with one broker's relativities for Q2 2026. Non-gas orders are assumed flat at $300M a quarter; the CFO said Q3 2025 held non-gas orders with no GW attached. Aero values for 2024 vintages ($21M to $34M a unit) look low against typical package prices, so the class split is rough even though dollars are conserved.
5. Street line: thin and not verifiable (kill reason 5).
6. Management's own framework and guide history sit near the Street for 2027 (section 11c).
7. A regression with similar back-test fit gives H1 2027 below the Street (section 4b).
8. Opening aero backlog and opening non-gas RPO are estimates. With an aero opening of zero the bias falls to 0.82.
9. Class split of forward output (60 / 40 HA to other heavy-duty by GW) is an assumption tied to one company statement (90 to 100 heavy-duty units at 24 GW).
10. Profit drop-through is not disclosed; the Street's Power margin may already include the price.
11. Past revenue beats did not move the stock (Q2 2026: revenue above consensus, shares -8.7% on the day).

## 17. Reproduce

Base parameters. Prints the bias, the back-test table in 6a and the base rows of 8a. The grid in 6b varies the constants at the top.

```python
import json, numpy as np
Q=['2023Q1','2023Q2','2023Q3','2023Q4','2024Q1','2024Q2','2024Q3','2024Q4','2025Q1','2025Q2','2025Q3','2025Q4','2026Q1','2026Q2']
# (heavy-duty units incl. HA, HA units, aero units, GW) from the 10-Q / 10-K Power tables
SOLD=[(18,4,5,3.6),(9,3,5,2.3),(12,2,7,2.7),(19,5,16,5.2),(10,1,7,2.3),(8,1,7,1.5),(13,5,5,3.3),(17,8,8,4.8),(12,5,7,3.0),(18,8,3,5.2),(14,6,6,4.0),(10,5,11,3.1),(15,5,10,4.2),(13,3,16,3.3)]
ORD =[(6,4,7,2.3),(14,0,12,2.1),(12,4,8,3.1),(9,0,25,2.1),(16,8,18,4.9),(14,4,1,4.1),(14,9,15,5.1),(24,4,10,6.1),(29,8,9,7.1),(20,7,27,5.1),(20,13,9,7.4),(41,15,18,10.2),(28,12,9,8.1),(52,15,61,12.1)]
REV =[1180,1147,1291,1980,1201,1285,1426,1796,1491,1505,1744,1946,1885,1965]                      # Power equipment revenue
RPO =[13579,13992,13980,13865,13636,14394,10978,11392,12461,13920,16133,18977,24707,28530,39261]  # Power equipment RPO, end-2022 first
NG  =[939,1080,949,1248,994,996,741,932,844,874,916,1127,905,1050]                                 # Nuclear + Hydro + Steam revenue
EDF=3900; MHA,MAE=0.43,0.04; RHA,RAE=1.2,2.28; NGO=300; NG_SHARE=0.30; A0=20; NG_RPO0=2500
W={0:0.5,1:1/6,2:1/6,3:1/6}        # heavy-duty: half in the shipment quarter, half over the three quarters before
FQ=[f'{y}Q{q}' for y in range(2026,2032) for q in range(1,5)][2:]
PATH={'flat':[5]*22,'july':[5]*6+[5.5,5.5,6,6]+[6.5]*4+[7.5]*8,'ladder':[5,5,5,5,5.5,6,6,6,6.5,7]+[7]*4+[7.5]*8}
NGF={'2026':2223/2,'2027':4507/4,'2028':4795/4,'2029':5586/4,'2030':6589/4,'2031':6589/4}  # Street Nuclear + Hydro per quarter (Bloomberg, 2026-10-01)
def model(path='july',aero=(16,18),ohd_share=0.40,p_future=700.0,ae_future=60.0):
    cls=lambda t:(t[1],t[0]-t[1],t[2])
    D=[RPO[i+1]-RPO[i]+REV[i]+(EDF if Q[i]=='2024Q2' else 0) for i in range(14)]
    ogw0=21.7-MHA*28-MAE*A0; p0=(RPO[0]-EDF-NG_RPO0)/(RHA*MHA*28+ogw0+RAE*MAE*A0)
    L={'HA':[[28.0,p0*RHA*MHA]],'oHD':[[ogw0,p0]],'AE':[[float(A0),p0*RAE*MAE]]}   # [quantity, $M a unit or $/kW]
    V={c:[] for c in L}
    for i,q in enumerate(Q+FQ):
        if i<14:
            ha,ohd,ae=cls(SOLD[i]); ship={'HA':ha,'oHD':max(SOLD[i][3]-MHA*ha-MAE*ae,0.06*ohd),'AE':ae}
        else:
            gw=PATH[path][i-14]; ae=aero[0] if q[:4]=='2026' else aero[1]; hd=gw-MAE*ae
            ship={'HA':(1-ohd_share)*hd/MHA,'oHD':ohd_share*hd,'AE':ae}
        for c in L:
            if sum(l[0] for l in L[c])<ship[c]+1e-9: L[c].append([1e9,{'HA':p_future*RHA*MHA,'oHD':p_future,'AE':ae_future}[c]])
            need,val=ship[c],0.0
            while need>1e-9:
                t=min(L[c][0][0],need); val+=t*L[c][0][1]; L[c][0][0]-=t; need-=t
                if L[c][0][0]<1e-9: L[c].pop(0)
            V[c].append(val)
        if i<14:
            ha,ohd,ae=cls(ORD[i]); ogw=max(ORD[i][3]-MHA*ha-MAE*ae,0.06*ohd)
            p=(D[i]-NGO)/(RHA*MHA*ha+ogw+RAE*MAE*ae)
            L['HA'].append([float(ha),p*RHA*MHA]); L['oHD'].append([ogw,p]); L['AE'].append([float(ae),p*RAE*MAE])
    n=len(Q+FQ); tot=np.array([NG_SHARE*(NG[i] if i<14 else NGF[(Q+FQ)[i][:4]]) for i in range(n)])
    for c in V:
        for s in range(n):
            for k,x in (W if c!='AE' else {0:1.0}).items():
                if 0<=s-k<n: tot[s-k]+=x*V[c][s]
    return dict(zip(Q+FQ,tot))
m=model('july'); act=dict(zip(Q,REV)); bias=sum(REV)/sum(m[q] for q in Q); print('bias',round(bias,3))
per={'FY2023':Q[0:4],'FY2024':Q[4:8],'FY2025':Q[8:12],'H1 2026':Q[12:14],'H1 2023':Q[0:2],'H2 2023':Q[2:4],'H1 2024':Q[4:6],'H2 2024':Q[6:8],'H1 2025':Q[8:10],'H2 2025':Q[10:12]}
for k,qs in per.items(): print(k,sum(act[q] for q in qs),round(sum(m[q] for q in qs)),f'{sum(act[q] for q in qs)/sum(m[q] for q in qs)-1:+.1%}')
d=json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
st=lambda qs:sum(d[f'Total Revenue|Power|Equipment|{q[:4]} Q{q[5]}'] for q in qs)
fp={'H2 2026':['2026Q3','2026Q4'],'H1 2027':['2027Q1','2027Q2'],'FY2027':[f'2027Q{i}' for i in range(1,5)],'FY2028':[f'2028Q{i}' for i in range(1,5)]}
for path in PATH:
    m=model(path); print(path,{k:(round(sum(m[q] for q in qs)*bias),round(st(qs))) for k,qs in fp.items()})
```

Other scripts (scratchpad `uc/`): `data.py`, `model.py`, `run.py` (full model with profiles and stress switches), `grid.py`, `biggrid.py` (9,720 sets), `fwd.py`, `sens.py`, `final1.py` (regression, first-in-first-out layers, Street per kW), `final2.py` (tables in sections 8, 9 and 13). Corpus query for the unit tables: `SELECT accession, filing_date, text FROM chunks WHERE ticker='GEV' AND form IN ('10-Q','10-K') AND text LIKE '%Gas Turbine Gigawatts%'`.
