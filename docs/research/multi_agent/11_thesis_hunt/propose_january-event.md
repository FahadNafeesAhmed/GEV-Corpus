# Lens: the next two reports as a number (Q3'26 on 28 Oct 2026; Q4'26 + first 2027 outlook, late Jan 2027)

_Research input only: facts, arithmetic, tables, sources. No memo sentences, no forecast choices (ranges and methods only). Bloomberg data: "Bloomberg, 2026-10-01", academic licence, keep inside the project folder._

## 0. Sources used

| Key | File / document | What was read |
|---|---|---|
| BBG-Q | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (keys `Block|Parent|Line|YYYY Qn`), same data as `01..05-eeo-company-specific.xlsx` | Quarterly consensus by division, Q3'26-Q4'27 |
| BBG-M | `data/bloomberg/GEV_Pull_2026-10-01/06_modl.xlsx` (Period 2026:Q3; mean / low / high / median) | Q3'26 distribution per line |
| BBG-F | `data/bloomberg/GEV_Pull_2026-10-01/01_eeo_annual.xlsx` | Quarterly FCF consensus with broker counts (15 / 15 / 13 / 12) |
| BBG-A | `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheets Consensus, ConsensusHistory | Annual BEst; weekly history |
| R-xQyy | Earnings releases in `gev.db` documents (8-K EX-99): 0001996810-25-000072 / -000132 / -000159, -26-000012 / -000063 / -000147 | Segment orders, revenue, EBITDA, guidance text |
| 10-Q / 10-K | `gev.db` documents: 10-Q 0001996810-26-000148 (Q2'26), -26-000064, -25-000160, -25-000133, -25-000073; 10-K -26-000015, -25-000011 | RPO schedule note, unit tables (gas, wind), tax note |
| CALL-2Q26 | `gev.db` sources id 3161 (company transcript PDF, 2026-07-22) | Q3 and FY guide wording |
| CALL-1Q26 | gevernova.com `gev_webcast_transcript_04222026.pdf` (read 2026-10-01) | Q2 guide wording; data-centre orders in Q1 |
| CALL-4Q25 / 3Q25 | `gev.db` sources id 2660, 3796 | Q1'26 and Q4'25 guide wording; Wind miss explanation |
| CONF-0916 | gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` (read 2026-10-01) | CEO statements of 2026-09-16 |
| XBRL | `data/financials/gev_segments.csv`, `gev_quarterly.csv` | Equipment / services by segment, contract liabilities |
| MB | MarketBeat earnings page for GEV (read 2026-10-01) | Revenue consensus before each print (single vendor) |

Python was used for every number below (scratch scripts, not saved in the repo). The Firecrawl connector was not authorised in this session; Exa fetch was used for the two company PDFs.

## 1. The Street for the two reports (BBG-Q; $M)

| Line | Q3'26 | Q4'26 | Q1'27 | Q2'27 |
|---|---|---|---|---|
| Revenue | 11,993 | 13,915 | 11,143 | 12,968 |
| Equipment (sum of three divisions) | 7,482 | 8,339 | 6,675 | 7,748 |
| Services (sum) | 4,485 | 5,629 | 4,536 | 5,139 |
| Adj. EBITDA | 1,672 | 2,500 | 1,810 | 2,228 |
| Power revenue (equipment / services) | 5,776 (2,394 / 3,389) | 7,384 (3,097 / 4,272) | 6,061 | 6,885 |
| Power EBITDA (margin) | 1,047 (18.1%) | 1,508 (20.6%) | 1,144 | 1,433 |
| Electrification revenue | 3,881 | 4,289 | 3,671 | 4,304 |
| Electrification EBITDA (margin) | 745 (19.1%); "adjusted" row 681 | 917 (21.3%); 843 | 725 | 885 |
| Wind revenue | 2,341 | 2,344 | 1,522 | 1,866 |
| Wind EBITDA | +4 ("adjusted" row +25) | +208 (+183) | -8 | +15 |
| Corporate / other | -144 | -107 | -17 | -92 |
| Orders total (Power / Wind / Electrification) | 20,332 (12,213 / 1,510 / 6,498) | 25,071 (14,991 / 1,761 / 7,492) | 23,056 | 23,737 |
| FCF (brokers) | 1,502 (15) | 1,148 (15) | 729 (13) | 1,726 (12) |
| Wind deliveries MW | 1,648 | 1,633 | 694 | 1,188 |
| Diluted EPS | 4.04 | 5.61 | 4.49 | 5.67 |

Q3'26 spread (BBG-M): revenue 11,469-12,384; EBITDA 1,378-1,795 (median 1,694); Electrification orders 5,775-7,498 (median 6,307); Power orders 8,785-15,501; FCF -1,622 to 7,062; contract liabilities mean 37,492 / median 39,944 (Q2 actual 40,037); change in contract liabilities mean -1,402 / median -50.

Data flags (they affect anyone quoting these cells):
- RPO "mean" for Q3'26 (196,789) and Q4'26 (209,676) is distorted by one Wind RPO entry (Wind high 112,612 against a Q2 actual of 20,388). Median Q3 RPO is 185,946. Use the median.
- "Free Cash Flow 2026 Q2 (Rep)" = 9,897 is the half-year figure, not the quarter (quarter = 5,107).
- Electrification "organic growth" for Q1'27 = 84,484% is a broker entry error.
- Sum of quarterly FCF for H2'26 = 2,650; annual BEst FCF 12,196 less H1 9,897 = 2,299. Two different broker sets.

## 2. Management's own numbers for the two quarters

| Item | Guide | Source |
|---|---|---|
| Q3 Power | revenue +17% to +19%; margin "approximately 17% to 18%"; Q3 is the seasonally lowest services quarter | CALL-2Q26 |
| Q3 Electrification | revenue $3.8-4.0B; margin "modestly above 2Q 2026 levels" (18.4%) | CALL-2Q26 |
| Q3 Wind | revenue down low double digits; EBITDA "approximately break-even" | CALL-2Q26 |
| Q3 company | revenue growth, margin expansion, positive FCF (no numbers) | CALL-2Q26 |
| FY26 | revenue $45.5-46.5B; margin 12-14%; FCF $11.5-12.5B; Power +18-20% organic, 17-19%; Electrification $14.5-15.0B, 18-20%; Wind down low double digits, about -$400M; corporate -$450M to -$500M; highest revenue and EBITDA in Q4 | R-2Q26, CALL-2Q26 |
| Gas output | 5 GW per quarter in Q3 and Q4; "beginning of next year ... very similar" | CONF-0916 |
| Orders | "very strong third quarter orders"; $200B backlog "very early in 2027"; H2 gas commitments about 20 GW "likely ... conservative", Q4 larger than Q3 | CONF-0916 |
| Electrification orders | data-centre orders above $5B in H1 = "almost 40%" of segment orders; "probably more like 20%" in Q3 and Q4; India HVDC (almost $1.5B) books in Q4 | CONF-0916 |
| January call | FY26 actuals, 2026 change in equipment margin in backlog, 2027 outlook, date of the capital markets day (spring 2027) | CONF-0916 |

Quarterly guide versus actual, 2026 (releases and call transcripts):

| Quarter | Line | Guide | Actual | Result |
|---|---|---|---|---|
| Q1'26 | Power revenue growth | high single digit | +11.7% (4,971 vs 4,449 recast) | above |
| Q1'26 | Power margin | 14-15% | 16.3% | +1.3 pts above top |
| Q1'26 | Electrification revenue | "similar to Q4'25" (2,960) | 2,959 | in line |
| Q1'26 | Electrification margin | 16-17% | 17.8% | +0.8 above top |
| Q1'26 | Wind EBITDA | -300 to -400 | -382 | in range, weak end |
| Q2'26 | Power revenue growth | +15-17% | +14.5% | 0.5 below bottom |
| Q2'26 | Power margin | 17-18% | 18.8% | +0.8 above top |
| Q2'26 | Electrification revenue | 3.3-3.5B | 3,637 | +3.9% above top |
| Q2'26 | Electrification margin | modestly above 17.8% | 18.4% | met |
| Q2'26 | Wind EBITDA | -200 to -300 | -275 | in range, weak end |
| Q2'26 | Wind revenue | down mid-teens | -10% | better |

## 3. Rebuild of Q3'26 (reports 28 Oct 2026)

| Line | Street | Rebuild from guide (range) | Rebuild with 2026 beat pattern or seasonality | Gap vs Street |
|---|---|---|---|---|
| Power revenue | 5,776 | 4,862.9 x 1.17-1.19 = 5,690-5,787 | same | -1.5% to +0.2% |
| Power EBITDA | 1,047 (18.1%) | 17-18% = 967-1,042 | 18.8-19.3% (two-quarter pattern) = 1,070-1,117 | -8% to +7% |
| Electrification revenue | 3,881 | 3,800-4,000 | Q3/Q2 ratio 1.05 / 1.08 / 1.20 (2023-25) x 3,637 = 3,819-4,364 | -2% to +12%, centre +4% |
| Electrification EBITDA | 745 | 18.6-19.3% = 707-772 | 19.0% x 3,900-4,037 = 741-767 | -5% to +4% |
| Wind revenue | 2,341 | 2,647 x 0.87-0.90 = 2,303-2,382 | same | -1.6% to +1.8% |
| Wind EBITDA | +4 | about 0 | not rebuildable: Vineyard Wind settlement signed 2026-09-16, terms confidential (court records: GEV claimed $308-360M owed; the customer claimed $394-850M) | unknown sign |
| Corporate | -144 | FY -450 to -500 less H1 -239, split evenly = -106 to -131 | | |
| Revenue | 11,993 | 11,758-12,134 | 11,774-12,499 | -2% to +4% |
| Adj. EBITDA | 1,672 | 1,543-1,708 (mid 1,625) | 1,693-1,766 (mid 1,729) | -8% to +6%; centres -2.8% (guide mid) and +3.4% (beat pattern) |
| EPS (GAAP diluted) | 4.04 | at Street EBITDA: 1,672 - D&A 420 (Q2 actual 418; Street mean 349-370, median 416) + interest 75 + non-operating benefit income 120 - restructuring and separation 55 = pre-tax 1,392 (Street 1,453); tax 24-30% (Q2'26 was 29.8%, 10-Q Note 16); 268.5M shares | 3.66-3.96 | -2% to -9% |
| Orders: Electrification | 6,498 | see section 5 | 4,500-5,900 (centre 5,160) | -9% to -31%, centre -21% |
| Orders: total | 20,332 | year-end RPO must be about 195-199B for "$200B very early in 2027": H2 orders 44.6-48.6B vs Street 45.4B | | -2% to +7% (H2) |
| Equipment revenue | 7,482 | guide-implied 7,250-7,690 | | -3% to +3% |
| FCF | 1,502 | "positive" | see section 8 | band too wide |

Result: no consolidated profit-and-loss line in the Q3 report differs from the Street by 5% with an error band narrower than the gap. The one line that does is Electrification orders.

## 4. Rebuild of Q4'26 (reports late January 2027)

| Line | Street | Guide-implied (FY guide less H1 actual less Q3) | Seasonality check | Gap vs Street |
|---|---|---|---|---|
| Power revenue | 7,384 | 19,873 x 1.18-1.20 - 10,449 - 5,738 = 7,263-7,661 | Q4/Q3 1.44 / 1.29 / 1.19 (2023-25); Street 1.28 | -1.6% to +3.8% |
| Power margin | 20.6% | FY 17-19%: Q4 mid 18.9% | Q4 minus Q3 margin +7.1 / +3.1 / +3.6 pts: 17.5% + 3.1 to 3.6 = 20.6-21.1% | in line |
| Electrification revenue | 4,289 | 14.5-15.0B - 6,597 - 3,900 = 4,003-4,503 | Q4/Q2 1.31 / 1.22 / 1.37; on organic base 2,737 plus Prolec about 930 = 4,270-4,680 | 0% to +9%, centre +5% |
| Electrification margin | 21.3% | FY 18-20% | Q4 minus Q3 +4.4 / +2.6 / +1.9 pts: 20.9-21.6% | in line |
| Wind revenue | 2,344 | 9,110 x 0.87-0.90 - 3,459 - 2,343 = 2,124-2,397 | | -9% to +2% |
| Wind EBITDA | +208 (+183) | -400 + 657 - Q3 (0) = +257 | best quarter since the spin +19 (Q4'24); see section 7 | band wider than gap |
| Adj. EBITDA | 2,500 | company guide mid (13% x 46.0B = 5,980) less 2,146 less 1,672 = 2,162; segment guide mids (Power 18%, Electrification 19%, Wind -400, corporate -475 = 6,185) give 2,367 | Street Power 1,508 + Electrification at 20.9-21.6% on 4,289-4,680 (896-1,011) + Wind +30 to +120 - 107 = 2,327-2,532 (centre about 2,430) | -7% to +1%, centre -3%; -5.3% at segment guide mids |
| Revenue | 13,915 | 45.5-46.5B less 20,442 less 11,993 = 13,065-14,065 | Power 7,384 + Electrification 4,270-4,680 + Wind 2,344 - 35 = 13,960-14,370 | +0.3% to +3.3% |
| FY26 EBITDA margin | 13.7% (6,334 / 46,240) | 12-14% | Street sits about 83-86% up the guide range | |

Seasonality ratios (XBRL segment revenue; Street from BBG-Q):

| Line | Q4/Q3 2023 / 24 / 25 | Street 2026 | Q4/Q2 2023 / 24 / 25 | Street 2026 |
|---|---|---|---|---|
| Power equipment | 1.54 / 1.21 / 1.12 | 1.29 | 1.73 / 1.29 / 1.28 | 1.58 |
| Power services | 1.38 / 1.32 / 1.23 | 1.26 | 1.21 / 1.17 / 1.16 | 1.22 |
| Electrification equipment | 1.31 / 1.09 / 1.12 | 1.05 | 1.38 / 1.24 / 1.37 | 1.12 |
| Electrification total | 1.25 / 1.13 / 1.14 | 1.11 | 1.31 / 1.22 / 1.37 | 1.18 |
| Wind services | 1.22 / 1.15 / 1.19 | 1.00 | 1.23 / 1.15 / 1.18 | 0.86 |
| Total equipment | 1.13 / 1.11 / 1.01 | 1.11 | 1.26 / 1.40 / 1.22 | 1.29 |
| Total services | 1.34 / 1.30 / 1.22 | 1.26 | 1.21 / 1.17 / 1.18 | 1.21 |

The only seasonal outliers are Electrification in H2 (Street below every prior year's Q4/Q2 ratio; part of the difference is Prolec, which is not seasonal) and Wind services (Street Q3 and Q4 at 545 against a Q2 actual of 631; total Wind revenue is pinned by the guide, so this is mix only).

## 5. Candidate 1: Electrification orders, Q3'26

| Step | Value | Source |
|---|---|---|
| H1'26 Electrification orders | 7,112 + 6,347 = 13,460 | R-1Q26, R-2Q26 |
| Data-centre orders in H1 | above $5B, "almost 40%" of segment orders: 5,000-5,380 (37-40%); Q1 alone about 2,400 | R-2Q26, CALL-1Q26, CONF-0916 |
| Non-data-centre orders in H1 | 13,460 - 5,000 to 5,380 = 8,080-8,460; 4,040-4,230 per quarter; Q2 alone 3,370-3,750 | computed |
| Data-centre share in Q3 | "probably more like 20%" (tested 15-25%) | CONF-0916 |
| Q3 orders = non-data-centre / (1 - share) | 4,130 / 0.80 = 5,160; low 3,600 / 0.80 = 4,500; high 4,700 / 0.80 = 5,875 | computed |
| Street | 6,498 (low 5,775, median 6,307, high 7,498) | BBG-Q, BBG-M |
| Gap | centre -20.6%; range -9.6% to -30.7%; the centre is below the lowest broker | |
| Q4 by the same method | (4,130 + 1,500 India HVDC) / 0.80 = 7,040 vs Street 7,492 (-6%); H2 12,200 vs 13,990 (-13%) | |

Cross-checks:
- The Street's Electrification RPO path (44,563 to 46,998) implies Q3 orders of 6,316, so the two consensus lines agree with each other.
- The CEO said Electrification backlog grows "in a very healthy way" in Q3 and Q4; 5,160 against revenue of about 3,900 satisfies that (book-to-bill 1.3, against 1.7 in Q2 and 2.4 in Q1).
- Year-ago: Q3'25 orders 5,110 (included $1.6B of Saudi synchronous condensers) with no Prolec; 5,160 including Prolec would be an organic decline.
- Implied data-centre orders about 1.0B in the quarter against about 2.6B per quarter in H1.

Price relevance, from the record: Electrification orders fell year on year in Q1'24 (-7%), Q2'24 (-4%), Q1'25 (-5%) and Q2'25 (-31%); report-day moves were +1.5%, -4.5% (blade failure), +3.1%, +14.6%. Total orders +71% (Q1'26) gave +13.75%; +88% (Q2'26) gave -8.69%. Orders have not driven the report-day move. Profit effect in the 3-12 month window: none.

## 6. The equipment-conversion gap: which report shows it

Inputs: 10-Q Q2'26 RPO note: equipment RPO 87,821, 36% within one year = 31,616 (35.5-36.5%: 31,176-32,055). Street equipment for Q3'26-Q2'27 = 30,245 (BBG-Q): 15,821 in H2'26, 14,424 in H1'27.

Test 1, is the gap in H2'26? 10-K 2025: equipment RPO 64,245, 37% within one year = 23,771 for FY26 (before Prolec). H1'26 equipment 11,713, of which Prolec about 1,380 (Q2 revenue "nearly $900M", two months in Q1); ex-Prolec 10,333.

| Method | FY26 ex-Prolec | H2'26 incl. Prolec (about 1,570) | vs Street 15,821 |
|---|---|---|---|
| schedule x 1.03 (ex-Prolec ratio of the two latest windows) | 24,484 | 15,721 | -0.6% |
| schedule x 1.06 | 25,197 | 16,434 | +3.9% |
| schedule x 1.105 (FY25 ratio) | 26,267 | 17,504 | +10.6% |
| H1 share of the year 42.5% (2023-25: 43.1 / 41.2 / 43.4%) | 24,313 | 15,550 | -1.7% |
| H1 share 41.2% | 25,080 | 16,317 | +3.1% |
| Q3 guide, equipment implied | | Q3 7,250-7,690 vs Street 7,482 | -3% to +3% |

H2'26 Street equipment is consistent with the FY26 schedule, with seasonality and with the Q3 guide (-2% to +4%). Precedent the other way: in 2025 the July guide ("higher end of $36-37B") implied H2 of at most 19.86B and H2 came in at 20.93B (+5.4%); in 2024 H2 landed at the top of the range (19.47B vs 19.54B).

Test 2, the residual: 31,616 - 15,821 = 15,795 scheduled for H1'27 against Street 14,424: +9.5% (15,355-16,233 with rounding: +6.5% to +12.5%), before any book-and-ship. On H1'27 total revenue (Street 24,111): +5.7% (+3.9% to +7.5%). At an equipment gross margin of 19-25% (Street Q3 product revenue 7,361 vs cost of equipment 5,952, BBG-M): +$260-340M on H1'27 EBITDA of 4,038 (+6% to +8%).

Diagnostic: realised / scheduled by number of Street quarters in the window (BLOOMBERG_VERDICT section 10, ex-Prolec): no Street quarters 1.105, 1.048, 1.061; one 1.033; two 1.028; three 1.004; four 0.957. The ratio falls as Street quarters replace reported ones.

Attack, by division (equipment revenue of the next four quarters as a share of opening equipment RPO):

| Division | Equipment RPO 6/30/26 | Street next 4Q | Street share | History | Next 4Q at history | vs Street |
|---|---|---|---|---|---|---|
| Electrification | 40,600 (R-2Q26) | 13,541 | 33.4% | 35.4% (6/30/25, ex-Prolec), about 35% (12/31/24), about 37% (9/30/24); opening RPO for the last two taken from "up $X year on year" statements | 14,400 at 35.5%; capacity view: prior 4Q organic 8,489 x 1.25-1.30 + Prolec 3,600 = 14,200-14,600 | +5% to +8% |
| Power | 39,261 (10-Q) | 10,874 | 27.7% | 45.7%, 53.7% (not comparable: slots are now sold into 2030 and beyond) | capacity: 20 GW vs 14.6 GW shipped in the prior 4Q (+37%) x 7,541 = 10,300-11,300 | in line |
| Wind | 8,197 (10-Q) | 5,830 | 71.1% | 64.9%, 67.4%, 63.3% | 5,160-5,490 at face value; but offshore run-off raises the blended rate, and trailing orders of 4.3 GW x 1.16-1.34 = 5.0-5.8 GW cover the Street's 5.16 GW | no robust gap |

Division build: Street plus about 0.7-1.1B (Electrification) = 30.9-31.3B, i.e. 0.98-0.99 of the schedule. The division view supports roughly 50-80% of the 1,371M gap and places it in Electrification. H1'27 seasonality by division (H1 / prior H2: Power 0.76 / 0.95 / 1.08; Electrification 0.99 / 1.02 / 0.99 ex-Prolec; Wind 0.62 / 0.62 / 0.57) is matched by the Street (0.98 / 1.00 / 0.64). So the schedule and normal seasonality cannot both hold with H2'26 at the guide: either H2'26 beats the guide by about $1.4B, or H1'27 runs above seasonal, or conversion falls below the schedule for the first time.

What the next two reports print on this:
- 28 Oct (10-Q the same day): Q3 equipment revenue against 7,482 (BBG-M product revenue 7,361); new schedule = equipment RPO at 9/30/26 x % within one year. Roll-forward estimate 31.1-32.1B for Q4'26-Q3'27 against Street 31,314 for that window; a print of 32.5B or more keeps the gap at 4% or more.
- Late Jan (the 10-K was filed one day after the release in 2026): 12/31/26 equipment RPO x % within one year = scheduled FY27 equipment revenue, against Street FY27 equipment of 32,382 (Power 12,150 + Electrification 14,869 + Wind 5,363). FY27 revenue guide against Street 53,029.
- Late Apr and late Jul 2027: Q1'27 and Q2'27 equipment revenue against 6,675 and 7,748.

## 7. Wind in Q4'26: the Street's own numbers do not agree with each other

| Fact | Value | Source |
|---|---|---|
| Street Q4'26 Wind EBITDA | +208 (EBITDA row), +183 (adjusted row); margin 8.8% on 2,344 | BBG-Q |
| Street FY27 Wind EBITDA, four quarters | -8, +15, +65, +115 = +188 on revenue 7,589 (2.5%) | BBG-Q |
| GEV 2028 Wind margin target | 6% | R-4Q25 |
| Best Wind quarter since the spin | +19 (Q4'24, revenue 3,109) | R-4Q24 |
| Guide-implied Q4 | -400 + 657 - 0 = +257 | R-2Q26, CALL-2Q26 |
| October guide vs outcome, FY24 | "nearly 50% improvement" on -1,033 (about -520 to -560) vs actual -588 | R-3Q24, R-4Q24 |
| October guide vs outcome, FY25 | about -400 (Q4 implied -28) vs actual -598 (Q4 -225; offshore stop-work order of 22 Dec 2025) | R-3Q25, CALL-4Q25 |
| Year-on-year bridge, H2'25 (-286) to H2'26 | +200 stop-work accrual not repeated; +70 to +140 tariffs passed through; -70 to -100 lower onshore volume (equipment 3,552 vs 4,032); +100 to +150 onshore services; 0 to +150 offshore costs; +50 price and mix = +34 to +334, centre about +200 | CALL-4Q25, CALL-1Q26, CALL-2Q26, 10-Q; component sizes are estimates |
| Quarter-on-quarter view from the Q3 guide (0) | services seasonal uplift (Q4/Q3 1.15-1.22) and lower offshore cost: +30 to +120 | estimate |

The Street has Wind earning more in Q4'26 alone (+208) than in all of 2027 (+188). Two readings, both revealed in the January report: (a) Q4'26 lands near the Street's 2027 run-rate (+30 to +120): FY26 Wind about -540 to -630 against the -400 guide, and Q4 EBITDA 3.5-7% below 2,500; (b) Q4'26 lands at +200 or more: the 2027 Wind consensus (+188) is then below one quarter's exit rate. The two methods give +30 to +250 for Q4, so the band is wider than the gap and no single number is offered. Report-day record for Wind misses: -4.5% (Q2'24), +1.3% (Q3'24), -1.6% (Q3'25), +2.7% (Q4'25).

## 8. Free cash flow: guide record and deposit arithmetic

Remaining-period FCF implied by the guide versus what happened:

| Guide date | FY guide | Year-to-date then | Implied remainder | Actual remainder | vs top of implied |
|---|---|---|---|---|---|
| Jul 2024 | 1.3-1.7B | H1 0.16B | H2 1.14-1.54B | 1.54B | at top |
| Oct 2024 | "higher end" of 1.3-1.7B | 9M 1.13B | Q4 up to 0.57B | 0.57B | at top |
| Jul 2025 | 3.0-3.5B | H1 1.17B | H2 1.83-2.33B | 2.54B | +9% |
| Oct 2025 | 3.0-3.5B | 9M 1.90B | Q4 1.10-1.60B | 1.81B | +13% |
| Apr 2026 | 6.5-7.5B | Q1 4.79B | Q2-Q4 1.71-2.71B | Q2 alone 5.11B | above |
| Jul 2026 | 11.5-12.5B | H1 9.90B | H2 1.60-2.60B | Street 2.30B (annual) / 2.65B (quarters) | open |

Deposit arithmetic: Power-segment contract liabilities rose 3,902 / 3,853 / 7,285 in Q4'25 / Q1'26 / Q2'26 on 24 / 21 / 20 GW of new gas commitments: $163M / $183M / $364M per GW (three-quarter average $231M per GW; the CEO said a slot reservation carries "like, 25% down"). Total contract liabilities have risen in every quarter since the spin (smallest rise +379M). H2'26 commitments of 20-26 GW (CEO: 20 GW "likely ... conservative") at $163-364M per GW, less higher liquidation at 5 GW per quarter, plus Electrification and Wind: change in contract liabilities +2.8B to +7.9B (centre +4.9B). FCF H2 = EBITDA 4.17B - capex 0.92B - cash tax about 1.1B + interest and other 0.05B + change in contract liabilities - other working capital 2.5-3.5B (H1'26: -3.4B; FY25: -5.4B) = 1.5-7.5B, centre about 4.1B, against the Street's 2.3-2.65B. The centre is 55-80% above the Street but the low end is below it: band wider than the gap. Report-day record: the largest FCF raise (+$5B at the midpoint, Q2'26) coincided with -8.69%.

Street Q3 contract liabilities: the mean of 37,492 implies a fall of 2.5B, which has never happened; the median of 39,944 implies no change. Arithmetic range 41.0-42.9B.

## 9. Report-day record by type of line

| Report | Revenue vs consensus (MB) | Other | Guide action | Day move |
|---|---|---|---|---|
| Q4'24 (2025-01-22) | 10.56 vs 10.70B: -1.3% | EPS miss | reaffirm | +2.67% |
| Q1'25 (2025-04-23) | 8.03 vs 7.56B: +6.2% | | reaffirm | +3.07% |
| Q2'25 (2025-07-23) | 9.11 vs 8.78B: +3.8% | profit beat | margin and FCF raised | +14.58% |
| Q3'25 (2025-10-22) | 9.97 vs 9.15B: +9.0% | EPS 1.64 vs 1.72 | reaffirm; Wind guide worse | -1.59% |
| Q4'25 (2026-01-28) | 10.96 vs 10.21B: +7.3% | EBITDA 1,158 vs about 1,290 (single source) | raise for Prolec; margin held | +2.73% |
| Q1'26 (2026-04-22) | 9.34 vs 9.19B: +1.6% | orders +71% | margin raised | +13.75% |
| Q2'26 (2026-07-22) | 11.10 vs 10.79B: +2.9% | EBITDA 1,250 vs about 1,280; EPS 2.47 vs 3.17 | revenue and FCF raised; margin held | -8.69% |

Revenue beat in six of seven, mean +4.2%, median +3.8%; correlation of the revenue surprise with the day move is -0.22 (n = 7). The three moves above 13% all came with a margin-guide or framework raise (also +15.62% on 2025-12-10). Reaffirm-only days: -1.6% to +3.1%.

First annual guide against the Street on the eve (Bloomberg ConsensusHistory):

| Guide | Range implied ($M) | Street just before | Midpoint vs Street | Day move |
|---|---|---|---|---|
| FY26, 2025-12-09: $41-42B x 11-13% (ex-Prolec) | 4,510-5,460, mid 4,980 | 5,249 (2025-12-05) | -5.1% | +15.62% (2028 framework raised the same day) |
| FY26 with Prolec, 2026-01-28: $44-45B x 11-13% | 4,840-5,850, mid 5,340 | 5,396 (2026-01-23) | -1.0% | +2.73% |
| FY27, late Jan 2027 | whole-number 2-point margin range on a $1B revenue range: 16-18% x about 52.5B = mid 8,925; 17-19% = mid 9,450 | 9,471 | -5.8% or -0.2% | no framework event that day (capital markets day in spring) |

FY26 Street EBITDA is now 6,334, 19% above the January 2026 guide midpoint: first guides have been floors.

## 10. Reveal calendar with pass marks (Street values from BBG-Q / BBG-M)

| Date | Line | Street | Arithmetic range | Note |
|---|---|---|---|---|
| 28 Oct 2026 | Electrification orders Q3 | 6,498 | 4,500-5,900 | below 5,775 = under every broker |
| 28 Oct 2026 | Adj. EBITDA Q3 | 1,672 | 1,543-1,766 | Power margin against 18.1% is the swing |
| 28 Oct 2026 | Equipment revenue Q3 | 7,482 | 7,250-7,690 | |
| 28 Oct 2026 | 10-Q: equipment RPO x % within 1 year | 31,314 (Street, Q4'26-Q3'27) | 31.1-32.1B | 32.5B or more keeps the conversion gap |
| 28 Oct 2026 | Contract liabilities | median 39,944 | 41.0-42.9B | |
| Late Jan 2027 | Wind EBITDA Q4 | +208 | +30 to +250 | FY27 Street Wind +188 |
| Late Jan 2027 | Adj. EBITDA Q4 | 2,500 | 2,327-2,532 | 2,367 at segment guide mids; 2,162 at the company-guide midpoint |
| Late Jan 2027 | FY27 margin guide | 17.9% (9,471 / 53,029) | 16-18% or 17-19% | |
| Late Jan 2027 | 10-K: scheduled FY27 equipment | 32,382 | 31.1-34.8B | |
| Late Apr / Jul 2027 | Equipment revenue Q1'27 + Q2'27 | 14,424 | 15,355-16,233 if H2'26 = Street | |

## 11. Checked, no gap

- Q3 and Q4 Power revenue and margin: Street inside the guide and on seasonality.
- Q3 and Q4 total revenue: within -2% to +4% of the Street.
- Q3 EBITDA: Street sits between the guide midpoint (Street 2.9% above) and the 2026 beat pattern (Street 3.3% below).
- H2'26 equipment revenue: within -2% to +4% of the Street on the FY26 schedule and on seasonality.
- Total orders and backlog: Street H2 orders of 45.4B give year-end RPO of about 195.8B, consistent with "$200B very early in 2027".
- Wind deliveries and equipment revenue for the next four quarters: trailing orders (4.3 GW) x the historical sales / orders ratio (1.16-1.34) cover the Street's 5.16 GW.
- Q3 EPS: -2% to -9% at Street EBITDA depending on the tax rate (24-30%); centre about -5%.
- FY27 revenue guide: division growth rates from the 2028 framework give about 52.5-53.0B against the Street's 53.0B.
