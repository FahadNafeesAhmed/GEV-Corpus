# Thesis hunt, Wind lens: working file (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences and no forecast choices; ranges and methods only. Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

## 0. Sources used

| Tag | Source | Where |
|---|---|---|
| BBG | Bloomberg EEO company-specific and MODL exports | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (keys `Block|Parent|Line|YYYY Qn`), `06_modl.xlsx`, `01-eeo-company-specific.xlsx` |
| 10-Q 2Q26 | Form 10-Q for 6/30/2026 | corpus `gev.db`, accession 0001996810-26-000148 (MD&A Wind p.31; RPO note p.15) |
| 10-K 2025 | Form 10-K for 2025 | accession 0001996810-26-000015 (Wind MD&A p.27; revenue-recognition note: offshore contract losses) |
| 10-Q 3Q25, 10-Q 3Q24, 10-K 2024 | earlier filings | accessions -25-000160, -24-000083, -25-000011 |
| PR | Earnings releases (8-K exhibits) 1Q24 to 2Q26 | corpus documents 369, 338, 328, 326, 291, 277, 268, 265, 226, 215 |
| DECK | Earnings decks 7/23/25, 10/22/25, 1/28/26, 4/22/26, 7/22/26 | gevernova.com `gev_webcast_presentation_<date>.pdf`; the 7/22/26 deck is corpus source 3157 |
| CALL | Call transcripts 10/22/25, 1/28/26, 4/22/26, 7/22/26 | gevernova.com `gev_webcast_transcript_<date>.pdf`; 7/22/26 is corpus source 3161 |
| IU25 | Investor update 12/9/2025, transcript and slides (slide 19 offshore backlog; slide 7 2028 assumptions) | gevernova.com `gev_webcast_transcript_12092025.pdf`, `gev_webcast_presentation_12092025.pdf` |
| CALL 4Q24, 3Q24 | 1/22/2025 and 10/23/2024 transcripts | gevernova.com |
| LAGUNA | Conference transcript 9/16/2026 | project scratch copy (pp. 2-3, 9-10) |
| NEWS | Vineyard Wind settlement 9/16/2026 | company release; Reuters; corpus news sources 3598, 3672 |

## 1. Wind history by quarter ($M unless stated)

| | 1Q24 | 2Q24 | 3Q24 | 4Q24 | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 1,639 | 2,062 | 2,891 | 3,109 | 1,850 | 2,245 | 2,647 | 2,368 | 1,432 | 2,026 |
| Equipment revenue | 1,232 | 1,668 | 2,494 | 2,653 | 1,412 | 1,797 | 2,203 | 1,839 | 889 | 1,395 |
| Services revenue | 407 | 394 | 397 | 455 | 438 | 448 | 445 | 529 | 543 | 632 |
| Offshore revenue | 441 | 353 | 388 | 195 | 204 | 225 | 195 | 28 | 246 | 305 |
| Segment EBITDA | (173) | (117) | (317) | 19 | (146) | (165) | (61) | (225) | (382) | (275) |
| Cost of revenues (ex D&A) | 1,610 | 1,975 | 2,998 | 2,930 | 1,840 | 2,226 | 2,532 | 2,410 | 1,649 | 2,123 |
| Gross profit ex D&A (revenue - cost) | 29 | 87 | (107) | 179 | 10 | 19 | 115 | (42) | (217) | (97) |
| SG&A + R&D + other (gross profit - EBITDA) | 202 | 204 | 210 | 160 | 156 | 184 | 176 | 183 | 165 | 178 |
| Orders, equipment | 744 | 1,774 | 1,349 | 1,580 | 202 | 1,614 | 1,220 | 2,436 | 739 | 721 |
| Orders, services | 405 | 387 | 397 | 451 | 438 | 448 | 613 | 709 | 460 | 528 |
| Orders GW (turbines + repower) | 0.7 | 1.8 | 1.2 | 1.6 | 0.1 | 1.6 | 0.9 | 2.2 | 0.6 | 0.6 |
| Sales GW | 1.1 | 1.6 | 2.4 | 2.7 | 1.3 | 1.7 | 2.1 | 1.9 | 0.6 | 1.4 |
| Equipment RPO, end | 13,119 | 13,147 | 12,182 | 10,720 | 9,676 | 9,731 | 8,782 | 9,112 | 8,905 | 8,197 |
| Services RPO, end | 13,045 | 12,626 | 12,788 | 11,962 | 12,484 | 12,777 | 12,726 | 12,518 | 12,443 | 12,191 |

Sources: DECK trending tables and "Wind: key performance metrics" pages; PR segment tables (cost of revenues, SG&A and R&D are disclosed from the 4Q24 release onward; 1Q24-3Q24 from prior-year columns); 10-Q and 10-K unit tables. 3Q24 revenue includes a $0.5B settlement of a cancelled offshore project and a $0.3B gain.

Identity check (equipment RPO end = start + equipment orders - equipment revenue): residuals by quarter -102, -78, +180, -389, +166, +238, +34, -267, -57, -34. The identity holds within about 3% a quarter (currency and contract changes).

## 2. Offshore numbers the segment line hides

**Incremental offshore contract losses (revenue-recognition note):** 2023 $379M; 2024 $1,005M (H1 $103M, 3Q $676M, 4Q $226M); 2025 $637M (H1 $125M, 3Q $171M, 4Q $341M) [10-K 2025; 10-Q 3Q25; 10-Q 3Q24]. The 1Q26 and 2Q26 10-Qs give no figure; the MD&A says "higher contract losses" (1Q) and "higher project costs" (2Q).

**Segment EBITDA with those charges added back (and the 3Q24 $300M gain removed):**

| | H1 24 | 3Q24 | 4Q24 | H1 25 | 3Q25 | 4Q25 | FY24 | FY25 |
|---|---|---|---|---|---|---|---|---|
| Reported | (290) | (317) | 19 | (312) | (61) | (225) | (588) | (598) |
| + offshore incremental losses | 103 | 676 | 226 | 125 | 171 | 341 | 1,005 | 637 |
| - settlement gain | | (300) | | | | | (300) | |
| = before offshore charges | (187) | 59 | 245 | (187) | 110 | 116 | 117 | 39 |

Reading for the model: the Street's 4Q26 Wind of +$183M is not "ten times the best quarter since 2023". Before offshore charges, 4Q24 was +$245M (revenue $3,109M) and 4Q25 was +$116M (revenue $2,368M). The Street's 4Q26 equals roughly the average of those two and assumes no offshore charge.

**Onshore / offshore split from management statements:**

| Year | Onshore margin stated | Onshore revenue | Onshore EBITDA (computed) | Segment EBITDA | Offshore EBITDA (computed) | Offshore backlog at start of year | Offshore loss / opening backlog |
|---|---|---|---|---|---|---|---|
| 2024 | "approximately 7%" [CALL 4Q24] | 7,781 (8,323 with LM) | 545 to 583 | (588) | (1,133) to (1,171) | ~$4B [IU25 slide 19] | 28-29% |
| 2025 | "within the high single-digit range" (guide) [CALL 4Q24] | 8,241 + 217 LM | 590 to 680 at 7-8% | (598) | (1,190) to (1,280) | ~$3B | 40-43% |
| 2026 guide | "mid-single digit margins" [IU25] | ~7,200 (Street) | 290 to 430 at 4-6% | ~(400) guide | (690) to (830) | ~$2B | 35-42% |
| 2028 target | Wind 6%, "both Offshore Wind projects in backlog complete" [IU25 slide 7] | | | | ~0 | | |

A sell-side question at the March 2024 investor day put the 2023 offshore loss at "about $1.1 billion". Management on 12/9/2025: offshore 2026 "higher revenue ... with slightly less EBITDA losses". Dogger Bank B and C run "through the better part of '27" [CALL 4/22/26].

## 3. Bloomberg Wind consensus (BBG, 2026-10-01)

| | 2Q26 act | 3Q26 | 4Q26 | 1Q27 | 2Q27 | 3Q27 | 4Q27 | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wind revenue | 2,026 | 2,341 | 2,344 | 1,522 | 1,866 | 2,123 | 2,078 | 7,589 | 6,813 | 7,381 | 7,440 |
| Equipment | 1,395 | 1,789 | 1,763 | 1,019 | 1,259 | 1,616 | 1,469 | 5,363 | 4,537 | 5,258 | 5,315 |
| Services | 632 | 545 | 545 | 483 | 573 | 492 | 544 | 2,092 | 2,048 | 2,069 | 2,082 |
| Onshore | 1,721 | 2,088 | 2,221 | 1,250 | 1,623 | 1,996 | 2,005 | 6,873 | 6,635 | 7,690 | 7,863 |
| Offshore | 305 | 215 | 119 | 178 | 212 | 233 | 172 | 795 | 250 | 185 | 160 |
| Adjusted EBITDA | (275) | 25 | 183 | (9) | (12) | 59 | 150 | 188 | 373 | 598 | 630 |
| Orders | 1,249 | 1,510 | 1,761 | 1,180 | 1,296 | 1,567 | 1,635 | 5,678 | 5,638 | 5,352 | 5,471 |
| MW delivered | 1,400 | 1,648 | 1,633 | 694 | 1,188 | 1,571 | 1,515 | 4,968 | 4,479 | 6,087 | 6,316 |

MODL 3Q26 spread: Wind adjusted EBITDA mean 24.6, low (9), high 106, median 0.6; Wind orders mean 1,510, low 721, high 2,198. Individual broker values are not exposed on this export, so the number of contributors per Wind line is unknown. The Street's Wind RPO for 3Q26 and 4Q26 (35,153 and 38,068) is a data error in the mean (high 112,612); ignore it.

Street FY26 Wind = (657) + 25 + 183 = (449). Company guide: about (400), reaffirmed 7/22/2026, with 3Q "approximately break-even". Guide-implied 4Q26 = +257 if 3Q is zero.

## 4. Tests run and results

### T1. Revenue against the guide: no gap
FY26 guide "organic revenue down low-double digits" on 9,110 gives 7,926-8,199 before currency (+59 in H1); H2 implied 4.5-4.8B. Street H2 4,685. 3Q guide "down low-double digits" on 2,647 gives 2,303-2,382; Street 2,341.

### T2. Equipment revenue against the Wind equipment backlog: Street at the top of the range, not outside it
Next-four-quarter Wind equipment revenue / opening Wind equipment RPO:

| Date | Equipment RPO | Next 4Q equipment revenue | Ratio | Basis |
|---|---|---|---|---|
| 12/31/23 | 13,709 | 8,047 | 58.7% | reported |
| 6/30/24 | 13,147 | 8,356 | 63.6% | reported |
| 12/31/24 | 10,720 | 7,251 | 67.6% | reported |
| 6/30/25 | 9,731 | 6,326 | 65.0% | reported |
| 12/31/25 | 9,112 | 5,836 | 64.1% | H2 is Street |
| 6/30/26 | 8,197 | 5,830 | 71.1% | all Street |

At 63.6-67.6% the window would be 5,213-5,541, which is 5-11% below the Street. But with offshore taken out (offshore backlog about 3.0B, 2.5B, 2.3B and 1.5-1.8B at the last four dates, from IU25 slide 19 less offshore revenue) the onshore-only ratio is 72.8%, 85.1%, 77.2%, 72.9% and the Street's is 79.4%: inside the range. Second check: next-4Q onshore equipment revenue / trailing-12-month equipment orders = 1.21, 1.17, 0.90, and Street 1.00 (5,106 / 5,116). Result: no candidate. The error band is wider than the gap.

### T3. The Street's own Wind orders against its own Wind revenue: inconsistent after 2027
Equipment backlog path = 8,197 + (Street Wind orders - Street services revenue) - Street equipment revenue: end-2026 6,826; 2027 5,048; 2028 4,101; 2029 2,126; 2030 199. Book-to-bill 0.75, 0.83, 0.73, 0.74. The Street's 2029 Wind revenue rebound (+8%) is not supported by the Street's own orders line. Few analysts supply 2029-2030 and the period is outside the pitch horizon, so this is a note, not a candidate.

### T4. 2028 Wind revenue against the company's stated growth rate
"Down low-double digits organic revenue CAGR ... 2025 is the base year" [PR 4Q25]: 9,110 x 0.90^3 = 6,641; x 0.88^3 = 6,208; x 0.87^3 = 5,999. Street 6,813 (CAGR -9.2%). The Street is 2.6% above the top of the range before currency. Not a gap.

### T5. 4Q26 and FY26 Wind EBITDA: Street is reasonable, the guide needs the best case
H2 onshore margins computed from section 2: about 8.6-10% (H2 2024) and 9-12% (H2 2025). H2 2026 onshore revenue 4,310 (Street) at 9-12% = 390-515. If the 2026 offshore loss (690-830 on the guide) was booked mostly in H1, H2 offshore is about (150) to (300). H2 2026 Wind = +90 to +365; Street +208; guide +257. The guide needs the top of the onshore range and the low end of offshore losses. The Street's (449) for FY26 already sits below the guide. No provable gap. The Vineyard Wind settlement (9/16/2026, terms confidential; the company had claimed $300-360M owed, the customer $850M of damages) lands in 3Q26 and its sign is unknown.

### T6. FY27 Wind EBITDA by parts: Street at the top edge of the range
- Onshore: Street Wind revenue 7,589 less Street offshore 795 = 6,794. At 4% / 5% / 6% / 7%: 272 / 340 / 408 / 476.
- Offshore: Street-implied loss = 188 - (272 to 408) = (84) to (220), against (690)-(830) guided for 2026. Opening 2027 offshore backlog about $1.0-1.4B (IU25 slide 19 path; Street offshore revenue after 2026 is 1,390). Offshore loss / opening backlog was 28-43% in 2024-2026. At 28% / 37% / 43% on 1.0-1.4B: loss 280 to 600; central 1.1B x 37% = 407.
- Wind FY27 = onshore - offshore loss: low 272 - 600 = (328); central 340 - 407 = (67); high 476 - 280 = +196. Street +188.
- Company effect of the central case: (67) - 188 = (255), which is 2.7% of Street FY27 adjusted EBITDA of 9,471.
- First-half check: the Street has H1 2027 at (21) on revenue 3,388. H1 2024, H1 2025 and H1 2026 were (290), (312) and (657) on revenue 3,701, 4,095 and 3,459.

### T7. Wind and the surviving equipment-conversion discrepancy
Company: 36% of $87,821M equipment RPO within one year = $31,616M (31,176-32,055 for rounding) [10-Q 2Q26 p.15]. Street equipment revenue 3Q26-2Q27 by division (BBG): Power 10,874; Electrification 13,541; Wind 5,830; total 30,245.

| Assumed Wind conversion of its 8,197 equipment RPO | Wind scheduled | Power + Electrification scheduled | vs Street Power + Electrification 24,415 |
|---|---|---|---|
| 71.1% (the Street's own Wind figure) | 5,830 | 25,786 | +5.6% |
| 68% (highest reported ratio) | 5,574 | 26,042 | +6.7% |
| 64% | 5,246 | 26,370 | +8.0% |
| 60% | 4,918 | 26,698 | +9.3% |

Break-even: for the Street's Power + Electrification figure to equal the schedule, Wind would have to convert (31,616 - 24,415) / 8,197 = 87.9% of its equipment backlog in a year (82.5-93.2% for rounding). Its reported ratio has been 58.7-67.6%, and that ratio includes orders booked and shipped inside the year.

Back-test of the same statistic (Power + Electrification actual equipment revenue / (company scheduled - Wind actual)): window from 12/31/24: 13,683 / 11,690 = 1.170; from 3/31/25: 15,263 / 13,737 = 1.111 (1.077 without Prolec's 469 in 1Q26); from 6/30/25: 17,230 / 14,553 = 1.184 (1.094 without Prolec's 1,303 in H1 2026). Windows that contain Street quarters fall as the Street share rises: about 1.05 (9/30/25, one Street quarter), 1.04 (12/31/25, two), 1.005 (3/31/26, three), 0.947 (6/30/26, all Street).

Applying 1.00 / 1.077 / 1.170 to 25,786: 25,786 / 27,770 / 30,170, against Street 24,415: +5.6% / +13.7% / +23.6%.

Segment detail for the model's comparison tab (next-4Q equipment revenue / opening equipment RPO): Power 53.6% (12/31/24), 50.9%, 46.7% (6/30/25), then with Street quarters 43.2%, 37.8%, 35.2%, 27.7% (6/30/26, all Street). Electrification 36.9% (12/31/24), 38.6%, 41.5% (36.1% without Prolec), then 40.7%, 33.6%, 33.4% (6/30/26, all Street).

### T8. Smaller items
- 3Q26 Wind orders: Street 1,510. Management on 9/16/2026: "I wouldn't expect a different orders dynamic in the third quarter" (1Q 1,199, 2Q 1,249). Not a profit line.
- Wind services revenue: the Street has 545 a quarter in H2 2026 and 2,092 for 2027, below the last four quarters (2,149) and below trailing services orders (2,310). No disclosed schedule proves a number.
- Tariffs: 1Q26 Wind carried about $70M [CALL 1/28/26]; the company-wide 2026 estimate was cut from $250-350M (April) to $100-200M (10-Q 2Q26) "including pursuing the recovery of certain tariffs".

## 5. What comes out

| # | Line and period | Street | Arithmetic | Gap | Status |
|---|---|---|---|---|---|
| 1 | Power + Electrification equipment revenue, 3Q26-2Q27 (company equipment revenue with Wind removed) | 24,415 | 25,786 floor; 27,770 with the smallest reported uplift | +5.6% floor; +13.7% | candidate; sharpens the surviving discrepancy |
| 2 | Wind segment EBITDA, FY27 | +188 | (67), range (328) to +196 | (255), 2.7% of company EBITDA | weak candidate; band about as wide as the gap; use as a model input |
| - | Wind equipment revenue, 3Q26-2Q27 | 5,830 | 5,213-5,541 blended; inside range onshore-only | -5% to -11% or nil | no candidate |
| - | Wind EBITDA 4Q26 / FY26 | +183 / (449) | H2 +90 to +365 | inside range | no candidate |
| - | Wind revenue FY28 | 6,813 | 5,999-6,641 | +2.6% above top | no candidate |

## 6. Open items
- The 6/30/26 offshore backlog and the H1 2026 offshore loss are not disclosed; both are estimated above.
- Segment-level "within one year" percentages are not disclosed; T7 bounds Wind with its realised turnover.
- Reveal dates: 3Q26 results 10/28/2026 (Wind 3Q EBITDA, implied 4Q guide, settlement effect); January 2027 call (FY27 Wind guide, 1Q27 Wind guide, 10-K offshore loss figure for 2026); 10-Qs in April and July 2027.
