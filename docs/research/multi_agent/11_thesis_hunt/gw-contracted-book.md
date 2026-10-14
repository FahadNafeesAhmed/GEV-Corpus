# Gigawatts, rebuild 1: the contracted book, cumulatively (id: gw-contracted-book)

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast is chosen for the team; every "our value" is a range with its method. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Words used here. **Firm backlog** = gas turbines on firm order (53 GW, inside the $39,261M Power equipment RPO). **Reservation** = slot reservation agreement: a paid place in the production queue, not yet an order and not in RPO (63 GW). **Contracted book** = the two together (116 GW). **Haircut (k)** = revenue actually recognised divided by the book dollars of the gigawatts shipped, from the back-test in section 3. **All-in $/kW** = Power equipment order dollars divided by gas GW ordered (the dollars include aeroderivative units and non-gas equipment).

## 0. Result

**Verdict: does not hold (holds = false).** Two reasons. (1) In every cumulative window the gap is smaller than, or about equal to, its own error. (2) No cumulative window is reported inside 12 months.

| Window from 1 July 2026 | Street Power equipment revenue, cumulative $M (Bloomberg, 2026-10-01) | Contracted book x haircut, July output plan, reservations at $825/kW, $M | Gap | Range across output paths, prices and haircut | Error band on our value | Gap larger than band? | Last quarter of the window is reported |
|---|---|---|---|---|---|---|---|
| to end-2028 (10 quarters) | 33,530 | 36,042 | +7.5% | -9.0% to +24.0% | +/-11.0% (haircut alone +/-5.4%) | No | February 2029 |
| to end-2029 (14 quarters) | 52,786 | 57,979 | +9.8% | -4.4% to +26.4% | +/-9.1% (+/-11.8% with the wide haircut range) | No (about equal) | February 2030 |
| to end-2030 (18 quarters) | 76,256 | 81,615 | +7.0% | -9.1% to +22.2% | +/-9.1% | No | February 2031 |
| to Q2 2031 (20 quarters) | 88,596 | 93,433 | +5.5% | -10.8% to +20.1% | +/-9.1% | No | July 2031 |
| Company-wide, 2 years (filed schedule) | 65,382 (all equipment) | 57,084 scheduled + $8.7-13.8B of later orders = 65,802-70,892 | +0.6% to +8.4% | +11.8% to +29.3% if the old ratio held (it has not; section 6) | +/-4.5% on the dollar basis | No | July 2028 |
| Company-wide, 5 years (filed schedule) | 214,266 | 85,186 scheduled; no completed 5-year window exists | not testable | | | No | July 2031 |

What the cumulative rebuild shows instead:
- The Street's cumulative Power equipment revenue is the contracted book, shipped about 5-8% slower than the July plan, or at plan with reservations converting at about $725/kW (range $655-865 across paths at a 0.955 haircut). Published prices for those reservations are $750-950/kW.
- By year, the Street sits 14% above the book in H2 2026, 13-22% below it in 2027-2028, and on it by 2030 and H1 2031 (section 4d). The difference is about which year the dollars land, and it shrinks as the window gets longer. The first version's checkers said this; the cumulative numbers confirm it.
- Every dollar of Street Power equipment revenue through 2030 is already signed: firm RPO alone is 117% of the Street total to end-2028; firm plus reservations is 113-126% of the Street total to end-2030.
- The angle is usable as (a) an exhibit of what consensus assumes in physical terms, (b) the driver structure of a Power equipment revenue line, and (c) dated checks on output and reservation price (sections 8 and 9).

## 1. Inputs

### 1a. Street (Bloomberg, 2026-10-01)
File `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, key `Total Revenue|Power|Equipment|YYYY Qn`.

| $M | H2 2026 | FY2027 | FY2028 | FY2029 | FY2030 | H1 2031 |
|---|---|---|---|---|---|---|
| Power equipment | 5,491 | 12,151 | 15,888 | 19,256 | 23,469 | 12,340 |
| Power services | 7,661 | 15,675 | 17,665 | 19,711 | 22,357 | 10,784 |
| Power total | 13,160 | 28,121 | 33,521 | 39,522 | 45,215 | 23,124 |
| Nuclear + Hydro lines (equipment and services) | 2,224 | 4,507 | 4,794 | 5,586 | 6,589 | 3,072 |
| Power orders | 27,204 | 52,958 | 50,239 | 52,482 | 54,312 | 23,541 |
| Power adj. EBITDA | 2,576 | 5,906 | 7,810 | 9,983 | 12,174 | 5,853 |

| Cumulative from Q3 2026, $M | to end-2028 | to end-2029 | to end-2030 | to Q2 2031 |
|---|---|---|---|---|
| Power equipment | 33,530 | 52,786 | 76,256 | 88,596 |
| Power adj. EBITDA | 16,292 | 26,275 | 38,448 | 44,301 |
| Company EBITDA | 26,442 | 42,674 | 62,145 | 72,469 |
| Company equipment (Power + Wind + Electrification) | 86,574 | 132,440 | 185,672 | 214,266 |

Quality of the line (it gets worse, not better, in the longer windows):
- Q3 2026 Power equipment: mean 2,394, low 2,063, high 2,591, median 2,433 (`06_modl.xlsx`). No broker count is shown for division lines.
- Number of annual EBITDA estimates: 35 / 36 / 33 / 21 / 20 for 2026-2030 (workbook sheet Consensus).
- Equipment + services less Power total: -8, -295, +33, -555, +611, 0 for the six columns above. Exactly zero in 2031 points to one model.
- Street Power RPO line against its own orders and revenue (RPO at 6/30/26 + orders - revenue): the line is +$2.0B at YE26, +$0.2B at YE27, -$4.4B at YE28, +$10.2B at YE29, +$9.2B at YE30, -$17.7B at Q2 2031. Contributors drop in and out.

### 1b. Company quarterly data (10-Q / 10-K MD&A "POWER" tables)
Accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148. Q4 = full year less nine months. Orders $M = change in Power equipment RPO + Power equipment revenue (+$3.9B in Q2 2024 for the Steam nuclear business sold to EDF).

| Quarter | GW ordered | Units ordered: heavy-duty / of which HA / aero | GW sold | Units sold: heavy-duty / HA / aero | Equipment revenue $M | Equipment RPO end $M | Orders $M | All-in $/kW |
|---|---|---|---|---|---|---|---|---|
| Q1 2023 | 2.3 | 6 / 4 / 7 | 3.6 | 18 / 4 / 5 | 1,180 | 13,992 | 1,593 | 693 |
| Q2 2023 | 2.1 | 14 / 0 / 12 | 2.3 | 9 / 3 / 5 | 1,147 | 13,980 | 1,135 | 540 |
| Q3 2023 | 3.1 | 12 / 4 / 8 | 2.7 | 12 / 2 / 7 | 1,291 | 13,865 | 1,176 | 379 |
| Q4 2023 | 2.1 | 9 / 0 / 25 | 5.2 | 19 / 5 / 16 | 1,980 | 13,636 | 1,751 | 834 |
| Q1 2024 | 4.9 | 16 / 8 / 18 | 2.3 | 10 / 1 / 7 | 1,201 | 14,394 | 1,959 | 400 |
| Q2 2024 | 4.1 | 14 / 4 / 1 | 1.5 | 8 / 1 / 7 | 1,285 | 10,978 | 1,769 | 431 |
| Q3 2024 | 5.1 | 14 / 9 / 15 | 3.3 | 13 / 5 / 5 | 1,426 | 11,392 | 1,840 | 361 |
| Q4 2024 | 6.1 | 24 / 4 / 10 | 4.8 | 17 / 8 / 8 | 1,796 | 12,461 | 2,865 | 470 |
| Q1 2025 | 7.1 | 29 / 8 / 9 | 3.0 | 12 / 5 / 7 | 1,491 | 13,920 | 2,950 | 415 |
| Q2 2025 | 5.1 | 20 / 7 / 27 | 5.2 | 18 / 8 / 3 | 1,504 | 16,133 | 3,717 | 729 |
| Q3 2025 | 7.4 | 20 / 13 / 9 | 4.0 | 14 / 6 / 6 | 1,744 | 18,977 | 4,588 | 620 |
| Q4 2025 | 10.2 | 41 / 15 / 18 | 3.1 | 10 / 5 / 11 | 1,946 | 24,707 | 7,676 | 753 |
| Q1 2026 | 8.1 | 28 / 12 / 9 | 4.2 | 15 / 5 / 10 | 1,885 | 28,530 | 5,708 | 705 |
| Q2 2026 | 12.1 | 52 / 15 / 61 | 3.3 | 13 / 3 / 16 | 1,965 | 39,261 | 12,696 | 1,049 |

Yearly: orders $589 / $417 / $635 / $916 per kW for 2023 / 2024 / 2025 / H1 2026 (H1 2026 = 18,404 / 20.1 GW). Revenue per kW sold: $406 / $480 / $437 / $513; 14-quarter average $450.

### 1c. Gigawatts under contract (earnings releases, 8-K exhibits 99.1)

| Quarter end | Firm backlog GW | Reservations GW | Total | New reservations in the quarter | Reservations converted to orders | Direct orders | Shipped | Equipment RPO per firm GW, $/kW |
|---|---|---|---|---|---|---|---|---|
| 3/31/25 | 29 | 21 | 50 | 7 | | | | 480 |
| 6/30/25 | 29 | 25 | 55 | 7 | 3 | 2 | 5 | 556 |
| 9/30/25 | 33 | 29 | 62 | 12 | 7 | 1 | 4 | 575 |
| 12/31/25 | 40 | 43 | 83 | 22 (derived) | 8 | 2 (derived) | 3 | 618 |
| 3/31/26 | 44 | 56 | 100 | 19 | 6 | 2 | 4 | 648 |
| 6/30/26 | 53 | 63 | 116 | 18 | 10 | 2 | 3 | 741 |

- Roll of the reservation book (prior + new - converted): 25 / 30 / 43 / 56 / 64 against disclosed 25 / 29 / 43 / 56 / 63. It ties within 1 GW of rounding, so no lapse of reservations is visible.
- 34 GW converted in five quarters. On a first-in-first-out count the 21 GW open at 3/31/25 and the 25 GW open at 6/30/25 have all converted. The 63 GW open today were signed from Q3 2025 to Q2 2026.
- Roll of firm backlog from the 10-Q GW tables, anchored at 53 GW: 29.9 / 29.8 / 33.2 / 40.3 / 44.2 against disclosed 29 / 29 / 33 / 40 / 44.
- Company statements: at least 125 GW under contract by year-end 2026, "mostly sold out through '30" and more than half of 2031 sold; second-half conversions to take firm backlog above reservations; 20 GW of new commitments in H2 "likely to prove to be conservative" (Q2 2026 call, corpus source 3161; conference transcript 2026-09-16, gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf`).

### 1d. Output path
Statements: "about three gigawatts of output a quarter to five gigawatts of output a quarter, starting in the third quarter"; "that next step-up in output in '28 to 24 gigawatts annualized"; "at least 30 gigawatts" over the next six quarters; 30 GW in 2030 (Q2 2026 call). Five GW in Q3 and Q4 2026, "the beginning of next year will feel generally very similar", six GW a quarter "sometime in the second half of next year", then in 2028 "six gigawatts for a period of time" and "seven gigawatts a quarter" (conference, 2026-09-16). GW figures are total gas turbine GW, aeroderivatives included, as in the 10-Q "Gas Turbine Gigawatts" line.

| Path, GW | H2 2026 | 2027 | 2028 | 2029 | 2030 | H1 2031 | Cumulative to end-2028 / 2029 / 2030 / Q2 2031 |
|---|---|---|---|---|---|---|---|
| A. July plan | 10 | 20 | 23 | 26 | 30 | 15 | 53 / 79 / 109 / 124 |
| B. September ladder | 10 | 21.5 | 25.5 | 28 | 30 | 15 | 57 / 85 / 115 / 130 |
| C. Slip (stress case set here, not a company statement: about half a GW a quarter below the plan) | 9 | 19 | 21 | 24 | 27 | 14 | 49 / 73 / 100 / 114 |

History for scale: GW sold 13.8 / 11.9 / 15.3 in 2023-2025; last four quarters 4.0, 3.1, 4.2, 3.3 = 14.6. The first quarter at 5 GW would be Q3 2026.

### 1e. Published prices for the reservation book
| Source | Statement | $/kW it gives |
|---|---|---|
| Company, Q3 2025 call (corpus source 3796) | Reservations "are at higher price and more attractive margins" than orders and convert "directionally in the next 12 months" | no number |
| Company, Q4 2025 call, 2026-01-28 (corpus source 2660) | "another 10 to 20 points of pricing strength in the SRAs today" versus existing backlog | Q4 2025 orders 753 x 1.10-1.20 = 828-904 |
| Company, Q2 2026 call | "first half 2026 orders were priced more than 20% above 4Q'25 equipment orders, reflecting a conversion of higher-priced SRAs"; H2 orders "at the higher end of the range of 10 to 20 points versus 4Q'25" | H1 2026 all-in 916 (+22%); H2 guide 866-904 on derived orders, 838-875 on the deck's order dollars (729) |
| Company, 2026-09-16 conference | 12 GW of added 2030-31 supply "at premium pricing"; 2026 change in backlog margin larger than 2025's low double digits | no number |
| BNP Paribas note, 2026-07-22 (via Utility Dive, corpus source 301) | Estimate for Q2 2026 orders by class | heavy-duty 790; HA with combined-cycle scope 950; aeroderivative 1,800 |
| Morgan Stanley note, 2026-07-23 (press report on finance.yahoo.com; corpus source 3886) | "30 GW of shipments in 2030 at a price of roughly $900 per kilowatt"; reservations near $3,000/kW of implied whole-plant price | 900 |
| Wood Mackenzie (corpus sources 137, 145) | Turbine-only price index about $600/kW by end-2027 | 600, turbine only |
| Observed all-in order price | Q4 2025 753; Q1 2026 705 (6 of 8.1 GW were conversions); Q2 2026 1,049 (10 of 12.1 GW were conversions; 61 aeroderivatives) | 705-1,049 |

Range used for the 63 GW: **$750 / $825 / $900 per kW** (low = heavy-duty-only price of H1 2026 orders, section 2; high = Morgan Stanley, and the BNP class prices at the reservation mix give $876).

## 2. The contracted book by class

Gigawatts per unit, least squares on 28 quarterly observations of orders and sales (GW = a x HA + b x other heavy-duty + c x aero, R2 0.97): HA 0.435 (s.e. 0.022), other heavy-duty 0.17 (s.e. 0.015), aeroderivative not different from zero in orders and 0.04 in sales. The company says smaller aeroderivatives are "30-, 35-megawatt applications". Used: 0.435 / 0.17 / 0.035.

**Firm backlog, 53 GW, $39,261M at 6/30/26 (estimate; GEV does not disclose it by class)**

| Class | Units | GW | $M | Basis |
|---|---|---|---|---|
| HA | 70 | 30.4 | inside heavy-duty | 51 "HA-Turbines in RPO" at 12/31/25 (10-K) + 27 ordered - 8 sold in H1 2026 |
| Other heavy-duty | about 100 | 16.6-17.3 | inside heavy-duty | residual GW / 0.17 |
| Heavy-duty total | about 170 | 47.4 | 26,200-28,500 = $552-596/kW | RPO less aero less non-gas |
| Aeroderivative | 150-170 | 5.3-6.0 | 6,800-10,100 | orders less sales since end-2021 = +130 units, plus 20-40 assumed at the start; 2026 units at $54-63M (BNP $1,800/kW x 30-35 MW), 2025 units at $40-55M, older at $30-40M |
| Non-gas (hydro, nuclear, steam) | | | 3,000-4,000 | Ex-EDF RPO at end-2023 of $9.7B less 17.5 GW of gas at $380-420/kW = $2.4-3.1B; MD&A reports increases in Hydro and Nuclear equipment in 2025 |

Heavy-duty-only order price (all-in orders less aeroderivative units x $63M less $0.3B a quarter of non-gas orders, over GW ordered less aero GW): Q1 2025 307, Q2 2025 413, Q3 2025 525, **Q4 2025 652, Q1 2026 622, Q2 2026 858, H1 2026 755** (+16% on Q4 2025; with aero at $45M a unit: 686 / 643 / 968 / 826, +20%). So the "10 to 20 points" guide matches the heavy-duty-only price; the +22% all-in figure includes aeroderivative mix. Pre-2026 heavy-duty units still in backlog: about 29.7 GW at about $460/kW.

**Reservations, 63 GW (not in RPO; composition is an estimate)**

| Class | Units | GW | Price range $/kW | $B |
|---|---|---|---|---|
| HA | about 78 | 34 | 800-950 | 27.1-32.2 |
| Other heavy-duty | about 170 | 29 | 700-790 | 20.3-22.9 |
| Total | | 63 | 754-876; 900 on the Morgan Stanley figure | 47.5-56.7 |

Basis: "130 machines running ... 195 more machines on contract" (conference, 2026-09-16); 70 in RPO; about 47 shipped and being installed (43 at 12/31/25 + 8 sold - 4 newly running). 195 - 70 - 47 = 78. Check: HA share of contracted GW = (30.4 + 33.9) / 116 = 56%, against "more than half" (Q2 2026 call). Aeroderivatives are ordered directly and are assumed not to sit in reservations.

**Non-gas equipment inside the division.** FY2025 revenue: Nuclear $1,018M, Hydro $806M, Steam $1,937M (10-K 2025 p.26); the equipment share is not disclosed. Estimate $1.2B a year of equipment revenue (range $0.9-1.6B), about 18% of FY2025 Power equipment revenue and about 7-9% of the Street cumulative to 2030 ($5.4-7.2B of $76.3B). $3-4B of it is already in RPO. New non-gas orders are left out of the contracted-book figures and shown as an add-on in section 5.

## 3. Cumulative back-test and the haircut

Method. Pick a start quarter. Opening layer = firm backlog GW and equipment RPO at that date (less the $3.9B EDF item before Q2 2024). Each later quarter adds a layer (GW ordered, order dollars). Ship the reported GW from the oldest layer first. Compare cumulative reported Power equipment revenue with the cumulative layer dollars shipped. This is the same build as the forward calculation in section 4, with GW and order dollars known.

Reported revenue / layer dollars, by start quarter and window length:

| Start | 4 quarters | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|---|
| Q1 2023 | 0.91 | 1.03 | 0.93 | 0.87 | 0.93 | 0.98 |
| Q2 2023 | 0.91 | 0.97 | 0.95 | 0.88 | 0.95 | |
| Q3 2023 | 0.99 | 0.91 | 0.85 | 0.92 | 0.97 | |
| Q4 2023 | 0.99 | 0.94 | 0.86 | 0.94 | | |
| Q1 2024 | 0.86 | 0.81 | 0.90 | 0.97 | | |
| Q2 2024 | 0.91 | 0.82 | 0.93 | | | |
| Q3 2024 | 0.79 | 0.88 | 0.96 | | | |
| Q4 2024 | 0.83 | 0.92 | | | | |
| Q1 2025 | 0.90 | 0.96 | | | | |
| Q2 2025 | 0.92 | | | | | |
| Q3 2025 | 0.95 | | | | | |
| Windows | 11 | 9 | 7 | 5 | 3 | 1 |
| Min / max | 0.79 / 0.99 | 0.81 / 1.03 | 0.85 / 0.96 | 0.87 / 0.97 | 0.93 / 0.97 | 0.98 |
| Mean (s.d.) | 0.906 (0.062) | 0.916 (0.071) | 0.913 (0.043) | 0.918 (0.041) | 0.952 (0.021) | 0.977 |

Same test with one continuous stack from end-2022 (the form the first version's checker used): 4 quarters 0.73-1.26 (s.d. 0.150); 8 quarters 0.87-0.99 (0.042); 10 quarters 0.87-1.00 (0.049); 12 quarters 0.93-0.99; 14 quarters 0.98. Calendar years 0.91 / 0.95 / 0.94; H1 2026 1.27.

Readings:
- Multi-year windows cut the error from about +/-27% (four quarters, continuous form) to about +/-5% (ten quarters) and +/-3% (twelve to fourteen quarters).
- The sample is small. All windows of eight quarters or more come from 14 quarters of data, about one and a half independent observations. The dollar miss depends only on the end quarter: -$2.0B to -$2.1B for windows ending Q2-Q3 2025, -$1.3B ending Q4 2025, -$1.0B ending Q1 2026, -$0.5B ending Q2 2026. It has been closing as aeroderivative units ship ahead of the queue.
- Why the ratio is below 1: the oldest layer carries the long-dated non-gas equipment, which the method "ships" first. Read as a fixed amount ($0.5-2.1B) on a $39B book, the haircut would be 0.95-0.99 (gap to end-2028 on path A +10.9% to +15.6%); read as a ratio it is 0.87-0.98. The ratio form is used below because it is the lower of the two.
- Haircut used: **0.918 (0.87-0.97) for the 10-quarter window; 0.955 (0.93-0.98) for longer windows**; wide range 0.85-1.00 (every window of eight quarters or more, both forms). No window of 18 or 20 quarters exists, so the two longest forward windows borrow the 12-14 quarter figure.
- Not tested at all: the reservation leg. No reservation open at a disclosure date has yet been both converted and shipped inside a completed window. Only conversion to orders is observable (section 1c). The back-test also uses actual GW shipped; the forward calculation has to assume the output path.
- Cycle form (revenue while the opening backlog GW ships, over opening RPO): 1.01, 0.94, 0.91, 0.94, 0.82, 0.81, 0.86, 0.92 for starts Q1 2023 to Q4 2024 (5.5-7.2 quarters each); shortfall -$0.1B to +$2.0B.

## 4. Cumulative comparison (all-in method, the back-tested one)

Formula. Value(window) = k x [dollars of the first G gigawatts of the book]. G = cumulative GW shipped on the path. The book is the seven firm layers at 6/30/26 in order-date sequence (3.0 GW $1,926M; 7.1 / 2,950; 5.1 / 3,717; 7.4 / 4,588; 10.2 / 7,676; 8.1 / 5,708; 12.1 / 12,696; total 53 GW, $39,261M), then 63 GW of reservations at P, then open slots at P.

### 4a. Gap against the Street (low / mean / high haircut)

| Window | Path | GW shipped (firm / reservations / open) | P = $750 | P = $825 | P = $900 |
|---|---|---|---|---|---|
| to end-2028, Street 33,530, k 0.87 / 0.918 / 0.97 | A | 53 / 0 / 0 | +1.9% / +7.5% / +13.6% | same | same |
| | B | 53 / 4 / 0 | +9.7% / +15.7% / +22.3% | +10.4% / +16.5% / +23.1% | +11.2% / +17.3% / +24.0% |
| | C | 49 / 0 / 0 | -9.0% / -4.0% / +1.4% | same | same |
| to end-2029, Street 52,786, k 0.93 / 0.955 / 0.98 | A | 53 / 26 / 0 | +3.5% / +6.3% / +9.1% | +7.0% / +9.8% / +12.7% | +10.4% / +13.4% / +16.3% |
| | B | 53 / 32 / 0 | +11.5% / +14.5% / +17.4% | +15.7% / +18.8% / +21.9% | +19.9% / +23.1% / +26.4% |
| | C | 53 / 20 / 0 | -4.4% / -1.8% / +0.7% | -1.8% / +0.9% / +3.5% | +0.9% / +3.6% / +6.3% |
| to end-2030, Street 76,256 | A | 53 / 56 / 0 | -0.9% / +1.8% / +4.4% | +4.2% / +7.0% / +9.8% | +9.3% / +12.3% / +15.2% |
| | B | 53 / 62 / 0 | +4.6% / +7.4% / +10.2% | +10.3% / +13.2% / +16.2% | +15.9% / +19.1% / +22.2% |
| | C | 53 / 47 / 0 | -9.1% / -6.7% / -4.2% | -4.8% / -2.3% / +0.3% | -0.5% / +2.1% / +4.8% |
| to Q2 2031, Street 88,596 | A | 53 / 63 / 8 | -2.9% / -0.3% / +2.3% | +2.7% / +5.5% / +8.2% | +8.3% / +11.2% / +14.1% |
| | B | 53 / 63 / 14 | +1.8% / +4.6% / +7.3% | +7.9% / +10.8% / +13.7% | +14.0% / +17.0% / +20.1% |
| | C | 53 / 61 / 0 | -10.8% / -8.4% / -6.0% | -6.0% / -3.4% / -0.9% | -1.2% / +1.5% / +4.2% |

Dollar values at path A, P = $825, mean k: 36,042 / 57,979 / 81,615 / 93,433. Book dollars before the haircut: 39,261 / 60,711 / 85,461 / 97,836. Full range to end-2030: $69.3B (path C, $750, k 0.93) to $93.2B (path B, $900, k 0.98).

### 4b. Gap against the error

| Window | Gap (path A, $825, mean k) | Haircut range | Price range | Path (B to C, half) | Haircut + price | All three, in quadrature | With the wide haircut (0.85-1.00) | Gap larger than the cumulative back-test error? |
|---|---|---|---|---|---|---|---|---|
| to end-2028 | +7.5% (+$2.5B) | +/-5.4% | 0 | +/-9.5% | +/-5.4% | +/-11.0% | +/-12.6% | Larger than the haircut error alone (low end +1.9%); smaller once the path is counted. **No** |
| to end-2029 | +9.8% (+$5.2B) | +/-2.6% | +/-3.2% | +/-8.2% | +/-4.1% | +/-9.1% | +/-11.8% | About equal on four overlapping windows; smaller on the wide range. **No** |
| to end-2030 | +7.0% (+$5.4B) | +/-2.6% (borrowed) | +/-4.9% | +/-7.2% | +/-5.6% | +/-9.1% | +/-11.8% | **No** |
| to Q2 2031 | +5.5% (+$4.8B) | +/-2.6% (borrowed) | +/-5.4% | +/-6.7% | +/-6.0% | +/-9.1% | +/-11.7% | **No** |

Break-even output at $825 and mean k: 50.4 / 72.4 / 102.2 / 117.9 GW against 53 / 79 / 109 / 124 on the July plan, which is 4.9% / 8.3% / 6.2% / 5.0% below it. On the September ladder alone the gap is +13% to +19% in the first three windows and would clear the haircut-plus-price error. But the Street's GW are not observable, and the ladder describes a run rate, not a calendar-year delivery guide.

### 4c. What the Street number means in physical terms

| Reading of the Street figure | to end-2028 | to end-2029 | to end-2030 | to Q2 2031 |
|---|---|---|---|---|
| Street $ per kW shipped, path A / B / C | 633 / 588 / 684 | 668 / 621 / 723 | 700 / 663 / 763 | 714 / 682 / 777 |
| Haircut on the firm book that gives the Street (path A / B / C) | 0.854 / 0.788 / 0.956 | | | |
| Reservation price that gives the Street at k = 0.955 (path A / B / C) | | 616 / 500 / 801 | 725 / 655 / 864 | 754 / 695 / 877 |
| Same at k = 0.90 | | 746 / 606 / 970 | 812 / 733 / 967 | 834 / 769 / 970 |
| Firm RPO as % of the Street figure | 117% | 74% | 51% | 44% |
| Firm RPO + 63 GW at $750-900 as % of the Street figure | 258-286% | 164-182% | 113-126% | 98-108% |

Five-year identity. Street to Q2 2031 = $88,596M. Firm RPO expected within five years = $38,083M (97% of $39,261M, if Power follows the company-wide percentage). The remainder, $50,513M, over 63 GW = **$802/kW**. So the Street's five-year total equals the firm backlog plus the whole reservation book at about $800/kW with no haircut, and nothing for orders not yet signed (aeroderivatives beyond today's backlog, non-gas equipment beyond RPO, the 8-14 GW of open H1 2031 slots).

### 4d. Where in time the difference sits (P = $825, before haircut)

| Period | Path A: GW / book $M / book $/kW | Street $M / $/kW | Street / book | Path B: Street / book |
|---|---|---|---|---|
| H2 2026 | 10 / 4,834 / 483 | 5,491 / 549 | 1.136 | 1.136 |
| 2027 | 20 / 13,915 / 696 | 12,151 / 608 | 0.873 | 0.808 |
| 2028 | 23 / 20,511 / 892 | 15,888 / 691 | 0.775 | 0.700 |
| 2029 | 26 / 21,450 / 825 | 19,256 / 741 | 0.898 | 0.834 |
| 2030 | 30 / 24,750 / 825 | 23,469 / 782 | 0.948 | 0.948 |
| H1 2031 | 15 / 12,375 / 825 | 12,340 / 823 | 0.997 | 0.997 |

The Street price per kW rises smoothly (549, 608, 691, 741, 782, 823). The book in order-date sequence jumps in 2028 (the Q2 2026 layer). By 2030-31 the Street is on the reservation price. The Street books the higher-priced layers about one to two years later than order-date sequence does. That matches management's own timing statement (the 2026 change in backlog margin shows up in 2029 and 2030, "because that's most of when that equipment delivers").

## 5. By-class version and what lies outside the contracted book

Method. Aeroderivative backlog (160 units, $8.6B at vintage prices) ships first, at 16 units a quarter (the Q2 2026 rate) or 25. Heavy-duty GW = path GW less aero GW, shipped in order-date sequence over heavy-duty layers (pre-2026 29.7 GW at $463/kW; Q1 2026 7.8 GW at $622; Q2 2026 10.0 GW at $858; then reservations at P). Non-gas from RPO at $1.2B a year up to $3.4B. Add-ons are not under contract: aeroderivative units beyond the backlog at $63M, non-gas beyond RPO, open heavy-duty slots at P.

| Window, path A, P = $825 | Contracted $M (aero at 16 / 25 a quarter) | Gap, no haircut | Gap at k = 0.955 | Add-ons $M (16 / 25) | Gap with add-ons at 0.955 |
|---|---|---|---|---|---|
| to end-2028 | 38,761 / 36,057 | +15.6% / +7.5% | +10.4% / +2.7% | 0 / 5,670 | +10.4% / +18.8% |
| to end-2029 | 58,758 / 55,120 | +11.3% / +4.4% | +6.3% / -0.3% | 4,837 / 12,775 | +15.1% / +22.8% |
| to end-2030 | 81,660 / 76,982 | +7.1% / +1.0% | +2.3% / -3.6% | 10,069 / 20,275 | +14.9% / +21.8% |
| to Q2 2031 | 91,131 / 87,914 | +2.9% / -0.8% | -1.8% / -5.2% | 14,665 / 24,025 | +14.0% / +20.7% |

Same contracted column at 16 a quarter and k = 0.955 on path B: +19.8% / +15.3% / +8.5% / -1.8%; on path C: +0.6% / -2.7% / -7.0% / -8.5%.

Readings:
- Splitting by class does not open a gap. On the July plan the contracted book alone is +10% (2028), +6% (2029), +2% (2030), -2% (Q2 2031) at a 0.955 haircut; across paths it is -9% to +20%.
- Aeroderivatives are about 10% of firm GW and about 20% of firm dollars, and they ship inside ten quarters. That moves dollars forward (the Street is above the order-date book in H2 2026) but not into or out of a window that ends in 2028 or later.
- A double-digit cumulative gap needs revenue that is not under contract today: 130-340 more aeroderivative units by 2030-31 ($8-21B), new non-gas orders ($2-3B), open 2031 slots ($2-7B). That is a forecast of future orders, not arithmetic on the signed book.
- No haircut has been back-tested for the by-class build. The 0.955 column borrows the all-in figure and may double count, because non-gas is already treated separately here.

## 6. Company-wide version from the filed schedule

RPO note in every filing: equipment RPO and the share expected within 1 / 2 / 5 years. Revenue = consolidated equipment revenue (XBRL, product). Street quarters = sum of the three division equipment lines (Bloomberg, 2026-10-01; about $30M a quarter of intersegment sales included). "Ex-Prolec" removes Prolec equipment revenue (469 and 834 reported in Q1 and Q2 2026; $3.4B in 2026 rising to $4.8B in 2031 assumed from the acquisition deck) when the backlog date is before the acquisition. "Fill" = revenue in the window less the scheduled amount, which is revenue from orders booked after the date.

| Filing date | Equipment RPO $M | 1 / 2 / 5 yr % | Within 2 yrs $M | Next 8 quarters $M (Street quarters in it) | Ratio (ex-Prolec) | Fill ex-Prolec $M | Within 5 yrs $M | Next 20 quarters $M (Street quarters) | Ratio (ex-Prolec) |
|---|---|---|---|---|---|---|---|---|---|
| 12/31/23 | 40,478 | 51 / 77 / 100 | 31,168 | 39,886 (0) | 1.280 (1.280) | 8,718 | 40,478 | 138,174 (10) | 3.41 (3.15) |
| 3/31/24 | 42,210 | 45 / 71 / 93 | 29,969 | 41,523 (0) | 1.386 (1.370) | 11,085 | 39,255 | 144,181 (11) | 3.67 (3.37) |
| 6/30/24 | 41,561 | 47 / 69 / 91 | 28,677 | 43,788 (0) | 1.527 (1.481) | 13,808 | 37,821 | 151,004 (12) | 3.99 (3.65) |
| 9/30/24 | 42,069 | 46 / 70 / 91 | 29,448 | 45,980 (1) | 1.561 (1.489) | 14,404 | 38,283 | 157,663 (13) | 4.12 (3.76) |
| 12/31/24 | 43,047 | 44 / 69 / 93 | 29,702 | 48,468 (2) | 1.632 (1.532) | 15,814 | 40,034 | 165,087 (14) | 4.12 (3.75) |
| 3/31/25 | 45,478 | 45 / 71 / 91 | 32,289 | 50,947 (3) | 1.578 (1.458) | 14,784 | 41,385 | 172,245 (15) | 4.16 (3.77) |
| 6/30/25 | 49,712 | 42 / 70 / 92 | 34,798 | 53,801 (4) | 1.546 (1.408) | 14,208 | 45,735 | 180,135 (16) | 3.94 (3.56) |
| 9/30/25 | 54,092 | 41 / 71 / 97 | 38,405 | 56,472 (5) | 1.470 (1.322) | 12,351 | 52,469 | 188,009 (17) | 3.58 (3.23) |
| 12/31/25 | 64,245 | 37 / 69 / 97 | 44,329 | 59,917 (6) | 1.352 (1.202) | 8,950 | 62,318 | 197,385 (18) | 3.17 (2.86) |
| 3/31/26 | 75,924 | 38 / 69 / 98 | 52,388 | 62,688 (7) | 1.197 | 10,300 | 74,406 | 205,420 (19) | 2.76 |
| **6/30/26** | **87,821** | **36 / 65 / 97** | **57,084** | **65,382 (8)** | **1.145** | **8,298** | **85,186** | **214,266 (20)** | **2.52** |

Street by division at 6/30/26: 8 quarters = Power 24,740, Wind 10,796, Electrification 29,845; 20 quarters = Power 88,596, Wind 26,603, Electrification 99,067. Rounding of the percentages moves the scheduled amounts by +/-$440M.

Two-year window:
- Three fully reported windows: 1.280, 1.370, 1.481 (ex-Prolec); fill $8.7B, $11.1B, $13.8B. The Street's ratio for the current window (1.145) and its fill ($8.3B) are below all three.
- If the old ratio held: 57,084 x 1.280 to 1.481 = $73.1-84.5B, +11.8% to +29.3%. If the old dollar fill held: 57,084 + 8.7 to 13.8 = $65.8-70.9B, +0.6% to +8.4% (mean fill $11.2B: +4.4%).
- The ratio is not stable. It has fallen at every date since 12/31/24 (1.53, 1.46, 1.41, 1.32, 1.20, 1.20, 1.145) as orders are placed further ahead and more of the next two years is already in backlog. The dollar basis is the usable one. On it the gap (+0.6% to +8.4%) is no larger than the spread of the three observations (+/-$2.5B, +/-4.5% of the total). **The gap does not exceed the error.**
- The first year of this window is the separate candidate "equipment-revenue-vs-rpo-schedule" (same folder), already tested.

Five-year window:
- No five-year window has completed; the oldest still has 10 of 20 quarters on Street numbers. The ratio falls from about 3.2-3.8 (2023-2025 dates, ex-Prolec) to 2.5 today for the same reason as above. The Street's five-year fill is $129B, against company equipment orders of about $42B in 2025 (change in equipment RPO + revenue) and about $31B in H1 2026 after taking out about $4B of acquired Prolec backlog. **Nothing to test.**
- Power only: section 4c (firm + reservations at $802/kW = Street).

## 7. The six kill reasons, each answered

| # | Kill reason | What the cumulative rebuild does with it | Status |
|---|---|---|---|
| 1 | Rival explanation: Street FY2028 = 24 GW x $735 x 0.90 | It extends to every window. Street to end-2028 = the firm book x 0.854 on the July plan (8-quarter back-test low 0.85, 10-quarter low 0.87). Street to end-2030 = firm book + reservations at $725/kW at k 0.955, or at $812 at k 0.90 (section 4c). Street to Q2 2031 = firm RPO within five years + 63 GW at $802 with no haircut. Each sits inside published prices and the back-tested haircut. No gap is needed to explain any window | **Stands.** Not refuted |
| 2 | The gap sat in the Q2 2026 layer ($1,049/kW, aeroderivative mix and combined-cycle scope; 2026 heavy-duty orders deliver mostly 2029-31) | Partly removed. With aeroderivatives split out, the heavy-duty part of that layer is about 10 GW at about $858/kW ($8.6B, 22% of firm dollars). In a window to end-2028 or later the aeroderivative dollars are inside the window whenever they ship. If the 2026 heavy-duty units ship in 2029-31 and reservations converting at $750-900 take their 2028 slots, the total to end-2028 moves by -$1.1B to +$0.4B (-3% to +1%). But section 4d shows the difference between book and Street still sits in 2027-2029, peaks in 2028 (Street / book 0.775) and closes by 2030-31. Lengthening the window dilutes the layer; it does not create a gap | **Partly answered.** The layer no longer drives the result; the result is then small |
| 3 | Error band: four-quarter back-tests miss by -27% to +25% | Multi-year windows cut the haircut error to +/-5.4% (10 quarters) and +/-2.6% (12-14 quarters). Two errors enter that the back-test cannot see: the reservation price (+/-3% to +/-5%) and the output path (+/-7% to +/-10%). Total +/-9% to +/-11%; +/-12% on the wide haircut range. Central gaps are +5.5% to +9.8% | **Not cleared** in any window |
| 4 | Reveal date outside the horizon | Worse. The windows end December 2028 to June 2031. Inside 12 months there are only checks on two inputs (output and conversion price), section 9 | **Not answered** |
| 5 | Thin, partly stale Street data on the division line; Morgan Stanley already at 30 GW x about $900 for 2030 | Worse in longer windows. 2029-2031 rest on fewer models (21 and 20 annual estimates against 33-36; one model in 2031; RPO line breaks of +$10B and -$18B). The top of our price range ($900) is the Morgan Stanley figure; 30 GW x $900 = $27.0B for 2030 against the Bloomberg mean of $23.5B. The upper half of our range is already a published broker view | **Not answered** |
| 6 | Small profit effect | Path A centre: +$2.5B to +$5.4B of cumulative revenue. At the Street's own cumulative Power margin (21.8-24.3%) that is $0.5-1.3B, 1.6-2.8% of cumulative company EBITDA. If it were all price on signed GW with 60-90% drop-through: 4-11%. Inside 12 months: zero | **Stands** |

## 8. What the angle is good for

1. **Exhibit: consensus in physical terms.** Section 4d (Street $/kW by year against the signed book by year) and section 4c (the Street's cumulative total = firm backlog + 63 GW of reservations at about $725-800/kW). Ready to chart: two step lines of $/kW by year, plus the published price range $750-950.
2. **Exhibit: coverage.** Street Power equipment revenue is 117% covered by firm RPO to end-2028 and 113-126% covered by firm RPO plus reservations to end-2030. The Street figure to end-2030 needs 0.79-0.88 of the contracted dollars to convert (76,256 / 95,961 to 86,511). What is left to deliver the number is output and conversion, not new demand.
3. **Driver structure for a Power equipment revenue line** (the team sets the values):
   - revenue = sum over classes of (GW shipped x price of the order vintage that fills the slot) x k + non-gas;
   - classes: aeroderivative (units x $ per unit; about 160 units in backlog; 16 shipped in Q2 2026), HA and other heavy-duty (firm 47 GW at $550-600/kW; reservations 63 GW at $750-900), non-gas ($0.9-1.6B a year);
   - k from section 3: 0.87-0.97 over ten quarters, 0.93-0.98 over twelve to fourteen; lower and noisier over four (0.79-0.99, or 0.73-1.26 in the continuous form);
   - output path from section 1d.
4. **Sensitivities** (to end-2030, July plan): $50/kW on the reservation book = $2.7B (3.5% of the Street cumulative); 0.01 of k = $0.85B; 1 GW of cumulative output = $0.8B; half a GW a quarter of slippage (path C) = -$7.1B (-9 points).
5. **A dated test of the two inputs that matter** (section 9). It tells the team early whether the reservation book converts at the guided price and whether output steps to 5 GW a quarter. It does not test the revenue line.

## 9. Company-reported checks inside 12 months (inputs, not the named line)

| Date | Number | Street (Bloomberg, 2026-10-01) | Level that supports the upper half of our range | Level that supports the lower half |
|---|---|---|---|---|
| 2026-10-28, Q3 2026 10-Q | Gas turbine GW sold | none (no GW line) | 5.0 GW or more | 4.5 GW or less |
| same | Power equipment revenue | $2,394M (low 2,063, high 2,591) | | |
| same | All-in order price = (change in Power equipment RPO + equipment revenue) / GW ordered | Power orders $12.2B (low 8.8, high 15.5), equipment and services together | $838/kW or more | $753/kW or less (no step up on Q4 2025) |
| same | Firm backlog GW and reservation GW | | conversions of 8 GW or more | |
| Late January 2027, 10-K 2026 | Power equipment RPO at 12/31/26 and firm backlog GW | Power orders H2 2026 $27.2B; less services orders of about $8.5-9.5B leaves about $17.7-18.7B of equipment, an RPO of about $51.5-52.5B | $50.5B or more on 63 GW or more firm (20 GW ordered in H2 at $838 or more); $54.7B or more if 25 GW | $48.8B or less on 63 GW (H2 orders at $753 or less) |
| same | 2026 change in Power backlog margin; FY2027 outlook with gas output for 2027 | Street 2027 Power equipment $12,151M = $608/kW on 20 GW | 2027 output of 21 GW or more | 20 GW or fewer |
| Spring 2027 capital markets day | 2030 outlook with the equipment / services split | Street 2030 Power equipment $23,469M = 30 GW x $782 | implied Power equipment of $25.5B or more (30 GW x $850) | $23.5B or less |
| Late July 2027, Q2 2027 10-Q | Four quarters of GW sold (Q3 2026 to Q2 2027) | Street Power equipment for the four quarters $10,874M | 20 GW or more | 18 GW or fewer |

The Street's own order line already assumes about $18B of H2 2026 equipment orders, which is about 20-21 GW at the guided price. So a year-end RPO on the guide confirms the Street rather than surprising it. An outlook at the capital markets day is guidance, not a reported result.

## 10. Limits

1. GW sold x price is an approximation. Gas turbines are recognised over time on costs incurred (10-K 2025, "Revenue Recognition on Equipment on an Over-Time Basis"), and commissioning can follow shipment by 6-18 months (Q2 2026 call).
2. The class split of backlog and reservations is an estimate from unit counts; GEV discloses neither by class in dollars or GW. Aeroderivative unit prices rest on one broker's figure.
3. The reservation price is not disclosed. The 10-K 2025 risk factor says reservations "may not result in orders" and counterparties "may not place orders equal to the value of their reservation amount or at all". No lapse is visible so far (section 1c).
4. RPO excludes orders the customer can cancel without a substantive penalty (10-Q), so order dollars derived from RPO can lag signed contract value.
5. The back-test has about one and a half independent multi-year observations and ends in a period when the ratio was rising.
6. Path C is a stress case set here, not a company statement. The error from the output path is a judgement, not a back-test.
7. Out-year Street division lines are thin (section 1a).

## 11. Sources and reproduce

| Data | Where |
|---|---|
| Street | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` sheet Consensus. Bloomberg, 2026-10-01 |
| GW, units, Power equipment revenue and RPO | `data/gev.db`, chunks of the ten accessions in section 1b (query: `text LIKE '%Gas Turbine Gigawatts%'`) |
| Backlog and reservation GW | 8-K exhibits 99.1: 0001996810-25-000072, -25-000132, -25-000159, -26-000012, -26-000063, -26-000147 |
| RPO schedule | RPO note of each 10-Q / 10-K; 12/31/23 from 0001193125-24-063739; 3/31/24 from 0001193125-24-131304 |
| Consolidated equipment revenue | `data/financials/gev_segments.csv` (`RevenueFromContractWithCustomerExcludingAssessedTax`, Product) |
| Calls and conference | corpus sources 3161 (Q2 2026 call), 3796 (Q3 2025 call), 2660 (Q4 2025 call), 1844 (December 2025 update); conference transcript PDF on gevernova.com, fetched 2026-10-01 |
| Broker prices | corpus sources 301 (BNP Paribas via Utility Dive), 3886 and finance.yahoo.com (Morgan Stanley), 137 / 145 (Wood Mackenzie) |
| Earlier work | `propose_power-equipment-physical.md`, `verify_power-equipment-fy28-fy29_reproduce.md`, `_already-known.md`, `_wedge-tests.md`, `propose_price-implied.md`, `propose_rpo-equipment.md` (this folder) |

Run from the `gev-corpus` folder. It prints the back-test (section 3) and the gap table (section 4a).

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
FQ = [f'{y} Q{q}' for y in range(2026, 2032) for q in range(1, 5)][2:22]            # Q3 2026 .. Q2 2031
eq = [d[f'Total Revenue|Power|Equipment|{q}'] for q in FQ]
N = {'end-2028': 10, 'end-2029': 14, 'end-2030': 18, 'Q2 2031': 20}
street = {e: sum(eq[:n]) for e, n in N.items()}
# quarter: (GW sold, Power equipment revenue, GW ordered, Power equipment RPO at end), 10-Q / 10-K Power tables
Q = {'2023Q1': (3.6, 1180, 2.3, 13992), '2023Q2': (2.3, 1147, 2.1, 13980), '2023Q3': (2.7, 1291, 3.1, 13865), '2023Q4': (5.2, 1980, 2.1, 13636),
     '2024Q1': (2.3, 1201, 4.9, 14394), '2024Q2': (1.5, 1285, 4.1, 10978), '2024Q3': (3.3, 1426, 5.1, 11392), '2024Q4': (4.8, 1796, 6.1, 12461),
     '2025Q1': (3.0, 1491, 7.1, 13920), '2025Q2': (5.2, 1504, 5.1, 16133), '2025Q3': (4.0, 1744, 7.4, 18977), '2025Q4': (3.1, 1946, 10.2, 24707),
     '2026Q1': (4.2, 1885, 8.1, 28530), '2026Q2': (3.3, 1965, 12.1, 39261)}
K = sorted(Q); EDF = 3900; rpo0 = 13579                                             # rpo0 = Power equipment RPO at 12/31/22 (10-K 2024)
ords, opn_rpo, opn_gw = {}, {}, {}
g = 53.0 - sum(Q[k][2] for k in K) + sum(Q[k][0] for k in K); prev = rpo0           # backlog GW rolled back from 53 GW at 6/30/26
for k in K:
    opn_rpo[k], opn_gw[k] = prev, g
    ords[k] = Q[k][3] - prev + Q[k][1] + (EDF if k == '2024Q2' else 0)             # equipment orders = change in RPO + revenue
    prev = Q[k][3]; g += Q[k][2] - Q[k][0]
def backtest(i0, n):                                                                # reported revenue / first-in-first-out layer dollars over n quarters
    k0 = K[i0]; stack = [[opn_gw[k0], opn_rpo[k0] - (EDF if k0 <= '2024Q2' else 0)]]; pred = act = 0.0
    for k in K[i0:i0 + n]:
        need = Q[k][0]
        while need > 1e-9:
            gq, u = stack[0]; t = min(gq, need); pred += u * t / gq
            stack[0] = [gq - t, u - u * t / gq]; need -= t
            if stack[0][0] < 1e-9: stack.pop(0)
        act += Q[k][1]; stack.append([Q[k][2], ords[k]])
    return act / pred
for n in (4, 8, 10, 12, 14):
    r = [backtest(i, n) for i in range(len(K) - n + 1)]
    print(n, 'quarters:', len(r), 'windows, min %.2f max %.2f mean %.3f' % (min(r), max(r), sum(r) / len(r)))
lay = [(Q[k][2], ords[k]) for k in K[8:]]                                           # firm layers at 6/30/26: Q1 2025 .. Q2 2026, plus the older remainder
lay = [(53 - sum(a for a, _ in lay), 39261 - sum(b for _, b in lay))] + lay
def book(gw, P):                                                                    # $M in the first gw GW: firm layers, then reservations and open slots at P $/kW
    c, left = 0.0, gw
    for a, b in lay:
        t = min(a, left); c += b * t / a; left -= t
    return c + left * P
paths = {'July plan': [5]*6 + [5.5, 5.5, 6, 6] + [6.5]*4 + [7.5]*6,
         'September ladder': [5]*4 + [5.5, 6, 6, 6, 6.5, 7] + [7]*4 + [7.5]*6,
         'slip': [4.5]*4 + [5]*4 + [5.5]*2 + [6]*4 + [6.75]*4 + [7]*2}
kk = {'end-2028': (0.87, 0.918, 0.97), 'end-2029': (0.93, 0.955, 0.98), 'end-2030': (0.93, 0.955, 0.98), 'Q2 2031': (0.93, 0.955, 0.98)}
for e, n in N.items():
    for p, v in paths.items():
        gw = sum(v[:n])
        print(e, p, 'GW %.1f' % gw, 'Street %.0f' % street[e],
              ' '.join('P=%d: %+.1f%%/%+.1f%%/%+.1f%%' % ((P,) + tuple(100 * (book(gw, P) * k / street[e] - 1) for k in kk[e])) for P in (750, 825, 900)))
```
