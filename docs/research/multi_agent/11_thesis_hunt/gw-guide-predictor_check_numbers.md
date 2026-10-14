# Check (recompute and back-test): gw-guide-predictor

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team (ranges and methods only). Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Check type: RECOMPUTE AND BACK-TEST. Every number in `gw-guide-predictor.md` was redone in Python from the primary files. All money in $M unless stated.

Terms (same as the rebuild): **price in backlog** = Power equipment RPO / firm gas GW. **k** = Power equipment revenue per kW in a target year / price in backlog at the vantage date. **Street** = Bloomberg BEst mean. **Like-for-like** = our figure and the Street figure built from the same set of broker models.

## 0. Verdict

| Item | Rebuild | This check |
|---|---|---|
| Arithmetic reproduces from primary files | | **Yes** (small slips, section 2) |
| Gap, 2030 EBITDA, centre | +4.6% | **+2.2%** like-for-like; +0.4% to +1.1% after the rebuild's own aeroderivative strip |
| Gap, 2030 revenue, centre | +2.6% | **+1.3%** like-for-like; -0.3% to +0.3% after the strip |
| Error band, EBITDA | about +/-13% | **about +/-12%** (+/-9% from inputs; +/-12% from outlook-against-Street history) |
| Error band, revenue | about +/-8% | +/-6% to +/-8% |
| Gap at least 7% | No | **No** |
| Gap clearly larger than the band | No | **No** (gap is about one fifth of the band) |
| Kill reasons answered (of 6) | | 0 fully; 2 in part (reasons 2 and 4); 4 conceded |
| **survives** | holds = false | **false** |

The rebuild's own verdict (does not hold) is confirmed. The corrections below make the gap smaller, not larger.

## 1. What was recomputed, and whether it matches

| Item | Rebuild | Recomputed | Match |
|---|---|---|---|
| Street Power equipment 2027-30 (`segment_quarterly.json`) | 12,151 / 15,888 / 19,256 / 23,469 | same | yes |
| Street Power services / Power total 2030 | 22,357 / 45,215 | same; equipment + services = 45,826 (611 above the Power total) | yes |
| Company revenue / EBITDA 2030, annual BEst (workbook, sheet Consensus) | 79,724 / 19,544; 20 estimates; sd 2,147 | same; sd 11.0%; low -16.5%; high +31.8% | yes |
| Company revenue / EBITDA 2030, sum of quarters | 80,718 / 19,471 | same; 12 / 11 brokers (`02-eeo-annual-2030.xlsx`) | yes |
| GW ordered and sold, equipment revenue, equipment RPO, Q3 2024 to Q2 2026 (10-Q / 10-K Power tables in `gev.db`) | section 2a | all 8 quarters match the filings | yes |
| Firm GW and SRA GW (earnings releases, documents 291, 277, 268, 265, 226, 215) | 29 / 29 / 33 / 40 / 44 / 53; 21 / 25 / 29 / 43 / 56 / 63 | same | yes |
| Deck equipment orders (Q4 2025 deck p.18; Q2 2026 deck p.15) | 2,906 / 2,842 / 3,519 / 4,448 / 7,432 / 5,611 / 12,650; FY24 8,340; FY25 18,241 | same | yes |
| Price in backlog | 465 / 483 / 480 / 556 / 575 / 618 / 648 / 741 | same | yes |
| FY26 Power on H1 actual + Street H2 | 23,609 (+18.8% on 19,873) | 23,609; +18.8% | yes |
| Back-test A, December 2024: residual Power 2028; ratio; k | 24.9B (23.5-26.2); 1.08; 0.99 | 24,873 (23,515-26,193); 1.076; 0.989 | yes |
| Back-test A, December 2025: published / arithmetic; k | 1.11; 1.16 | 1.106; 1.159 | yes |
| Back-test B: layers for 17.5 GW; FY26 growth | 7,624; +8.7% to +10.0% | 7,624; +8.7% to +10.0% | yes |
| 2026 equipment against layers | about 23% ahead | 9,342 / 7,624 = 1.225 | yes |
| Back-test C: outlook against Street (sheet ConsensusHistory) | revenue -2.8%, -0.6%, +3.4%; EBITDA -11.8%, +12.3%, +6.8% | same | yes |
| Street 2028 EBITDA one week after December 2025 | +12% | 9,264 to 10,385 = +12.1% | yes |
| Street today against the 2028 framework | +8.9% / +12.1% | +8.9% / +12.1% | yes |
| Year-end price in backlog | $799-829 | $799-829 | yes |
| 2030 ranges (equipment, Power, company, EBITDA methods 1-3) | section 7a | all cells match (low case 74,786 against 74,776: rounding of k) | yes |
| FY27 Power guide range in dollars | 27,386-28,566; centre 27,740 (-1.4%) | same | yes |
| 2028 restated cases | 31,293 / 34,835 / 40,486 | same | yes |
| Street in physical terms | 16.4 / 21.4 / 26.0 / 31.7 GW at $741; $782/kW in 2030 | same | yes |
| Per-share effect | +$44 at 13.0x | 901 x 13.03 / 266.334 = $44.1 | yes |
| Company statements (December 2024 deck, release, transcript; December 2025 deck, release, transcript; January 2026 deck; July 2026 call; 16 September 2026 conference transcript) | sections 3a, 6 | each read again on gevernova.com or in the corpus; wording confirmed | yes |

## 2. Corrections

| # | Point | Effect |
|---|---|---|
| 1 | **Two different Street bases are mixed.** The centre is built from division lines that come from quarterly models (12 brokers; total 80,718). It is then compared with the annual BEst mean (20 estimates; 79,724), which is 1.25% lower. Putting pure Street division figures through the rebuild's own formula (Power 45,215 + Electrification 28,422 + Wind 7,440 - 450) gives 80,627, already +1.1% against 79,724 with no view at all | Revenue gap like-for-like is 81,781 / 80,718 = **+1.3%**, not +2.6% |
| 2 | **The EBITDA gap contains a margin opinion.** +4.6% = centre revenue x 25.0%, against a Street margin of 24.5% (annual) or 24.1% (quarterly basis). The rule says nothing about margin | Without the margin opinion: +2.6% (annual Street margin), +0.9% (quarterly-basis margin), **+2.2%** (extra Power revenue of 1,794 at the Street's Power margin of 26.8%, less the Wind cut of 640 at the Street's Wind margin = +434) |
| 3 | The Power centre (+4.0%) is measured against the Power total (45,215). Against the Street's own equipment + services lines (45,826) it is +2.6% | Division-level gap is smaller than shown |
| 4 | The aeroderivative strip (-3% to -5% on the year-end price in backlog) is sized in section 9 of the rebuild but not applied to its centre | Applied: equipment 24.9-25.5B (+6% to +9% on the Street line); company revenue +0.9% to +1.6% against BEst, **-0.3% to +0.3% like-for-like**; EBITDA +0.4% to +1.1% like-for-like |
| 5 | k centre of 1.07 is the mean of two outlook-implied values. On reported results the three-year k has been 0.94, 0.97 and 1.08 (section 3b), mean 1.00 | At k = 1.00: equipment 24,450; Power 45,200 = the Street's 45,215; company +0.3% against BEst, -0.9% like-for-like |
| 6 | Only one of the three "eve" comparisons is a true pre-event, independent one. The December 2024 Street figure is dated 2025-01-10 (after the event). January 2026 only added Prolec | Independent pre-event comparisons: n = 1 (December 2025), not 2 |
| 7 | The year-end price in backlog is a forecast. H2 2026 orders not yet booked are 27% to 40% of the year-end backlog dollars. The Q2 2026 layer alone lifts the 6/30/26 average from $651 to $741 (+14%). Q2 2026 and H2 2026 layers together are 54% to 63% of year-end dollars | The dependence on one order layer becomes a dependence on two, one of them not yet booked |
| 8 | Small items. Nine-month 2024 order price: 395 (derived) against 385 from the deck, (8,340 - 2,906) / 14.1. FY27 layer dollars: 13,966-15,095 (rebuild: 14.0-15.5B). The 2026-01-28 price move is a same-day close, not next-day. The "$6.5B" figure at the December 2024 event was an analyst's own estimate inside a question; management did not confirm it and the year is not clear. The corpus copy of source 3886 does not contain the "$900 per kilowatt" sentence; the live article does (Yahoo Finance, 2026-07-25) | None on the verdict |

## 3. Back-tests re-run on every window available

### 3a. The two three-year outlooks (the rebuild's calibration)

| | December 2024 | December 2025 |
|---|---|---|
| Published Power 2028 | none; residual 24,873 (23,515-26,193) | 19,767 x 1.18^3 = 32,478 (31,659-33,311) |
| Arithmetic (GW x order price x 0.90 + services) | 23,113 | 29,352 |
| Published / arithmetic | 1.076 | 1.106 |
| k at centre | 0.989 | 1.159 |
| k across services growth only | 0.92-1.05 | 1.09-1.22 |
| k across all undisclosed inputs | 0.78-1.19 | 0.98-1.29 (base 19,305-19,767; rate 17-19%; services 6-10%) |
| k if the 2028 GW is a calendar total of 22-23, not 24 | n/a | 1.21-1.27 |

**Out-of-sample test (n = 1 each way).** Take k from one event and predict the other.

| Direction | Predicted equipment | Implied by the published outlook | Error on equipment | Error on Power | Error on company revenue |
|---|---|---|---|---|---|
| k of December 2024 (0.989) applied to December 2025 (24 GW x $575) | 13,643 | 16,000 | **-14.7%** | -7.3% | -4.5% |
| k of December 2025 (1.159) applied to December 2024 (20 GW x $465) | 10,782 | 9,194 | **+17.3%** | +6.4% | +3.5% |

- Direction test for December 2025. Rule Power 30,126 against published 32,478. With the other divisions as published, the rule gives company revenue of about 49.6B, which is 5.1% below the Street on the eve (52,294). The outlook came out 0.6% below the Street on revenue and 12.3% above it on EBITDA. The rule would have pointed the wrong way on the number that moved the stock (+15.6%). The other divisions' Street figures on that date are not in the pull, so this uses the published figures for them.

### 3b. The rule against reported results (not used by the rebuild)

Rolling four-quarter windows. Realised k = equipment revenue / (GW sold x price in backlog at the start). Firm GW is disclosed from Q1 2025 and rolled back before that (+/-1 GW). The EDF item ($3.7-3.8B) is removed before Q2 2024.

| Start | Window | GW sold | Revenue | Revenue $/kW | Price in backlog | k |
|---|---|---|---|---|---|---|
| YE22 | 2023 | 13.8 | 5,598 | 406 | 452 | 0.90 |
| Q1 2023 | Q2 2023-Q1 2024 | 12.5 | 5,619 | 450 | 502 | 0.90 |
| Q2 2023 | Q3 2023-Q2 2024 | 11.7 | 5,757 | 492 | 507 | 0.97 |
| Q3 2023 | Q4 2023-Q3 2024 | 12.3 | 5,892 | 479 | 492 | 0.97 |
| YE23 | 2024 | 11.9 | 5,708 | 480 | 567 | 0.85 |
| Q1 2024 | Q2 2024-Q1 2025 | 12.6 | 5,998 | 476 | 532 | 0.90 |
| Q2 2024 | Q3 2024-Q2 2025 | 16.3 | 6,217 | 381 | 484 | 0.79 |
| Q3 2024 | Q4 2024-Q3 2025 | 17.0 | 6,535 | 384 | 465 | 0.83 |
| YE24 | 2025 | 15.3 | 6,685 | 437 | 483 | 0.91 |
| Q1 2025 | Q2 2025-Q1 2026 | 16.5 | 7,079 | 429 | 480 | 0.89 |
| Q2 2025 | Q3 2025-Q2 2026 | 14.6 | 7,540 | 516 | 556 | 0.93 |
| Q3 2025 | Q4 2025-Q3 2026 (one Street quarter) | 15.6 | 8,190 | 525 | 575 | 0.91 |
| YE25 | 2026 (two Street quarters, 17.5 GW plan) | 17.5 | 9,341 | 534 | 618 | 0.86 |

Eleven fully reported windows: k 0.79 to 0.97, mean 0.89, standard deviation 0.05.

Longer horizons. Year-end price in backlog against revenue per kW in a later calendar year:

| Vantage (price) | +1 year | +2 years | +3 years | +4 years |
|---|---|---|---|---|
| YE22 ($452) | 0.90 | 1.06 | 0.97 | 1.18 |
| YE23 ($567) | 0.85 | 0.77 | 0.94 | |
| YE24 ($483) | 0.91 | 1.11 | | |
| YE25 ($618) | 0.86 | | | |
| 9/30/23 ($492) to 2026 | | | 1.08 | |

- Ten year-end pairs: k 0.77 to 1.18, mean 0.95, standard deviation 0.12. Three-year pairs (overlapping): 0.94, 0.97, 1.08.
- One-year k is stable (0.79-0.97) but sits near 0.89, and it falls when prices rise fast (0.86 for 2026). It cannot be carried to the 2030 target. Multi-year k has a spread of +/-0.12 to +/-0.2.

### 3c. Oldest-first layers (the method that was killed)

Rolling four-quarter windows, reported / predicted, 11 windows: 0.73 to 1.25, mean 0.95, standard deviation 0.14. Same as the earlier checker. Forward: H2 2026 layers 4,493 (4,044 at 0.90) against Street and guide 5,491.

### 3d. One-year guides

| | FY25 first guide | FY26 first guide | FY27 (forward) |
|---|---|---|---|
| Guide | mid-single digit | 16-18% | Street +19.1% |
| Oldest-first layers | +8.0% (unit ratio 55 / 48) | +8.7% to +10.0% | not usable |
| GW x price in backlog + services | +6.9% (13.6 GW x $465) | +21.7% (17.5 GW x $575) | +28% to +41% (20-21.5 GW x $741-815) |
| Guide against layers | about 3 points below | about 8 points above | |
| Guide against GW x price in backlog | about 2 points below | about 5 points below | |
| Outcome | +9.0% (+10% organic) | tracking +18.8% | |

Neither form calls a one-year guide. The two forms miss FY26 in opposite directions (-8 and +5 points). The rebuild's statement that the method cannot call the FY27 guide is confirmed. The FY27 range (16-21%) rests on the framework arithmetic and the pattern of two earlier guides, not on gigawatts.

### 3e. Outlook against the Street on the eve

| Event | Revenue gap | EBITDA gap | Pre-event Street? | Independent? |
|---|---|---|---|---|
| 2024-12-10 | -2.8% | -11.8% | No (Street dated 2025-01-10) | yes |
| 2025-12-09 | -0.6% | +12.3% | Yes (2025-12-05) | yes |
| 2026-01-28 | +3.4% | +6.8% | Yes (2026-01-23) | no (Prolec only) |

- Root mean square: revenue 2.6%; EBITDA 10.6% (three events), 12.0% (first two).
- The Street leads the company. On the eve of December 2025 the Street's 2028 revenue was already 16% above the old $45B framework. Today it is 8.9% (revenue) and 12.1% (EBITDA) above the current framework. FY2029 EBITDA consensus is up 24% from 2026-01-02 to 2026-09-25 (27% to the 2026-10-01 annual figure).

## 4. Corrected gap (2030 outlook against the Street)

| Basis | Revenue | EBITDA |
|---|---|---|
| Rebuild, as stated | +2.6% | +4.6% |
| Like-for-like Street basis (correction 1), no margin opinion (correction 2) | +1.3% | +2.2% |
| Same, with the aeroderivative strip (correction 4) | -0.3% to +0.3% | +0.4% to +1.1% |
| Same, k = 1.00 (mean realised three-year k) | -0.9% | about 0% |
| Range across the rebuild's low and high cases | -6.2% to +10.3% (BEst basis); -7.3% to +8.9% (like-for-like) | -8.2% to +21.5% |

What a pass would need (other lines held at the rebuild's centre, margin 25%):

| Target | 2030 EBITDA | Company revenue | Power equipment | k at $815 | or price in backlog at k 1.07 |
|---|---|---|---|---|---|
| +7% (the floor) | 20,913 | 83,650 | 28,128 | 1.15 | $873/kW |
| +12% to +13% (the band) | 21,890-22,085 | 87.6-88.3B | 32.0-32.8B | 1.31-1.34 | $994-1,019/kW |

A 7% gap needs k at the very top of the two back-tested values, or a year-end price in backlog above the top of the estimated range ($829). Clearing the band needs inputs outside every back-tested value.

## 5. Corrected error band

| Source | Size on 2030 EBITDA | Size on 2030 revenue |
|---|---|---|
| Equipment: k +/-15% (out-of-sample -15% / +17%; realised multi-year spread 0.12) | +/-5.4% | +/-4.9% |
| Margin +/-1.5 points (the rebuild's 24% to 27%) | +/-6.3% | n/a |
| Electrification +/-2.0B (the rebuild's 26-30B) | +/-2.6% | +/-2.5% |
| Services +/-1.25B (19.5-22.0B) | +/-1.7% | +/-1.6% |
| Wind +/-0.75B | +/-0.3% | +/-0.9% |
| Combined (root sum of squares) | **+/-8.9%** | **+/-5.8%** |
| Outlook against Street history (section 3e) | **+/-10.6% to +/-12.0%** | +/-2.6% |
| Half-width of the rebuild's own range | +/-15% | +/-8% |
| Spread of the 20 Street estimates (one standard deviation) | 11.0% | not in the pull |

Band used: about +/-12% on EBITDA, +/-6% to +/-8% on revenue. The corrected centre gap (+2.2% EBITDA, +1.3% revenue) is 0.2 of one standard deviation of the Street's estimates.

## 6. The six kill reasons, one by one

| # | Kill reason | Answered? | Check |
|---|---|---|---|
| 1 | Rival explanation (Street = management's plan at backlog prices) | **No. Conceded.** | Confirmed and extended by the recompute: Street 2028 equipment / 24 GW = $662 against $667 implied by the December 2025 framework. Street 2030 = 30 GW x $782 = 1.06 x today's price in backlog, 0.96 x the estimated year-end price. The Street sits inside the rule's own k range. No gap is left to explain |
| 2 | Gap sat in one order layer (Q2 2026, mix-lifted) | **In part.** | Timing of that layer no longer matters for a 2030 figure. Its price still does: it lifts the average from $651 to $741. The centre also rests on H2 2026 orders not yet booked (27-40% of year-end dollars). The mix strip (-3% to -5%) is sized but left out of the centre; applied, the revenue gap is about zero |
| 3 | Error band | **No. Conceded.** | Calibration is n = 2. Out-of-sample error on equipment is -15% / +17%. Realised k ranges 0.77 to 1.18. One-year guides are missed by -8 and +5 points. Band about +/-12% against a gap of +2.2% |
| 4 | Reveal date | **In part (form only).** | Two outlooks fall inside 12 months: the FY27 outlook on the late-January 2027 call, and a 2030 outlook at a capital markets day "in the spring", before the summer (date to be set in January; 16 September 2026 transcript, confirmed). Both are outlooks, not results. The FY27 Power guide gap is -1.4% (no call). The Street moves first: +16% above the old framework before December 2025; +12% in one week after it; +9% / +12% above the current one today |
| 5 | Thin Street data; a broker already publishes 30 GW at about $900/kW | **No.** | 2030 company figures have 20 estimates, but one standard deviation is 11% and low / high are -17% / +32%. Division inputs still come from 12 quarterly models, on a basis 1.25% above the annual mean. No 2030 or division history in the pull. The published broker figure (27.0B) is above the rebuild's equipment centre (26.3B) |
| 6 | Small profit effect | **No.** | +901 at the rebuild's centre (+4.6%, $44 a share at 13.0x). Like-for-like +434 (+2.2%, $21 a share). Range -1,596 to +4,191, both signs |

## 7. What can be used

| Use | Status after this check |
|---|---|
| Thesis | No |
| Supporting evidence for a direction | No (centre near zero, range has both signs) |
| Exhibit: the Street's Power equipment in physical terms (16.4 / 21.4 / 26.0 / 31.7 GW at $741; $608-565, $662-623, $741-688, $782 per kW on the stated output path) | **Yes.** Reproduces exactly from disclosed data. Needs a footnote: price in backlog is all-in (aeroderivatives, added plant scope, non-gas equipment) |
| Model structure: Power revenue = GW x price in backlog x k + services | Usable as a structure with wide ranges: k 0.8-1.0 one year out (mean 0.89); 0.77-1.18 at two to four years; outlook-implied 0.99 and 1.16 |
| Dated scorecard (2026-10-28; late January 2027; spring 2027) | Usable as a checklist. The Street must be pulled again on the eve, and compared on one basis (annual with annual) |

## 8. Sources and scripts

- Bloomberg, 2026-10-01: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `02-eeo-annual-2030.xlsx`, `01_eeo_annual.xlsx`, `06_modl.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (sheets Consensus, ConsensusHistory).
- `data/gev.db` (read-only): 10-Q / 10-K Power tables for accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148; release documents 291, 277, 268, 265, 226, 215; sources 1844, 2648, 3157, 3161, 2660, 3886, 681, 3750; table `prices`.
- gevernova.com (read 2026-10-01 with the Exa fetch tool): `gev_investor_update_pressrelease_12102024.pdf`, `gev_investor_update_presentation_12102024.pdf`, `gev_investor_update_transcript_12102024.pdf`, `gev_webcast_transcript_12092025.pdf`, `gev_webcast_presentation_01282026.pdf`, `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf`.
- Scripts (session scratchpad, folder `chk`): `chk1.py` (Street and company tables), `chk2.py` (back-tests A and B, out-of-sample k), `chk3.py` (forward ranges, like-for-like gap, exhibit), `chk4.py` (rule against reported results, every window), `chk5.py` (layer back-test, outlook against Street, band, pass thresholds).
- Not rechecked: the company-level FY27 guide figures taken from `propose_january-event.md`; the non-gas share of Power equipment RPO (not disclosed).
