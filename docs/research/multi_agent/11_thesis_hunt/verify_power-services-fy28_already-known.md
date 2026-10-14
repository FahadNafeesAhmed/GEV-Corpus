# Check: "already known or bad data" on candidate power-services-fy28 (2026-10-01)

_AI-assisted research input only. Facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg data is licensed for academic use: keep it inside the project folder and cite it as "Bloomberg, 2026-10-01"._

**Result: does not survive this check.** The arithmetic reproduces. The candidate fails on three of the four outside tests: the Street line is thin and cannot be confirmed as solid, the "company's own chart" has been publicly disowned by the company as a path, and there is an ordinary explanation for the Street sitting above it.

## 0. What reproduced

| Item | Candidate | Recomputed | Source |
|---|---|---|---|
| Street FY28 Power services | 17,665 | 17,665 (3,898.5 + 4,367.7 + 4,216.8 + 5,182.5) | Bloomberg, 2026-10-01, `segment_quarterly.json` |
| Street FY27 / FY29 / FY30 | 15,675 / 19,711 / 22,357 | same | same |
| FY26 (H1 actual + Street H2) | 14,259 | 14,259; Street H2'26 = 7,661 = +10.2% on recast H2'25 (6,949) | same + 10-Q2'26 |
| Power services FY23-FY25 | 11,838 / 12,419 / 13,081 | same | 10-K25 MD&A Power table |
| H1'26 vs H1'25 recast | 6,598 vs 6,238 (+5.8%) | same | 10-Q2'26 p.29 |
| Contract-service revenue | FY24 5,473; H1'25 2,720; H1'26 2,689 | same | Note "Contract and other deferred assets" in 10-K24, 10-Q2'25, 10-Q2'26 |
| Component build 2028 | 16,017 to 17,574 | same (contract 0-5%, non-contract 11-15%) | candidate's own formula |
| Chart rate | 6.25% a year | (22/12)^0.1 - 1 = 6.25% | Dec 2025 deck slide 28 |

## 1. Is the Street figure solid? No, it cannot be confirmed.

- **Contributor count is not shown.** `06_modl.xlsx` (Q3'26) lists 29 brokers, but every broker cell on the Power equipment and Power services rows is blank on this terminal. Only the mean, low, high and median are visible.
- **Lower bound on count, from the four visible statistics (Q3'26 Power services: mean 3,389.0, low 3,167.3, high 3,737.2, median 3,328.8):** two brokers would give a mean of 3,452.3; three 3,411.1; four 3,390.5. None equals 3,389.0, so there are at least five. Five is feasible. Total revenue for the same quarter has 28 brokers (`01_eeo_annual.xlsx`).
- **Upper bound for 2028:** quarterly EPS for Q3'28 and Q4'28 has 13 contributors (`08_eeg_2028.xlsx`: mean 8.643846 = 112.37 / 13). Quarterly revenue for 2030 has 12. Annual EBITDA for 2028 has 33. So the FY28 services line comes from at most about 13 brokers, probably fewer.
- **The mean is pulled up by a high estimate.** Q3'26 mean is 1.8% above the median. Year on year (recast Q3'25 about 3,119): mean +8.7%, median +6.7%, low +1.5%, high +19.8%. The spread around the mean is -6.5% to +10.3% for a quarter that had already ended when the data was pulled.
- **The division lines do not add up, which shows the broker set changes from line to line:**

| Year | Equipment + services less Power total $M | Gas + nuclear + hydro less Power total $M |
|---|---|---|
| 2027 | -295 (-1.0%) | -796 (-2.8%) |
| 2028 | +33 (quarters range -151 to +138) | -1,275 (-3.8%) |
| 2029 | -555 (-1.4%) | -452 (-1.1%) |
| 2030 | +611 (+1.4%) | +704 (+1.6%) |
| Q1-Q2 2031 | 0 exactly (one broker, or one identical set) | |

- Power services growth drops from +14.3% (Q4'30) to +2.2% (Q1'31) when the set shrinks. The 2029-2030 lines are therefore not comparable with 2027-2028.
- **No second vendor for the division split.** A free vendor page (S&P-based, date not stated, share price shown $1,110) has total revenue 45,483 / 51,907 / 59,203 for 2026-2028, which is 1.6% / 2.1% / 2.9% below Bloomberg. It has no services line.
- Reading: internal inconsistency of 1-4% and a mean-to-median skew of about 2% sit against a claimed FY28 gap of 6.6%.

## 2. Is the idea already stated? Yes, and the company has answered it.

| Date | Source | What was said |
|---|---|---|
| 2025-12-09 | Investor update transcript (gevernova.com) | Gas and steam services "at least $22 billion" by 2035. In Q&A the CEO said to "expect a higher services revenue base in 2026 and 2027 and 2028", that the company was not ready to quantify it, and that the 2035 figure is a financial floor |
| 2025-12-09 | Same, slide 28 narration | Contract escalation "every year"; upgrades to grow "at least 50%, and likely will be higher late in the decade" |
| 2026-07-22 | Q2'26 call (corpus src:3161) | Transactional services orders per unit "continue to rise by double digits annually" |
| 2026-09-12 | Jefferies note, as reported in the press | The market undervalues services; current forecasts are below the broker's own |
| **2026-09-16** | **Conference transcript (stockanalysis.com, Quartr)** | **The CEO called the $10B rise a "conservative marker" and said the 2030 number to be shown at the capital markets day "will certainly make the 2035 marker of $22 billion look low"** |

- The 2026-09-16 statement is the key one. The candidate's Method 1 treats the chart as the company's path, and its reveal table uses "2030 services at $20B or less" at the spring 2027 capital markets day as a pass mark. The company has said in advance that its 2030 figure will sit well above the chart line. The candidate text records "the CEO has called it conservative" but not this sentence.
- So brokers above the chart are following what management has told them. This is not a schedule nobody models.
- The published debate on this line runs the other way (a broker arguing services forecasts are too low).

## 3. Has the stock moved on it?

- 2026-09-15 close $882.8; 2026-09-16 (conference day) $925.1, +4.8%. Services was one of several topics that day.
- Quarterly services growth has not driven the stock. Q1'26: services +4.3%, stock +13.7% on the day. Q2'26: services +7.1%, stock -8.7%. Q3'25: services +11.3%, stock -1.6%.

## 4. Ordinary explanations for the gap

- **Guided total, brokers' own split.** Management guides Power revenue in total: Q3'26 +17-19%, FY26 organic +18-20%, 2028 high-teens growth a year from 2025 (19,767 x 1.17^3 to 1.19^3 = $31.7-33.3B). The Street's Power total follows these (FY26 23.6B, FY28 33.5B). The equipment and services split is each broker's allocation. The same broker set has equipment below the backlog schedule (BLOOMBERG_VERDICT section 10) and services above trend. The two offset in revenue. They are one observation about the split, not two.
- **Quarterly services growth is noisy.** Reported year on year, Q1'24 to Q2'26: +7.3, +6.2, +6.9, +0.7, +3.5, +2.6, +11.3, +4.6, +4.3, +7.1%. Mean 5.4%, standard deviation 2.8 points, range 0.7% to 11.3%. A quarter above 10% has already happened (Q3'25). The proposed pass mark (8% or less) and fail mark (10% or more) are less than one standard deviation apart.
- **Reported history understates organic growth.** Part of Steam Power was sold in mid-2024, and 2025 figures were recast in 2026. Company-wide organic services growth: FY25 +7%, 9M'25 +9%, Q3'25 +11%, Q1'26 +4%, Q2'26 +10% (10-K25, 10-Qs).
- **Leading indicators grow faster than revenue.** Power services RPO 72,388 vs 63,088 a year earlier (+14.7%). Power services orders +15% (Q4'25) and +12% (Q2'26).
- **The 2025 chart base is approximate.** "About $12B" and "at least $22B" are rounded. The business units were realigned on 2026-01-01 (Steam Power folded into Gas, Nuclear and Hydro), so the "gas + steam" base can no longer be read from filings.

## 5. Corrected numbers

| | Candidate | After this check |
|---|---|---|
| Street FY28 Power services | 17,665 (stated as consensus) | 17,665 is a mean of an undisclosed subset (at least 5 brokers in Q3'26, at most about 13 in 2028). If the Q3'26 mean-to-median skew held, the median would be about 17,350 |
| Research range FY28 | 15.8-17.1B, central 16.5B (two methods) | Chart method withdrawn. Component method alone: 16.0-17.6B, central about 16.8B |
| Gap | -6.6% | about -5% against the mean (range -9% to -0.5%); about -3% against a median-adjusted figure |
| Error band on research value | not stated | about plus or minus 5% |

- The gap is about the size of its own error band and is below the 7% lower edge of the winners' range.
- FY28 is not reported inside the 3-12 month horizon. The in-horizon events are four noisy quarterly prints, a January guide that carried no services number in January 2026, and a capital markets day at which the company has said the services figure will be high.

## 6. What is left that is true

- Contract-service revenue has been flat for ten quarters (5,473 in FY24, 5,412 in FY25 as given by the candidate and not re-read here, 2,689 vs 2,720 in H1). All services growth is non-contract. This is a real, checkable fact that few models split out.
- The Street needs H2'26 Power services +10.2% against +5.8% in H1'26. Q3'26 (2026-10-28) is the first reading; the median broker has +6.7%.
- These are monitoring items for the team's model. They are not a wedge on their own.

## Sources

- Bloomberg, 2026-10-01: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx`, `08_eeg_2028.xlsx`.
- Filings in `data/gev.db`: 10-K25 (0001996810-26-000015), 10-Q1'26 (-26-000064), 10-Q2'26 (-26-000148), 10-Q3'25 (-25-000160), 10-Q2'25 (-25-000133), 10-K24 (-25-000011), 10-Qs of 2024.
- Corpus sources: src:1844 (Dec 2025 deck), src:3161 (Q2'26 call), src:2660 (Q4'25 call), src:681 (conference coverage).
- Web, fetched 2026-10-01: gevernova.com/sites/default/files/gev_webcast_transcript_12092025.pdf; stockanalysis.com/stocks/gev/transcripts/745262-morgan-stanley-s-14th-annual-laguna-conference/; press report of the 2026-09-12 broker note (pro.edgex.exchange); simplywall.st GEV future page.
- Prices: `prices` table in `gev.db`.
