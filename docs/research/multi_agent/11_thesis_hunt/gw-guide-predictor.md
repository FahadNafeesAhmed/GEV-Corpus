# Rebuild 3 of the gigawatts angle: predict what the company will say inside the horizon

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team (ranges and methods only). Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Id: `gw-guide-predictor`. Working date 2026-10-01. All money in $M unless stated.

Terms used:
- **Firm GW** = gas turbine gigawatts in backlog (an order is booked). **SRA** = slot reservation agreement (a paid reservation of a factory slot, not yet an order).
- **Price in backlog** = Power equipment RPO in dollars divided by firm GW. It is "all-in": the dollars include aeroderivatives, steam turbines, generators and non-gas equipment.
- **k** = the Power equipment revenue per kW that a company outlook implies for its target year, divided by the price in backlog on the date the outlook was given.
- **Street** = Bloomberg BEst mean.

## 0. Result

| Question | Answer |
|---|---|
| Does GW x price on the day reproduce the Power path management published? | For the two three-year outlooks, yes, within about 10%. Published Power revenue for 2028 was 1.08x (December 2024) and 1.11x (December 2025) the simple arithmetic. Expressed as k: 0.99 and 1.16 (section 3) |
| For one-year guides? | No. The first FY25 Power guide was about 3 points of growth below the arithmetic. The first FY26 guide was about 8 points above it (section 4) |
| How far was each outlook from the Street on the eve? | Revenue: -2.8%, -0.6%, +3.4%. EBITDA: -11.8%, +12.3%, +6.8%. The sign is not stable. Only two events are independent (section 5) |
| Same rule on today's book, 2030 | Power equipment $23.7B to $28.9B (centre $26.3B). Power $43.2B to $50.9B (centre $47.0B). Company revenue $74.8B to $87.9B (centre $81.8B). EBITDA $17.9B to $23.7B (centre $20.4B) (section 7) |
| Against the Street for 2030 | Revenue +2.6% (range -6.2% to +10.3%) against $79,724M. EBITDA +4.6% (range -8.2% to +21.5%) against $19,544M |
| FY27 Power growth guide (late January 2027) | 16% to 21%, centre about 17.5%. The Street has +19.1%. Centre is 1.4% below the Street's Power revenue |
| Restated 2028 Power revenue, if given | $31.3B to $40.5B, centre $34.8B. The Street has $33.5B (+3.9%, range -6.6% to +20.8%) |
| Error band from the back-tests | About +/-13% on the 2030 EBITDA figure; about +/-8% on revenue |
| Gap larger than the band? | **No** |
| Revealed inside 12 months? | Yes for the two events (late January 2027; spring 2027). But they are outlooks, and the Street moves before and after them |
| **holds** | **false** |

What the angle is good for is in section 10: an exhibit of the Street in physical terms, the driver structure for a Power model with back-tested ranges, and a dated scorecard for the two events.

## 1. Sources

| Key | Document | Where |
|---|---|---|
| BBG-Q | Quarterly consensus by division, Q3 2026 to Q2 2031 | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (keys such as `Total Revenue\|Power\|Equipment\|2030 Q4`). Bloomberg, 2026-10-01 |
| BBG-A | Annual consensus with counts | `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheet Consensus |
| BBG-H | Weekly consensus history from 2025-01-03 (FY2026 to FY2029 EBITDA; FY2027 and FY2028 revenue) | same workbook, sheet ConsensusHistory |
| BBG-M | Q3 2026 low / high by line; 2030 quarterly counts | `06_modl.xlsx`; `02-eeo-annual-2030.xlsx` |
| 10-Q / 10-K | Power tables: units and GW ordered and sold, equipment and services revenue, equipment RPO | `gev.db`, accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148 |
| REL | Earnings releases (firm GW and SRA counts each quarter) | `gev.db` documents 291, 277, 268, 265, 226, 215 |
| IU24 | Investor update 2024-12-10: deck, release, transcript | gevernova.com `gev_investor_update_presentation_12102024.pdf`, `gev_investor_update_pressrelease_12102024.pdf`, `gev_investor_update_transcript_12102024.pdf` (read 2026-10-01; not in the corpus) |
| IU25 | Investor update 2025-12-09: deck, release, transcript | corpus sources 1844, 2648; gevernova.com `gev_webcast_transcript_12092025.pdf` (read 2026-10-01) |
| D4Q25 | Q4 2025 deck, release, call (2026-01-28) | gevernova.com `gev_webcast_presentation_01282026.pdf` (read 2026-10-01); `gev.db` document 265; corpus source 2660 |
| C1Q26 | Q1 2026 call (2026-04-22) | gevernova.com `gev_webcast_transcript_04222026.pdf` |
| C2Q26 | Q2 2026 call and deck (2026-07-22) | corpus sources 3161, 3157 |
| LAG | Conference transcript 2026-09-16 | gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` |
| PX | Daily closes | `gev.db` table `prices` |

Web pages were read with the Exa fetch tool. The Firecrawl connector was not authorised in this session.
Every number was computed with Python (section 12). Earlier work read first: `propose_power-equipment-physical.md`, the three `verify_power-equipment-fy28-fy29_*.md` files, `propose_price-implied.md`, `propose_rpo-equipment.md`, `propose_power-services.md`, `propose_january-event.md`, and `09_finrobot_overnight/BLOOMBERG_VERDICT.md`, `S01_backlog_margin_conversion.md`.

## 2. Inputs

### 2a. Company data by quarter (10-Q / 10-K Power tables; equipment orders from decks D4Q25 p.18 and C2Q26 p.15)

| Quarter | GW ordered | GW sold | Equipment revenue | Equipment RPO, end | Firm GW, end | SRA GW, end | Price in backlog $/kW | Equipment orders | Order $/kW |
|---|---|---|---|---|---|---|---|---|---|
| Q3 2024 | 5.1 | 3.3 | 1,426 | 11,392 | 24.5 (rolled) | 9 (on 2024-12-10) | 465 | 1,840 (derived) | 361 |
| Q4 2024 | 6.1 | 4.8 | 1,796 | 12,461 | 25.8 (rolled) | n/a | 483 | 2,906 | 476 |
| Q1 2025 | 7.1 | 3.0 | 1,491 | 13,920 | 29 | 21 | 480 | 2,842 | 400 |
| Q2 2025 | 5.1 | 5.2 | 1,504 | 16,133 | 29 | 25 | 556 | 3,519 | 690 |
| Q3 2025 | 7.4 | 4.0 | 1,744 | 18,977 | 33 | 29 | 575 | 4,448 | 601 |
| Q4 2025 | 10.2 | 3.1 | 1,946 | 24,707 | 40 | 43 | 618 | 7,432 | 729 |
| Q1 2026 | 8.1 | 4.2 | 1,885 | 28,530 | 44 | 56 | 648 | 5,611 | 693 |
| Q2 2026 | 12.1 | 3.3 | 1,965 | 39,261 | 53 | 63 | 741 | 12,650 | 1,045 |

- "Rolled" = firm GW worked back from 53 GW with filed GW ordered and sold. It gives 29.9 / 29.8 / 33.2 / 40.3 / 44.2 against the disclosed 29 / 29 / 33 / 40 / 44.
- "Derived" orders = change in equipment RPO plus equipment revenue. Where a deck figure exists the derived figure is 0.4% to 5% higher (for example Q4 2025: 7,676 against 7,432).
- Period prices: nine months 2024 $395 (derived); FY24 $413 (8,340 / 20.2); nine months 2025 $551; FY25 $612 (18,241 / 29.8); Q4 2025 plus Q1 2026 $713; H1 2026 $909 (18,261 / 20.1).
- Power revenue: FY24 18,127 (equipment 5,708; services 12,419). FY25 19,767 (6,686; 13,081); recast base 19,873. H1 2026 10,449 (3,851; 6,598).
- FY26 on H1 actual plus Street H2: Power 23,609 (equipment 9,342; services 14,259), +18.8% on the recast base. The company guide is +18% to +20%.

### 2b. Street (Bloomberg, 2026-10-01)

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Power equipment (sum of quarters, BBG-Q) | 12,151 | 15,888 | 19,256 | 23,469 |
| Power services | 15,675 | 17,665 | 19,711 | 22,357 |
| Power revenue | 28,121 | 33,521 | 39,522 | 45,215 |
| Power EBITDA (margin) | 5,826 (20.7%) | 7,949 (23.7%) | 10,087 (25.5%) | 12,101 (26.8%) |
| Electrification revenue / Wind revenue | 17,704 / 7,589 | 21,270 / 6,813 | 24,959 / 7,381 | 28,422 / 7,440 |
| Company revenue, annual BEst (BBG-A) | 53,029 | 60,985 | 70,851 | 79,724 |
| Company EBITDA, annual BEst (number of estimates) | 9,471 (36) | 12,553 (33) | 16,496 (21) | 19,544 (20) |
| EBITDA margin | 17.9% | 20.6% | 23.3% | 24.5% |
| Company revenue / EBITDA, sum of quarters | 53,097 / 9,391 | 61,421 / 12,880 | 71,549 / 16,231 | 80,718 / 19,471 |

- 2030 EBITDA: standard deviation 2,147 (11% of the mean); low 16,314 (-17%); high 25,769 (+32%).
- 2030 quarterly models: 12 brokers for revenue, 11 for EBITDA. The count on division lines is not shown.
- The pull holds no history for 2030 consensus and none for any division line.

## 3. Back-test A: the three-year outlooks

### 3a. The rule, as management stated it

| Date | What was said (paraphrased) | Source |
|---|---|---|
| 2024-12-10 | Gas shipments ramp to 20 GW in 2027 and stay there in 2028. At least 20 GW of orders a year. No price is assumed above the price at which orders were then being taken. The 9 GW of SRAs (for 2027 and 2028 slots, priced above current orders) were left out of the framework until permits and construction contracts were further along. Listed upside: price beyond recent order levels | IU24 deck p.9, transcript |
| 2025-12-09 | Deck assumption: pricing reflecting recent orders; deliveries reach 20 GW annualised in mid-2026 and about 24 GW in 2028; sold out through 2028. CEO: "our outlook is tied to the price in backlog today." SRAs sit at a higher price than backlog on average, and their conversion is upside. Listed upside: gas turbine pricing above current order levels | IU25 deck p.8-9, transcript |
| 2026-01-28 | Same Power assumptions. Prolec added to the company figure. SRAs are priced 10 to 20 points above backlog | D4Q25 p.11; call |
| 2026-09-16 | The CEO called the company's published markers conservative. A 2030 financial case, split into equipment and services, comes at the capital markets day. The 2030 services figure will make the 2035 marker ($22B) look low | LAG |

### 3b. Inputs on the day, the arithmetic, and what was published

| | December 2024 (target 2028) | December 2025 (target 2028) |
|---|---|---|
| Contracted GW | about 24.5 firm (9/30/24, rolled) + 9 SRA = about 34 | 33 firm + 29 SRA = 62 (9/30/25); 18 GW more signed in the quarter to date; about 80 expected at year-end |
| GW to ship up to the target year, on the plan then | 2025-28: about 14 + 17 + 20 + 20 = 71 | 2026-28: about 17.5 + 21 + 23 = 62 |
| Share of that volume under contract | 48% (firm only: 35%) | about 100% at 9/30/25; about 130% at year-end |
| Target-year output | 20 GW | about 24 GW |
| Price on the day, $/kW | backlog 465; orders 395 (nine months), 413 (FY24), 476 (Q4) | backlog 575 (9/30/25), 618 (12/31/25); orders 601 (Q3), 729 (Q4) |
| Published | Company $45B and 14%; Power margin 16%. No Power revenue figure | Power: high-teens organic growth a year from 2025. Company $52B and 20% |
| Power 2028 that this implies | $23.5B to $26.2B, mid $24.9B. Method: $45.0B + $0.45B eliminations - Wind $7.5-8.5B (onshore flat near $8B, offshore complete) - Electrification $11.8-13.4B (2025 at +17%, then 10% to 15% a year). Check: 16% x (24.9 + 12.6) + 10% x 8.0 - 0.4 = $6.4B against 14% x $45B = $6.3B | 19,767 x 1.17^3 to 1.19^3 = $31.7B to $33.3B, mid $32.5B ($30.8B to $32.5B on the 2025 base expected then) |
| Arithmetic: GW x price x 0.90 + services | 20 x 413 x 0.90 = 7,434; services 12,419 x 1.06^4 = 15,679; total **$23.1B** (range $21.4B to $25.7B for price 395-476, conversion 0.80-0.99, services 5-7%) | 24 x 596 x 0.90 = 12,874; services 13,081 x 1.08^3 = 16,478; total **$29.4B** (range $25.7B to $34.7B for 22-24 GW, price 575-729, conversion 0.80-0.99, services 6-10%) |
| Published / arithmetic | **1.08** | **1.11** |
| Equipment revenue per kW implied by the published figure | (24,873 - 15,679) / 20 = $460 ($430 to $489 for services 7% to 5%) | (32,478 - 16,478) / 24 = $667 ($628 to $704 for services 10% to 6%) |
| **k** = implied $/kW / price in backlog | 460 / 465 = **0.99** (0.92 to 1.05; 0.78 to 1.19 across the full range of the residual) | 667 / 575 = **1.16** (1.09 to 1.22; 0.97 to 1.28 across the base and growth range) |

- 0.90 is the mean conversion ratio from the earlier back-test (range 0.80 to 0.99).
- Cross-check for 2024: an analyst at the event put gas equipment revenue for the period near $6.5B. With about $1.2-1.6B of non-gas equipment that is $7.7-8.1B, between the arithmetic ($7.4B) and the residual ($9.2B).
- January 2026 is not a third test. Power was unchanged; only Prolec was added ($52B + about $4B = $56B at the same 20%).
- The Street today sits on the December 2025 rule: Street 2028 Power equipment 15,888 / 24 GW = $662/kW, against $667/kW implied by the framework. As a multiple of the 12/31/25 price in backlog ($618) that is 1.07.

Reading: both times the published Power figure was 8% to 11% above "GW x price x 0.90 + services". On the price in backlog, k was 0.99 and 1.16 (mean 1.07). Sample size is two. Each k carries a range of about +/-0.2 from the inputs that are not disclosed (services growth; the Power residual in 2024).

## 4. Back-test B: the first one-year Power guides

| | FY25 guide (given 2024-12-10) | FY26 guide (given 2025-12-09) |
|---|---|---|
| First guide, Power organic growth | mid-single digit | 16% to 18% |
| Volume plan on the day | about 55 heavy-duty units, one more year at the old rate (48 shipped in 2024) (IU24 transcript) | 17 to 19 GW (high-teens, Q4 2025 call) against 15.3 in 2025 |
| Arithmetic | equipment 5,708 x 55/48 = 6,540; services 12,419 x 1.05 = 13,040; Power 19,580 = **+8.0%** | first-in-first-out layers of the 12/31/25 backlog for 17.5 GW = 7,624 (7,260 to 8,717 for 17 to 19 GW); services +6% to +8%; Power **+8.7% to +10.0%** (+6.9% to +15.5% across 17 to 19 GW) |
| Guide against arithmetic | about 3 points below | about 8 points above |
| What happened | raised to 6-7%; actual +9.0% reported, +10% organic; equipment 6,686 | held in January and April 2026; raised to 18-20% in July 2026; tracking 23,609 (+18.8%); equipment 9,342 |
| Equipment revenue per kW sold | 2024 $480; 2025 $437 | 2026 tracking $534 (9,342 / 17.5 GW); the layers gave $436 |

Reading: the sign flips. In 2026 equipment revenue is running about 23% ahead of the oldest-first layers at 17.5 GW (7% to 29% for 19 to 17 GW). Likely causes: aeroderivative units, revenue recognised over time ahead of shipment, non-gas equipment. The same gap shows in H2 2026: layers $4.5-4.8B, Street and guide $5.49B. **GW x layer price does not predict a one-year guide.** For FY27 the same layers give $14.0-15.5B of equipment, and the back-tested ratios (0.75 to 1.27) turn that into $10.5-19.6B against a Street of $12.2B. That band is not usable.

## 5. Back-test C: each outlook against consensus on the eve (BBG-H)

| Event | Outlook for 2028 | Street FY2028 before (date) | Revenue gap | EBITDA gap | Margin: outlook / Street | Next-day close | Street one week later |
|---|---|---|---|---|---|---|---|
| 2024-12-10 | $45,000M; 14%; $6,300M | 46,307 / 7,140 (2025-01-10, the first value in the pull, one month after the event) | -2.8% | -11.8% | 14.0% / 15.4% | +5.0% (327.39 to 343.80) | not in the pull |
| 2025-12-09 | $52,000M; 20%; $10,400M | 52,294 / 9,264 (2025-12-05) | -0.6% | +12.3% | 20.0% / 17.7% | +15.6% (625.30 to 723.00) | 54,136 / 10,385 (2025-12-12): EBITDA equal to the outlook, revenue 4.1% above it |
| 2026-01-28 (adds Prolec) | $56,000M; 20%; $11,200M | 54,174 / 10,486 (2026-01-23) | +3.4% | +6.8% | 20.0% / 19.4% | +2.7% (692.70 to 711.59) | 56,157 / 11,120 (2026-01-30) |
| Today | $56,000M; $11,200M (unchanged) | 60,985 / 12,553 (2026-10-01) | Street is 8.9% above | Street is 12.1% above | 20.0% / 20.6% | | |

First annual guides: FY26 guide midpoint $4,980M against a Street of $5,249M on 2025-12-05 (-5.1%); with Prolec $5,340M against $5,396M on 2026-01-23 (-1.0%). The Street for FY26 is now $6,334M, 18.6% above that midpoint.

Reading:
- Outlook revenue has been within -3% to +3% of the Street each time.
- Outlook EBITDA was 12% below, then 12% above, then 7% above. The December 2024 comparison uses a Street figure taken after the event, so it is weak. Independent events: two.
- After the December 2025 outlook the Street's 2028 EBITDA rose 12% in one week to the outlook itself, and revenue went above it. Ten months later the Street is 9% (revenue) and 12% (EBITDA) above the framework. The Street does not wait for the company.

## 6. Today's book

| Item | Value | Source |
|---|---|---|
| Contracted | 53 firm + 63 SRA = 116 GW at 6/30/26; at least 125 GW at year-end; H2 commitments of about 20 GW called likely conservative | REL Q2 2026; LAG |
| Output path | 5 GW a quarter from Q3 2026; 6 GW a quarter some time in H2 2027; 6 then 7 GW a quarter during 2028; 24 GW annualised in 2028; 30 GW in 2030 | C2Q26; LAG |
| GW to ship 2027 to 2030 on that path | 21-22 + 24-25.5 + 26-28 + 30 = 101 to 105.5 GW | computed |
| Share under contract at year-end 2026 | 125 / 105.5 = 118% or more. Mostly sold out through 2030; more than half of 2031 | computed; C2Q26 |
| Extra supply | 12 GW added over the summer for 2030 and 2031, all in contracting at premium prices | LAG |
| Price in backlog, 6/30/26 | 39,261 / 53 = $741/kW | 10-Q |
| H2 2026 order price guide | higher end of +10 to +20 points on Q4 2025 ($729 deck, $753 derived): $838 to $904/kW | C2Q26 |
| Price in backlog at 12/31/26 (estimate) | (39,261 + H2 order GW x price - Street H2 equipment revenue 5,491) / (53 + H2 order GW - 10). For 15 to 25 GW at $838 to $904: **$799 to $829/kW** | computed |
| Backlog margin | Power equipment margin in backlog +11 points in 2025; the 2026 change expected to be larger; management ties it to 2029-30 deliveries | D4Q25 p.5; LAG |

The year-end price in backlog is itself a company-reported number (10-K, late January or early February 2027): Power equipment RPO and firm GW.

## 7. The same rule on today's book

Formula: Power revenue in year T = output GW x price in backlog at the date of the outlook x k + services. k from section 3: 0.99 (low), 1.07 (centre), 1.16 (high).

### 7a. 2030 (the spring 2027 outlook)

| Line | Low | Centre | High | Street | Centre vs Street (range) |
|---|---|---|---|---|---|
| Power equipment | 30 x 800 x 0.99 = 23,726 | 30 x 815 x 1.07 = 26,259 | 30 x 830 x 1.16 = 28,869 | 23,469 | +11.9% (+1.1% to +23.0%) |
| Power services | 19,500 | 20,750 | 22,000 | 22,357 | -7.2% (-12.8% to -1.6%) |
| Power revenue | 43,226 | 47,009 | 50,869 | 45,215 | +4.0% (-4.4% to +12.5%) |
| Electrification | 26,000 | 28,422 (Street) | 30,000 | 28,422 | |
| Wind | 6,000 | 6,800 | 7,500 | 7,440 | |
| Eliminations | -450 | -450 | -450 | | |
| **Company revenue** | **74,776** | **81,781** | **87,919** | **79,724** | **+2.6% (-6.2% to +10.3%)** |
| EBITDA, method 1: Street margin 24.5% | 18,332 | 20,049 | 21,553 | 19,544 | +2.6% (-6.2% to +10.3%) |
| EBITDA, method 2: margin 24% / 25% / 27% | 17,946 | 20,445 | 23,738 | 19,544 | +4.6% (-8.2% to +21.5%) |
| EBITDA, method 3: bridge | 18,661 | 21,527 | 24,741 | 19,544 | +10.1% (-4.5% to +26.6%) |

Where each input comes from:
- Services. Company chart (IU25 p.28): gas and steam services about $12B in 2025 to at least $22B in 2035. A straight line or a constant 6.25% a year gives $16.3-17.0B in 2030, plus nuclear and hydro services of $1.6-2.2B: $17.8-19.2B. The CEO has since called the chart conservative and said the 2030 figure will make the 2035 marker look low. Services grew 5% a year in FY22-FY25 and track +8% in FY26. From 14,259 in FY26: 8% a year gives 19,399 in 2030, 10% gives 20,876, and the Street's 22,357 needs 11.9%. Range used: 19,500 to 22,000.
- Electrification and Wind are not rebuilt here. The centre uses the Street. The range is the framework path (Electrification: high-teens organic growth to 2029 from 9,642, plus Prolec) to the pace of 2026 guide raises.
- Method 2 margins: the framework has 20% in 2028; the Street has 20.6% (2028), 23.3% (2029), 24.5% (2030).
- Method 3: Power EBITDA = equipment x 30% / 35% / 40% + services x 22% / 24.5% / 27%; Electrification, Wind and corporate at the Street (7,229 / 531 / -507). Basis: FY25 Power EBITDA 2,902 on services of 13,081 is 22% if equipment earned about nothing (the CEO said in December 2025 that nearly all Power profit was in gas and steam services). Equipment margin in backlog rose 11 points in 2025 and is expected to rise more in 2026. The 30-40% is an assumption, not a disclosed figure. Power EBITDA on this method: 11,408 / 14,274 / 17,488 against the Street's 12,101.
- Morgan Stanley's published 2030 figure (note of 2026-07-23, corpus source 3886): 30 GW x about $900/kW = $27.0B. That is 15% above the Bloomberg mean for the line and 3% above the centre here.

### 7b. FY27 Power growth guide (late January 2027)

| Method | Result |
|---|---|
| Framework: high-teens a year from 2025. After +18.8% in 2026, the growth left for 2027-28 | 16.1% / 17.6% / 19.1% a year for a 17% / 18% / 19% three-year rate |
| Pattern of first guides | FY25: below the arithmetic and below the outcome by 4-5 points. FY26: 16-18%, later raised by 2 points |
| Layers (section 4) | +18% to +25% at ratios of 0.90 to 1.0; not usable (ratio range 0.75 to 1.27) |
| Range for the guide midpoint | 16% to 21%; centre about 17.5% |
| In dollars on FY26 of 23,609 | 27,386 to 28,566; centre 27,740 |
| Street | 28,121 (+19.1%). One Bloomberg contributor carries exactly 18.0% organic growth for every 2027 and 2028 quarter |
| Gap | -1.4% (range -2.6% to +1.6%) |

Company level, from `propose_january-event.md`: revenue guide $52.5-53.0B against $53,029M; EBITDA midpoint $8,925M (16-18% margin) or $9,450M (17-19%) against $9,471M.

### 7c. 2028, if the framework is restated

| Case | GW | Price $/kW | k | Equipment | Services (FY26 x growth^2) | Power | vs Street 33,521 |
|---|---|---|---|---|---|---|---|
| Low: management's timing, old conversion | 24 | 693 (Q1 2026 orders) | 0.90 | 14,969 | 16,325 (7%) | 31,293 | -6.6% |
| Centre | 24.75 | 723 (Q4 2025 to Q1 2026 orders) | 1.00 | 17,894 | 16,941 (9%) | 34,835 | +3.9% |
| High: oldest-first layers | 25.5 | 895 | 1.00 | 22,822 | 17,663 (11.3%) | 40,486 | +20.8% |

Company 2028 on the same cases: $56.5B / $62.5B / $68.5B against $60,985M (-7.3% / +2.4% / +12.4%). The framework says $56B.
The range is as wide as the three checkers found. The delivery year of each order is not disclosed, and nothing in this rebuild narrows it. It is also not certain that 2028 will be restated; the CEO named a 2030 outlook.

## 8. The Street in physical terms (exhibit)

| Year | Street Power equipment | Plan GW (July / September path) | Street $/kW at plan GW | k on today's price in backlog ($741) | GW the Street buys at $741 |
|---|---|---|---|---|---|
| 2027 | 12,151 | 20 / 21.5 | 608 / 565 | 0.82 / 0.76 | 16.4 |
| 2028 | 15,888 | 24 / 25.5 | 662 / 623 | 0.89 / 0.84 | 21.4 |
| 2029 | 19,256 | 26 / 28 | 741 / 688 | 1.00 / 0.93 | 26.0 |
| 2030 | 23,469 | 30 | 782 | 1.06 | 31.7 |

- Street 2030 equals 30 GW at today's price in backlog x 1.06. It equals 30 GW at the estimated year-end price ($815) x 0.96.
- So the Street's 2030 line is the company's own rule applied to today's backlog. The centre in section 7a is higher only because (i) the price in backlog will be about 8% to 12% higher at year-end as $838-904/kW orders are booked and cheaper layers ship, and (ii) k is taken at 1.07, not 1.0.

## 9. The six kill reasons

| # | Kill reason | How this rebuild deals with it |
|---|---|---|
| 1 | Rival explanation: Street 2028 = 24 GW x $735 x 0.90 | Confirmed, not removed. Street 2028 equipment ($662/kW at 24 GW) equals the equipment implied by the December 2025 framework ($667/kW). Street 2030 equals 30 GW x the price in backlog (k = 1.06 on $741). The Street is built on management's rule. This rebuild therefore does not claim the Street is wrong. It asks whether the next company outlook will sit above it. The centre says by 3% to 5%; the range crosses zero |
| 2 | The gap sat in the Q2 2026 layer (aeroderivative mix, added scope) | The 2030 arithmetic uses the average price of the whole year-end backlog, so it does not depend on which year the Q2 2026 layer ships. The mix problem remains in a smaller form: removing 61 aeroderivative units ($3.4-4.2B, about 2.2 GW) cuts the year-end price in backlog from $802-815 to $762-790/kW (-3% to -5%), and equipment by the same share. H2 2026 conversions, guided on a like-for-like basis, enter at $838-904 |
| 3 | Error band of the layer method (-27% to +25%) | This rebuild's own back-tests. Three-year outlooks: published / arithmetic 1.08 and 1.11; k 0.99 and 1.16 (n = 2; each +/-0.2 on undisclosed inputs). One-year guides: 3 points below and 8 points above. Outlook against Street: EBITDA -12% and +12%. Band on the 2030 EBITDA figure about +/-13%; on revenue about +/-8%. The gap (+4.6%; +2.6%) is inside both |
| 4 | Reveal date outside 12 months | Fixed in form only. The FY27 outlook comes on the late-January 2027 call; the 2030 outlook at a capital markets day in spring 2027 (date to be set on the January call). Both are inside 12 months. They are outlooks, not results. The comparison is with a moving Street: it rose 12% in the week after the last outlook, and FY2029 EBITDA consensus is up 27% this year |
| 5 | Thin Street data; Morgan Stanley already at 30 GW x $900 | Partly fixed. The claim is moved to company revenue and EBITDA for 2030 (20 annual estimates; 11-12 quarterly models). But the spread there is 11% (one standard deviation), so a +4.6% gap is 0.4 of one standard deviation. The centre for Power equipment ($26.3B) is below the published Morgan Stanley figure ($27.0B). There is no 2030 consensus history in the pull |
| 6 | Small profit effect | 2030 EBITDA: +$0.9B at the centre (-$1.6B to +$4.2B). At today's EV / 2030 EBITDA of 13.0x that is +$44 a share (+4.5%), range -$78 to +$205. The centre is small; the range is not, but it has both signs |

## 10. Verdict and what the angle is good for

| Test | Result |
|---|---|
| Gap | 2030 outlook against the Street: revenue +2.6%, EBITDA +4.6% (centres) |
| Error band | about +/-8% on revenue; about +/-13% on EBITDA |
| Gap larger than the band | No |
| Company number inside 12 months | Yes, two outlooks. Neither is a reported result |
| **holds** | **false** |

Uses that do survive:
1. **Exhibit: what consensus assumes in physical terms** (section 8). The Street's Power equipment path is 16 / 21 / 26 / 32 GW at today's backlog price, or the stated output path at $565-608, $623-662, $688-741 and $782/kW. It shows the Street is on the company's plan, with no ramp failure and no price above backlog.
2. **Driver structure for the model.** Power revenue = GW x price in backlog x k + services. Inputs with back-tested ranges: k 0.99 to 1.16 for a three-year outlook; conversion 0.80 to 0.99 over a backlog cycle; services growth 5% (FY22-25) to 8% (FY26); price in backlog $741 now, $799-829 at year-end.
3. **A check on any 2030 number.** Company revenue of $75-88B and EBITDA of $18-24B is what the company's own rule supports. A model outside that range needs a stated reason.
4. **Composition.** On the rule, a 2030 outlook would show more equipment and less services than the Street (equipment +1% to +23%; services -13% to -2%). That matters for what a 2030 multiple is applied to; it is not a gap in total revenue.
5. **The bar for the spring event.** The Street is already 8.9% (revenue) and 12.1% (EBITDA) above the 2028 framework. The December 2025 outlook was 12% above the Street's EBITDA and the stock rose 15.6%. An outlook equal to the Street is the base case on this arithmetic.
6. **Scorecard** (section 11).

## 11. Dates and pass marks

Street figures are as of 2026-10-01 and must be pulled again on the eve of each event.

| Date | Company number | Street today | Rule range | Mark |
|---|---|---|---|---|
| 2026-10-28 (Q3 10-Q) | Power equipment RPO / firm GW | n/a | 6/30: $741. On the path: $778-795 at 9/30 (8 to 12 GW of orders at $838-904, 5 GW shipped, Street Q3 equipment revenue 2,394) | $775 or more keeps the year-end range of $799-829; under $760 does not |
| Late January 2027 (Q4 call) | FY27 Power organic growth guide | +19.1% ($28,121M) | 16% to 21% | midpoint of 20% or more is above the Street; 16-18% is 1.8% below it |
| same | 2027 gas output | n/a | 21 to 22 GW | 21 GW or more |
| same (10-K) | Power equipment RPO / firm GW at 12/31/26 | n/a | $799-829/kW | $800 or more supports the 2030 centre; under $780 puts 2030 equipment at or below the Street |
| same | 2026 change in Power equipment margin in backlog | n/a | more than 11 points (management) | size sets the equipment margin for method 3 |
| Spring 2027 (capital markets day) | 2030 revenue | $79,724M | $74.8B to $87.9B | $84B or more is 5% above today's Street |
| same | 2030 EBITDA (revenue x margin) | $19,544M; 24.5% | $17.9B to $23.7B | $20.5B or more is 5% above; $22.1B or more is beyond the +/-13% band |
| same | 2030 Power equipment / services | 23,469 / 22,357 | 23.7-28.9B / 19.5-22.0B | split is promised by the CEO |
| same | 2028, if restated | 60,985; 20.6%; 12,553 | $56.5B to $68.5B | $61B and 21% equal the Street |

## 12. Limits

1. Two independent outlooks. No statistical weight.
2. The December 2024 Power figure is a residual (company total less Wind and Electrification assumptions). Its range moves k from 0.78 to 1.19.
3. No pre-event Street for December 2024 and no division-level or 2030 consensus history.
4. The price in backlog is all-in. Mix (aeroderivatives, combined-cycle scope, non-gas equipment) moves it without any change in like-for-like price.
5. Revenue on customised equipment is recognised over time, ahead of shipment. GW x price is an approximation; in 2026 revenue ran about 20% ahead of the layers.
6. Electrification and Wind are held at the Street in the centre case, so the company-level gap is the Power gap only.
7. Method 3 margins are assumptions.
8. A new CFO starts 2027-01-01 (8-K 0001996810-26-000153). The January guide will be the first under that CFO.
9. Management could set the 2030 output above 30 GW (the CEO said the steps can move earlier if execution is at its best). That would raise the figure; it is not in the range.

## 13. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
yr = lambda stem, y: sum(d[f'{stem}|{y} Q{q}'] for q in range(1, 5))
EQ, SV, PW = 'Total Revenue|Power|Equipment', 'Total Revenue|Power|Services', 'Total Revenue||Power'
BEST30 = (79723.7, 19544.4)                       # workbook sheet Consensus: 2030 revenue, EBITDA
# back-test 1: December 2024 outlook ($45B; Power margin 16%; 20 GW in 2028)
elec = [7550 * 1.17 * (1 + g) ** 3 for g in (0.10, 0.125, 0.15)]; wind = [7500, 8000, 8500]
fw24 = [45000 + 450 - wind[2 - i] - elec[2 - i] for i in range(3)]          # Power 2028 as a residual
sv24 = [12419 * (1 + g) ** 4 for g in (0.05, 0.06, 0.07)]
print(fw24[1] / (20 * 413 * 0.90 + sv24[1]))                                # 1.08
k24 = (fw24[1] - sv24[1]) / 20 / 465                                        # 0.99 ($465 = RPO per firm GW, 9/30/24)
# back-test 2: December 2025 outlook (Power high-teens from 19,767; 24 GW in 2028)
fw25 = 19767 * 1.18 ** 3; sv25 = 13081 * 1.08 ** 3
print(fw25 / (24 * 596 * 0.90 + sv25))                                      # 1.11
k25 = (fw25 - sv25) / 24 / 575                                              # 1.16 ($575 = RPO per firm GW, 9/30/25)
k = (k24 + k25) / 2                                                         # 1.07
# year-end 2026 price in backlog
h2 = d[EQ + '|2026 Q3'] + d[EQ + '|2026 Q4']
ye = [(39261 + g * p - h2) / (53 + g - 10) for g in (15, 20, 25) for p in (729 * 1.15, 753 * 1.20)]   # 799..829
# 2030 on the rule
eq = [30 * 800 * k24, 30 * 815 * k, 30 * 830 * k25]; sv = [19500, 20750, 22000]
el = [26000, yr('Total Revenue||Electrification', 2030), 30000]; wi = [6000, 6800, 7500]
co = [eq[i] + sv[i] + el[i] + wi[i] - 450 for i in range(3)]
print([round(x) for x in co], [round(x / BEST30[0] - 1, 3) for x in co])    # 74,776 / 81,781 / 87,919
eb = [co[0] * .24, co[1] * .25, co[2] * .27]
print([round(x) for x in eb], [round(x / BEST30[1] - 1, 3) for x in eb])    # 17,946 / 20,445 / 23,738
# FY27 guide and Street in physical terms
fy26 = 10449 + d[PW + '|2026 Q3'] + d[PW + '|2026 Q4']                      # 23,609
print(yr(PW, 2027) / fy26 - 1, [fy26 * (1 + g) / yr(PW, 2027) - 1 for g in (.16, .175, .21)])
print({y: round(yr(EQ, y) / 741, 1) for y in (2027, 2028, 2029, 2030)})                   # GW at $741: 16.4 / 21.4 / 26.0 / 31.7
```

Consensus on the eve of each outlook: workbook sheet `ConsensusHistory`, rows dated 2025-01-10, 2025-12-05, 2025-12-12, 2026-01-23, 2026-01-30. Prices: `gev.db` table `prices`. The layer stack used in section 4 is the one in `verify_power-equipment-fy28-fy29_wedge-tests.md`, section 9.
