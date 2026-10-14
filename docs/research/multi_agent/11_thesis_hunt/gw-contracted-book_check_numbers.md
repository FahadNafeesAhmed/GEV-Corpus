# Check (recompute and back-test): gw-contracted-book

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast is chosen for the team; every value is a range with its method. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Checked file: `gw-contracted-book.md` (same folder). Check type: redo every number from the primary files, re-run the back-test on every window, test the six kill reasons one by one.

Words used. **Haircut (k)** = reported Power equipment revenue divided by the book dollars of the gigawatts shipped. **Book** = firm backlog layers in order-date sequence, then reservations at a price P per kW. **Path A** = the July output plan (53 GW shipped by end-2028, 109 GW by end-2030).

## 0. Verdict

| Item | Result |
|---|---|
| Arithmetic reproduces from primary files | Yes. Every table re-derived; three small slips (section 5) |
| Rebuild's own verdict | Does not hold. Confirmed |
| Survival test (gap at least 7% and clearly larger than its error band) | **Fails in every window** |
| Headline window (Q3 2026 to Q4 2030), Street | $76,256M (Bloomberg, 2026-10-01) |
| Rebuild gap / band, headline window | +7.0% / +/-9.1% |
| Corrected gap / band, headline window | **+3.8% (range +2.2% to +7.0%) / +/-10.3% (+/-11.9% with the wide haircut range)** |
| Best window (to end-2029) | Rebuild +9.8% vs +/-9.1%. Corrected +6.5% (range +5.6% to +9.8%) vs +/-10.3% |
| Kill reasons answered | None fully. 1, 4, 5, 6 not answered. 2 partly. 3 improved less than stated |
| Usable as | Exhibit (consensus in physical terms; coverage) and model structure. Not a thesis. Not evidence of a gap |

Why the corrected gap is smaller than the rebuild's:
1. The rebuild uses a haircut of 0.918 for the 10-quarter window and 0.955 for the longer ones. That switch alone is 4.1 of the 7.0 points in the headline window. With one haircut for all windows the headline gap is +2.9% (0.918) to +3.8% (0.926, all 16 windows of 8 quarters or more).
2. The 0.955 rests on three 12-quarter windows and one 14-quarter window. They are not separate observations: the dollar miss of every long window depends only on its end quarter (section 2b). They are the last three points of one series, read while it was closing.
3. The contracted book alone (by class, no orders that are not yet signed) gives +2.2% in the headline window at the rebuild's own haircut.

## 1. Inputs recomputed

| Item | Rebuild | Recomputed | Source | Match |
|---|---|---|---|---|
| Street Power equipment, cumulative to end-2028 / 2029 / 2030 / Q2 2031, $M | 33,530 / 52,786 / 76,256 / 88,596 | 33,530 / 52,786 / 76,256 / 88,596 | `segment_quarterly.json`, key `Total Revenue\|Power\|Equipment` (Bloomberg, 2026-10-01) | yes |
| Street by period H2 26 / 27 / 28 / 29 / 30 / H1 31 | 5,491 / 12,151 / 15,888 / 19,256 / 23,469 / 12,340 | same | same | yes |
| Equipment + services less Power total | -8, -295, +33, -555, +611, 0 | same | same | yes |
| Street Power RPO line less (RPO + orders - revenue) | +2.0, +0.2, -4.4, +10.2, +9.2, -17.7 $B | +1.97, +0.24, -4.43, +10.22, +9.24, -17.69 | same | yes |
| Q3 2026 Power equipment mean / low / high / median | 2,394 / 2,063 / 2,591 / 2,433 | same | `06_modl.xlsx` | yes |
| Annual EBITDA estimate counts 2026-2030 | 35 / 36 / 33 / 21 / 20 | same | workbook sheet Consensus | yes |
| 14 quarters of GW sold, GW ordered, units by class, Power equipment revenue, Power equipment RPO | table 1b | all 14 rows re-read from the ten filings | 10-Q / 10-K Power tables in `gev.db` (accessions in the rebuild) | yes |
| Power equipment RPO 12/31/22 | 13,579 | 13,579 | 10-K 2024 | yes |
| EDF item | $3.9B in Q2 2024 | "approximately $3.9 billion" | 10-Q Q2 2024 | yes |
| Order dollars and $/kW by quarter | 693 ... 1,049 | same (Q4 25 753, Q1 26 705, Q2 26 1,049, H1 26 916) | change in RPO + revenue | yes |
| Firm backlog / reservations by quarter | 29/21, 29/25, 33/29, 40/43, 44/56, 53/63 | same | 8-K exhibits 99.1 | yes |
| RPO schedule 6/30/26 | 87,821; 36 / 65 / 97% | same; 31,616 / 57,084 / 85,186 | 10-Q Q2 2026 | yes |
| RPO schedules 12/31/23 to 3/31/26 | table 6 | all ten sentences found and matched | S-1, 10-Qs, 10-Ks | yes |
| Consolidated equipment revenue by quarter | table 6 sums | 8-quarter sums 39,886 / 41,523 / 43,788 | `gev_segments.csv` (Product) | yes |
| Prolec equipment revenue Q1 / Q2 2026 | 469 / 834 | 469 / 834 ("Less: Acquisitions" line) | 10-Q Q1 and Q2 2026 | yes |
| Street 8-quarter equipment, three divisions | 24,740 + 10,796 + 29,845 = 65,382 | same | Bloomberg, 2026-10-01 | yes |
| Output ladder (5, then 6, then 7 GW a quarter) | quoted | found verbatim | company transcript PDF, 2026-09-16, gevernova.com | yes |
| "130 machines running ... 195 more on contract" | quoted | found verbatim (HA units) | same | yes |
| Class price estimate 790 / 950 / 1,800 per kW | quoted | found | corpus source 301 | yes |
| GW per unit regression | HA 0.435, other heavy-duty 0.17, aero about 0 | 0.435 / 0.173 / -0.003, R2 0.97 | 28 observations | yes |
| Aeroderivative orders less sales since end-2021 | +130 units | +130 | 10-K / 10-Q tables | yes |
| Gap table 4a (36 cells), ranges, break-even output, error table 4b | section 4 | all cells reproduced | script in section 7 | yes |
| By-class contracted values (16 aero a quarter) | 38,761 / 58,758 / 81,660 / 91,131 | 38,697 / 58,702 / 81,604 / 91,075 | own build from the rebuild's stated inputs | yes (0.1-0.2%) |
| Profit effect | 1.6-2.8% of cumulative company EBITDA; 4-11% at 60-90% drop-through | 1.6-2.8%; 4.0-11.0% | Street margins 21.8-24.3% | yes |

## 2. Back-test, re-run on every window

Data: 14 quarters, Q1 2023 to Q2 2026. Method as in the rebuild: opening layer = firm GW and equipment RPO at the start date (less $3.9B before Q2 2024); each quarter adds a layer (GW ordered, order dollars); ship the reported GW oldest first; compare reported revenue with layer dollars shipped.

### 2a. Results by form

| Form | 4 quarters | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|---|
| Restart at each date (rebuild table): windows | 11 | 9 | 7 | 5 | 3 | 1 |
| min / max | 0.79 / 0.99 | 0.81 / 1.03 | 0.85 / 0.96 | 0.87 / 0.97 | 0.93 / 0.97 | 0.98 |
| mean (s.d.) | 0.906 (0.062) | 0.916 (0.071) | 0.913 (0.043) | 0.918 (0.041) | 0.952 (0.021) | 0.977 |
| One continuous stack: min / max | 0.73 / 1.26 | | 0.87 / 0.99 | 0.87 / 1.00 | 0.93 / 0.99 | 0.98 |
| mean (s.d.) | 0.967 (0.150) | | 0.930 (0.042) | 0.935 (0.049) | 0.964 (0.030) | 0.977 |
| Restart, backlog anchored at 52.2 GW instead of 53.0: mean | 0.873 | | 0.890 | 0.900 | 0.936 | 0.961 |

- Single quarters (continuous form): 0.51 to 1.92.
- Calendar years (continuous form): 0.91 / 0.95 / 0.94; H1 2026 1.27.
- Cycle form (revenue while the opening backlog GW ships, over opening RPO), starts Q1 2023 to Q4 2024: 1.01, 0.94, 0.91, 0.94, 0.82, 0.81, 0.86, 0.92. Mean 0.901. Each cycle 5.5 to 7.2 quarters.
- All 16 restart windows of 8 quarters or more pooled: min 0.85, max 0.98, mean 0.926, median 0.932.
- All of the above match the rebuild.
- Anchor note. Rolling the filed GW back from 53.0 gives 29.9 / 29.8 / 33.2 / 40.3 / 44.2 against disclosed 29 / 29 / 33 / 40 / 44. Disclosed backlog is rounded to whole GW, so the anchor is uncertain by about 0.8 GW. That moves the haircut by about 2 points.

### 2b. What the long windows actually measure

Dollar miss (reported revenue less layer dollars shipped), by the quarter in which the window ends:

| Window ends | Q4 24 | Q1 25 | Q2 25 | Q3 25 | Q4 25 | Q1 26 | Q2 26 |
|---|---|---|---|---|---|---|---|
| 6-quarter windows, $M | -901 | -544 | -2,072 | -1,981 | -1,324 | -933 | -477 |
| 8-quarter windows | -885 | -596 | -2,072 | -1,981 | -1,324 | -954 | -517 |
| 10-quarter windows | | | -2,072 | -1,981 | -1,324 | -954 | -517 |
| 12-quarter windows | | | | | -1,324 | -954 | -517 |
| 14-quarter window | | | | | | | -517 |

- Once the opening backlog has shipped (about six quarters), the miss is the same whatever the start date. Arithmetic reason: miss = layer dollars still in the stack less reported RPO at the end date. Both sides share opening RPO plus all later orders.
- So the long-window "sample" is one series of seven quarter-end values. The 12- and 14-quarter windows are its last three points (-1,324, -954, -517), taken while the miss was closing.
- The ratio moves towards 1 as the window lengthens because the shared base grows, not because the method predicts better. The rebuild says "about one and a half independent observations"; one is closer.

### 2c. Placebo: does the back-test confirm order-date sequence?

Same test, same data, different shipping rule:

| Rule | 4 quarters | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|
| Oldest first (the method) | 0.79-0.99 | 0.85-0.96 | 0.87-0.97 | 0.93-0.97 | 0.98 |
| Average backlog price (no sequence at all) | 0.82-0.99 | 0.88-0.96 | 0.90-0.93 | 0.91-0.93 | 0.92 |
| Newest first (the opposite) | 0.68-1.13 | 0.80-0.98 | 0.83-0.90 | 0.85-0.87 | 0.83 |

- A rule with no sequence gives a tighter 10-quarter range (0.90-0.93) than the method (0.87-0.97), and the same mean (0.91).
- The opposite rule still lands at 0.80-0.98 over eight quarters.
- The back-test therefore cannot tell which order layer fills which slot. That is the question kill reason 2 turns on.
- Under the average-price rule there is no step up at 12-14 quarters (0.92). The step up to 0.955 is specific to the oldest-first rule and the last three quarter ends.

### 2d. Forward-style test: the price of gigawatts beyond the firm backlog

The rebuild's back-test knows the actual GW shipped and the actual dollars of every later order. The forward calculation knows neither. Test of the price leg only: at date t, firm backlog as one layer; GW shipped beyond it priced at the trailing four-quarter all-in order price known at t; actual GW.

| Start | P at t, $/kW | Window | GW shipped (beyond firm backlog) | Predicted $M | Reported $M | Ratio | Ratio with later order dollars known (2a) |
|---|---|---|---|---|---|---|---|
| Q1 2024 | 589 | 8 quarters | 27.2 (9.7) | 15,450 | 12,393 | 0.80 | 0.90 |
| Q1 2024 | 589 | 10 quarters | 34.7 (17.2) | 19,868 | 16,243 | 0.82 | 0.97 |
| Q2 2024 | 494 | 8 quarters | 29.1 (9.0) | 14,936 | 13,077 | 0.88 | 0.93 |
| Q3 2024 | 469 | 8 quarters | 30.9 (8.2) | 14,821 | 13,757 | 0.93 | 0.96 |

- Four windows, overlapping. Ratio 0.80-0.93 against 0.90-0.97 when later order dollars are known. The price leg cost 3 to 15 points.
- Cause: the all-in order price swings with aeroderivative mix (834, 400, 431, 361 per kW in four consecutive quarters), so a recent all-in price is a poor guide to the next layers.
- Limit of this test: in 2024 there was no company commentary on reservation prices; today there is (10 to 20 points above Q4 2025 orders). It is the only test of this leg the data allow. In the headline window 56 of 109 GW (51%) come from this leg.

## 3. Corrected gap and error band

### 3a. Gap by haircut choice (path A, reservations at $825/kW)

| Haircut basis | to end-2028 | to end-2029 | to end-2030 | to Q2 2031 |
|---|---|---|---|---|
| Rebuild: 0.918 then 0.955 | +7.5% | +9.8% | +7.0% | +5.5% |
| One haircut, 10-quarter mean 0.918 | +7.5% | +5.6% | +2.9% | +1.4% |
| One haircut, pooled 8 quarters or more, 0.926 | +8.4% | +6.5% | +3.8% | +2.3% |
| Cycle form 0.901 (like for like to end-2028: path A ships exactly the opening backlog) | +5.5% | +3.6% | +1.0% | -0.5% |
| Anchor 52.2 GW: 0.900 then 0.936 | +5.4% | +7.7% | +4.9% | +3.4% |
| Contracted book by class, 16 aero a quarter, 0.955 | +10.2% | +6.2% | +2.2% | -1.8% |
| Same, 25 aero a quarter | +2.5% | -0.4% | -3.7% | -5.3% |

Book dollars before haircut (path A, $825): 39,261 / 60,711 / 85,461 / 97,836. Reproduced.

Extra item for the end-2028 window. Management says 2026 heavy-duty orders ship mostly in 2029-31. If the 17.8 GW of heavy-duty units ordered in H1 2026 (about $13.4B on the rebuild's class split) leave the window and 2025-vintage reservations at $650-780/kW heavy-duty-only take their slots, the end-2028 book moves by -$1.9B to +$0.5B (-$1.7B to +$0.4B after the 0.918 haircut): the +7.5% becomes +2.4% to +8.7%.

### 3b. Corrected centre and range

| Window | Street $M | Rebuild gap | Corrected centre (method) | Corrected range |
|---|---|---|---|---|
| to end-2028 | 33,530 | +7.5% | +5.5% (cycle-form haircut 0.901) | +2.4% to +8.7% |
| to end-2029 | 52,786 | +9.8% | +6.5% (pooled 0.926) | +5.6% to +9.8% |
| **to end-2030 (headline)** | **76,256** | **+7.0%** | **+3.8% (pooled 0.926)** | **+2.2% to +7.0%** |
| to Q2 2031 | 88,596 | +5.5% | +2.3% (pooled 0.926) | -1.8% to +5.5% |

The range is the spread of defensible haircut choices on path A at $825 only. It is not the full range across paths and prices (rebuild: -11% to +26%, reproduced).

### 3c. Error band

| Window | Haircut | Reservation price ($750-900) | Output path (half of B to C) | Total, in quadrature | With the wide haircut range (0.85-1.00) | Rebuild |
|---|---|---|---|---|---|---|
| to end-2028 | +/-5.4% | 0 | +/-9.5% | +/-11.0% | +/-12.5% | +/-11.0% |
| to end-2029 | +/-5.4% | +/-3.2% | +/-8.2% | +/-10.3% | +/-11.9% | +/-9.1% |
| to end-2030 | +/-5.4% | +/-4.9% | +/-7.2% | +/-10.3% | +/-11.9% | +/-9.1% |
| to Q2 2031 | +/-5.4% | +/-5.4% | +/-6.7% | +/-10.2% | +/-11.9% | +/-9.1% |

- Change from the rebuild: haircut error held at +/-5.4% for every window instead of dropping to +/-2.6%. Reason: section 2b (the tighter figure is three points of one series) and section 2c (no tightening under the average-price rule).
- Not in the band: the anchor (+/-2 points), the price-leg miss in section 2d (3 to 15 points, one direction), the noise in the Street figure itself (section 4, reason 5). Each would widen it.
- The output-path error is a judgement, not a back-test. Checks on it: GW sold in the last four quarters 4.0, 3.1, 4.2, 3.3 = 14.6; the plan needs 5.0 a quarter from Q3 2026, a 37% step. The one earlier output guide that can be tested ("over 10 gigawatts" in the last three quarters of 2025) was met at 12.3. The ramp date moved once, from mid-2026 to Q3 2026. Path C to end-2028 is 4 GW below path A; two more quarters at 3.3 GW instead of 5.0 GW would be 3.4 GW.

### 3d. Gap against band

| Window | Corrected gap | Corrected band | Gap at least 7%? | Gap clearly larger than band? |
|---|---|---|---|---|
| to end-2028 | +5.5% (+2.4 to +8.7) | +/-11.0% | no at the centre | no |
| to end-2029 | +6.5% (+5.6 to +9.8) | +/-10.3% | no at the centre | no |
| to end-2030 | +3.8% (+2.2 to +7.0) | +/-10.3% | no | no |
| to Q2 2031 | +2.3% (-1.8 to +5.5) | +/-10.2% | no | no |
| Company-wide, 2 years | +0.6% to +8.4% (mean fill +4.4%) | +/-4.5% | no at the centre | no |

Even on the rebuild's own figures no window passes (+7.5 / +9.8 / +7.0 / +5.5 against +/-11.0 / 9.1 / 9.1 / 9.1).

## 4. The six kill reasons, one by one

| # | Kill reason | Rebuild says | Check | Answered? |
|---|---|---|---|---|
| 1 | Rival explanation | Stands; extends to every window | Confirmed. Street = book x 0.854 / 0.869 / 0.892 / 0.906 (path A, $825). Three of the four sit inside the back-tested range of 0.85-0.98; the first is at its bottom edge. Or: plan output less 5% / 8% / 6% / 5%. Or: reservations at $725 (haircut 0.955) to $769 (0.926) to end-2030. Street cumulative per kW on path A is $633 / $668 / $700 / $714; the firm backlog average is $741. No gap is needed | **No.** Conceded, and correct to concede |
| 2 | Gap sat in the Q2 2026 layer | Partly answered; "the layer no longer drives the result" | Overstated. In the headline window the layer's dollars above $825/kW are $2,714M; x 0.955 = $2,591M = 48% of the +$5,360M centre gap. In the end-2028 window the layer is the whole gap (Street / book by year: 1.136, 0.873, 0.775, 0.898, 0.948, 0.997, reproduced). The placebo in 2c shows the back-test cannot place this layer in time | **Partly.** Diluted by the longer window, still about half of the centre gap |
| 3 | Error band (four-quarter misses of -27% to +25%) | Haircut error falls to +/-5% and +/-3%; total +/-9% to +/-12%; not cleared | Not cleared, and the improvement is smaller than stated. The +/-3% is three end-quarters of one series (2b). An average-price rule back-tests as well as the method (2c). With only time-t information the ratio was 0.80-0.93 (2d). Corrected band +/-10% to +/-12% against corrected gaps of +2% to +7% | **No** |
| 4 | Reveal date | Not answered; worse | Confirmed. Windows close with filings in February 2029, February 2030, February 2031, July 2031. Inside 12 months: Q3 2026 10-Q (2026-10-28), 10-K 2026 (late January 2027), capital markets day (spring 2027), Q2 2027 10-Q (late July 2027). All test inputs (GW sold, order price, RPO), none the named line. Threshold arithmetic reproduced: 39,261 + 20 GW x $838 - 5,491 = $50.5B; at $753 = $48.8B; Street's own H2 2026 orders imply $51.5-52.5B, so a result on guide confirms the Street | **No** |
| 5 | Thin, partly stale Street data | Not answered; worse | Confirmed. 21 and 20 annual EBITDA estimates for 2029-30 against 33-36 earlier. Equipment + services less total is exactly 0 in 2031 (one model). Street RPO line breaks +$10.2B (YE29) and -$17.7B (Q2 2031). Power organic growth is a flat 18.0 for 2027-28 and 9.0 for 2029-30. Nearest quarter spread on this line is -14% / +8%. A broker's published 2030 case (30 GW x about $900 = $27.0B) is already 15% above the mean ($23,469M) | **No** |
| 6 | Small profit effect | Stands | Confirmed. Centre gap $2.5-5.4B x Street cumulative Power margin (21.8-24.3%) = $0.5-1.3B = 1.6-2.8% of cumulative company EBITDA. On the corrected headline gap (+3.8% = $2.9B): about $0.7B, 1.1%. Nothing inside 12 months | **No** |

## 5. Slips found in the rebuild (none changes the verdict)

1. Table 1c, Q4 2025: the release states 21 GW of new reservations and 3 GW of direct orders ("Signed 24 gigawatts ... including 21 GW of slot reservation agreements and 3 GW of orders"). The rebuild shows 22 and 2, marked derived. The roll then gives 42 against the disclosed 43 (1 GW of rounding).
2. Source for "30 GW of shipments in 2030 at roughly $900 per kilowatt": the sentence is not in corpus source 3886 (that copy carries only the "$3,000 per kilowatt" whole-plant figure). It is in the original press article of the same title (thestreet.com, 2026-07-22), confirmed by web search on 2026-10-01. Cite that, not 3886.
3. Quarterly GW ordered for 2023 sum to 9.6 against the 10-K's 9.5 (rounding). No effect.
4. Section 3 wording "about one and a half independent observations": section 2b shows one series; the 12-14 quarter haircut is not a separate reading.
5. Section 7, reason 2, "the layer no longer drives the result": it is 48% of the centre gap to end-2030.
6. Coverage line "firm RPO is 117% of the Street total to end-2028": the ratio is right (39,261 / 33,530). Two qualifiers belong next to it: $3-4B of that RPO is non-gas equipment, and management places 2026 heavy-duty orders mostly in 2029-31, so not all of it can land by end-2028.

## 6. What survives as usable material

| Item | Status | Condition |
|---|---|---|
| Street cumulative Power equipment revenue in physical terms ($/kW by year: 549, 608, 691, 741, 782, 823 on path A) | Reproduced | Label the output path as an assumption; the Street publishes no GW line |
| Street to end-2030 = firm backlog + 56 GW of reservations at $725-812/kW | Reproduced (725 at 0.955, 769 at 0.926, 812 at 0.90) | Show the haircut range with it |
| Coverage: firm RPO + 63 GW at $750-900 = 113-126% of Street to end-2030 | Reproduced (86,511-95,961 / 76,256) | Add the qualifiers in section 5, item 6 |
| Driver structure for a Power equipment line (GW by class x vintage price x haircut + non-gas) | Usable as structure | Haircut 0.85-0.98 for windows of 8 quarters or more; one value for all windows, not a step up; four-quarter windows stay at 0.79-0.99 (0.73-1.26 continuous) |
| Sensitivities to end-2030 | Reproduced: $50/kW on reservations = $2.7B; 0.01 of haircut = $0.85B; 1 GW = $0.8B; path C = -$7.1B | |
| Dated input checks (GW sold 5.0; order price $838 or $753; year-end RPO $50.5B or $48.8B) | Arithmetic reproduced | They test inputs and mostly confirm the Street |

What would change the verdict (company-reported): a delivery-year split of backlog and reservations; a disclosed reservation price; broker-level detail on the out-year division line; several more quarters at 5 GW or above.

## 7. Reproduce

Run from the `gev-corpus` folder. Prints sections 2a, 2b, 2c and the gap rows of 3a.

```python
import json, statistics as st
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
FQ = [f'{y} Q{q}' for y in range(2026, 2032) for q in range(1, 5)][2:22]
eq = [d[f'Total Revenue|Power|Equipment|{q}'] for q in FQ]
N = {'end-2028': 10, 'end-2029': 14, 'end-2030': 18, 'Q2 2031': 20}
S = {e: sum(eq[:n]) for e, n in N.items()}
# quarter: (GW sold, Power equipment revenue, GW ordered, Power equipment RPO at end), 10-Q / 10-K Power tables
Q = {'2023Q1': (3.6, 1180, 2.3, 13992), '2023Q2': (2.3, 1147, 2.1, 13980), '2023Q3': (2.7, 1291, 3.1, 13865), '2023Q4': (5.2, 1980, 2.1, 13636),
     '2024Q1': (2.3, 1201, 4.9, 14394), '2024Q2': (1.5, 1285, 4.1, 10978), '2024Q3': (3.3, 1426, 5.1, 11392), '2024Q4': (4.8, 1796, 6.1, 12461),
     '2025Q1': (3.0, 1491, 7.1, 13920), '2025Q2': (5.2, 1504, 5.1, 16133), '2025Q3': (4.0, 1744, 7.4, 18977), '2025Q4': (3.1, 1946, 10.2, 24707),
     '2026Q1': (4.2, 1885, 8.1, 28530), '2026Q2': (3.3, 1965, 12.1, 39261)}
K = sorted(Q); EDF = 3900; RPO0 = 13579
def setup(anchor):
    ords, orpo, ogw = {}, {}, {}
    g = anchor - sum(Q[k][2] for k in K) + sum(Q[k][0] for k in K); prev = RPO0
    for k in K:
        orpo[k], ogw[k] = prev, g
        ords[k] = Q[k][3] - prev + Q[k][1] + (EDF if k == '2024Q2' else 0)
        prev = Q[k][3]; g += Q[k][2] - Q[k][0]
    return ords, orpo, ogw
def run(i0, n, mode='fifo', anchor=53.0):
    ords, orpo, ogw = setup(anchor); k0 = K[i0]
    stack = [[ogw[k0], orpo[k0] - (EDF if k0 <= '2024Q2' else 0)]]; pred = act = 0.0
    for k in K[i0:i0 + n]:
        need = Q[k][0]
        if mode == 'avg':
            G = sum(s[0] for s in stack); U = sum(s[1] for s in stack); pred += U * need / G; stack = [[G - need, U - U * need / G]]
        else:
            while need > 1e-9:
                j = 0 if mode == 'fifo' else -1
                gq, u = stack[j]; t = min(gq, need); pred += u * t / gq
                stack[j] = [gq - t, u - u * t / gq]; need -= t
                if stack[j][0] < 1e-9: stack.pop(j)
        act += Q[k][1]; stack.append([Q[k][2], ords[k]])
    return act, pred
for mode, anchor in (('fifo', 53.0), ('fifo', 52.2), ('avg', 53.0), ('lifo', 53.0)):
    for n in (4, 6, 8, 10, 12, 14):
        r = [run(i, n, mode, anchor) for i in range(len(K) - n + 1)]; rr = [a / p for a, p in r]
        print(mode, anchor, n, 'min %.2f max %.2f mean %.3f' % (min(rr), max(rr), st.mean(rr)),
              '| miss by end quarter:', ' '.join('%s:%+.0f' % (K[i + n - 1], a - p) for i, (a, p) in enumerate(r)) if mode == 'fifo' and anchor == 53.0 else '')
pool = [a / p for n in (8, 10, 12, 14) for a, p in (run(i, n) for i in range(len(K) - n + 1))]
print('pooled 8+ quarters: n %d mean %.3f' % (len(pool), st.mean(pool)))
lay = [(3.0, 1926), (7.1, 2950), (5.1, 3717), (7.4, 4588), (10.2, 7676), (8.1, 5708), (12.1, 12696)]   # firm layers at 6/30/26
def book(gw, P=825):
    c, left = 0.0, gw
    for a, b in lay:
        t = min(a, left); c += b * t / a; left -= t
    return c + left * P
A = [5]*6 + [5.5, 5.5, 6, 6] + [6.5]*4 + [7.5]*6                                                     # July plan
for lab, kk in (('rebuild', (0.918, 0.955, 0.955, 0.955)), ('0.918', (0.918,)*4), ('pooled 0.926', (0.926,)*4), ('cycle 0.901', (0.901,)*4)):
    print(lab, ' '.join('%s %+.1f%%' % (e, 100 * (book(sum(A[:n])) * k / S[e] - 1)) for (e, n), k in zip(N.items(), kk)))
```

Other scripts (scratchpad, not kept): forward-style test of section 2d (firm backlog as one layer, GW beyond it at the trailing four-quarter order price), by-class build of section 3a (160 aero units, $8.6B; heavy-duty layers 29.7 GW at $463, 7.8 at $622, 10.0 at $858; non-gas $3.4B at $1.2B a year), error-band quadrature of section 3c.

Sources: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (sheet Consensus); `data/gev.db` documents for accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148, S-1 0001193125-24-066951, and the six earnings-release exhibits; `data/financials/gev_segments.csv`; corpus sources 3161, 301, 681, 3886, 288; company conference transcript PDF (gevernova.com, 2026-09-16), fetched 2026-10-01.
