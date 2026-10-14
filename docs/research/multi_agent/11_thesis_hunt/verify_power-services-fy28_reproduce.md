# Verify (reproduce): power-services-fy28

_AI-assisted research input only. Facts, arithmetic, tables and sources. Bloomberg data is licensed for academic use: keep it inside the project folder and cite it as "Bloomberg, 2026-10-01"._

Check type: REPRODUCE. Every number recomputed from the primary files. Verdict at the end.

Sources used
- Bloomberg, 2026-10-01: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (keys `Total Revenue|Power|Services|YYYY Qn`, `...|Equipment|...`, `Total Revenue||Power|...`), `06_modl.xlsx` (Q3'26 mean / low / high / median), `street_segments_annual_2026-10-01.csv`.
- Filings in `gev.db` (documents table): 10-K FY24 0001996810-25-000011; 10-K FY25 0001996810-26-000015; 10-Q Q1'24 -24-000008; Q2'24 -24-000067; Q3'24 -24-000083; Q1'25 -25-000073; Q2'25 -25-000133; Q3'25 -25-000160; Q1'26 -26-000064; Q2'26 -26-000148; Form 10 exhibit 0001193125-24-063739.
- December 2025 investor update: deck = corpus sources id 1844 (slide 28); transcript = gevernova.com/sites/default/files/gev_webcast_transcript_12092025.pdf (fetched 2026-10-01, not in the corpus).

## 1. Street side: reproduces exactly

| Item | Candidate | Recomputed | Result |
|---|---|---|---|
| FY28 Power services | 17,665 | 3,898.5 + 4,367.7 + 4,216.8 + 5,182.5 = 17,665.4 | match |
| FY27 | 15,675 | 15,675.0 | match |
| FY28 growth | +12.7% | +12.70% | match |
| FY30 | 22,357 | 22,356.6 | match |
| FY26 (H1 actual + Street H2) | 14,259 | 3,086 + 3,512 + 3,389.0 + 4,271.5 = 14,258.5 | match |
| Growth FY26-FY30 | 11.9% a year | 11.90% | match |
| Street 2028 Power revenue / equipment / adj. EBITDA / margin | 33,521 / 15,888 / 7,810 / 23.3% | 33,520.9 / 15,888.5 / 7,810.0 / 23.30% | match |
| Q3'26 growth | +8.7% | +9.5% on reported Q3'25 (3,094); +8.6% on an estimated recast base (3,120) | match, but the base is an estimate |
| Q4'26 growth | +11.6% | +12.3% on reported 3,802; +11.6% on estimated recast 3,828 | match, same caveat |
| Q1'27, Q2'27 growth | +11.0%, +10.2% | 3,424.1 / 3,086 = +11.0%; 3,870.2 / 3,512 = +10.2% | match |
| Next four quarters vs trailing | 14,955, +10.8% | 14,954.9; +10.8% on reported trailing 13,494; +10.4% on recast 13,547 | match |

Definition check: Bloomberg's Q2'26 actuals (services 3,512, equipment 1,965, Power 5,477) equal the 10-Q MD&A Power table, so the Street line and the company line are on the same definition (segment revenue including intersegment). The XBRL external-revenue figure (3,509) is 3 lower; not material.

Quality of the Street line (new findings)
- Broker-level values are not shown for this line in `06_modl.xlsx` (no broker column is populated). The number of contributors is unknown.
- Q3'26: mean 3,389.0, median 3,328.8, low 3,167.3, high 3,737.2. The mean is 1.8% above the median. Low to high is -6.5% to +10.3% around the mean, in the nearest quarter.
- Street equipment plus services does not equal Street Power total: FY27 -295 (-1.05%), FY28 +33 (+0.1%), FY29 -555 (-1.4%), FY30 +611 (+1.35%). The lines come from different broker sets.
- Year-on-year growth in the Street line steps from +9.2% (Q4'27) to +13.9% (Q1'28). Q1'31 is +2.2% on Q1'30. Both are signs that the contributor set changes at the year boundary. Part of the FY28 "+12.7%" may be a change in who is in the mean.

## 2. Company history: reproduces

Power MD&A table, services row ($M):

| Period | Services | Source |
|---|---|---|
| FY22 / FY23 / FY24 | 11,228 / 11,838 / 12,419 | 10-K FY24 |
| FY25 | 13,081 | 10-K FY25 |
| Q1'25 / Q2'25 / Q3'25 / Q4'25 (as first reported) | 2,931 / 3,253 / 3,094 / 3,802 | 10-Qs; Q4 = 13,081 - 9,279 |
| Q1'25 / Q2'25 recast | 2,958 / 3,280 (H1 6,238) | 10-Q Q1'26, Q2'26 |
| Q1'26 / Q2'26 | 3,086 / 3,512 (H1 6,598) | 10-Q Q1'26, Q2'26 |

- Growth FY23, FY24, FY25: +5.4%, +4.9%, +5.3%. H1'26: +5.8%. All match.
- By quarter on a like basis: Q3'25 +11.3%, Q4'25 +4.6%, Q1'26 +4.3%, Q2'26 +7.1%. Trailing twelve months to Q2'26: +6.7% (13,440 vs 12,600 on the old basis).
- Recast: the 2026 10-Qs moved a part of the former Electrification Software unit into Gas Power ("a component of our former Electrification Software business unit was realigned into Gas Power"). It adds about 27 a quarter to 2025 services. The candidate's FY25 recast of 13,187 and the Q3'25 / Q4'25 recast bases are estimates, not reported figures (error about 0.2% a year, 0.8% a quarter).
- Not in the candidate: FY24 and H1'25 growth is held down by the sale of part of Steam Power's nuclear activities (closed Q2'24). The 5% history understates like-for-like growth for those periods. The four quarters after the anniversary average +6.7%.

## 3. Method 1 (the 2035 chart): arithmetic reproduces, the reading does not hold as a 2028 number

- Slide 28 (sources id 1844): "Total Gas Power & Steam Power services revenue", "~$12B" (2025E), "+$10B", "~$22B" (2035E); sub-title "services revenue accelerating in the 2030s".
- Transcript: "about $12 of the $19 billion in revenue this year is in Gas and Steam services. That number by 2035, that $12 billion will be at least $22 billion."
- (22/12)^(1/10) - 1 = 6.249%. 12 x 1.0625^3 = 14.39. Plus nuclear and hydro services 1.19 x 1.06^3 to 1.13^3 = 1.42 to 1.72. Total 15.81 to 16.72 = -10.5% to -5.4% vs 17,665. Match.
- Simpler version: all Power services at 6.25% from FY25 = 15,690 (reported base) to 15,817 (recast base) = -11.2% to -10.5%.
- Read the other way: to reach the Street's 2028, gas and steam services must grow 10.0% to 10.6% a year from $12B. Held for ten years that rate gives $31B to $33B in 2035.

Problems
1. The 2035 figure is a floor. The CEO said "at least $22 billion", and in Q&A: "I view our role here is to continue to give you incremental financial floors". A September 2026 conference report (sources id 681, secondary) says he called the path conservative.
2. The company gives no 2026, 2027 or 2028 services number. In Q&A: "I don't think we're ready to kind of quantify that number per se." The 2028 value is a constant-rate line drawn between two company figures. That is the method the brief lists as failed.
3. The quote "We should expect a higher services revenue base in 2026 and 2027 and 2028" is ambiguous in context (it sits between a sentence about the order book growing and a sentence about a four-to-five-year lag). It cannot be used for either side.
4. "~$12B" is rounded: 11.5 to 12.5 is plus or minus 4% on the base.

## 4. Method 2 (Note 9 components): numbers reproduce, the growth range is too narrow

Note 9 sentence, each filing ("Net contractual service agreements increased primarily due to revenues recognized of $X million, partially offset by billings of $Y million and net unfavorable changes in estimated profitability of $Z million"):

| Period | Revenue recognised | Billings | Profitability change | Accession |
|---|---|---|---|---|
| FY23 | 4,658 | 5,047 | +34 | 0001193125-24-063739 |
| FY24 | 5,473 | 5,021 | -319 | 0001996810-25-000011 |
| FY25 | 5,412 | 5,362 | -151 | 0001996810-26-000015 |
| H1'25 | 2,720 | 2,533 | -42 | 0001996810-25-000133 |
| H1'26 | 2,689 | 2,392 | -218 | 0001996810-26-000148 |

- Scope check: "net" is contract-service assets less contract-service liabilities (5,399 - 1,880 = 3,519 at 6/30/26; 5,417 - 1,977 = 3,440 at 12/31/25; change +79 = 2,689 - 2,392 - 218). So the revenue figure covers all contract service agreements, not only those in an asset position. The candidate's use of it is valid.
- By quarter, Q1'24 to Q2'26: 1,174 / 1,363 / 1,173 / 1,763 / 1,261 / 1,459 / 1,104 / 1,588 / 1,280 / 1,409. Match.
- FY25 -1.1%, H1'26 -1.1%. Match. Non-contract: FY24 6,946, FY25 7,669 (+10.4%); H1'25 3,518, H1'26 3,909 (+11.1%). Match.
- Candidate's scenario grid reproduces: contract 0-5%, non-contract 11-13% gives FY28 16,017 to 17,063 (-9.3% to -3.4%).

Corrections
1. "Flat for ten quarters" starts after a +17.5% step (FY23 4,658 to FY24 5,473). From FY23 to the trailing twelve months (5,381) contract revenue grew 5.9% a year. It is lumpy (quarterly year-on-year: +7.4%, +7.0%, -5.9%, -9.9%, +1.5%, -3.4%).
2. Non-contract services grew faster than the candidate's 11-13% on a clean trailing basis. Quarterly year-on-year: Q1'25 +0.7%, Q2'25 -0.7% (both still carry the Steam disposal), Q3'25 +23.8%, Q4'25 +18.3%, Q1'26 +6.5%, Q2'26 +15.7%. Trailing twelve months to Q2'26: 8,059 vs 6,944 = +16.1%.
3. The Street's 2030 needs non-contract growth of about 15.5% to 18%. The trailing rate is 16.1%. So the component split does not separate the Street from the data.

Grid extended to the trailing rate (FY28, $M, gap vs 17,665):

| Contract growth | Non-contract 11% | 13% | 15% | 16% |
|---|---|---|---|---|
| 0% | 16,017 (-9.3%) | 16,512 (-6.5%) | 17,022 (-3.6%) | 17,283 (-2.2%) |
| 2.5% | 16,289 (-7.8%) | 16,784 (-5.0%) | 17,294 (-2.1%) | 17,555 (-0.6%) |
| 5% | 16,568 (-6.2%) | 17,063 (-3.4%) | 17,574 (-0.5%) | 17,834 (+1.0%) |

Total-growth view from the recast FY25 base 13,187: 6.6% a year gives 15,974 (-9.6%); 8% gives 16,612 (-6.0%); 9% gives 17,078 (-3.3%); 10% gives 17,552 (-0.6%). The answer is set by which growth rate is assumed, not by a disclosed schedule.

## 5. Other items

| Item | Candidate | Recomputed | Result |
|---|---|---|---|
| Services gross margin H1'26 | 31.6% | (8,729 - 5,974) / 8,729 = 31.6% | match, but company-wide (includes Wind and Electrification services), not Power |
| Incremental services gross margin | 52% | (2,755 - 2,405) / (8,729 - 8,052) = 350 / 677 = 51.7% | match, same caveat |
| Power services backlog growth | +14.7% | 72,388 / 63,088 = +14.7% | match |
| Power services orders | +12% to +29% a quarter | Q4'25 +15%, Q1'26 +29%, Q2'26 +12% (press releases, call) | match |
| Framework tie-out | 19,767 x 1.17^3 to 1.19^3 = 31.7 to 33.3 | 31.66 to 33.31; deck says "Revenue up high teens at Power & Electrification" 2025-2028 | match; this framework predates the FY26 Power guide raise to 18-20% |
| Years 2-5 scheduled services | +26% in 18 months | 75,976 x 35% / 4 = 6,648 (12/31/24); 88,463 x 38% / 4 = 8,404 (6/30/26); +26.4% | match (evidence for the Street) |
| HA cross-check | $25M per GW a year | rests on a secondary news report; not checked against a filing | not verified |
| Profit effect 2028 | $0.27-0.83B, 2-7% of 12,553 | 0.8-1.7 x 35-50% = 0.28-0.85; 2.2%-6.8% | match |

## 6. In-horizon lines (reported within 12 months)

| Line | Street | Arithmetic at 6% / 7.5% / 9% growth | Gap |
|---|---|---|---|
| Q3'26 (2026-10-28) | 3,389 mean; 3,329 median | 3,307 / 3,354 / 3,401 on base 3,120 | -2.4% to +0.4% vs mean; inside the mean-median spread |
| Q4'26 (late Jan 2027) | 4,271.5 | 4,058 / 4,115 / 4,173 on base 3,828 | -5.0% to -2.3% |
| Q3'26-Q2'27 | 14,955 | 14,360 / 14,563 / 14,766 on base 13,547 | -4.0% to -1.3% |

No in-horizon line reaches a 5% gap at its central value. FY28 is not reported until early 2029.

## 7. Corrected values and verdict

| | Candidate | Corrected |
|---|---|---|
| Street FY28 Power services | 17,665 | 17,665 (mean; contributor count unknown; median likely lower) |
| Our value FY28 | 15.8 to 17.1, central about 16.5 | 15.7 to 17.8, central about 16.7 |
| Gap | -6.6% | about -5% (range -11% to +1%) |
| Error band on our value | not stated (range is plus or minus 4%) | about plus or minus 6%, before Street-side noise of 1-2% |

Reproduced: yes. Every figure in the candidate recomputes from the primary files, apart from the HA per-GW figure (secondary source) and the recast H2'25 bases (estimates).

Survives: no, on the stated rule (gap at least about 5% and larger than its own error band).
1. The corrected gap (about -5%) is not larger than its error band (about plus or minus 6%). With non-contract services at the trailing-twelve-month rate (16.1%) the FY28 gap is -2% to +1%.
2. The FY28 value is not arithmetic on a disclosed schedule. Method 1 interpolates a figure the company calls a floor. Method 2 depends on a chosen growth rate.
3. The settling year is outside the horizon. In-horizon lines show gaps of 0% to -5%, central about -3%.
4. The Street line is a mean of an unknown number of brokers, 1.8% above its median in the nearest quarter, and equipment plus services misses the Power total by up to 1.4%.
5. Profit effect even if right: 2% to 7% of Street FY28 EBITDA.

What does stand (usable as a qualifier or a supporting fact, not as the wedge)
- The Street has Power services growth stepping up from a reported 5-7% to 10-13% in FY27-FY28. That step is real and reproducible.
- The Street's FY30 Power services ($22.4B) equals the company's 2035 floor for gas and steam services ($22B). True as arithmetic; the company's own wording ("at least", "floors") limits what it proves.
- Useful near-term tests: Q3'26 services growth vs +8.6% (mean) or +6.7% (median); nine-month contract-service revenue vs 3,824; FY26 contract-service revenue vs 5,412.

## 8. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
S = lambda y, q: d[f'Total Revenue|Power|Services|{y} Q{q}']
street28 = sum(S(2028, q) for q in range(1, 5))            # 17,665.4
g = (22 / 12) ** 0.1 - 1                                    # 6.249%
csa_q = [1174, 1363, 1173, 1763, 1261, 1459, 1104, 1588, 1280, 1409]      # Note 9, Q1'24..Q2'26
svc_q = [2833, 3170, 2781, 3635, 2931, 3253, 3094, 3802, 3086 - 27, 3512 - 27]  # MD&A, old basis
non_q = [s - c for s, c in zip(svc_q, csa_q)]
ttm_non_growth = sum(non_q[6:]) / sum(non_q[2:6]) - 1      # +16.1%
h2_non = (3119 + 3828) - (1104 + 1588)
def fy28(cg, ng):
    non26 = (6598 - 2689) + h2_non * (1 + ng)
    return 5381 * (1 + cg) ** 2 + non26 * (1 + ng) ** 2
```
