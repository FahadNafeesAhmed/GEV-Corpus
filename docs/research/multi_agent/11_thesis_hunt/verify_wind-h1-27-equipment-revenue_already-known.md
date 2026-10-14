# Verify (ALREADY KNOWN / BAD DATA): candidate `wind-h1-27-equipment-revenue`

_AI-assisted research input only: facts, arithmetic, tables, sources. No memo sentences, no forecast choices. Bloomberg figures cited as "Bloomberg, 2026-10-01"; keep inside the project folder._

**Verdict: does NOT survive.** The numbers reproduce, but (1) the reason given for why the market missed it is factually wrong, (2) with the company's reported order figures the Street sits inside the observed range, (3) the method failed its only out-of-sample test by 34-44%, (4) the Street figure is a thin sub-line, and (5) the mechanism is stated by management on every call. Usable only as a small model input.

## 1. Street side (Bloomberg, 2026-10-01)

Source: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `01-eeo-company-specific.xlsx` row 27, `06_modl.xlsx`, `01_eeo_annual.xlsx`.

| Line | 1Q27 | 2Q27 | H1 2027 | H1 2026 actual |
|---|---|---|---|---|
| Wind equipment revenue | 1,019 | 1,259 | **2,278** | 2,284 |
| Wind services revenue | 483 | 573 | 1,056 | 1,175 |
| Wind segment revenue | 1,522 | 1,866 | 3,388 | 3,459 |
| Offshore revenue | 178 | 212 | 390 | 551 |
| Wind MW delivered | 694 | 1,188 | 1,882 | 2.0 GW (10-Q) |
| Wind orders (equipment + services) | 1,180 | 1,296 | 2,476 | 2,448 |

Candidate figures match. Problems with the Street figure:

1. **No contributor count.** Company revenue for 1Q27 and 2Q27 has 22 analysts (`01_eeo_annual.xlsx`). The Wind sub-lines carry no count on any export, and individual broker cells are blank on `06_modl.xlsx`.
2. **Wide spread on the nearest quarter.** 3Q26 Wind equipment: mean 1,789, median 1,813, low 1,274, high 2,244 (-29% / +25% around the mean). 3Q26 Wind services: low 392, high 1,043 (median 499); the high looks like one broker with a different equipment/services split. No low/high is available for 1Q27 or 2Q27. The candidate's gap (-11% to -35%) is inside the broker spread one quarter out.
3. **Sub-lines do not tie.** H1 2027: equipment + services = 3,334 against Wind 3,388 (-54). Onshore + offshore = 3,263 against 3,388 (-125). Different broker sets feed each line.
4. **Services split looks stale.** Street Wind services H1 2027 is 1,056, 10% below H1 2026 actual 1,175, while reported services grew 20% (1Q26) and 39% (2Q26) organically. Wind total less services held at the H1 2026 actual gives equipment of 2,213, not 2,278.
5. **Street orders and Street revenue disagree.** FY27 Street Wind orders 5,678 less services about 2,092 leaves about 3,586 of equipment orders against Street equipment revenue 5,363.
6. **MW line cannot be tied to the company's definition.** Bloomberg shows no reported actual for 2Q26. Street H1 2027 onshore equipment per MW is $1.00M; H1 2026 orders were booked at $1.22M per MW ($1,460M / 1.2 GW). The "GW sold / GW ordered = 1.57, above every observation" step mixes a revenue line and a MW line from different brokers. At the order price the same Street revenue is about 1.55 GW, ratio 1.29.

Freshness of the company-level consensus is fine: most listed brokers updated on or after 2026-07-22 (workbook sheet `Bulk`). Sub-line freshness is not visible.

## 2. "Why missed" is wrong: Wind equipment orders in dollars are published

The candidate says GEV does not publish Wind equipment orders in dollars, so they must be derived from RPO change plus revenue. The 10-Q does not show them. **The earnings deck does, every quarter, on the page "Wind: key performance metrics".**

| Half | Reported Wind equipment orders $M | Derived figure (RPO change + revenue); candidate's in brackets | Difference |
|---|---|---|---|
| H1 2024 | 2,518 | 2,338 (2,325) | -7% |
| H2 2024 | 2,929 | 2,720 (2,704) | -7% |
| H1 2025 | 1,816 | 2,220 (2,203) | **+22%** |
| H2 2025 | 3,656 | 3,423 (3,413) | -6% |
| H1 2026 | **1,460** | 1,369 (1,368) | -6% |

Sources: decks of 2025-01-22 (FY24 5,447), 2025-07-23 (H1 2024 2,518; H1 2025 1,816), 2026-01-28 (FY25 5,472), 2026-07-22 (H1 2026 1,460, "(19)%" organic; corpus source 3157). All on gevernova.com; the three earlier decks were read from the PDFs on 2026-10-01.

- Reported H1 2026 equipment orders fell **20% (19% organic)** against H1 2025, not 33-44%. The 33% and 44% are GW and units (1.2 GW / 342 units against 1.8 GW / 609 units; 10-Q 0001996810-26-000148). Dollars per MW ordered rose from $1.01M to $1.22M.
- The derived series is off by -7% to +22% per half (currency and contract changes). On the derived series H1 2026 is -38%; on the reported series -20%.

## 3. The proof redone with reported orders

k = (Wind equipment revenue - offshore revenue) / reported equipment orders two halves earlier.

| Half | Equipment revenue | Offshore revenue | Orders two halves earlier | k (reported orders) | k (candidate) |
|---|---|---|---|---|---|
| H1 2025 | 3,209 | 430 | 2,518 | 1.10 | 1.19 |
| H2 2025 | 4,042 | 222 | 2,929 | 1.30 | 1.41 |
| H1 2026 | 2,284 | 551 | 1,816 | 0.95 | 0.79 |
| H2 2026 Street | 3,552 | 334 | 3,656 | 0.88 | 0.94 |
| H1 2027 Street | 2,278 | 390 | 1,460 | **1.29** | 1.38 |

- Street H1 2027 needs k = 1.29. Observed range 0.95 to 1.30. **The Street is inside the range**, at the top.
- H1 2027 equipment = 1,460 x k + 390: 1,783 (k 0.95), 2,001 (k 1.10), 2,294 (k 1.30). Against 2,278: **-22% to +1%**, -12% at the middle observation.
- Second method, H1 share of a June-to-June window: 38.4% (window from 6/30/24), 36.1% (from 6/30/25), Street 39.1%. Holding Street H2 2026 at 3,552: H1 2027 = 2,007 to 2,215, which is -12% to -3%.

## 4. Out-of-sample test of the candidate's method

Apply it one year earlier, with what was known at 12/31/2025 (two observations of k).

| Inputs | Predicted H1 2026 onshore equipment | Actual | Miss |
|---|---|---|---|
| Derived orders: 2,220 x 1.19 to 1.40 | 2,639 to 3,118 | 1,733 | **-34% to -44%** |
| Reported orders: 1,816 x 1.10 to 1.30 | 2,004 to 2,368 | 1,733 | -14% to -27% |

The candidate's ratio moved from 1.41 to 0.79 in one half-year. The method's error is larger than the gap it claims.

## 5. Already stated by the company, and visible in the Street

- 2Q26 call (2026-07-22, corpus source 3161): lower onshore deliveries were "a result of soft orders in the first half of 2025"; 70% of 2025 equipment orders came in the second half and deliver in the second half of 2026. The same wording is in the 1Q26 and 2Q26 releases and in the 4Q25 call (2026-01-28, corpus source 2660: only 30% of expected 2026 onshore turbine shipments in the first half).
- 3Q25 call (2025-10-22, corpus source 3796): permitting delays and tariff uncertainty would likely weigh on 2026 onshore revenue. Reuters carried it the same day.
- Multi-year outlook (release of 2026-01-28, corpus source 671): Wind organic revenue down low-double digits CAGR through 2028, 2025 base. At -10% to -13% a year: 2027 = 6,895 to 7,379; 2028 = 5,999 to 6,641. Street FY27 Wind revenue 7,589 is 3% to 10% above that path; FY28 6,813 is 3% above the top. The direction of the candidate is the company's own published outlook.
- 4Q25 call: the company projects a smaller onshore backlog given soft U.S. orders.
- Conference 2026-09-16 (company transcript, pp. 9-10): second-half onshore orders "materially larger" than the first half; no different orders dynamic in 3Q; no inflection close.
- The Street already has the sign by quarter: 1Q27 equipment +15% on 1Q26 (1Q26 orders $739M against $202M a year earlier), 2Q27 -10% (2Q26 orders $721M against $1,614M). Street organic growth line: 1Q27 +3.3%, 2Q27 -8.9%, 3Q27 -7.7%, 4Q27 -9.2%.
- No broker note or article stating a number for H1 2027 Wind equipment revenue was found (Exa and web search, 2026-10-01). The specific number is not published; the mechanism and the inputs are.

## 6. Has the stock moved on it

- 2026-07-22: close 985.03 against 1,078.81 (-8.7%); Reuters led with the EBITDA miss caused by wider Wind losses, and Wind orders down about 40%. Wind weakness was the headline.
- 2025-10-22: -1.6% on the close (Reuters reported a larger intraday fall on the Wind warning).
- Size of this candidate after correction: $0 to $0.5B of revenue on Street H1 2027 company revenue of 24,111 (0% to 2%); at an assumed 10-20% contribution, $0 to $100M on Street H1 2027 EBITDA of 4,038 (0% to 2.5%). Not a line the stock trades on at 28.5x EBITDA.

## 7. Ordinary explanations that close the gap

1. **Backlog covers it.** Wind equipment RPO 8,197 less offshore backlog about 1.45-1.8B (December 2025 investor update slide 19, chart-read, less H1 2026 offshore revenue) leaves onshore equipment RPO of about 6.4-6.7B. Street onshore equipment for 3Q26-2Q27 is 5,106 = 76-80% of it. Reported onshore-only conversion: 71.7% (12/31/23), 77.0% (6/30/24), 84.4% (12/31/24), 76.5% (6/30/25). Street is inside the range. The candidate's step 6 used the blended ratio (71.1% against 58.7-67.6%), which history understates because offshore backlog converts slowly. The Wind-lens working file (`propose_wind.md`, T2) reached the same result and marked this line "no candidate".
2. **Second-half 2026 orders.** Management guides them materially larger than H1; Street H2 2026 Wind orders are 3,271 against 2,448 in H1. Orders booked in 3Q26 can ship by 2Q27 (1Q26 onshore equipment revenue of 643 followed 1Q25 orders of 202, so the lag is not a fixed four quarters).
3. **Easy first-quarter base.** 1Q26 equipment revenue (889) was the trough that followed the 0.1 GW order quarter of 1Q25.
4. **Price and mix.** Dollars per MW ordered rose about 20% year on year, so GW understates the dollar order book.
5. **4Q25 orders.** $2,436M of equipment orders in 4Q25, the largest quarter of 2025, primarily outside North America (4Q25 call); international projects can carry longer delivery schedules, part of which may fall in 2027. Not quantified in any filing.
6. Not found: any acquisition, reclassification or currency effect that would explain it. LM Wind Power is folded into Onshore from 2026 in both periods.

## 8. Result against the survival test

| Test | Result |
|---|---|
| Street figure solid | **No.** Sub-line, no count, lines do not tie, 3Q26 broker range -29% / +25%, services split stale |
| Idea not already stated | **No.** Order-to-delivery lag stated by management each quarter; equipment orders in dollars published each quarter; multi-year decline guided |
| No ordinary explanation | **No.** Backlog coverage inside the reported range; reported orders put the Street inside the observed ratio range |
| Numbers reproduce | Yes (Street side and candidate arithmetic). Corrections: reported H1 2026 equipment orders 1,460 not 1,368; order decline 20% in dollars; Street-needed k 1.29 not 1.38; range -22% to +1% not -35% to -11% |
| Gap larger than error band | No. Middle gap about -12%; band about +/-13% on the range, and the one back-test missed by 14-44% |

What can still be used: the reported equipment-order series (section 2) and the onshore-only backlog conversion (section 7.1) as inputs to a Wind revenue tab. The point made for the first candidate, that Wind cannot absorb the company-level schedule gap, still holds: Street Wind conversion is at or above history on either lens.

Early read: 2026-10-28, 3Q26 deck "Wind: key performance metrics" (equipment orders $M; equipment RPO against 8,197) and the 10-Q units table.

Files: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `01-eeo-company-specific.xlsx`, `06_modl.xlsx`, `01_eeo_annual.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Bulk); `data/financials/gev_segments.csv`; `data/gev.db` (10-Q 0001996810-26-000148; sources 671, 2660, 3157, 3161, 3796; prices); gevernova.com decks 2025-01-22, 2025-07-23, 2026-01-28 and conference transcript 2026-09-16.
