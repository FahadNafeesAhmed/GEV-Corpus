# Checker: the 13 wedge tests applied to "power-equipment-fy28-fy29"

_Research input only (facts, arithmetic, sources). No memo sentences, no forecast chosen for the team. Bloomberg figures cited as "Bloomberg, 2026-10-01"; keep inside the project folder._

Candidate: Power segment equipment revenue, FY2028 (physical lens) and FY2029 (price-implied lens), direction long, stated gap +17%.

## 0. Verdict

**Does not survive.** Passes 4 of 13 tests, fails 9. Two of the four mandatory tests fail (error band, reveal date).

| # | Test | Result | One-line reason |
|---|---|---|---|
| 1 | Line-item | PASS (qualified) | Named line, sourced Street figure, named year. But two years are offered and the two lenses disagree on FY2028. |
| 2 | Consensus-side | PASS (qualified) | It rebuts the Bloomberg mean, not an outlier. The number of brokers on this division line is not in the exports. |
| 3 | Distance | PASS (conditional) | FY2028 +14% to +17% at 22-23 GW. It is -1% to +2% at 20 GW, and FY2029 falls to +6% once the same haircut is applied. |
| 4 | Ratio | FAIL | Profit effect is +3% to +10% of FY2028 EBITDA. Average sell-side target is +24%. Most of any return would be multiple. |
| 5 | Physical quantity | FAIL | Street = 19.6 GW at the signed price OR 23 GW at $753/kW. Two unknowns, and the most GEV ever shipped in a year is 15.3 GW, so history does not refute the Street. |
| 6 | Rival explanation | FAIL | Price, volume, delivery order and aeroderivative timing all explain the same Street number; the candidate cannot tell them apart. |
| 7 | Error band | **FAIL (mandatory)** | Back-test error of the method on four-quarter windows is -27% to +25% (s.d. 14%). The gap claimed is +14% to +17%. |
| 8 | Why missed | FAIL (half) | The undisclosed delivery year is a real gap. But the price uplift is in the Q2 call and a per-class $/kW estimate is in a sell-side note. |
| 9 | Already priced | FAIL | Stock +51% year to date on this story; fell 8.7% on the day the key data was released. Not addressed by the candidate. |
| 10 | Cash | PASS (weak) | Moves EBITDA by +$0.4B to +$1.3B, but in 2028, and customer cash is already collected as deposits. |
| 11 | Reveal date | **FAIL (mandatory)** | FY2028 is reported in February 2029. The whole gap sits in H2 2028. Inside 12 months there is only guidance. |
| 12 | Counter-move | FAIL | Weak points are listed but none is stressed with numbers. |
| 13 | Multiple consistency | FAIL | No exit multiple or bear-case multiple is given. |

## 1. What was reproduced from primary files

All figures recomputed with Python from `segment_quarterly.json`, the workbook `GEV_bloomberg_pull_filled_2026-10-01.xlsx`, and the 10-Q / 10-K Power tables in `gev.db` (accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148).

| Item | Candidate says | Recomputed | Match |
|---|---|---|---|
| Street Power equipment, H2 2026 / 2027 / 2028 / 2029 / 2030 ($M) | 5,491 / 12,151 / 15,888 / 19,256 / 23,469 | 5,491 / 12,151 / 15,888 / 19,256 / 23,469 | yes |
| Power equipment RPO 6/30/26 and firm backlog | $39,261M, 53 GW | $39,261M (10-Q table), 53 GW | yes |
| Order $/kW (change in RPO + revenue, over GW ordered) | Q4'25 753, Q1'26 714, Q2'26 1,049, H1'26 915-916 | 753 / 714 / 1,049 / 916 | yes |
| H1'26 uplift over Q4'25 | +22% | +21.7% | yes |
| FY2028 layer dollars: flat / July plan / ladder | 17,439 / 20,586 / 23,058 | 17,439 / 20,586 / 23,058 | yes |
| Cycle conversion ratios | 0.99, 0.88, 0.80, 0.82, 0.93, 0.95 | 0.98, 0.88, 0.79, 0.82, 0.93, 0.95 | yes (rounding) |
| Residual 39,261 - 5,491 - 12,151 | 21,619 | 21,619 | yes |
| FY2028 revenue consensus 07-10 to 09-25 | 59,196 to 60,842 (+2.8%) | same | yes |
| FY2029: 26 x 790, 27 x 838, 28 x 875 | +7%, +17%, +27% | +6.7%, +17.5%, +27.2% | yes |

Only the last two cycle ratios use Street quarters (0.5 and 2.9 quarters). The four fully reported ones are 0.98, 0.88, 0.79, 0.82 (mean 0.87).

## 2. Test 7, error band (mandatory): fail

The method is: dollars of the backlog layers that ship in a period (oldest first), times a conversion ratio. Two back-tests on reported data.

**2a. First-in-first-out layers against reported revenue.** Stack starts at 12/31/22 (20.9 GW, $9,679M after removing the $3.9B EDF item). Each quarter ships the reported GW from the oldest layers. The stack ends at 52.1 GW / $38.4B on 6/30/26 against the reported 53 GW / $39.3B, so the bookkeeping ties.

| Window | Reported $M | Layer prediction $M | Reported / predicted |
|---|---|---|---|
| FY2023 | 5,598 | 6,391 | 0.88 |
| FY2024 | 5,708 | 6,168 | 0.93 |
| FY2025 | 6,685 | 7,044 | 0.95 |
| H1 2026 | 3,850 | 3,131 | 1.23 |
| Q3'24-Q2'25 | | | 0.73 |
| Q4'24-Q3'25 | | | 0.75 |
| Q3'25-Q2'26 | | | 1.25 |
| All 11 rolling four-quarter windows | | | min 0.73, max 1.25, mean 0.95, s.d. 0.14 |
| Single quarters | | | 0.53 to 1.85 |

**2b. The one forward window where the company has guided.** H2 2026: layers give $4,793M before haircut, $4,314M at 0.90. The Street has $5,491M, and its Power total for H2 2026 matches the company's Power revenue guide (the guide is for Power in total; the equipment split is the Street's). That is 27% above the method. So in the nearest period the method already misses by more than the gap it claims for 2028.

**2c. Size of error against size of gap.**

| Source of error | Size | Effect on the FY2028 July-plan figure |
|---|---|---|
| Rolling four-quarter back-test (known GW) | s.d. 14%; range -27% to +25% | $15.0B to $25.7B (-5% to +62%) |
| Cycle conversion ratio | 0.79 to 0.98 | $16.3B to $20.2B (+2% to +27%) |
| GW shipped in 2028 (not back-testable) | 20 / 22 / 23 / 25.5 GW | -1% / +11% / +17% / +31% at 0.90 |
| Gap claimed | | +14% to +17% |

The back-test error with GW known is as large as the gap. The GW path adds a second error of about the same size. Combined (in quadrature) about +/-18% on the candidate's value.

**2d. The gap is a timing allocation.** Over the whole span the Street is close to the backlog:

| Period (July plan, x0.90) | Method $M | Street $M | Gap |
|---|---|---|---|
| H2 2026 | 4,314 | 5,491 | -21% |
| FY2027 | 12,494 | 12,151 | +3% |
| H1 2028 | 7,196 | 7,099 | +1% |
| H2 2028 | 11,332 | 8,790 | +29% |
| H2 2026 to end-2028, cumulative | 35,335 | 33,530 | +5.4% (x0.93: +8.9%; x0.80: -6.3%; x0.99: +15.9%) |

The cumulative gap is +5% to +9%, inside the conversion band. The FY2028 gap exists because the method puts the whole Q2 2026 layer (12.1 GW, $12,696M, $1,049/kW) into H2 2028.

## 3. Test 11, reveal date (mandatory): fail

- FY2028 Power equipment revenue is in the 10-K filed February 2029. H2 2028, where the whole gap sits, starts 21 months from now.
- The 10-Q backlog schedule (36% / 65% within 1 / 2 years) runs to Q2 2028. It stops exactly where the gap starts, so no filed schedule inside the horizon can show it.
- Proxies offered, and what each can show:

| Date | Proxy | Problem |
|---|---|---|
| 2026-10-28 | Q3 gas GW sold of 4.8 or more | Management already guided 5 GW in Q3 and Q4; Street Q3 Power revenue sits on the company's Q3 guide. A pass confirms the Street. |
| 2026-10-28 | Equipment RPO per firm GW of $780/kW or more | Rises automatically as old layers ship; says nothing about which year the new layers deliver. |
| Late January 2027 | FY27 Power growth guide of 21% or more; 2027 output of 21 GW or more | Guidance for FY2027, a year where the proposal itself found no gap. Not a reported result. First outlook under a new CFO (8-K 0001996810-26-000153). |
| Spring 2027 (no date set) | 2028 output of 24 GW or more restated | 24 GW in 2028 has been public since 2025-12-09 and was repeated 2026-07-22. A restatement is not new information. |

None is a company-reported number for the named line and period.

## 4. Test 6, rival explanation: fail

**4a. The Street figure fits the plan volume at an older price as well as it fits flat volume at the new price.**

| Reading of Street FY2028 $15,888M | GW | $/kW before haircut | Haircut |
|---|---|---|---|
| Candidate's reading: output does not ramp | 20 | 872 | 0.91 |
| Plan volume at the Q4 2025 order price | 23 | 753 | 0.915 |
| Plan volume at backlog average on 6/30/26 | 23 | 741 | 0.93 |
| Ladder volume at Q1 2026 order price | 25.5 | 714 | 0.87 |

**4b. The company's own 2028 outlook already contains about 24 GW and lands on the Street.** Investor update 2025-12-09 (gevernova.com `gev_webcast_presentation_12092025.pdf`, corpus source 1844): Power revenue "up high teens" from 2025 to 2028; assumptions listed as pricing "reflecting recent orders" and gas deliveries "increasing to ~24 GW in '28"; "sold out on new equipment through '28". FY25 Power revenue $19,767M at 17% / 18% / 19% a year = $31.7B / $32.5B / $33.3B. Street FY2028 Power = $33,521M (19.25% a year). So the Street is not on a no-ramp path; it is on (slightly above) the company's own with-ramp path. For the candidate to hold, the company's outlook has to be about $3B low on Power equipment while its 2028 slots were already sold. Possible (the assumption reads "recent orders", not reservation prices; the update said "opportunities for upside"), but not shown.

**4c. Aeroderivative timing.** The Q2 2026 layer contains 61 aeroderivative units. Regression value $69M a unit = $4.2B; BNP estimate $1,800/kW x about 2.3 GW = $4.1B (Utility Dive 2026-07-22). Aeroderivatives have shipped about three to four quarters after order (27 ordered Q2 2025; 11 / 10 / 16 sold in Q4 2025 / Q1 2026 / Q2 2026). The method ships them last, in H2 2028. If they ship in 2027 and older heavy-duty units move into 2028:

| 2028 GW | FY2028 as proposed (x0.90) | With the 61 aeroderivatives shipped in 2027 | vs Street |
|---|---|---|---|
| 22 | 17,583 (+11%) | 15,354 to 15,416 | -3% |
| 23 | 18,528 (+17%) | 16,298 to 16,360 | +3% |

Recent quarters support this: reported / FIFO was 1.58, 1.19, 1.27 in Q4 2025, Q1 2026, Q2 2026, i.e. dollars are arriving ahead of the oldest-first order. Aeroderivatives ordered in 2027 would add back to 2028, but that volume is not in backlog and is a forecast.

**4d. "24 GW in 2028" is an annualised rate.** Q2 2026 call (source 3161): "that next step-up in output in '28 to 24 gigawatts annualized". Calendar-2028 output on the July wording is 22 GW (5, 5, 6, 6) to 24 GW, not a firm 23-24.

## 5. Tests 1-3: pass, with limits

- **Line-item.** `Total Revenue|Power|Equipment`, FY2028 $15,888M, Bloomberg 2026-10-01. Named and sourced. The candidate offers two periods and its lenses disagree on FY2028, which breaks the "one line, one period" form.
- **Consensus-side.** The figure rebutted is the mean. Limits: the exports give no broker count for division lines; the Power organic-growth line is 18.0 in every quarter of 2027-28 and 9.0 in 2029-30 (one broker); Power RPO jumps $19B between Q4 2028 and Q1 2029 (contributor change); equipment + services differs from the Power total by -1.4% (2029) and +1.4% (2030). Headline FY2028 EBITDA has 33 estimates with a standard deviation of $2,235M (17.8% of the mean).
- **Distance.** FY2028: +8% to +20% at 22-23 GW and haircut 0.88-0.93, centre about +14%. At 20 GW -1% to +2%. FY2029: the price-implied lens applied no haircut. With the same 0.90 the physical lens uses:

| FY2029 | No haircut | x0.90 | x0.93 |
|---|---|---|---|
| 26 GW x $790 | 20,540 (+6.7%) | 18,486 (-4.0%) | -0.8% |
| 27 GW x $838 | 22,626 (+17.5%) | 20,363 (+5.8%) | +9.3% |
| 28 GW x $875 | 24,500 (+27.2%) | 22,050 (+14.5%) | +18.3% |

FY2029 centre drops from +17% to about +6%, below the 7% floor, and its price input (the 63 GW reservation book) is not disclosed.

## 6. Tests 4, 5, 8, 9, 10, 12, 13

- **Ratio (fail).** EBITDA effect +$0.4B to +$1.3B = +3.2% to +10.4% of Street FY2028 $12,553M. At today's EV / FY2028 EBITDA of 20.3x that is $30 to $99 a share (3% to 10%). Average sell-side target $1,225.32 is +24.1%. Target return over estimate gap = 2.4x to 8x. The candidate gives no evidence for the multiple. The effect is 0.2 to 0.6 of one standard deviation of analyst FY2028 EBITDA estimates.
- **Physical quantity (fail).** The Street converts to GW only after choosing a price, or to a price only after choosing GW. Check against own history: most GW ever shipped in a year is 15.3 (2025); H1 2026 annualised is 15.0; Q2 2026 was 3.3. Street-implied 19.6 GW is above anything achieved, so history does not show the Street is low. The only thing it is low against is a plan. Deriving $/kW takes ten filings of differencing, not seconds.
- **Why missed (fail on the second half).** Real gap: GEV does not disclose delivery year by order or $/kW; Bloomberg has no gas GW line. But: "first half 2026 orders were priced more than 20% above 4Q'25" and the H2 2026 guide are in the Q2 call; 24 GW in 2028 is in the December 2025 deck and the July release; BNP Paribas published a $/kW estimate by turbine class on results day. The one input that is truly missing (which orders fill 2028 slots) is also missing for the candidate.
- **Already priced (fail).** Since early December 2025: FY2028 revenue consensus +16.3% (52,294 to 60,842), FY2028 EBITDA consensus +35% (9,264 to 12,511), share price +51% from year-end ($653.57 to $987.45). On 2026-07-22, the day the $1,049/kW quarter and the 24 GW / 30 GW path were released, the stock fell 8.7% ($1,078.81 to $985.03). After the September ladder it rose about 4.8% ($882.81 to $924.93) while FY2028 revenue consensus moved +0.2%. The candidate does not say how much of the move remains. The companion price-implied file states the arithmetic upside is about what the price already needs.
- **Cash (weak pass).** It moves EBITDA, not a label. Limits: nothing inside 12 months; slot deposits are already received, so the cash line moves less than EBITDA.
- **Counter-move (fail).** Not stressed. Items to stress separately: (a) customers defer delivery for site, labour or grid reasons (revenue slips a year; price unchanged); (b) management sets the first FY2027 outlook low under a new CFO; (c) supply of castings and forgings limits the step to 6 GW a quarter; (d) Siemens Energy and Mitsubishi add capacity for 2029-30 slots (affects the FY2029 price leg, not the signed 2028 layers); (e) scope shifts between equipment and services lines.
- **Multiple consistency (fail).** No exit multiple or bear multiple in the candidate. Forward EV/EBITDA is 28.5x; lowest weekly close of the last 12 months is 27.3x. A +3% to +10% EBITDA change does not offset a move to the low-20s.

## 7. Corrected figures (ranges, method stated; not a forecast)

| | Street (Bloomberg, 2026-10-01) | Corrected range | Gap |
|---|---|---|---|
| FY2028 Power equipment, 22-23 GW, haircut 0.88-0.93 | $15,888M | $17.2B to $19.1B, centre about $18.1B | +8% to +20%, centre +14% |
| Same, aeroderivatives of Q2 2026 shipped in 2027 | | $15.4B to $16.4B | -3% to +3% |
| Same, output flat at 20 GW | | $15.3B to $16.2B | -3% to +2% |
| Full band (20-25.5 GW, ratio 0.79-0.98) | | $13.8B to $22.6B | -13% to +42% |
| H2 2026 to 2028 cumulative, July plan | $33,530M | $35.3B to $36.5B | +5% to +9% |
| FY2029 with 0.90 haircut | $19,256M | $18.5B to $22.1B, centre $20.4B | -4% to +15%, centre +6% |

Error band on the FY2028 centre: about +/-18% (method s.d. 14% and GW path, combined).

## 8. What would change this verdict

1. A filed or stated delivery-year split of the 53 GW backlog (none exists today).
2. A back-test of the layer method on four-quarter windows with error under about 7%. The current one is 14%.
3. A company-reported number inside 12 months that the flat reading and the ramp reading predict differently. Today both predict 5 GW a quarter through mid-2027.
4. Broker-level detail on the Power equipment line for FY2028 (count, high, low).

## 9. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
EQ = 'Total Revenue|Power|Equipment'
st = {y: sum(d[f'{EQ}|{y} Q{q}'] for q in range(1, 5)) for y in (2027, 2028, 2029, 2030)}
# quarter: (GW sold, Power equipment revenue $M, GW ordered, Power equipment RPO end $M), 10-Q/10-K Power tables
Q = {'2023Q1': (3.6, 1180, 2.3, 13992), '2023Q2': (2.3, 1147, 2.1, 13980), '2023Q3': (2.7, 1291, 3.1, 13865),
     '2023Q4': (5.2, 1980, 2.1, 13636), '2024Q1': (2.3, 1201, 4.9, 14394), '2024Q2': (1.5, 1285, 4.1, 10978),
     '2024Q3': (3.3, 1426, 5.1, 11392), '2024Q4': (4.8, 1796, 6.1, 12461), '2025Q1': (3.0, 1491, 7.1, 13920),
     '2025Q2': (5.2, 1504, 5.1, 16133), '2025Q3': (4.0, 1744, 7.4, 18977), '2025Q4': (3.1, 1946, 10.2, 24707),
     '2026Q1': (4.2, 1885, 8.0, 28530), '2026Q2': (3.3, 1965, 12.1, 39261)}
keys = sorted(Q); prev = 13579; stack = [[20.9, 9679.0]]; pred = {}
for k in keys:
    gs, rev, go, rpo = Q[k]
    need, p = gs, 0.0
    while need > 1e-9:                       # ship reported GW from the oldest layers
        g, u = stack[0]; t = min(g, need); p += u * t / g
        stack[0] = [g - t, u - u * t / g]; need -= t
        if stack[0][0] < 1e-9: stack.pop(0)
    pred[k] = p
    stack.append([go, rpo - prev + rev + (3900 if k == '2024Q2' else 0)]); prev = rpo
ratios = [sum(Q[k][1] for k in keys[i:i+4]) / sum(pred[k] for k in keys[i:i+4]) for i in range(len(keys) - 3)]
print(min(ratios), max(ratios))              # 0.73, 1.25
```
Price path: `gev.db` table `prices` (GEV). Consensus history: workbook sheet `ConsensusHistory`. Company framework: corpus source 1844. Call quotes: corpus source 3161. September conference summary: corpus source 681.
