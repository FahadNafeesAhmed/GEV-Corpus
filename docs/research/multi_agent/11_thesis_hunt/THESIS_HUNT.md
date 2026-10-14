# Thesis hunt: final research report (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences. The team writes every sentence, chooses every forecast number, every pass mark and the direction. Bloomberg data is licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep it inside the project folder._

Working date 2026-10-01. Price $987.45. All figures $M unless stated.

Terms used:
- **Street**: Bloomberg BEst mean consensus, 2026-10-01.
- **RPO**: remaining performance obligations. Signed orders not yet delivered. GEV calls it backlog.
- **Schedule (Y1)**: equipment RPO x the share GEV's 10-Q says it will recognise "within 1 year". A dollar amount for the next four quarters.
- **Uplift**: actual next-four-quarter equipment revenue divided by Y1. Above 1.00 means extra orders were booked and shipped inside the year.
- **NTM EBITDA**: adjusted EBITDA for the next twelve months. The stock is valued as a multiple of it.
- **Drop-through**: adjusted EBITDA earned on each extra dollar of revenue.
- **Error band**: how far the method has missed reported numbers in the past (one standard deviation).
- **Wedge**: one number that differs from the Street and that the pitch rests on.
- **Roll-forward**: the return earned if the Street's own numbers come true and the multiple does not change.

Inputs: seven candidates from ten search lenses (`propose_*.md`), three checks on each (`verify_*.md`), one deepened file (`candidate_equipment-revenue-vs-rpo-schedule.md`), three judges. For this report the key figures were recomputed with Python from the primary files (list in section 8).

---

## 1. Result in five lines

1. **No candidate meets the winners' definition.** Winners put one number 7-22% from consensus on one line, with a method error smaller than the gap. Here every gap is either under 7% or smaller than its own error band.
2. **Best candidate:** equipment revenue for Q3 2026 to Q2 2027. GEV's own filed backlog schedule gives $31,616M. The Street has $30,245M. The fact is true and a judge can check it in seconds. It is too small to carry a pitch alone.
3. **Direction:** it leans long, weakly. Both short candidates were killed. No number found supports a short.
4. **Gap against its error band:** +4.5% as printed; +2.7% to +3.5% on a corrected Street; +5% to +7% at the checkers' centre (uplift 1.00-1.03). Error band +/-4.5% to +/-7%. So the gap is 0.4 to 1.6 times its error. On adjusted EBITDA it is +1.5% to +6.6% for the four quarters, and about -3% to +6.6% (centre near +1%) after the services and Wind offsets.
5. **Judges:** 3 of 3 say "no winning thesis" and name no winner. 3 of 3 rank the equipment schedule first. They differ on three points (table below).

| Judge | Winner | Score for the best candidate (each judge used its own scale) | Second place | Main reason | What it says to do next |
|---|---|---|---|---|---|
| Portfolio-manager view | none | 48 | FY26 free cash flow | Timing, not level. At 10-12 months the NTM window no longer holds the thesis quarters. Net EBITDA effect centres near zero | Present the long openly as a call on the multiple, with the schedule as one supporting fact |
| Playbook view | none | 5 | FY26 free cash flow | Passes 3 of 6 parts (arithmetic, dated test, honest return split). Fails distance, error band, attack | Move the claim to the FY27 equipment line using the one-year and two-year shares (new arithmetic, not yet checked; section 9.3) |
| Statistician view | none | 4.5 | Wind FY27 and FY26 free cash flow, tied | Gap is 0.4 to 1.2 standard errors. The best of 7 candidates is expected to show 1.35 by luck alone. The schedule has shown no forecasting skill beyond a plain growth rule | Get a longer back-test from peers that file the same sentence. Fix one pairing and one pass mark before 2026-10-28 |

No judge found a candidate that was wrongly killed.

---

## 2. The best candidate as X, Y, Z and date

Line: **consolidated equipment revenue**. Period: **Q3 2026 to Q2 2027** (four quarters, across FY26 and FY27).

| | Number | Source and method |
|---|---|---|
| **X: what the Street expects** | **$30,245M** = 7,482 / 8,339 / 6,675 / 7,748 by quarter. Other fair readings of the same line: $29.5B to $30.8B | Bloomberg, 2026-10-01. `GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx`, sheet "Multiple Periods", rows 24 + 27 + 30, columns F:I. Same as `segment_quarterly.json` keys `Total Revenue\|Power\|Equipment`, `...\|Wind\|Equipment`, `...\|Electrification\|Equipment` |
| **Y: what the price implies** | $987.45 = (28.54 x 8,923 + 8,298) / 266.334. NTM EBITDA of $8,923M is the Street. So the price implies X. Break-even multiple on Street numbers: 26.2x (late January 2027), 22.6x (late July 2027), 21.6x (1 October 2027) | Snapshot sheet, row 3. 254,694 / 28.544 = 8,923 |
| **Z: arithmetic on disclosed data** | Schedule alone: **$31,616M** ($31,176M to $32,055M for rounding of the 36%). With uplift 1.00-1.03: **$31.6B to $32.6B**. $29.0B if the one past miss (0.918) repeats | 10-Q Q2 2026, accession 0001996810-26-000148, RPO note: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years". 87,821 x 0.36 |
| **Gap, Z vs X** | +4.5% floor on the printed Street. +2.7% to +3.5% on a corrected Street. +5% to +7% at the checkers' centre. Full range +1% to +11% | Matrix in 2.3 |
| **Error band on Z** | +/-4.5% to +/-7% | Back-test in 2.2 |
| **D: the date you find out** | First read 2026-10-28 (Q3 10-Q, new one-year amount). Main read late January 2027 (10-K one-year amount, FY27 guide). Final late July 2027 (Q2 2027 10-Q) | Company events page; prior report dates |

### 2.1 Proof table (each step can be redone by hand)

| Step | Arithmetic | Result | Where |
|---|---|---|---|
| 1 | Equipment RPO at 6/30/26 x one-year share | 87,821 x 36% = **31,616** | 10-Q Q2 2026 RPO note (corpus chunk 5683) |
| 2 | Street equipment revenue, four quarters, three divisions | Power 10,874 + Wind 5,830 + Electrification 13,541 = **30,245** | Bloomberg rows 24, 27, 30 |
| 3 | Step 1 / step 2 | **+4.5%** (+$1,371M) | |
| 4 | Same sum for seven finished windows: actual next-four-quarter equipment revenue / Y1 (Prolec removed) | 0.918, 1.028, 1.036, 1.076, 1.105, 1.052, 1.066. Mean 1.040, standard deviation 0.060 | Table 2.2 |
| 5 | Street / Y1 for the current window | 0.957. Below six of seven finished windows | |
| 6 | Wind cannot absorb the gap | Street has Wind converting 5,830 / 8,197 = 71.1% of its equipment backlog. Reported range 58.5% to 69.3%. For Power + Electrification on the Street to equal the schedule, Wind would need 87.8% | 10-Q segment RPO tables |
| 7 | Sign check on eight Street readings (means, medians, consolidated basis, services-row fix; share at 35.5% and 36%) | Schedule is above the Street on all eight | `verify_equipment-revenue-vs-rpo-schedule_already-known.md` |

### 2.2 Back-test: every window since the schedule was first filed

| Backlog date | Equipment RPO | 1-yr share | Scheduled (Y1) | Next 4 quarters, Prolec removed | Ratio | Growth the schedule asked for | Growth delivered |
|---|---|---|---|---|---|---|---|
| 12/31/23 | 40,478 | 51% | 20,644 | 18,952 | 0.918 | +13.1% | +3.8% |
| 3/31/24 | 42,210 | 45% | 18,994 | 19,532 | 1.028 | +3.3% | +6.2% |
| 6/30/24 | 41,561 | 47% | 19,534 | 20,232 | 1.036 | +7.4% | +11.2% |
| 9/30/24 | 42,069 | 46% | 19,352 | 20,822 | 1.076 | +4.0% | +11.9% |
| 12/31/24 | 43,047 | 44% | 18,941 | 20,934 | 1.105 | -0.1% | +10.5% |
| 3/31/25 | 45,478 | 45% | 20,465 | 21,522 | 1.052 | +4.8% | +10.2% |
| 6/30/25 | 49,712 | 42% | 20,879 | 22,253 | 1.066 | +3.2% | +10.0% |
| 9/30/25 (open, 1 Street quarter) | 54,092 | 41% | 22,178 | | 1.03 to 1.04 | +6.5% | open |
| 12/31/25 (open, 2 Street quarters) | 64,245 | 37% | 23,771 | | 1.02 to 1.03 | +13.6% | open |
| 3/31/26 (open, 3 Street quarters) | 75,924 | 38% | 28,851 | | 1.004 | +31.2% | open |
| **6/30/26 (all Street)** | 87,821 | 36% | **31,616** | **30,245** | **0.957** | **+34.2%** | Street +28.4% |

What the back-test does and does not show:

| Fact | Number | Meaning |
|---|---|---|
| Ratio, seven windows | mean 1.040, standard deviation 0.060 | One miss in seven |
| Windows overlap | about 2 to 2.5 independent years | Predictive error about 7% |
| Leave-one-out error of "Y1 x mean ratio" | 6.4% to 6.7% | About the size of the gap |
| Leave-one-out error of a plain rule (last four quarters x average growth) | 3.0% to 3.2% | The plain rule did better. Today it gives about $28.0B, below the Street |
| Correlation of the ratio with the growth the schedule asked for | -0.93 | The schedule was beaten when it asked for little. The one window that asked for double digits missed by 8% |
| Correlation of delivered growth with growth asked for | -0.60 | No sign yet that a bigger schedule means bigger growth |
| Range of Y1 in the sample | 18.9B to 20.9B. Today 31.6B | The method is being used outside the range it was measured on |
| Open windows on reported quarters | Tracking 1.00 to 1.04, not 1.05 to 1.10 | Supports an uplift of 1.00-1.03 |

### 2.3 The gap on every pairing

| Street reading | 35.5% share (31,176) | Schedule (31,616) | x1.02 (32,248) | x1.03 (32,564) | x1.04 (32,880) | x0.918 (29,023) |
|---|---|---|---|---|---|---|
| Consolidated basis (30,125) | +3.5% | +4.9% | +7.0% | +8.1% | +9.1% | -3.7% |
| **Division means, printed (30,245)** | +3.1% | **+4.5%** | +6.6% | +7.7% | +8.7% | -4.0% |
| Services row corrected (30,545 to 30,685) | +1.6% to +2.1% | +3.0% to +3.5% | +5.1% to +5.6% | +6.1% to +6.6% | +7.2% to +7.6% | -5.0% to -5.4% |
| Scaled to Q3 medians (30,781) | +1.3% | +2.7% | +4.8% | +5.8% | +6.8% | -5.7% |

- Do not use the +8.7% headline. It is the top corner of this table and needs an uplift the latest data do not support.
- Do not use the "gap sits in H1 2027" form. It assumes H2 2026 lands exactly on the Street.

### 2.4 Same finding on broader lines

| Line (same four quarters) | Street | Arithmetic range | Gap |
|---|---|---|---|
| Total revenue (22-28 brokers) | 50,019 | 50,400 to 52,700 | +0.8% to +5.3% |
| Power + Electrification equipment | 24,415 | 25,300 to 26,300 | +3.8% to +7.7% |
| Adjusted EBITDA | 8,210 | +137 to +541 on top | +1.7% to +6.6%; -3% to +6.6% if Street services are too high |

---

## 3. From the number to profit and to price

### 3.1 Profit effect by size of the revenue gap (four quarters, against the printed Street)

| Case | Equipment revenue | Extra revenue | Total revenue | EBITDA at 10% drop-through | at 13% | at 20% |
|---|---|---|---|---|---|---|
| 35.5% share, no uplift | 31,176 | +931 (+3.1%) | +1.9% | +93 (+1.1%) | +121 (+1.5%) | +186 (+2.3%) |
| Schedule, no uplift | 31,616 | +1,371 (+4.5%) | +2.7% | +137 (+1.7%) | +178 (+2.2%) | +274 (+3.3%) |
| x1.02 | 32,248 | +2,003 (+6.6%) | +4.0% | +200 (+2.4%) | +260 (+3.2%) | +401 (+4.9%) |
| x1.03 | 32,564 | +2,319 (+7.7%) | +4.6% | +232 (+2.8%) | +302 (+3.7%) | +464 (+5.7%) |
| x1.04 | 32,880 | +2,635 (+8.7%) | +5.3% | +264 (+3.2%) | +343 (+4.2%) | +527 (+6.4%) |
| Downside: 0.918 repeats | 29,023 | -1,222 (-4.0%) | -2.4% | -122 (-1.5%) | -159 (-1.9%) | -244 (-3.0%) |

EBITDA percentages are of the Street's $8,210M.

Evidence for the drop-through range:

| Range | Evidence |
|---|---|
| 10% to 13% | Equipment gross margin: 10.4% (FY25), 11.8% (H1 2026), 13.1% (Q2 2026) |
| 14% to 20% | Extra equipment gross profit per extra dollar: 13.9% (Q2 2026), 18.1% (H1 2026). Street segment margins for the window: Power 20.0%, Electrification 19.3% |
| Break point | Below 16.4% (the Street's average margin for the window) the margin percentage falls even though dollars rise |

Offsets found by other lenses (ranges; the team decides whether to carry them):

| Offset | Size against the Street | Evidence |
|---|---|---|
| Services | 0 to -$1.25B revenue; -$150M to -$310M EBITDA at the centre | Street services are 1.398x the 16% services schedule. History 1.24x to 1.365x |
| Wind FY27 | -$175M to -$255M EBITDA at the mid-points (range $0 to -$540M) | Street +$188M is a mean of about four models with one high outlier. Method error about +/-$300M |
| Net, next four quarters | EBITDA -5% to +7%, centre about +1% | `propose_street-identity.md` section 5 |

Free cash flow: +$0.10B to +$0.43B if cash follows profit; about zero if the deposits were already collected. The sign is not identified. Free cash flow is not the line for this candidate.

### 3.2 Which NTM EBITDA the finding can move

| Valuation date | Street NTM EBITDA | Do the thesis quarters (Q3'26-Q2'27) sit in the NTM window? |
|---|---|---|
| Late January 2027 | 9,727 | Yes, H1 2027 only |
| Late April 2027 | 10,498 | Q2 2027 only |
| Late July 2027 | 11,269 | No |
| 1 October 2027 | 11,783 | No |

- At 10-12 months the direct effect on forward EBITDA is zero. Any effect needs brokers to carry the higher level forward.
- Months 13-24 show no gap (Street 35,137 against 25,468 scheduled). That points to timing, not level.
- If brokers did carry it forward in full: NTM EBITDA +1.8% to +5.8%.

### 3.3 Price grid

Bridge: price = (multiple x NTM EBITDA + 8,298) / 266.334. All cells recomputed for this report. Rows are paths for NTM EBITDA against the Street. The team picks the path its model supports.

**Late January 2027** (Street NTM 9,727; break-even multiple 26.2x; roll-forward at 28.54x +8.7%)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 9,727 | $798 (-19%) | $871 (-12%) | $930 (-6%) | $981 (-1%) | $1,028 (+4%) | $1,072 (+9%) | $1,127 (+14%) | $1,218 (+23%) |
| +1.5% | 9,873 | $810 (-18%) | $884 (-10%) | $943 (-4%) | $995 (+1%) | $1,043 (+6%) | $1,088 (+10%) | $1,143 (+16%) | $1,236 (+25%) |
| +3% | 10,019 | $821 (-17%) | $896 (-9%) | $957 (-3%) | $1,009 (+2%) | $1,058 (+7%) | $1,103 (+12%) | $1,160 (+17%) | $1,254 (+27%) |
| +5% | 10,214 | $837 (-15%) | $913 (-8%) | $975 (-1%) | $1,028 (+4%) | $1,078 (+9%) | $1,124 (+14%) | $1,182 (+20%) | $1,278 (+29%) |
| +6.6% | 10,369 | $849 (-14%) | $927 (-6%) | $989 (0%) | $1,043 (+6%) | $1,094 (+11%) | $1,141 (+16%) | $1,199 (+21%) | $1,297 (+31%) |
| -3% | 9,436 | $775 (-22%) | $846 (-14%) | $903 (-9%) | $952 (-4%) | $998 (+1%) | $1,041 (+5%) | $1,094 (+11%) | $1,183 (+20%) |

**Late July 2027** (Street NTM 11,269; break-even multiple 22.6x; roll-forward +25.5%)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 11,269 | $920 (-7%) | $1,004 (+2%) | $1,072 (+9%) | $1,131 (+15%) | $1,186 (+20%) | $1,237 (+25%) | $1,300 (+32%) | $1,406 (+42%) |
| +3% | 11,607 | $946 (-4%) | $1,034 (+5%) | $1,103 (+12%) | $1,164 (+18%) | $1,221 (+24%) | $1,273 (+29%) | $1,339 (+36%) | $1,448 (+47%) |
| +5% | 11,832 | $964 (-2%) | $1,053 (+7%) | $1,124 (+14%) | $1,186 (+20%) | $1,244 (+26%) | $1,297 (+31%) | $1,364 (+38%) | $1,475 (+49%) |
| -3% | 10,931 | $893 (-10%) | $975 (-1%) | $1,041 (+5%) | $1,098 (+11%) | $1,152 (+17%) | $1,201 (+22%) | $1,262 (+28%) | $1,365 (+38%) |

**1 October 2027** (Street NTM 11,783; break-even multiple 21.6x; roll-forward +31.0%)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 11,783 | $960 (-3%) | $1,049 (+6%) | $1,119 (+13%) | $1,181 (+20%) | $1,239 (+25%) | $1,292 (+31%) | $1,358 (+38%) | $1,469 (+49%) |
| +3% | 12,136 | $988 (0%) | $1,079 (+9%) | $1,152 (+17%) | $1,216 (+23%) | $1,275 (+29%) | $1,330 (+35%) | $1,398 (+42%) | $1,512 (+53%) |
| +5% | 12,372 | $1,007 (+2%) | $1,100 (+11%) | $1,174 (+19%) | $1,239 (+25%) | $1,299 (+32%) | $1,355 (+37%) | $1,425 (+44%) | $1,541 (+56%) |
| -3% | 11,429 | $932 (-6%) | $1,018 (+3%) | $1,087 (+10%) | $1,147 (+16%) | $1,203 (+22%) | $1,254 (+27%) | $1,319 (+34%) | $1,426 (+44%) |

### 3.4 How much of any target is the estimate and how much is the multiple

Points of return on $987.45. Roll-forward = Street numbers at today's 28.54x. Estimate = the change from the corrected path at 28.54x. Multiple = the rest.

| Date | Path | Exit multiple | Price | Total | Roll-forward | Estimate | Multiple |
|---|---|---|---|---|---|---|---|
| Late Jan 2027 | +3% | 24.6x | $957 | -3.1% | +8.7 | +3.2 | -15.0 |
| Late Jan 2027 | +3% | 27.3x | $1,058 | +7.2% | +8.7 | +3.2 | -4.7 |
| Late Jan 2027 | +5% | 28.5x | $1,126 | +14.0% | +8.7 | +5.3 | 0.0 |
| Late Jul 2027 | +3% | 24.6x | $1,103 | +11.7% | +25.5 | +3.7 | -17.4 |
| Late Jul 2027 | +5% | 28.5x | $1,299 | +31.6% | +25.5 | +6.1 | 0.0 |
| 1 Oct 2027 | Street | 27.0x | $1,225 (sell-side mean target) | +24.1% | +31.0 | 0.0 | -6.9 |
| 1 Oct 2027 | +3% | 24.6x | $1,152 | +16.7% | +31.0 | +3.8 | -18.2 |
| 1 Oct 2027 | +5% | 28.5x | $1,357 | +37.4% | +31.0 | +6.4 | 0.0 |

- The whole estimate leg is +1.6 to +8.4 points. That equals 0.4 to 1.9 turns of the multiple.
- One turn of the multiple is worth $36 to $44 a share (3.7% to 4.5%).
- Any target above about +10% is carried by the roll-forward and by the multiple holding. It is not carried by this finding.

Evidence on hand for the multiple (it has not been through the three checks as a thesis):

| Anchor | Level |
|---|---|
| Today | 28.5x (6th percentile of the last 12 months) |
| Last 52 weeks | low 27.3x, median 32.4x, high 42.4x. No week at or below 26x |
| March-April 2025 sell-off | 18.5x to 24.0x |
| Peer line (multiple against growth and margin, 11 peers) | 24.6x for late January 2027; 21.2x for late September 2027. R-squared 0.82, but 0.04 without Bloom Energy |
| Peers today | 10.9x to 22.3x |
| Report-day record | Moves above 13% all came with a margin-guide or framework raise. -8.7% on 2026-07-22 with a revenue beat and a held margin guide. Correlation of revenue surprise with the day move: -0.22 (seven reports) |

---

## 4. What the model must contain so it matches this finding

Existing workbook: `data/model/GEV_model_shell.xlsx`. It is annual and values on a P/E. The finding is a four-quarter window, so the model needs a half-year bridge.

| Tab | What to add | Formula in words |
|---|---|---|
| Backlog vintage | The 12/31/23 row; columns for next-four-quarter equipment revenue, Prolec, ratio, growth asked for | Ratio = (next four quarters - Prolec) / Y1 |
| Backlog vintage | Driver block "Conversion, Q3'26-Q2'27" | Window equipment revenue = Y1 x uplift. Uplift is one input cell (evidence range 0.92 to 1.04; the checks support 1.00 to 1.03). Switch for the share (35.5 / 36 / 36.5%) |
| Segments | Equipment and services by division, by half-year (H2'26, H1'27, H2'27) | Wind = Wind equipment RPO 8,197 x a turnover input (58% to 71%). Power + Electrification = total - Wind. The Power / Electrification split is an input; it is not disclosed. Share of Y1 that falls in H2'26 is an input (Street 50%; guide 47-51%; earlier June windows 57%) |
| Segments | Check row | Half-year build must equal the annual build (GW x $/kW for Power, growth for the rest) |
| Drivers | Drop-through on extra equipment revenue (10% to 30%); services ratio to its schedule (1.24 to 1.40); Wind FY27 EBITDA input | Extra EBITDA = (model equipment revenue - Street equipment revenue) x drop-through |
| P&L | Revenue, adjusted EBITDA, EPS for H2'26 and H1'27, then full years | |
| Cash | State whether the finding is left out of free cash flow or carried after tax as an upper case | |
| vs Consensus | Rows: window equipment revenue (30,245); H1'27 equipment (14,424); FY27 equipment (32,383); window total revenue (50,019); window EBITDA (8,210). Replace free-vendor placeholders with Bloomberg FY27 values 53,029 / 9,471 / 24.52 / 7,654 | Source column = file and cell |
| Valuation | EV/EBITDA bridge and the three-leg split (roll-forward, estimate, multiple) by date | Price = (multiple x NTM EBITDA + 8,298) / 266.334. Update the reference price to $987.45 |
| Scenarios | Rows read the same driver cells: uplift (0.918 / 1.00 / 1.03), drop-through, services ratio, exit multiple (bear anchored on 21x-24.6x; base 27.3x-28.5x; bull 30x-32.5x) | |
| Sensitivity | Two-way table: uplift x exit multiple at the chosen date | |
| Checks | Y1 = 31,616. Street window = 30,245. Bridge returns $987.45 at 28.544x and 8,923. Half-years sum to years. Every memo number equals a cell | |

Consistency check: the research supports window EBITDA of about -3% to +6.6% against the Street's $8,210M. A model far outside that range no longer matches the finding.

---

## 5. Dated tests, pass marks and the kill rule

All numbers are reported by GEV. Marks are candidates computed from the data. The team sets its own. Both main dates fall after the memo is handed in, so they can be written only as tests, not as proof.

| Date | Number GEV reports | Compare with | Pass (candidate) | Fail (candidate) |
|---|---|---|---|---|
| **2026-10-28**, Q3 10-Q | (a) New one-year amount = equipment RPO at 9/30/26 x new share | Street Q4'26-Q3'27 equipment 31,314 | 32,880 or more (+5%) | 31,314 or less |
| | (b) Q3 equipment revenue | Street 7,482 | 7,860 or more | below 7,300. Weak test: management's Q3 guide equals the Street |
| | (c) The 9/30/25 window closes: (Q4'25 to Q3'26 equipment less acquisitions) / 22,178 | 1.03 | Q3 organic equipment of 6,470 or more | below 5,805 (ratio under 1.00) |
| **Late January 2027**, 10-K and FY27 guide | (d) 10-K one-year amount at 12/31/26 | Street FY27 equipment 32,383 | 34,000 or more (+5%). 34,700 or more would put the distance above 7% with no uplift assumed | 32,383 or less |
| | (e) The FY26 window closes: (FY26 equipment less acquisitions) / 23,771. First finished window that asked for double-digit growth | 1.03 | 24,484 or more | below 23,771 |
| | (f) FY26 revenue | Guide top 46,500 | above 46,500 | below 45,500 |
| | (g) FY27 revenue guide midpoint | Street 53,029 | at or above the Street | not a fail alone: the January 2026 guide started 2-6% below its schedule and was raised twice |
| **Late April 2027**, Q1 10-Q | (h) Cumulative equipment revenue Q3'26 to Q1'27 | Street 22,497 | 23,712 or more (75% of Y1) | 22,497 or less |
| **Late July 2027**, Q2 10-Q | (i) Four-quarter equipment revenue | Street 30,245; schedule 31,616 | 31,616 or more | 30,781 or less |

Lookup for test (a): RPO at 9/30/26 (rows) x share printed (columns), against 31,314.

| RPO | 33% | 34% | 35% | 36% |
|---|---|---|---|---|
| 92,000 | 30,360 (-3.0%) | 31,280 (-0.1%) | 32,200 (+2.8%) | 33,120 (+5.8%) |
| 96,000 | 31,680 (+1.2%) | 32,640 (+4.2%) | 33,600 (+7.3%) | 34,560 (+10.4%) |
| 100,000 | 33,000 (+5.4%) | 34,000 (+8.6%) | 35,000 (+11.8%) | 36,000 (+15.0%) |

Kill-rule candidates (the team writes its own):

| # | Date | Condition | What it would show |
|---|---|---|---|
| K1 | 2026-10-28 | New one-year amount at or below $31.3B | The schedule no longer differs from the Street |
| K2 | Late January 2027 | FY26 organic equipment below $23,771M and the 10-K one-year amount at or below $32.4B | The first high-growth window missed and next year's schedule equals the Street |
| K3 | Any report | Cumulative equipment revenue from Q3 2026 more than 2% below the Street's path (7,482 / 15,821 / 22,497 / 30,245) | Slippage, as in the 12/31/23 window |
| K4 | Any date | A disclosed deferral or cancellation of scheduled deliveries above about $1.4B | Customer counter-move |
| Final | Late July 2027 | Four-quarter equipment revenue at or below $30.8B | No gap |

Risks set aside, each with the observation that would show it matters:

| Risk set aside | Observation that would show it matters |
|---|---|
| Rounding of the 36% | The next filing prints a share that implies Y1 fell |
| Soft Street sub-line | A terminal pull for Q4'26 to Q2'27 shows medians more than 3% above means |
| Deliveries slip | Gas GW shipped in Q3 2026 below 4.5 against the 5 GW guide |
| Revenue beats do not move the stock | Negative report-day move on 2026-10-28 with a revenue beat and a held margin guide |
| Size is perishable | FY27 revenue consensus moved +2.0% to +4.8% within 30 days of each of the last four reports. That is the size of the gap |

---

## 6. Every other candidate

| Candidate | Line and period | Direction | Claimed gap | Corrected gap | Error band | What killed it | Use that remains |
|---|---|---|---|---|---|---|---|
| FY26 free cash flow from H2 deposits | Free cash flow FY2026 | long | +19% | +2.5% to +4.4% like for like; 0% to +4.5% against the 15 brokers who publish quarters ($12,548M, already above the guide top) | 10% to 20% | The 1.79x overshoot came from a selected set of guides; the full-record median is 1.11x. Deposit models miss single quarters by 36-81%. A broker note of 2026-07-22 already says management under-guides. It is one-time cash worth $1-9 a share. The stock fell 8.7% the day the cash guide rose $5B | Supporting fact for a long: 7 of 8 past guide remainders finished at or above the top. Do not use the 9/30/26 contract-liabilities balance as a test |
| Power services FY2028 | Power services revenue FY2028 | short | -6.6% | about -5% (range -11% to +1%) | 5% to 6% | FY2028 is reported in January 2029. The benchmark chart is a stated floor; the CEO called it conservative on 2026-09-16. Clean trailing growth of non-contract services is 16%, which reproduces the Street. Services backlog due within five years grew 14% in a year | Mirror of the equipment finding: the same brokers have equipment low and services high |
| Power equipment FY2028-FY2029 | Power equipment revenue | long | +17% | about +8% (up to +14%) | 13% to 20% | Nothing prints inside 12 months. The whole FY2028 gap sits in H2 2028 and in one order layer whose price is lifted by aeroderivative mix. 24 GW x $735/kW x 0.90 reproduces the Street. A broker already publishes the 2030 version | Context for out-year EBITDA only |
| Electrification Q3 2026 orders | Electrification orders Q3 2026 | either | -20.6% | -14% to -20%; the sign flips with the base (-20% to +12%) | 30% to 37% | The CEO gave a share, not a level; the Street fits the same remark. Orders only: no revenue, profit or cash effect. Public since 2026-09-16 (stock +4.8% that day). Fails 9 of 13 tests | Dated accuracy check on 2026-10-28: below $5,775M is under every broker |
| Wind FY2027 EBITDA | Wind adjusted EBITDA FY2027 | short | -$255M (-136% of a near-zero line) | about -$190M to -$250M; 1.8% to 2.7% of company EBITDA | about $300M | The gap sits inside its error band. The Street figure is a mean of about four models with one high outlier. The loss ratio has no mechanical basis under loss-contract accounting. Management said the opposite on 2026-09-16 | Model input and known offset to the long side ($0.1B to $0.25B) |
| Wind H1 2027 equipment revenue | Wind equipment revenue Q1 + Q2 2027 | short | -23% | -11% to -13% | 13% to 17% | The premise was wrong: GEV prints Wind equipment orders in dollars every quarter, and on that series H1 2026 fell 20%, not 33-44%. The Street's needed ratio (1.29) is inside the observed range (0.95-1.30). Effect 0-2.5% of H1 2027 EBITDA | Supports the best candidate: Wind cannot absorb the schedule gap |

---

## 7. What was searched and showed no gap (do not repeat)

Ten lenses, 59 Bloomberg lines, 20 quarters. Each row is a line where arithmetic on disclosed data landed on the Street or bracketed it.

| Area | Line and period | Street | Arithmetic | Result |
|---|---|---|---|---|
| Company | Q3 2026 revenue and EBITDA against the quarter guide | 11,993; 1,672 | 11.8-12.1B; 1,543-1,766 | in line |
| Company | FY26 EBITDA against the guide | 6,334 (13.7% margin) | 12-14% guide; Q4 needs 18.0% | upper half of the guide |
| Company | H2 2026 orders against "$200B backlog very early in 2027" | 45.4B | year-end about $196B | consistent |
| Company | FY27 revenue from the 2028 framework growth rates | 53.0B | 52.5-53.0B | in line |
| Company | FY27 EPS rebuilt from Street EBITDA | 24.52 | about 24.1 | under 2% |
| Company | Consensus mean against median | FY27 EBITDA 9,471 | median 9,364 | 1-2.5% |
| Company | Free cash flow FY27 and FY29 | 7,654; 9,702 | depends on GW signed; $5.5-10B | band spans the Street |
| Company | Share count, interest income, tax | | | each under 3% of EPS |
| Schedule | Equipment, months 13-24 | 35,137 | 25,468 scheduled | no gap; earlier ordering |
| Schedule | Equipment, eight quarters | 65,382 = 1.145x the two-year schedule | history 1.28-1.48x | read as longer-dated orders; no gap claimed |
| Schedule | Services, four quarters, share of services RPO | 22.4% | 21.3-22.6% | inside |
| Schedule | Calendar 2027 total revenue | 53.0B | +0.8% to +5.7% | under the bar |
| Power | H2 2026 Power equipment | 5.49B | guide | Street equals the guide |
| Power | Power equipment Q3'26-Q2'27 | 10.87B | 10.5-12.3B | error 10-19% |
| Power | Power equipment FY2027 | 12.15B | 12.5-14.0B | band -9% to +22% |
| Power | Power equipment per kW, 2027 and 2028 | $552-662 | inside FY24-FY25 order prices | no gap |
| Power | Gas output ladder x order price, 2027-2030 | 12,151 to 23,469 | revenue per GW does not track order price (ratio 0.73 to 1.26) | band wider than gap |
| Power | Firm gas backlog against the shipment ladder to 2028 | 33.5B | Power equipment RPO 39.3B | consistent |
| Power | Power services Q3'26, Q4'26, next four quarters, FY27 | 3,389; 4,272; 14,955; 15,675 | inside to -3% | no gap |
| Power | Total Power revenue 2029-2030 | | equipment above and services below cancel | no gap |
| Power | Street gross margin against backlog margin | implied equipment margin 16% to 34% (2026-2030) | two readings bracket it | not provable |
| Power | Service-contract estimate changes | | -$319M, -$151M, -$218M; recurring | already in reported margins |
| Electrification | Revenue H2'26, next four quarters, Q1'27, FY27 | 8,169; 16,145; 3,671; 17,704 | +2% to +9%; about +4%; +3.5% to +4.8%; -0.3% to +10% | under the bar or band wider than gap |
| Electrification | Segment EBITDA Q3'26, Q4'26, FY27, 2028 | 745; 917; 3,774; 4,972 | methods bracket the Street | no gap |
| Electrification | Prolec margin and purchase accounting | | about $90M a year | not material |
| Wind | Revenue against the guide, H2 2026 and Q3 | 4,685; 2,341 | 4.5-4.8B; 2,303-2,382 | no gap |
| Wind | Equipment revenue against onshore-only backlog | 79.4% conversion | 72.8-85.1% | inside |
| Wind | Q4 2026 and FY26 Wind EBITDA | +208; -449 | H2 +90 to +365 | inside |
| Wind | FY2028 Wind revenue | 6,813 | 5,999-6,641 | 2.6% above the top; not a gap |
| Cash | Street cash build against Street free cash flow | +3.9B net cash | 5.1B less dividends and buybacks | consistent |
| Cash | Q3 2026 contract-liabilities consensus | median 39,944 | equals the last reported balance: a carry-forward, not a forecast | bad data; not a test |
| Price | Price at 28.5x | 8,937 needed | Street NTM 8,923 | price equals the Street |
| Price | Reverse DCF on Street free cash flow | | 86% of value after 2030; 2030 exit 16.2x at a 9% rate | context; no test inside 12 months |

Killed in earlier rounds (new evidence needed to reopen): "Street FY27 EBITDA is too high because of Power margin" (Street Power 21.0%, research 20.5%); "analysts flatten margins after 2028" (they do not); "the margin step is unprecedented"; "incremental margins are too high"; a rebuttal of the one Sell-rated analyst; reading plant price per kW straight into margin.

Street lines that are artefacts and should not be quoted: total RPO mean for Q3'26 and Q4'26 (one Wind outlier); Wind RPO; the total orders line (8% above the division sum in 2027); the FY26 EPS mean (24.39; median 28.68); division D&A lines; the Electrification services row; the Wind FY27 EBITDA mean (+188).

What the hunt did establish: on the line the price sits on (NTM EBITDA), disclosed data put the Street about right, within roughly +/-5%, in both directions.

---

## 8. Hand-checks before anything is used, and what is single-source

Recomputed for this report from the primary files (all matched):
- Street equipment by quarter and the 30,245 sum; H2'26 15,821; H1'27 14,424; FY27 32,383; Q4'26-Q3'27 31,314; months 13-24 35,137; window revenue 50,019 and EBITDA 8,210 (`segment_quarterly.json`).
- The RPO sentence for 6/30/24 and for every date from 12/31/24 to 6/30/26, read in `gev.db`.
- The seven back-test ratios, mean 1.040, standard deviation 0.060, correlations -0.93 and -0.60, leave-one-out errors 6.7% and 3.0%.
- The price bridge, break-even multiples, every grid cell and the return split.
- The FY27 fiscal-year arithmetic in section 9.3.

Not recomputed here (taken from the checkers' files): the peer regression, the plain-rule figure of $28.0B, the EDF adjustment, the bottom-up H1 2027 count, the day-move table, and everything on the six killed candidates.

Hand-check, in this order:

| # | Check | Where | Expected |
|---|---|---|---|
| 1 | The RPO sentence | 10-Q Q2 2026 PDF, RPO note (page 15 or 16) | "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97%" |
| 2 | The multiplication | Calculator | 87,821 x 0.36 = 31,616 |
| 3 | The Street rows | `01-eeo-company-specific.xlsx`, "Multiple Periods", rows 24, 27, 30, columns F:I | Sum 30,245 |
| 4 | Two back-test windows | 10-K 2024 (43,047; 44%) and FY25 equipment revenue 20,934. 10-Q Q2 2025 (49,712; 42%) and 5,880 + 5,963 + 5,254 + 6,459 = 23,556 less Prolec 1,303 | 1.105 and 1.066 |
| 5 | Prolec equipment lines | 10-Q Q1 and Q2 2026, organic revenue table, "Less: Acquisitions" | 469; 834 |
| 6 | Division equipment RPO | 10-Q Q2 2026 segment tables | 39,261 / 8,197 / 40,589 |
| 7 | Price bridge | Snapshot sheet row 3 | (28.544 x 8,923 + 8,298) / 266.334 = $987.45 |
| 8 | Report date | Company investor events page | 2026-10-28, 7:30 am ET. The corpus calendar table still shows an unconfirmed 10-21 |

Small corrections already found: Wind conversion maximum is 69.3%, not 67.6%. Six-window mean is 1.060, not 1.061. H1 2026 revenue is 20,442 in the 10-Q.

Single-source or assumed:

| Item | Status |
|---|---|
| Street equipment split by division | Bloomberg only. Contributor count hidden on the export. No second vendor. Uncertain by about 2% |
| Electrification services-row correction (331 to 481) | One lens |
| Prolec equipment revenue for Q3-Q4 2026 (850 to 1,000 a quarter) | Assumption |
| EDF-disposal adjustment to the 12/31/23 window | Assumes $350M of removed revenue; not disclosed |
| Drop-through on extra equipment revenue | Not disclosed; bracketed by 10-13% gross margin and 19-20% segment margins |
| Peer regression (24.6x) | Rests on one company |
| Pre-report revenue consensus for past quarters | Free vendors; two agree within 1 point |
| Published FY27 revenue estimate of $54.5B (2026-08-04) | One source |
| Broker prices by turbine class ($790 / $950 / $1,800 per kW) and a broker's 2030 model (30 GW at about $900/kW) | Press summaries of the notes |
| Whether a broker note already uses the schedule | Unknown. Paid research could not be read |
| Currency | Not tested; no FX series in the pull |

Terminal pulls that would firm up the Street side: MODL for Q4 2026, Q1 2027 and Q2 2027 (medians, product-revenue line); EEO broker detail for the three division equipment rows (contributor count and dates). If eight or more brokers sit within about 3% of $30.2B, the floor gap becomes a hard number. If medians sit 3% above means, the candidate is finished.

---

## 9. No candidate qualifies: the strongest honest pitch and what it lacks

### 9.1 The six parts, scored for the best candidate

| Part | Has it? | Evidence |
|---|---|---|
| 1. One number against the Street, 7-22% away | **Lacks** | +4.5% as printed; +2.7% to +3.5% on a corrected Street; +0.8% to +5.3% on total revenue; +1.5% to +6.6% on EBITDA |
| 2. Proof by simple arithmetic | **Half** | The multiplication is checkable in seconds. The step from "scheduled" to "will be reported" is not proven: the schedule has not beaten a plain growth rule in the back-test |
| 3. Why the market missed it | **Weak** | Brokers sit on the guide, and no piece was found that multiplies the 36% out. But the same shortfall existed a year ago and showed up as ordinary revenue beats of about 5%, which the stock did not reward |
| 4. A dated test | **Has** | 2026-10-28, late January 2027, late July 2027; all company-reported. All fall after the memo is handed in |
| 5. An honest return split | **Has, and it shows the problem** | Estimate leg +1.6 to +8.4 points; roll-forward +8.7 to +31 points; the multiple decides the rest |
| 6. Survives attack | **Lacks** | 6 of 13 tests pass. The gap equals its error. The uplift is used outside its sample. The stock has moved on the margin guide, not on revenue |

### 9.2 What a pitch can honestly rest on today (facts only; the choice is the team's)

| Element | Facts available |
|---|---|
| Type of call | Near-consensus on estimates. The playbook's distance test says such a pitch is a call on the roll-forward and the multiple, and must say so |
| Roll-forward | Street numbers at an unchanged 28.54x: +8.7% (late January 2027), +25.5% (late July 2027), +31.0% (1 October 2027) |
| Cushion | Break-even multiple on Street numbers: 26.2x, 22.6x, 21.6x at those dates |
| Multiple evidence | 52-week low 27.3x; no week at or below 26x in a year; 18.5x-24.0x in the 2025 sell-off; peer line 24.6x resting on one company |
| Supporting facts, long side | Equipment schedule above the Street on all eight readings. FY26 free cash flow at or above the guide top in 7 of 8 past cases. Revenue beat consensus in six of seven reports |
| Known offsets | Wind FY27 (-$175M to -$255M at mid-points). Street services 2-6% above their schedule |
| Net estimate view | EBITDA for the next four quarters -3% to +6.6% against the Street, centre near +1% |
| Short side | No supporting number. Both short candidates failed. A short is a pure call that the multiple falls more than 21% by October 2027 |
| Dated checks | Section 5 |

### 9.3 Leads that could become a wedge (none has been through the three checks)

**Lead A. Move the schedule claim to the FY27 equipment line.** Raised by the playbook judge. The arithmetic was reproduced for this report.

| Fiscal year | Backlog date | Y1 | H2 already delivered | Months 13-24 amount | In backlog for that year (45% to 57% of months 13-24 fall in the year) | Equipment revenue | Left to come from orders booked after June |
|---|---|---|---|---|---|---|---|
| FY25 | 6/30/24 | 19,534 | 11,141 (actual) | 9,143 | 12,507 to 13,604 | 20,934 (actual) | 7,330 to 8,427 |
| FY26 | 6/30/25 | 20,879 | 11,843 (actual) | 13,919 | 15,300 to 16,970 | about 24,200 to 24,500 (guide-implied, less Prolec; the judge's figure, not re-derived) | 7,230 to 9,200 |
| **FY27** | 6/30/26 | 31,616 | 15,821 (Street) | 25,468 | **27,255 to 30,311** | **32,383 (Street)** | **2,072 to 5,128** |

- Reading: the Street needs $2.1B to $5.1B of 2027 equipment revenue from orders booked after June 2026. The two earlier years had $7.2B to $9.2B.
- If the earlier amount repeated: FY27 equipment of about $35B to $38B, +8% to +17% against the Street. That is +$2.6B to +$5.5B of revenue (+5% to +10% on total revenue) and about +3.5% to +11.5% on FY27 EBITDA at a 13-20% drop-through.
- Points against, to attack before any use:
  - Two past years only, one of them on guidance.
  - The 45% to 57% split of months 13-24 is assumed.
  - Gas is sold out, so new gas orders cannot ship in 2027. Wind equipment orders fell 20% in dollars in H1 2026.
  - An H2 2026 beat lowers the FY27 figure dollar for dollar.
  - The lens files read the same pattern over eight quarters as "customers now order earlier" and claimed no gap.
  - Division builds in the lens files give FY27 equipment of about $31.2B to $36.4B (Power 12.5-14.0; Electrification 14.9-17.0; Wind 3.8-5.4). That is -4% to +12%, centre about +4%. One lens put the 10-K one-year amount at $31.1B to $34.8B.
  - FY27 equipment revenue is reported in late January 2028, outside 12 months. Inside the horizon only the 10-K one-year amount (late January 2027) and the H1 2027 prints test it.
  - To reach $34.7B the one-year amount must rise $3.1B in two quarters. The last three organic quarterly steps were +$1.3B, +$1.6B and +$2.8B. The Street will also move by then.

**Lead B. The January 2027 margin guide.** The stock has moved on the margin guide, not on revenue.
- GEV guides margin as a whole-number two-point range. On about $52.5B of revenue, 16-18% gives a midpoint EBITDA of about 8,925 (5.8% below the Street's 9,471). 17-19% gives about 9,450 (0.2% below).
- First guides have been floors: FY26 Street EBITDA (6,334) is now 19% above the January 2026 guide midpoint.
- No arithmetic yet says which range management will pick. A lens that could would address the line the stock reacts to.

**Lead C. Equipment margin added to backlog (disclosed once a year, in January).** 2025: $8B. Management's floor for 2026: "at least as much". Arithmetic range for 2026: $12B to $22B. There is no Bloomberg line for it, so there is no X. It bears on 2029-2030 estimates, not on the next 12 months.

**Lead D. A longer back-test from peers.** Other equipment makers file the same one-year sentence. Twenty to forty firm-years could shrink the 7% error band below the gap, or confirm that the schedule carries no information at high growth.

**Lead E. Fix one pairing before 2026-10-28.** One Street reading, one share, one uplift, one pass mark. The deep file has 30 pairings. Choosing after the fact is what the statistician's "search noise" point is about.

### 9.4 What would turn the best candidate into a thesis

| Missing part | What would supply it | Date |
|---|---|---|
| Distance of 7% or more with no uplift assumed | 10-K one-year amount of about $34.7B or more against Street FY27 equipment of $32,383M | Late January 2027 |
| Error band smaller than the gap | The FY26 window closes at 1.00 or more (organic equipment of 23,771 or more). It is the first finished window that asked for double-digit growth | Late January 2027 |
| A solid Street figure | Broker count and medians for the three equipment rows | Next terminal session |
| Level, not timing | A gap in months 13-24 as well, or Lead A surviving the three checks | Open |
| Profit link | A disclosed drop-through of 20% or more on converting backlog, or the division split of the one-year share | January 2027 call |
| The multiple | Its own evidence and a dated trigger. No candidate supplies this, and it carries most of any target return | Open |

---

Files: `candidate_equipment-revenue-vs-rpo-schedule.md` (deep file), `verify_*.md` (checkers' working), `propose_*.md` (ten lenses), all in this folder; `../09_finrobot_overnight/BLOOMBERG_VERDICT.md` (earlier verdict, same conclusion). One web-search connector (Firecrawl) is not authorised in this session and was not used; other search tools were.
