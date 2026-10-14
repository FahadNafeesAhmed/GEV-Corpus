# Verify (REPRODUCE): candidate `wind-fy27-ebitda`

_AI-assisted research input only: facts, arithmetic, tables, sources. No memo sentences, no forecast choices. Bloomberg figures cited as "Bloomberg, 2026-10-01"; keep inside the project folder._

**Verdict: numbers reproduce; the candidate does NOT survive as a wedge.** The Street value (+$188M) sits inside the candidate's own range and inside the corrected range. The gap is smaller than its error band, and the company-level effect is under 3% of FY27 adjusted EBITDA. Usable as a model input and as a known offset only.

## 1. Street side, recomputed (Bloomberg, 2026-10-01)

Source: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`; cross-checked against `01..02-eeo-company-specific.xlsx` (field `IS_ADJUSTED_EBITDA_AS_REPORTED`, segment `SEG5357074923`) and `street_segments_annual_2026-10-01.csv`.

| Line | 1Q27 | 2Q27 | 3Q27 | 4Q27 | FY27 | Candidate | Match |
|---|---|---|---|---|---|---|---|
| Wind adjusted EBITDA | -9.2 | -11.8 | 58.6 | 150.0 | **187.7** | 188 | yes |
| Wind EBITDA (second line, `IS_EBITDA`) | -8.0 | 15.5 | 65.5 | 115.5 | 188.5 | n/a | consistent |
| Wind revenue | 1,522 | 1,866 | 2,123 | 2,078 | 7,588.5 | 7,589 | yes |
| Offshore revenue | 178 | 212 | 233 | 172 | 794.6 | 795 | yes |
| Onshore revenue (own line) | 1,250 | 1,623 | 1,996 | 2,005 | 6,873.4 | 6,794 (derived) | see note |

- H1 2027: EBITDA -20.9 on revenue 3,388.0. H2 2027: +208.6 on 4,200.5. Match.
- FY26 Street: -382 - 275 (actual) + 24.6 + 183.2 = **-449.2**. Match. H2 2026 Street +207.8.
- FY26 Wind revenue 8,143; offshore 885; onshore 7,257. Match ("about 7,200").
- Wind share of Street EBITDA growth 2026 to 2027: (188 + 449) / (9,471 - 6,334) = 637 / 3,137 = 20.3%. Match.
- Size: (-67 - 188) / 9,471 = -2.69%; range +0.08% to -5.45%. Match.

Notes on the Street side:
1. **Definition is the same.** Bloomberg "Adjusted EBITDA - Company Basis: Wind" is GEV segment EBITDA. No acquisition effect in Wind (Prolec sits in Electrification). Calendar fiscal year.
2. **Onshore line does not tie.** Street onshore (6,873) + offshore (795) = 7,668, not 7,589. The sub-lines come from a different set of contributors. The candidate's 6,794 is a subtraction, not a Street figure. Effect on onshore EBITDA at 4-7%: +3 to +6. Immaterial.
3. **Thin and skewed sample.** `06_modl.xlsx` for 3Q26 Wind adjusted EBITDA: mean 24.6, median 0.6, low -9, high 106.4. Those four statistics fit about four contributors with one high outlier. No count, high, low or median is available for any 2027 Wind quarter. The "+188" may be the mean of three to five models.

## 2. Company side, recomputed from filings

| Item | Value | Source | Candidate | Match |
|---|---|---|---|---|
| Wind segment EBITDA 1Q24..4Q24 | -173, -117, -317, +19 = -588 | XBRL, `data/financials/gev_segments.csv` | -588 | yes |
| 1Q25..4Q25 | -146, -165, -61, -225 = -597 (FY reported -598) | same | -598 | yes |
| 1Q26, 2Q26 | -382, -275 = -657 | 10-Q 0001996810-26-000148 | -657 | yes |
| H1 EBITDA / revenue | 2024: -290 / 3,701; 2025: -311 / 4,095; 2026: -657 / 3,458 | same | -290, -312, -657; 3,701, 4,095, 3,459 | yes (rounding) |
| Onshore revenue | 2024: 7,781 (+LM 542 = 8,323); 2025: 8,241 (+LM 217 = 8,458) | 10-K 0001996810-26-000015 | same | yes |
| Offshore revenue | 2024: 1,377; 2025: 652; 1Q26 246; 2Q26 305 | same; 10-Qs | n/a | n/a |
| Offshore incremental contract losses | 2023 $379M; 2024 $1,005M; 2025 $637M | 10-K 0001996810-26-000015, revenue-recognition note | same | yes |
| By period | H1'24 103; 3Q24 676; 4Q24 226; H1'25 125; 3Q25 171; 4Q25 341 | 10-Q 0001996810-25-000160 ($171M / $676M quarter; $296M / $779M nine months) | n/a | n/a |
| 2026 10-Qs | no dollar figure; "higher contract losses" (1Q), same wording for six months (2Q) | 0001996810-26-000064; -26-000148 | "continued in H1 2026" | yes, amount undisclosed |
| FY26 Wind guide | about -$400M, reaffirmed 2026-07-22; 3Q26 "approximately break-even" | 2Q26 call transcript (corpus source 3161) | same | yes |
| Guide-implied 4Q26 | -400 + 657 - 0 = +257 | arithmetic | n/a | n/a |

Quoted passages:
- 10-K 2025 (0001996810-26-000015): "we recorded incremental contract losses for certain Offshore Wind contracts of $637 million, $1,005 million, and $379 million, respectively."
- 10-Q 2Q26 (0001996810-26-000148), six months: "Segment EBITDA decreased $0.3 billion organically*, primarily at Onshore Wind due to lower equipment deliveries and the impact of tariffs, and at Offshore Wind due to higher contract losses, partially offset by lower costs at Onshore Wind services."
- Investor update transcript 2025-12-09, p.7: "In Onshore Wind, we expect lower profitability year over year at mid-single digit margins ... in Offshore Wind, we expect to deliver higher revenue in 2026 with slightly less EBITDA losses".
- Same, pp.8-9: "the remaining portion of the Dogger Bank project in 2026 and 2027. As we reduce the existing Offshore backlog, we expect EBITDA losses to improve."
- 2024 annual report letter and proxy (0001996810-25-000049): "Onshore delivering high single digit EBITDA margin in 2024". The candidate's "about 7%" (January 2025 call) is not in the corpus; it is consistent with this wording but not verified here.
- Conference transcript 2026-09-16 (CEO): "we're reaching a profitability pivot point in Wind ... '27 will be much better than '26"; later, "the profitability of our Wind segment will be drastically better, going forward."

## 3. Proof steps, recomputed

| Step | Candidate | Recomputed | Note |
|---|---|---|---|
| 2. Offshore EBITDA 2024 | -1,133 to -1,171 | -588 - (545 to 583) = -1,133 to -1,171 | match |
| 2. Offshore 2025 | -1,190 to -1,280 | -598 - (592 to 677) = -1,190 to -1,275 | rounding |
| 2. Offshore 2026 guide | -690 to -830 | -400 - (290 to 435) = -690 to -835 | rounding |
| 3. Opening offshore backlog | ~$4B, ~$3B, ~$2B | slide 19 labels ~$4B, ~$3B, ~$2B for YE2023, YE2024, YE2025E. Bar heights in the PDF are 226.0 / 149.0 / 102.7 / 51.4 points = **4.4 / 2.9 / 2.0 / 1.0** | YE2026E bar has no label; height implies ~$1.0B |
| 3. Loss / opening backlog | 28-29%, 40-43%, 35-42% | with bar heights: 26-27%, 41-44%, 35-42% | band widens to 26-44% |
| 4. Onshore 2027 at 4/5/6/7% | 272 / 340 / 408 / 476 | on 6,794: same. On Street onshore 6,873: 275 / 344 / 412 / 481 | match |
| 5. Offshore 2027 loss | 280 to 600; central 407 | 26-44% x $1.0-1.4B = 260 to 616; 36% x 1.2B = 432 | slightly wider |
| 6. Wind 2027 | -328 / -67 / +196 | **-344 / about -60 / +221** | Street +188 inside |
| 7. Street-implied offshore loss | 84 to 220 | 188 - (272 to 408) = 84 to 220; at 7% onshore: 288 | match |

Opening 2027 offshore backlog cross-check: YE2024 2.9B - 2025 offshore revenue 0.652B - Street 2026 offshore revenue 0.885B = about 1.36B. Company chart (December 2025): about 1.0B. Street offshore revenue 2027-2030 sums to 1,390. Range $1.0-1.4B holds.

## 4. Error band

1. **Out-of-sample test of the method.** Apply it one year earlier with what was known in December 2025: onshore 4-6% x 7,257 = 290 to 435; offshore 26-44% x $2.0-2.25B = 520 to 990. Wind 2026 = -700 to -85. Guide -400, Street -449. The method brackets the answer with a band of about +/- $300M. The same width applies to 2027.
2. **Corrected 2027 range: -344 to +221, half-width about $280M. Gap to Street at the central case: about -$250M.** Band is larger than the gap. Street is inside the range.
3. **The ratio has no mechanical basis.** Offshore losses in 2024 and 2025 were mostly estimate-change charges ($1,005M and $637M). Under loss-contract accounting the full expected loss is booked when estimated; later revenue on a provided contract carries no margin. Backing the charges out (and the $300M 3Q24 gain):

| | 2024 | 2025 |
|---|---|---|
| Segment EBITDA before offshore charges | -588 + 1,005 - 300 = +117 | -598 + 637 = +39 |
| Less onshore (7% / 7-8%) | 545 to 583 | 592 to 677 |
| Offshore running loss before charges | -428 to -466 | -553 to -638 |

   The Street-implied 2027 offshore loss (84 to 220) is 50-85% below that running loss, with no new charge. That is the cleanest statement of what the Street needs. It is not a proof that the Street is wrong: the running loss is itself a residual of an onshore margin that is only spoken, never filed.

4. **Second method (half-year bridge), same data.**

| | H1 EBITDA before offshore charges | H1 revenue | margin | H2 before charges | H2 revenue | margin |
|---|---|---|---|---|---|---|
| 2024 | -290 + 103 = -187 | 3,701 | -5.1% | 59 + 245 = +304 | 5,500 ex settlement | 5.5% |
| 2025 | -311 + 125 = -186 | 4,095 | -4.5% | 110 + 116 = +226 | 5,015 | 4.5% |
| 2026 | -657 reported (charge undisclosed) | 3,458 | -19.0% | guide-implied +257; Street +208 | 4,685 | 5.5% / 4.4% |
| 2027 Street | -21 | 3,388 | -0.6% | +209 | 4,200 | 5.0% |

   - H2 2027: 4.4-5.5% x 4,200 = 185 to 231. Street 209. No gap.
   - H1 2027: -4.5% to -5.1% x 3,388 = -152 to -173 before any charge. Street -21. Gap -130 to -155 before charges.
   - FY27 by this method: +12 to +79 before charges and before any structural improvement; lower by any 2027 offshore charge (H1 charges were 103, 125 and an undisclosed larger amount in 2024-2026).
   - Street H1 2027 equipment revenue 2,278 is flat on H1 2026 actual 2,284, while Street EBITDA moves from -657 to -21.
   - Offsets the method cannot size: onshore services margin gains (three quarters of "significant margin expansion"), tariff protection on newer orders (1Q26 tariff cost about $70M), G&A cuts, smaller offshore organisation.
   - The two methods give central values of about -60 and about +45. They agree on direction (below the Street) and disagree by about $100M on size.

## 5. Evidence for and against (facts only)

For the direction:
- Initial Wind guides against outcomes: 2024 "approaching profitability" (8-K exhibits 2024-04-25, 2024-07-24) against -588; 2025 "$200-$400 million of segment EBITDA losses" (8-K exhibit 2025-01-22) against -598.
- Offshore charges were booked in every year 2023-2025 and again in 1Q26 and 2Q26.
- Dogger Bank B and C continue through most of 2027; Street offshore revenue 795 in 2027 against 885 in 2026.

Against:
- CEO on 2026-09-16: "profitability pivot point", "'27 will be much better than '26", "drastically better". Both -60 and +188 are "much better" than -400, but "pivot point" reads as a positive year.
- Guide-implied 4Q26 of about +257 and 3Q26 break-even, with offshore still in execution.
- 2028 target of 6% on a smaller revenue base (about 6.0-6.6B) is roughly +360 to +400; Street 2028 is 373. A path of -400, +188, +373 is a straight line, as the candidate says, but the company's own end point supports it.
- Vineyard Wind settlement (2026-09-16), terms confidential, removes one open exposure; sign of the 3Q26 effect unknown.
- Street FY26 (-449) is already below the guide (-400): the Street is not simply copying management on this line.

## 6. Result against the survival test

| Test | Result |
|---|---|
| Numbers reproduce from primary files | Yes, within rounding. Corrections: backlog bars 4.4 / 2.9 / 2.0 / 1.0; ratio band 26-44%; 2025 offshore -1,275 not -1,280; Street onshore line 6,873 |
| Same definition, period, units | Yes (segment EBITDA, calendar FY2027, $M) |
| Gap at least about 5% | On the line: -132% of a near-zero base (not meaningful). On company FY27 adjusted EBITDA: -2.6% central. Fails the 5% level at company scale |
| Gap larger than error band | **No.** Gap about $250M; band about +/- $280M; Street inside the range |
| Checkable in seconds from public data | No. Rests on spoken margin comments, one chart with an unlabeled bar, and two undisclosed figures (H1 2026 offshore charge; mid-2026 offshore backlog) |

Reveal dates confirmed: 3Q26 results 2026-10-28 (Wind against Street +24.6 mean, +0.6 median; guide break-even); January 2027 call (FY27 outlook, per the 2026-09-16 transcript); FY26 10-K (2026 offshore incremental loss).

Files: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01..05-eeo-company-specific.xlsx`; `data/bloomberg/street_segments_annual_2026-10-01.csv`; `data/financials/gev_segments.csv`; `data/gev.db` (accessions above; sources 1844, 2660, 3161, 3663, 3796); investor update slides and transcript 2025-12-09 (gevernova.com).
