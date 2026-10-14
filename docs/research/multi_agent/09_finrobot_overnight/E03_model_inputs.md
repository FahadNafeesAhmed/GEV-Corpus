# Model inputs pack — every number the team will type, with two sources

_E03_model_inputs — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:25:51. Requests 46, input tokens 4157798, output tokens 42498._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV model inputs: sourced tables for the Excel build (as of 2026-09-30)

Research only. No forecasts. Every number below is a published figure, or arithmetic on published figures with the formula shown. The team chooses its own forecast numbers.

**Source keys used throughout** (all GEV accessions start 0001996810-):
- **Earnings releases (8-K EX-99):** R1Q25 = -25-000072 · R2Q25 = -25-000132 · R3Q25 = -25-000159 · R4Q25 = -26-000012 · R1Q26 = -26-000063 · R2Q26 = -26-000147
- **Annual reports:** 10-K24 = -25-000011 · 10-K25 = -26-000015
- **Quarterly reports:** 10-Q1'25 = -25-000073 · 10-Q2'25 = -25-000133 · 10-Q3'25 = -25-000160 · 10-Q1'26 = -26-000064 · 10-Q2'26 = -26-000148
- **SA-Q** = stockanalysis.com quarterly financials. Read via Exa on 2026-09-30; the page snapshot shows its price as of 2026-08-31.
- **MS** = MarketScreener finances page. The Exa cache I read was dated 2026-09-04; facts.csv CT-01/02/04/06 holds the 2026-09-29 fetch.
- **SA-F** = stockanalysis forecast page (S&P Global data), last updated 2026-09-22.
- **FS** = FactSet survey published via cnyes 2026-07-23 (facts.csv CT-10/11; I did not re-read it).
- **Rtr** = Reuters, 2026-07-22.

---

## 1. Bottom line

- **All historical P&L, segment, cash-flow and RPO rows tie across two GEV documents** (release plus 10-Q/10-K). Company revenue, segment revenue, OCF, capex and FCF also tie to an outside vendor (SA-Q) within about $1M.
  - Segment EBITDA and segment equipment/services splits are company-only: two documents, one publisher. No free vendor carries them.
- **Trap 1 — two segment bases.** 2025 quarterly segment data exists on two bases:
  - *Original:* the 2025 releases.
  - *Recast for the 2026 realignment:* part of Electrification Software moved into Gas Power services.
  - SA-Q mixes them: Q1–Q2'25 recast, Q3–Q4'25 original.
  - The team must pick one basis per column. The recast Q3'25 and Q4'25 figures exist only in the realignment supplement xlsx (research files, PP-13/VF-09). The Q4'25 recast figure is computed. [R2Q25; 10-Q2'26 MD&A p.29; SA-Q]
- **Trap 2 — Power equipment/services has two versions.**
  - MD&A (10-Q p.29) for Q2'26: equipment $1,965M / services $3,512M, which sums to segment revenue.
  - Segment note (p.23): equipment $1,957M / services $3,509M / intersegment $12M.
  - Use the MD&A split for the build; it is the one the research series (PMX) uses.
- **Adjusted EBITDA = total segment EBITDA + "Corporate and other".** Corporate and other ran −$116M (FY23), −$323M (FY24), −$541M (FY25), −$239M (H1'26).
  - MarketScreener's EBITDA history equals GEV adjusted EBITDA exactly (FY24 $2,035M, FY25 $3,196M; quarters $457/770/811/1,158/896/1,250M). So consensus EBITDA is on GEV's adjusted basis. [10-K25 segment note p.72; 10-Q2'26 p.24; MS]
- **Consensus is effectively single-vendor for FY26 EBITDA and FY27–28 FCF** (MarketScreener only). Revenue and EPS have second vendors: S&P via SA-F, and FactSet.
  - MarketScreener moved slightly between 2026-09-04 and 2026-09-29. FY27 EBITDA went from $9,570M to $9,574M.
- **Four source conflicts need a decision in the model** (details in §7):
  - Buyback dollars H1'26: $3,645M (Part II Item 2) vs $3,671M (cash-flow statement).
  - Q4'25 diluted EPS: $13.39 (release) vs $13.36 (SA-Q).
  - Power services RPO at YE25: $69,680M (10-K) vs $69,841M (recast, in 10-Q).
  - Q2'25 gas GW total: 29 + 25 = 54 vs the 55 in the release headline.

---

## 2. Answers — the input tables

### Q1. Company P&L, annual and half-year ($M)

| Line | FY23 | FY24 | FY25 | H1'25 | H1'26 | S1 | S2 |
|---|---|---|---|---|---|---|---|
| Total revenue | 33,239 | 34,935 | 38,068 | 17,143 | 20,442 | 10-K25 segment summary p.26 | SA-Q (sum of quarters: FY23 33,239; FY24 34,934–35; FY25 38,068) |
| Equipment revenue | n/f | 18,952 | 20,934 | 9,091 | 11,713 | R4Q25 p.5; R2Q26 p.7 | 10-Q2'26 income statement |
| Services revenue | n/f | 15,983 | 17,134 | 8,052 | 8,729 | same | same |
| Adj. EBITDA | 807 | 2,035 | 3,196 | 1,227 | 2,146 | 10-K25 p.26; R2Q26 p.2 | MS EBITDA row (2,035 / 3,196) |
| Adj. EBITDA margin | 2.43% [computed] | 5.8% | 8.4% | 7.2% | 10.5% | releases | MS (5.83% / 8.4%) |
| D&A (as in adj. EBITDA reconciliation) | 847 | 1,008 | 847 | 406 | 760 | 10-K25 recon p.72 | R4Q25 p.11; R2Q26 p.8 |
| Interest & other financial (income)/charges, net (recon basis) | +53 | (130) | (185) | (97) | (100) | 10-K25 p.72 | R4Q25 p.11; MS interest row |
| Pretax income (GAAP) | n/f | 2,498 | 2,828 | 977 | 6,028 | R4Q25 p.5; 10-Q2'26 p.6 | MS EBT (2,498 / 2,828) |
| Tax provision (GAAP) | n/f | 939 | (2,051) | 221 | 630 | same | 10-K25 recon (2,062 ex-FS) |
| Net income incl. NCI | (474) | 1,559 | 4,879 | 756 | 5,398 | 10-K25 p.72; R2Q26 | SA-Q / MS (attributable 1,552 / 4,884) |
| Diluted EPS | n/m | 5.58 | 17.69 | 2.77 | 19.96 | R4Q25; R2Q26 | MS EPS row (5.58 / 17.69) |
| Diluted weighted-average shares (M) | 274 (spin count) | 278 | 276 | 278 | 271 | R4Q25 p.5 note (a); 10-Q2'26 p.6 | 10-Q2'26 Note 18 (RV-02) |

n/f = not fetched this session; FY23 lines are in the 10-K24 income statement. The FY23 adj. EBITDA of $807M = segment $923M − corporate $116M (10-K25 p.72, p.26).

### Q2. Company P&L by quarter ($M)

2025 figures are on the original basis; company totals are unaffected by the realignment.

| Line | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | S1 | S2 |
|---|---|---|---|---|---|---|---|---|
| Revenue | 8,032 | 9,111 | 9,969 | 10,956 | 9,339 | 11,104 | R1Q25 / R2Q25 / R3Q25 / R4Q25 / R1Q26 / R2Q26 p.2 | SA-Q; MS (identical) |
| Equipment revenue | 4,197c | 4,894 | 5,880c | 5,963 | 5,254c | 6,459 | R2Q26 p.7; R4Q25 p.5 | 10-Q2'26 income statement |
| Services revenue | 3,835c | 4,217 | 4,089c | 4,993 | 4,084c | 4,645 | same | same |
| Adj. EBITDA | 457 | 770 | 811 | 1,158 | 896 | 1,250 | releases p.2 | MS quarterly (identical) |
| Adj. EBITDA margin | 5.7% | 8.5% | 8.1% | 10.6% | 9.6% | 11.3% | releases | computed |
| D&A (recon) | 204c | 202 | 211c | 230 | 342c | 418 | R2Q26 p.8; R4Q25 p.11 | 10-Q2'26 segment note p.24 |
| Interest (income)/charges, net (recon) | (56)c | (41) | (44)c | (44) | (27)c | (73) | same | MS interest row: 56 / 41 / 44 / 44 / 28 / 73 |
| Pretax income | 332c | 645 | 746c | 1,105 | 5,103c | 925 | 10-Q2'26 p.6; R4Q25 p.5 | MS EBT (identical) |
| Tax provision (GAAP) | 68 | 153c | 293c | (2,565) | 354 | 276 | 10-Q1'26 CF (68 / 354); 10-Q3'25 CF (9M 514) | R4Q25 p.5 |
| Effective tax rate | 20.5%c | 23.7%c | 39.3%c | n/m (valuation allowance) | 6.9% | 29.8% | computed | 10-Q Note 16 (6.9%, 29.8%; VF-15) |
| Net income attributable to GEV | 254 | 514 | 452 | 3,664 | 4,745 | 668 | SA-Q | MS |
| Diluted EPS | 0.91 | 1.86 | 1.64 | 13.39 | 17.44 | 2.47 | releases | SA-Q (Q4'25 shows **13.36**, a conflict) |
| Diluted shares (M) | ~279c | 276 | ~276c | 274 | ~272c | 270 | 10-Q2'26 p.6; R4Q25 p.5 | computed: net income ÷ EPS |

c = computed as a difference of published totals (for example Q1'26 = H1'26 − Q2'26). Q4'25 includes a $2.9B tax benefit from a US valuation allowance release [R4Q25 p.1].

### Q3. Segments, annual and half-year ($M) — 2025-and-earlier basis unless marked "r"

| Segment | Line | FY23 | FY24 | FY25 | FY25r | H1'25 | H1'25r | H1'26 | S1 | S2 |
|---|---|---|---|---|---|---|---|---|---|---|
| Power | Revenue | 17,436 | 18,127 | 19,767 | 19,873.0 | 9,180 | 9,234 | 10,449 | 10-K25 MD&A p.26 | R4Q25 p.3; R2Q26 p.3 |
| Power | Equipment | 5,598 | 5,708 | 6,686 | n/d | 2,996 | 2,996 | 3,851 | 10-K25 p.26; 10-Q2'25 p.28; 10-Q2'26 p.29 | facts.csv PMX-01/02/05 |
| Power | Services | 11,838 | 12,419 | 13,081 | n/d | 6,185 | 6,238 | 6,598 | same | same |
| Power | Segment EBITDA | 1,722 | 2,268 | 2,902 | 2,935.7 | 1,286 | 1,303 | 1,842 | 10-K25 p.26 | releases |
| Power | Margin | 9.9% | 12.5% | 14.7% | 14.77% | 14.0% | 14.1% | 17.6% | same | computed |
| Electrification | Revenue | 6,378 | 7,550 | 9,642 | n/f | 4,080 | 4,001 | 6,597 | 10-K25 p.26 | R4Q25 p.4; R2Q26 p.3 |
| Electrification | Segment EBITDA | 234 | 679 | 1,433 | n/f | 535 | 519 | 1,200 | same | same |
| Electrification | Margin | 3.7%c | 9.0% | 14.9% | — | 13.1% | 13.0% | 18.2% | | |
| Wind | Revenue | 9,826 | 9,701 | 9,110 | 9,110 | 4,095 | 4,095 | 3,459 | 10-K25 p.26 | R4Q25; R2Q26 |
| Wind | Segment EBITDA | (1,033) | (588) | (598) | (598) | (312) | (312) | (657) | same | same |
| — | Eliminations & other (revenue) | (401) | (442) | (451) | — | (212)c | (187) | (62) | 10-K25 p.26; 10-Q2'26 p.28 | |
| — | Total segment EBITDA | 923 | 2,358 | 3,737 | — | 1,510 | 1,510 | 2,384 | 10-K25 recon p.72 | 10-Q2'26 p.24 |
| — | Corporate & other | (116) | (323) | (541) | — | (283) | (283) | (239) | same | same |
| — | **Adj. EBITDA** | **807** | **2,035** | **3,196** | — | **1,227** | **1,227** | **2,146** | 10-K25 p.26 | releases |

- FY25r Power comes from the realignment supplement xlsx, tab "Power" (facts.csv VF-09) **[SINGLE-SOURCE; not in the corpus]**. FY25r Electrification was not found.
- Other Power MD&A splits: Electrification H1'26 equipment/services $5,631M / $966M; Wind H1'26 $2,284M / $1,175M [10-Q2'26 pp.30–31].
- Power sub-segments FY25 (original basis): Gas $16,006M / Nuclear $1,018M / Hydro $806M / Steam $1,937M.
- Power sub-segments H1'26 (Steam folded in): Gas $8,493M / Nuclear $1,575M / Hydro $382M [10-K25 p.26; 10-Q2'26 p.23].

### Q4. Segments by quarter ($M)

**Original basis (2025 releases)**

| Segment | Line | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY25 check |
|---|---|---|---|---|---|---|
| Power | Revenue | 4,423 | 4,758 | 4,838 | 5,749 | 19,768 ✓ |
| Power | Equipment | 1,492c | 1,504 | 1,744 | 1,946c | 6,686 |
| Power | Services | 2,932c | 3,253 | 3,094 | 3,802c | 13,081 |
| Power | EBITDA | 508 | 778 | 645 | 971 | 2,902 ✓ |
| Power | Margin | 11.5% | 16.4% | 13.3% | 16.9% | |
| Electrification | Revenue | 1,879 | 2,201 | 2,601 | 2,960 | 9,641 ✓ |
| Electrification | EBITDA | 213c | 322 | 393 | 505 | 1,433 ✓ |
| Wind | Revenue | 1,850 | 2,245 | 2,647 | 2,368 | 9,110 ✓ |
| Wind | EBITDA | (146) | (165) | (61) | (225) | (597) vs (598) rounding |
| — | Corporate & other | (118)c | (165)c | (166)c | (93)c | (542) vs (541) |

Sources for the original-basis table:
- S1: R1Q25 pp.3–4; R2Q25 p.6; R3Q25 pp.3, 6; R4Q25 pp.3–4, 9.
- S2: 10-Q2'25 p.28 and 10-Q3'25 p.29 (Power equipment/services); 10-K25 FY totals.

**Recast basis (2026 structure)**

| Segment | Line | Q1'25r | Q2'25r | Q3'25r | Q4'25r | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|
| Power | Revenue | 4,449 | 4,785 | 4,862.9 | 5,775.1c | 4,971 | 5,477 |
| Power | Equipment | 1,492c | 1,504 | n/d | n/d | 1,886c | 1,965 |
| Power | Services | 2,958c | 3,280 | n/d | n/d | 3,086c | 3,512 |
| Power | EBITDA | 517 | 785 | 651.3 | 981.4c | 811 | 1,031 |
| Power | Margin | 11.6% | 16.4% | 13.39% | 16.99%c | 16.3% | 18.8% |
| Electrification | Revenue | 1,840 | 2,162 | 2,564.8 | n/f | 2,959 | 3,637 |
| Electrification | EBITDA | 205 | 314 | 387.3 | n/f | 528 | 671 |
| Wind | Revenue / EBITDA | 1,850 / (146) | 2,245 / (165) | unchanged | unchanged | 1,432 / (382) | 2,026 / (275) |
| — | Corporate & other | (119)c | (164) | — | — | (62)c | (177) |

Sources for the recast table:
- S1: R1Q26 pp.3–4; R2Q26 p.3; 10-Q2'26 pp.23–24, 29.
- S2: SA-Q for segment revenue (Power 4,449 / 4,785 / 4,971 / 5,477; Electrification 1,840 / 2,162 / 2,959 / 3,637).
- Q3'25r comes from the supplement xlsx via facts PP-13/PP-15 **[SINGLE-SOURCE]**.
- Q4'25r = FY25r − H1'25r − Q3'25r (computed).

Wind is unchanged by the realignment: Q1'25 −146 in both R1Q25 and R1Q26; H1'25 −312 in both.

### Q5. Reconciliation from net income to adjusted EBITDA ($M)

| Item | FY23 | FY24 | FY25 | Q4'25 | H1'25 | Q2'26 | H1'26 |
|---|---|---|---|---|---|---|---|
| Net income (GAAP, incl. NCI) | (474) | 1,559 | 4,879 | 3,670 | 756 | 649 | 5,398 |
| + Restructuring & other | 433 | 426 | 277 | 85 | 108 | 9 | 102 |
| + (Gains)/losses on business interests | (92) | (1,024) | (281) | (150) | (19) | 48 | (4,445) |
| + Separation costs (benefits) | — | (9) | 180 | 58 | 80 | 38 | 61 |
| + Arbitration refund | — | (254) | — | — | — | — | — |
| + Russia/Ukraine charges | 95 | — | — | — | — | — | — |
| + Non-operating benefit income | (567) | (536) | (459) | (119) | (225) | (119) | (253) |
| + D&A | 847 | 1,008 | 847 | 230 | 406 | 418 | 760 |
| + Interest & other financial, net | 53 | (130) | (185) | (44) | (97) | (73) | (100) |
| + Tax provision (ex Financial Services) | 512 | 995 | (2,062) | (2,572) | 218 | 279 | 623 |
| **Adj. EBITDA** | **807** | **2,035** | **3,196** | **1,158** | **1,227** | **1,250** | **2,146** |

- S1: 10-K25 segment recon p.72 (FY23–25, in segment-to-net-income form; signs flipped here).
- S2: R4Q25 p.11 (FY24, FY25, Q4); R2Q26 p.8 and 10-Q2'26 p.24 (2026).
- The H1'26 gains line includes the Prolec remeasurement gain (+$3,992M), the Proficy sale gain ($330M) and Prolec inventory fair-value expense ($106M) [R2Q26 p.8 note (a)].
- Separation costs include a one-time stock option grant [same, note (b)].

### Q6. Balance sheet and EV bridge inputs ($M)

| Item | 12/31/24 | 12/31/25 | 3/31/26 | 6/30/26 | S1 | S2 |
|---|---|---|---|---|---|---|
| Cash, equivalents & restricted cash | 8,205 | 8,848 | 10,172 | 13,120 | R4Q25 p.6; 10-Q1'26 CF; 10-Q2'26 CF p.8 | SA-Q "cash & investments": 7,767 / 8,935 / 9,772 / 12,720 (vendor excludes ~$0.4B restricted cash; definitions differ) |
| Total borrowings | n/f | LT 265 | n/f | 2,849 (LT 2,794 + current 55) | 10-Q2'26 Note 14 | SA-Q total debt 3,720 (includes ~$871M operating leases; D08) |
| Feb-2026 senior notes | — | — | 2,600 | 2,600 | 10-Q2'26 Note 14: $600M 4.25% 2031; $1,000M 4.875% 2036; $1,000M 5.5% 2056 | 10-Q1'26 CF "newly issued debt 2,567" (net) |
| Noncontrolling interests | 1,047 | 1,118 | 1,143 | 1,158 | R4Q25 p.6; 10-Q2'26 equity statement | 10-Q2'26 balance sheet (RV-07) **[vendor: none — yfinance null]** |
| Equity method investments | 2,149 | 1,834 | — | 1,384 | R4Q25 p.6; 10-Q2'26 Note 11 | 10-K25 Note 11 |
| Postretirement funded status (pre-tax) | — | net (1,300); deficit-only plans (2,470) | — | not updated quarterly | 10-K25 Note 13 (RV-08) | 10-K25 balance sheet: pension surplus asset $1,163M in "All other assets" (R4Q25 p.6 shows non-current comp & benefits $3,171M) |
| Voluntary pension contribution | — | — | — | ~$500M (Q2'26) | R2Q26 p.2 | CQ-15 ($516M H1) |
| Shares outstanding | 275,880,314 | 269,529,464 | ~269M | 266,333,581 | R4Q25 p.6; 10-Q2'26 cover | MS share count 266,334K; yfinance (D08) |
| Total equity | 10,593 | 12,296 | 15,065 (4/1) | 13,115 | R4Q25 p.6; 10-Q2'26 equity statement | — |

### Q7. Cash flow, FCF, capital returns ($M)

| Line | FY23 | FY24 | FY25 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | H1'26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Cash from operations | 1,186 | 2,583 | 4,987 | 1,161 | 367 | 980c | 2,480 | 5,188 | 5,492 | 10,680 |
| Capex (gross additions to PP&E and internal-use software) | (744) | (883) | (1,277) | (186) | (172) | (248)c | (671)c | (397) | (386) | (783) |
| **FCF** | **442c** | **1,701** | **3,710** | **975** | **194** | **732** | **1,809** | **4,791** | **5,107** | **9,897** |
| of which: Δ contract liabilities (deposits line in OCF) | 2,812 | 2,799 | 8,019 | 1,124 | 736c | 559c | 5,600c | 5,574 | 8,121c | 13,695 |
| Dividends paid | — | — | (275) | (69) | (70)c | (68)c | (68)c | (137) | (136)c | (273) |
| Buybacks (cash-flow basis) | — | (43) | (3,316) | (1,101) | (480)c | (660)c | (1,075)c | (1,278) | (2,393)c | (3,671) |
| Cash taxes paid | n/f | (623) | (830) | (145) | | | | (534) | | (1,258) |
| Share-based comp (pre-tax) | n/f | 155 | 257 | | 70 | | | 65c | 70 | 135 |

Sources:
- S1: R4Q25 cash-flow statement pp.7–8; 10-Q1'26, 10-Q3'25 and 10-Q2'26 cash-flow statements; FCF tables in R2Q26 p.8 and R4Q25.
- S2: SA-Q OCF / capex / FCF. FY23 quarters sum to 1,186 / 744 / 442; FY24 to 2,583 / 883 / 1,700. 2025–26 quarters match within $1M (Q3'25 capex 247, Q4'25 OCF 2,479).
- FY23 FCF = 1,186 − 744 (computed; the FY23 row is pre-spin).
- SBC from 10-K25 and 10-Q2'26 equity statements (RV-35).

- **Buyback share counts:** H1'26 4,266,417 shares at an average $854.43 (Q2 2,467K at $952.47). Cumulative program $6,963M; $3,037M authorization left at 6/30 [10-Q2'26 Part II Item 2; VF-13] [R2Q26 p.2: "4.3 million shares… average price of $854"].
- **Dividend per share:** $0.25 per quarter through 2025; $0.50 per quarter in 2026.
  - S1: R2Q26 p.2 ("$0.50 per share quarterly dividend").
  - S2: MS DPS FY25 $1.00. SA-F shows $1.25 for FY25, most likely a declared-basis count; could not confirm.
  - 2025 cash paid of ~$68–70M per quarter ÷ ~272M shares ≈ $0.25 (computed).

### Q8. FY26 guidance — latest version (2026-07-22) and history

| Line | Dec-9-25 (first; excluded Prolec) | Jan-28-26 | Apr-22-26 | **Jul-22-26 (current)** | S1 | S2 |
|---|---|---|---|---|---|---|
| Revenue | $41–42B | $44–45B | $44.5–45.5B | **$45.5–46.5B** | R2Q26 p.2 | Rtr ("to $45.5 billion–$46.5 billion from $44.5–45.5") |
| Adj. EBITDA margin | 11–13% | 11–13% | 12–14% | **12–14% (held)** | R2Q26; R1Q26 | Rtr ("unchanged at 12%–14%") |
| FCF | $4.5–5.0B | $5.0–5.5B | $6.5–7.5B | **$11.5–12.5B** | R2Q26 | stocktitan 8-K summary 2026-07-22 |
| Power | — | 16–18% organic growth; 16–18% margin | 16–18%; **17–19%** | **18–20% organic growth; 17–19% margin** | R2Q26; R1Q26; R4Q25 | 10-Q2'26 does not repeat guidance; Q2 transcript (PP-12) |
| Electrification | ~20% organic; 17–19% | $13.5–14.0B incl. ~$3B Prolec; 17–19% | $14.0–14.5B; **18–20%** | **$14.5–15.0B incl. ~$3.1B Prolec; 18–20%** | same | same |
| Wind | similar losses to 2025 | organic down low-double digits; ~−$400M | same | **same (~−$400M EBITDA)** | same | same |
| Q3'26 segment guides (call) | | | | Power +17–19% revenue, ~17–18% margin; Electrification $3.8–4.0B, margin modestly above 18.4%; Wind revenue down LDD, EBITDA ~break-even | Q2'26 transcript (PP-12/PP-15) | **[SINGLE-SOURCE: transcript only]** |

Dec-25 figures come from facts BR-12 (Dec-2025 release PDF).

### Q9. 2028 framework (issued 2026-01-28; not restated in the Q1/Q2'26 releases)

| Line | Value | S1 | S2 |
|---|---|---|---|
| Revenue | $56B (up from $52B; the step is Prolec) | R4Q25 p.3 | Motley Fool Q4'25 transcript 2026-01-28 (it says "at least $56 billion"; the release says "$56 billion") |
| Organic growth | low-teens | R4Q25 p.3 | Fool |
| Adj. EBITDA margin | 20% (= $11,200M computed) | R4Q25 | Fool |
| Cumulative FCF 2025–28 | ≥$24B (up from ≥$22B) | R4Q25 | Fool |
| Power | high-teens organic revenue CAGR; 22% margin | R4Q25 | Dec-2025 investor PDF (BR-28) |
| Electrification | high-teens organic CAGR + ~$4B Prolec revenue; 22% margin | R4Q25 | same |
| Wind | down low-double-digit organic CAGR; 6% margin (cut from 10% in Dec-25) | R4Q25 | Dec-2025 PDF (BR-11) |
| Capex / R&D commitments | $6B capex 2025–28 (incl. $1B Prolec 2026–28); $5B R&D 2025–28 | R2Q26 p.2 | last10k copy of R4Q25 (same text; weak) |

### Q10. Consensus FY26–FY28

| Metric | FY26 | FY27 | FY28 | Source / date | Second source | Flag |
|---|---|---|---|---|---|---|
| Revenue | 46,282 | 52,740 | 60,500 | MS 2026-09-29 (CT-01) | SA-F (S&P) 46.28B / 52.74B (2026-09-22); FS FY27 52,632 / FY28 60,511 (2026-07-23) | close |
| — | 46,259 | 52,731 | 60,466 | MS cache 2026-09-04 | — | drift +0.05% |
| Adj. EBITDA | 6,359 | 9,574 | 13,064 | MS 2026-09-29 (CT-02) | FY27: GLJ "Street $9.45B" (−1.3%); FY28: Motley Fool CAGR back-solve within 0.2% (D08) | **FY26 single-source** |
| — | 6,353 | 9,570 | 13,059 | MS 2026-09-04 | | |
| Adj. EBITDA margin | 13.74% | 18.15% | 21.6% | MS | computed | |
| EPS (GAAP-type; FY26 includes the Prolec gain) | 30.78 | 24.85 | 34.22 | MS 09-29 (CT-04) | FS mean FY27 24.78 / FY28 34.71; MS 09-04: 30.74 / 24.80 / 34.14 | basis trap |
| EPS (non-GAAP, S&P) | 15.16 | 25.13 | n/a | SA-F 2026-09-22 | — | FY26 ≠ MS basis |
| FCF | 12,017 | 7,417 | 9,248 | MS 09-29 (CT-06) | SA-F FY26 $12.02B only; MS 09-04: 12,011 / 7,402 / 9,240 | **FY27–28 single-source** |
| Capex | 1,479 / 1,447 | 1,457 / 1,390 | 1,558 / 1,495 | MS 09-29 / 09-04 | — | single-source |
| Q3'26 revenue / EBITDA | 12,013 / 1,706 | | | MS 09-29 (VF-10) | MS 09-04 12,004 / 1,702; Zacks revenue $12.07B, EPS $4.08 (D08) | |
| Q4'26 revenue / EBITDA | 13,905 / 2,535 | | | MS 09-29 | MS 09-04 13,876 / 2,523 | |
| FY27 quarterly EBITDA | Q1 1,928 · Q2 2,354 · Q3 2,413 · Q4 3,191 (sum 9,886 ≠ annual 9,570) | | | MS 09-04 | — | **internal inconsistency; single-source** |
| Target price | $1,237 (37 analysts; median $1,250; low $940; high $1,450) | | | SA-F | MS (CT-33) | |

### Q11. Gas turbines: GW shipped, orders, backlog, SRAs

| Quarter | Orders GW (10-Q units table) | Shipped GW | New contracts signed (SRA + orders) | SRAs converted | Firm backlog GW (end) | SRAs GW (end) | Total GW | S1 | S2 |
|---|---|---|---|---|---|---|---|---|---|
| FY23 | 9.5 | 13.8 | | | | | | 10-K25 p.26 | facts PMX-08 |
| FY24 | 20.2 | 11.9 | | | | | | 10-K25 | PMX-08 |
| Q1'25 | 7.1c | 3.0c | | | 29 | 21 | 50 | 10-Q2'25 p.28 (H1 12.2 / 8.2) | R2Q25 ("from 50 to 55"; SRA "from 21") |
| Q2'25 | 5.1 | 5.2 | 9 (7 + 2) | 3 | 29 | 25 | 55 headline (54 by sum) | 10-Q2'25 p.28 | R2Q25; R3Q25 ("from 25") |
| Q3'25 | 7.4 | 4.0 | 13 (12 + 1) | 7 | 33 | 29 | 62 | 10-Q3'25 p.29 | R3Q25 |
| Q4'25 | 10.2c | 3.1c | 24 (21 + 3) | 8 | 40 | 43 | 83 | 10-K25 (FY 29.8 / 15.3) | R4Q25 |
| FY25 | 29.8 | 15.3 | | | | | | 10-K25 p.26 | PMX-08 |
| Q1'26 | 8.0c | 4.2c | 21 (19 + 2) | 6 | 44 | 56 | 100 | 10-Q2'26 p.29 (H1 20.1 / 7.5) | R1Q26 |
| Q2'26 | 12.1 | 3.3 | 20 (18 + 2) | 10 | 53 | 63 | 116 | 10-Q2'26 p.29 | R2Q26 p.1 |

- **Tie-out:** the 10-Q "orders GW" ≈ new firm orders + SRA conversions in the release. Q2'26: 2 + 10 = 12 vs 12.1. Q1'26: 2 + 6 = 8. Q2'25: 2 + 3 = 5.
- **Unit mix Q2'26 shipped:** 29 turbines, 13 heavy-duty (3 HA), 16 aero. H1'26: 54 units (8 HA).
- **Output path:** 20 GW/yr run-rate from Q3'26 (5 GW/qtr); 24 GW in 2028; actions toward 30 GW in 2030; ≥125 GW under contract by YE26 [R2Q26 p.1] [Laguna transcript p.4, PP-22].
- **Wind GW** (orders / sales): FY23 9.1 / 8.8; FY24 5.3 / 7.8; FY25 4.9 / 6.9; H1'26 1.2 / 2.0 [10-K25 p.26; 10-Q2'26 p.30].

### Q12. RPO and conversion

**Company RPO ($M) and share expected to be recognised**

| Date | Equipment RPO | % within 1 / 2 / 5 yrs | Services RPO | % within 1 / 5 / 10 / 15 yrs | Total | S1 | S2 |
|---|---|---|---|---|---|---|---|
| 12/31/23 | 40,478 | 51 / 77 / 100 | n/f | | n/f | POS-20 (S-1/A) | — |
| 12/31/24 | 43,047 | 44 / 69 / 93 | 75,976 | 18 / 53 / 78 / 91 | 119,023 | 10-K24 Note 9 | 424B3 -25-000012 (same text) |
| 3/31/25 | 45,478 | 45 / 71 / 91 | 77,959 | 18 / 53 / 78 / 91 | 123,438 | 10-Q1'25 Note 8 | 424B3 -25-000074 |
| 6/30/25 | 49,712 | 42 / 70 / 92 | 78,938 | 17 / 53 / 78 / 91 | 128,650 | 10-Q2'25 p.14 | — |
| 9/30/25 | 54,092 | 41 / 71 / 97 | 81,177 | 17 / 53 / 78 / 91 | 135,269 | 10-Q3'25 Note 9 | — |
| 12/31/25 | 64,245 | 37 / 69 / 97 | 85,993 | 17 / 52 / 77 / 91 | 150,238 | 10-K25 Note 9 p.53 | GLJ-21; Q4'25 call "$64 billion" |
| 3/31/26 | 75,924 | 38 / 69 / 98 | 87,352 | 16 / 53 / 78 / 91 | 163,276 | 10-Q1'26 p.14 | R1Q26 "$163 billion" |
| 6/30/26 | 87,821 | 36 / 65 / 97 | 88,463 | 16 / 54 / 79 / 92 | 176,284 | 10-Q2'26 p.15 | R2Q26 "$176 billion"; biggo transcript summary "$88 billion" equipment |

**Segment RPO ($M), equipment / services**

| Segment | 12/31/23 | 12/31/24 | 6/30/25 | 9/30/25 | 12/31/25 | 6/30/26 |
|---|---|---|---|---|---|---|
| Power | 13,636 / 59,338 | 12,461 / 60,890 | 16,133 / 62,932 (r: 63,088) | 18,977 / 65,083 | 24,707 / 69,680 (r: 69,841) | 39,261 / 72,388 |
| Electrification | n/f | n/f | 23,950 / 3,168 (r) | n/f | 30,508 / 3,734 | 40,589 / 3,974 |
| Wind | 13,709 / 13,240 | 10,720 / 11,962 | 9,731 / 12,777 | n/f | 9,112 / 12,518 | 8,197 / 12,191 |

- Sources: 10-K25 MD&A p.26; 10-Q2'25 p.28; 10-Q3'25 p.29; 10-Q2'26 pp.29–31. S2 for Power equipment: facts GLJ-14.
- Segment sums exceed the company total by $226M (equipment) and $90M (services) at 6/30/26; the gap is eliminations/other (computed).

---

## 3. Evidence table (headline inputs)

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY25 revenue | 38,068 | 10-K25 p.26 | SA-Q sum; MS | exact | H |
| 2 | FY25 adj. EBITDA | 3,196 | R4Q25 p.3 | MS EBITDA row | exact | H |
| 3 | FY25 corporate & other | (541) | 10-K25 p.26 | 10-K25 p.72 recon (same filing, 2 tables) | exact | M (company-only) |
| 4 | H1'26 adj. EBITDA | 2,146 | R2Q26 p.2 | 10-Q2'26 p.28; MS 896 + 1,250 | exact | H |
| 5 | H1'26 corporate & other | (239) | 10-Q2'26 p.24 | 10-Q2'26 p.28 MD&A | exact | M |
| 6 | Q2'26 Power revenue / EBITDA | 5,477 / 1,031 | R2Q26 p.3 | 10-Q2'26 p.29; SA-Q revenue | exact | H |
| 7 | Power equipment / services FY25 | 6,686 / 13,081 | 10-K25 p.26 | facts PMX-01 | exact | M (company-only) |
| 8 | Power split Q2'26 | 1,965 / 3,512 (MD&A) | 10-Q2'26 p.29 | 10-Q2'26 p.23: 1,957 / 3,509 / 12 interseg | **conflict (definition)** | M |
| 9 | Q3'25 Power recast | 4,862.9 / 651.3 | supplement xlsx (PP-13) | none | **SINGLE-SOURCE** | M |
| 10 | FY25 FCF | 3,710 = 4,987 − 1,277 | R4Q25 p.7 | SA-Q quarters; MS | exact | H |
| 11 | H1'26 FCF | 9,897 = 10,680 − 783 | R2Q26 p.8 | SA-Q 4,791 + 5,106 | exact (±1) | H |
| 12 | H1'26 deposits line | 13,695 (Q1 5,574) | 10-Q2'26 CF | 10-Q1'26 CF (Q1) | consistent | M |
| 13 | Cash 6/30/26 | 13,120 | 10-Q2'26 CF p.8 | R2Q26 "$13.1B"; SA-Q 12,720 ex-restricted | close (definition) | H |
| 14 | Borrowings 6/30/26 | 2,849 | 10-Q2'26 Note 14 | SA-Q 3,720 incl. leases | reconciles | H |
| 15 | NCI | 1,158 | 10-Q2'26 equity statement | 10-Q2'26 balance sheet | exact | M |
| 16 | Shares outstanding | 266,333,581 | 10-Q2'26 cover | MS 266,334K | exact | H |
| 17 | Diluted weighted-average Q2'26 | 270M | 10-Q2'26 p.6 | 668 / 2.47 = 270.4 computed | close | H |
| 18 | H1'26 buybacks | 3,671 (CF) | 10-Q2'26 CF | Part II Item 2: $3,645M | **conflict** | M |
| 19 | FY26 guide | 45.5–46.5B / 12–14% / 11.5–12.5B | R2Q26 p.2 | Rtr 2026-07-22 | exact | H |
| 20 | 2028 framework | $56B / 20% / ≥$24B | R4Q25 p.3 | Fool transcript ("at least $56B") | close | H |
| 21 | Consensus FY27 EBITDA | 9,574 | MS 09-29 | GLJ $9.45B; MS 09-04 9,570 | close | M |
| 22 | Consensus FY26 EBITDA | 6,359 | MS | none independent | **SINGLE-SOURCE** | M |
| 23 | Consensus FY27–28 FCF | 7,417 / 9,248 | MS | none (SA-F paywalled) | **SINGLE-SOURCE** | L-M |
| 24 | Consensus FY27 EPS | 24.85 | MS | FS 24.78; SA-F 25.13 non-GAAP | close | H |
| 25 | Equipment RPO 6/30/26 | 87,821; 36 / 65 / 97% | 10-Q2'26 p.15 | R2Q26 / transcript "$88B" | exact / close | H |
| 26 | Gas 53 + 63 = 116 GW | — | R2Q26 p.1 | SE comparison (RQ-16) / Laguna | exact | H |
| 27 | FY25 gas shipped / ordered | 15.3 / 29.8 GW | 10-K25 p.26 | facts PMX-08 | exact | H |
| 28 | FY25 D&A (recon) | 847 | 10-K25 p.72 | R4Q25 p.11 | exact | H |
| 29 | FY25 dividends / buybacks paid | 275 / 3,316 | R4Q25 CF p.8 | 10-K25 CF | exact | H |
| 30 | Q4'25 diluted EPS | 13.39 | R4Q25 p.3 | SA-Q 13.36 | **conflict** | M |

---

## 4. Arithmetic (all computed items)

**Quarterly differences** (Q = period total − other published periods):
- Revenue: Q1'26 = 20,442 − 11,104 = 9,338 (release says 9,339; rounding).
- Adj. EBITDA: Q1'25 = 1,227 − 770 = 457 ✓ R1Q25.
- D&A: Q1'25 = 406 − 202 = 204; Q3'25 = 847 − 406 − 230 = 211; Q1'26 = 760 − 418 = 342.
- Tax: Q2'25 = 221 − 68 = 153; Q3'25 = 514 − 221 = 293; Q4'25 = −2,051 − 514 = −2,565 ✓ R4Q25.
- Pretax: Q1'25 = 977 − 645 = 332; Q3'25 = 2,828 − 1,105 − 977 = 746; Q1'26 = 6,028 − 925 = 5,103 (all ✓ MS).
- ETR: Q1'26 = 354 / 5,103 = 6.9%; Q2'26 = 276 / 925 = 29.8%; FY24 = 939 / 2,498 = 37.6%; FY25 = −2,051 / 2,828 = −72.5% (valuation allowance).

**Company equipment/services splits:**
- Q1'25: equipment 9,091 − 4,894 = 4,197; services 8,052 − 4,217 = 3,835.
- Q3'25: equipment 20,934 − 9,091 − 5,963 = 5,880; services 17,134 − 8,052 − 4,993 = 4,089.
- Q1'26: equipment 11,713 − 6,459 = 5,254; services 8,729 − 4,645 = 4,084.

**Power splits:**
- Q1'25 original: 2,996 − 1,504 = 1,492 equipment; 6,185 − 3,253 = 2,932 services.
- Q4'25 original: 6,686 − 4,740 = 1,946 equipment; 13,081 − 9,279 = 3,802 services.
- Q1'26: 3,851 − 1,965 = 1,886 equipment; 6,598 − 3,512 = 3,086 services.
- Q4'25 recast: revenue 19,873.0 − 9,234 − 4,862.9 = 5,775.1; EBITDA 2,935.7 − 1,303 − 651.3 = 981.4; margin 16.99%.

**Corporate & other = adj. EBITDA − Σ segment EBITDA:**
- Q1'25 original: 457 − (508 − 146 + 213) = −118.
- Q3'25: 811 − (645 − 61 + 393) = −166.
- Q4'25: 1,158 − (971 − 225 + 505) = −93.
- Q1'26: 896 − (811 + 528 − 382) = −61.9 (10-Q H1 − Q2 = −239 + 177 = −62).

**Cash flow:**
- Q3'25 OCF = 2,508 − 1,528 = 980; capex = 606 − 359 = 247–248.
- Q4'25 capex = 2,480 − 1,809 = 671.
- Contract-liability line by quarter: 1,860 − 1,124 = 736; 2,419 − 1,860 = 559; 8,019 − 2,419 = 5,600; 13,695 − 5,574 = 8,121.
- Buybacks: Q2'25 = 1,581 − 1,101 = 480; Q3'25 = 2,241 − 1,581 = 660; Q4'25 = 3,316 − 2,241 = 1,075; Q2'26 = 3,671 − 1,278 = 2,393.

**Other:**
- Diluted shares: Q1'25 = 254 / 0.91 = 279; Q3'25 = 452 / 1.64 = 276; Q1'26 = 4,745 / 17.44 = 272.1.
- 2028 framework EBITDA = 56,000 × 20% = 11,200.
- Annual coupon on the Feb-2026 notes = 600 × 4.25% + 1,000 × 4.875% + 1,000 × 5.5% = $129.25M. This is a research computation, not the reported interest line.
- Gas GW: Q4'25 orders = 29.8 − 19.6 = 10.2; Q4'25 shipped = 15.3 − 12.2 = 3.1; Q1'26 orders = 20.1 − 12.1 = 8.0; Q1'26 shipped = 7.5 − 3.3 = 4.2.
- Recast deltas H1'25: Power +54 revenue / +17 EBITDA; Electrification −79 / −16 (4,080 → 4,001; 535 → 519). The shift is roughly a wash; corporate is unchanged at −283.

---

## 5. General question bank items answered along the way

- **G12 / G24 (deposits).** The deposits line was 57% of H1'26 OCF in Q1 alone (5,574 / 10,680 of the half) and 8,121 in Q2 [10-Q1'26; 10-Q2'26]. Quarterly lumpiness is large: 559 in Q3'25 vs 5,600 in Q4'25. A model that treats FCF as a function of EBITDA will miss this.
- **G20 (definition traps found in this session).**
  - Two segment bases for 2025.
  - MD&A vs segment-note Power split.
  - Vendor cash excludes restricted cash; vendor debt includes leases.
  - FY26 GAAP-type vs ex-items EPS.
  - The MarketScreener FY27 quarterly EBITDA sum (9,886) does not equal its own annual figure (9,570). That makes quarterly consensus less reliable than annual.
- **G2.** Consensus FY27 adj. EBITDA margin is 18.15% [MS]. The best adj. EBITDA margin GEV has printed in any quarter is 11.3% (Q2'26) [R2Q26].

---

## 6. What would change this

- **A Q3'26 10-Q/release (2026-10-28) that recasts Q3'25 differently from the supplement.** Replace rows 9 and the Q4'25r derivation with it.
- **A new MarketScreener fetch** would supersede the 09-29 consensus. Any move above ~1% in FY27 EBITDA matters for valuation.
- **A GEV 8-K with a Q3 buyback figure, or a new guide** (none since 2026-08-27 per D08).
- **The $3,645M vs $3,671M buyback gap.** If Part II excludes excise tax or settlement timing, the cash-flow figure is the right one for FCF uses; the Part II figure is the right one for share-count math.

---

## 7. Disagreements with the master brief

1. **Buybacks.** The brief (VF-13) uses $3,645M for H1'26. The cash-flow statement shows $3,671M, and the Q2 equity statement shows $2,373M for Q2 vs $2,350M implied by Part II (2,467K × $952.47). These are not the same number. The team should state which basis it uses. [10-Q2'26 CF p.8; equity statement p.10; Part II Item 2]
2. **Power FY23–FY25 margins vs H1'26 are on different perimeters.** The brief's series (9.88% → 12.51% → 14.68% → 17.63%) splices bases. The like-for-like FY25 figure is 14.77% recast (VF-09), and H1'25r is 14.1%. The brief notes the realignment elsewhere but not in §3.
3. **Consensus freshness.** The MarketScreener values in the brief (09-29) and the Exa-cached page (09-04) differ by 0.04–0.2%. That is immaterial, but the retrieval date must go on the Inputs tab.
4. **The "$56B" 2028 revenue** is worded "$56 billion" in the release but "at least $56 billion" in the Fool transcript summary. Use the release wording.
5. **Minor data issues.**
   - The Q2'25 gas total in the release headline (55 GW) is one more than backlog + SRAs (29 + 25).
   - Q4'25 EPS: release $13.39 vs SA-Q $13.36.
   - Power services RPO YE25: $69,680M (10-K) vs $69,841M (recast).
   - None of these changes a conclusion.

---

## 8. Open items (where to look next)

- **Recast FY25 / Q4'25 Electrification** (not found): realignment supplement xlsx at gevernova.com, tab "Electrification".
- **Quarterly 2025 Power equipment/services on the recast basis for Q3/Q4'25:** same supplement, if it carries the split; otherwise not disclosed.
- **FY23 income-statement detail** (equipment/services revenue, pretax, tax) and FY23 services RPO: 10-K24 income statement and Note 9.
- **Pension funded status at 6/30/26:** not disclosed quarterly. Use YE25 (−$1,300M net) and adjust for the ~$0.5B Q2 contribution only if the team documents it.
- **Q2'25 Power orders on the original basis, and quarterly Electrification/Wind orders:** R2Q25 pp.3–4 (not fetched).
- **Independent second source for segment EBITDA:** none found free. Reuters carries only Wind (−$275M vs −$165M) and adj. EBITDA $1.25B for Q2'26 (Rtr). The LSEG estimate is behind the paywall.
- **Consensus FY26 EBITDA and FY27–28 FCF:** only MarketScreener. Try Visible Alpha or FactSet through a university terminal, if the team has access, for a second vendor.
- **Dividend declared basis:** the Q2'25 equity statement shows "Dividends declared ($0.50 per common share)" of $138M, while cash paid was ~$0.25 per quarter. Check the 10-Q2'25 equity statement and the Dec-2024 / May-2025 declaration 8-Ks.
