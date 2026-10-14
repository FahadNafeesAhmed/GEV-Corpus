# What exactly does the Street assume for FY27, and how solid is the consensus number?

_S02_street_bridge — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 10:07:45. Requests 55, input tokens 5304535, output tokens 42370._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV FY27 Street consensus: vendor reconciliation, segment and quarterly shape, and how solid the number is (research input, as of 2026-09-30)

*Research input only. Every range here is a research estimate, and the team chooses its own number and writes every memo sentence.*

**Source key**
- **MS-0904**: MarketScreener finances page, Exa cache stamped 2026-09-04 (annual and quarterly tables), read this session.
- **MS-0929**: MarketScreener on 2026-09-29, as verified in evidence_lanes CT-01/02/04/05/06.
- **BOURSO**: Boursorama consensus page. It says "Le présent consensus est fourni par la société FactSet". Estimates are dated 26/09/2026. Read this session.
- **MW**: MarketWatch analyst-estimates page, "Last Updated: Sep 2, 2026" (FactSet). Read this session. Earlier outputs had this as unverifiable; it is now confirmed.
- **YF**: Yahoo /analysis, a cached snapshot at an intraday price of $944.66, second half of September; exact date unverified. Read this session.
- **CM**: ChartMill analyst page, cached with price as of 2026-08-20. Read this session.
- **TIKR**: TIKR blog (S&P Capital IQ data), last updated 2026-09-27. Read this session.
- **CN**: cnyes FactSet surveys (R08, CT-10/11).
- **EQ**: Equibles 09-23 (CT-09).
- **INV-MZ**: Investing.com, Mizuho note, 2026-09-30.
- **SI-MZ**: StreetInsider, Mizuho, 2026-09-30.
- **GF**: GuruFocus GLJ write-up, 2026-09-15.
- **10K**: 0001996810-26-000015. **10Q**: -26-000148. **Q2REL**: -26-000147 EX-99.

---

## 1. Bottom line

- **The FY27 consensus for adjusted EBITDA is a band of $9.34–9.65B across vendors, not a single $9,574M.**
  - FactSet (Boursorama, 09-26): $9,339M. MarketScreener: $9,574M (09-29) and $9,570M (09-04). ChartMill: $9,652M (08-20). GLJ's quoted "Street": $9.45B (09-14).
  - [S1: BOURSO table "Prévisions de résultats… au 26/09/2026"] [S2: MS-0904/MS-0929 "EBITDA" row] [S3: CM yearly table] [S4: GF]
  - Only MarketScreener and FactSet show GEV's adjusted-EBITDA FY25 actual of $3,196M. ChartMill's FY25 "EBITDA" is 2,525, so ChartMill is on a different basis.
- **The vendors' EBIT line is mixed-basis.** So the $8,150M EBIT that MarketScreener and FactSet share tells you nothing about which EBITDA figure is right.
  - The FY25 EBIT actual in both vendors (1,388 / 1,389) is GAAP operating income [10K MD&A "Operating income (loss) $1,388"].
  - The FY27 EBITDA–EBIT gap the vendors imply is only $1,189–1,424M. Filings put FY27 D&A alone at about $1.67B: Q2'26 D&A of $418M × 4, lifted by roughly $715M a year of Prolec intangible amortization [computed; 10Q Note 24 reconciliation and Prolec PPA table; Q2REL p.8].
  - At least some contributors must be submitting EBIT before acquisition amortization.
- **FY27 EPS of $24.69–24.85 is internally consistent with MarketScreener's own line items.** It does not tie to either EBITDA figure on a full-GAAP basis.
  - Using filings-based D&A and add-backs, a GAAP EPS of $24.85 needs about $9.9–10.2B of adjusted EBITDA.
  - If brokers exclude Prolec amortization, it needs about $9.2–9.4B, which sits nearer FactSet's $9,339M.
  - The P/E of 38.7x therefore rests on an EPS of mixed definition [computed §4-C].
- **No published segment consensus exists for FY26–FY28 in any free source searched.**
  - The only published FY27 segment figures are GLJ's own Power 18.5% and its quoted "consensus" of 20.7% [S1: GF] [S2: corpus 235411, MarketBeat 09-18].
  - New since the brief: Mizuho (Neutral, $949, 09-30) cut FY27 EBITDA from $9.4B to $9.3B "due to lower Electrification margin growth" and raised FY28 from $12.8B to $13.0B. **[SINGLE-SOURCE for the estimates]** [S1: INV-MZ]. SI-MZ confirms the note, rating and analyst, but the estimates sit behind its paywall.
- **Quarterly consensus is not internally consistent, and the two vendors miss in opposite directions.**
  - MarketScreener's FY27 quarters sum to EBITDA of $9,886M against an annual $9,570M (+3.3%).
  - ChartMill's quarters sum to $9,093M against an annual $9,652M (−5.8%).
  - The H2'26 margin consensus needs is the same at both: 16.33% (MarketScreener) and 16.29% (ChartMill), against 15.0% at the guide midpoint and 16.75% at the top of guide [computed §4-B].
- **Consensus FY26→FY27 incremental EBITDA margin is 44.7% (FactSet) to 49.8% (MarketScreener).**
  - Delivered: 37.1% for FY24→FY25, and 27.9% for H1'26 year on year [computed §4-D; 10K; Q2REL; MS quarters].
  - This bridge of company totals is the only Street FY26→FY27 bridge that can be built from published inputs.

---

## 2. Answers

### Q1. Vendor reconciliation

**FY27**

| Vendor (date) | Revenue $M | EBITDA $M | EBIT $M | EPS | FCF $M | n / range | FY25 EBITDA actual shown |
|---|---|---|---|---|---|---|---|
| MarketScreener (09-29) | 52,740 | 9,574 (18.15%) | 8,150 | 24.85 | 7,417 | 37 analysts (ratings); no per-line count | 3,196 ✓ adj |
| MarketScreener (09-04 cache) | 52,731 | 9,570 | 8,166 | 24.80 | 7,402 | — | 3,196 ✓ |
| FactSet / Boursorama (09-26) | 52,888 | 9,339 (17.66%) | 8,150 | 24.76 | n/a (cash flow/share 32.55) | 40 analysts (ratings) | 3,196 ✓ adj; EBIT 1,389 ≈ GAAP |
| FactSet / MarketWatch (09-02) | — | — | — | 24.70 (17.16–29.49) | — | 40 ratings | FY25 EPS "7.28" (not GAAP 17.69) |
| FactSet / cnyes (07-23) | 52,632 mean / 52,405 median (49,104–55,657) | — | — | 24.78 / 24.68 (17.16–30.41) | — | 25 (FY26 EPS) | — |
| Yahoo (Sep, cache) | 52,680 (49,100–55,660) | — | — | 24.69 (17.16–29.49) | — | revenue n=35; EPS n=27 | — |
| Equibles (09-23) | 52,740 (49,100–55,660) | — | — | 24.85 (17.16–29.95) | — | revenue n=34; EPS n=26 | Same feed as MarketScreener (CT-09) |
| ChartMill (08-20 cache) | 53,346 | 9,652 | 8,466 | 24.75 | — | — | **2,525 ✗** (EBIT 1,672 ✗) |
| S&P CIQ / TIKR (09-27) | — | — | — | — | "~7.4B" | 33 price targets, low $940 | — |
| Zacks / Barchart | — | — | — | 24.24 (08-04); 24.27 (08-18, n=11); 24.09 (09-24) | — | — | — |
| LSEG | not found for FY27 (only Q2 "below LSEG estimates", Reuters 07-22) | | | | | | |
| Visible Alpha | FY27 not found; only FCF FY26 $12.4B, FY29 $10.9B (Motley Fool/AOL 09-02) | | | | | | |

**FY26**

| Vendor | Revenue | EBITDA | EBIT | EPS |
|---|---|---|---|---|
| MarketScreener (09-29) | 46,282 | 6,359 | 4,662 | 30.78 |
| FactSet / Boursorama | 46,306 | 6,394 | **4,342** | 30.91 |
| FactSet / MarketWatch | — | — | — | 30.69 (26.83–33.23) |
| Yahoo | 46,260 (45,300–46,840; n=31) | — | — | 30.74 (n=20) |
| ChartMill | 46,511 | 6,400 | 4,772 | 15.52 (ex-gain basis) |
| Zacks (09-03) | 46,290 | — | — | 30.62 |
| Mizuho (09-30) | ">46B" | 6.5B | — | — |

**FY28**

| Vendor | Revenue | EBITDA | EPS |
|---|---|---|---|
| MarketScreener | 60,500 | 13,064 (21.6%) | 34.22 |
| FactSet / cnyes (07-23) | 60,511 | — | 34.71 |
| FactSet / MarketWatch (09-02) | — | — | 34.76 (22.45–46.41) |
| ChartMill | 61,516 | 13,184 | 35.40 |
| Mizuho | — | 13.0B | — |

Boursorama does not show FY28.

**Definition check.** Two vendors are on GEV's adjusted-EBITDA definition:
- MarketScreener: FY24 2,035 and FY25 3,196 [CT-03].
- FactSet/Boursorama: FY25 3,196.
- Both match the 10-K reconciliation "Adjusted EBITDA (Non-GAAP) $3,196 $2,035" [10K MD&A chunk 29797].
- ChartMill's actuals (FY25 2,525; FY24 2,064) are not on that basis. Its FY27 figure of $9,652M should not be used as a like-for-like consensus.

**Why EBIT can match while EBITDA differs.**
1. The line is mixed-basis. The FY25 EBIT actual is GAAP operating income ($1,388M) [S1: 10K MD&A "Operating income (loss) $1,388 $471"] [S2: MS-0904 EBIT row 471 / 1,388; BOURSO 1,389]. But the FY27 EBITDA–EBIT gaps (1,424 MarketScreener; 1,189 FactSet) are below the filings-implied FY27 D&A of about $1.67B (§4-C). The EBIT estimates are therefore mostly not GAAP operating income.
2. Each line is averaged over whichever brokers submit it. EBITDA and EBIT contributor sets differ, and neither vendor publishes per-line counts.
3. The two vendors may be the same feed at different settings. EBIT matches to the dollar on 09-26 and 09-29, but FY26 EBIT differs by $320M (4,662 vs 4,342), so they are not identical feeds.
   - Boursorama notes that FactSet recommends the median. Whether Boursorama displays median or mean is **not stated**.
   - MarketScreener's upstream provider is **not verified**.
   - The $235M FY27 EBITDA gap is the same order of size as FY25 restructuring plus separation add-backs (277 + 180 = 457 [10K]). That fits a mix of "GAAP EBITDA" and "adjusted EBITDA" contributors. **This is a hypothesis, not verified.**

### Q2. Published segment-level estimates

| Item | Value | Source | Status |
|---|---|---|---|
| GLJ FY27 Power margin | 18.5% | GF 09-15; corpus 235411 | Two sources (same GLJ wire) |
| GLJ-quoted "consensus" FY27 Power margin | 20.7% | Same | **[SINGLE-ORIGIN]**: GLJ is the only originator; no vendor publishes it |
| GLJ FY27 EBITDA | $7.42B vs "Street $9.45B" | GF; corpus 235411 | Two sources |
| Mizuho FY27 EBITDA | $9.3B (from $9.4B), cut on "lower Electrification margin growth" (no segment number) | INV-MZ 09-30 | **[SINGLE-SOURCE]**; SI-MZ paywalled |
| Mizuho FY26 | revenue >$46B; margin ~14%; adjusted EBITDA $6.5B (from $6.7B), with "modest power margin improvement in the third quarter" | INV-MZ | **[SINGLE-SOURCE]** |
| Visible Alpha segment consensus | exists (S&P editorial post 2026-03-10 says VA shows growth "led by the Electrification and Power divisions") but no numbers are public | LinkedIn post, Anisha T., 03-10 | Numbers not accessible |
| Company-compiled consensus | none found (GEV corpus and web) | — | — |

Also searched with no segment numbers found: StreetInsider, TheFly (via TipRanks), Investing.com, MarketScreener news, Benzinga, Barron's/Bloomberg, Reuters, 24/7 Wall St, Lark Research (company-level only).

**Implication.** The "Street needs Power at 21.5–23.5%" figure (D01A §1) remains a back-solve. It assumes Electrification at 21–22% [R01 errata #2]. The only published comparison is GLJ's 20.7%.

### Q3. Quarterly shape

MarketScreener figures are from the 09-04 cache; ChartMill from the 08-20 cache.

| Quarter | Revenue: MS / CM / YF | EBITDA: MS / CM | Margin: MS / CM | EPS: MS-implied / CM / YF / MW |
|---|---|---|---|---|
| Q3'26 | 12,004 / 12,118 / 12,000 (n=18) | 1,702 / 1,728 (TIKR "~1.7B") | 14.18% / 14.26% | NI 1,125 / 4.09 / 4.17 (n=14) / 4.08 (3.08–5.28) |
| Q4'26 | 13,876 / 13,954 / 13,880 | 2,523 / 2,520 | 18.18% / 18.06% | — / 6.40 / 6.44 / 6.33 (3.74–8.05) |
| Q1'27 | 11,146 / 11,159 | 1,928 / 1,841 | 17.30% / 16.50% | — / 4.53 |
| Q2'27 | 12,791 / 12,946 | 2,354 / 2,288 | 18.40% / 17.67% | — / 5.46 |
| Q3'27 | 13,394 / 13,018 | 2,413 / 2,164 | 18.02% / 16.62% | — / 5.76 |
| Q4'27 | 15,684 / 15,081 | 3,191 / 2,800 | 20.35% / 18.57% | — / 7.26 |
| **FY27 quarters summed** | 53,015 / 52,204 | **9,886 / 9,093** | 18.65% / 17.42% | — / 23.01 |
| FY27 annual | 52,731 / 53,346 | 9,570 / 9,652 | 18.15% / 18.09% | 24.80 / 24.75 |

- **Do the quarters sum to the annual?** No, at either vendor, and the errors run in opposite directions: MarketScreener +$316M, ChartMill −$559M. Quarterly estimates come from a smaller subset of brokers. The 9,886 vs 9,570 finding from the earlier pull is reproduced.
- **H2'26 margin needed** [computed §4-B]:
  - Consensus: 16.33% (MarketScreener) and 16.29% (ChartMill).
  - Guide midpoint: 15.00%. Top of guide: 16.75%. Bottom of guide: 13.25%.
  - Consensus therefore sits about 74% of the way from the midpoint to the top.
- **Seasonal point.** FY27 consensus of 18.15% roughly equals the Q4'26 consensus exit rate (18.2%). Delivered Q4 margins have run above the full year: +2.2 pts in FY25 (10.57% vs 8.40%) and +4.4 pts in FY24 (10.22% vs 5.83%) [MS quarters; 10K]. So FY27 consensus means the full-year average reaches a seasonal-peak exit rate.
- **Recent quarterly EBITDA consensus record.**
  - Q4'25: $1,158M vs $1.29B estimate (−10.3%) [corpus 468381, StockStory].
  - Q2'26: $1,250M vs about $1,276M (−2.0%) [TIKR] [R08: StockStory −2.1%; Reuters "below LSEG"].
  - Q1'26 consensus: not found.

### Q4. Range and dispersion

- **FY27 EPS**
  - Low $17.16 appears in every vendor: Yahoo, MarketWatch, Equibles and FactSet/cnyes. It was already in the pool on 07-23, so it is **not** GLJ, who initiated on 09-14. The holder is **not identified**.
  - High: $29.49 (Yahoo, MarketWatch); $29.95 (Equibles); $30.41 (FactSet 07-23).
  - Dispersion: (29.49 − 17.16) / 24.69 = 50% of the mean [computed].
- **FY27 revenue:** $49.10–55.66B across Yahoo, Equibles and FactSet 07-23. That is 12.4% of the mean.
- **FY27 EBITDA high/low:** not published by any vendor found. Named individual estimates:
  - GLJ $7.42B (09-14, lowest public).
  - Mizuho $9.3B (09-30).
  - No named estimate above $9.65B was found.
  - Lark Research (independent, Sell, $900 target, 08-04) publishes FY27 revenue of $54.5B and GAAP EPS of $21.50, but no EBITDA [Lark 08-04; F01 "Lark, single-source"].
- **Rating-count traps.**
  - FactSet (Boursorama, MarketWatch) shows 1 Sell. MarketScreener shows 0.
  - ChartMill logs "GLJ Research Maintains Buy→Buy 2026-01-12", which conflicts with "initiated at Sell 09-14" [CM; GF]. This is a vendor-log quirk; single-source.

### Q5. What bulls cite for FY27 (since July)

1. **Higher-priced backlog converting.** Guggenheim (Osha) raised its target to $1,450, with "margin expansion from higher-priced backlog" among three pillars. This is the article's paraphrase, not a verbatim quote.
   - [S1: 24/7 Wall St 09-16] [S2: WallStreetZen 07-23 target log $1,450]
2. **Services and installed base.**
   - Jefferies (Dumoulin-Smith), target $1,155 → $1,185 on 09-11. The note criticised "peak order myopia" (verbatim phrase) and forecast >$70M per GW-year of services in the 2030s.
   - Jefferies catalysts: the January FY27 guide and March-2027 long-term guidance.
   - Baird (Outperform, $1,400, 09-17) and Morgan Stanley (Arcaro, $1,350, 09-17) both cite service durability.
   - [S1: edgex 09-12] [S2: corpus 246520] [S3: Investing.com 09-17 Baird; TipRanks 09-17]
3. **Electrification and data centres.** Guggenheim's "hyperscaler-driven demand for transformers and turbines" [24/7 Wall St 09-16]. Bernstein (Outperform, $1,298) cites electrification [INV-MZ recap; R08 Bitget].

Not found in any broker text: Wind losses ending, and buybacks as FY27 drivers. The Wind improvement claim is the CEO's ("materially better in 2027") [D01A; MB-LAG].

### Q6. Neutral and negative views

| Broker (date) | Rating / target | View | Sources |
|---|---|---|---|
| Citi, Kaplowitz (07-22/23) | Neutral; $1,219 → $1,125 | The "relatively modest" revenue raise and unchanged margin forecast "could limit upside" (Bloomberg paraphrase) | S1: Financial Post/Bloomberg 07-22; S2: MarketScreener 07-23 (target change) |
| William Blair, Dorsheimer (07-22) | Buy | Investors "were expecting another EBITDA beat and raise with margin expansion" (Reuters paraphrase) | S1: Reuters 07-22; S2: **[SINGLE for the quote]** |
| Mizuho, Mandloi (09-30) | Neutral, $949 | FY27 cut to $9.3B on lower Electrification margin growth | S1: INV-MZ; S2: SI-MZ (rating and target only) |
| BNP Paribas, Sutton (04-27) | Outperform → Neutral; target $765 → $1,190 | Needs visibility on execution of >110 GW; capacity sold out | S1: MarketScreener AU 04-27; S2: AInvest / GuruFocus 04-27 |
| GLJ, Johnson (09-14) | Sell, $470 | Power 18.5% vs consensus 20.7%; FY27 EBITDA $7.42B | S1: GF; S2: corpus 235411 |
| Lark Research (08-04) | Sell, $900 | Valuation; FY27 GAAP EPS $21.50 | S1: larkresearch.com; S2: **[SINGLE]** |

No broker note found that states a FY27 Power margin number, other than GLJ.

### Q7. Does FY27 EPS reconcile to EBITDA?

**MarketScreener's own walk ties.**

| Step | 09-29 | 09-04 |
|---|---|---|
| EBITDA | 9,574 | 9,570 |
| Less "D&A + other" | 1,424 | 1,404 |
| EBIT | 8,150 | 8,166 |
| Plus EBIT→EBT (non-op/interest) | 714 | 679 |
| EBT | 8,864 | 8,845 |
| Tax + NCI | 24.9% | 24.9% |
| Net income | 6,655 | 6,642 |
| EPS | 24.85 | 24.80 |
| Implied shares | 267.8M | 267.8M |

The implied share count compares with MarketScreener's own 266.334M, which would give $24.99. MarketScreener's "interest paid" line for FY27 is −140, i.e. net interest income [MS-0904].

FactSet: EBITDA 9,339 → EBIT 8,150 (gap 1,189) → EPS 24.76. FactSet does not show EBT or NI.

**Against the filings.** Annualised H1'26 items [10Q Note 24; Q2REL p.8]:

| Item | Annualised FY27 value |
|---|---|
| D&A (Q2 418 × 4) | 1,672 |
| Restructuring | 204 |
| Separation | 122 |
| Non-operating benefit income | 506 |
| Net interest income | 200 |

- A GAAP EPS of $24.85 needs adjusted EBITDA of **$9.93–10.16B**.
- If brokers exclude about $715M of Prolec amortization, it needs **$9.21–9.44B**.
- At MarketScreener's $9,574M, GAAP EPS comes out at about **$23.2–23.9**.

**Verdict.** The EPS clusters tightly ($24.69–24.85) while EBITDA spreads ($9,339–9,574M). The EPS is anchored on a broker "EBIT" that sits before at least some amortization. On an ex-amortization basis it supports FactSet's ~$9.34B better than MarketScreener's $9.57B. On a full-GAAP basis it supports neither. **Research inference; the definitions are not disclosed.**

### Q8. Street bridge and cleanest figure

**Published pieces**
- Company revenue, EBITDA, EBIT and EPS (two vendors).
- FY26 segment guides (company).
- GLJ's Power 20.7% (single origin).
- Mizuho's qualitative Electrification driver.

**Missing**
- Any segment consensus for revenue or margin, in any year.
- A Wind consensus.
- Corporate costs.
- A per-line EBITDA contributor count.

**Company-level bridge** [computed]:
- MarketScreener: +$6,458M revenue, +$3,215M EBITDA → 49.8% incremental margin.
- FactSet: +$6,582M revenue, +$2,945M EBITDA → 44.7%.

**Cleanest single figure.** FY27 adjusted EBITDA is shown as a two-vendor band, $9,339M (FactSet via Boursorama, 26-Sep-2026) to $9,574M (MarketScreener, 29-Sep-2026). Both vendors show FY25 = $3,196M, GEV's non-GAAP adjusted EBITDA. Whether to pick one end or the midpoint of about $9.46B is the team's choice. Quarterly sums and ChartMill should not be used.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agree | Conf |
|---|---|---|---|---|---|---|
| 1 | FY27 EBITDA, FactSet | 9,339 | BOURSO 09-26 | GLJ "Street $9.45B" (GF) | close (1.2%) | M |
| 2 | FY27 EBITDA, MarketScreener | 9,574 / 9,570 | MS-0929 (CT-02) | MS-0904 | exact (vendor over time) | H |
| 3 | FY27 EBIT shared | 8,150 | BOURSO | MS-0929 (brief/CT) | exact | M |
| 4 | Vendor FY25 EBITDA = adjusted | 3,196 | 10K MD&A chunk 29797 | BOURSO; MS | exact | H |
| 5 | Vendor FY25 EBIT = GAAP operating income | 1,388 | 10K MD&A "Operating income (loss) $1,388" | MS-0904; BOURSO 1,389 | exact / close | H |
| 6 | ChartMill FY25 EBITDA is off-basis | 2,525 vs 3,196 | CM | 10K | conflict | H |
| 7 | Q2'26 D&A | 418 (H1 760) | 10Q Note 24 | Q2REL p.8 | exact | H |
| 8 | Prolec intangibles and lives | 2,860/12; 533/6; 8/3; 771/2 years | 10Q Prolec note (offset 37044) | [SINGLE-SOURCE]; Q1 10-Q -26-000064 has a prior version | — | M |
| 9 | FY27 EPS | 24.85 / 24.76 / 24.70 / 24.69 | MS | BOURSO; MW; YF | close | H |
| 10 | FY27 EPS range | 17.16–29.49 | YF | MW | exact | H |
| 11 | FY27 revenue range | 49.10–55.66B | YF | EQ; CN 07-23 | exact | H |
| 12 | FY27 FCF | 7,417 / ~7.4B | MS | TIKR (CIQ) | close; **no longer single-source** | M |
| 13 | Q3'26 EBITDA consensus | 1,702 / 1,728 / ~1.7B | MS-0904 | CM; TIKR | close | H |
| 14 | Q3'26 revenue consensus | 12,004 / 12,118 / 12.0B | MS | CM; YF | close | H |
| 15 | Q3'26 EPS consensus | 4.08 / 4.09 / 4.17 | MW | CM; YF | close | H |
| 16 | FY27 quarterly EBITDA sums | 9,886 (MS) vs 9,093 (CM) | MS-0904 | CM | conflict (finding) | H |
| 17 | H2'26 consensus margin | 16.33% / 16.29% | MS | CM | close | H |
| 18 | Mizuho FY27 / FY28 EBITDA | 9.3B / 13.0B | INV-MZ 09-30 | SI-MZ (rating/target only) | **[SINGLE]** on estimates | M |
| 19 | GLJ Power 18.5% vs "consensus" 20.7% | — | GF | corpus 235411 | exact (same origin) | M |
| 20 | Q2'26 EBITDA miss | 1,250 vs ~1,276 | TIKR | StockStory via R08; Reuters | close | H |
| 21 | Q4'25 EBITDA miss | 1,158 vs 1.29B | corpus 468381 (StockStory) | [SINGLE] for the estimate | — | M |
| 22 | Citi target 1,219 → 1,125, Neutral | — | MarketScreener 07-23 | Fancy Hints 07-25 | exact | H |
| 23 | BNP downgrade to Neutral, $1,190 | — | MarketScreener AU 04-27 | GuruFocus / AInvest 04-27 | exact | H |
| 24 | FactSet ratings include 1 Sell | 1 | BOURSO | MW | exact | H |

## 4. Arithmetic

**A. EV multiples and lookup values**
- EV/EBITDA = 247,200 / 9,339 = **26.5x**; 247,200 / 9,574 = 25.8x. EV is from the brief.
- Lookup value at 25x on FactSet: (25 × 9,339 + 9,113) / 266.33 = **$910.8**. On MarketScreener: $932.9. Difference: −$22/share.

**B. H2'26 margins**
- Guide midpoint: FY26 revenue 46,000 × 13% = 5,980. Less H1 EBITDA 2,146 = 3,834. H2 revenue = 46,000 − 20,442 = 25,558. H2 margin = 3,834 / 25,558 = **15.00%**.
- Top of guide: 46,500 × 14% − 2,146 = 4,364; 4,364 / 26,058 = **16.75%**.
- Bottom of guide: 45,500 × 12% − 2,146 = 3,314; 3,314 / 25,058 = **13.23%**.
- MarketScreener consensus: (1,702 + 2,523) / (12,004 + 13,876) = 4,225 / 25,880 = **16.33%**.
- ChartMill consensus: 4,248 / 26,072 = **16.29%**.
- H1 inputs: Q2REL; 10Q.

**C. EPS↔EBITDA**
- Prolec amortization: 2,860/12 + 533/6 + 8/3 + 771/2 = 238.3 + 88.8 + 2.7 + 385.5 = **715** per year (straight-line assumption).
- Adjusted EBITDA required for EBT of 8,864, full GAAP: 8,864 + 1,672 + (100 to 326 of restructuring and separation) − 506 − 200 = **9,930–10,156**.
- Excluding Prolec amortization: subtract 715 → **9,215–9,441**.
- GAAP EPS at 9,574: (9,574 − 1,672 − 326 + 706) × 0.7508 / 267.8 = **$23.22**; with 100 of adjustments, **$23.85**.

**D. Incremental margins**
- FY26→FY27, MarketScreener: (9,574 − 6,359) / (52,740 − 46,282) = 3,215 / 6,458 = **49.8%**.
- FY26→FY27, FactSet: (9,339 − 6,394) / (52,888 − 46,306) = 2,945 / 6,582 = **44.7%**.
- FY24→FY25: (3,196 − 2,035) / (38,068 − 34,935) = **37.1%** [10K].
- H1'26 year on year: (2,146 − 1,227) / (20,442 − 17,143) = **27.9%** [Q2REL; H1'25 revenue from MS quarters 8,032 + 9,111].

**E. Quarterly sums and margins** are shown in the Q3 table; each margin is quarter EBITDA / quarter revenue.

## 5. General question bank

- **G2:** FY27 consensus needs 45–50% incremental margins, against 37% delivered in FY25 (§4-D). The full-year FY27 margin roughly equals the Q4'26 exit rate.
- **G20:** Definition traps:
  - EBIT is mixed-basis.
  - EPS is mixed ex-amortization/GAAP.
  - ChartMill is off-basis.
  - Quarterly sums don't tie.
  - The FactSet MarketWatch FY25 EPS of "7.28" is not GAAP.
  - The 20.7% Power figure has a single origin.
- **G22:** The only dated revelation of segment assumptions is GEV's own January FY27 outlook. The Street publishes no segment numbers the team could track before then.
- **G24:** FY27 FCF of about $7.4B is now two-sourced (MarketScreener; TIKR/CIQ).

## 6. What would change this

- **If the upstream sources became known:** MarketScreener's provider disclosed as FactSet would reduce the $235M gap to mean vs median (or refresh timing). Either vendor publishing per-line counts would also re-open the vendor comparison.
- **If Prolec amortization turns out different:** if the "trademarks and other" $771M asset is not straight-line over 2 years, or the final PPA (due by Q1'27) changes the lives, FY27 D&A changes and so does the §4-C walk.
- **If a segment consensus surfaced:** any Visible Alpha, company-compiled or broker segment table would replace GLJ's single-origin 20.7%.
- **If FY27 EPS diverges:** an FY27 EPS revision that is not matched by EBIT would break the EBIT-anchoring inference.

## 7. Disagreements with the master brief

1. The brief treats "consensus FY27 EBITDA" as $9,574M. It is a vendor band of **$9,339–9,574M**, and the multiple is 25.8x–26.5x.
2. "38.7x FY27 EPS" rests on an EPS that is not a clean GAAP figure (§4-C).
3. FY27 FCF is **no longer single-sourced** (TIKR/CIQ ~$7.4B).
4. The brief lists no December event and no later broker estimate. Mizuho's 09-30 note, published after the brief's 09-29 cut, trims FY27 to $9.3B and raises FY28 to $13.0B. **[SINGLE-SOURCE]**

## 8. Open items

- **MarketScreener's data provider:** check the MarketScreener legal/about page, and whether Boursorama shows median or mean.
- **Per-line contributor counts:** only paid Bloomberg or FactSet terminals give these.
- **The $17.16 FY27 EPS holder:** not identified. Check TipRanks or MarketBeat per-broker estimate logs.
- **Mizuho $9.3B second source:** the StreetInsider premium text, or TheFly.
- **Q1'26 EBITDA consensus vs actual ($896M):** this would complete the quarterly miss record.
- **Visible Alpha segment consensus:** an S&P MI article linked from the 2026-03-10 LinkedIn post (lnkd.in/eiVCRDiW). It was not opened.
- **Final Prolec PPA and amortization schedule:** the Q3'26 10-Q, filed 10-28.
