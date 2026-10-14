# Check (ordinary explanation and already known): rebuild "gw-contracted-book"

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast is chosen for the team. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Words used here. **Haircut (k)** = revenue recognised divided by the book dollars of the gigawatts shipped (from the rebuild's back-test). **Reservation** = slot reservation agreement, a paid place in the queue that is not yet an order. **All-in $/kW** = Power equipment order dollars divided by gas GW ordered (includes aeroderivative units and non-gas equipment). **Heavy-duty-only $/kW** = the same with aeroderivative units and non-gas orders taken out.

## 0. Result

**Does not survive.** The rebuild itself reports "holds = false". This check confirms it and adds three reasons.

| Test | Result |
|---|---|
| Arithmetic reproduces from primary files | Yes. Street cumulatives, the back-test, and all 36 cells of the gap table match (section 1) |
| An ordinary reading removes the gap | Yes, in every window. Company-stated GW x order prices stepped along the company's own price statements x 0.90 gives the Street cumulative within +0.1% to +0.7% (section 2) |
| The central gap (+5.5% to +9.8%) is robust to input choice | No. About 6 points of it is the choice of haircut 0.955 over 0.90; about 3 to 7 points is the choice of $825/kW for reservations (section 3) |
| Gap larger than its error | No. Corrected centre to end-2030 about +1% against about +/-12% (section 3) |
| Street figure solid | No. No broker count; 56% of the end-2030 total comes from 2029-2030, where the feed is thinnest (section 4) |
| Idea not already published | No. Method, prices and the "sold out" coverage point are all public (section 5) |
| A company-reported number inside 12 months settles it | No. The named line prints February 2029 to July 2031. Inside 12 months only 12% to 32% of each window prints (section 6) |

Usable as: exhibit only (consensus in physical terms; coverage of the Street by the signed book). The driver structure in the rebuild's section 8 is also usable as model structure. Neither is a claim that the Street is wrong.

## 1. Reproduction

Recomputed with Python from `segment_quarterly.json` and the 10-Q / 10-K Power tables in `gev.db`.

| Item | Rebuild | Recomputed |
|---|---|---|
| Street Power equipment, cumulative from Q3 2026, $M: end-2028 / end-2029 / end-2030 / Q2 2031 | 33,530 / 52,786 / 76,256 / 88,596 | same (Bloomberg, 2026-10-01) |
| Street by period, $M: H2 2026 / 2027 / 2028 / 2029 / 2030 / H1 2031 | 5,491 / 12,151 / 15,888 / 19,256 / 23,469 / 12,340 | same |
| Q2 2026 Power table: GW ordered 12.1, GW sold 3.3, units ordered 52 heavy-duty / 15 HA / 61 aeroderivative, equipment RPO $39,261M | as stated | same (accession 0001996810-26-000148) |
| Firm layers at 6/30/26 (GW / $M) | 3.0 / 1,926; 7.1 / 2,950; 5.1 / 3,717; 7.4 / 4,588; 10.2 / 7,676; 8.1 / 5,708; 12.1 / 12,696 | same |
| Back-test, reported revenue / layer dollars | 4 quarters 0.79-0.99; 8 quarters 0.85-0.96; 10 quarters 0.87-0.97 (mean 0.918); 12 quarters 0.93-0.97; 14 quarters 0.98 | same (0.789-0.990; 0.852-0.964; 0.873-0.969, mean 0.918; 0.931-0.974; 0.977) |
| Gap table (3 paths x 3 prices x 3 haircuts x 4 windows) | section 4a of the rebuild | all cells match |
| Equipment RPO schedule 6/30/26 | $87,821M; 36% / 65% / 97% within 1 / 2 / 5 years | same (10-Q note) |
| Annual EBITDA estimate counts 2026-2030 | 35 / 36 / 33 / 21 / 20 | same (workbook sheet Consensus) |

Three corrections to sources and inputs in the rebuild file:

1. The sentence "30 GW of shipments in 2030 at a price of roughly $900 per kilowatt" is **not in corpus source 3886**. The corpus copy of that article stops short of it. The sentence is in the full article (thestreet.com; a republished copy is dated 2026-07-25), next to "raised its revenue and EBITDA projections by $8 billion and $2 billion". Cite the web article.
2. The January 2026 statement compares reservations with the **backlog**, not with Q4 2025 orders: "our slot reservation agreements 10 to 20 points higher in price than where we are in the backlog" (Q4 2025 call, corpus source 2660). The rebuild's table 1e turns it into $753 x 1.10-1.20 = $828-904. Read as worded it is $618 (equipment RPO per firm GW at 12/31/25) x 1.10-1.20 = **$680-741/kW**. The comparison with Q4 2025 orders starts with the April and July 2026 statements, and those are about orders, not about the reservation book.
3. The same press article calls the next checkpoint a "December analyst day". The company transcript of 2026-09-16 says the next capital markets day is "certainly in the spring", after the January call. The transcript governs.

## 2. Ordinary readings of the Street figure that need no gap

### 2a. Company-stated output x order prices stepped along the company's own statements x 0.90

Every input is a company figure or comes straight from the filings. The haircut 0.90 is the mean of the first version's back-test; the rebuild's own means are 0.906 (4 quarters), 0.913 (8) and 0.918 (10).

| Period | GW (source) | $/kW (source) | x 0.90, $M | Street $M (Bloomberg, 2026-10-01) | Difference | Cumulative difference |
|---|---|---|---|---|---|---|
| H2 2026 | 10 (5 a quarter) | company guide | 5,491 | 5,491 | 0 | 0 |
| 2027 | 20 (July plan) | 697 (orders booked H2 2025, all-in) | 12,543 | 12,151 | +3.2% | +2.2% |
| 2028 | 24 (company's stated 2028 rate) | 729 (orders booked Q4 2025 and Q1 2026) | 15,738 | 15,888 | -0.9% | **+0.7%** (to end-2028) |
| 2029 | 26 (July plan) | 828 (Q4 2025 orders + 10 points) | 19,371 | 19,256 | +0.6% | **+0.7%** (to end-2029) |
| 2030 | 30 (company's stated 2030 rate) | 865 (Q4 2025 orders + 15 points, the middle of the 10-20 guide) | 23,367 | 23,469 | -0.4% | **+0.3%** (to end-2030) |
| H1 2031 | 15 | 903 (Q4 2025 orders + 20 points) | 12,191 | 12,340 | -1.2% | **+0.1%** (to Q2 2031) |

- This is the first version's rival explanation (24 GW x about $735 x 0.90) carried to every year. It lands within 1% of the Street cumulative in all four windows.
- It is one of several combinations that work. Which price goes to which year was chosen here, so the closeness of the fit is partly selection. What it shows: the Street needs no assumption outside company statements.
- The same table at k = 0.926 gives +3.0% to +3.3% cumulative; at k = 0.955 it gives +5.9% to +6.2%. So the rebuild's central gap is, almost exactly, the step from a 0.90 haircut to a 0.955 haircut (0.955 / 0.90 = +6.1%).
- The Street's own $/kW rises smoothly: 549, 608, 691, 741, 782, 823 (July plan GW). That is the shape of a price guide rolled forward a year at a time, not of a first-in-first-out layer build.

### 2b. The Street equals the signed book at published prices and a back-tested haircut

Recomputed from the rebuild's own book (firm layers, then reservations at P). July plan.

| Window | Haircut that gives the Street at P = $825 | Reservation price that gives the Street at k = 0.955 / 0.918 / 0.90 |
|---|---|---|
| to end-2028 | 0.854 (no reservations in the window) | - |
| to end-2029 | 0.869 | 616 / 702 / 746 |
| to end-2030 | 0.892 | **725 / 782 / 812** |
| to Q2 2031 | 0.906 | 754 / 806 / 834 |

Published and derived prices for the reservation book:

| Reading | $/kW |
|---|---|
| January 2026 statement as worded (10-20 points above the backlog, $618) | 680-741 |
| Heavy-duty-only price of Q4 2025 orders ($652-686) + 10-20 points (reservations hold no aeroderivatives, per the rebuild's section 2) | 717-823 |
| Q4 2025 all-in orders ($753) + 10-20 points | 828-903 |
| BNP Paribas class prices at the reservation mix; Morgan Stanley 2030 assumption | 876; 900 |

- The Street-implied reservation price ($725-812 to end-2030) sits in the middle of the published range ($680-900). The implied haircuts for the three longer windows (0.87-0.91) sit inside the 8- and 10-quarter back-test range (0.85-0.97).
- To end-2028 the implied haircut is 0.854: at the 8-quarter low (0.852), just under the 10-quarter low (0.873). The same number follows from output about 5% under the July plan (50.4 GW against 53) at the mean haircut. First-half 2026 shipments were 7.5 GW against 8.2 GW a year earlier; Q2 2026 shipped 3.3 GW.

### 2c. Analysts following guidance

| Item | Street (Bloomberg, 2026-10-01) | Company |
|---|---|---|
| Power revenue growth 2026 / 2027 / 2028 | +19.4% / +19.1% / +19.2% (FY2026 = H1 actual $10,450M + Street H2 $13,160M) | "Revenue up high teens at Power" 2025 to 2028 (December 2025 update, corpus source 1844); 17-19% a year from $19,767M = $31.7-33.3B in 2028 against Street $33.5B |
| Power revenue growth 2029 / 2030 | +17.9% / +14.4% | no outlook until the capital markets day |
| Power services growth 2026 to 2030 | +9.1%, +9.9%, +12.7%, +11.6%, +13.4% | $12B in 2025 to $22B in 2035, called "conservative" (2026-09-16) |
| Power equipment growth 2026 to 2030 | +39.7%, +30.1%, +30.8%, +21.2%, +21.9% | residual of the two lines above |

Through 2028 the Street's Power total is the company framework, and equipment is what is left after services. The 2028 slots were already sold out and the 24 GW rate already stated when that framework was set (December 2025).

### 2d. Timing by class (kill reason 2)

- The rebuild's by-year table still shows the whole difference in 2027-2029 (Street / book 0.87, 0.78, 0.90) and none by 2030-31 (0.95, 1.00). The company says the 2026 change in backlog margin shows up in 2029 and 2030 "because that's most of when that equipment delivers" (2026-09-16 transcript, confirmed on gevernova.com).
- Filed schedule: 35% of company equipment RPO ($30.7B) is expected after June 2028. If 25-40% of Electrification equipment RPO and 0-20% of Wind equipment RPO fall after that date (assumptions set here; not disclosed by segment), **$12.9-20.6B of the $39.3B Power firm book (33-52%) is scheduled after June 2028**. First-in-first-out leaves about $12.6B (the Q2 2026 layer) after that date, at the bottom of that range, and then needs all of it recognised in H2 2028, where the Street has $8.8B. So part of the firm book may ship after 2028, with earlier-priced reservations filling 2028 slots. The size cannot be fixed from filings.

## 3. Corrected centre and error

The rebuild's centre uses k = 0.955 for windows past ten quarters and P = $825.

- k = 0.955 rests on three 12-quarter windows and one 14-quarter window. They overlap almost fully and all end in Q4 2025 to Q2 2026, when the ratio was rising (H1 2026 alone is 1.27). No 18- or 20-quarter window exists. All 16 windows of eight quarters or more: mean 0.926, range 0.852-0.977.
- P = $825 is an all-in price applied to a book with no aeroderivatives. The readings in 2b centre near $780-790.

Gap against the Street on the July plan:

| Window | Rebuild centre | P 825, k 0.90 | P 782, k 0.926 | P 790, k 0.926 | P 741, k 0.926 | P 680, k 0.955 |
|---|---|---|---|---|---|---|
| to end-2028 (no reservation price enters) | +7.5% | +5.4% | +8.4% | +8.4% | +8.4% | +7.5% (k 0.918) |
| to end-2029 | +9.8% | +3.5% | +4.5% | +4.9% | +2.7% | +3.0% |
| to end-2030 | +7.0% | +0.9% | +0.9% | +1.4% | -1.9% | -3.1% |
| to Q2 2031 | +5.5% | -0.6% | -0.9% | -0.3% | -4.0% | -5.6% |

Error on the corrected centre (P 782, k 0.926): haircut +/-6.7% (0.852-0.977); price +/-0% / 4.0% / 6.2% / 6.9% by window on $717-900 (about +/-7.4% to end-2030 on $680-900); output path +/-9.3% / 7.9% / 7.1% / 6.6%. Combined in quadrature: **+/-11.5% / 11.1% / 11.6% / 11.7%**. Full range across paths, prices and haircut: -11% to +25% (end-2028), -14% to +26%, -19% to +22%, -20% to +20%.

- Headline window (to end-2030): corrected gap about **+1%** (centres run from -3% to +1.4%) against about **+/-12%**.
- The end-2028 window keeps a +5% to +8% centre on the July plan. Its band is +/-11.5%, and section 2d shows the layer order in that window is not known.

## 4. How thin the Street line is (Bloomberg, 2026-10-01)

| Check | Finding | File |
|---|---|---|
| Broker count on Power equipment | Not shown. MODL lists 29 brokers for Q3 2026; the Power equipment row shows no broker values (mean, low, high, median only). Across the whole sheet only 3 brokers show any value | `06_modl.xlsx` |
| Spread one quarter out | Q3 2026: mean 2,394, low 2,063 (-13.8%), high 2,591 (+8.3%) | `06_modl.xlsx` |
| Quarterly revenue estimates (company level) | 28 for Q3-Q4 2026; 22 for Q1-Q2 2027; 12 for each 2030 quarter. Division lines come from a subset of these | `01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx` |
| Annual EBITDA estimates | 35 / 36 / 33 / 21 / 20 for 2026-2030 | workbook sheet Consensus |
| Weight of the thin years | 2029-2030 is 56% of the end-2030 cumulative; 2028-2030 is 77%; 2029 to Q2 2031 is 62% of the 20-quarter total | `segment_quarterly.json` |
| Quarterly subset against the full annual set | Sum of quarterly revenue consensus is +0.1% / +0.7% / +1.0% / +1.2% above annual consensus for 2027-2030. The quarterly models run higher than the full Street | same; sheet Consensus |
| Internal consistency | Equipment + services less Power total: -231 to +307 a quarter in 2027-2030, exactly 0 in both 2031 quarters. Gas + Nuclear + Hydro less Power total: -432 to +367. Segment sum less company revenue: -11 to +122 | `segment_quarterly.json` |
| One-model signatures | Power organic growth is exactly 18.0 in all eight quarters of 2027-28 and exactly 9.0 in all eight of 2029-30, then blank. The Power RPO line jumps $19.2B from Q4 2028 to Q1 2029 and falls $26.7B from Q4 2030 to Q1 2031. In H1 2031 services growth drops to +2.2% and +5.5% from 11-14% | same |
| Freshness | 45 dated rating rows: 12 on or after 2026-09-17 (after the output ladder was stated), 25 between 2026-07-22 and 09-16, 8 older. FY2028 revenue consensus moved +0.0% from 2026-09-11 to 09-25 | sheets Bulk, ConsensusHistory |
| 2028 quarterly EPS | 15 brokers listed, 2 shown; one shows 3.55 and 28.64 for Q3 and Q4 2028 | `08_eeg_2028.xlsx` |

The longer the window, the more of the Street total rests on the thinnest part of the feed. The Q2 2031 window ends on what looks like one or two models.

## 5. Already published

| Who / when | What is public | Source |
|---|---|---|
| Company, December 2025 | Sold out through 2028; less than 10 GW left for 2029; 20 GW rate mid-2026, about 24 GW in 2028; Power revenue up high teens to 2028 | corpus source 1844 |
| Company, Q4 2025 call | Reservations 10-20 points above the backlog in price | corpus source 2660 |
| Company, Q2 2026 call | H1 2026 orders more than 20% above Q4 2025 orders; Q2 price lifted by aeroderivative mix and added combined-cycle scope; H2 orders at the higher end of 10-20 points; most of 2030 and more than half of 2031 contracted by year-end | corpus source 3161 |
| Company, 2026-09-16 conference | 5 / 6 / 7 GW a quarter; 2026 backlog-margin change shows up in 2029-30; 12 GW of added 2030-31 supply "at premium pricing"; 2030 outlook at a spring 2027 capital markets day | gevernova.com transcript (fetched 2026-10-01) |
| BNP Paribas, 2026-07-22 | Class prices: about $790/kW heavy-duty, $950/kW HA with combined-cycle scope, $1,800/kW aeroderivative | corpus source 301 |
| Morgan Stanley, 2026-07-23 | 2029 sold out; 30 GW shipped in 2030 at about $900/kW ($27.0B, 15% above the Bloomberg mean of $23,469M for all Power equipment); revenue and EBITDA projections raised $8B and $2B | thestreet.com article (web; the sentence is missing from corpus source 3886) |
| Morgan Stanley, March 2026 | "consensus estimates for 2030 could move higher" | investing.com / streetinsider.com |
| Mizuho, on CNBC, 2026-07-02 | "pretty much sold out until 2028. There's not much upside to the revenue estimates through 2030" | corpus source 1775 |
| Morningstar, 2025-08-14 | Power revenue built as GW shipped x price; says its estimates are in line with or above consensus through 2028 | morningstar.com |
| GLJ Research, 2026-09-14 | High-priced orders show up only in 2029; 2026-27 orders ship in 2030-31 | tikr.com summary |

- The method (GW x $/kW), the price inputs, the output path and the coverage point ("every Street dollar through 2030 is already signed") are all public. The coverage exhibit restates "sold out through 2030" in dollars.
- The top of the rebuild's range (30 GW x $900) is one broker's published model. The bottom is the Bloomberg mean. The rebuild's centre sits between two published views.
- Not found: any published statement that cumulative Power equipment consensus is too low. One covering analyst says the opposite.

## 6. Reveal inside 12 months

| Window | Last quarter reported | Street dollars reported by late July 2027 (Q3 2026 to Q2 2027: $10,874M) as a share of the window |
|---|---|---|
| to end-2028 | February 2029 | 32.4% |
| to end-2029 | February 2030 | 20.6% |
| to end-2030 | February 2031 | 14.3% |
| to Q2 2031 | July 2031 | 12.3% |

- The part that prints inside the horizon is a four-quarter window. The same back-test gives 0.79-0.99 for four-quarter windows (0.73-1.26 in the continuous form). The rebuild's by-year table has the Street 14% **above** the book in H2 2026.
- The Street's H2 2026 Power orders ($27.2B) already carry about 20 GW at the guided price, so a year-end RPO on the guide confirms the Street.
- A 2030 outlook at the capital markets day is guidance, not a reported number.

## 7. The six kill reasons after this check

| # | Kill reason | Status |
|---|---|---|
| 1 | Rival explanation | Stands in every window (2a, 2b, 2c). Cumulative fit within 1% |
| 2 | One order layer | Diluted in long windows, as the rebuild says. Still open to end-2028 (2d) |
| 3 | Error band | Not cleared. Corrected band about +/-11% to +/-12% in every window; corrected centre about +1% to end-2030 |
| 4 | Reveal date | Fails. Nothing inside 12 months settles the named line |
| 5 | Thin Street data | Fails, and worse in longer windows (section 4) |
| 6 | Profit effect | Stands. At the corrected centre the revenue difference to end-2030 is about +$0.7B on $76.3B |

## 8. What can be kept

1. Exhibit: the Street's $/kW by year (549, 608, 691, 741, 782, 823) against published prices ($680-900). It shows what consensus assumes in physical terms.
2. Exhibit: coverage. Firm RPO is 117% of the Street total to end-2028; firm plus reservations at $750-900 is 113-126% of the Street total to end-2030 (108% at $680).
3. Model structure: revenue = sum over classes of GW shipped x vintage price x k, plus non-gas. Ranges: k 0.85-0.98 for windows of eight quarters or more; reservation price $680-900.
4. Dated input checks from the rebuild's section 9 (GW sold, order price, year-end equipment RPO). They test inputs, not the line.

## 9. Sources and reproduce

- `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx`, `08_eeg_2028.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (sheets Consensus, ConsensusHistory, Bulk). Bloomberg, 2026-10-01.
- `data/gev.db` (read-only): chunks of accessions 0001996810-26-000148, -26-000064, -26-000015; sources 301, 1775, 1844, 2660, 3161, 3886.
- Web, fetched 2026-10-01: gevernova.com conference transcript (2026-09-16); thestreet.com article on the 2026-07-23 broker note (read through a republished copy); utilitydive.com (2026-07-23, 2026-04-23); tikr.com (2026-09-27); morningstar.com (2025-08-14).

Run from the `gev-corpus` folder. It prints sections 2a, 2b and the gap table in section 3.

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
FQ = [f'{y} Q{q}' for y in range(2026, 2032) for q in range(1, 5)][2:22]            # Q3 2026 .. Q2 2031
eq = [d[f'Total Revenue|Power|Equipment|{q}'] for q in FQ]
per = {'H2 2026': (0, 2), '2027': (2, 6), '2028': (6, 10), '2029': (10, 14), '2030': (14, 18), 'H1 2031': (18, 20)}
S = {k: sum(eq[a:b]) for k, (a, b) in per.items()}
q4, q1, h2 = 7676 / 10.2, 5708 / 8.1, (4588 + 7676) / (7.4 + 10.2)                  # all-in order $/kW: Q4 2025, Q1 2026, H2 2025
rows = [('2027', 20, h2), ('2028', 24, (q4 + q1) / 2), ('2029', 26, q4 * 1.10), ('2030', 30, q4 * 1.15), ('H1 2031', 15, q4 * 1.20)]
for k in (0.90, 0.926, 0.955):                                                       # section 2a
    cum = cs = S['H2 2026']
    for y, gw, p in rows:
        v = gw * p * k; cum += v; cs += S[y]
        print(k, y, round(v), round(S[y]), f'{v / S[y] - 1:+.1%}', 'cumulative', f'{cum / cs - 1:+.1%}')
lay = [(3.0, 1926), (7.1, 2950), (5.1, 3717), (7.4, 4588), (10.2, 7676), (8.1, 5708), (12.1, 12696)]
def book(gw, P):                                                                     # firm layers, then reservations at P
    c, left = 0.0, gw
    for a, b in lay:
        t = min(a, left); c += b * t / a; left -= t
    return c + left * P
st = {'end-2028': (53, sum(eq[:10])), 'end-2029': (79, sum(eq[:14])), 'end-2030': (109, sum(eq[:18])), 'Q2 2031': (124, sum(eq[:20]))}
for e, (gw, s) in st.items():                                                        # sections 2b and 3, July plan
    print(e, 'k at $825: %.3f' % (s / book(gw, 825)),
          ' '.join('P=%d,k=%.3f: %+.1f%%' % (P, k, 100 * (book(gw, P) * k / s - 1)) for P, k in ((825, 0.90), (782, 0.926), (790, 0.926), (741, 0.926), (680, 0.955))))
```
