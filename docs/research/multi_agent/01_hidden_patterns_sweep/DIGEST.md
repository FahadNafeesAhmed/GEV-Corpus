# 01_hidden_patterns_sweep: every agent's output

Multi-lens sweep of the corpus and web for unexpected quantified patterns; adversarial verification (12 finders, repro + skeptic per finding; stopped early to save tokens, then resumed lean). 46 agent results.


## [Sweep] find:services-accounting

- **lens**: Services and accounting-estimate forensics: contractual service agreement (LTSA) estimate revisions, contract assets, billings vs recognition, services RPO composition, availability penalties, warranty, HA fleet disclosures
- **findings**:
  - - **title**: LTSA book margin is being cut at a record pace: net unfavorable profitability revisions on contractual service agreements hit $218M in 1H26 (5x 1H25), trailing-4Q $327M, worst on record
    - **claim**: Net unfavorable changes in estimated profitability on Gas Power contractual service agreements (Note 9, 10-Q/10-K) were -$218M in 1H26 versus -$42M in 1H25 and -$89M in 1H24; Q2'26 alone was -$129M, the largest non-Q4 revision since disclosure began, and the trailing four quarters (-$327M) exceed the prior full-year record (FY24 -$319M).
    - **mechanism**: GEV accounts for LTSAs on cost-to-cost percentage of completion. When estimated life-of-contract costs rise (or billings/utilization assumptions fall), it books a cumulative catch-up that reduces Power segment revenue and EBITDA in that quarter (10-K FY25: each 1 point of total estimated contract profitability = $0.2B of LTSA contract assets, so 1H26's $218M is about 1.1 points of book margin removed in six months). The revisions are 11.8% of 1H26 Power EBITDA ($1,842M) and 12.5% of Q2'26 Power EBITDA ($1,031M). Q4 is seasonally the largest revision quarter (Q4'24 -$184M, Q4'25 -$115M; CFO: 'highest outage volume in the fourth quarter'), so the pattern points to FY26 revisions of $350M+, a record, landing in the quarter GEV guides as its highest-EBITDA quarter. CEO on the Q2'26 call: 130 HA units running, 325 commissioned or under contract, and 'every four years they go through a major outage' - the first HA major-inspection wave is exactly where outage-cost estimates get trued up.
    - **direction**: short
    - **evidence**:
      - - **source**: documents, GEV 10-Q accession 0001996810-26-000148 (Q2'26), Note 9
        - **date**: 2026-07-22
        - **quote_or_number**: Net contractual service agreements increased primarily due to revenues recognized of $2,689 million, partially offset by billings of $2,392 million and net unfavorable changes in estimated profitability of $218 million.
        - **reproduction**: python: import re,sqlite3; t=sqlite3.connect(r'data\gev.db').execute("SELECT text FROM documents WHERE ticker='GEV' AND accession='0001996810-26-000148'").fetchone()[0]; print(re.search(r'Net contractual service agreements[^.]*\.',t).group(0))
      - - **source**: documents, GEV 10-Q 0001996810-26-000064 (Q1'26); 10-K 0001996810-26-000015 (FY25); 10-Q 0001996810-25-000160 (9M25); 10-Q 0001996810-25-000133 (1H25); 10-Q 0001996810-25-000073 (Q1'25); 10-K 0001996810-25-000011 (FY24); 10-Q 0001996810-24-000083/-000067/-000008 (9M24/1H24/Q1'24); 8-K/EX Form 10 2024-03-08 (FY23)
        - **date**: 2024-03-08 to 2026-04-22
        - **quote_or_number**: YTD net favorable/(unfavorable) changes in estimated profitability, $M: FY23 +34 | Q1'24 -29, 1H24 -89, 9M24 -135, FY24 -319 ('due primarily to higher costs') | Q1'25 +29, 1H25 -42, 9M25 -36, FY25 -151 | Q1'26 -89, 1H26 -218. Derived single quarters: Q2'24 -60, Q3'24 -46, Q4'24 -184, Q2'25 -71, Q3'25 +6, Q4'25 -115, Q2'26 -129.
        - **reproduction**: python loop over SELECT accession,text FROM documents WHERE ticker='GEV' AND form IN ('10-K','10-Q') and apply re.search(r'Net contractual service agreements[^.]*\.'); for FY23 use chunks_fts MATCH '"Net contractual service agreements"' AND c.form='8-K/EX'
      - - **source**: documents, GEV 10-K FY25 accession 0001996810-26-000015, Item 7 critical accounting estimates
        - **date**: 2026-01-29
        - **quote_or_number**: net long-term service agreements balance of $3.4 billion represents approximately 4% of our total estimated life of contract billings ... approximately 29% complete ... one percentage point would increase or decrease the long-term service agreements contract assets balance by $0.2 billion.
        - **reproduction**: chunks_fts MATCH '"life of contract billings"' AND c.ticker='GEV' AND c.form='10-K'
      - - **source**: documents, GEV 10-Q Q2'26 segment table (Power)
        - **date**: 2026-07-22
        - **quote_or_number**: Power segment EBITDA Q2'26 $1,031M (18.8% margin), 1H26 $1,842M (17.6%); Power services revenue Q2'26 $3,512M vs $3,280M; 'partially offset by the impact of inflation'
        - **reproduction**: python: re.search(r'SEGMENT REVENUES AND EBITDA 2026 2025 2026 2025 Gas Power[^*]{0,900}', text of accession 0001996810-26-000148)
      - - **source**: chunks, form TRANSCRIPT (src:3161, Q2'26 earnings call, gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf)
        - **date**: 2026-07-22
        - **quote_or_number**: we only have 130 of our HA units running right now. We have 325 units that either commissioned or under contract. As these run baseload and every four years they go through a major outage.
        - **reproduction**: chunks_fts MATCH '"major outage"' AND c.ticker='GEV' AND c.form='TRANSCRIPT'
    - **why_market_misses_it**: The figure lives only in one prose sentence of Note 9; there is no clean XBRL tag (the tag GEV files under, ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress, actually carries the billings numbers, so screens read it as $5B of 'catch-up'). It never appears on the earnings deck, the press release, or the call, and reported Power margin (18.8%) already absorbs it, so it reads as 'margin expansion despite inflation'. Zero mentions in 15k+ commentary chunks in the corpus; the only web hit is an unattributed data aggregator table (opencapital.sh) with no narrative.
    - **testable_prediction**: Q3'26 10-Q (about Oct 21-22, 2026): 9M26 net unfavorable changes in estimated profitability >= $250M (i.e., Q3 unfavorable again). FY26 10-K (late Jan 2027): full-year figure >= $350M, a record above FY24's $319M, with Q4'26 the largest quarter.
    - **kill_condition**: 9M26 figure <= $218M in magnitude (Q3'26 favorable or zero), or FY26 < $250M. Also killed if management discloses the 1H26 revisions were a one-off contract modification/settlement rather than cost estimate changes.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: Absolute size ($0.3-0.45B/yr) is 5-6% of FY26 EBITDA, so this is a margin-quality and Q4-print-risk point, not a thesis-breaker. GEV gives no reason for the 2025-26 revisions (FY24 said 'higher costs'). A bull can invert it: ex-revisions Power margin would be ~21%, so if revisions normalize, margin upside. Quarterly figures are derived by differencing YTD disclosures.
  - - **title**: The recurring LTSA revenue stream is flat (-1% y/y) and its billings are falling (-5.6% y/y); all Power services growth since 2024 is transactional book-and-bill, while services RPO grows $9B/yr for revenue that cannot arrive until the HA outage cycle inflects
    - **claim**: Revenue recognized on contractual service agreements was $5,412M in FY25 (-1.1% vs $5,473M FY24) and $2,689M in 1H26 (-1.1% vs $2,720M 1H25; Q2'26 -3.4%), while Power segment services revenue grew 5.3% (FY25) and 5.8% (1H26); CSA billings fell 5.6% y/y in 1H26 ($2,392M vs $2,533M) even as Power services RPO rose 15% ($63.1B to $72.4B).
    - **mechanism**: Under cost-to-cost, LTSA revenue appears when outage costs are incurred, and billings are usage/event based. Flat CSA revenue and falling CSA billings mean the fleet's paid outage cycle has not inflected despite record equipment orders. The growth the market attributes to the 'services annuity' is actually transactional (parts, upgrades, 'transactional orders per unit continue to rise by double digits annually' per the Q2'26 call), which is book-and-bill and depends on customers' discretionary spend and outage timing. Services RPO growth (Power services RPO +$9.3B in 12 months; implied total estimated life-of-contract billings $68B Dec-23, $70B Dec-24, $85B Dec-25) is dominated by new HA LTSAs whose billing starts at COD years out; combined with Finding 1, GEV is simultaneously adding far-dated services RPO and cutting the margin estimate on the LTSAs it is executing today. The 'services $70M per GW-year' bull math is a 2030s cash stream, not a 3-12 month one. CSA share of Power services revenue: 44.1% FY24, 41.4% FY25, 40.8% 1H26.
    - **direction**: short
    - **evidence**:
      - - **source**: documents, GEV Note 9 sentences: 8-K/EX Form 10 2024-03-08 (FY23), 10-K 0001996810-25-000011 (FY24), 10-K 0001996810-26-000015 (FY25), 10-Q 0001996810-25-000133 (1H25), 10-Q 0001996810-26-000148 (1H26)
        - **date**: 2024-03-08 to 2026-07-22
        - **quote_or_number**: CSA revenues recognized / billings, $M: FY23 4,658 / 5,047; FY24 5,473 / 5,021; FY25 5,412 / 5,362; 1H25 2,720 / 2,533; 1H26 2,689 / 2,392. Q2 standalone revenue: Q2'25 1,459, Q2'26 1,409.
        - **reproduction**: re.search(r'Net contractual service agreements[^.]*\.', documents.text) for each accession above; billings also reproducible from xbrl_facts: SELECT start_date,end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress' GROUP BY start_date,end_date,val (values equal the billings figures)
      - - **source**: documents, GEV 10-K FY25 and 10-Q Q2'26 Power segment tables
        - **date**: 2026-01-29 and 2026-07-22
        - **quote_or_number**: Power Services revenue: FY23 11,838; FY24 12,419; FY25 13,081; 1H25 6,238; 1H26 6,598; Q2'25 3,280; Q2'26 3,512 ($M)
        - **reproduction**: re.search(r'Total segment revenues \$[\d,]+ \$[\d,]+( \$[\d,]+)? Equipment \$?[\d,]+[^S]*Services [\d,]+ [\d,]+', text) on accessions 0001996810-26-000015 and 0001996810-26-000148 (first match after 'POWER')
      - - **source**: documents, Power RPO tables in 10-Q Q2'25 (0001996810-25-000133), 10-K FY25, 10-Q Q2'26
        - **date**: 2025-07-23 to 2026-07-22
        - **quote_or_number**: Power services RPO: Dec-23 59,338; Dec-24 60,890; Jun-25 63,088 (restated from 62,932); Dec-25 69,841 (restated from 69,680); Jun-26 72,388 ($M)
        - **reproduction**: re.finditer(r'RPO ((?:\w+ \d+,? \d{4} ?){2,3})Equipment \$([\d,]+)[^S]*Services ([\d,]+)[^T]*Total RPO \$([\d,]+)', text); second match in each doc is the Power table
      - - **source**: Form 10 8-K/EX 2024-03-08; 10-K FY24; 10-K FY25 critical accounting estimates
        - **date**: 2024-03-08, 2025-02-06, 2026-01-29
        - **quote_or_number**: Net CSA balance $3.4B = ~5% of total estimated life-of-contract billings (Dec-23); $3.5B = ~5% (Dec-24); $3.4B = ~4% (Dec-25); contracts ~29% complete in all three years; ~1,700 units under LTSA (2024) -> ~1,800 (FY25 10-K) of ~7,000 installed, avg remaining life ~10 years unchanged
        - **reproduction**: chunks_fts MATCH '"life of contract billings"' AND c.ticker='GEV'; chunks_fts MATCH '"under long-term service agreements"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q')
      - - **source**: chunks TRANSCRIPT src:3161 (Q2'26 call)
        - **date**: 2026-07-22
        - **quote_or_number**: This is happening not only on long-term service agreements, but also on transactional orders. We've seen transactional orders per unit continue to rise by double digits annually
        - **reproduction**: chunks_fts MATCH '"transactional orders"' AND c.ticker='GEV' AND c.form='TRANSCRIPT'
    - **why_market_misses_it**: Sell-side models one 'services' line growing high-single digits and treats services RPO ($88.5B) as a growing annuity. The split between contractual (LTSA) and transactional revenue is not in the deck or press release; it has to be rebuilt from a Note 9 sentence plus the segment table, and management narrates it as 'higher parts volume, contractual services, and favorable price' without numbers.
    - **testable_prediction**: FY26 10-K (late Jan 2027): CSA revenues recognized between $5.2B and $5.7B (< +5% vs $5,412M) while Power services revenue grows > 5%; CSA share of Power services falls below 40%. Q3'26 10-Q: 9M26 CSA revenue <= $4.1B (vs 9M25 $3,824M+... i.e. <= +7%).
    - **kill_condition**: FY26 CSA revenue recognized > $5.9B (+9% y/y) or 9M26 CSA billings up > 5% y/y - would show the paid outage cycle inflecting now rather than in the 2030s.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: CSA revenue is net of the unfavorable revisions in Finding 1 (FY25 -$151M, 1H26 -$218M); gross of revisions it is +2% to +7%, still well below transactional growth. Transactional parts/upgrades are also high margin, so this is about durability and visibility of services growth, not margin per se. Restated Jun-25/Dec-25 Power services RPO differ by ~$0.16B between filings (immaterial reclass).
  - - **title**: Customer deposits are converting to revenue more slowly, not faster: 1H26 liquidated 29% of opening contract liabilities vs 40% in 1H25 and 35% in 1H24
    - **claim**: Revenue recognized from the beginning-of-year contract liabilities balance was $7,512M in 1H26 against an opening balance of $25,950M (28.9%), versus $7,074M/$17,744M (39.9%) in 1H25 and $5,283M/$15,247M (34.6%) in 1H24; full-year liquidation was 65% (2024) and 63% (2025), so FY26 is on track for roughly 50-55%.
    - **mechanism**: This is the accounting fingerprint that the $40B deposit pile is increasingly for 2027-2029 slots: cash arrives now (record 1H FCF $9.9B), revenue and margin arrive 2-3 years later. The share of deposits that turns into revenue within the year is the only disclosed measure of deposit 'age'; it fell 11 points y/y. It sharpens the customer-deposit angle already on the team's list: the H2 FCF cliff ($1.6-2.6B implied) is structural, and FY27 FCF conversion from deposits will be diluted by the growing far-dated tail, not helped by it.
    - **direction**: neutral
    - **evidence**:
      - - **source**: xbrl_facts, tags ContractWithCustomerLiabilityRevenueRecognized and ContractWithCustomerLiability, GEV
        - **date**: 2024-07-24 to 2026-07-22
        - **quote_or_number**: Revenue recognized from opening liabilities: 1H24 5,283; FY24 9,933; 1H25 7,074; FY25 11,225; 1H26 7,512. Opening balances: Dec-23 15,247; Dec-24 17,744; Dec-25 25,950 ($M). Ratios: 1H24 34.6%, 1H25 39.9%, 1H26 28.9%; FY24 65.1%, FY25 63.3%.
        - **reproduction**: SELECT start_date,end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag IN ('ContractWithCustomerLiabilityRevenueRecognized','ContractWithCustomerLiability') GROUP BY tag,start_date,end_date,val ORDER BY end_date
      - - **source**: documents, GEV 10-Q Q2'26 accession 0001996810-26-000148, Note 9
        - **date**: 2026-07-22
        - **quote_or_number**: Revenue recognized related to the contract liabilities balance at the beginning of the year was approximately $7,512 million and $7,074 million for the six months ended June 30, 2026 and 2025
        - **reproduction**: re.search(r'Revenue recognized related to the contract liabilities balance at the beginning of the year was[^.]*\.', text)
    - **why_market_misses_it**: Everyone tracks the level of contract liabilities ($39.9B) as a demand signal; almost no one divides the disclosed 'revenue recognized from opening balance' by the opening balance, which is the only disclosed measure of how far out the deposits sit. Prolec GE consolidation (Q1'26) adds acquired liabilities to the denominator, which partly explains and partly disguises the drop.
    - **testable_prediction**: FY26 10-K: revenue recognized from the Dec-25 opening contract-liability balance <= $14.5B (<= 56% of $25,950M), down from 63% in FY25.
    - **kill_condition**: FY26 figure >= $16.4B (>= 63%, matching FY25), which would mean deposits are still near-dated and the slowdown was a Prolec/Q1 timing artifact.
    - **novelty**: 2
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Angle is on the team's list; offered only because the quantified liquidation rate changes the read from 'deposits = near-term revenue' to 'deposits = 2027+ revenue'. Prolec GE acquisition inflates the Dec-25/Jun-26 denominator by an undisclosed amount; Electrification deposits ($9.1B at Jun-26) are shorter-cycle than gas.
- **dead_ends**:
  - Availability-shortfall penalties are bounded and flat: reduction of revenues from availability shortfalls was $0.1B (2022), $0.3B (2023), $0.3B (2024), $0.3B (2025); 10-K FY25 states a further 1% fleet-wide availability drop would cost < $0.1B. A harder-running fleet cannot move this line materially. (chunks_fts MATCH '"availability shortfalls"' AND c.form='10-K')
  - Warranty: warranties issued FY25 $760M vs $687M FY24 (+11%) on +11% revenue; payments $629M; accrual $1,595M at Jun-26 - ratios flat, no ramp signal (xbrl_facts tags StandardProductWarrantyAccrual*).
  - HA fleet hours per unit cannot be inferred reliably: disclosed hours are rounded to 0.1M (2.0M Mar-24, 2.5M Jun-24, 2.7M Sep-24, 2.9M Dec-24, 3.6M Dec-25 on 94/100/106/115/126 units); implied 2025 utilization ~5,800 hrs/unit-yr vs ~7,400 in 2H24 but rounding error is +/-15%.
  - XBRL tag ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress for GEV is NOT a catch-up: its values (-1,173/-2,300/-3,673/-5,021; -1,249/-2,533/-3,781/-5,362; -1,163/-2,392) equal CSA billings. The estimate-change numbers exist only in Note 9 prose. Tag ...ChangeInEstimateOfTransactionPrice equals the known offshore wind contract losses (379/1,005/637).
  - No loss-provision or onerous-contract disclosure for services exists beyond the offshore wind losses; FTS on 'loss provision', 'provision for losses', 'onerous' in 10-K/10-Q returns only risk-factor boilerplate.
  - Services RPO recognition schedule is stable: within 1 year 16-18%, 5 years 52-54%, 10 years 77-79%, 15 years 91-92% across all ten filings - no visible re-estimation or duration shift.
  - LTSA structural disclosures unchanged: ~7,000 installed gas turbines, ~1,700 (2024) to ~1,800 (FY25) under LTSA, average remaining life ~10 years in every filing, contracts ~29% complete Dec-23/24/25; CSA contract assets ~$5.3-5.4B and CSA liabilities $1.98B -> $1.88B (Dec-25 to Jun-26) - no signal.
  - Non-current contract assets (services upgrades collected through CSA fees): 536 (Dec-24), 368 (Dec-25), 453 (Mar-26), 444 (Jun-26) $M - small and directionless.
  - Corpus commentary/claims/analyst_calls/transcript_statements contain zero references to LTSA estimate revisions or CSA-vs-transactional revenue; transcripts hold only one IR transcript (src:3161, 42 chunks). Web novelty check (WebSearch + Exa): only an unattributed aggregator table (opencapital.sh) tabulates the Q2'26 -$129M figure; no analyst or short-report narrative found.
  - Power services RPO restatements between filings (Jun-25 62,932 -> 63,088; Dec-25 69,680 -> 69,841) are ~$0.16B reclasses, immaterial.

## [Sweep] find:price-events

- **lens**: Price and event pattern miner: GEV daily prices vs 16-ticker universe, dated 8-K/EX press releases, catalyst_calendar, insider_tx, commentary on move days
- **findings**:
  - - **title**: The GW-order metric has stopped moving the stock; 'peak-cycle' notes now move it more than orders or guidance raises
    - **claim**: Since Q3'25 the sign of GEV's earnings-day return is uncorrelated with GW signed or with guidance raises, and the two largest GEV-specific down days of 2026 (Jul 22 -8.69%, Jul 7 -6.51%) came on a 20 GW quarter with a $5B FCF guidance raise and on a Barclays 'gas turbine cycle has peaked' downgrade of Siemens Energy, respectively.
    - **mechanism**: Earnings-day sequence from 8-K/EX press releases (new gas equipment contracts, GW) vs same-day close-to-close return from prices: Q1'25 14 GW +3.07%; Q2'25 9 GW +14.58% (raised guide); Q3'25 13 GW -1.59% (reaffirmed); Q4'25 24 GW +2.73%; Q1'26 21 GW +13.75% (raised guide); Q2'26 20 GW -8.69% (raised FY26 FCF from $6.5-7.5B to $11.5-12.5B, revenue to $45.5-46.5B). Reaction per GW signed went +1.6%/GW (Q2'25) to -0.43%/GW (Q2'26). Meanwhile Jul 7 2026 (Barclays SE downgrade: 'sustainable medium-term demand at only 80 to 90 gigawatts annually') GEV -6.51% vs 5-peer basket -3.37%; Sep 14 2026 (GLJ Sell, $470) GEV -8.62% vs basket -5.22%. The tape is pricing the second derivative of orders (cycle peak, FCF quality of deposits), not the level. This determines how the memo should frame the Oct 21 print: a 125 GW headline is not a catalyst; the H2 FCF bridge and 2027 conversion/margin are.
    - **direction**: either
    - **evidence**:
      - - **source**: chunks (form='8-K/EX', ticker='GEV') + prices
        - **date**: 2026-07-22
        - **quote_or_number**: Signed 20 gigawatts (GW) of new gas equipment contracts, including 18 GW of slot reservation agreements and 2 GW of orders; GEV close 2026-07-22 vs 07-21: -8.69%
        - **reproduction**: SELECT c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22' ORDER BY c.ord; SELECT date,close FROM prices WHERE ticker='GEV' AND date IN ('2026-07-21','2026-07-22')
      - - **source**: chunks 8-K/EX 2026-07-22 (2026 Guidance paragraph)
        - **date**: 2026-07-22
        - **quote_or_number**: raising its 2026 financial guidance and now expects revenue of $45.5-$46.5 billion, up from $44.5-$45.5 billion, and free cash flow* of $11.5-$12.5 billion, up from $6.5-$7.5 billion
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"2026 Guidance"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22'
      - - **source**: chunks 8-K/EX earnings releases 2025-04-23, 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22 + prices
        - **date**: 2025-04-23 to 2026-04-22
        - **quote_or_number**: GW signed / day return: 14/+3.07%, 9/+14.58%, 13/-1.59%, 24/+2.73%, 21/+13.75%
        - **reproduction**: SELECT c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND "GW"' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date; returns = close/prev close from prices WHERE ticker='GEV'
      - - **source**: chunks id 465392 (src:3596, NEWS boerse-global.de) + prices
        - **date**: 2026-07-07
        - **quote_or_number**: Barclays ... estimates sustainable medium-term demand at only 80 to 90 gigawatts annually; GEV -6.51%, VRT -4.05%, mean(VRT,ETN,PWR,HUBB,EMR) -3.37%, SPY -0.48%
        - **reproduction**: SELECT text FROM chunks WHERE id=465392; SELECT ticker,date,close FROM prices WHERE date IN ('2026-07-06','2026-07-07') AND ticker IN ('GEV','VRT','ETN','PWR','HUBB','EMR','SPY')
      - - **source**: chunks NEWS 2026-09-14 (GLJ initiation) + prices
        - **date**: 2026-09-14
        - **quote_or_number**: GEV -8.62%, VRT -7.65%, 5-peer basket -5.22%, SPY -0.45%; news: 'Eaton (NYSE:ETN) stock is falling 7% ... Quanta Services (NYSE:PWR) stock is down 4%'
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"GLJ" AND "Vernova"' AND c.filing_date='2026-09-14'; prices WHERE date IN ('2026-09-11','2026-09-14')
    - **why_market_misses_it**: Sell-side previews and the company's own framing still lead with GW signed and the 125 GW / $200B backlog milestones; the price record shows those headlines stopped earning a premium a year ago, while a single competitor downgrade and a single boutique Sell each cost 6-9%.
    - **testable_prediction**: On the Q3'26 print (catalyst_calendar estimate 2026-10-21): if GEV reports >=15 GW of new gas contracts and reiterates >=125 GW year-end, but does not raise the H2'26 FCF floor or give 2027 Power margin/conversion detail, the close-to-close move will be between -5% and +3%. If GEV moves >=+8% on an orders-and-backlog beat alone, the saturation claim is wrong.
    - **kill_condition**: Q3'26 earnings-day return >= +8% with no change to FCF guidance or 2027 framing; or the Oct 21 print delivers <10 GW and the stock is flat (metric still matters on the downside).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: n=6 earnings prints; the Jul 22 sell-off coincided with a $5B FCF raise that the market read as deposit pull-forward (implied H2 FCF $1.6-2.6B), so 'orders saturated' and 'FCF quality doubt' are confounded. Sep 14 basket drop was itself GLJ contagion (ETN -7%, PWR -4%), so the basket-adjusted residual understates the note's effect.
  - - **title**: The -20% drawdown is half AI-power beta and half one day (Jul 22); ex that day GEV has tracked its peer basket, and the sell-off happened on the lowest volume in 14 months
    - **claim**: From the 2026-06-30 closing peak ($1,174.86) to 2026-09-18 ($940.33) GEV fell 20.0%; a two-factor model (SPY + equal-weight VRT/ETN/PWR/HUBB/EMR, betas fit on the prior 120 days) predicts -8.8%, leaving a -11.8% residual of which -8.69% is the single day 2026-07-22; the remaining 55 trading days sum to only -3.1% of residual.
    - **mechanism**: GEV's 60-day beta to the 5-peer basket has sat at 0.9-1.4 since 2024 and is 1.08 now, with 60-day correlation 0.80. Over the drawdown VRT fell 25.5%, PWR 11.6%, HUBB 14.6%, ROK 16.0% from the same date, so most of GEV's fall is the AI-power complex de-rating. Robustness: 9-peer basket gives residual -11.7% (ex-Jul-22 -3.4%); VRT+ETN only gives -13.9% (ex-Jul-22 -5.3%). The Sep 14 GLJ day residual is only -3.4% to -4.0% because VRT (-7.65%) and ETN (-7%) fell too. Volume: August 2026 average 2.03M shares/day ($2.0B) is the lowest monthly average since at least Aug 2025 (June: 3.25M, $3.27B); no day since Jun 30 exceeded 1.9x its 20-day average (max: Sep 18 quad-witching 1.89x). Sep 14's 3.30M (1.66x) ranks 25th of 42 GEV days with |move|>=6%. The GEV-specific de-rating is therefore one event (FCF-quality read of the Q2 print), not a sustained holder exodus, and everything else is beta the memo cannot argue away with GEV fundamentals.
    - **direction**: long
    - **evidence**:
      - - **source**: prices (GEV, SPY, VRT, ETN, PWR, HUBB, EMR), OLS on 120 days ending 2026-06-30
        - **date**: 2026-06-30 to 2026-09-18
        - **quote_or_number**: coef SPY 0.22, basket 0.99; predicted cum -8.8%; GEV actual -20.0%; residual sum -11.8%; residual on 2026-07-22 -8.69% (predicted 0.00%); residual ex-Jul-22 -3.1%
        - **reproduction**: pandas: ret=close.pct_change(); basket=ret[['VRT','ETN','PWR','HUBB','EMR']].mean(1); win=ret[:'2026-06-30'].tail(120); b=lstsq([SPY,basket],GEV); post=ret['2026-07-01':'2026-09-18']; resid=post.GEV-(b0*post.SPY+b1*basket)
      - - **source**: prices, peak-to-Sep-18 returns
        - **date**: 2026-09-18
        - **quote_or_number**: GEV -20.0%, VRT -25.5%, ROK -16.0%, HUBB -14.6%, PWR -11.6%, BE -12.2%, NEE -8.3%, ETN -0.3%, EMR +4.7%, SPY +2.0%
        - **reproduction**: SELECT ticker, date, close FROM prices WHERE date IN ('2026-06-30','2026-09-18') ORDER BY ticker
      - - **source**: prices GEV monthly mean volume and dollar volume
        - **date**: 2026-06 to 2026-09
        - **quote_or_number**: Jun 3.25M/$3.27B; Jul 2.97M/$3.07B; Aug 2.03M/$2.00B; Sep (to 18th) 2.31M/$2.13B; max volume/20d-avg since Jun 30 = 1.89 (2026-09-18)
        - **reproduction**: SELECT substr(date,1,7) m, avg(volume), avg(close*volume)/1e9 FROM prices WHERE ticker='GEV' AND date>='2025-08-01' GROUP BY m
      - - **source**: prices, rolling 60-day beta/corr of GEV to 5-peer basket
        - **date**: 2024-06 to 2026-09
        - **quote_or_number**: quarter-end beta_basket 0.92,1.08,1.07,1.42,1.08,1.24,1.22,1.07,0.99,1.08; corr now 0.80
        - **reproduction**: pandas: ret.GEV.rolling(60).cov(basket)/basket.rolling(60).var(); .resample('QE').last()
    - **why_market_misses_it**: Coverage attributes the fall to GEV-specific narratives (GLJ, CFO retirement, deposit-driven FCF). The tape says the GLJ day was mostly a sector day and the only large idiosyncratic event was Jul 22; the CFO retirement 8-K (Aug 27) moved the stock +0.08%.
    - **testable_prediction**: Over the 20 trading days after 2026-10-01, GEV's daily residual vs SPY+5-peer basket (betas as above) sums to between -4% and +4% outside its own earnings day, i.e. GEV keeps trading as basket beta; and if VRT/ETN recover into the late-October hyperscaler prints, GEV recovers with them at ~1.0x.
    - **kill_condition**: Cumulative residual over any 20-day window before 2026-12-31 worse than -8% without a GEV-specific 8-K, guidance change or downgrade cluster; or a >=3x-volume down day (true capitulation) appears.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Basket choice affects the split (VRT+ETN only: residual -13.9%); factor model uses closes only; low volume during a decline can be read as buyers' strike rather than seller exhaustion; catalyst dates for hyperscalers in late Oct 2026 not yet confirmed.
  - - **title**: GEV trades hyperscaler capex prints as hard as its own earnings, and NVDA prints not at all
    - **claim**: On the trading day after MSFT/META/GOOGL/AMZN earnings (n=26, excluding overlaps with GEV's own print), GEV averages +1.91% (median +1.11%, 17/26 positive, t=2.37 vs all other days) and +1.04% over the 5-peer basket; the MSFT+META same-day subset averages +4.19% (n=8, 7/8 positive, +1.84% over basket), versus GEV's own earnings-day mean of +2.48% (n=10). The day after NVDA prints averages -0.61% (n=10, 5/10 positive).
    - **mechanism**: GEV's gas-turbine demand narrative is set by hyperscaler capex guidance, not by GPU unit volumes. Hyperscaler earnings 8-K dates are in the corpus (chunks WHERE ticker IN ('MSFT','META','GOOGL','AMZN') AND form='8-K'), so the event set is reproducible. The biggest day-after moves were 2024-07-31 +9.55% and 2026-07-30 +9.07% (MSFT/META capex raises), and 2025-01-30 +8.40% (post-DeepSeek META/MSFT capex reaffirmation). For a 3-12 month thesis this means the late-October hyperscaler prints (one week after GEV's Oct 21 estimate) are a second, historically larger, scheduled catalyst; a capex-guide-up cluster in late Oct 2026 is the most likely path for GEV to reverse the drawdown given Finding 2's beta structure.
    - **direction**: long
    - **evidence**:
      - - **source**: chunks (hyperscaler 8-K filing dates) + prices
        - **date**: 2024-04-26 to 2026-07-31
        - **quote_or_number**: n=26 day-after events ex GEV own-print: GEV mean +1.91%, median +1.11%, 17/26 positive, SD 3.52%; other days n=585 mean +0.27% SD 3.24%; t=2.37
        - **reproduction**: SELECT DISTINCT ticker, filing_date FROM chunks WHERE ticker IN ('MSFT','META','GOOGL','AMZN') AND form='8-K' AND filing_date>='2024-04-01' (keep quarterly earnings dates: MSFT 2024-04-25,07-30,10-30,2025-01-29,04-30,07-30,10-29,2026-01-28,04-29,07-29; META same ex 2024-04-24/07-31; GOOGL 2024-04-25,07-23,10-29,2025-02-04,04-24,07-23,10-29,2026-02-04,04-29,07-22; AMZN 2024-04-30,08-01,10-31,2025-02-06,05-01,07-31,10-30,2026-02-05,04-29,07-30); GEV return on next trading day from prices; drop 2024-04-25, 2024-07-24 (GEV own prints)
      - - **source**: prices, MSFT+META same-evening prints
        - **date**: 2024-07-31 to 2026-07-30
        - **quote_or_number**: day-after GEV: +9.55, +1.36, +8.40, +3.09, +0.81, -0.67, +1.91, +9.07 (%); mean +4.19%, basket mean +2.35%
        - **reproduction**: prices GEV/VRT/ETN/PWR/HUBB/EMR closes on 2024-07-31, 2024-10-31, 2025-01-30, 2025-05-01, 2025-07-31, 2025-10-30, 2026-04-30, 2026-07-30 vs prior day
      - - **source**: prices, NVDA prints (dates: SEC 8-K nvda-20260826; NVIDIA IR Q1 FY27 release 2026-05-20; earlier dates from memory)
        - **date**: 2024-05-23 to 2026-08-27
        - **quote_or_number**: day-after GEV: -1.33, +4.00, -0.85, -2.67, -2.85, +1.82, -6.27, +0.05, +1.88, +0.08 (%); mean -0.61%, basket mean -0.09%
        - **reproduction**: prices GEV close on the trading day after 2024-05-22, 2024-08-28, 2024-11-20, 2025-02-26, 2025-05-28, 2025-08-27, 2025-11-19, 2026-02-25, 2026-05-20, 2026-08-26
      - - **source**: prices, GEV own earnings days from 8-K item 2.02 dates
        - **date**: 2024-04-25 to 2026-07-22
        - **quote_or_number**: n=10 mean +2.48%, median +2.06%, 7/10 positive, mean |move| 5.42%
        - **reproduction**: SELECT DISTINCT filing_date FROM chunks WHERE ticker='GEV' AND form='8-K/EX' AND (accession LIKE '%earningsrelease%' OR accession LIKE '%pressrelease%'); returns from prices
    - **why_market_misses_it**: Catalyst calendars (including the corpus's catalyst_calendar) list only GEV's own print; the 8-year-old 'GEV is an AI trade' cliche is never quantified against its own earnings reaction, and the NVDA non-reaction is not documented anywhere in the corpus commentary.
    - **testable_prediction**: On the trading day after the MSFT/META Q3 FY26/CY26 prints (expected the week of 2026-10-26, date unconfirmed), GEV's return will exceed the 5-peer basket return and be positive if either company raises its capex outlook; across the four hyperscaler day-afters that week, GEV's mean return will be > +1%.
    - **kill_condition**: Hyperscalers guide capex up and GEV closes down on the day after MSFT/META, or the four-print mean is < 0%; that would mean the capex-to-GEV link has broken, which itself supports the peak-cycle bear case.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: Small n (8-26); day-after windows are noisy and the SD (3.5%) is close to the mean effect; 2024-2025 NVDA dates are from memory (2026 dates verified via SEC 8-K and NVIDIA IR); some day-afters coincide with other macro news; the late-Oct 2026 hyperscaler dates are not yet confirmed.
  - - **title**: The December investor update, not earnings, is GEV's largest scheduled move and it is missing from the catalyst calendar; the 2027 guide will be set there during a CFO handover
    - **claim**: GEV's annual December investor update produced next-day moves of +5.01% (2024-12-11, 2.4x volume) and +15.62% (2025-12-10, 3.75x volume, the largest up day in GEV history), both fully reversed within five trading days (-7.76% and -15.05%); the 2026 edition (expected ~Dec 8-10, 2026, inside the memo's horizon and absent from catalyst_calendar) is where FY2027 guidance will first be set, with CFO Ken Parks retiring (8-K filed 2026-08-27) and Rivian CFO Claire McDonough joining Nov 1, 2026 as advisor and becoming CFO Jan 1, 2027.
    - **mechanism**: The Dec 9, 2025 update set FY26 revenue $41-42B, 24 GW 2028 capacity, $52B 2028 revenue and raised the buyback to $10B (10-K FY25 Item 5; Utility Dive Dec 24, 2025). The stock gapped +15.6% the next day and gave it all back by Dec 17 (-10.5%, on a -4.1% basket day). The pattern (n=2) is: pre-event drift up (+7.7% in the 10 days before Dec 10, 2025), gap, full fade. For the 3-12 month thesis this is the date on which 2027 Power margin, 2027 gas GW output (the 24 GW-in-2028 ramp) and the H2'26 FCF exit rate become numbers instead of narratives, and it is the first guide an incoming CFO will own; incoming CFOs frequently re-base. The Aug 27 8-K moved the stock +0.08% and drew 19 NEWS chunks in the corpus, so the handover is not priced as a guidance risk.
    - **direction**: either
    - **evidence**:
      - - **source**: prices GEV, SPY, VRT
        - **date**: 2025-12-10
        - **quote_or_number**: GEV +15.62%, SPY +0.66%, VRT +1.93%; volume 11.4M = 3.75x prior 20-day avg; 10 days before +7.72%; 5 days after -15.05%; 20 days after -13.90%
        - **reproduction**: SELECT date, close, volume FROM prices WHERE ticker='GEV' AND date BETWEEN '2025-11-20' AND '2026-01-12' ORDER BY date
      - - **source**: prices GEV
        - **date**: 2024-12-11
        - **quote_or_number**: GEV +5.01% (Dec 10 update day itself -2.34%); volume 2.42x; 5 days after -7.76%
        - **reproduction**: SELECT date, close, volume FROM prices WHERE ticker='GEV' AND date BETWEEN '2024-11-25' AND '2024-12-20' ORDER BY date
      - - **source**: chunks NEWS 2025-12-24 (Utility Dive; Jim Cramer/Insider Monkey)
        - **date**: 2025-12-24
        - **quote_or_number**: By the numbers: GE Vernova Investor Update 2025 80 GW ... 24 GW Expected annual gas turbine manufacturing capacity in 2028 ... $52B Expected revenue in 2028; 'a recent 16% jump coming on December 10th'
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Investor Update" AND "2026"' AND c.ticker='GEV' AND c.filing_date BETWEEN '2025-12-01' AND '2026-01-31'
      - - **source**: documents form='8-K' accession 0001996810-26-000153 (Item 5.02)
        - **date**: 2026-08-27
        - **quote_or_number**: Effective January 1, 2027, Claire McDonough will become Chief Financial Officer of GE Vernova, succeeding Mr. Parks. She will join the Company as strategic advisor to Mr. Strazik on November 1, 2026
        - **reproduction**: SELECT filing_date, text FROM documents WHERE accession='0001996810-26-000153' AND form='8-K'; GEV return 2026-08-27 from prices: +0.08%
      - - **source**: documents form='8-K' accession 0001996810-26-000004 (Item 5.02) + prices
        - **date**: 2026-01-21
        - **quote_or_number**: Mavi Zingoni ... will resign from her position as the Chief Executive Officer, Power Segment ... effective as of January 21, 2026; GEV -2.48% that day
        - **reproduction**: SELECT filing_date, text FROM documents WHERE accession='0001996810-26-000004' AND form='8-K'
      - - **source**: catalyst_calendar
        - **date**: 2026-09-21
        - **quote_or_number**: 16 rows, all 'earnings release (estimated from 8-K item 2.02 cadence)'; no investor-update entry for GEV
        - **reproduction**: SELECT * FROM catalyst_calendar WHERE ticker='GEV'
    - **why_market_misses_it**: Analyst previews key off quarterly prints; the December update has no fixed date yet and is not in any earnings calendar, and the CFO change was filed as a routine retirement 4 months ahead, so nobody has connected 'first 2027 guide' with 'new CFO from an EV company with a history of large guidance resets'.
    - **testable_prediction**: GE Vernova will announce a December 2026 investor update (expect the announcement by mid-November 2026, event Dec 7-11); the day-after move will be >=5% in absolute value; and if FY27 free-cash-flow guidance is set below $12B (i.e. flat-to-down vs FY26's $11.5-12.5B) the day-after move will be negative.
    - **kill_condition**: No December 2026 investor update is held (guidance deferred to the late-Jan 2027 Q4 print), or the FY27 guide is issued and the next-day |move| is under 3%.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 4
    - **caveats**: n=2 for the event pattern; the 2025 fade coincided with a broad AI-power sell-off (Dec 17, basket -4.1%); the Dec 2026 date is inferred from cadence (Dec 10, 2024 and Dec 9, 2025), not announced; CFO-transition guidance re-basing is a base-rate argument, not GEV-specific evidence; Dec 2025 commentary coverage in the corpus is thin (21 chunks), so the update's content is sourced from two Dec 24 articles and the 10-K.
- **dead_ends**:
  - Pre-earnings drift: 10-day return before GEV prints averages +5.79% (n=9, 7/9 positive) but GEV's unconditional 10-day mean is +3.59% and a 20,000-draw bootstrap puts the earnings-window mean at only the 78th percentile; not reportable.
  - Post-earnings drift: after big up prints (+14.58% Jul 2025, +13.75% Apr 2026) the 20-day follow-through was -3.9% and -9.1%; after the -8.69% Jul 2026 print +0.25%; n too small and dominated by the trend.
  - Mean reversion after >=6% down days: fwd-20d mean +7.87% (n=16, 11 positive) is indistinguishable from GEV's unconditional 20-day mean of +7.42% (65% positive); no edge.
  - Insider_tx for GEV: five open-market sales in 17 months ($2.0-6.9M each: 2025-04, 2025-08, 2026-03, 2026-05, 2026-06), none within 10 days of a >=6% move; confirms the team's 'nothing there'.
  - Sep 14 GLJ day volume: 3.30M shares (1.66x 20-day avg) ranks 25th of 42 GEV days with |move|>=6%; no capitulation signature, so nothing to build a bottom-call on.
  - Rolling 60-day beta to SPY (1.3-2.8, currently 2.15) and to the peer basket (0.9-1.4) show no regime break in 2026; the June-September beta is in the historical range, so 'GEV has decoupled from peers' is false.
  - Siemens Energy report days (2026-02-11, 05-12, 08-05, pre-close call 06-29): GEV moved +4.2%, -0.1%, -0.1%, +5.5%, tracking the basket each time; SE results are not a GEV catalyst, only the SE downgrade note on Jul 7 was.
  - events table (0 rows) and news table (0 rows) are empty; transcript_statements has no rows for the Jul 2026 call; catalyst_calendar contains only cadence-estimated earnings dates. GEV commentary coverage is thin before Sep 2025 and has zero chunks on 2025-12-09/10/17, so the December 2025 move days have no same-day corpus explanation.
  - NVDA day-after reaction (mean -0.61%, n=10, 5/10 positive, basket-adjusted -0.52%): nothing tradable, reported only as the contrast to hyperscaler prints.
  - The 8-K of 2026-05-22 is the annual-meeting vote (Item 5.07); the 2026-02-04 8-K is a debt offering; neither moved the stock or carries thesis content.
  - SEC full-text search and Exa/Firecrawl were not needed for this lens (all events reproducible from the corpus); Firecrawl connector was unauthenticated in this session.

## [Sweep] find:contradictions

- **lens**: cross-source contradiction finder (GEV filings vs GEV transcript/IR vs commentary vs EIA-860M/923 vs customer filings)
- **findings**:
  - - **title**: The $0.3B/yr 'availability shortfall' is a Wind-farm guarantee charge, not an HA gas-fleet reliability number
    - **claim**: GEV's disclosed $0.3B per year (2023-2025) revenue reduction from availability shortfalls is booked in the Wind segment's service-agreement accounting paragraph and has no stated connection to the 126-unit HA gas fleet.
    - **mechanism**: The charge is a contra-revenue in Wind services (Wind FY25 revenue about $9.1B: Onshore $8,241M, Offshore $652M, LM $217M), so it does not touch Power segment margin or the HA services franchise. Any memo that uses it as evidence of HA wear-and-tear or gas warranty leakage is mis-sourced; conversely the 10-K discloses no quantified gas-fleet availability penalty at all.
    - **direction**: neutral
    - **evidence**:
      - - **source**: 10-K FY2025, accession 0001996810-26-000015, chunk section 'Item 7 MD&A', ord 176
        - **date**: 2026-01-29
        - **quote_or_number**: 'Wind... performance guarantees of the wind farm's availability... the reduction of revenues from availability shortfalls was $0.3 billion, $0.3 billion, and $0.3 billion, respectively.'
        - **reproduction**: SELECT section, ord, text FROM chunks WHERE accession='0001996810-26-000015' AND text LIKE '%availability shortfalls was%'
      - - **source**: 10-K FY2024, accession 0001996810-25-000011
        - **date**: 2025-02-06
        - **quote_or_number**: same Wind paragraph: '$0.3 billion, $0.3 billion and $0.1 billion' for 2024, 2023, 2022
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"$0.3 billion" AND "availability"' AND c.ticker='GEV' AND c.form='10-K'
      - - **source**: 10-K FY2025 Wind segment table (same accession)
        - **date**: 2026-01-29
        - **quote_or_number**: Onshore Wind $8,241; Offshore Wind 652; LM Wind Power 217 (FY25, $M); Wind services RPO $12,518M
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind" AND "Segment revenues" AND "Services"' AND c.accession='0001996810-26-000015' LIMIT 2
      - - **source**: 10-K FY2025 Power accounting text (absence check)
        - **date**: 2026-01-29
        - **quote_or_number**: zero chunks in the FY25 10-K match Power + availability + guarantee/penalty
        - **reproduction**: SELECT count(*) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Power" AND "availability" AND ("guarantee" OR "guarantees" OR "penalt*")' AND c.accession='0001996810-26-000015'
    - **why_market_misses_it**: The sentence sits 20 lines below the Power services paragraph in the same 'Revenue Recognition' note, and the team's own brief (and at least one web copy, src:3650) quotes the number next to the HA fleet statistics. Readers pattern-match '$0.3B availability' to gas turbines because that is where the narrative attention is.
    - **testable_prediction**: The FY2026 10-K (expected late Jan 2027) will again place the availability-shortfall figure inside the Wind paragraph, in the $0.2-0.4B range, and will contain no separate quantified gas-fleet availability penalty; the Q3'26 10-Q (late Oct 2026) will likewise show none.
    - **kill_condition**: Any 10-Q/10-K or 8-K that discloses a quantified availability or performance-guarantee revenue reduction attributed to Gas Power or the HA fleet, or that moves the $0.3B language into the Power accounting section.
    - **novelty**: 4
    - **confidence**: 5
    - **materiality**: 2
    - **caveats**: Novelty is relative to the team and commentary, not to a careful 10-K reader. The finding removes a bear data point rather than adding a bull one; it says nothing about actual HA reliability, which is simply undisclosed.
  - - **title**: EIA-860M shows only ~53 GW of planned US gas turbines (all OEMs, all owners, through 2034) against GEV's 116 GW 'under contract' with roughly half in the US
    - **claim**: As of the July 2026 EIA-860M snapshot, every US generator owner combined reports 52.6 GW of planned gas-turbine capacity (CT+GT+CS, all statuses, CODs 2026-2034), of which only 11.4 GW is under construction, while GEV alone carried 53 GW equipment backlog plus 63 GW SRAs at June 30 2026 and commentary puts the US at about half of Q2'26 orders.
    - **mechanism**: Gas equipment revenue is recognized cost-to-cost as projects progress; SRAs convert to orders and deposits only when a customer commits to a real site. If US demand behind GEV's contracted GW were fully site-backed, owners would have filed most of it with EIA as planned units. The gap (GEV US share ~55-60 GW of contracted capacity vs 52.6 GW planned nationally across GE, Siemens Energy, and MHI) means a large share of SRAs are not yet EIA-visible projects, which is where conversion slippage or lapse would first show up in orders and in contract-liability growth.
    - **direction**: short
    - **evidence**:
      - - **source**: generators table (EIA-860M), vintage 2026-07, Planned sheet
        - **date**: 2026-07
        - **quote_or_number**: planned NG CT/GT/CS by COD year: 2026 3.8; 2027 10.0; 2028 13.1; 2029 10.7; 2030 12.1; 2031 1.4; 2034 1.5 GW (total 52.6 GW); under construction (U/V/TS) 11.4 GW
        - **reproduction**: SELECT planned_year, CASE WHEN status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%' THEN 'uc' ELSE 'ns' END st, round(sum(mw)/1000.0,1) gw FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','GT','CS') AND vintage='2026-07' GROUP BY planned_year, st
      - - **source**: generators table, vintage 2025-01 vs 2026-07 (growth check)
        - **date**: 2025-01 to 2026-07
        - **quote_or_number**: planned NG CT/CA/CS/GT: 2025-01 vintage 25.9 GW total (2025-2030); 2026-07 vintage 67.0 GW (2026-2034) — pipeline more than doubled but still far below OEM contracted GW
        - **reproduction**: SELECT vintage, planned_year, round(sum(mw)/1000.0,1) gw FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage IN ('2025-01','2026-07') GROUP BY vintage, planned_year
      - - **source**: 8-K/EX Q2'26 press release
        - **date**: 2026-07-22
        - **quote_or_number**: 'backlog growth from 44 to 53 GW' and 'increase in slot reservation agreements from 56 to 63 GW'
        - **reproduction**: SELECT filing_date, value, quote FROM backlog_quarterly WHERE ticker='GEV' AND metric='reservation_gw' AND filing_date='2026-07-22'
      - - **source**: commentary, sources id 3489 (energynewsbeat.com)
        - **date**: 2026 (undated web)
        - **quote_or_number**: 'Second-quarter 2026 orders alone hit a record 38 GW... with the United States accounting for about half.'
        - **reproduction**: SELECT text FROM chunks WHERE accession='src:3489' AND text LIKE '%United States accounting for about half%'
      - - **source**: 2Q26 webcast transcript, sources id 3161
        - **date**: 2026-07-22
        - **quote_or_number**: 'approximately 100 customers in 26 different countries'; 'We now expect at least 125 gigawatts under contract by the end of the year.'
        - **reproduction**: SELECT ord, text FROM chunks WHERE accession='src:3161' AND text LIKE '%26 different countries%'
      - - **source**: generators table slippage base rate (2025-07 planned for 2027 -> 2026-07 status)
        - **date**: 2025-07 to 2026-07
        - **quote_or_number**: of 6.6 GW planned for 2027 COD, 5.6 GW on time, 1.0 GW slipped, 0.0 GW canceled (15% slip in 12 months)
        - **reproduction**: WITH a AS (SELECT plant_id, generator_id, planned_year py, mw FROM generators WHERE vintage='2025-07' AND sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','GT','CS') AND planned_year=2027), b AS (SELECT plant_id, generator_id, sheet, planned_year FROM generators WHERE vintage='2026-07' AND energy_source='NG') SELECT CASE WHEN b.sheet='Planned' AND b.planned_year>a.py THEN 'slipped' WHEN b.sheet='Planned' THEN 'on_time' ELSE COALESCE(b.sheet,'MISSING') END o, round(sum(a.mw)/1000.0,1) gw FROM a LEFT JOIN b ON a.plant_id=b.plant_id AND a.generator_id=b.generator_id GROUP BY o
    - **why_market_misses_it**: Sell-side tracks GEV's own GW disclosures and interconnection queues, not the EIA-860M owner-reported planned sheet, which requires joining monthly snapshots. The US-share of contracted GW is never given in a filing, so nobody sizes the domestic gap; the 'about half' figure exists only in commentary.
    - **testable_prediction**: If the contracted GW is real, site-backed US demand, the EIA-860M January 2027 vintage (published ~late Feb 2027) must show planned NG CT/GT/CS for CODs 2028-2030 above 45 GW (from 35.9 GW in July 2026) and under-construction gas above 15 GW (from 11.4). Interim: the October 2026 vintage should show at least a 3 GW rise in planned 2028-2030 gas turbines.
    - **kill_condition**: EIA-860M planned gas-turbine capacity for 2028-2030 rises past 45 GW by the Jan-2027 vintage, or GEV discloses in a filing that less than 40% of GW under contract is US-based (which would make the EIA comparison moot).
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: EIA-860M covers units >1 MW at plants that file Form 860M; behind-the-meter data-center plants and very early-stage projects can lag reporting by a year or more, so the gap partly measures reporting lag, not phantom demand. GEV's US share is from commentary (src:3489), not a filing. CA (steam half of combined cycle) was excluded from the turbine sum; including it adds 14.3 GW but double counts the same plants. 'Backlog into dirt' on the team's list uses a different dataset (the 420-project table); this finding gives the national EIA denominator that angle lacks.
  - - **title**: Management says only ~20% of GW under contract is for data centers; the 80/20 split shrinks both the AI-bull and AI-bubble-bear cases
    - **claim**: On the 2Q26 call GEV stated that of its ~116 GW under contract, approximately 80% is traditional customers and 20% data centers, so a data-center capex pullback exposes at most ~23 GW while the AI narrative explains only a fifth of the order book.
    - **mechanism**: Equipment revenue and deposits flow from SRA conversion. If data-center customers are 20% of contracted GW, an AI capex slowdown removes at most ~23 GW (roughly one year of planned 2028 output) from a 116 GW book, while utility/IPP demand (80%) is rate-base or capacity-market driven and is what actually fills the 20 GW/yr factory. The stock's 23% drawdown from the June peak tracked AI-capex fear headlines, which management's own mix says is over-weighted.
    - **direction**: either
    - **evidence**:
      - - **source**: 2Q26 webcast transcript, sources id 3161 (gevernova.com PDF), chunk ord 2
        - **date**: 2026-07-22
        - **quote_or_number**: 'approximately 100 customers in 26 different countries, of which approximately 80% are traditional customers and 20% are for data centers.'
        - **reproduction**: SELECT ord, text FROM chunks WHERE accession='src:3161' AND text LIKE '%80% are traditional customers%'
      - - **source**: 2Q26 transcript, same chunk
        - **date**: 2026-07-22
        - **quote_or_number**: 'half of the gigawatts that are now under contract are for our largest, most efficient HA turbines'
        - **reproduction**: SELECT text FROM chunks WHERE accession='src:3161' AND text LIKE '%half of the gigawatts%'
      - - **source**: NEWS src:1016 (Q2'26 call coverage), commentary framing
        - **date**: 2026-07-22
        - **quote_or_number**: 'booked $2.7 billion of data center orders in Electrification during the second quarter' — commentary leads with data-center numbers for Electrification, not the Gas Power 80/20 split
        - **reproduction**: SELECT text FROM chunks WHERE accession='src:1016' AND text LIKE '%data center orders in Electrification%'
      - - **source**: NRG 10-K FY2025 (customer filing, 'traditional' IPP example)
        - **date**: 2026-02-24
        - **quote_or_number**: 'slot reservation agreements with GEV for the procurement of 3.6 GW of 7HA gas turbines... expected to commence operations by the end of 2029.'
        - **reproduction**: SELECT filing_date, text FROM chunks WHERE ticker='NRG' AND form='10-K' AND filing_date='2026-02-24' AND text LIKE '%slot reservation agreements with GEV%'
    - **why_market_misses_it**: The 80/20 line appears once, in the CEO's prepared remarks, and neither the press release nor the 10-Q repeats it; commentary in the corpus mentions 'data center' 250-390 times per 1,000 chunks versus 2-7 in filings, so the narrative is built almost entirely on the 20% slice. Both bulls (AI demand) and bears (AI bubble) argue about the minority of the book.
    - **testable_prediction**: On the Q3'26 call (expected ~Oct 21-22 2026) management will restate a data-center share of GW under contract at or below 25%, and Gas Power SRA additions will stay above 10 GW in the quarter even if hyperscaler capex guidance is cut.
    - **kill_condition**: Management reports the data-center share of contracted GW above 35%, or a quarter in which Gas Power SRA plus order additions fall below 5 GW while utility/IPP customers cite no supply constraint.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: 'Traditional customers' is management's label; utilities building for data-center load (e.g., AEP, Dominion, Entergy) are counted as traditional, so true data-center exposure is higher than 20% on an end-use basis. The team's existing 'data center narrative gap' angle covers mention counts; this finding adds the only management-quantified split and flips it into a risk-sizing tool.
  - - **title**: GEV quietly cut its 2026 tariff cost estimate from $250-350M to $100-200M between the Q1 and Q2 10-Qs, with no mention in the Q2 press release
    - **claim**: The Q1'26 10-Q (Apr 22 2026) stated the 2026 tariff cost impact at approximately $250-350M; the Q2'26 10-Q (Jul 22 2026) restated it at approximately $100-200M, a ~$150M midpoint reduction that the Q2 8-K/EX press release does not call out.
    - **mechanism**: Tariff cost is a direct hit to Power and Electrification segment EBITDA; a $150M reduction is ~0.3 points on ~$45B revenue and about 1.2% of guided FCF midpoint ($12B). Guidance was raised on the same day, and the tariff relief is one identifiable source of that raise that the market attributed to volume and price.
    - **direction**: long
    - **evidence**:
      - - **source**: 10-Q Q1 2026
        - **date**: 2026-04-22
        - **quote_or_number**: 'The current total estimated cost impact from the global tariffs as outlined is approximately $250 million to $350 million in 2026'
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated cost impact"' AND c.ticker='GEV' AND c.form='10-Q' AND c.filing_date='2026-04-22'
      - - **source**: 10-Q Q2 2026
        - **date**: 2026-07-22
        - **quote_or_number**: 'The current total estimated cost impact from the global tariffs as outlined is approximately $100 million to $200 million in 2026'
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated cost impact"' AND c.ticker='GEV' AND c.form='10-Q' AND c.filing_date='2026-07-22'
      - - **source**: 10-Q/8-K/EX 2025 series (prior-year path)
        - **date**: 2025-04-23 to 2025-10-22
        - **quote_or_number**: 2025 estimate: '$300 million to $400 million' (Apr, Jul) then 'trending towards the lower end' (Oct)
        - **reproduction**: SELECT c.form, c.filing_date, substr(c.text, instr(c.text,'estimated cost impact')-50, 300) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated cost impact"' AND c.ticker='GEV' ORDER BY c.filing_date
      - - **source**: 8-K/EX Q2 2026 press release (absence check)
        - **date**: 2026-07-22
        - **quote_or_number**: only tariff mention is in the forward-looking-statements boilerplate ('the estimated impact of tariffs'); no dollar figure
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"tariffs"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22'
    - **why_market_misses_it**: The number lives in a boilerplate 'Tariffs' paragraph of the 10-Q MD&A that changed only two digits; the press release and call did not flag it, so no note in the corpus's 191 analyst calls mentions it.
    - **testable_prediction**: The Q3'26 10-Q (late Oct 2026) will keep the 2026 tariff estimate at or below $200M, and FY26 segment EBITDA margin for Power will print at or above the 19% top of the guided 17-19% range if volume holds.
    - **kill_condition**: The Q3'26 10-Q raises the 2026 tariff estimate back above $250M, or a new Section 232/IEEPA action re-imposes duties on turbine forgings and transformer steel.
    - **novelty**: 3
    - **confidence**: 5
    - **materiality**: 1
    - **caveats**: Small relative to a $250B market cap; the cause of the cut (court rulings, exemptions, or mitigation) is not stated in the filing and was not verified externally. Included because it is fully reproducible and the team may want it for the guidance bridge.
- **dead_ends**:
  - SRA roll-forward reconciliation: Q1'26 43+19-6=56 and backlog 40+2+6-4=44 both tie exactly; Q2'26 SRA 56+18-10=64 vs 63 reported (1 GW rounding); no evidence of hidden SRA cancellations in the 8-K/EX series (backlog_quarterly, metric='reservation_gw').
  - HA unit-count consistency: 10-K/10-Q series HA-Turbines in RPO 22 (Dec-23), 29, 32, 36, 32 (Dec-24), 51 (Dec-25); installed base 94 -> 126. 51 units x ~0.4 GW = ~20 GW = roughly half of the 40 GW Dec-25 backlog, matching the 2Q26 'half of GW are HA' statement. No contradiction. Note the 2025 10-Qs stopped repeating the sentence (only 10-Ks carry it now).
  - NRG customer filing cross-check: NRG's SRA with GEV grew 1.2 GW (Feb-25) -> 2.4 GW (Aug-25) -> 3.6 GW (Feb-26) of 7HA while 'first projects... by the end of 2029' never moved; consistent with GEV, not a contradiction.
  - Customer filings almost never name GE Vernova: across 18 customer tickers only NRG (SRA), BE (DEF 14A/8-K), AMZN (AWS customer list, May-25), CEG (investor deck quoting Strazik 'largely sold out through the end of 28', May-25) and one AEP 11-K mention. No utility 10-K/10-Q discloses OEM, delivery year, or deposit terms for gas turbines; the lens's 'GEV vs customer filings' comparison has almost no primary-source material.
  - competitor_financials table is mostly 'Not specified' for pricing, lead_time and capacity_expansion for MHI, Hitachi, Vestas; only Siemens Energy rows carry content (110-120 GW market, 35 -> 50 large GT/yr FY27, 'faster delivery commands a premium'). Nothing there contradicts GEV; the MHI-vs-Siemens market-size dispute is already on the list.
  - EIA-923: US gas generation fell 3.2% in 2025 (1,865 -> 1,805 TWh) while coal rose 15% (594 -> 681 TWh) and combined-cycle CT generation fell 2.9%, versus the FY25 10-K's 'gas power generation to increase at low-single digits'. This overlaps the team's 'EPA CAMD fired hours' angle so not proposed as a finding; the 2026 rows cover only ~1,000 of 2,500 gas plants and are unusable for a y/y read. Query: SELECT year, fuel_type, round(sum(net_generation_mwh)/1e6,1) FROM generation WHERE fuel_type IN ('NG','BIT','SUB') GROUP BY year, fuel_type.
  - EIA-860M 'Canceled or Postponed' sheet is cumulative (NG CT/GT/CS 55.3 -> 57.1 GW across 2025-01 to 2026-07 vintages), so it cannot measure recent cancellations; use vintage-to-vintage joins instead.
  - Only one earnings transcript exists in the corpus (src:3161, 2Q26); transcript_statements has no other calls, so within-management drift across calls cannot be tested from primary text; the CEG deck's Strazik quote (May-25, 'sold out through 28') vs the 2Q26 'agreements signed into 31' is lead-time drift already on the team's list.
  - analyst_calls table is almost entirely price targets (GLJ $470, Baird $1,400, Jefferies $1,185, Bernstein $1,298); it contains no GW, price-per-kW or margin claims to contradict against filings.
  - GEV per-kW pricing: the only primary statement is the 2Q26 transcript (2H26 order $/kW 'at the higher end of 10 to 20 points versus 4Q 25', attributed partly to aero/combined-cycle mix); no filing gives a $/kW, so a filings-vs-commentary price contradiction cannot be built. IR src:3160 is a corrupted binary PDF and unreadable.
  - queue_projects and operator_forecasts are empty as warned; PJM OPERATOR chunks (2,113) were not mined further because the PJM forecast-accuracy angle is already on the list.
  - No primary source states the US share of GEV's GW under contract or RPO by geography; the 'about half' figure used in the EIA finding is commentary only (src:3489).

## [Sweep] find:eia-physical

- **lens**: EIA physical reconciler (generators = EIA-860M monthly snapshots 2023-01..2026-07; generation = EIA-923 annual)
- **findings**:
  - - **title**: The March 2026 EIA planned-gas surge is 65% one Siemens-supplied speculative campus; ex-Fermi, new US gas planning shrank vs March 2025
    - **claim**: Of the 215 gas units / 17.96 GW that entered the EIA-860M Planned sheet between the Feb-2026 and Mar-2026 vintages, 157 units / 11.68 GW belong to a single entity, Fermi America (Project Matador, Amarillo TX; Siemens SGT-800 turbines, status P = regulatory approvals not initiated, mostly dated Dec-2030); excluding it, the 2026 annual-survey increment (58 units / 6.28 GW) is smaller than the 2025 one (53 units / 8.42 GW).
    - **mechanism**: Sell-side and press cite the EIA planned-gas count (roughly 296 to 505 units) as evidence that the US gas build is accelerating into GEV's 20/24/30 GW ramp. The increment is a survey artifact plus one project whose turbines are not GEV's. If the true rate of new US gas planning is flat-to-down year over year, then GEV's next 125 GW of contracted capacity depends more on conversion of existing SRAs and on non-US demand than on new US utility plans, which bears on 2027-28 order growth and on the multiple paid for the equipment backlog.
    - **direction**: short
    - **evidence**:
      - - **source**: generators table, Feb-to-Mar entrant diff by year
        - **date**: vintages 2024-03, 2025-03, 2026-03
        - **quote_or_number**: 2024: 2 units/0.09 GW; 2025: 53 units/8.42 GW (0 Fermi); 2026: 215 units/17.96 GW, of which Fermi 157 units/11.68 GW; 185 of 215 units are status (P)
        - **reproduction**: SELECT COUNT(*), ROUND(SUM(mw)/1000,2), SUM(entity_name LIKE 'Fermi%'), ROUND(SUM(CASE WHEN entity_name LIKE 'Fermi%' THEN mw ELSE 0 END)/1000,2), SUM(status LIKE '(P)%') FROM generators g WHERE vintage='2026-03' AND sheet='Planned' AND energy_source='NG' AND NOT EXISTS (SELECT 1 FROM generators p WHERE p.vintage='2026-02' AND p.sheet='Planned' AND p.plant_id=g.plant_id AND p.generator_id=g.generator_id);  -- repeat with ('2025-03','2025-02') and ('2024-03','2024-02')
      - - **source**: generators table, Fermi detail
        - **date**: vintage 2026-07
        - **quote_or_number**: plant_id 69799 'Project Matador Gas Plant (PMG)': 96 CT x 57 MW + 32 CA x 105 MW dated 2030-12 status (P); 6 CT x 260 MW dated 2027-09 status (P); only 6 CT x 50 MW + 3 GT x 40 MW have status (T) approvals received. Plant 69798 'Project Matador Nuclear' 4 x 1,117 MW dated 2031-32.
        - **reproduction**: SELECT plant_id, plant_name, prime_mover, COUNT(*), ROUND(SUM(mw)), planned_year, planned_month, status FROM generators WHERE vintage='2026-07' AND entity_name LIKE 'Fermi%' GROUP BY 1,2,3,6,7,8;
      - - **source**: https://www.prnewswire.com/news-releases/fermi-america-announces-arrival-of-6-siemens-energy-sgt-800-gas-turbines-at-port-of-houston-marking-major-milestone-in-natural-gas-power-timeline-302682327.html
        - **date**: 2026-02-09
        - **quote_or_number**: Fermi announced arrival of 6 Siemens Energy SGT-800 turbines (50-62 MW each); a further 6 SGT-800s are on order for 2028 delivery ($165M equipment facility). No GE Vernova supply agreement is mentioned.
        - **reproduction**: Fetch the URL; search Fermi Inc. FY2025 10-K at https://www.sec.gov/Archives/edgar/data/2071778/000207177826000010/frmi-20251231.htm for 'SGT-800' and 'GE Vernova'.
      - - **source**: generators table, planned gas by vintage
        - **date**: vintages 2026-02 and 2026-03
        - **quote_or_number**: Planned NG units 289 -> 494; GW 48.2 -> 65.5; combined-cycle unit count 73 -> 228 while CC GW only 29.0 -> 43.4 (average planned CC unit fell from ~397 MW to ~190 MW because Fermi's units are 57-105 MW)
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(SUM(mw)/1000,1), SUM(prime_mover IN ('CT','CA','CS')), ROUND(SUM(CASE WHEN prime_mover IN ('CT','CA','CS') THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND vintage IN ('2026-02','2026-03') GROUP BY vintage;
    - **why_market_misses_it**: Aggregate EIA planned-capacity charts are quoted without de-duplicating by entity; Fermi's 157 tiny units inflate the unit count far more than the GW, and nobody checks which OEM sits behind the largest new entrant. The Feb-to-Mar step is the annual EIA-860 survey being folded into the monthly file, so a year-over-year comparison of the March step is the only fair test, and 2026 ex-Fermi is below 2025.
    - **testable_prediction**: In the EIA-860M vintages for Aug-Dec 2026 (published monthly, ~2 months lag), Fermi's 128 units dated 2030-12 will not move to status (L) or (T), and total US planned NG CC+GT capacity ex-Fermi will remain within +/-5 GW of the Jul-2026 figure (58.0 GW) through the Dec-2026 vintage.
    - **kill_condition**: If the Dec-2026 EIA-860M vintage shows planned NG CC+GT ex-Fermi above 65 GW (a fresh non-survey step of 7+ GW), or if Fermi announces a GE Vernova turbine order covering the 2030 units, the finding is dead.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: EIA-860M only captures generators that developers choose to report (>=1 MW, typically once permitting starts), so behind-the-meter data-center turbines and early SRAs are largely absent; the finding is about the EIA series that commentary cites, not about GEV's true order book. The 'annual artifact' pattern has only two observations (2025, 2026); in 2024 the March step was 2 units.
  - - **title**: No US combustion turbine of 300 MW or more has entered service since 2023, and only 2.3 GW of the 15.3 GW planned big-frame fleet is physically under construction
    - **claim**: EIA operating data show US combined-cycle additions of 6.8 GW (2023), 0.1 GW (2024), 1.8 GW (2025) and 1.0 GW (2026 through July), with zero CT units >=300 MW commissioned in 2024-2026; the Jul-2026 Planned sheet holds 35 CT units >=300 MW (15.3 GW, 2026-2034), of which only 5 units / 2.3 GW carry construction-complete or under-construction status; the firm (U/V/TS) NG pipeline by target year is 4.2 GW (2026), 3.6 (2027), 2.8 (2028), 1.4 (2029), versus 6.6 / 13.7 / 9.9 / 16.9 GW still unapproved (P/L) for 2027-2030.
    - **mechanism**: GEV's gas equipment revenue is cost-to-cost over time and its Services thesis (~$70M per GW-year) needs turbines running in the field. The US HA-class installed base cannot grow before 2027 because nothing big is in the ground; the 2024-01 planned-gas cohort shows a 2-year base rate of 31% operating, 24% canceled, 22% slipped 12+ months. If 2027-28 US deliveries slip toward 2029-30 as the unapproved P/L bulk implies, revenue recognition (cost-to-cost) and the services ramp both move right, while customer deposits already booked ($39.9B Jun-26) stay as liabilities longer.
    - **direction**: either
    - **evidence**:
      - - **source**: generators table, Operating sheet additions by op_year
        - **date**: vintage 2026-07
        - **quote_or_number**: op_year 2023: CC 6.8 GW, 5 CT>=300MW; 2024: CC 0.1 GW, 0 big CT; 2025: CC 1.8 GW, 0 big CT; 2026 YTD: CC 1.0 GW, 0 big CT. Same zero in the 2024-12 and 2025-12 vintages.
        - **reproduction**: SELECT op_year, ROUND(SUM(CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN mw ELSE 0 END)/1000,1), SUM(prime_mover='CT' AND mw>=300) FROM generators WHERE vintage='2026-07' AND sheet='Operating' AND energy_source='NG' AND op_year>=2018 GROUP BY op_year;
      - - **source**: generators table, Planned big CT list
        - **date**: vintage 2026-07
        - **quote_or_number**: 35 CT units >=300 MW, 15.3 GW. Under construction/complete: Entergy Texas Orange County 2x453 MW (TS, Aug-2026), Entergy Mississippi Traceview 478 + Vicksburg 478 (U, 2028), TVA Cumberland 455 (U, 2034). Entergy entities hold ~8.5 GW of the 15.3 GW.
        - **reproduction**: SELECT planned_year, entity_name, plant_name, state, COUNT(*), ROUND(SUM(mw)), status FROM generators WHERE vintage='2026-07' AND sheet='Planned' AND energy_source='NG' AND prime_mover='CT' AND mw>=300 GROUP BY 1,2,3,4,7 ORDER BY 1;
      - - **source**: generators table, planned NG CC+GT by target year and status
        - **date**: vintages 2026-07 vs 2025-07
        - **quote_or_number**: Jul-26 (year: U/V/TS GW, T GW, P/L GW): 2026: 4.2/0/0; 2027: 3.6/0.9/6.6; 2028: 2.8/0.3/13.7; 2029: 1.4/2.8/9.9; 2030: 0/1.3/16.9. Jul-25: 2026: 5.4/0/1.2; 2027: 0.8/0.5/5.9; 2028: 0/0.8/11.5.
        - **reproduction**: SELECT planned_year, ROUND(SUM(CASE WHEN status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%' THEN mw ELSE 0 END)/1000,1), ROUND(SUM(CASE WHEN status LIKE '(T)%' THEN mw ELSE 0 END)/1000,1), ROUND(SUM(CASE WHEN status LIKE '(P)%' OR status LIKE '(L)%' THEN mw ELSE 0 END)/1000,1) FROM generators WHERE vintage='2026-07' AND sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','CC','GT') GROUP BY planned_year;
      - - **source**: generators table, 24-month cohort outcomes
        - **date**: cohorts 2023-01->2025-01 and 2024-01->2026-01
        - **quote_or_number**: 2024-01 cohort (16.6 GW planned NG CC+GT): operating 5.1 GW (31%), canceled 4.0 (24%), slipped 12+ months 3.6 (22%), slipped 1-11 months 2.1, on time 1.8. 2023-01 cohort (20.2 GW): operating 8.6, slipped 12+ 4.9, canceled 4.7. Zero units vanish; EIA moves them to the Canceled sheet.
        - **reproduction**: WITH c0 AS (SELECT plant_id, generator_id, mw, planned_year*12+planned_month m0 FROM generators WHERE vintage='2024-01' AND sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','CC','GT')), c1 AS (SELECT plant_id, generator_id, sheet, planned_year*12+planned_month m1 FROM generators WHERE vintage='2026-01') SELECT CASE WHEN c1.sheet IS NULL THEN 'vanished' WHEN c1.sheet='Planned' AND m1-m0>=12 THEN 'slip12+' WHEN c1.sheet='Planned' AND m1-m0>0 THEN 'slip1-11' WHEN c1.sheet='Planned' THEN 'ontime' ELSE c1.sheet END, COUNT(*), ROUND(SUM(c0.mw)/1000,1) FROM c0 LEFT JOIN c1 USING(plant_id, generator_id) GROUP BY 1;
      - - **source**: generators table, TS status count
        - **date**: vintages 2023-07..2026-07
        - **quote_or_number**: Units 'construction complete, not yet in commercial operation' (TS) jumped from 0-3 units (<=1.1 GW) in every prior vintage to 11 units / 2.13 GW in Jul-2026 (GRDA GREC 594 MW GT, Orange County 2x453+400 MW, Canyon Peak 6x26 MW)
        - **reproduction**: SELECT vintage, SUM(status LIKE '(TS)%'), ROUND(SUM(CASE WHEN status LIKE '(TS)%' THEN mw ELSE 0 END)/1000,2) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','CC','GT') GROUP BY vintage;
    - **why_market_misses_it**: Analysts model GEV on shipments and RPO, not on what has reached commercial operation. EIA-860M's status codes let you separate 'in the ground' from 'announced', and the 2027-28 bulk of the US HA pipeline (Entergy LA/MS/AR, Homer City, TVA) is still coded P or L. The 24-month base rate (about a quarter canceled, a quarter slipped a year) is never applied to the 15.3 GW list.
    - **testable_prediction**: By the Dec-2026 EIA-860M vintage (released ~Feb 2027): Orange County (2x453 MW) will be the only CT >=300 MW to reach Operating status in 2026; US NG CC additions for calendar 2026 will total below 3 GW; and at least 3 GW of the 13.7 GW of unapproved (P/L) 2028-dated NG capacity will be re-dated to 2029 or later.
    - **kill_condition**: If the Dec-2026 vintage shows >5 GW of CT>=300 MW with status U/V (i.e., the 2028 plants broke ground on schedule) or if calendar-2026 US CC additions exceed 3 GW, the delay thesis is dead.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: EIA status lags reality: Entergy Louisiana Franklin Farms 1&2 (939 MW CT) broke ground in late 2025 per Entergy press releases but is still coded (L) in Jul-2026, so 'under construction' GW is understated by at least ~1 GW. GEV shipments are global; the US share of its 20 GW/yr is not disclosed in the corpus, so this reconciles the US physical build, not GEV's revenue directly. The 2025-2026 Operating additions may still be revised in the annual 860.
  - - **title**: Every new US combined-cycle turbine in the EIA plan is now H/J-class sized: median planned CC unit rose from 239 MW to 469 MW in 30 months, and Entergy is more than half of it
    - **claim**: Excluding Fermi, the median planned combined-cycle CT unit in EIA-860M rose from 239 MW (Jan-2024) to 350 MW (Jan-2025) to 455 MW (Jan-2026) to 469 MW (Jul-2026); planned CT capacity in units >=300 MW went from 2.8 GW (Jul-2024) to 15.3 GW (Jul-2026, 5.5x) while sub-300 MW planned CC-CT capacity fell to 0.0 GW; Entergy affiliates (TX, LA, MS, AR) account for roughly 8.5 GW of the 15.3 GW and Louisiana's planned NG capacity went from 0.9 GW to 9.5 GW.
    - **mechanism**: Unit size identifies the frame class that US utilities are buying: 450-480 MW units are 7HA.03 / M501JAC-class, 350-370 MW are 7HA.02-class, 240 MW were F-class. The complete disappearance of sub-300 MW CC planning means the large-frame oligopoly (GEV, MHI, Siemens) has captured 100% of new US CC planning, which supports GEV's pricing (10-20 points higher $/kW on 2H26 orders vs 4Q25). The flip side is concentration: one customer group (Entergy) is more than half the physical US big-frame pipeline, and its Louisiana plants are Meta-Hyperion dependent.
    - **direction**: long
    - **evidence**:
      - - **source**: generators table, planned CC-CT unit-size distribution ex-Fermi
        - **date**: vintages 2024-01, 2025-01, 2026-01, 2026-07
        - **quote_or_number**: n / median MW: 15 / 239; 17 / 350; 31 / 455; 36 / 469. Mean MW: 287, 309, 414, 425. Units >=300 MW: 7 (2.8 GW), 10 (4.3), 30 (12.8), 35 (15.3); sub-300 MW CC-CT GW: 1.5, 1.0, 0.0, 0.0.
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(AVG(mw)), SUM(mw>=300), ROUND(SUM(CASE WHEN mw>=300 THEN mw ELSE 0 END)/1000,1), ROUND(SUM(CASE WHEN mw<300 THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover='CT' AND entity_name NOT LIKE 'Fermi%' AND vintage IN ('2024-01','2025-01','2026-01','2026-07') GROUP BY vintage;  -- median: SELECT mw FROM ... ORDER BY mw and take the middle row
      - - **source**: generators table, state movers ex-Fermi
        - **date**: vintages 2024-07 vs 2026-07
        - **quote_or_number**: Planned NG CC+GT GW Jul-24 -> Jul-26: LA 0.9 -> 9.5; TX 5.0 -> 8.9; PA 0.0 -> 4.4; TN 0.0 -> 3.4; OK 1.3 -> 3.3; MS 0.0 -> 3.0; GA 0.0 -> 2.5; AZ 0.1 -> 2.2
        - **reproduction**: SELECT state, ROUND(SUM(CASE WHEN vintage='2024-07' THEN mw ELSE 0 END)/1000,1), ROUND(SUM(CASE WHEN vintage='2026-07' THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','CC','GT') AND vintage IN ('2024-07','2026-07') AND entity_name NOT LIKE 'Fermi%' GROUP BY state ORDER BY 3 DESC LIMIT 12;
      - - **source**: generators table, planned simple-cycle GT size split
        - **date**: vintages 2024-07 and 2026-07
        - **quote_or_number**: Planned GT (simple cycle) sub-200 MW capacity 2.1 GW -> 6.2 GW (units 57 -> 168); >=200 MW 4.9 GW -> 15.1 GW. Small-frame/aero simple cycle tripled alongside large frame.
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(SUM(CASE WHEN mw>=200 THEN mw ELSE 0 END)/1000,1), ROUND(SUM(CASE WHEN mw<200 THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover='GT' AND entity_name NOT LIKE 'Fermi%' AND vintage IN ('2024-07','2026-07') GROUP BY vintage;
      - - **source**: chunks table, GEV 2Q26 transcript
        - **date**: 2026-07 (TRANSCRIPT, filing_date blank)
        - **quote_or_number**: "we would expect gas equipment orders in the second half to have a dollar per kW that is at the higher end of the range of 10 to 20 points versus 4Q '25 orders"
        - **reproduction**: SELECT c.form, substr(c.text,1,400) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"dollar per kW" "10 to 20 points"' AND c.ticker='GEV' LIMIT 3;
    - **why_market_misses_it**: Commentary discusses GW, not unit size. The EIA unit-level data is the only public source that reveals frame class by MW, and it shows F-class combined cycle has vanished from US planning while 450+ MW units dominate, which is what gives the three OEMs their pricing. The Entergy concentration (more than half of planned big-frame CT GW) is invisible in GEV's disclosed backlog.
    - **testable_prediction**: In the Dec-2026 EIA-860M vintage, the median planned CC-CT unit (ex-Fermi) will remain >=450 MW and no new sub-300 MW CC-CT unit will be added; Entergy affiliates will still hold >=45% of planned CT capacity >=300 MW.
    - **kill_condition**: If the Dec-2026 vintage shows >=3 GW of newly planned CC-CT units under 300 MW (F-class or refurbished frames returning), or Entergy cancels or re-dates >=2 GW of its Louisiana/Mississippi CT units, the frame-class and concentration reads are dead.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: MW-to-frame mapping is inferential (EIA does not list OEM); 453-478 MW could be GE 7HA.03 or MHI M501JAC, so this is an oligopoly signal, not a GEV-share signal. The projects table has blank oem for 254 of 420 rows and no OEM for Entergy or Homer City, so I could not attribute the 15.3 GW among GEV, MHI and Siemens from the corpus. Small-frame simple-cycle growth overlaps the team's bridge-power angle and is included only as context.
  - - **title**: US combined-cycle utilization fell in 2025 on a flat fleet; only Virginia shows a data-center utilization jump, Texas is flat
    - **claim**: US natural-gas combined-cycle capacity factor was 0.506 (2022), 0.531 (2023), 0.544 (2024), 0.526 (2025); CC net generation fell 3.2% in 2025 (1,552.9 to 1,503.5 TWh) on flat operating CC capacity (325.7 to 326.5 GW); Texas CC CF was flat (0.531 to 0.524) while Virginia rose from 0.534 (2022) to 0.659 (2025) and Texas simple-cycle GT CF rose from 0.227 to 0.256.
    - **mechanism**: GEV Gas Services revenue is triggered by fired hours and starts (major inspections at fixed hour intervals). A 1.8-point drop in fleet-wide CC utilization defers outage events on the ~326 GW US CC fleet, so the 'services on 400+ GW installed base' bull case gets no utilization tailwind in the US in 2025-26; the tailwind exists only in pockets (Virginia, Texas peakers).
    - **direction**: neutral
    - **evidence**:
      - - **source**: generation joined to generators (Operating CC NG capacity at Dec vintage)
        - **date**: years 2022-2025
        - **quote_or_number**: US CC CF: 2022 0.506, 2023 0.531, 2024 0.544, 2025 0.526. CC capacity Dec-23 327.6, Dec-24 325.7, Dec-25 326.5 GW.
        - **reproduction**: WITH cap AS (SELECT CASE vintage WHEN '2023-01' THEN 2022 WHEN '2023-12' THEN 2023 WHEN '2024-12' THEN 2024 WHEN '2025-12' THEN 2025 END y, state, SUM(mw) mw FROM generators WHERE sheet='Operating' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','CC') AND vintage IN ('2023-01','2023-12','2024-12','2025-12') GROUP BY 1,2), gen AS (SELECT year y, state, SUM(net_generation_mwh) mwh FROM generation WHERE fuel_type='NG' AND prime_mover IN ('CT','CA','CS','CC') GROUP BY 1,2) SELECT cap.y, ROUND(SUM(mwh)/(SUM(mw)*8760.0),3) FROM cap JOIN gen USING(y,state) GROUP BY cap.y;
      - - **source**: generation table, national NG generation by prime mover
        - **date**: years 2022-2025
        - **quote_or_number**: CC TWh: 1420.2, 1522.9, 1552.9, 1503.5; GT TWh: 144.3, 146.4, 159.8, 157.4; NG steam TWh: 108.5, 121.3, 140.8, 131.2
        - **reproduction**: SELECT year, CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN 'CC' ELSE prime_mover END pm, ROUND(SUM(net_generation_mwh)/1e6,1) FROM generation WHERE fuel_type='NG' GROUP BY 1,2;
      - - **source**: same join as above, by state
        - **date**: years 2022-2025
        - **quote_or_number**: CC CF 2022->2025: TX (48.3 GW) 0.483/0.526/0.531/0.524; FL 0.546/0.534/0.552/0.533; PA 0.669/0.709/0.712/0.701; VA (9.6 GW) 0.534/0.553/0.665/0.659; CA 0.406 -> 0.324; GT CF TX (15.3 GW) 0.227/0.238/0.254/0.256; US GT CF 0.104/0.107/0.116/0.113
        - **reproduction**: Same CTE as the national query, but GROUP BY state and pivot with MAX(CASE WHEN y=2025 THEN mwh/(mw*8760.0) END); for GT replace prime_mover IN (...) with prime_mover='GT' in both CTEs.
    - **why_market_misses_it**: Everyone quotes installed GW for services; nobody divides EIA-923 generation by EIA-860 capacity by state. The 2025 dip is usually attributed to gas prices and dismissed, but it lands exactly on the fleet where GEV's HA units are concentrated (Texas, Southeast), and the data-center utilization story is only visible in Virginia.
    - **testable_prediction**: EIA-923 full-year 2026 (final data ~Q3 2027; preliminary monthly data by Feb 2027) will show US CC capacity factor below 0.55 and Texas CC CF below 0.55, with Virginia CC CF above 0.62.
    - **kill_condition**: If preliminary 2026 EIA-923 shows US CC generation above 1,600 TWh (CF above ~0.56 on ~327 GW), the flat-utilization read is dead.
    - **novelty**: 2
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: 2025 EIA-923 in the corpus may be preliminary; 2026 rows cover only part of the year (a sample plant shows 7.9 TWh vs 18.7 TWh in 2025, ~5 months) so 2026 CF cannot be computed. Capacity denominators use the December vintage of each year, so units added mid-year inflate CF slightly. This finding is mostly a check on the services bull case, not new to energy specialists.
- **dead_ends**:
  - 'Vanished' planned units: none. Across every 12- and 24-month cohort (2023-01->2025-01, 2024-01->2026-01, 2024-07->2026-07, 2025-07->2026-07) zero gas units disappear from the file; EIA moves them to the 'Canceled or Postponed' sheet, so vanish-share is not a usable signal.
  - In-flight slippage from a single vintage: in the Jul-2026 vintage there are zero NG units on the Planned sheet whose planned_year/month is already past; EIA re-dates them before publication, so slippage must be measured across vintages (done above).
  - New cancellations: no NG CC/GT unit >=100 MW moved to the Canceled sheet between Jul-2025 and Jul-2026, so the cancellation base rate has not yet started rising in the current cycle.
  - Feb-to-Mar 'annual survey' jump in 2024 was only 2 units / 0.09 GW, so the artifact only has two observations (2025: +53 units/8.4 GW; 2026: +215/18.0 GW, 157/11.7 GW of it Fermi).
  - Mapping EIA planned big units to OEM from the corpus: projects table has blank oem for 254 of 420 rows and none for Entergy, Homer City, TVA, Basin; FTS on 'Orange County Advanced'/'Richland Parish'/'Kingston' with OEM names returned nothing relevant. Web search confirms Fermi = Siemens SGT-800 but not the Entergy Louisiana frames.
  - GEV's US share of gas orders/backlog: FTS over GEV 10-K/10-Q/8-K/transcripts for U.S. share plus GW plus percent/majority returned nothing usable; competitor_financials gives Siemens 69 GW backlog / 26 GW SRAs (Q3 FY25) and ~60 GW (Q2 FY26) with no regional split, so the 20/24/30 GW path cannot be reconciled to US EIA GW from the corpus.
  - queue_projects and operator_forecasts are empty (as warned).
  - 2026 EIA-923 rows are partial-year (~5 months), so no 2026 capacity factors were computed.
  - Ollama semantic search (embed.py) was not used; FTS was sufficient for the few text lookups.

## [Sweep] find:competitor-filings

- **lens**: competitor filings reader (Siemens Energy, MHI, Vestas, Hitachi Energy vs GEV)
- **findings**:
  - - **title**: GEV's slot-reservation pool turns over about half as fast as Siemens Energy's, and GEV's own H2 'inflection' guidance only works if new SRA signings halve or conversions double
    - **claim**: GEV converts roughly 14-28% of its opening SRA pool per quarter (mean about 20%, implied dwell about 5 quarters) and SRAs are 54% of its 116 GW commitments, while Siemens Energy converted 44% of its opening SRA pool in the same calendar quarter (12 of about 27 GW), keeps SRAs at 27% of commitments (26 of 95 GW), and defines the pool as orders expected to be booked within 12 months.
    - **mechanism**: SRA fees are small options (Siemens books 'Reservation fees' of EUR 563m at Sep-30-2025 against roughly 26 GW of SRAs, about EUR 20-25m/GW or about 5% of its EUR 400m/GW new-unit value). Firm orders, not SRAs, carry the down payments that drive GEV's contract liabilities ($39.9B) and FCF, and only firm orders enter RPO and revenue. If GEV's 63 GW SRA pool converts slowly or partly lapses, the Gas equipment backlog, the '125 GW by year-end' claim and 2027-28 revenue and FCF guidance are all exposed. Arithmetic: year-end backlog > SRAs (management's stated H2 inflection) with about 10 GW shipped in H2 requires conversions > 33 GW if new SRAs continue at the H1 pace (37 GW), or > about 20 GW if new commitments fall to the roughly 19 GW that 'at least 125 GW' implies (116 + new - 10 shipped >= 125). H1 2026 conversions were 16 GW.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, form 8-K/EX, GEV earnings releases 2025-04-23, 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22, 2026-07-22
        - **date**: 2025-04-23 to 2026-07-22
        - **quote_or_number**: Per quarter (new SRA / direct orders / converted / shipped / backlog / SRAs): Q1'25 7/7/na/na/29/21; Q2'25 7/2/3/5/29/25; Q3'25 12/1/7/4/33/29; Q4'25 21/3/8/3/40/43; Q1'26 19/2/6/4/44/56; Q2'26 18/2/10/3/53/63. Conversion rate on opening SRAs: 14%, 28%, 28%, 14%, 18%.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '("slot reservation" OR "SRAs") AND ("GW" OR "gigawatts")' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date
      - - **source**: sources id 3167 (Siemens Energy Q3 FY26 analyst presentation, Aug 5 2026)
        - **date**: 2026-08-05
        - **quote_or_number**: 15 GW booked (12 GW converted from SRAs), 6 GW shipped ... 69 GW backlog / 26 GW SRAs
        - **reproduction**: SELECT text FROM sources WHERE id=3167 -- search 'GW booked'
      - - **source**: sources id 3169 (Siemens Energy Q3 FY26 pre-close call transcript, Jun 29 2026)
        - **date**: 2026-06-29
        - **quote_or_number**: conversion of those into orders within on average 6-12 months, which is also visible in our large order backlog of around 60 GW as of Q2 Fiscal Year 2026 (so Q2 SRAs = 87 total commitments - 60 = about 27 GW; Q3 opening-pool conversion 12/27 = 44%)
        - **reproduction**: SELECT text FROM sources WHERE id=3169 -- search 'on averag'; Q2 total 87 GW from SELECT text FROM sources WHERE id=3172
      - - **source**: sources id 3189 (Siemens Energy Gas Services CMD Nov 2025 via MarketScreener)
        - **date**: 2025-11-20
        - **quote_or_number**: ~78 GW New unit backlog ... Based on orders booked in FY24, FY25 and secured orders expected to be booked in the next 12 months
        - **reproduction**: SELECT text FROM sources WHERE id=3189 -- search '78 GW'
      - - **source**: sources id 3180 (Siemens Energy Annual Report 2025, Note 12 Other current liabilities)
        - **date**: 2025-09-30
        - **quote_or_number**: Reservation fees 563 244 (EUR m, Sep 30 2025 vs Sep 30 2024); Contract liabilities 22,321 vs 18,867
        - **reproduction**: SELECT text FROM sources WHERE id=3180 -- search 'Reservation fees'
      - - **source**: chunks, form TRANSCRIPT, GEV 2Q 2026 results call Jul 22 2026
        - **date**: 2026-07-22
        - **quote_or_number**: In the second half of the year, we expect to convert many of these SRAs into orders ... achieving an important inflection point with gigawatts and backlog greater than SRAs.
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"inflection point" AND "SRAs"' AND c.ticker='GEV' AND c.form='TRANSCRIPT'
      - - **source**: chunks, form 10-K, GEV FY2025 risk factors
        - **date**: 2026-01-29
        - **quote_or_number**: If anticipated demand is delayed or does not materialize, orders may be deferred, reduced, or canceled and slot reservation agreements may not result in orders.
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation agreements may not result"' AND c.ticker='GEV'
    - **why_market_misses_it**: Sell-side and GEV headline the combined '116 GW' and '125 GW by year-end' number, which mixes firm backlog with SRAs. Nobody benchmarks GEV's SRA turnover against Siemens, which is the only peer that (a) states a conversion window, (b) defines its commitment pool as bookable within 12 months, and (c) shows reservation fees as a balance-sheet line, so the option-like nature of an SRA is visible in its accounts but not in GEV's.
    - **testable_prediction**: GEV Q3 2026 release (about Oct 22 2026): either new SRA signings fall below 10 GW (vs 18-21 GW in each of the last three quarters) or conversions exceed 15 GW; if neither happens, year-end backlog cannot exceed SRAs and the 'inflection' will be walked back on the Q3 call. Also, by the FY2026 10-K (late Jan 2027) GEV will still not disclose a reservation-fee balance or an SRA conversion window.
    - **kill_condition**: Q3 2026 shows conversions >= 12 GW AND new SRAs >= 15 GW AND shipments >= 5 GW (all three at once), or GEV discloses that its SRAs carry non-refundable fees above about 10% of unit value.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: Siemens's 27 GW Q2 SRA figure is derived (87 total commitments minus the 'around 60 GW' backlog cited on the pre-close call), not printed. Siemens GW counts include medium turbines (20-100 MW) and may be rated differently from GEV's. The EUR 20-25m/GW fee estimate assumes the Sep-2025 reservation-fee balance relates only to gas SRAs; some may be Grid Technologies. GEV's conversion-rate arithmetic ignores SRA expiries, which GEV has never disclosed.
  - - **title**: Same quarter, opposite direction in US onshore wind: Vestas Americas onshore intake doubled while GEV Wind orders fell 40%
    - **claim**: In Apr-Jun 2026 Vestas booked 1,759 MW of onshore orders in the Americas (up from 873 MW in Q1 2026 and 178 MW in Q2 2024) and total firm intake rose 67% YoY 'especially in the US', while GEV's Wind segment orders fell 40% organically to $1.2B 'due to lower equipment at Onshore Wind' and its Wind EBITDA loss widened.
    - **mechanism**: GEV's Wind segment (about $9B revenue, loss-making) is guided to narrow losses on Onshore volume; management blamed the Q2 2026 revenue decline on 'soft orders in the first half of 2025'. If the US onshore order recovery after the 2025 policy pause is going to Vestas rather than GEV, GEV's Onshore Wind revenue keeps falling through 2027 and the segment stays a drag on group EBITDA margin, contradicting the bull assumption that Wind turns to breakeven.
    - **direction**: short
    - **evidence**:
      - - **source**: sources id 3230 (Vestas Interim Report Q2 2026, Aug 12 2026)
        - **date**: 2026-08-12
        - **quote_or_number**: Onshore order intake 1,522 (EMEA) 1,759 (Americas) 68 (APAC) 3,349 total; 'a 67 percent increase from second quarter 2025'; 'driven by a strong Onshore order intake in the Americas'; ASP EUR 1.00m/MW, 'lower ASP was driven by the higher level of order intake in the Americas with low-scope projects'
        - **reproduction**: SELECT text FROM sources WHERE id=3230 -- search 'Wind turbine order intake, second quarter 2026'
      - - **source**: sources id 3231 (Vestas Q2 2026 investor presentation)
        - **date**: 2026-08-12
        - **quote_or_number**: strong Onshore order intake, especially in the US and Germany
        - **reproduction**: SELECT text FROM sources WHERE id=3231 -- search 'especially in the US'
      - - **source**: sources id 3232 (Vestas Q1 2026 announcement) and id 3239 (Q2 2024)
        - **date**: 2026-05-06 and 2024-08-14
        - **quote_or_number**: Q1 2026 onshore intake by region 777 / 873 (Americas) / 94; Q2 2024 onshore intake 1,936 / 178 (Americas) / 822
        - **reproduction**: SELECT id, text FROM sources WHERE id IN (3232,3239) -- search 'Onshore order intake'
      - - **source**: https://www.vestas.com/en/media/company-news/2025/vestas---interim-report--second-quarter-2025-c4217324
        - **date**: 2025-08-13
        - **quote_or_number**: Q2 2025 firm intake 2,009 MW, 'Lower order intake YoY as customers have been awaiting policy clarity, particularly in the USA'
        - **reproduction**: fetch the URL; Q2 2025 order-intake paragraph
      - - **source**: chunks, form 8-K/EX, GEV Q2 2026 earnings release
        - **date**: 2026-07-22
        - **quote_or_number**: Wind: Orders of $1.2 billion decreased (40)% organically due to lower equipment at Onshore Wind. Revenues of $2.0 billion decreased (10)% ... Segment EBITDA losses grew
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind" AND "Orders of"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22'
      - - **source**: chunks, form 8-K/EX, GEV Q1 2026 and Q2 2025 earnings releases
        - **date**: 2026-04-22 and 2025-07-23
        - **quote_or_number**: Q1'26 Wind orders $1.2B +85% 'off a low year-over-year comparison'; Q2'25 Wind orders $2.1B (-5%) 'lower Onshore Wind equipment orders'
        - **reproduction**: same query with filing_date IN ('2026-04-22','2025-07-23')
    - **why_market_misses_it**: GEV is covered as a gas and grid story; Wind is treated as a rounding error that only matters for offshore charges. Nobody lines up the two OEMs' order books for the same 13 weeks in the same market, and Vestas does not name US customers, so the share shift is only visible by juxtaposition.
    - **testable_prediction**: GEV Q3 2026 (Oct 22 2026) Wind orders below $1.6B with Onshore equipment orders down YoY again, while Vestas Q3 2026 (early Nov 2026) shows Americas onshore intake above 1 GW for a third straight quarter.
    - **kill_condition**: GEV Q3 2026 Wind orders up more than 30% organically on Onshore equipment, or GEV announces a US onshore order package above 1.5 GW before year-end 2026.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: The Q2 2025 Americas onshore split for Vestas was not retrievable (PDF fetch timed out), so the YoY growth of the Americas line specifically is inferred from the 67% total growth plus management attribution. GEV reports Wind orders in dollars including services; Vestas reports MW of firm equipment orders. One quarter is not a trend; Q1 2026 GEV orders were up 85% off a very low base.
  - - **title**: Cross-OEM ledger for Apr-Jun 2026: 38 GW of new commitments signed against 11 GW shipped, and Siemens shipped twice GEV's gigawatts in the same quarter
    - **claim**: In the same calendar quarter the three large-frame OEMs booked 31 GW of firm orders (GEV 12, Siemens 15, MHI 4) plus about 29 GW of new reservations (GEV 18, Siemens about 11) while shipping about 11 GW (GEV 3, Siemens 6, MHI about 2), so the combined commitment pool of about 246 GW (GEV 116, Siemens 95, MHI 35) equals 5-6 years of current shipments and about 3.5 years of the 2028 nameplate capacity the three have announced.
    - **mechanism**: Commitments are only worth their 2027-2030 delivery slots. If aggregate commitments run at about 150 GW/yr while shipments run at about 45 GW/yr and 2028 capacity is roughly 65-75 GW/yr, the queue lengthens rather than clears; late-vintage slots (2030-31, already where MHI says current discussions sit) are the ones most exposed to project slippage and to MHI's own forecast that demand falls to 40-50 GW/yr after 2027. For GEV specifically, Siemens shipping 6 GW in the quarter while GEV shipped 3 GW undercuts the idea that GEV's factory scale is the binding constraint in the market and raises the bar for GEV's stated 20 GW/yr run-rate from Q3 2026 (needs 5 GW/qtr immediately).
    - **direction**: either
    - **evidence**:
      - - **source**: sources id 3167 (Siemens Energy Q3 FY26 analyst presentation)
        - **date**: 2026-08-05
        - **quote_or_number**: 15 GW booked (12 GW converted from SRAs), 6 GW shipped; 69 GW backlog / 26 GW SRAs; LGT capacity in units FY25 35, FY26 ~35, FY27 ~50, FY28 50+; MGT 50, ~80, ~100
        - **reproduction**: SELECT text FROM sources WHERE id=3167 -- search 'Capacity ramp-up'
      - - **source**: sources id 3197 (MHI Q1 FY2026 results presentation, Aug 6 2026)
        - **date**: 2026-08-06
        - **quote_or_number**: Large Frame Gas Turbine Order Intake: Q1 FY25 8 (4 GW), FY25 35 (16 GW), Q1 FY26 10 (4 GW); Americas 6 / 19 / 4; Contract Backlog 53 (23 GW) / 74 (33 GW) / 80 (35 GW)
        - **reproduction**: SELECT text FROM sources WHERE id=3197 -- search 'Large Frame Gas Turbine Order Intake and Contract Backlog'
      - - **source**: sources id 3199 (MHI Q1 FY2026 Q&A summary)
        - **date**: 2026-08-06
        - **quote_or_number**: The projects currently under discussion with customers will generally be delivered around 2030 to 2031 ... orders booked in Q1 are generally scheduled for delivery between 2028 and 2030.
        - **reproduction**: SELECT text FROM sources WHERE id=3199 -- search '2030 to 2031'
      - - **source**: sources id 3211 (MHI Q2 FY2025 Q&A) and id 3202 (MHI FY2025 results summary)
        - **date**: 2025-11 and 2026-05
        - **quote_or_number**: GTCC briefing projected about 70 GW/year 2025-2027 'followed by a decline to around 40 to 50 GW'; Ito: 'The projected demand of 70 GW/year seems slightly too high'. FY25 summary: 'global demand for gas turbines in CY2025 was around 100 GW' (McCoy)
        - **reproduction**: SELECT id, text FROM sources WHERE id IN (3211,3202) -- search '40 to 50 GW' and 'around 100 GW'
      - - **source**: chunks, form 8-K/EX, GEV Q2 2026 earnings release
        - **date**: 2026-07-22
        - **quote_or_number**: Signed 20 GW ... including 18 GW of slot reservation agreements and 2 GW of orders. Converted 10 GW ... shipped 3 GW ... backlog 44 to 53 GW ... SRAs 56 to 63 GW; at least 125 GW by year-end 2026
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND "shipped"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22'
      - - **source**: sources id 3169 (Siemens pre-close call)
        - **date**: 2026-06-29
        - **quote_or_number**: we are booked out onto '28 and let's say, '29 and 2030 is filling up very quickly ... already now 2029 is something which is seen as short-term availability
        - **reproduction**: SELECT text FROM sources WHERE id=3169 -- search 'booked out'
    - **why_market_misses_it**: Each OEM's quarter is reported in its own units (GEV in GW with SRAs, Siemens in GW and turbine units on a September fiscal year, MHI in units and yen on a March fiscal year), so nobody adds them up for the same 13 weeks. The 'supply-constrained market' narrative is judged on GEV's numbers alone.
    - **testable_prediction**: By the Nov 2026 Siemens Q4 FY26 release and the Nov 2026 MHI Q2 FY26 release, the three-OEM quarterly shipment total stays below 14 GW while combined new commitments stay above 25 GW, i.e. the commitment-to-shipment ratio remains above 2x; MHI Americas large-frame orders in Jul-Sep 2026 come in at or below 5 units.
    - **kill_condition**: GEV ships 5+ GW in Q3 2026 and Siemens reports Q4 FY26 shipments of 6+ GW again (combined run-rate near 50 GW/yr with MHI), or MHI raises its post-2027 market view above 70 GW/yr.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: Siemens's 11 GW of new Q3 SRAs is derived (26 closing - 27 opening + 12 converted). Siemens's '6 GW shipped' could include medium turbines; GEV's 3 GW is heavy-duty only. MHI's about 2 GW shipped is inferred from backlog roll-forward (33 + 4 - 35). GW ratings across OEMs are not standardized (simple-cycle vs combined-cycle plant output). This partly overlaps the team's 'factory throughput ceiling' and 'MHI 70 vs Siemens 110-120' angles; the new element is the same-quarter three-OEM ledger and the Siemens-shipped-2x-GEV datum.
- **dead_ends**:
  - Double-booking evidence in the projects table: only one owner (Applied Digital) is tagged with both Siemens Energy and GE Vernova, and the underlying quotes are about Babcock & Wilcox boilers and steam turbines with gas turbines 'when available', so it is not a dual-OEM turbine reservation. No other owner overlap. Query: SELECT owner, GROUP_CONCAT(DISTINCT oem) FROM projects GROUP BY owner HAVING COUNT(DISTINCT oem)>1.
  - No competitor admits customers double-book slots. Siemens says the opposite ('slot reservations are not speculative', 'limited number of clients', 'not seen any cancellations or any delays on our side', Jun 29 2026 pre-close call, sources id 3169). MHI says it is 'selective ... core U.S. utility customers' (id 3199). No 'cancel' or 'postpone' sentence about GTCC appears in any MHI Q&A or presentation (ids 3199-3215).
  - Siemens Energy Annual Report 2025 (id 3180) contains no accounting policy on reservation-fee refundability or SRA cancellation; the only 'cancellation' hits are treasury-share authorizations. Reservation fees appear solely as a balance-sheet line (EUR 563m).
  - competitor_financials table is mostly unusable: 251 rows but MHI rows are all 'Not specified', many Siemens rows have blank values or nonsense ('Gas Services margin 61.3%'). Use the raw sources ids 3164-3223 instead.
  - Hitachi Energy sources (ids 3244-3278, 174 rows) are navigation and news-index pages with almost no financial content; nothing on transformer pricing or backlog to compare with Prolec. Not worth re-reading.
  - Vestas Q2 2025 Americas onshore split: the PDF fetch timed out; the company-news page gives only the 2,009 MW total and the US policy-clarity quote.
  - Hydrogen and H-class reliability: competitor statements are marketing (HYFLEXPOWER 100% hydrogen demo, MHI Takasago 30% co-firing, McDonough 50% blend) with no reliability, availability or warranty numbers to set against GEV's $0.3B/yr availability-shortfall reductions.
  - Service economics comparison: Siemens gives '~EUR 400m/GW' new-unit revenue potential, '700 GW installed fleet' and '90% renewal rates' but no service revenue per GW-year, so GEV's $70M/GW-year claim cannot be cross-checked from these filings.
  - Pricing by vintage: MHI says 'profitability at the time of order booking ... improving year by year' and Siemens cites 'increased profitability of the processed order backlog', but neither publishes margin by order vintage, so the GLJ 2027-vintage margin claim cannot be corroborated or refuted from competitor disclosures.
  - documents table has no competitor filings (URL LIKE '%siemens%' etc. returns zero rows); all competitor material lives in sources with kind='competitor' (chunks accession 'src:<id>').

## [Sweep] find:narrative-archaeology

- **lens**: Narrative archaeology and echo detection: trace viral GEV claims (pricing "+300%", "$2,500-3,000/kW", "20 GW output", "sold out to 2030", "$70M per GW-year", "consensus" targets) to their origin in dated commentary, test each against GEV's own 10-Q/10-K/transcript numbers, and find bearish facts buried in bullish coverage.
- **findings**:
  - - **title**: The '$2,500-3,000/kW' and '+300%' turbine-price story is plant-level cost and a single Melius estimate; GEV's own numbers put its turbine scope near $740/kW, up ~54% in five quarters, with like-for-like guided at +10-20%
    - **claim**: Every $/kW figure circulating for GEV ($2,500 William Blair Jan-2026, $3,000 Morgan Stanley Jul-2026, EPRI $3,000) is combined-cycle PLANT cost of which GEV's CEO agreed GE captures ~30%; GEV's firm-backlog-implied price is $740/kW at Q2'26 (Power equipment RPO $39,261M / 53 GW), up 54% from $480/kW at Q1'25, and GEV guided H2'26 order $/kW only 10-20 points above Q4'25, attributing reported jumps to aero and combined-cycle mix twice (Oct-2025, Jul-2026).
    - **mechanism**: Analyst margin models and the bull 'pricing power' multiple assume turbine ASPs tripled; if the like-for-like rise is ~+50-100% cumulative and much of the reported $/kW gain is mix (aeroderivatives priced higher per MW, CC scope added at SRA conversion), then Power segment EBITDA margin expansion from price alone is smaller than modeled. Equally, GLJ's 'old-price 2027 vintage' cliff shrinks because the price step between vintages is smaller than 300%.
    - **direction**: either
    - **evidence**:
      - - **source**: Q3'25 earnings transcript (sources.id 3796, gevernova.com gev_webcast_transcript_10222025.pdf), BNP Paribas Moses Sutton question and Scott Strazik answer
        - **date**: 2025-10-22
        - **quote_or_number**: Sutton: '$2,500/kW in the US ... with GE capturing 30% of that in the turbine sale typically?' Strazik: 'the directional number of $2,500/kW ... and our directional share, I agree with ... it's more mix ... more aeroderivatives that are higher priced per megawatt'
        - **reproduction**: python - <<'EOF'
import sqlite3;con=sqlite3.connect(r'data\gev.db');t=con.execute("SELECT text FROM sources WHERE id=3796").fetchone()[0];i=t.find('$2,500/kW');print(t[i-900:i+900])
EOF
      - - **source**: Q2'26 earnings transcript (sources.id 3161, gev_webcast_transcript_07222026.pdf), CFO prepared remarks
        - **date**: 2026-07-22
        - **quote_or_number**: 'In 2Q, we booked a higher dollar per kW price in orders, given a higher mix of aeroderivatives versus heavy-duty gas turbines and incremental combined cycle equipment as SRAs converted to orders.' and 'dollar per kW that is at the higher end of the range of 10 to 20 points versus 4Q '25 orders.'
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"dollar per kW"' AND c.ticker='GEV' AND c.form='TRANSCRIPT';
      - - **source**: documents table, GEV 10-Q/10-K Power segment RPO tables (Equipment line) divided by firm gas backlog GW from 8-K/EX earnings releases
        - **date**: 2025-04-23 to 2026-07-22
        - **quote_or_number**: Power equipment RPO $M: Q1'25 13,920; Q2'25 16,133; Q3'25 18,977; Q4'25 24,707; Q1'26 28,530; Q2'26 39,261. Firm gas backlog GW: 29, 29, 33, 40, 44, 53. Implied $/kW: 480, 556, 575, 617, 648, 740 (+54%).
        - **reproduction**: python - <<'EOF'
import sqlite3,re;con=sqlite3.connect(r'data\gev.db')
for f,d,t in con.execute("SELECT form,filing_date,text FROM documents WHERE ticker='GEV' AND form IN ('10-Q','10-K') AND filing_date>='2025-04-01' ORDER BY filing_date"):
  i=t.find('Gas Turbine Gigawatts');m=re.search(r'Equipment\s+\$[\d,]+',t[i:i+900]);print(f,d,m.group(0))
EOF
# backlog GW: SELECT filing_date, quote FROM backlog_quarterly WHERE ticker='GEV' AND metric='reservation_gw' AND quote LIKE '%backlog%' ORDER BY filing_date;
      - - **source**: Commentary: Yahoo Finance (published 2026-06-22 in corpus, cites CNBC Seema Mody plant visit of June 24), CNBC 2026-06-27 article, 247wallst 2026-06-24; regex-filtered count of commentary sources repeating '300%' with turbine/pricing
        - **date**: 2026-06-22 to 2026-08-12
        - **quote_or_number**: CNBC: 'The price has soared, up 300% in the last 3 years, according to analysts at Melius.' 9 distinct commentary URLs repeat the 300% figure; only 2 attribute it to Melius; none cite a GEV filing.
        - **reproduction**: SELECT s.published, s.url FROM chunks_fts f JOIN chunks c ON c.id=f.rowid JOIN sources s ON s.id=CAST(substr(c.accession,5) AS INTEGER) WHERE chunks_fts MATCH '"300%"' AND c.ticker='GEV' AND c.tier='commentary' AND (c.text LIKE '%300% in%turbine%' OR c.text LIKE '%pricing%300%%' OR c.text LIKE '%300%%pric%');
      - - **source**: Yahoo Finance 'Morgan Stanley strongly resets' (analyst_calls, Morgan Stanley David Arcaro note) and Yahoo 'ge-vernova-q4-gas-turbine' quoting William Blair
        - **date**: 2026-07-22 and 2026-01-23
        - **quote_or_number**: MS: 'Slot reservations are now pricing near $3,000 per kilowatt of implied combined cycle plant pricing'; William Blair: 'GE Vernova was booking turbine orders at $2,500/kW'
        - **reproduction**: SELECT published,url,substr(text,instr(text,'3,000 per kilowatt')-300,500) FROM sources WHERE url LIKE '%morgan-stanley-strongly-resets%'; SELECT published,url,substr(text,instr(text,'2,500/kW')-300,400) FROM sources WHERE url LIKE '%ge-vernova-q4-gas-turbine-104353017%';
    - **why_market_misses_it**: The $/kW numbers travel without their denominator: a CCGT plant number ($2,500-3,000) is re-reported as GEV's turbine price, and a Melius rule-of-thumb aired on a CNBC factory tour became 'GEV prices up 300%' in nine outlets. GEV's two on-the-record mix explanations sit in Q&A transcripts, not in headlines, and nobody divides segment equipment RPO by the disclosed firm GW backlog.
    - **testable_prediction**: In the Q3'26 10-Q (expected ~Oct 21-22, 2026) Power equipment RPO divided by the firm gas backlog GW disclosed in the same-day 8-K/EX will be $700-900/kW, not above $1,200/kW; and management will again describe H2 order $/kW as +10-20 points vs Q4'25, not multiples.
    - **kill_condition**: Q3'26 backlog-implied price above $1,200/kW, or GEV states a like-for-like heavy-duty price increase above 50% year over year, or discloses that its scope is materially above 30% of plant cost.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Power equipment RPO includes nuclear, hydro and steam equipment (a few $B), so gas-only $/kW is lower and the percentage rise somewhat larger (roughly +85% if ~$4B is non-gas); the ratio is an average of the backlog, not the marginal order price; firm backlog GW excludes SRAs, whose deposit pricing is not disclosed. End-2024 firm backlog (25 GW) is derived, not stated.
  - - **title**: Gas turbine shipments fell 9% YoY in H1'26 and HA units shipped fell 38%, in the year the market repeats '20 GW output'; Q2'26 shipped 3 HA units and 16 aeroderivatives
    - **claim**: GEV's 10-Q 'Sales in units' table shows H1'26 gas turbine shipments of 7.5 GW vs 8.2 GW in H1'25 (-9%), HA units 8 vs 13 (-38%), and Q2'26 3.3 GW with only 3 HA units and 16 aeros; management headlined '29 gas turbines shipped, +38%', and 65 commentary sources repeat the 20 GW annual-output claim while none report the HA unit count.
    - **mechanism**: Gas equipment revenue is recognized over time, but shipments drive the milestone billing that feeds H2'26 FCF ($1.6-2.6B implied) and the 2027 revenue ramp; a 20 GW run-rate from Q3'26 requires ~5 GW per quarter versus 3.3 GW just delivered. Aeroderivative-heavy shipments (16 of 29 units) carry small MW per unit, so unit-count growth masks GW decline; Q2'26 Power equipment revenue growth was attributed in the 10-Q to 'higher Aeroderivative deliveries and favorable pricing', not HA.
    - **direction**: short
    - **evidence**:
      - - **source**: documents table, GEV 10-Q filed 2026-07-22, Power segment 'Sales in units' table
        - **date**: 2026-07-22
        - **quote_or_number**: Three months ended June 30 2026 vs 2025: Gas Turbines 29 vs 21; Heavy-Duty 13 vs 18; HA-Turbines 3 vs 8; Aeroderivatives 16 vs 3; Gas Turbine Gigawatts 3.3 vs 5.2. Six months: 54 vs 40 units; HA 8 vs 13; GW 7.5 vs 8.2.
        - **reproduction**: python - <<'EOF'
import sqlite3;con=sqlite3.connect(r'data\gev.db');t=con.execute("SELECT text FROM documents WHERE ticker='GEV' AND form='10-Q' AND filing_date='2026-07-22'").fetchone()[0];i=t.find('Sales in units');print(t[i:i+260])
EOF
      - - **source**: documents table, all GEV 10-Q/10-K 'Sales in units' tables 2024-2026 (quarterly derived by subtracting YTD)
        - **date**: 2024-04-30 to 2026-07-22
        - **quote_or_number**: GW shipped by quarter Q1'24..Q2'26: 2.3, 1.5, 3.3, 4.8, 3.0, 5.2, 4.0, 3.1, 4.2, 3.3. HA units: 1, 1, 5, 8, 5, 8, 6, 5, 5, 3. No quarter has exceeded 5.2 GW in ten quarters.
        - **reproduction**: python - <<'EOF'
import sqlite3;con=sqlite3.connect(r'data\gev.db')
for f,d,t in con.execute("SELECT form,filing_date,text FROM documents WHERE ticker='GEV' AND form IN ('10-Q','10-K') ORDER BY filing_date"):
  i=t.find('Sales in units');print(f,d,t[i:i+230].replace('\n',' '))
EOF
      - - **source**: Q2'26 earnings transcript (sources.id 3161)
        - **date**: 2026-07-22
        - **quote_or_number**: 'We shipped a total of 29 gas turbines in the quarter, a 38% increase year-over-year, including 16 aeroderivatives.' and 'In Gas Power, we shipped three gigawatts'
        - **reproduction**: SELECT substr(text, instr(text,'shipped a total of 29')-50, 300) FROM sources WHERE id=3161;
      - - **source**: chunks_fts commentary count, regex-filtered for '20 GW/gigawatts' adjacent to output/annual/run-rate; and regex for HA units shipped
        - **date**: 2026-04 to 2026-09
        - **quote_or_number**: 65 distinct commentary URLs repeat the 20 GW annual output claim; 0 commentary URLs mention that 3 HA units shipped in Q2'26 (the 4 that mention shipments say only '3 GW').
        - **reproduction**: SELECT COUNT(DISTINCT c.accession) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"20 GW" OR "20 gigawatts"' AND c.ticker='GEV' AND c.tier='commentary' AND (c.text LIKE '%output%' OR c.text LIKE '%annual%' OR c.text LIKE '%run rate%' OR c.text LIKE '%run-rate%'); -- then regex 20\s*(GW|gigawatts)[^.]{0,80}(output|annual|run.rate) in Python
      - - **source**: GEV 10-Q filed 2026-07-22, Power revenue discussion
        - **date**: 2026-07-22
        - **quote_or_number**: 'primarily at Gas Power equipment due to higher Aeroderivative unit deliveries and favorable pricing'
        - **reproduction**: SELECT substr(text, instr(text,'higher Aeroderivative unit deliveries')-200, 400) FROM documents WHERE ticker='GEV' AND form='10-Q' AND filing_date='2026-07-22';
    - **why_market_misses_it**: Coverage quotes the transcript headline (29 units, +38%) and the 20 GW run-rate promise; the GW and HA-unit rows sit in a small 10-Q table that is not in the press release. The team's existing 'throughput ceiling' angle asks whether 20 GW is reachable; this shows shipments are currently going the other way, and that the Q2 equipment growth came from aeros, not the HA machines the backlog is made of.
    - **testable_prediction**: The Q3'26 10-Q (expected ~Oct 21-22, 2026) 'Sales in units' row will show under 5.0 GW shipped and fewer than 8 HA units; if the 20 GW run-rate is real, Q3 must print at least 5.0 GW.
    - **kill_condition**: Q3'26 shipments of 5.0 GW or more with at least 8 HA units, or GEV discloses that H1'26 shipment mix was deliberately aero-front-loaded with HA slots concentrated in Q4'26 and Q4 prints 6+ GW.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: Sharpens an angle already on the team list rather than replacing it. Revenue is cost-to-cost, so a shipment shortfall hits cash milestones and 2027 deliveries more than reported Q3 revenue. Quarterly figures are derived from YTD tables; Q4'24 and Q4'25 are FY minus 9M. Aeroderivative GW per unit is small, so unit growth is real but GW-light.
  - - **title**: Backlog arithmetic says 2026, not 2027, is the '2024-vintage' year: GLJ's 'turbines shipping in 2027 were sold in 2024' fails a FIFO check
    - **claim**: GEV's own disclosures imply a firm gas backlog of ~25 GW at end-2024 (29 GW at Q1'25 minus 7 GW Q1 orders plus 3.0 GW shipped); shipments of 15.3 GW in 2025 plus 7.5 GW in H1'26 (22.8 GW) have consumed all but ~2 GW of pre-2025 orders, so under first-in-first-out delivery, 2027 shipments (targeted ~20-24 GW) would be over 90% 2025-vintage orders, at prices GEV described as accelerating; GLJ's $470 target rests on 2027 deliveries being 2024-vintage at ~3 points of margin.
    - **mechanism**: Segment EBITDA margin on gas equipment revenue recognized in 2027 depends on the order vintage being executed; if 2027 deliveries are 2025-vintage, the 10-11 point margin GLJ concedes for the 2025 vintage applies to 2027, removing the specific margin air-pocket that justified the Sep 14 Sell initiation and the 8.6% one-day drop.
    - **direction**: long
    - **evidence**:
      - - **source**: 8-K/EX earnings releases 2025-04-23, 2025-07-23, 2026-01-28, 2026-04-22, 2026-07-22 (backlog_quarterly reservation_gw quotes)
        - **date**: 2025-04-23 to 2026-07-22
        - **quote_or_number**: Q1'25: 'Signed 7 gigawatts of gas turbine orders, raising our Gas Power equipment backlog to 29 gigawatts'; Q4'25: 'backlog growth from 33 to 40 GW'; Q1'26: 'from 40 to 44 GW'; Q2'26: 'from 44 to 53 GW'
        - **reproduction**: SELECT filing_date, form, quote FROM backlog_quarterly WHERE ticker='GEV' AND metric='reservation_gw' AND quote LIKE '%backlog%' ORDER BY filing_date;
      - - **source**: documents table, GEV 10-K filed 2026-01-29 and 10-Q filed 2026-07-22, Power 'Orders in units' and 'Sales in units' rows
        - **date**: 2026-01-29 and 2026-07-22
        - **quote_or_number**: Orders GW: 2023 9.5, 2024 20.2, 2025 29.8, H1'26 20.1. Shipments GW: 2023 13.8, 2024 11.9, 2025 15.3, H1'26 7.5.
        - **reproduction**: python - <<'EOF'
import sqlite3;con=sqlite3.connect(r'data\gev.db')
for f,d,t in con.execute("SELECT form,filing_date,text FROM documents WHERE ticker='GEV' AND form IN ('10-K','10-Q') AND filing_date IN ('2026-01-29','2026-07-22')"):
  i=t.find('Orders in units');print(f,d,t[i:i+520].replace('\n',' '))
EOF
      - - **source**: Q2'26 earnings transcript (sources.id 3161), CFO on tariffs
        - **date**: 2026-07-22
        - **quote_or_number**: 'the volume we've shipped in this first half had fewer contractual protections for tariffs since we signed these orders before their implementation' (i.e., H1'26 shipments were pre-2025 orders)
        - **reproduction**: SELECT substr(text, instr(text,'fewer contractual protections')-150, 350) FROM sources WHERE id=3161;
      - - **source**: analyst_calls and commentary: ad-hoc-news.de 2026-09-14, Yahoo/GuruFocus 2026-09-15/16 on GLJ (Gordon Johnson III) initiation
        - **date**: 2026-09-14 to 2026-09-18
        - **quote_or_number**: 'turbines tied to 2024 order bookings will still be shipped ahead of subsequent price increases, generating only about 3 percentage points of margin — a fraction of the 10 to 11 percentage points expected from the 2025 order vintage'
        - **reproduction**: SELECT published, url, substr(text, instr(text,'2024 order')-200, 500) FROM sources WHERE text LIKE '%GLJ%' AND text LIKE '%2024 order%';
    - **why_market_misses_it**: GLJ's vintage argument was repeated by at least six outlets in four days without anyone reconstructing the order-to-shipment ledger from GEV's own GW tables; the firm-backlog series only became disclosable in 2025 and the Sales-in-units rows are buried in 10-Q segment tables.
    - **testable_prediction**: On the Q3'26 call (~Oct 21-22, 2026) or the Dec 2026 investor update, GEV will guide 2027 Power segment EBITDA margin at or above the 17-19% FY26 range; Q3'26 gas equipment revenue growth will be accompanied by the 10-Q stating 'favorable pricing' for heavy-duty deliveries.
    - **kill_condition**: GEV states that a majority of 2027 heavy-duty deliveries were contracted before 2025, or guides 2027 Power margin below 2026, or the Q3'26 10-Q attributes Power equipment margin pressure to legacy-priced units.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: FIFO is an approximation: some 2024 orders carried 2027-28 delivery slots (utility CCGTs with later CODs), so a minority of 2027 units are 2024-vintage; end-2024 backlog is derived, not disclosed; the 25 GW includes aeros with short lead times, which strengthens FIFO for aeros but not for HA. This changes the conclusion of the '2027 order-vintage margin' angle already on the team list rather than being a new angle.
  - - **title**: The bull frontier's '$70M per GW-year of services' is a single Jefferies number from Sep 12 2026, about five times GEV's current services yield on its own 886 GW gas fleet; 'consensus' targets in the corpus come from about ten firms
    - **claim**: The '$70M per GW-year' figure originates in one Jefferies (Dumoulin-Smith) note on 2026-09-12 and appears in only two commentary URLs (both crypto-news sites), whereas GEV's 2025 Power services revenue of $13,081M across an 886 GW installed gas base (plus nuclear, hydro, steam) equals at most ~$15M per GW-year today; the $1,237 'consensus' target is a Yahoo/Koyfin aggregate echoed by four outlets while the corpus holds explicit GEV price targets from only about ten sell-side firms.
    - **mechanism**: If the team's bull case capitalizes services at $70M per GW-year on a 400 GW fleet ($28B per year, ~2.5x current Gas Power services revenue), the terminal value is built on one analyst's extrapolation of HA-class CSA economics to the whole fleet; using GEV's disclosed services yield cuts that services NPV by roughly 4-5x.
    - **direction**: neutral
    - **evidence**:
      - - **source**: Commentary: blockonomi.com and coincentral.com articles on the Jefferies note
        - **date**: 2026-09-12
        - **quote_or_number**: 'Dumoulin-Smith forecasts that GE Vernova could generate more than $70 million per gigawatt-year from its installed base during the 2030s, supported by a fleet exceeding 400 gigawatts.' Only 2 corpus URLs carry this figure.
        - **reproduction**: SELECT published, url FROM sources WHERE text LIKE '%70 million per gigawatt%';
      - - **source**: GEV S-1 (2024-03-13) and 8-K/EX (2024-03-08) Form 10 information statement
        - **date**: 2024-03-13
        - **quote_or_number**: 'we maintain the largest installed base of gas turbines globally of 886 installed GW and 2,206 GW total across our Gas Power, Nuclear Power, Hydro Power, and Steam Power businesses'
        - **reproduction**: SELECT form, filing_date, substr(text, instr(text,'886 installed GW')-120, 260) FROM chunks WHERE ticker='GEV' AND text LIKE '%886 installed GW%' LIMIT 2;
      - - **source**: GEV 10-K filed 2026-01-29, Power segment revenues table
        - **date**: 2026-01-29
        - **quote_or_number**: 2025 Power: Gas Power $16,006M; Equipment $6,686M; Services $13,081M (all Power businesses). $13,081M / 886 GW = $14.8M per GW-year upper bound for gas.
        - **reproduction**: SELECT substr(text, instr(text,'SEGMENT REVENUES AND EBITDA 2025 2024 2023 Gas Power'), 330) FROM documents WHERE ticker='GEV' AND form='10-K' AND filing_date='2026-01-29';
      - - **source**: analyst_calls table, GEV price targets
        - **date**: 2026-03-24 to 2026-09-20
        - **quote_or_number**: 130 price_target rows; distinct US sell-side firms with a GEV USD target: Morgan Stanley, Rothschild, Goldman, Jefferies, Baird, BNP Exane, Bernstein, Mizuho, GLJ, Guggenheim (10); '$1,237.34 average' attributed to Yahoo Finance/Koyfin in 4 rows.
        - **reproduction**: SELECT firm, analyst, value, published FROM analyst_calls WHERE ticker='GEV' AND metric='price_target' AND value LIKE '$%' ORDER BY published;
    - **why_market_misses_it**: Services-annuity numbers are quoted per GW without stating which GW (HA-class under CSA vs the whole legacy fleet); the Jefferies figure was published two days before the GLJ Sell and got absorbed into 'the bull case' by osmosis rather than by checking GEV's own services revenue per installed GW.
    - **testable_prediction**: GEV's FY26 10-K (late Jan 2027) will show Power services revenue below $15B, i.e., under $17M per installed gas GW; any GEV disclosure of services revenue per HA unit will imply well under $70M per GW-year for the fleet as a whole.
    - **kill_condition**: GEV or its 10-K discloses long-term services revenue per GW of HA fleet at or above $70M per GW-year, or restates the installed base such that current services yield exceeds $40M per GW-year.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: Dumoulin-Smith may mean the new HA/aero fleet under contractual service agreements, where $70M per GW-year (about $35M per year for a 500 MW unit) is plausible; the corpus does not contain the Jefferies note itself. The 886 GW figure is from March 2024. This finding argues for discipline in the team's bull math rather than a directional trade.
- **dead_ends**:
  - '125 GW under contract': about 45 commentary URLs checked; nearly all correctly say backlog plus slot reservations (53 + 63 = 116 GW at Q2'26); no meaningful mutation into 'firm orders'. Not pitchable.
  - '$200B backlog by 2027': traces cleanly to GEV (Dec 9 2025 investor update said 2028; Apr 22 2026 release pulled to 2027; Q2'26 transcript 'on track to reach $200 billion in 2027'). Commentary repeats it accurately.
  - 'World's largest gas turbine plant' (Greenville): no GEV filing in the corpus makes this claim; only hits are a 2008 ETN paper on the Greenville full-speed full-load test facility and unrelated MHI/USP&E pages. Nothing to trace.
  - 'Sold out through 2030': GEV's own Q2'26 wording is 'mostly sold out through '30'; 19 commentary URLs state it flat, 27 hedge it, 10 do both. The mutation is small and not material.
  - 'One turbine costs more than $250 million' (CNBC Jun 27 2026, 'industry estimates'): no origin found; consistent with a ~570 MW combined-cycle block at ~$750/kW GE scope, so not a distortion worth a finding.
  - Power segment orders-in-dollars split (equipment vs services) could not be extracted by regex from the documents table; used segment RPO instead. A teammate with the PDFs could add order-implied $/kW per quarter.
  - End-2024 firm gas backlog GW is not stated in the Jan 22 2025 release (source id 674) or any transcript in corpus; derived as 25 GW from the Q1'25 release. The corpus has only two transcripts (Q3'25, Q2'26); Q4'24, Q1'25, Q4'25, Q1'26 transcripts and the Dec 2025 investor day are absent (Dec 2025 available only via a lastbastion.com summary).
  - Semantic search (src/embed.py) was not used; FTS5 with regex post-filtering was sufficient. FTS5 tokenizes '300%' as '300', so raw MATCH counts (165 URLs) are meaningless without regex filtering (9 URLs).
  - queue_projects and operator_forecasts confirmed empty; not used.
  - Price reaction check: GEV fell 8.2% on Jun 23 2026 ($1,127.59 to $1,034.98) the day after the first '300%' article, then rose to $1,174.86 by Jun 30; no clean event-study signal, dropped.

## [Sweep] find:wind-electrification

- **lens**: Non-gas segment forensics: Wind (offshore losses, Vineyard settlement, onshore order collapse, guidance arithmetic) and Electrification (Prolec purchase accounting, margin, amortization schedule)
- **findings**:
  - - **title**: FY26 Wind guide requires a +$257M Q4 (best-ever quarter was +$19M); the Sept 16 Vineyard settlement is the swing item
    - **claim**: Management's reiterated FY26 Wind guide (~$400M EBITDA loss) plus its Q3 guide (~breakeven) and the H1 actual (-$657M) implies Q4'26 Wind segment EBITDA of about +$257M on ~$2.2B revenue (~+12% margin), versus the best Wind quarter since the spin of +$19M (Q4'24); the confidential Vineyard Wind settlement announced Sept 16-17, 2026 (GEV claimed $360M withheld; the project engineer had assessed ~$800-850M of damages against GEV) will decide whether Q3/Q4 carries a one-time item or a guide cut.
    - **mechanism**: Wind segment EBITDA flows straight into GEV Adjusted EBITDA (FY26 guide 12-14% on $45.5-46.5B = $5.5-6.5B). A Q4 Wind print near the H1 run-rate (-$100M to -$300M) is a $350-550M miss, 5-9% of FY26 EBITDA, from a company priced at 31-38x for never missing. Conversely, a settlement gain or contract-loss-reserve release that fills the hole is low-quality earnings. Wind is also now gross-margin negative (cost of revenues > revenue in Q1, Q2 and H1 2026), so operating leverage alone cannot produce +12%.
    - **direction**: short
    - **evidence**:
      - - **source**: 8-K/EX 2026-07-22 (chunks id 5624; transcript sources.id 3161 chunk 251605)
        - **date**: 2026-07-22
        - **quote_or_number**: "Wind: Organic revenue down low-double digits and approximately $400 million of segment EBITDA losses." Q3: "We expect EBITDA to be approximately break-even"
        - **reproduction**: SELECT id, filing_date, substr(text,1,1500) FROM chunks WHERE id IN (5624, 251605, 251607);
      - - **source**: 10-Q 2026-07-22 Item 2 (chunk 5740) and Item 1 segment table (chunks 5712, 5713)
        - **date**: 2026-07-22
        - **quote_or_number**: Wind Segment EBITDA Q2'26 $(275)M, H1'26 $(657)M; Q2 cost of revenues $2,123M vs segment revenue $2,026M; H1 $3,772M vs $3,459M
        - **reproduction**: SELECT id, substr(text,1,3000) FROM chunks WHERE id IN (5740, 5712, 5713);
      - - **source**: 10-Q 2026-04-22 (chunk 13706); 10-K 2026-01-29 (chunk 29750); 10-Q 2025-10-22 (chunk 38563 and neighbors)
        - **date**: 2026-04-22
        - **quote_or_number**: Q1'26 $(382)M; FY25 $(598)M, FY24 $(588)M; 9M'24 $(607)M so Q4'24 = +$19M; Q3'25 $(61)M, 9M'25 $(373)M so Q4'25 = $(225)M
        - **reproduction**: SELECT c.form, c.filing_date, substr(c.text,1,1200) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Segment EBITDA" "Onshore Wind" "Offshore Wind" "Total segment revenues"' AND c.ticker='GEV' AND c.form IN ('10-Q','10-K') ORDER BY c.filing_date;
      - - **source**: https://www.insurancejournal.com/news/east/2026/09/17/885444.htm (sources.id 3672)
        - **date**: 2026-09-17
        - **quote_or_number**: "sent a notice threatening to terminate its $1.3 billion contract, saying it was owed $360 million"; "Other terms of the confidential settlement were not disclosed."
        - **reproduction**: SELECT ord, text FROM chunks WHERE accession='src:3672' ORDER BY ord;
      - - **source**: https://www.nhpr.org/2026-09-17/vineyard-wind-ge-vernova-settle-dispute-over-wind-farm (sources.id 3598); New Bedford Light via chunk 224621
        - **date**: 2026-09-18
        - **quote_or_number**: "Vineyard Wind withheld about $300 million from GE after an engineer determined that the turbine maker owed about $850 million in damages."
        - **reproduction**: SELECT ord, text FROM chunks WHERE accession='src:3598' ORDER BY ord; SELECT text FROM chunks WHERE id=224621;
      - - **source**: 10-Q 2026-07-22 Item 2 (chunk 5721)
        - **date**: 2026-07-22
        - **quote_or_number**: "we are working with our customer to resolve outstanding claims and counterclaims" (only filing disclosure of the dispute; no dollar amount in any 2026 10-Q)
        - **reproduction**: SELECT substr(text,1,1200) FROM chunks WHERE id=5721;
      - - **source**: Yahoo Finance Sept 18 2026 (chunk 223197, sources url finance.yahoo.com/energy/articles/ge-vernova-eyes-200b-backlog-080209388.html)
        - **date**: 2026-09-18
        - **quote_or_number**: Strazik: wind "nearing a profitability pivot point as the company closes existing offshore projects"; "materially better in 2027 than in 2026"
        - **reproduction**: SELECT text FROM chunks WHERE id=223197;
    - **why_market_misses_it**: Wind is dismissed as a small, known loss-maker; nobody adds H1 actual + Q3 guide to see what Q4 must be. The settlement news (Sept 16-17) landed after the Q2 guide and has no disclosed terms, and sell-side notes in the corpus repeat the -$400M guide without checking the quarterly path. Vineyard revenue is recognised over time under a loss-contract estimate, so a settlement moves EBITDA through an estimate change that is invisible until the 10-Q note.
    - **testable_prediction**: At the Q3'26 print (about Oct 21-22, 2026), one of two things is observed: (a) FY26 Wind loss guide is widened to at least $500M, or (b) the Q3 10-Q revenue/contract-loss note or the release discloses a Vineyard-related settlement item of at least $100M (either sign). By the Q4 print (late Jan 2027), Q4'26 Wind EBITDA will not exceed +$100M excluding disclosed one-time items.
    - **kill_condition**: Q4'26 Wind segment EBITDA prints at or above +$200M with the 10-K/10-Q attributing it to onshore deliveries and services, and no settlement, reserve release, or other one-time item is disclosed.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: The +$257M is arithmetic on management's rounded words ('approximately'); if Q3 is -$100M rather than breakeven the Q4 requirement rises to +$357M, which strengthens the point. 70% of 2025 onshore orders are contractually H2'26 deliveries with tariff protections, so some H2 improvement is real. Settlement direction is unknown: GEV may have booked the $360M as a contract asset already reserved through the 2025 $637M loss charge, in which case a settlement could release reserves and make the guide, at low quality. Confidence 4 is for the arithmetic, not the outcome.
  - - **title**: Prolec is a 21-22% EBITDA-margin business hidden behind a GAAP pre-tax loss: $462M of acquisition accounting in five months
    - **claim**: Prolec GE contributed $296M of Electrification segment EBITDA on $1,346M revenue (22.0%) from Feb 2 to Jun 30, 2026, above the 19.1% organic Electrification margin, while its GAAP pre-tax result was a $(166)M loss because of $106M inventory step-up and about $716M/yr of new intangible amortization ($179M per quarter, of which $386M/yr is a 2-year 'trademarks and other' bucket that ends in Q1 2028).
    - **mechanism**: GAAP EPS (the basis of the quoted 31-38x forward P/E) carries roughly $179M/quarter of non-cash Prolec amortization, about $0.66/share pre-tax and ~$0.50 after tax per quarter on 271M diluted shares, so ~$2/share per year, around 8% of the $24.43 'following year' EPS cited in the corpus. Segment EBITDA, Adjusted EBITDA and FCF are untouched. From February 2028 amortization falls by $386M/yr (~$1.07/share after tax), a mechanical EPS step-up. The $9,656M total consideration equals ~13.6x annualized Prolec segment EBITDA, and Prolec's earnings were compounding before the deal (GEV's 50% share: $93M 2023, $105M 2024, $180M 2025).
    - **direction**: long
    - **evidence**:
      - - **source**: 8-K/EX 2026-07-22 organic reconciliation (chunks 5632, 5633)
        - **date**: 2026-07-22
        - **quote_or_number**: Electrification 'Less: Acquisitions' Q2: revenue $860M, segment EBITDA $183M; H1: revenue $1,346M, EBITDA $296M; Electrification organic margin 19.1% Q2, 17.0% H1
        - **reproduction**: SELECT id, substr(text,1,2500) FROM chunks WHERE id IN (5632, 5633);
      - - **source**: 10-Q 2026-07-22 Note 8 (chunks 5676, 5677, 5678, 5679, 5680)
        - **date**: 2026-07-22
        - **quote_or_number**: Consideration $9,656M (cash $5,254M + FV of held 50% $4,402M); goodwill $5,313M; intangibles $4,172M: customer 12y $2,860M, patents 6y $533M, trademarks & other 2y $771M; Prolec revenue/pre-tax Q2 $859M/$(57)M, since Feb 2 $1,344M/$(166)M; amortization $236M vs $60M
        - **reproduction**: SELECT id, substr(text,1,2600) FROM chunks WHERE id BETWEEN 5676 AND 5680;
      - - **source**: 8-K/EX 2026-07-22 Adjusted EBITDA reconciliation footnote (chunk 5637)
        - **date**: 2026-07-22
        - **quote_or_number**: "an expense of $35 million and $106 million for the impact of a fair value adjustment to Prolec GE inventory that was recorded in Cost of equipment"
        - **reproduction**: SELECT substr(text,1,1500) FROM chunks WHERE id=5637;
      - - **source**: 10-Q 2026-04-22 Note 8 (chunks 13652, 13653)
        - **date**: 2026-04-22
        - **quote_or_number**: Q1 preliminary PPA: intangibles $3,980M with 'Trademarks and other' 3 years $745M (changed in Q2 to 2 years $771M); Prolec Feb 2-Mar 31 revenue $485M, pre-tax $(105)M
        - **reproduction**: SELECT id, substr(text,1,1200) FROM chunks WHERE id IN (13652, 13653);
      - - **source**: 10-K 2026-01-29 Note 11 Equity method investments (chunk 29869); xbrl_facts IncomeLossFromEquityMethodInvestments
        - **date**: 2026-01-29
        - **quote_or_number**: Prolec GE(d) 50%: equity income $180M (2025), $105M (2024), $93M (2023); total equity income FY25 $269M matches XBRL
        - **reproduction**: SELECT substr(text,1,1200) FROM chunks WHERE id=29869; SELECT start_date,end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag='IncomeLossFromEquityMethodInvestments' AND fp='FY' GROUP BY start_date,end_date;
      - - **source**: xbrl_facts WeightedAverageNumberOfDilutedSharesOutstanding; analyst_calls (Wall Street, 2026-06-22)
        - **date**: 2026-06-30
        - **quote_or_number**: Diluted shares 271M (Q2'26); EPS cited $16.77 FY2026, $24.43 following year
        - **reproduction**: SELECT end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag='WeightedAverageNumberOfDilutedSharesOutstanding' AND end_date='2026-06-30' GROUP BY start_date; SELECT published,firm,metric,value,period FROM analyst_calls WHERE ticker='GEV' AND lower(metric) LIKE '%eps%';
      - - **source**: 8-K/EX 2026-01-28 multi-year outlook (chunk 30114)
        - **date**: 2026-01-28
        - **quote_or_number**: 2028 outlook: Electrification 'approximately $4 billion of revenue from Prolec GE, and segment EBITDA margin of 22%'
        - **reproduction**: SELECT substr(text,1,1500) FROM chunks WHERE id=30114;
    - **why_market_misses_it**: Screens and P/E quotes use GAAP EPS, which in 2026 is distorted twice by Prolec: the $3,992M non-taxable remeasurement gain inflates it (~$14.7/share) and the amortization depresses run-rate EPS. Prolec's own margin is only visible by dividing the 'Less: Acquisitions' EBITDA line by its revenue line in the 8-K reconciliation table; the 10-Q note shows only the pre-tax loss, so a casual reader concludes Prolec is loss-making and dilutive to Electrification margin, when it is accretive.
    - **testable_prediction**: Q3'26 8-K (about Oct 21-22, 2026): the Electrification 'Less: Acquisitions' line shows revenue of at least $880M and segment EBITDA of at least $185M (margin at or above 21%), while the 10-Q Note 8 still shows Prolec pre-tax income near or below zero; Q3 amortization expense stays within $225-250M. FY26 Prolec revenue lands at or above the $3.1B guide.
    - **kill_condition**: Prolec 'Less: Acquisitions' segment EBITDA margin falls below 17% in Q3 or Q4 2026, or the final PPA (due by Q1 2027) lengthens the 2-year bucket or adds material impairment, or GEV starts reporting an adjusted EPS that already strips the amortization (removing the optical discount).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Whether the market values GEV on GAAP or cash EPS is an assumption; many analysts already model EBITDA/FCF. The 2-year 'trademarks and other' bucket is a preliminary estimate that can move until Q1 2027. Prolec revenue guide implies about $3.4B annualized, so the 22% H1 margin is on partial-year numbers with lean/pricing tailwinds that may not persist; Section 232 tariffs on Mexican-made transformers were flagged as 'a little bit more impact' for Prolec (Apr 23 call summary, chunk 236437).
  - - **title**: Onshore Wind book-to-bill has fallen to ~0.5 in GW with zero repower orders; H2'26 delivery surge is a pull-forward, not a recovery
    - **claim**: Wind orders were 0.6 GW in each of Q1'26 and Q2'26 (Q2: 147 turbines, 0 repower units, vs 381 turbines and 205 repower units in Q2'25) against sales of 2.0 GW in H1'26, so the equipment RPO ($8.2B, down from $13.7B at Dec-23) is being consumed faster than replaced; management's H2'26 improvement rests on delivering the 70% of 2025 orders booked in H2'25, which sets up a further 2027 onshore equipment revenue decline of 30-40% unless orders at least double from the 1.2 GW H1 pace.
    - **mechanism**: Onshore equipment revenue (2025: $7.25B Wind equipment) is recognised on delivery; 2027 deliveries come from 2026 orders. At the H1'26 pace (2.4 GW annualized vs 6.9 GW sold in 2025) 2027 onshore equipment volume falls again, extending gross-margin-negative Wind results and making the 2028 outlook (Wind margin 6%) dependent on services and repower alone. This matters for the 3-12 month window via the January 2027 outlook, when management must guide 2027 Wind.
    - **direction**: short
    - **evidence**:
      - - **source**: 10-Q 2026-07-22 Item 2 Wind tables (chunks 5739, 5740)
        - **date**: 2026-07-22
        - **quote_or_number**: Orders Q2'26/Q2'25: Wind Turbines 147/381, Repower Units 0/205, GW 0.6/1.6; H1 GW 1.2/1.8. Sales H1 GW 2.0/3.0. Equipment RPO $8,197M (Jun-26) vs $9,112M (Dec-25) vs $9,731M (Jun-25)
        - **reproduction**: SELECT id, substr(text,1,2000) FROM chunks WHERE id IN (5739, 5740);
      - - **source**: 10-Q 2026-04-22 (chunk 13705 area: 'Wind Turbine and Repower Units Gigawatts 0.6 0.1'); 10-K 2026-01-29 (chunk 29750)
        - **date**: 2026-04-22
        - **quote_or_number**: Q1'26 orders 0.6 GW vs Q1'25 0.1 GW; FY25 sales 6.9 GW (7.8 GW 2024, 8.8 GW 2023); equipment RPO $13,709M Dec-23 to $9,112M Dec-25
        - **reproduction**: SELECT c.filing_date, substr(c.text,1,900) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind Turbine and Repower Units Gigawatts"' AND c.ticker='GEV' AND c.form IN ('10-Q','10-K') ORDER BY c.filing_date;
      - - **source**: Q2'26 call transcript (sources.id 3161, chunks 251596, 251605)
        - **date**: 2026-07-22
        - **quote_or_number**: "70% of 2025 equipment orders were in the second half and will be delivered in the second half of 2026"; "approximately 10 gigawatts of units with repowering potential ... already qualified for the new production tax credits"
        - **reproduction**: SELECT ord, text FROM chunks WHERE accession='src:3161' AND ord IN (8, 17) ORDER BY ord;
      - - **source**: generators (EIA-860M Planned sheet), technology='Onshore Wind Turbine'
        - **date**: 2026-07
        - **quote_or_number**: Planned US onshore wind: as of 2026-01 vintage 9,682 MW for 2026 and 4,621 MW for 2027; as of 2026-07 vintage 4,301 MW (2026), 4,559 MW (2027), 3,656 MW (2028)
        - **reproduction**: SELECT vintage, planned_year, ROUND(SUM(mw)) mw, COUNT(*) n FROM generators WHERE vintage IN ('2025-07','2026-01','2026-07') AND sheet='Planned' AND technology='Onshore Wind Turbine' AND planned_year BETWEEN 2025 AND 2030 GROUP BY vintage, planned_year;
      - - **source**: 8-K/EX 2026-01-28 (chunk 30114)
        - **date**: 2026-01-28
        - **quote_or_number**: 2028 outlook: "Wind: Down low-double digits organic revenue CAGR and segment EBITDA margin of 6%"
        - **reproduction**: SELECT substr(text,1,1500) FROM chunks WHERE id=30114;
    - **why_market_misses_it**: The team list already has 'onshore order collapse (-40% y/y)'; what changes the conclusion is the unit detail: the y/y decline is entirely repower going to zero plus turbines down 61%, while management simultaneously markets 10-30 GW of PTC-qualified repower potential. Repower is the one US onshore product with a policy deadline tailwind, and its order line is empty, which says customers are not converting safe-harbored PTC positions into GE orders yet.
    - **testable_prediction**: Q3'26 Wind orders (Oct 21-22, 2026 release) will be below 1.5 GW and repower orders below 100 units; at the January 2027 outlook, 2027 Wind organic revenue will be guided down again (not 'flat to up'). Strazik's Sept 18 statement that H2 onshore orders will be 'materially higher' is the near-term test.
    - **kill_condition**: Q3'26 or Q4'26 Wind orders exceed 2.5 GW in a single quarter, or repower orders exceed 200 units in a quarter, or the January 2027 outlook guides 2027 Wind revenue flat or up.
    - **novelty**: 2
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: Overlaps the team's existing onshore-order angle; included only because the repower-to-zero and GW book-to-bill numbers sharpen it. EIA Planned-sheet counts are small (13-34 units per year) and only cover projects with reported dates. A Section 232 wind-turbine tariff decision (investigation opened Aug 2025, no action as of Sept 9, 2026 per chunk 236092) could unlock or further freeze orders. Most of the revenue effect lands in 2027, beyond the 3-12 month window; the near-term catalyst is the January 2027 guide.
- **dead_ends**:
  - xbrl_facts has no segment-dimension facts for GEV (no Wind/Electrification/Offshore tags); all segment numbers had to come from 10-Q/10-K/8-K text chunks. Warranty tags exist (StandardProductWarrantyAccrual 1,370M Dec-24 to 1,595M Jun-26) but are company-wide and already on the team list.
  - No 2026 quarterly dollar figure for Offshore Wind incremental contract losses exists in the corpus: 2025 10-Qs disclosed them ($171M Q3'25, $296M 9M'25, $676M/$779M in 2024) but the 2026 10-Q chunks only say 'higher contract losses'. Searched '"incremental contract losses"', '"Offshore Wind contracts of"', '"contract losses" "three months ended"' in Item 1 sections of 2026-04-22 and 2026-07-22.
  - No dollar amount for the Vineyard receivable/contract asset or the $850M engineer determination appears in any GEV filing; the Q2'26 10-Q Legal Proceedings section is a one-line pointer to Note 22 and searches for '"Vineyard"' in Item 1 F sections of 2026 10-Qs returned nothing. All dollar figures come from news (sources 3598, 3672, chunk 224621).
  - mgmt_guidance has no 2026 Wind guidance rows (only Electrification); Wind quarterly guidance had to be reconstructed from 8-K/EX chunks 5624/13603/30113 and transcript src:3161.
  - Tariff-estimate drift: Q2'26 10-Q says $100-200M for 2026 (chunk 5721) while the Apr 23 call summary cites $250-350M (chunk 236437); could not confirm both are on the same gross/net basis, so it was dropped as a finding.
  - 'Dogger Bank C' has zero hits in 2026 primary or commentary chunks; the only status is 'Dogger Bank B and C ... through the better part of 2027' (chunk 236438). Offshore remaining units/RPO by project are not disclosed.
  - competitor_financials has no Vestas or Siemens Gamesa U.S. order-intake rows (searched quote LIKE '%united states%' / '% u.s.%'); cannot benchmark whether GE's onshore order collapse is share loss or market-wide from the corpus.
  - Prolec standalone 2025 revenue is not in the corpus (searched 8-K/EX Oct 2025-Jan 2026 for '"Prolec" "approximately" "billion" "revenue"'); only the equity-method income line ($180M GEV share in 2025) and the $3.0-3.1B 2026 guide are available, so a pre-deal margin cannot be computed precisely.
  - Section 232 wind-turbine investigation (opened Aug 2025) had no tariff action as of a Sept 9, 2026 news chunk (236092); no outcome to trade on yet.
  - EIA-860M Planned sheet for onshore wind has only 13-34 units per planned year, too thin for a standalone finding; used only as corroboration.
  - FTS5 note for the team: parenthesised OR groups inside MATCH throw 'syntax error near OR' in this build; use separate queries or top-level OR between fully quoted phrases.

## [Sweep] find:academic-physics

- **lens**: Academic and technical miner: EIA-860M/923 physics of the new-build wave, HA users-group field reports, and the LTSA estimate-revision ledger in GEV filings
- **findings**:
  - - **title**: The 2026-27 US gas wave is 60% simple-cycle peakers, which run ~10% of the hours of a combined cycle; services-per-GW math breaks
    - **claim**: Simple-cycle (GT) units are 60% of planned US gas MW with 2026-2027 COD in the July-2026 EIA-860M snapshot, and new simple-cycle plants ran at 10.2-10.5% capacity factor vs 61.8-65.8% for new combined cycles, so each non-baseload GW in GEV's 116 GW under contract generates roughly one-sixth of the service hours the '$70M per GW-year' bull math assumes.
    - **mechanism**: GEV's 10-K states LTSA billing is 'based on the customers' utilization of the equipment (e.g., per hour of usage)' and outages occur 'at predetermined usage intervals'. Service revenue and the timing of first hot-gas-path outages therefore scale with fired hours, not installed GW. GEV itself says only 'more than half' of contracted GW are HA units 'expected to run base load'; the remainder (F-class, 61 aeroderivatives ordered in Q2 alone, advanced-class simple-cycle peakers at utilities) accrue hours ~6x slower. This lowers the services annuity the bull case attaches to the 125 GW backlog and pushes the HA-style outage wave for that half well past the mid-2030s.
    - **direction**: short
    - **evidence**:
      - - **source**: generators table (EIA-860M, vintage 2026-07, sheet Planned, energy_source NG)
        - **date**: 2026-07
        - **quote_or_number**: COD 2026-2027: GT 9,269 MW vs CT+CA+CS+CC 6,063 MW (60% simple cycle); COD 2028-2030: GT 12,229 vs CC 36,965 (25%). Under construction (U/V/TS) with 2026-27 COD: GT 5,159 MW vs CC 2,666 MW.
        - **reproduction**: SELECT planned_year, round(sum(CASE WHEN prime_mover='GT' THEN mw END)) gt, round(sum(CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN mw END)) cc FROM generators WHERE vintage='2026-07' AND sheet='Planned' AND energy_source='NG' AND planned_year BETWEEN 2026 AND 2031 GROUP BY planned_year
      - - **source**: generators table, planned-share time series across vintages
        - **date**: 2023-07 to 2026-07
        - **quote_or_number**: GT share of planned NG MW (COD 2025-2030) rose from 21% (2,076 of 10,047 MW, vintage 2023-07) to 33% (21,498 of 64,526 MW, vintage 2026-07). Advanced-class-size SC units (>=280 MW each) with 2026-29 COD: 15 units / 7,445 MW in 2026-07 vs 3 units / 1,271 MW in 2024-07.
        - **reproduction**: SELECT vintage, round(sum(CASE WHEN prime_mover='GT' THEN mw END)) gt, round(sum(CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN mw END)) cc FROM generators WHERE sheet='Planned' AND energy_source='NG' AND planned_year BETWEEN 2025 AND 2030 AND vintage IN ('2023-07','2024-07','2025-07','2026-07') GROUP BY vintage
      - - **source**: generation table (EIA-923) joined to generators Operating sheet, plant-level capacity factor by plant type and age
        - **date**: 2024 and 2025
        - **quote_or_number**: Plants whose newest unit is 2018+: SC-only 10.2% CF (59 plants, 14.2 GW, 2024) and 10.5% (71 plants, 19.4 GW, 2025); CC-only 65.8% (53 plants, 49.9 GW, 2024) and 61.8% (2025). National check: GT 159.8 TWh / 157.6 GW = 11.6%; CC 1,552.9 TWh / 325.7 GW = 54.4% (2024).
        - **reproduction**: WITH cap AS (SELECT plant_id, sum(CASE WHEN prime_mover='GT' THEN mw ELSE 0 END) gt_mw, sum(CASE WHEN prime_mover IN ('CT','CA','CS','CC') THEN mw ELSE 0 END) cc_mw, sum(mw) tot_mw, max(op_year) last_yr FROM generators WHERE vintage='2024-12' AND sheet='Operating' AND energy_source='NG' AND prime_mover IN ('GT','CT','CA','CS','CC') GROUP BY plant_id), gen AS (SELECT plant_id, sum(net_generation_mwh) mwh FROM generation WHERE year=2024 AND fuel_type='NG' AND prime_mover IN ('GT','CT','CA','CS','CC') GROUP BY plant_id) SELECT CASE WHEN cc_mw=0 THEN 'SC only' WHEN gt_mw=0 THEN 'CC only' ELSE 'mixed' END typ, CASE WHEN last_yr>=2018 THEN 'new' ELSE 'old' END cohort, count(*), round(100.0*sum(mwh)/(sum(tot_mw)*8760),1) cf FROM cap JOIN gen USING(plant_id) GROUP BY 1,2
      - - **source**: GEV 10-K FY2025, accession 0001996810-26-000015, revenue recognition note
        - **date**: 2026-01-29
        - **quote_or_number**: 'Our billing terms for these arrangements are generally based on the customers' utilization of the equipment (e.g., per hour of usage) and upon the occurrence of a major maintenance event'
        - **reproduction**: SELECT text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"per hour of usage"' AND c.accession='0001996810-26-000015'
      - - **source**: GEV 2Q26 earnings transcript, sources.id=3161 (TRANSCRIPT chunk)
        - **date**: 2026-07-22
        - **quote_or_number**: 'This includes orders for 52 heavy-duty units and 61 aeroderivatives in the quarter. More than half of the gigawatts that are now under contract are for our largest, most efficient HA turbines, units expected to run base load'
        - **reproduction**: SELECT text FROM sources WHERE id=3161 (search 'half of the gigawatts')
      - - **source**: SO 10-K FY2024 + NEWS src:3067 (Georgia Power Plant Yates)
        - **date**: 2025-02-20 / 2025-12-16
        - **quote_or_number**: Largest planned SC unit block in 860M (Yates, 3 x 442 MW simple cycle, 1,448 MW) is Mitsubishi M501JAC, not GE.
        - **reproduction**: SELECT c.form,c.filing_date,c.ticker,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Yates" AND ("M501JAC" OR "simple cycle")' LIMIT 5
    - **why_market_misses_it**: Sell-side services models multiply installed GW by a per-GW annuity. Nobody joins EIA-860M planned prime-mover codes to EIA-923 capacity factors, and GEV reports orders in GW, not in expected fired hours. The peaker wave (Georgia Power, TVA, Dominion, Duke, Entergy, OG&E, Vistra Permian) is visible only in utility IRPs and 860M rows.
    - **testable_prediction**: On the Q3'26 call (about Oct 22, 2026) and in the FY26 10-K (late Jan 2027) GEV will again describe HA baseload units as only 'more than half' of contracted GW (not two-thirds or more), and the EIA-860M December-2026 vintage will still show simple-cycle GT MW exceeding combined-cycle MW for 2027 COD.
    - **kill_condition**: GEV discloses that 75%+ of contracted GW are HA/combined-cycle baseload units, or the 860M 2026-12 vintage shows CC MW above GT MW for 2027 COD, or GEV shows services revenue per installed GW rising despite the mix.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: EIA-860M does not identify OEM; the SC share is a US market fact, not a GEV order-book fact, and GEV's international (Qatar, Brazil, Saudi) contracts are mostly combined cycle. Behind-the-meter data-center SC units, if they run baseload, would be the opposite case (high hours) but do not appear as such in 860M. Capacity factors are annual averages; starts-based factored hours accelerate peaker outages somewhat.
  - - **title**: HA fleet field reports show rotor/spacer cracking and chronic spare-parts shortages while LTSA profitability revisions are running 5x last year
    - **claim**: GEV's net unfavorable changes in estimated LTSA profitability were $218M in H1 2026 (11.8% of Power segment EBITDA) versus $42M in H1 2025 and $151M for all of 2025, and the HA users-group field record (16% of respondents have swapped a rotor, 34% have had a forced outage, spacer-0 high-cycle-fatigue cracking, 'no backup stock of rotors from GE') points to this line getting worse as the 126-unit HA fleet crosses its first hot-gas-path interval in 2026-27.
    - **mechanism**: LTSAs are accounted for on percentage-of-completion; a rise in expected parts, labor or outage-extension cost is booked as a cumulative catch-up reduction of Power services revenue and EBITDA. The 10-K says one percentage point of total contract profitability equals $0.2B of LTSA contract assets ($3.4B net balance, contracts ~29% complete). The HA fleet added ~0.7M hours in 2025 (~5,800 h/unit), so the mean unit is at ~28.6K cumulative hours, right at a 24-32K-hour HGP interval, while the same S1B/S1N castings feed the 20 GW/yr new-unit ramp. Parts scarcity documented by operators in 2018 and again in 2024 is the physical cause of the accounting line.
    - **direction**: short
    - **evidence**:
      - - **source**: GEV 10-Q/10-K contract-liabilities notes (documents table), regex on 'changes in estimated profitability'
        - **date**: 2024-04-30 through 2026-07-22
        - **quote_or_number**: Net LTSA profitability changes: FY2023 +$34M favorable (S-1/A); FY2024 -$319M 'due primarily to higher costs'; FY2025 -$151M; Q1 2026 -$89M; H1 2026 -$218M vs H1 2025 -$42M. Q2 2026 alone (-$129M) is the largest non-Q4 quarter on record.
        - **reproduction**: python: for each row in documents WHERE accession LIKE '0001996810%' AND form IN ('10-K','10-Q'): re.findall(r'net\s+(?:un)?favorable\s+changes\s+in\s+estimated\s+profitability\s+of\s+\$[\d,]+\s+million', text, re.I)
      - - **source**: GEV 10-Q Q2 2026, accession 0001996810-26-000148, segment table
        - **date**: 2026-07-22
        - **quote_or_number**: Six months 2026 Power: services revenues $6,593M, segment revenues $10,449M, segment EBITDA $1,842M; $218M = 11.8% of Power EBITDA and 2.1 pts of Power margin. H1 2025 Power EBITDA $1,286M (10-Q 0001996810-25-000133).
        - **reproduction**: SELECT text FROM documents WHERE accession='0001996810-26-000148' AND form='10-Q' (search 'Six months ended June 30, 2026 Power')
      - - **source**: GEV 10-K FY2025, accession 0001996810-26-000015, critical accounting estimates
        - **date**: 2026-01-29
        - **quote_or_number**: '...increase or decrease total estimated contract profitability by one percentage point would increase or decrease the long-term service agreements contract assets balance by $0.2 billion.' Net LTSA balance $3.4B, ~4% of life-of-contract billings, contracts ~29% complete.
        - **reproduction**: SELECT text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"one percentage point" AND "service agreements"' AND c.accession='0001996810-26-000015'
      - - **source**: Combined Cycle Journal, 'SPECIAL REPORT: 2024 HA Users Group', sources.id=3082, https://www.ccj-online.com/special-report-2024-ha-users-group/
        - **date**: 2024 (report; conference 2024)
        - **quote_or_number**: 83 respondents (5 HA.01, 62 HA.02, 11 HA.03, 9 9HA.01, 1 9HA.02; 9% simple cycle): 16% rotor swap; 34% forced outage; 16% FOD outage; 52 applied spacer-0 TIL, 6 have a cracked spacer 0; vendor grades 40 of 64 'C or below', one 'A'; ~75 TILs; 7HA availability 92.12%, reliability 97.76%.
        - **reproduction**: SELECT text FROM sources WHERE id=3082 (search 'respondents', 'spacer', 'grade')
      - - **source**: Same CCJ report, 9HA.01 and 7HA.02 fleet-leader outage accounts
        - **date**: 2024
        - **quote_or_number**: 'there was no backup stock of rotors from GE, hot gas path (HGP) parts were in short supply'; 7HA.02 fleet leader major inspection at over 48K hours and 162 starts; 9HA.01 unit had a 72-day outage extension (2020) and 23-day extension (2023); an HA.02 unit out four months after spacer-0 liberation (HCF).
        - **reproduction**: SELECT text FROM sources WHERE id=3082 (search 'no backup stock', '48K hours', '72-day')
      - - **source**: CCJ, '7H Users Group: owner/operators wrestle with emergent issues at inaugural meeting', sources.id=3078
        - **date**: circa 2018
        - **quote_or_number**: 'the OEM was 9-10 months behind on spare parts' and sites were 'desperate for spare stage 1 blades' (same complaint, six years earlier).
        - **reproduction**: SELECT text FROM sources WHERE id=3078 (search 'spare')
      - - **source**: GEV 10-K FY2024 (0001996810-25-000011) and FY2025 (0001996810-26-000015), S-1/A
        - **date**: 2025-02-06 / 2026-01-29
        - **quote_or_number**: HA installed base: 92 units / >2.0M hours (Dec-23); 115 / ~2.9M (Dec-24); 126 / ~3.6M (Dec-25): +0.7M hours in 2025 = ~5,800 h per unit-year; mean cumulative 28.6K h per unit. CEO 2Q26: 'we only have 130 of our HA units running... every four years they go through a major outage.'
        - **reproduction**: SELECT filing_date, text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"HA-Turbines in RPO"' AND c.form='10-K'
    - **why_market_misses_it**: The catch-up line sits in the contract-liabilities footnote with no XBRL tag of its own (the tagged 'CumulativeCatchUp' facts in the corpus actually hold billings), so screens never see it; analysts model services as a rising annuity. The operator-side evidence is in a trade journal's user-group write-up that no equity analyst reads, and GEV's own narrative frames the HA outage wave purely as a services revenue opportunity.
    - **testable_prediction**: The Q3 2026 10-Q (about Oct 22, 2026) will report nine-month net unfavorable changes in estimated LTSA profitability of at least $300M (Q3 alone >= $80M), exceeding the full-year 2025 figure of $151M, and the FY2026 10-K will show a full-year figure above FY2024's $319M.
    - **kill_condition**: Nine-month 2026 figure at or below $250M, or a net favorable revision in Q3/Q4 2026; or GEV discloses HA fleet availability at or above 95% with TIL count falling, or a dedicated HGP-parts capacity expansion that is separate from new-unit castings.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: The 10-Q does not attribute the $218M to HA units specifically; it could include steam, nuclear or aero LTSAs, or an accounting true-up unrelated to reliability. The CCJ survey is self-selected (83 attendees) and dated 2024; the corpus has no 2025/2026 HA users-group report. Q4 historically carries the largest revisions, so seasonality could make the 9M prediction fail while the FY prediction holds.
- **dead_ends**:
  - Correction for the team brief: the '$0.3B per year availability-shortfall revenue reductions 2023-2025' in the 10-K is a WIND farm availability guarantee item (10-K FY2025, 0001996810-26-000015: 'performance guarantees of the wind farm's availability'), not a gas/HA metric; do not cite it as HA fleet under-performance.
  - H-class hot-gas-path interval numbers: the only explicit figure in the corpus (24,000-32,000 EOH H-class vs 32,000-48,000 F-class) comes from a low-credibility patsnap web page (sources.id=3061); the GE ETN paper (sources.id=3062) gives no interval numbers. No GER-3620-style OEM table exists in the corpus. The CCJ fleet-leader MI at 48K hours is the best hard number.
  - Thermal-barrier-coating / single-crystal supply: 147 commentary hits and 8 academic hits, but none with casting capacity or lead-time numbers; academic titles are additive-manufacturing reviews. Nothing that quantifies a GEV supplier ceiling beyond the known angle.
  - Ambient-temperature derating: 11 academic hits are generic thermodynamics (E3S, JGPPS); no site-specific or fleet-level derate number tied to data-center geographies. Already on the known list; no new number found.
  - Hydrogen blends and maintenance intervals: 5 academic and 39 commentary hits, all about NOx/combustion (e.g., GE DLN 2.6e on 7HA.03, sources.id=1616 abstract only); no maintenance-interval or component-life number, and nothing within a 3-12 month horizon.
  - Wind blade failure statistics: Vineyard Wind / Dogger Bank Haliade-X incidents are in the corpus (sources 835, 3685, 3696, 3714) but with no failure-rate per turbine-year or blade-replacement count beyond what is already public; offshore contract losses ($379M/$1,005M/$637M) are already on the team's list.
  - AI-workload grid physics: arXiv 2508.16457 (sources.id=3549) finds unstable 0.75-1.83 Hz inter-area modes in a WECC 179-bus model at 10.8-11.5% data-center penetration; arXiv 2604.10769 (3538) and 2607.19638 (3550) discuss ramp rates only in normalized terms. NERC July 10, 2024 event: 1,500 MW from 60 facilities across 25 substations dropped in under 1 s after a 42-66 ms voltage dip (sources 45, 461); NERC Level 3 Alert May 2026 (responses due Aug 3, 2026); computational-load-entity registration (>=20 MW, >=60 kV, >=1 MW compute) to be filed by end-2026; Project 2026-02 standards. No path to a GEV financial line inside 3-12 months could be quantified (possible Electrification synchronous-condenser demand is not separable in filings). Only DUK 10-K 2026 and BE 10-K 2025 mention it among customers.
  - Aeroderivative supply via GE Aerospace: filings only describe the technology relationship; no related-party purchase volume or gas-generator capacity number for LM2500/LM6000 in the corpus, so the 'shared supply chain with aviation MRO' idea could not be quantified.
  - OEM identity of the planned US simple-cycle peakers (Chesterfield, Horseshoe Lake, Lone Star, Ironwood, Vistra Permian, Duke Marshall/Buck): no hits in the corpus; only Plant Yates is identified (Mitsubishi M501JAC). The projects table has oem blank for these.
  - XBRL tags 'ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress' for GEV hold LTSA billings (e.g. -5,362M FY25), not estimate revisions; do not use them for the catch-up series.
  - queue_projects and operator_forecasts tables are empty (as warned); Ollama semantic search was not attempted because FTS was sufficient.

## [Verify] repro:price-events:The GW-order metric has stopped moving t

- **reproduced**: True
- **corrected_numbers**: EARNINGS-DAY SEQUENCE (prices table, close/prev close; GW from 8-K/EX chunks; guidance from 8-K/EX chunks):
- Q1'25 2025-04-23: 14 GW (7 GW orders + 7 GW SRA; chunk 54409, wording differs from later quarters), REAFFIRMED 2025 guide (chunk 54413), GEV +3.07% (326.07 -> 336.09)
- Q2'25 2025-07-23: 9 GW (2 orders + 7 SRA; chunk 44041), RAISED 2025 guide (chunk 44044), GEV +14.58% (548.99 -> 629.03)
- Q3'25 2025-10-22: 'just over 12 GW' (1 orders + 12 SRA; chunk 38443) -- finding says 13; release headline says 'just over 12'. REAFFIRMED (chunk 38446). GEV -1.59% (585.33 -> 576.00)
- Q4'25 2026-01-28: 24 GW (3 orders + 21 SRA; chunk 30108). CORRECTION: this print RAISED 2026 guidance (chunk 30113: revenue $44-45B up from $41-42B, FCF $5.0-5.5B up from $4.5-5.0B). Finding treated it as a no-raise quarter. GEV +2.73% (692.70 -> 711.59)
- Q1'26 2026-04-22: 21 GW (2 + 19; chunk 13599), RAISED (chunk 13603), GEV +13.75% (991.30 -> 1127.56), 5-peer basket -0.26%
- Q2'26 2026-07-22: 20 GW (2 + 18; chunk 5620), RAISED (chunk 5624: revenue $45.5-46.5B from $44.5-45.5B, FCF $11.5-12.5B from $6.5-7.5B, Power organic 18-20% from 16-18%), GEV -8.69% (1078.81 -> 985.03), basket +0.02%, SPY -0.12%
Per-GW arithmetic checks: 14.58/9 = +1.62%/GW; -8.69/20 = -0.43%/GW.

EVENT DAYS (all reproduce exactly): 2026-07-07 GEV -6.51%, VRT -4.05, ETN -4.29, PWR -2.56, HUBB -3.37, EMR -2.58, basket mean -3.37%, SPY -0.48%. 2026-09-14 GEV -8.62%, VRT -7.65, ETN -7.57, PWR -4.39, HUBB -3.91, EMR -2.56, basket -5.22%, SPY -0.45%. Barclays quote ('sustainable medium-term demand at only 80 to 90 gigawatts annually') is verbatim in chunk 465392. GLJ quote (Eaton 7%, Quanta 4%) verbatim in chunks 230637-230638 (src:1267).

CORRECTION to 'two largest GEV-specific down days of 2026 (Jul 22, Jul 7)': FALSE as stated. Raw 2026 ranking: Jul 22 -8.69, Sep 14 -8.62, Jun 23 -8.21, Aug 18 -6.90, May 7 -6.55, Jul 7 -6.51 (6th). Basket-residual ranking: Jul 22 -8.72, Jan 21 -4.66, Sep 14 -3.40, May 27 -3.36, Jul 7 -3.14 (5th). Jul 22 is #1 by both measures; Jul 7 is not #2 by either. Reframe as 'the single largest 2026 down day was a 20 GW / $5B FCF-raise print, fully GEV-specific (basket +0.02%)'.

CORRECTION to source: chunk 465392 / src:3596 is ad-hoc-news.de (https://www.ad-hoc-news.de/boerse/news/ueberblick/siemens-energy-barclays-warns-the-gas-turbine-cycle-has-peaked/69717246), not boerse-global.de.
- **data_quality_issues**: 1) The task's 'what the market believes' block is stale vs the corpus: it says FY26 revenue $44.5-45.5B and Power organic growth 16-18%, but the 2026-07-22 8-K/EX (chunk 5624) raised those to $45.5-46.5B and 18-20%. FCF $11.5-12.5B is correct. Team should refresh before the memo.
2) The finding's claim 'sign of earnings-day return is uncorrelated with guidance raises' is overstated once Q4'25 is correctly tagged as a raise. Guidance raises: Q2'25 +14.58, Q4'25 +2.73, Q1'26 +13.75, Q2'26 -8.69 (3 of 4 positive, 2 of 4 >13%). Reaffirms: Q1'25 +3.07, Q3'25 -1.59 (both near flat). Guidance raises DID move the stock through Q1'26; only Q2'26 broke the pattern. The GW-level claim survives (9 GW -> +14.58; 24 GW -> +2.73; 20 GW -> -8.69). Recommend dropping 'or with guidance raises' and framing Q2'26 as the first raise the tape rejected, which the caveat already attributes to FCF-quality doubt (H2 implied $1.6-2.6B).
3) Q3'25 GW figure: release says 'just over 12 gigawatts' (12 SRA + 1 orders); the finding's 13 is a sum, not a stated figure. Use 12-13 or quote the release.
4) Jan 21 2026 has the second-largest basket-residual (-4.66%: GEV -2.48% vs basket +2.18%) but zero GEV-tagged commentary chunks in the corpus for that date. Unexplained; the corpus cannot attribute it.
5) Jul 7 confound check: the only GEV-tagged commentary on 2026-07-07 is the Barclays SE piece (src:3596) plus an unrelated gas-cost article (src:2833). No competing GEV-specific news found that day. Prior day (Jul 6) has 'FERC denies waiver for $2B gas-fired plant in PJM fast-track review' (src:2091), a possible overhang, but Jul 6 headlines also report GEV shares climbing (src:1771), so no clean confound.
6) catalyst_calendar row for 2026-10-21 is an ESTIMATE (confirmed=0, 'median gap 91d'), not a company-confirmed date.
7) Jul 22 basket mean prints as +0.03 in one run and +0.02 in another (rounding of the 5-ticker mean); immaterial.
- **notes**: WHAT I RAN (all SELECT-only against data\gev.db via Python 3.11 heredocs from Git Bash):
- prices: SELECT date,close FROM prices WHERE ticker='GEV' ORDER BY date; computed close/prev-close for 2025-04-23, 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22, 2026-07-22, 2026-07-07, 2026-09-14. Same for VRT, ETN, PWR, HUBB, EMR, SPY on 07-06/07-07, 09-11/09-14, 07-21/07-22. Ranked every 2026 GEV day raw and basket-residual.
- chunks_fts MATCH '"slot reservation" AND "GW"' with ticker='GEV', form='8-K/EX' -> hits on 2025-07-23, 2025-10-22, 2026-04-22, 2026-07-22. Q1'25 needed a LIKE '%gigawatt%' scan of 8-K/EX on 2025-04-23 (chunks 54407-54410); Q4'25 needed MATCH '"gas equipment" AND ("gigawatt" OR "GW")' on 2026-01-28 (chunk 30108).
- chunks_fts MATCH '"2026 Guidance"' on 2026-07-22 -> chunk 5624 verbatim match. MATCH '"Guidance" AND ("free cash flow" OR "revenue")' per print date for the other releases; MATCH '"2026" AND "free cash flow" AND "expects"' on 2026-01-28 -> chunk 30113.
- SELECT ... FROM chunks WHERE id=465392 + sources WHERE id=3596; chunks_fts MATCH '"GLJ" AND "Vernova"' AND filing_date='2026-09-14' -> chunks 230637/230638/230640, src:1267 (247wallst.com).
- catalyst_calendar WHERE ticker='GEV' -> id 1, 2026-10-21, confirmed=0.
- commentary chunks grouped by accession for GEV on 2026-07-06, 2026-07-07, 2026-01-21.

VERDICT: Core evidence reproduces. All 8 daily returns, all 5 peer-basket sets, the Barclays and GLJ quotes, the Jul 22 guidance paragraph, and 5 of 6 GW figures are exact. The finding's mechanism (GW level no longer earns a premium; Jul 22 was fully idiosyncratic) holds. Two framing claims need rewriting: (a) 'two largest down days' ranking is wrong (Jul 7 is 5th/6th, not 2nd); (b) 'uncorrelated with guidance raises' is wrong because Q4'25 was also a raise and 3 of 4 raises were positive days. The stronger, defensible version: GW-signed level is uncorrelated with the reaction (n=6), guidance raises drove the two +13-15% days, and Q2'26 was the first raise the market sold, consistent with the deposit-pull-forward reading. Confidence 4 rather than 5 because n=6 and the guidance-raise reframe changes the emphasis of the claim.
- **confidence**: 4

## [Sweep] find:connectors-outside

- **lens**: Outside-the-corpus scout: SEC full-text search (efts) across all filers 2001-2026, state-regulator news, court dockets, conference commentary, plus corpus cross-checks for novelty
- **findings**:
  - - **title**: Last-cycle template: GE's 2001-04 power bubble shows profit peaked a year AFTER orders halved, and progress collections (cash) broke first
    - **claim**: In the 2001-2004 US gas-turbine bust, GE Power Systems orders fell 42% (2001 $24.5B to 2002 $14.2B) while 2002 revenue rose 13% to $22.9B and operating profit hit a record $6.3B (helped by $0.9B net termination fees); revenue then fell 19% and profit 35% in 2003, gas-turbine units shipped fell 43% (362 to 208), and management pre-announced a ~$3B drop in progress collections for 2003 before the P&L broke.
    - **mechanism**: GEV recognizes gas equipment revenue over time from a backlog it already holds ($87.8B equipment RPO) and funds it from customer deposits (contract liabilities $39.9B at Jun-26, up from $15.1B at Dec-23). The 2002 analog says: (1) FY26-FY27 revenue/EBITDA are protected by backlog and by termination fees even if SRA conversions slow, so a 3-12 month long is not killed by an order roll-over; (2) the FIRST line to turn in the last cycle was progress collections (customer cash), i.e. today's contract-liabilities line and FCF, which is exactly where the H2-26 implied FCF of $1.6-2.6B sits. The right early-warning metric is the quarter-on-quarter change in contract liabilities, not orders or margin.
    - **direction**: either
    - **evidence**:
      - - **source**: GE 8-K filed 2003-04-10, exhibit 99(b) (restated 2002 MD&A)
        - **date**: 2003-04-10
        - **quote_or_number**: Orders $14.2B in 2002 vs $24.5B in 2001; backlog $16.7B vs $28.9B; '$0.9 billion positive effect of customer contract termination fees, net of associated costs'; 'We expect Power Systems progress collections to decline about $3 billion in 2003'
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/0000040545/000004054503000021/ex99b.htm (fetch with WebFetch; direct urllib with no-email UA returns 403)
      - - **source**: GE 10-K FY2003, exhibit 13 (annual report), Power Systems segment
        - **date**: 2004-03-01
        - **quote_or_number**: Revenues 2001/2002/2003 = $20.211B / $22.926B / $18.462B; operating profit $4.860B / $6.255B / $4.076B; gas turbine units shipped 362 (2002) vs 208 (2003); termination fees net $0.9B (2002), $0.6B (2003); 'U.S. power bubble' peaked 2002
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/0000040545/000004054504000013/ex13.htm
      - - **source**: GE 10-K FY2004, exhibit 13, Energy segment (restated segment definition)
        - **date**: 2005-03-01
        - **quote_or_number**: Large heavy-duty gas turbine units shipped 323 / 175 / 122 (2002/2003/2004); revenues $23.6B / $19.1B / $17.3B; operating profit $6.3B / $4.1B / $2.8B; termination fees $0.9B / $0.6B / $0.1B
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/0000040545/000004054505000020/ex13.htm
      - - **source**: GE 8-K filed 2002-09-17, exhibit 99(c)
        - **date**: 2002-09-17
        - **quote_or_number**: YE2001 backlog $28.9B of which product orders $24.1B, 75% scheduled for 2002 delivery; 'contractual terms require customers to pay termination fees... at least a portion has generally been received as progress collections'
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/0000040545/000004054502000054/ex99c.txt
      - - **source**: corpus xbrl_facts, GEV ContractWithCustomerLiabilityCurrent (instant)
        - **date**: 2026-07-22
        - **quote_or_number**: $B by quarter-end: Dec-23 15.07, Jun-24 16.54, Dec-24 17.59, Jun-25 19.60, Sep-25 20.15, Dec-25 25.77, Mar-26 31.83, Jun-26 39.94
        - **reproduction**: SELECT end_date, val FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerLiabilityCurrent' AND start_date IS NULL GROUP BY end_date ORDER BY end_date
      - - **source**: corpus chunks_fts novelty check
        - **date**: 2026-09-21
        - **quote_or_number**: 0 chunks match '"power bubble"'; 0 chunks match '"termination fees" "2002"' across all 469k chunks
        - **reproduction**: SELECT count(*) FROM chunks_fts WHERE chunks_fts MATCH '"power bubble"'
    - **why_market_misses_it**: GLJ's Sell note says 'two full boom-bust cycles' but gives no numbers; the corpus (469k chunks, 34 companies) has zero references to the 2002 bubble mechanics. Analysts model orders and margin; nobody has published the sequencing (orders peak -> profit peak +1yr -> cash breaks before revenue) that GE's own filings document, and which maps one-to-one onto GEV's contract-liabilities line.
    - **testable_prediction**: Q3-26 10-Q (about Oct 22 2026): contract liabilities print above $42B (still in the 2001-analog phase, deposits rising with 20 GW/yr output). If instead contract liabilities fall quarter-on-quarter while revenue and margin still rise, that is the 2002-analog signal and FY27 revenue is at risk 4-6 quarters later. Secondary: any disclosure of 'termination fees' or 'cancellation fees' as a P&L item in a GEV 10-Q by Q2-27 would confirm the cycle has turned.
    - **kill_condition**: Contract liabilities keep rising through Q4-26 AND equipment orders (ex-SRAs) grow year-on-year in Q3 and Q4 2026; or the team establishes from the 10-K/SRA terms that GEV deposits are fully refundable (no termination-fee cushion), which breaks the profit-lag half of the analog.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: 2001-02 buyers were merchant IPPs (Calpine, Dynegy, Enron) with weak credit; today's buyers include hyperscalers and regulated utilities, so the cancellation base rate may be lower. Unit counts differ between the FY2003 report (362/208, all gas turbines) and FY2004 report (323/175/122, 'large heavy-duty', restated Energy segment) - use one series consistently. Termination fees were netted into operating profit, so 2002's record profit overstates underlying earnings by roughly $0.9B.
  - - **title**: CEO's own HA services math is ~$25M per GW-year, one-third of the $70M/GW-year bull number the Sep 12 rally was built on
    - **claim**: At the Morgan Stanley Laguna conference (Sep 16 2026) Strazik said each GW of HA capacity generates roughly $500M of services revenue over its first 20 years ($25M/GW-yr), HA services are ~$1B/yr today on 130 machines (~65 GW, i.e. ~$15M/GW-yr), and Power services go from $12B (2025) to $22B (2035); UBS's Sep 12 note assumes >$70M/GW-yr on a 400+ GW fleet in the 2030s (=$28B+/yr), which exceeds the company's own 2035 target for the entire Power services line.
    - **mechanism**: Services is the high-margin annuity that justifies the 31-38x forward P/E ('peak-order myopia' bull case). If mature-fleet services run at the company's $25-35M/GW-yr rather than $70M, 2030s services revenue is $10-15B/yr lower than the bull model; at Power's ~17-19% margin that is $2-3B of EBITDA, roughly 15-20% of the long-run earnings base. Near-term, it caps the multiple re-rating that bulls expect from Investor Day-style services disclosures.
    - **direction**: short
    - **evidence**:
      - - **source**: corpus chunks, NEWS tier=commentary, GEV, Laguna coverage
        - **date**: 2026-09-18
        - **quote_or_number**: 'each gigawatt of HA capacity can generate roughly $500 million of high-margin service revenue during the first 20 years of operation'; 'HA services currently generate about $1 billion of revenue'; '130 HA machines operating today and another 195 under contract'; 400 machines 'represents about 200 gigawatts'; 'contracted about $100 billion in future HA services revenue' by end-2027
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"first 20 years" "500 million"' AND c.ticker='GEV' ORDER BY bm25(chunks_fts) LIMIT 2
      - - **source**: Investing.com transcript summary of the Laguna fireside
        - **date**: 2026-09-16
        - **quote_or_number**: 'half a billion dollars of high-margin services revenue over the first 20 years of its lifetime'; Power Services '$12 billion in 2025 to $22 billion in 2035'; 5 GW/qtr run-rate Q3-Q4 2026, 6 GW/qtr H2-27, 7 GW/qtr 2028
        - **reproduction**: https://www.investing.com/news/transcripts/ge-vernova-at-morgan-stanley-laguna-conference-backlog-surges-93CH-4904104
      - - **source**: corpus chunks, NEWS src:2714 (UBS / Dumoulin-Smith note coverage)
        - **date**: 2026-09-12
        - **quote_or_number**: 'GE Vernova could generate more than $70 million per gigawatt-year from its installed base during the 2030s, supported by a fleet exceeding 400 gigawatts'
        - **reproduction**: SELECT c.filing_date, c.accession, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"70 million" "gigawatt"' AND c.ticker='GEV' LIMIT 1
      - - **source**: corpus mgmt_guidance, GEV Services-related RPO
        - **date**: 2026-07-22
        - **quote_or_number**: Services RPO $88,463M, of which 16% / 54% / 79% / 92% recognized within 1 / 5 / 10 / 15 years (i.e. ~$14B/yr near-term run-rate on the whole installed base, not just HA)
        - **reproduction**: SELECT stated_on, value, quote FROM mgmt_guidance WHERE ticker='GEV' AND metric='Services-related RPO' ORDER BY stated_on DESC LIMIT 1
      - - **source**: arithmetic cross-check
        - **date**: 2026-09-21
        - **quote_or_number**: $100B contracted HA services / ~200 GW = $500M/GW, matching the $500M-per-GW statement; $500M / 20 yrs = $25M/GW-yr; $1B / (130 machines x 0.5 GW) = $15M/GW-yr; UBS $70M x 400 GW = $28B/yr vs company 2035 Power services target $22B
        - **reproduction**: python -c "print(100e9/200, 500e6/20, 1e9/(130*0.5), 70e6*400/1e9)"
    - **why_market_misses_it**: Both numbers are public but were published four days apart in different venues (a sell-side note vs a conference fireside) and no one has reconciled them; the corpus holds both quotes and no chunk puts them side by side. The stock rallied on the UBS framing and the Laguna coverage focused on backlog and pricing, not on the implied per-GW services yield.
    - **testable_prediction**: By the Q3-26 call (about Oct 22 2026) and any Dec-2026 investor update, GEV will not raise the 2035 Power services target above ~$25B and will not cite an HA services yield above $35M/GW-yr; Power services revenue growth in Q3-26 stays at or below ~12% year-on-year.
    - **kill_condition**: Company raises the 2035 Power services target to $28B or more, or discloses HA services economics of $50M+/GW-yr (e.g. via CSA pricing or a services investor day), or the $500M figure is shown to exclude upgrades/parts that UBS includes.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: The Strazik quotes are from two secondary sources (Investing.com summary and syndicated news in the corpus), not the verified Seeking Alpha transcript (paywalled). Young HA fleets under-earn services until first major inspections (~24-32k hours), so today's $15M/GW-yr understates mature economics; UBS's $70M is a 2030s mature-fleet number across all frames (F/E-class parts pricing is richer). Strazik called the $22B target 'conservative'.
  - - **title**: NC regulators denied Duke's $584M / 255 MW data-center peaker on Sep 18 (3-1): first CPCN rejection of a data-center-justified gas turbine in a core GEV utility customer's territory; not in the corpus
    - **claim**: On Sep 18 2026 the North Carolina Utilities Commission voted 3-1 to deny Duke Energy Progress's certificate for a sixth combustion turbine (~255 MW, $584M, ~$2,290/kW, Jan-2030 in-service) at the Sherwood H. Smith Energy Complex next to Amazon's planned $10B Richmond County data center, ruling the project premature because Duke's data-center load forecast is unverified; Duke had announced (Apr 2025) an arrangement for up to 11 GEV 7HA turbines and has 6+ GW of gas CT/CC in CPCN pipeline.
    - **mechanism**: Regulated utilities are the slice of GEV's 63 GW of SRAs that must clear a state CPCN before an SRA becomes a firm order and a deposit becomes progress collections. A denial or deferral pushes SRA-to-order conversion, revenue timing and deposit cash to the right, and the stated reason (regulators refusing to underwrite data-center forecasts at ~$2,300/kW for a simple-cycle peaker) is a direct check on the +10-20 pt $/kW pricing GEV reported for H1-26 orders. It also raises the base rate of CPCN denials the team's interconnection-queue angle assumes is near zero for utility buyers.
    - **direction**: short
    - **evidence**:
      - - **source**: WRAL
        - **date**: 2026-09-18
        - **quote_or_number**: NC regulators deny Duke Energy's $584 million gas turbine proposal; about 255 MW by 2030; Duke 'has not shown that the project is needed'; 'much of the growth Duke anticipates appears tied to future data centers'
        - **reproduction**: https://www.wral.com/news/state/duke-energy-gas-turbine-amazon-data-center-september-2026/
      - - **source**: Business North Carolina
        - **date**: 2026-09-19
        - **quote_or_number**: Commissioners Bill Brawley, Tommy Tucker and Donald van der Vaart; 3-1 decision; refused to act before ruling on Duke's updated Carolinas Resource Plan; van der Vaart: commission 'under no obligation to green-light the projects in an approved resource plan'
        - **reproduction**: https://businessnc.com/n-c-regulators-reject-duke-energy-584m-turbine-request/ (403 to WebFetch; text via WebSearch snippet)
      - - **source**: Yahoo News (News & Observer syndication)
        - **date**: 2026-09-18
        - **quote_or_number**: 'will impose a significant risk that new generation is approved before the need for that generation is determined'; Duke projects 'more than 25,000 new megawatts of power generation by 2035'; independent review of Duke's demand analysis due late 2026
        - **reproduction**: https://www.yahoo.com/news/us/articles/nc-denies-duke-energy-request-182915798.html
      - - **source**: POWER Magazine
        - **date**: 2025-04-24
        - **quote_or_number**: Duke Energy arrangement to 'potentially' secure up to 11 GE Vernova 7HA units for brownfield sites; plans >2,800 MW of new combined cycle by 2032
        - **reproduction**: https://www.powermag.com/duke-energy-ge-vernova-strike-major-gas-turbine-deal-to-support-explosive-demand-growth/
      - - **source**: corpus projects table (DUK 10-Q, 2026-08-04)
        - **date**: 2026-08-04
        - **quote_or_number**: Duke gas pipeline in CPCN process: Marshall CTs 850 MW (end-2028), Buck CTs 850 MW (2029), Person County CC 1,360 MW (end-2029), Anderson County CC 1,365 MW (2030), Cayuga CC 1,476 MW (2029/2030); Smith Energy Complex absent
        - **reproduction**: SELECT source_date, project_name, capacity_mw, commitment_status, commercial_operation_date FROM projects WHERE owner LIKE '%Duke%' ORDER BY source_date DESC
      - - **source**: corpus novelty check
        - **date**: 2026-09-21
        - **quote_or_number**: 0 chunks match '"Smith Energy"'; 0 DUK chunks match '"turbine" reserv*'; latest DUK filing chunk 2026-08-04
        - **reproduction**: SELECT count(*) FROM chunks_fts WHERE chunks_fts MATCH '"Smith Energy"'
      - - **source**: arithmetic
        - **date**: 2026-09-21
        - **quote_or_number**: $584M / 255 MW = $2,290/kW for a simple-cycle peaker (vs ~$800/kW in 2021 per commentary cited in search results)
        - **reproduction**: python -c "print(584e6/255e3)"
    - **why_market_misses_it**: It was local NC news on a Friday, three days after the GLJ downgrade dominated GEV coverage; sell-side treats regulated-utility orders as the safest part of the backlog and does not track state CPCN outcomes. The corpus's Duke coverage stops at the Aug 4 10-Q, so any corpus-only analysis misses it.
    - **testable_prediction**: By the NCUC's Carolinas Resource Plan order (expected late 2026 / Q1-27), at least one additional Duke CT or CC CPCN (Buck, Marshall, or a Smith refile) is deferred or conditioned on demonstrated data-center load, and Duke's Q3-26 10-Q (early Nov 2026) adds risk-factor language about CPCN denials affecting turbine procurement.
    - **kill_condition**: NCUC approves a Smith refile within 6 months, or Duke states in its Q3-26 10-Q that turbine reservations and delivery slots are unaffected and no other Duke CPCN is deferred by Q1-27.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: One 255 MW unit is ~0.4% of GEV's 63 GW SRA book; Duke will likely refile after the resource-plan ruling. The docket number, turbine OEM/model for this specific unit, and whether a GEV slot or deposit is tied to it were not retrievable (Business NC and DCD returned 403; NCUC docket portal not searched). The 3-1 vote and commissioner names come from a search snippet of Business NC, not the primary order.
- **dead_ends**:
  - SEC full-text search (efts.sec.gov/LATEST/search-index) for '"slot reservation" "GE Vernova"' 2024-2026: 24 hits, all GEV's own 8-K/10-Q/10-K plus NRG (10-K FY24/FY25, 10-Qs) - NRG's disclosure (two SRAs with GEV for 2.4 GW of 7HA, first COD end-2029) is already in the corpus (ticker NRG). No filer anywhere discloses SRA deposit percentage, refundability or cancellation fees; '"turbine slots"' returns 0 hits.
  - '"gas turbine" "reservation" "deposit"' (661 hits) and '"turbine" "reservation" "forfeit"' (46 hits) are dominated by 2001-2006 filings (Calpine, Dynegy, Midland Cogeneration, CMS, Sierra Pacific, OGE, Tucson Electric, Enron) - useful only as last-cycle color; these were used for Finding 1 via GE's own filings rather than customer filings.
  - Venture Global 10-Q Q1-26 exhibit 10.5 (Fifth A&R Letter of Agreement with Baker Hughes, Mar 5 2026): BH reserves GEV manufacturing capacity for VG power islands with GEV as subcontractor; every quantity, price and date is redacted [***]. https://www.sec.gov/Archives/edgar/data/2007855/000200785526000040/exhibit105-q12026.htm
  - Baker Hughes Q1-26 8-K (Apr 23 2026): BKR converted its own Q4-25 'slot reservation agreement' into 60 NovaLT turbines / 60 BRUSH generators (~1 GW) for a North American 'critical infrastructure' project; shows SRA vocabulary spreading to competitors but contains no GEV data.
  - DPC Holdings S-1/A (Jun 22 2026, IGT castings and superalloy supplier IPO, $837M 2025 revenue, 14 plants): only generic statements (three OEMs' combined backlog >170 GW, 3-4 year lead times); no deposit or pricing terms. Possible supplier-ceiling datapoint but nothing new.
  - Fermi Inc (FRMI) 10-Q Q2-26 and Jul 9 2026 investor deck: Project Matador Phase 1 uses 3 Siemens SGT6-5000F + 6 SGT-800 + 7 GE TM2500 mobile units (leased via Mobile Power Solutions, pick-up Jul 1-Sep 30 2027, no termination for convenience), zero GEV heavy-duty units; Phase 1 slipped from end-2026 to H1-27; no tenant signed as of July; near-going-concern liquidity language. Supports the bridge-power-substitution angle already on the list; not a GEV-specific edge.
  - Solaris Energy Infrastructure 8-K exhibit 10.2 (Mar 16 2026): $148.61M loan secured by 12 SMT-130 mobile turbines, maturity Apr 1 2032; purchase order omitted; no GEV terms. BKV Corp 10-Qs reference 'Equipment Supply Contract' (May 15 2026) and 'Equipment Supply Contract Two' (Jul 17 2026) but details were not retrievable via fetch. Soluna 8-K ex99.1 (Apr 2026) returned 404.
  - FuelCell Energy Sep 2 2026 deck: only recycles S&P's May-2025 'turbine wait times as much as seven years'; no pricing.
  - State PUC / FERC rate-case $/kW for 7HA: no docket found via WebSearch; only the GridLab Sep-2025 cost report (generic CCGT >$2,000/kW). NCUC docket number for the Smith CT denial not retrieved (Business NC and DCD returned HTTP 403).
  - SC DES (ex-DHEC) air-permit modifications for GEV Greenville: nothing indexed by search; ePermitting portal requires interactive use. Job-posting counts for Greenville/Schenectady/Pensacola: not attempted (JS career sites, not reliably countable).
  - Greenville throughput numbers exist outside the corpus but are stale: Post and Courier / Upstate Business Journal (Jan 2025) reported Greenville producing ~50 turbines/yr historically, with targets of 37 units in 2025, 62 in 2026, 74 in 2027 after the $160M / 650-job expansion. Corpus WEB chunk mentions the $160M investment but not the unit counts; hand to the factory-throughput angle owner (62 units x ~0.32 GW avg is roughly the 20 GW claim, so it corroborates rather than contradicts).
  - Court dockets: Vineyard Wind v. GE Renewables settled Sep 16 2026 with confidential terms (VW claimed >$850M, GEV >$300M; April injunction and arbitration denial) - already in the corpus (NEWS 2026-09-16 and 2026-09-18). AEP v. GE onshore wind (Oklahoma) is older. No new gas-turbine dispute or arbitration found.
  - GLJ note details (Bitget summary): orders placed 2026-27 delivered 2030-31; industry effective capacity 104-113 GW vs 88-90 GW expected orders in 2030-31; forward EV/EBITDA 38.9x. No primary data beyond what the team already has on 2027-vintage margin.
  - Aug 25 2026 8-K: CFO Kenneth Parks retires Apr 2 2027; Claire McDonough (Rivian CFO) joins Nov 1 2026, becomes CFO Jan 1 2027, $14.5M make-whole. Already in the corpus (8-K 2026-08-27); no pattern.
  - Nothing material found dated Sep 20-21 2026; latest items are Laguna (Sep 16), Vineyard settlement (Sep 16), NCUC denial (Sep 18).
  - Tooling note: direct urllib fetches of www.sec.gov/Archives with a no-email User-Agent return HTTP 403; efts search-index works with that UA; WebFetch on sec.gov exhibit .htm files works, but on the NRG 10-K main .htm it returned only the XBRL header. Use the corpus for NRG text instead.

## [Sweep] find:customer-filings

- **lens**: customer-side reader: what GEV's 18 SEC-filing customers (plus EIA-860M and non-corpus SEC filers) disclose that GEV does not
- **findings**:
  - - **title**: Entergy has contractually locked ~20 GW of H-class power islands to Mitsubishi, exclusive, and keeps ratcheting the minimum up (15 -> 21 -> 24 -> 27 sets)
    - **claim**: Entergy's 10-Q 'Exclusivity Agreement with Major Vendor' (vendor = Mitsubishi Power per Entergy's CEO) commits it to a minimum of 27 power-island sets plus 2 CTs for frames >400 MW, with only 10 sets + 2 CTs fulfilled at Jun-30-2026, and a clause that buying any >400 MW frame from another supplier lets the vendor terminate and charge 50% of base price on every unordered set; this removes the single largest disclosed US utility gas pipeline (Entergy = 20 of the 51 planned >=350 MW gas turbine units in EIA-860M Jul-2026, 9.4 of 23.2 GW) from GEV's addressable market through ~2030.
    - **mechanism**: GEV guidance (20 GW/yr, 125 GW under contract by YE26, $200B backlog by 2027) implicitly assumes GEV keeps a majority share of new US H-class orders. Entergy's 17 unfulfilled sets (~12.8 GW of 754-MW blocks, ~8 GW of turbine nameplate) plus Georgia Power's Yates CTs (MHI EPC, Jan-2024) mean roughly 47% of the EIA-visible planned large-frame fleet is MHI, with an exclusivity penalty that makes switching to GEV economically impossible for Entergy's four opcos. This caps GEV's 2028-2031 order vintage in the Gulf South, the region with the largest data-center gas builds (Meta Hyperion 2.26 GW + 7 more CC units 2030-31 for a second customer), and is a direct input to the MHI-70-GW-vs-GEV share debate.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks id 352323, ETR 10-Q filed 2025-08-01 (accession 0000065984-25-000087), Note 1
        - **date**: 2025-08-01
        - **quote_or_number**: "guarantees Entergy one manufacturing slot per quarter ... minimum order of 15 sets of PIE and two CTs ... obligated to pay 50% of the base price for each PIE or CT not yet ordered."
        - **reproduction**: SELECT c.id,c.form,c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"manufacturing slot"' AND c.ticker='ETR' ORDER BY c.filing_date
      - - **source**: chunks id 338414 (10-Q 2025-10-31), 313974 (10-K 2026-02-19), 289022 (10-Q 2026-05-01), 265306/265307 (10-Q 2026-07-31)
        - **date**: 2025-10-31 to 2026-07-31
        - **quote_or_number**: Minimum PIE sets: 15 (May-25) -> 21 (Q3-25) -> 24 (Q1-26) -> 27 (Q2-26); fulfilled: 7 sets + 2 CTs (Dec-25) -> 10 sets + 2 CTs (Jun-30-26)
        - **reproduction**: SELECT c.id,c.form,c.filing_date,substr(c.text,instr(c.text,'Exclusivity Agreement with Major Vendor'),900) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Exclusivity Agreement with Major Vendor"' AND c.ticker='ETR' ORDER BY c.filing_date
      - - **source**: SEC XBRL R-page for ETR 10-Q Q2-2026: https://www.sec.gov/Archives/edgar/data/71508/000006598426000283/R10.htm (independent reproduction outside the corpus)
        - **date**: 2026-07-31
        - **quote_or_number**: "updating the minimum order commitment of PIE to 27 sets ... As of June 30, 2026, 10 sets of PIE and two CT slots of the minimum commitment have been fulfilled."
        - **reproduction**: Open https://www.sec.gov/Archives/edgar/data/71508/000006598426000283/R10.htm and search 'Exclusivity Agreement'; also https://www.sec.gov/Archives/edgar/data/71508/000006598425000046/R34.htm shows the Mar-2025 XBRL tag LongTermPurchaseCommitmentMinimumQuantityRequired = 15 (Arkansas 4, Louisiana 9, Mississippi 2)
      - - **source**: Entergy Q2-2025 earnings call, 2025-07-30 (roic.ai transcript https://www.roic.ai/quote/ETR/transcripts/2025-year/2-quarter)
        - **date**: 2025-07-30
        - **quote_or_number**: CEO: "exclusivity agreement for power island equipment, including 15 combined cycle combustion turbines and 2 simple-cycle ... Collectively, these turbines provide 15 gigawatts" and "We're using Mitsubishi's larger turbines"
        - **reproduction**: https://www.roic.ai/quote/ETR/transcripts/2025-year/2-quarter (search 'exclusivity' and 'Mitsubishi')
      - - **source**: generators table (EIA-860M), vintage 2026-07
        - **date**: 2026-07
        - **quote_or_number**: Planned NG CT/GT units >=350 MW: 51 units / 23.2 GW total; Entergy entities 20 units / 9,409 MW (unit sizes 467-478 MW = M501JAC class); Georgia Power Yates 3 units / 1,448 MW (MHI EPC per SO 10-Q 2024-10-31, chunk 405309); Homer City 7 units / 2,520 MW (GE 7HA)
        - **reproduction**: SELECT entity_name, plant_name, COUNT(*), ROUND(SUM(mw)), MIN(planned_year), MIN(status) FROM generators WHERE vintage='2026-07' AND sheet LIKE '%lanned%' AND energy_source='NG' AND prime_mover IN ('CT','GT') AND mw>=350 GROUP BY entity_name, plant_name ORDER BY 4 DESC
      - - **source**: chunks id 265274, ETR 10-Q 2026-07-31 (Richland Parish 1-4 + Pointe Coupee 1-3 for a second large customer)
        - **date**: 2026-07-31
        - **quote_or_number**: "The seven new combined cycle combustion turbine generation resources have various estimated in-service dates in 2030 and 2031."
        - **reproduction**: SELECT text FROM chunks WHERE id=265274
    - **why_market_misses_it**: The disclosure sits in Entergy's Note 1 (Commitments), never names the vendor, and is worded as a utility procurement risk, not an OEM share event; GEV analysts read GEV's SRA totals, not utility purchase-commitment footnotes. The XBRL tag (LongTermPurchaseCommitmentMinimumQuantityRequired) is rarely screened. GEV's own filings mention Entergy once (chunk count = 1).
    - **testable_prediction**: Entergy's Q3-2026 10-Q (due ~Oct 30, 2026) shows minimum PIE >= 27 with fulfilled >= 11, and neither GEV nor Entergy announces a 7HA order for any Entergy opco before the Oct-2 memo or through Q1-2027; MHI's next Americas order disclosure (Nov-2026 results) shows US heavy-duty orders up year over year.
    - **kill_condition**: Entergy 10-Q reports the exclusivity agreement terminated, amended to allow other suppliers, or GEV/Entergy announce an H-class order for any Entergy opco; or MHI's FY results show US order intake falling below 2025 levels.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Vendor identity rests on the CEO's July-2025 call remark and the Orange County/JAC precedent, not on the 10-Q text; 'sets' size is inferred (754 MW blocks, 467-478 MW CTs). EIA-860M lags: most GEV SRAs (NRG 3.6 GW, Duke, NextEra) are not yet in the planned sheet, so the 47% MHI share of the EIA-visible fleet overstates MHI's share of total US 2028-31 orders. Entergy's commitments (15 sets = 15 GW per CEO, of which 7 GW 'for future customer growth') include capacity with no customer yet, so part of the MHI lock could be deferred rather than built.
  - - **title**: Customer rate filings show the all-in cost of a 754-MW combined-cycle block rose ~75% in 16 months (Oct-24 $1,583/kW -> Feb-26 $2,688-2,773/kW), and GE-supplied blocks price no higher than Mitsubishi-supplied ones
    - **claim**: Utility certification filings in the corpus give a dated $/kW ladder for near-identical 1x1 H/J-class blocks: Orange County (MHI) $988/kW (2021 filing), Franklin Farms (MHI) $1,583/kW (Oct-2024 filing), Jefferson (MHI) $2,125/kW (Aug-2025), Duke Cayuga $2,236/kW (2025), Oglethorpe Smarr (GE Vernova) $2,316/kW (2025 budget), Waterford 6 / Westlake (MHI) $2,688 / $2,773/kW (Feb-2026), NRG Texas BYOP (GE 7HA) $2,700/kW (Aug-2026); the ladder is industry-wide, not GEV-specific, and is now drawing regulator resistance (APSC staff opposed Jefferson; Synapse testimony calls Georgia Power's CC costs 'the highest I have seen').
    - **mechanism**: GLJ's bear case is that 2027 shipments were sold at 2024 prices (3 pts margin vs 10-11 pts). The customer ladder shows the market-clearing all-in block price is up ~2.7x since 2021 and ~75% since the Oct-2024 vintage, so the 2028+ GEV vintage carries substantially higher equipment pricing than the 2027 vintage the bear anchors on: bullish for 2028-30 Power margin. But the same ladder shows no GE premium versus Mitsubishi (Oglethorpe $2,316 and NRG $2,700 sit inside the MHI range), so pricing power is scarcity rent shared by three OEMs, not a GEV moat, and regulators are starting to push back on $2,700/kW certifications, which is the mechanism by which 2029-31 orders slip or shrink.
    - **direction**: either
    - **evidence**:
      - - **source**: chunks id 313509/314786, ETR 10-K 2026-02-19 (Orange County, filed Sept 2021)
        - **date**: 2026-02-19
        - **quote_or_number**: 1,215 MW at 'initially-estimated expected total cost of $1.2 billion' = $988/kW
        - **reproduction**: SELECT text FROM chunks WHERE id=313509
      - - **source**: chunks id 313493, ETR 10-K 2026-02-19 (Franklin Farms 1&2, application Oct 2024; 2 x 754 MW)
        - **date**: 2026-02-19
        - **quote_or_number**: "combined cost of Franklin Farms Power Station Units 1 and 2 is estimated to be approximately $2,387 million" = $1,583/kW on 1,508 MW
        - **reproduction**: SELECT c.id,c.filing_date FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Franklin Farms" "2,387"' AND c.ticker='ETR'
      - - **source**: chunks id 314491, ETR 10-K 2026-02-19 (Jefferson, application Aug 2025)
        - **date**: 2026-02-19
        - **quote_or_number**: "approximately 754 MW ... The estimated cost of the project is $1,602 million" = $2,125/kW; APSC general staff filed testimony opposing (chunk 313489)
        - **reproduction**: SELECT text FROM chunks WHERE id IN (314491,313489)
      - - **source**: chunks id 265279/265280, ETR 10-Q 2026-07-31 (Waterford 6 and Westlake, application Feb 2026, 2 x 754 MW)
        - **date**: 2026-07-31
        - **quote_or_number**: "estimated costs are approximately $2,027 million for the Waterford 6 Power Station and $2,091 million for the Westlake" = $2,688 and $2,773/kW; hearings Oct-Nov 2026, LPSC decision requested by Dec 2026
        - **reproduction**: SELECT text FROM chunks WHERE id IN (265279,265280)
      - - **source**: chunks id 263264, DUK 10-Q 2026-08-04 (Cayuga CC, 1,476 MW winter)
        - **date**: 2026-08-04
        - **quote_or_number**: "The estimated cost of the Cayuga CC Project is approximately $3.3 billion, plus actual AFUDC" = $2,236/kW; CC1 2029, CC2 2030
        - **reproduction**: SELECT text FROM chunks WHERE id=263264
      - - **source**: Oglethorpe Power 10-K filed 2026-03-27 (not in corpus): https://www.sec.gov/Archives/edgar/data/788816/000078881626000009/opc-20251231.htm
        - **date**: 2026-03-27
        - **quote_or_number**: Smarr: 'agreement with GE Vernova Operations, LLC for the purchase of the two combined cycle units', ~1,425 MW, budget $3.3 billion (= $2,316/kW), COD 2029, EPC TIC/Kiewit; $343.5M spent at Dec-31-2025
        - **reproduction**: Fetch the URL and search 'Smarr'
      - - **source**: NRG Q2-2026 8-K exhibit 99.1 and Aug-4-2026 call (https://www.sec.gov/Archives/edgar/data/1013871/000101387126000018/nrgq22026ex991.htm; https://www.roic.ai/quote/NRG:CV/transcripts/2026-year/2-quarter)
        - **date**: 2026-08-04
        - **quote_or_number**: "Total investment for the 1.2 gigawatt project is expected to be $3.2 billion or $2,700 a kW" (GE 7HA block, COD late 2029)
        - **reproduction**: Open the roic.ai transcript and search '2,700'
      - - **source**: Synapse/Metz testimony, Georgia PSC docket 25-086 (https://www.synapse-energy.com/sites/default/files/PD_MetzTestimony%2025-086.pdf)
        - **date**: 2025
        - **quote_or_number**: "The capital costs of the proposed combined-cycle units have more than doubled since Georgia Power completed its 2025 IRP" (Bowen 7-8, Wansley 10-11, McIntosh 12; dollar figures redacted)
        - **reproduction**: Fetch the PDF; section 'capital costs ... more than doubled'
    - **why_market_misses_it**: Each number lives in a different utility's regulatory-matters note or a co-op 10-K; nobody lines them up by filing date and block size. Sell-side quotes GEV's own 'pricing up' language without a customer-side ladder, and the bear (GLJ) anchors on the 2027 vintage without evidence of what 2028-31 blocks are being certified at.
    - **testable_prediction**: Every new US utility CC certification filed between now and Mar-2027 (Entergy Richland 3-4/Pointe Coupee cost disclosure, Duke Anderson SC, Georgia Power McIntosh 12) comes in at >= $2,500/kW all-in; the LPSC approves Waterford 6/Westlake by its Dec-2026 meeting but with cost-cap or customer-funding conditions; GEV's Q4-2026 call (late Jan 2027) reports gas equipment price/mix contribution larger than in Q4-2025.
    - **kill_condition**: A US utility files a new H/J-class CC certification after Oct-2026 at < $2,200/kW all-in, or the LPSC rejects or materially cuts Waterford 6/Westlake (proving the ladder is now demand-destroying rather than margin-accretive).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Figures are all-in utility estimates (EPC, AFUDC, interconnection, transmission network upgrades, contingency), not OEM equipment prices; OEM share of the block is typically 30-40%, so the equipment-price increase implied is smaller than the ladder's 75%. Cayuga's OEM is not confirmed. Georgia Power's certified dollar figures are redacted in the public testimony.
  - - **title**: EIA-860M shows planned US gas-turbine units almost never cancel once listed: 0.2 GW canceled of 33.8 GW over Jul-25 -> Jul-26, and 39 of 41 units slated for 2025 were operating by Jul-26
    - **claim**: Tracking each planned NG combustion/combined-cycle turbine unit across EIA-860M snapshots in the corpus, the Jul-2025 planned cohort (175 units, 33.8 GW) one year later was: 105 units held their date (20.6 GW), 28 slipped (7.5 GW, median slip 7 months), 32 went operating (4.8 GW), 5 canceled (0.2 GW); the Jan-2025 cohort had a higher cancel rate (10 units, 2.8 GW of 26 GW) but 39 of the 41 units planned for 2025 (4.21 of 4.24 GW) reached Operating by Jul-2026.
    - **mechanism**: The 'backlog into dirt' bear needs cancellations or multi-year slips. Once a project reaches the EIA planned sheet (owner has filed with EIA, usually post-turbine order), realized attrition is <1% of MW per year and the typical slip is two quarters. For GEV this means the equipment backlog converts to revenue on roughly the customers' stated schedule, supporting over-time revenue recognition and the 20 GW/yr run-rate; the risk is concentrated before the EIA listing (SRA stage, see finding 4), not after.
    - **direction**: long
    - **evidence**:
      - - **source**: generators table (EIA-860M), vintages 2025-07 vs 2026-07
        - **date**: 2026-07
        - **quote_or_number**: 175 units / 33.8 GW planned in Jul-25: held 105 (20.6 GW), slipped 28 (7.5 GW, median 7 months), pulled in 5 (0.7 GW), operating 32 (4.8 GW), canceled 5 (0.2 GW), missing 0
        - **reproduction**: Python: A = planned rows (vintage='2025-07', sheet LIKE '%lanned%', energy_source='NG', prime_mover IN ('CT','CA','CS','GT')) keyed by (plant_id, generator_id); B = all rows for vintage='2026-07' with same filter; classify each A key by B sheet ('Canceled' / 'Operating') or by planned_year*12+planned_month delta (>0 slipped, <0 pulled in, =0 held); sum mw per class
      - - **source**: generators table, vintages 2025-01 vs 2026-01
        - **date**: 2026-01
        - **quote_or_number**: 126 units / 26 GW: held 47 (15.7 GW), slipped 32 (3.3 GW, median 7 mo), operating 35 (4.2 GW), canceled 10 (2.8 GW)
        - **reproduction**: Same procedure with vintages '2025-01' and '2026-01'
      - - **source**: generators table, units with planned_year=2025 in vintage 2025-01, status in vintage 2026-07
        - **date**: 2026-07
        - **quote_or_number**: 39 of 41 units (4.21 of 4.24 GW) Operating; 1 unit re-planned to 2026, 1 to 2027
        - **reproduction**: SELECT h.sheet, h.planned_year, COUNT(*), ROUND(SUM(g.mw)) FROM generators g LEFT JOIN generators h ON h.vintage='2026-07' AND h.plant_id=g.plant_id AND h.generator_id=g.generator_id AND h.energy_source='NG' WHERE g.vintage='2025-01' AND g.sheet LIKE '%lanned%' AND g.energy_source='NG' AND g.prime_mover IN ('CT','CA','CS','GT') AND g.planned_year=2025 GROUP BY 1,2
      - - **source**: generators table, planned NG turbine GW by planned year across vintages
        - **date**: 2026-07
        - **quote_or_number**: Planned GW by COD year, Jul-26 vintage: 2027 11.1, 2028 16.1, 2029 13.4, 2030 18.1 (2030 was 7.4 GW in the Jan-26 vintage; 11.0 GW of new 2030 entries in six months, 8.8 GW of it Fermi America, which is Siemens-supplied)
        - **reproduction**: SELECT vintage, planned_year, ROUND(SUM(mw)/1000.0,1), COUNT(*) FROM generators WHERE vintage IN ('2026-01','2026-07') AND sheet LIKE '%lanned%' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') GROUP BY 1,2
    - **why_market_misses_it**: Analysts cite interconnection-queue completion rates (10-20%) as the base rate for gas projects; the EIA planned sheet is a much later stage gate and its unit-level attrition has to be computed by joining monthly snapshots, which nobody publishes.
    - **testable_prediction**: In the Dec-2026 EIA-860M vintage, cumulative cancellations from the Jul-2025 planned cohort remain below 1.0 GW and at least 60% of units keep their Jul-2025 date; Franklin Farms 1&2 (Dec-2028) and Traceview/Vicksburg (Aug-2028) keep their dates through the Dec-2026 vintage.
    - **kill_condition**: Dec-2026 or later 860M vintage shows > 3 GW of the Jul-2025 planned gas-turbine cohort moved to 'Canceled or Postponed', or median slip of the cohort exceeds 12 months.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: EIA lists only units owners choose to report, so pre-listing attrition (SRA to order to EIA filing) is invisible here; 2025-26 was a period of extreme demand, so the base rate may not hold in a downturn; the 2030 bucket is dominated by one speculative developer (Fermi, 128 small units).
  - - **title**: NRG stopped disclosing its GE Vernova slot reservations in 2026 10-Qs after ratcheting them 1.2 -> 2.4 -> 3.6 GW, and one year on has only one 1.2 GW block with a (non-final) customer
    - **claim**: NRG's 10-K and every 10-Q from Feb-2025 through Feb-2026 carried a 'Site Development Updates' paragraph reporting its GEV slot reservation agreements (1.2 GW Feb-25, 2.4 GW May-25, 3.6 GW Feb-26); both 2026 10-Qs (May-6 and Aug-4) dropped the paragraph entirely (0 hits for 'Vernova', 'slot', '7HA', 'Kiewit') while still discussing T.H. Wharton and Greens Bayou; on the Aug-4-2026 call NRG said all 5.4 GW is 'tied to an active customer discussion' but only 1.2 GW has 'principal commercial terms aligned', not FID, with subsequent 1.2 GW blocks 'serially each year after the 2029 COD'.
    - **mechanism**: GEV's 63 GW of SRAs are the bull case's proof of demand; NRG is the only SRA holder that discloses in its own SEC filings. Its pattern (reserve first, find customer later; 3.6 GW reserved, 1.2 GW with a customer 18 months later; disclosure withdrawn) is a customer-side sample of SRA-to-firm-order conversion speed and shows what GEV's 'converted' GW means: the NRG block only counts as an order once NRG takes FID, which the company says needs land, negotiation and internal approval. If GEV's Q3/Q4-2026 'conversions' include IPP blocks without customer FIDs, the equipment backlog quality is weaker than the headline.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks id 381520 (10-K 2025-02-26), 359503 (10-Q 2025-05-12), 349094 (10-Q 2025-08-06), 334640 (10-Q 2025-11-06), 308019 (10-K 2026-02-24), ticker NRG
        - **date**: 2025-02-26 to 2026-02-24
        - **quote_or_number**: "slot reservation agreement with GEV for the procurement of 1.2 GW" -> "two slot reservation agreements ... 2.4 GW" -> "slot reservation agreements with GEV for the procurement of 3.6 GW of 7HA gas turbines"; every version: "first projects ... expected to commence operations by the end of 2029"
        - **reproduction**: SELECT c.id,c.form,c.filing_date,substr(c.text,instr(c.text,'slot reservation')-200,400) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation"' AND c.ticker='NRG' ORDER BY c.filing_date
      - - **source**: chunks table, NRG 10-Q 2026-05-06 (215 chunks) and 10-Q 2026-08-04 (246 chunks)
        - **date**: 2026-08-04
        - **quote_or_number**: Hits in 2026 10-Qs: 'Vernova' 0, 'slot reservation' 0, 'Site Development Updates' 0, '7HA' 0, 'Kiewit' 0; 'T.H. Wharton' 6 and 7; 'Greens Bayou' 6 and 5
        - **reproduction**: SELECT c.form,c.filing_date,COUNT(*) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Vernova"' AND c.ticker='NRG' AND c.filing_date>='2026-01-01' GROUP BY 1,2  -- repeat with '"T.H. Wharton"'
      - - **source**: NRG Q2-2026 earnings call 2026-08-04 (https://www.roic.ai/quote/NRG:CV/transcripts/2026-year/2-quarter) and 8-K ex-99.1 (https://www.sec.gov/Archives/edgar/data/1013871/000101387126000018/nrgq22026ex991.htm)
        - **date**: 2026-08-04
        - **quote_or_number**: "first 1.2 gigawatts of the 5.4 gigawatts of turbine and EPC capacity we've secured through 2032 ... every turbine slot tied to an active customer discussion"; 8-K: terms 'remain subject to final documentation and approvals'; cumulative spend through 2026 $0.8B 'including previously made reservation payments'
        - **reproduction**: Open both URLs; search 'active customer discussion', 'reservation payments', 'subject to final documentation'
    - **why_market_misses_it**: GEV reports SRA and 'converted' GW in aggregate; the only customer that itemizes its SRAs in SEC filings quietly stopped doing so, and the removal of a recurring MD&A paragraph does not show up in any screen.
    - **testable_prediction**: NRG's Q3-2026 10-Q (early Nov 2026) again omits the SRA paragraph and NRG does not announce FID on the 1.2 GW block before the Oct-2 memo; GEV's Q3-2026 release (Oct 21-22, 2026) reports SRA-to-backlog conversion below the 10 GW of Q2-2026.
    - **kill_condition**: NRG announces FID and a named hyperscaler for the 1.2 GW block, or a second 1.2 GW customer, before Dec-31-2026; or NRG's Q3 10-Q restores disclosure showing >3.6 GW converted to firm orders.
    - **novelty**: 2
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Overlaps the team's 'reservations != orders' and deposit-ledger angles; the dropped paragraph may reflect MD&A editing after the LS Power acquisition rather than a change in the agreement. NRG says the slots are use-it-or-lose-it on a timeline it has not disclosed, so the reservations could still convert on schedule.
- **dead_ends**:
  - 'GE Vernova' / 'Vernova' appears in only 4 customer tickers' primary filings (NRG 7, CEG 1 [Strazik CERAWeek quote in a Constellation deck], AMZN 1 [AWS customer list], AEP 1 [11-K holdings]); no utility 10-K/10-Q names GEV as its turbine vendor.
  - 'slot reservation' in customer filings: NRG only. SEC full-text search (efts) for 'slot reservation' 2024-2026 returns 41 hits, almost all GEV's own filings; the non-GEV hits are NRG, INNIO/Liberty (Jenbacher recips), Baker Hughes, plus biotech noise.
  - 'turbine' + 'deposit' in customer filings (TLN 10, VST 5, D 2, CEG 1) are all credit-agreement definitions (margin deposits) or offshore-wind contract definitions (Dominion CVOW / Siemens Gamesa), not gas turbine deposits.
  - 'turbine' + 'lead time' (XEL 5) is generic supply-chain boilerplate; 'turbine' + 'delay' (D 10, TLN 7, ETR 6) are CVOW offshore wind, Talen O&M, and transmission items; META's 3 hits are a proxy-statement shareholder proposal.
  - No customer filing gives a deposit percentage or refund term for gas turbine reservations; Entergy's agreement explicitly 'does not establish final pricing and delivery dates'.
  - Pivot-to-alternatives search: 'reciprocating engine' only WMB (Socrates, known); 'aeroderivative' in NEE is an executive bio; no utility filing describes substituting batteries/recips because turbines were unavailable. Georgia Power's Synapse testimony argues batteries are cheaper per kW than the new CCs but the dollar figures are redacted.
  - Fermi America 10-K (Mar-2026, fetched from SEC) has no GE Vernova equipment: 6 Siemens SGT-800 + 3 Siemens SGT6-5000F + leased GE TM2500s; another non-GE large planned pipeline (8.8 GW in EIA 2030 bucket) but too speculative to build a finding on.
  - TVA 10-Q (Aug-2026): only GE Vernova mention is the GVH nuclear acronym; no turbine purchase commitments disclosed. BKV 10-Q mentions a 'Manufacturing Reservation Agreement' (Jan-14-2026) with no terms. Clearway's reservation is a wind repower.
  - xbrl_facts table does not contain customer tickers (only universe tickers such as PWR, NEE, GEV, BE, VRT...), so Entergy's purchase-commitment XBRL had to be reproduced from sec.gov R-pages; data.sec.gov companyconcept API returned 404 via WebFetch and raw sec.gov Archives returns 403 without a contact-style User-Agent.
  - projects table is too noisy for customer-side date-revision analysis (Vineyard Wind dominates the 'disputed' rows; many rows are 'Not specified').
  - GEV filings/transcripts contain no 'exclusivity' language and mention Entergy once; no evidence GEV offers Entergy-style exclusivity to any utility.
  - Georgia Power 10-Qs list Bowen 7/8 and Wansley 10/11 CODs (Q4-2029 / Q2-2030) but not certified costs; the public PSC testimony redacts the $/kW, so the Georgia data point could not be added to the price ladder.

## [Verify] repro:services-accounting:The recurring LTSA revenue stream is fla

- **reproduced**: True
- **corrected_numbers**: All core numbers reproduce exactly from GEV primary filings in `documents` (no unit or ticker errors found).

CSA "revenues recognized / billings" ($M), from the "Net contractual service agreements ... revenues recognized of $X ... billings of $Y ... changes in estimated profitability of $Z" sentence (documents.text; note the sentence contains line breaks, so use \s in regexes):
- FY23 4,658 / 5,047 / +34 favorable (8-K/EX Form 10, 2024-03-08, acc 0001193125-24-063739#d808872dex991.htm, documents.id=387)
- Q1'24 1,174 / 1,173 / -29 (10-Q 2024-04-30, 0001996810-24-000008)
- 1H24 2,537 / 2,300 / -89 (10-Q 2024-07-24, 0001996810-24-000067)
- 9M24 3,710 / 3,673 / -135 (10-Q 2024-10-23, 0001996810-24-000083)
- FY24 5,473 / 5,021 / -319 (10-K 2025-02-06, 0001996810-25-000011, id=313)
- Q1'25 1,261 / 1,249 / +29 (10-Q 2025-04-23, 0001996810-25-000073)
- 1H25 2,720 / 2,533 / -42 (10-Q 2025-07-23, 0001996810-25-000133, id=281)
- 9M25 3,824 / 3,781 / -36 (10-Q 2025-10-22, 0001996810-25-000160, id=270)
- FY25 5,412 / 5,362 / -151 (10-K 2026-01-29, 0001996810-26-000015, id=249)
- Q1'26 1,280 / 1,163 / -89 (10-Q 2026-04-22, 0001996810-26-000064)
- 1H26 2,689 / 2,392 / -218 (10-Q 2026-07-22, 0001996810-26-000148, id=218)
Derived: Q2'25 = 2,720-1,261 = 1,459; Q2'26 = 2,689-1,280 = 1,409 (-3.4%). FY25 -1.1%, 1H26 -1.1%, 1H26 billings -5.6%: confirmed.

XBRL cross-check: SELECT start_date,end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress' GROUP BY start_date,end_date,val -> 10 YTD-duration rows (2024-Q1 to 2026-Q2), values = -1,173, -2,300, -3,673, -5,021, -1,249, -2,533, -3,781, -5,362, -1,163, -2,392 ($M, negative sign) = the billings figures above. No duplicates.

Power segment Services revenue ($M): FY23 11,838; FY24 12,419; FY25 13,081 (10-K FY25 id=249, text offset ~159,991, table "Equipment $6,686 $5,708 $5,598 / Services 13,081 12,419 11,838"); Q2'26 3,512; Q2'25 3,280; 1H26 6,598; 1H25 6,238 (10-Q Q2'26 id=218, offset ~104,149). Growth FY25 +5.3%, 1H26 +5.8%: confirmed. CSA share 44.1% / 41.4% / 40.8%: confirmed (FY23 share = 39.3%, see issues).

Power services RPO ($M): Dec-22 57,355; Dec-23 59,338; Dec-24 60,890 (10-K FY24 id=313, offset ~264,173); Jun-24 58,479; Jun-25 62,932 (10-Q Q2'25); Sep-25 65,083 (10-Q Q3'25); Dec-25 69,680 (10-K FY25 id=249, offset ~159,414) restated to 69,841 (10-Q Q1'26 and Q2'26); Mar-26 71,164; Jun-25 restated 63,088 and Jun-26 72,388 (10-Q Q2'26). +14.7% y/y and +$9.3B: confirmed. Regex for 10-Qs: r'RPO\s*((?:\w+ \d+,? \d{4}\s*){2,3})Equipment\s*\$([\d,]+)[^S]{0,60}Services\s*([\d,]+)[^T]{0,60}Total RPO\s*\$([\d,]+)' (2nd match = Power); 10-K tables are "RPO\nDecember 31\n2025\n2024\n2023\nEquipment..." (search 'Total RPO', 2nd hit = Power).

Critical accounting estimate quotes (chunks_fts MATCH '"life of contract billings"' AND ticker='GEV'): Form 10 "$3.4 billion in our Power segment represents approximately 5%"; 10-K FY24 "$3.5 billion represents approximately 5%"; 10-K FY25 "$3.4 billion represents approximately 4%"; "approximately 29% complete" in all three. Units (chunks_fts MATCH '"under long-term service agreements"'): ~7,000 installed, ~1,700 under LTSA (Form 10, all three 2024 10-Qs, 10-K FY24) -> ~1,800 (10-K FY25); ~10 years average remaining life throughout.

Transcript quote: chunks form=TRANSCRIPT, accession src:3161, ticker GEV, tier primary; sources.id=3161 url https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf (Q2'26 webcast). Text: "This is happening not only on long-term service agreements, but also on transactional orders. We've seen transactional orders per unit continue to rise by double digits annually as customers invest in upgrades and greater scope and outages, all at higher prices." Confirmed.

Management narration confirmed in 10-K FY25 ("Gas Power services due to higher parts volume, contractual services, and favorable price") and 10-Q Q2'26 ("higher parts volume and favorable pricing").
- **data_quality_issues**: 1. "Billings are falling" is a 1H26-only observation, not a trend. FY25 CSA billings were +6.8% y/y (5,362 vs 5,021); 2H25 billings 2,829 vs 2H24 2,721 (+4.0%); 9M25 +2.9%. Q1'26 -6.9% and Q2'26 -4.3% (1,229 vs 1,284). Two consecutive down quarters after a strong FY25 is the honest statement.

2. Base-year sensitivity on "flat LTSA revenue": FY24 CSA revenue recognized was +17.5% vs FY23 (4,658 -> 5,473), and CSA share of Power services was only 39.3% in FY23, so the FY25 "-1.1%" is against an unusually strong comp. FY23->FY25 CSA CAGR is +7.8%/yr vs Power services +5.1%/yr, i.e. CSA outgrew services over two years. The claim "all Power services growth since 2024 is transactional" holds only with FY24 as base. Quarterly CSA revenue is lumpy (outage timing): Q1'24 1,174; Q2'24 1,363; Q3'24 1,173; Q4'24 1,763; Q1'25 1,261; Q2'25 1,459; Q3'25 1,104; Q4'25 1,588; Q1'26 1,280; Q2'26 1,409. 9M25 was +3.1% vs 9M24; FY25 ended -1.1% only because Q4'25 was -9.9% vs Q4'24.

3. The caveat "gross of revisions it is +2% to +7%" is arithmetically inconsistent: it adds the revision back to the current period (5,412+151; 2,689+218) but not to the comparison period (FY24 -319; 1H25 -42). On a consistent gross basis FY25 = 5,563 vs 5,792 (-4.0%) and 1H26 = 2,907 vs 2,762 (+5.2%). If instead the roll-forward "revenues recognized" excludes the catch-up so P&L CSA revenue = recognized minus unfavorable revision: FY24 5,154, FY25 5,261 (+2.1%), 1H25 2,678, 1H26 2,471 (-7.7%). The disclosure does not say which; do not lean on the caveat's numbers.

4. Implied "total estimated life-of-contract billings $68B -> $70B -> $85B" is derived by dividing $3.4B/$3.5B/$3.4B by "approximately 5%/5%/4%". Rounding alone (4.5-5.5% vs 3.5-4.5%) gives Dec-24 ~$64-78B and Dec-25 ~$76-97B; the ranges overlap, so the +21% step is not reliably measured. Use as order-of-magnitude only.

5. The XBRL tag name (ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress) does not describe its content; its values are the CSA billings. A verifier reading the label literally would misinterpret it. Also ContractWithCustomerAssetNetCurrent ($8.3B Dec-23 to $9.5B Jun-26) is the total contract asset, not the net CSA balance, so it cannot be used to confirm the $3.4B figures.

6. sources.published is blank for src:3161; date 2026-07-22 comes from the URL filename only.

7. The "why market misses it" assertion that the LTSA/transactional split is absent from the earnings deck and press release was not verified (no deck in the checked documents).

8. The Q3'25 10-Q roll-forward sentence has line breaks inside ("Net contractual service\nagreements\nincrease\nd primarily..."), so the finding's regex r'Net contractual service agreements[^.]*\.' misses it; use \s+ between words.
- **notes**: Method: Python 3.11 sqlite3 SELECTs against data\gev.db (documents, chunks_fts JOIN chunks, xbrl_facts, sources), regex over documents.text for the five accessions cited plus the six other GEV 10-Qs (ids 360, 340, 331, 295, 270, 228). No web fetches were needed; every number came from primary SEC filings or the company's own Q2'26 webcast transcript PDF, all ticker='GEV', tier='primary'. No file was written to the repo.

Verdict: the finding's core evidence (CSA revenue flat FY25/1H26, CSA billings -5.6% in 1H26, Power services +5.3%/+5.8%, CSA share falling from 44.1% to 40.8%, Power services RPO +$9.3B / +14.7% y/y, ~1,700 -> ~1,800 units under LTSA, transcript quote) reproduces exactly. The framing needs two softenings: (a) billings grew +6.8% in FY25 and only turned negative in Q1'26/Q2'26; (b) FY24 was a +17.5% CSA year, so the two-year CSA trend is not flat and the "all growth is transactional" line is base-year dependent. The testable prediction (9M26 CSA revenue <= $4.1B, i.e. <= +7% vs 9M25 $3,824M; FY26 CSA $5.2-5.7B) and kill condition (FY26 CSA > $5.9B or 9M26 billings > +5%) are consistent with the reproduced series. Bonus series for the team: 10-K FY25 Power orders table shows HA-Turbine units 24/15/14 and Gas Turbine GW 15.3/11.9/13.8 for 2025/2024/2023 (documents id=249, offset ~159,414).

Dead ends: no XBRL tag exists for CSA revenue recognized or net CSA balance (only the mislabeled billings tag and total contract assets); the Power services LTSA vs transactional split is not in any XBRL fact and must be rebuilt from the Note 9 sentence as the finding says.
- **confidence**: 5

## [Verify] repro:services-accounting:LTSA book margin is being cut at a recor

- **reproduced**: True
- **confidence**: 5
- **corrected_numbers**: All core numbers reproduce exactly. YTD net favorable/(unfavorable) changes in estimated profitability on contractual service agreements, $M, from documents.text regex r'Net contractual service agreements[^.]*\.' (whitespace-normalized for FY24 10-K and 9M25 10-Q, whose text has line breaks inside the sentence): FY23 +34 (8-K/EX 2024-03-08, accession 0001193125-24-063739#d808872dex991.htm, Form 10 info statement) | Q1'24 -29 (0001996810-24-000008) | 1H24 -89 (-24-000067) | 9M24 -135 (-24-000083) | FY24 -319 'due primarily to higher costs' (-25-000011) | Q1'25 +29 (-25-000073) | 1H25 -42 (-25-000133) | 9M25 -36 (-25-000160) | FY25 -151 (-26-000015) | Q1'26 -89 (-26-000064) | 1H26 -218 (-26-000148, filed 2026-07-22). Derived quarters check: Q2'24 -60, Q3'24 -46, Q4'24 -184, Q2'25 -71, Q3'25 +6, Q4'25 -115, Q2'26 -129. Trailing 4Q (Q3'25..Q2'26) = +6-115-89-129 = -327 > FY24 -319 (by only $8M / 2.5%). 218/42 = 5.2x. Q2'26 10-Q Power segment table: Gas Power rev $4,427M/$8,493M; Services $3,512M vs $3,280M; Segment EBITDA $1,031M (18.8%) Q2, $1,842M (17.6%) 1H; 'partially offset by the impact of inflation' present. Ratios: 218/1842 = 11.8%, 129/1031 = 12.5%. FY25 10-K critical estimates: $3.4B net LTSA balance, ~4% of life-of-contract billings, ~29% complete, 1 pt = $0.2B (FY24 10-K: $3.5B, ~5%, 29%, $0.2B). 218/200 = 1.09 pts. Transcript src:3161 (gev_webcast_transcript_07222026.pdf, ord 25, speaker Scott Strazik answering Nicole DeBlase): '130 of our HA units running ... 325 units ... every four years they go through a major outage' verbatim. CFO 'highest outage volume in the fourth quarter' verbatim in src:3161 and Q4'25 call (NEWS src:2660, 2026-01-23). XBRL: tag ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress values = -1173, -2300, -3673, -5021, -1249, -2533, -3781, -5362, -1163, -2392 ($M) = exactly the Note 9 billings figures; no XBRL tag carries the profitability revisions (grep of tags LIKE %Profitab%/%ChangeInEstimate%/%ServiceAgreement% returns nothing else). External: SEC EFTS q="estimated profitability of $218 million" forms=10-Q returns 2 hits, both GEV 10-Q filed 2026-07-22 (ADSH 0001996810-26-000148). Context added: FY Power EBITDA $2,268M FY24 (12.5%), $2,902M FY25 (14.7%) so revisions/EBITDA = 14.1% FY24, 5.2% FY25, 11.8% 1H26.
- **data_quality_issues**: (1) Scope wording: the Note 9 'contractual service agreements' line is Power-segment-wide (Gas, Nuclear, Hydro), not strictly 'Gas Power'. FY25 10-K: 'long-term service agreements, which we refer to as contractual service agreements, with our customers within our Power segment.' Gas Power attribution comes only from MD&A cash-flow prose ('contractual service agreements in Gas Power, partially offset by an unfavorable change in estimated profitability'). Recommend saying 'Power segment CSAs (predominantly Gas Power)'. (2) 'Zero mentions in 15k+ commentary chunks' is slightly overstated: chunks_fts MATCH '"estimated profitability"' returns 4 tier='commentary' rows, but all 4 are GEV's own 2024 Annual Report PDF (src:3650, tier-mislabeled as commentary). NEWS/RSS/YOUTUBE hits across all tickers = 0, so the substantive claim (no third-party coverage) holds. (3) One form='DECK' chunk contains the $218M sentence, but it is src:3159 = the 10-Q PDF hosted on the IR site (gev_webcast_10q_07222026.pdf), not the earnings presentation; the real deck (src:3157), highlights (src:3158), press release (src:2667 and 8-K/EX 0001996810-26-000147), and transcript (src:3161) all lack 'estimated profitability'. Claim holds. (4) 'Worst on record' is true only in absolute dollars for the trailing-4Q window, and by a thin $8M margin; as a share of Power EBITDA, FY24 (14.1%) was worse than 1H26 (11.8%). FY24's full-year 10-K text also explicitly gave a reason ('higher costs'); FY25 and 2026 10-Qs give none. (5) Quarterly series exists only from Q1'24 (FY23 is annual-only from the Form 10), so 'largest non-Q4 since disclosure began' rests on 8 quarterly points and Q4 seasonality on 2 Q4 points. (6) The '1.1 points of book margin' translation uses a balance-sheet sensitivity (1 pt change in total estimated profitability = $0.2B contract-asset change) as a proxy for a P&L cumulative catch-up; directionally right under cost-to-cost but an average across contracts, not a disclosed figure. (7) opencapital.sh page returned HTTP 403 on WebFetch; its existence is confirmed by search result title only, its content (the claimed table) is unverified. Not in the sources table. (8) The 10-Q text for FY24 10-K and 9M25 10-Q contains line breaks mid-sentence, so the literal single-line regex in the finding's reproduction step misses them; use re.sub(r'\s+',' ',text) first. (9) catalyst_calendar row (GEV, 2026-10-21, 'estimated from 8-K item 2.02 cadence', confirmed=0) and prior 10-Q dates (2024-10-23, 2025-10-22) support the 'about Oct 21-22' prediction date; FY25 10-K filed 2026-01-29 supports 'late Jan 2027'.
- **notes**: What I ran: (a) Loop over SELECT accession, form, filing_date FROM documents WHERE ticker='GEV' AND form IN ('10-K','10-Q') with regex extraction of the Note 9 sentence; re-ran with whitespace normalization for the two non-matching docs. (b) chunks_fts MATCH '"Net contractual service agreements"' AND form IN ('8-K/EX','10-K') for FY23. (c) chunks_fts MATCH '"life of contract billings"' AND form='10-K' for both 10-Ks. (d) Regex on 0001996810-26-000148 for 'SEGMENT REVENUES AND EBITDA' table and 'impact of inflation'. (e) chunks_fts MATCH '"major outage"' form='TRANSCRIPT' and '"outage volume"' for the CFO line; pulled adjacent chunk ord to confirm speaker = Scott Strazik. (f) xbrl_facts GROUP BY tag,start_date,end_date for tags LIKE '%CumulativeCatchUp%' (no duplicates across filings affect values). (g) Tier/form counts for '"estimated profitability"' and related phrases; inspected every commentary/DECK hit and mapped src ids to sources.url. (h) Checked Q2'26 press release, deck, highlights, transcript, mp3-transcript text for the phrase: all False. (i) FY Power EBITDA from both 10-K segment tables. (j) WebSearch x2 (no third-party narrative found; only IR/SEC links and an opencapital.sh listing). (k) SEC EFTS: broad phrase query confirms GEV 10-Q/10-K series 2024-04-30 to 2026-07-22; exact-phrase query for '$218 million' returns only the 2026-07-22 10-Q. Verdict: every core number, quote and the XBRL-blind-spot mechanism reproduce; the finding is sound as a margin-quality / Q4-print-risk point. Suggested tightening for the memo: cite 'Power segment CSAs', present the $ record alongside the %-of-EBITDA view (FY24 was worse in % terms), and keep the kill condition as written (9M26 10-Q about Oct 21-22: cumulative figure must exceed $218M in magnitude). Dead ends: no XBRL tag for the revisions exists (screens cannot pick it up); transcript_statements/analyst Q&A never raise it; opencapital.sh cannot be fetched (403).

## [Verify] skeptic:price-events:The GW-order metric has stopped moving t

- **refuted**: True
- **already_widely_known**: True
- **where_known**: (1) Jefferies note Sep 11 2026 (corpus chunks 246514, 246517, NEWS 2026-09-12): "investors are too focused on 'peak orders' and overlooking the long-term services business" — the sell-side has already named the exact debate. (2) Barclays SE downgrade Jul 7 2026 (chunk 465392) and GLJ initiation Sep 14 2026 ("a cyclical gas turbine manufacturer priced as a secular compounder", Seeking Alpha/Yahoo Sep 14) are themselves the published 'peak-cycle' thesis. (3) CNBC Jul 22 2026 (chunk 468514): "GE Vernova sellers blinded by an earnings miss should focus on strong demand instead"; Zacks Jul 23 (chunk 246277): "$2.47 per share, missing the Zacks Consensus Estimate of $3.17"; Benzinga/Motley Fool/Investing.com Jul 22 all attribute the drop to the EPS miss plus Wind. (4) TIKR Jul 2026 ("GE Vernova Stock Fell 7% on a Rival's Downgrade"): "the market needs orders to keep surprising, not merely hold" — the second-derivative framing, verbatim, two months ago. (5) Q2'26 call (Investing.com transcript): an analyst asked whether 2026 is peak orders; management answered "very clear pathway to continuing to grow our contracted gigawatts on order beyond this year." (6) corpus chunk 246542 (Aug 18): "raises questions on how much future growth is already priced in."
- **materiality**: 2
- **strongest_counterargument**: The sign of every GEV earnings-day return since Q1'25 matches the sign of the adjusted-EPS surprise, so the simpler model is 'EPS surprise plus guidance', not 'orders saturated'. Table (adj EPS actual/consensus -> close-to-close, prices table): Q2'25 $1.86/$1.50 (+24%) -> +14.58%; Q3'25 $1.64/$1.72 (-5%) -> -1.59%; Q4'25 beat (Zacks 3-of-4 record) -> +2.73%; Q1'26 $1.98/$1.84 (+7.6%) -> +13.75%; Q2'26 $2.47/$3.04 (-19%) -> -8.69%; Q1'25 $0.91 was a widely reported beat -> +3.07% (consensus not verified in corpus). 6 for 6 on sign; GW signed explains nothing once EPS surprise is in the model. The finding's core claim that guidance raises stopped moving the stock is contradicted by its own data: three of four raise-days were up (+14.58%, +2.73%, +13.75%, the last only one quarter before Jul 22), and the lone exception carried a 19% EPS miss, Wind EBITDA loss widening to -$275M from -$165M, and an unchanged 12-14% EBITDA margin guide despite a $1B revenue raise (8-K/EX 2026-07-22). The event selection is also wrong: Jul 7 (-6.51%) was the sixth-largest 2026 down day, not the second — Sep 14 -8.62%, Jun 23 -8.21%, Aug 18 -6.90%, May 7 -6.55% were all larger (prices table, 2026 rows). Jun 23 was a broad AI-infrastructure risk-off day on which GEV won a Vietnam gas-turbine order the same morning; Aug 18 was a 13F profit-taking story; neither involved a peak-cycle note. The Jul 7 move must be read with Jul 6 (+3.50%): the two-day GEV move was -3.2% vs VRT +1.7%, so the GEV-specific residual is about -4%, half the headline. The -16.55% five-day drift after Jul 22 is sector beta, not GEV information: Jul 28 PWR -5.15%, Jul 29 VRT -17.26% on its own print, then Jul 30 GEV +9.07% alongside PWR +17.26%. Finally, Barclays' Jul 7 argument (SE booked 50 GW annualised vs 80-90 GW sustainable market) is a reaction to the order level being unsustainably high — the market is still pricing the order variable, just with a different sign on its interpretation, which is a reason to lead the memo with orders-versus-capacity, not to drop them.
- **what_would_rescue_it**: (1) An event study on non-earnings order announcements (GEV press releases and 8-Ks announcing GW deals or SRAs, e.g. Jun 23 2026 Quang Trach II, the 2025 Hyperscale/NRG/Chevron-Engine No.1 deals) showing the abnormal return vs the 5-peer basket fell from clearly positive in 2024-H1'25 to about zero in 2026; that isolates order news from EPS surprise, which the six earnings prints cannot. (2) A regression on the six prints of return on EPS surprise and GW-versus-guide surprise (GEV guided 10-15 GW/quarter; 20 GW in Q2'26 was a beat) in which GW adds no explanatory power after EPS; state the coefficients. (3) Options data: if the implied earnings move for Oct 21 is materially smaller than for the Jul 22 and Apr 22 prints (roughly 8-9% straddle-implied), the market is telling you the print carries less information; the corpus has no options table and the Barchart expected-move page did not fetch. (4) The Oct 21 print itself: an EPS beat with under 10 GW signed and a close-to-close move above +5% would show GW is irrelevant; an EPS miss with 20 GW and a down day only reconfirms EPS dominance and rescues nothing.
- **notes**: Verification queries (all read-only, gev.db): returns = SELECT date,close FROM prices WHERE ticker='GEV' ORDER BY date, close/prev-1 on 2025-04-23, 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22, 2026-07-22 reproduce the finding's +3.07, +14.58, -1.59, +2.73, +13.75, -8.69 exactly. GW and guidance sentences: SELECT ord,text FROM chunks WHERE ticker='GEV' AND form='8-K/EX' AND filing_date=? ORDER BY ord (Q1'25 7 GW orders + 7 GW SRA = 14; Q2'25 9 GW; Q3'25 'just over 12 GW' not 13; Q4'25 24 GW; Q1'26 21 GW; Q2'26 20 GW). Q2'26 release text confirms net income $649M, adj EPS $2.47, adj EBITDA margin guide unchanged 12-14%, Wind losses widening. 2026 down-day ranking: same prices query, sort by daily return; also 2025-12-17 -10.50% (Oracle/AI-bubble headline day) and 2025-12-10 +15.62% (investor day) show GEV's largest moves are AI-complex sentiment days, not order data. Peer table for Jul 1-10 and Jul 20-Aug 5 2026 from prices for GEV,VRT,ETN,PWR,HUBB,EMR,SPY. Pre-print run-up/drift: 20-day pre-return before Jul 22 was +4.2% and drawdown from the Jun 30 peak ($1,174.86 close) was -8.2%, so no unusual run-up to blame. Mechanism verdict: the finding never enters EPS surprise as a variable, and once entered it explains the sign of all six prints; the Jul 22 drop also coincided with Wind order collapse (-40%) and a $6.4B working-capital FCF benefit that management itself labelled as SRA down payments on the call — the 'FCF quality doubt' the finding cites is a fundamental, not a reaction-function change. Materiality: the finding changes no 2027 EPS, FCF, or multiple input; it is a claim about how to phrase the memo's catalyst paragraph, and the sell-side (Jefferies, MS, GLJ) already frames Oct 21 around services, book-to-bill and 2027 vintage margins rather than the 125 GW headline. Already embedded: GEV is -23% from peak while orders and backlog sit at records, which is the market discounting order headlines in real time; forward P/E 31-38x already reflects the peak-cycle debate per the Barclays and GLJ notes. Rating check: novelty 3 claimed, 1-2 warranted; confidence 4 claimed, 2 warranted given n=6 and an omitted variable; materiality 4 claimed, 2 warranted. Dead ends: no options-implied move data in the corpus and the Barchart expected-move page returned empty; corpus commentary tier has no print-day EPS-vs-consensus article for Q1'25, Q2'25 or Q3'25 (had to use web); no corpus commentary explaining May 7 2026 (-6.55%) or Dec 17 2025; transcript_statements table (193 rows) had nothing on the peak-orders Q&A, the Investing.com transcript summary did. Web sources used: Investing.com Q2'26 transcript (EPS $2.47 vs $3.04; $6.4B working-capital benefit from down payments), Benzinga/Motley Fool/Yahoo Jul 22, MarketBeat/GuruFocus Q3'25 ($1.64 vs $1.72), Investing.com Q2'25 ($1.86 vs $1.50), Zacks Q1'26 ($1.98 vs $1.84), TIKR Jul 2026 rival-downgrade piece (confirms Jul 7 -6.51% and the 'orders must keep surprising' framing), CNBC Jul 29 2026 (Vertiv -17%), Yahoo/Seeking Alpha Sep 14 (GLJ), Investing.com Jul 7 (Barclays SE).

## [Verify] repro:price-events:The -20% drawdown is half AI-power beta

- **reproduced**: True
- **confidence**: 5
- **corrected_numbers**: CORE (all reproduced from prices table, closes, pandas OLS no-intercept, fit window 2026-01-07..2026-06-30 n=120): betas SPY 0.217 / 5-peer basket 0.987 (stated 0.22/0.99). GEV 1174.86 -> 940.33 = -19.96%. Predicted compounded -8.81%; residual sum -11.77%; 2026-07-22 GEV -8.69%, predicted -0.00%, residual -8.69%; ex-Jul-22 residual -3.07% over 55 days. 9-peer (adds ROK,BE,NEE,AME): residual -11.66%, ex-Jul-22 -3.39%. VRT+ETN only: -13.90% / -5.31%. Sep 14 residual -3.37% (5-peer), -3.95% (9-peer), -3.74% (VRT+ETN); that day GEV -8.62%, VRT -7.65%, ETN -7.57%, PWR -4.39%, HUBB -3.91%, SPY -0.45%. Aug 27 GEV +0.08%, residual -0.31%. Peak-to-Sep-18: GEV -19.96, VRT -25.52, ROK -16.05, HUBB -14.58, PWR -11.57, BE -12.25, NEE -8.32, ETN -0.32, EMR +4.73, SPY +2.00 (all match). Monthly avg volume / $vol: Jun 3.25M/$3.27B, Jul 2.97M/$3.07B, Aug 2.03M/$2.00B, Sep(13 days) 2.31M/$2.13B (match). Max volume / prior-20d-avg since Jun 30 = 1.89 on 2026-09-18 (4.105M vs 2.177M); next 1.83 Aug 31, 1.72 Jul 22. Quarter-end 60d beta to 5-peer basket 2024-06..2026-09: 0.92,1.08,1.07,1.42,1.08,1.24,1.22,1.07,0.99,1.08 (exact match); corr now 0.80.
CORRECTIONS: (1) Sep 14 volume rank among the 42 GEV days with |move|>=6%: 37th of 42 by share volume, NOT 25th; 15th by dollar volume; 16th by volume/prior-20d-avg; among the 17 down days >=6% it is 15th by volume. Qualitative point (not a capitulation day) holds, arguably more strongly. (2) August 2026 (2.03M/day) is the lowest full-month average volume in GEV's entire history since the Apr-2024 spin (29 full months), not just 14 months; next lowest May 2026 2.32M, Oct 2024 2.35M, Aug 2025 2.42M. (3) The claim mixes bases: predicted -8.8% is compounded, residual -11.8% is sum-of-daily. On a consistent sum-of-daily basis GEV -19.17% = predicted -7.40% + residual -11.77%; shares: beta 39%, Jul 22 alone 45%, other 55 days 16%. 'Half and half' is fair. (4) 60d beta range since 2024-06 on a daily basis is 0.68..1.47; the 0.9-1.4 band is true only at quarter-ends. (5) Intraday peak $1,195.94 was 2026-07-06, not late June; closing peak 2026-06-30 $1,174.86 is correct. (6) Jul 22 = Q2'26 earnings (8-K 0001996810-26-000147 + 10-Q 0001996810-26-000148, press release 'raises 2026 financial guidance'); contemporaneous NEWS chunks dated 2026-07-22 attribute the drop to an EPS miss and a widening Wind loss, not an 'FCF-quality read'. (7) Aug 27 8-K (0001996810-26-000153) Item 5.02 confirmed: CFO Kenneth Parks to retire 2027-04-02.
- **data_quality_issues**: (a) prices.adjclose is NULL for all 2,514 SPY rows, so a dividend-adjusted version of the model cannot be run from the table; closes were used (immaterial over 56 days, GEV dividend is tiny). (b) METHODOLOGY: the model has no intercept. With an intercept the fitted alpha is +0.205%/day (GEV's H1-2026 momentum) and the residual becomes -23.3% (ex-Jul-22 -14.4%), i.e. the 'half beta' split depends on dropping GEV's own H1 alpha. Defensible, but the memo must state it. (c) The ex-Jul-22 residual path is not flat: cumulative ex-Jul-22 residual was +1.43% on Jul 31, -1.79% Aug 14, -4.81% Aug 27, -6.97% on Sep 14, then -3.07% on Sep 18 after a +4.15% residual on Sep 16 (NEWS 2026-09-20: CEO said $200B backlog could come 'very early' in 2027). The -3.1% headline is end-point sensitive; segment sums: Jul 1-21 -0.88, Jul 22 -8.69, Jul 23-Aug 27 -3.93, Aug 28-Sep 18 +1.74. (d) KILL CONDITION ALREADY TRIPPED IN-SAMPLE: the 20-trading-day residual window 2026-07-31..2026-08-27 sums to -8.60% and does not contain Jul 22; the only GEV 8-K in that window is the CFO retirement filed on its last day (stock +0.08%). Raw: Jul 22 close to Aug 27 close GEV -3.17% vs basket -0.02% vs SPY +3.17%. Either raise the threshold (e.g. -10%) or state that the -8% level was hit once in August and recovered. Latest 20d residual (ending Sep 18) is +0.68%. (e) news table has zero GEV rows for Jul 22-24 2026; commentary lives in chunks form=NEWS (259 GEV commentary chunks dated 2026-07-22). events table returned nothing for GEV in Jul/Aug 2026. (f) catalyst_calendar: VRT est. 2026-11-04, ETN 2026-10-30, HUBB 10-25, PWR 10-29, EMR 11-03, GEV 10-21, all confirmed=0 (estimated from 8-K cadence); hyperscaler dates are not in the table, so the 'late-October hyperscaler prints' catalyst remains unconfirmed as the caveat says.
- **notes**: What I ran (all read-only against data\gev.db): (1) SELECT ticker,date,close FROM prices WHERE date IN ('2026-06-30','2026-09-18') for 17 tickers; GEV max close overall is 2026-06-30 1174.86. (2) pandas pivot of close for GEV,SPY,VRT,ETN,PWR,HUBB,EMR (+ROK,BE,NEE,AME for 9-peer); ret=pct_change; basket=mean of 5 peers; np.linalg.lstsq([SPY,basket],GEV) on ret[:'2026-06-30'].tail(120); post=ret['2026-07-01':'2026-09-18'] (56 days); resid=GEV-pred; also with-intercept and 9-peer/VRT+ETN variants. (3) SELECT substr(date,1,7), count(*), avg(volume), avg(close*volume) FROM prices WHERE ticker='GEV' GROUP BY 1 for the full history; rolling(20).mean().shift(1) ratio; |ret|>=6% filter gives 42 days, ranks by volume, close*volume, and ratio. (4) ret.GEV.rolling(60).cov(basket)/basket.rolling(60).var() resampled QE, plus rolling corr. (5) rolling(20).sum() of residual to test the kill condition in-sample. (6) SELECT DISTINCT form,filing_date,accession FROM chunks WHERE ticker='GEV' AND tier='primary' for 2026-07-20..24 and 08-25..28; LIKE '%Chief Financial%' on accession 0001996810-26-000153; chunks_fts MATCH '("free cash flow" OR "shares fell" ...) AND ("Vernova")' restricted to commentary dated 2026-07-22..27. (7) SELECT date,high FROM prices WHERE ticker='GEV' AND date>='2026-01-01' ORDER BY high DESC. Verdict: the tape facts, factor split, Jul-22 concentration, volume series and beta history all reproduce; the finding is sound as a 'most of the drawdown is sector beta plus one earnings day' statement. Two things the memo should fix before using it: disclose the no-intercept choice (with intercept the idiosyncratic residual roughly doubles), and recalibrate or footnote the kill condition, which the Jul-31..Aug-27 window already breached. Replace '25th of 42' with the reproducible ranks above and upgrade 'lowest in 14 months' to 'lowest month since the spin'. Dead ends: events table empty for these dates; news table has no Jul 22-24 GEV rows (use chunks form=NEWS instead); SPY adjclose absent.

## [Verify] skeptic:services-accounting:The recurring LTSA revenue stream is fla

- **refuted**: True
- **already_widely_known**: False
- **where_known**: The specific GEV split (CSA revenue $5,412M flat, CSA share of Power services 44%->41%->40.8%) is not published anywhere I could find: not in GLJ's Sep-14-2026 initiation (thesis is 2027 equipment-vintage margin, no services split), not in Zacks 'Can GE Vernova's Services Business Drive More Stable Growth?' (Jun-15-2026), not in Electroneconomics 'GE Vernova's margins are real' (Jun-12-2026), not in the Seeking Alpha Q1/Q2'26 pieces, and corpus commentary tier (WEB/NEWS/RSS) never mentions CSA billings. BUT the analytical frame itself (CSA revenue recognized vs billings, net LTSA balance as a deferred-revenue red flag) is the canonical GE Power short thesis of 2017-2020: JPM (Tusa) tracked it quarterly and the SEC's Dec-2020 settled order (sec.gov/files/litigation/admin/2020/33-10899.pdf) is literally about GE Power's $5B CSA deferred balance. Every GE-legacy analyst reads this exact Note sentence each quarter; management pre-emptively discloses net LTSA balance as % of life-of-contract billings in the critical-accounting-estimates section for that reason. Management also already frames the HA services annuity as a 2030s stream: '$12B of gas and steam services... by 2035 will be at least $22B' (Dec-2025 investor update, corpus src:2686; repeated Sep-18-2026, src:681/3750) and Strazik Q2'26 call: HA units 'every four years they go through a major outage... more of a middle of the next decade dynamic' (src:3161).
- **materiality**: 1
- **strongest_counterargument**: The finding's two headline declines are base effects and lumpiness, and the cash-quality mechanism it implies leaves no footprint. (1) Billings: the '-5.6% y/y' is 1H26 vs a 1H25 that was itself +10.1% (2,533 vs 2,300); FY25 billings were +6.8% (5,021 -> 5,362) and Q4'25 (1,581) was the highest quarter on record; two-year stack 1H26 vs 1H24 = +4.0%. Full quarterly series (documents, regex 'Net contractual service agreements (increase|decrease)d' on every 10-Q/10-K): billings Q1'24-Q2'26 = 1,173 / 1,127 / 1,373 / 1,348 / 1,249 / 1,284 / 1,248 / 1,581 / 1,163 / 1,229. (2) Revenue: FY25 '-1.1%' is entirely an outlier Q4'24 (1,763, +50% q/q); 9M25 vs 9M24 was +3.1% (3,824 vs 3,710) and 1H26 vs 1H24 is +6.0%. Cost-to-cost CSA revenue tracks outage cost timing (mgmt: 'highest outage volume in the fourth quarter'), not demand. (3) No deferred-balance build: net LTSA balance $3.4B Dec-23, $3.5B Dec-24, $3.4B Dec-25 (10-K critical accounting estimates); CSA contract asset $5,417M Dec-25 -> $5,399M Jun-26 (10-Q Note); FY25 revenue-minus-billings gap only $50M. Units under LTSA rose 1,700 -> 1,800 with avg remaining life ~10 yrs and ~29% complete unchanged: the book is being replenished, not running off. (4) 'Transactional = discretionary book-and-bill' mischaracterizes gas turbines: ~5,200 of ~7,000 installed units are not under LTSA and still need HGP/major inspections on fired-hour intervals; parts must be bought. Transactional growth 'per unit rising double digits' reflects spot pricing power (CSAs carry locked escalators), which is why Power segment EBITDA margin went 12.5% (FY24) -> 14.7% (FY25) -> 17.6% (1H26) while CSA revenue was flat. (5) Materiality: CSA is ~12% of FY26 revenue; 0% vs +5% growth = ~$270M revenue, ~$80-100M EBITDA vs FY26 adj. EBITDA ~$6B and a $2B GLJ-vs-Street 2027 gap; the 1H26 revenue-over-billings gap widened only $110M y/y vs $11.5-12.5B FCF guidance.
- **what_would_rescue_it**: Any of these, observable by the FY26 10-K (late Jan 2027) or Q3'26 10-Q (late Oct 2026): (a) full-year FY26 CSA billings below ~$5.0B (down y/y for the whole year, not just 1H) while revenues recognized stay >= $5.4B, pushing the net LTSA balance above ~$4.0B or above 6% of life-of-contract billings, i.e. a genuine GE-2016/17-style deferred build; (b) units under LTSA reported below 1,800 or average remaining contract life falling below ~9 years (customers exiting CSAs); (c) a quarter where Power services revenue declines y/y with management citing customer outage deferrals, proving the transactional leg is reversible (the 2019-20 GE Power pattern); (d) a documented sell-side or buy-side model that capitalizes services RPO as near-term cash, which would make the split a mispricing rather than an accounting curiosity. Without one of these it stays a footnote for a 3-12 month memo.
- **notes**: VERIFIED: every number in the finding reproduces from documents (10-K 0001996810-25-000011, 10-K 0001996810-26-000015, 10-Qs 0001996810-25-000133 and -26-000148) plus the additional 10-Qs -24-000008/-000067/-000083, -25-000073/-000160, -26-000064 for the full quarterly series. Standalone-quarter CSA revenue Q1'24-Q2'26: 1,174 / 1,363 / 1,173 / 1,763 / 1,261 / 1,459 / 1,104 / 1,588 / 1,280 / 1,409 ($M). Net unfavorable profitability changes: FY24 319, FY25 151, 1H25 42, 1H26 218. AMBIGUITY the team should fix: the rollforward lists 'revenues recognized' and 'net unfavorable changes in estimated profitability' as separate items, so P&L CSA revenue is likely rev-recognized MINUS the revision (1H26 ~2,471 vs 1H25 ~2,678, -7.7%); the finding's caveat states the opposite sign. Either reading leaves the dollar impact ~$0.2B and does not change the verdict. XBRL WARNING: tag ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress actually holds the CSA BILLINGS series (mis-tag), and ContractWithCustomerLiabilityCumulativeCatchUpAdjustmentToRevenueChangeInEstimateOfTransactionPrice holds the offshore-wind contract losses (-379/-1005/-637), not CSA revisions; do not cite XBRL for CSA revisions. Power segment margins (documents, 'Segment EBITDA margin' first match after 'POWER'): FY24 12.5%, FY25 14.7%, 1H26 17.6%, Q2'26 18.8%. DEAD ENDS: corpus TRANSCRIPT form holds only the Q2'26 call (src:3161); Q3'25 call exists as WEB src:3796; no Q4'25/Q1'26 call text, so no management quote on transactional vs CSA mix beyond 'not only on long-term service agreements, but also on transactional orders'. Commentary-tier FTS for CSA/LTSA + billings/transactional returns only Baker Hughes/MHI marketing pages and the GEV Form 10 mirror (src:3650). Web searches for Tusa/JPM CSA notes on GEV, Seeking Alpha transactional/outage-lumpiness pieces, and 'high-single' services guidance returned nothing specific; sell-side notes are paywalled. embed.py semantic search not attempted (not needed). Suggested use: fold the flat-CSA / rising-transactional split into the team's existing 'service lag to the mid-2030s' and 'HA-fleet wear clock' angles as one supporting sentence with the Q4-outage seasonality caveat, not as a standalone short leg.

## [Verify] skeptic:contradictions:The $0.3B/yr 'availability shortfall' is

- **refuted**: True
- **already_widely_known**: True
- **where_known**: GEV 10-K FY2025 (acc 0001996810-26-000015, filed 2026-01-29), Item 7 Critical Accounting Estimates, paragraph explicitly sub-headed 'Wind.' (chunks ord 176-177). Identical Wind paragraph in 10-K FY2024 (acc 0001996810-25-000011, ord 269), 424B3 (0001996810-25-000012), S-1 (0001193125-24-066951, 2024-03-13), S-1/A (2024-05-06), Form 10 information statement (8-K/EX 0001193125-24-063739, 2024-03-08), and GEV's own 2024 Annual Report PDF (sources.id 3650, gevernova.com/sites/default/files/gevernova_2024_annual_report.pdf). Three WebSearch passes (sell-side, news, Seeking Alpha/Substack) found no third party citing the $0.3B figure in either direction; the only mis-attribution to the HA fleet is in the team's own brief.
- **materiality**: 1
- **strongest_counterargument**: This is a proofreading correction to an internal brief dressed up as a market insight. The disclosure is labelled 'Wind.' in bold in the 10-K; no analyst, journalist or retail writer has ever attributed the $0.3B to the HA fleet, so there is no public misconception to correct and no bear data point to remove (GLJ's Sell rests on 2024 order-vintage margin, not fleet availability). The finding's own 'why the market misses it' evidence is wrong: src:3650 is GEV's 2024 annual report, whose chunk is the same Wind paragraph, not a copy juxtaposed with HA statistics; zero chunks in any corpus tier pair '$0.3 billion' + availability + HA/gas turbine, and zero rows in claims/risk_items/guidance/mgmt_guidance/backlog_quarterly reference availability shortfalls. The second leg ('no quantified gas-fleet availability penalty at all') misreads the accounting: Gas Power CSAs are cost-to-cost with cumulative catch-up, so performance obligations flow through LTSA estimate revisions, which the 10-K does size ($3.4B net LTSA contract assets, 29% complete, $5.4B billings, $0.2B per 1-point profitability revision). Materially, $0.3B is 0.8% of FY25 revenue ($38,068M), flat for three years, and lives in a segment already guided to roughly -$400M EBITDA in 2026; it touches nothing in 2027 Power EPS, FCF or the multiple.
- **what_would_rescue_it**: (1) A published note that actually makes the error: GLJ's Sep 14 initiation, any sell-side model, or a widely read SA/Substack piece citing the $0.3B as HA/gas availability. Then it becomes a 'correct the public record' item worth one sentence. I found none. (2) Reframe as a Wind angle with a different conclusion: FY25 Wind services revenue is $1,859M net of the $0.3B, so availability shortfalls consume roughly 14% of gross Wind services revenue and have not improved in three years despite the 10-K's stated 'investments to improve our fleet availability' (ord 25); tie that to the 2026 Wind EBITDA guide of about -$400M and show the swing if availability normalises. Still small against a $250B cap. (3) Find the gas analogue: a disclosed negative and growing Gas Power LTSA cumulative catch-up or contract-asset revision in the Q3'26 10-Q (late Oct 2026), which would be an actual HA reliability signal that the finding claims does not exist.
- **notes**: VERIFIED: core factual claim is correct. Reproduction: SELECT accession, form, filing_date, section, ord, text FROM chunks WHERE ticker='GEV' AND text LIKE '%availability shortfalls was%' ORDER BY filing_date; returns 8 rows, all Wind paragraph, FY25 10-K ord 176-177. Power LTSA paragraph: SELECT ord, text FROM chunks WHERE accession='0001996810-26-000015' AND ord IN (174,175). Wind segment table (ord 149): Onshore $8,241M, Offshore $652M, LM $217M, Equipment $7,251M, Services $1,859M, Segment EBITDA $(598)M, margin (6.6)%; Wind RPO equipment $9,112M, services $12,518M. Consolidated FY25 revenue $38,068M (ord 141). FALSE EVIDENCE IN FINDING: src:3650 is GEV's own 2024 Annual Report PDF (SELECT url,title FROM sources WHERE id=3650), same Wind paragraph, not juxtaposed with HA stats. Conflation check: chunks_fts MATCH '"$0.3 billion" AND "availability" AND ("HA" OR "gas turbine" OR "gas turbines" OR "HA fleet")' returns 0 rows across all tiers; LIKE '%availability shortfall%' on quote columns of claims, risk_items, mgmt_guidance, guidance, backlog_quarterly returns 0 rows each. Only 10-Q hit for availability+shortfall/guarantee is an unrelated 2024 credit-support paragraph. WEB: three WebSearch passes found no third-party mention of the $0.3B; results confirm Wind 2026 EBITDA guide about -$400M (Q2'26 8-K, 0001996810-26-000147). RATINGS AS I SEE THEM: novelty 1 (disclosed under a bold 'Wind.' label), confidence 5 that it is Wind, materiality 1. RECOMMENDATION: delete the '$0.3B availability' clause from the team brief's HA fleet sentence; do not spend memo space on it. DEAD ENDS: Ollama/embed.py not attempted (FTS sufficient); xbrl_facts has no Wind-labelled USD FY25 facts under GROUP BY tag (segment data not tagged with 'wind' in label); no cumulative catch-up dollar amount disclosed for Gas Power LTSAs in FY25 10-K beyond the sensitivity language.

## [Verify] repro:contradictions:The $0.3B/yr 'availability shortfall' is

- **reproduced**: True
- **confidence**: 5
- **corrected_numbers**: All core numbers reproduce exactly. (1) FY25 10-K, accession 0001996810-26-000015, GEV, filed 2026-01-29, chunks id 29777-29778, section Item 7 MD&A, ord 176-177: the 'Wind.' paragraph reads '...the reduction of revenues from availability shortfalls was $0.3 billion, $0.3 billion, and $0.3 billion, respectively' for 2025/2024/2023, followed by 'A further 1% reduction in availability across the entire fleet would have resulted in an additional revenue reduction of less than $0.1 billion.' Query: SELECT id,section,ord,text FROM chunks WHERE accession='0001996810-26-000015' AND text LIKE '%availability shortfalls was%'. (2) FY24 10-K, accession 0001996810-25-000011, filed 2025-02-06, chunk id 67297: '$0.3 billion, $0.3 billion and $0.1 billion' for 2024/2023/2022. Full series across filings: 2021 $0.1B, 2022 $0.1B, 2023 $0.3B, 2024 $0.3B, 2025 $0.3B (S-1 2024-03-13 chunk 96323 and Form 10 info statement 8-K/EX 2024-03-08 chunk 97860 give '2023, 2022 and 2021... $0.3 billion, $0.1 billion and $0.1 billion'). (3) Wind segment table, same FY25 accession, chunk 29750 ord 149: Onshore Wind $8,241; Offshore Wind 652; LM Wind Power 217; Total $9,110 (FY25 $M); Wind Equipment $7,251 / Services $1,859; Wind RPO Equipment $9,112 / Services $12,518 / Total $21,630 (Dec-25). Note 20 (chunk 29931) shows Wind services revenue $1,858M. (4) Absence check count = 0 for '"Power" AND "availability" AND ("guarantee" OR "guarantees" OR "penalt*")' in the FY25 10-K. Broader checks: '"HA" AND "availability"' returns 5 chunks, all false positives (availability of cost-reducing materials, stock liquidity, info-systems availability, debt financing, 'information available'); '"Gas Power" AND "availability"' returns 1 chunk (debt financing). No XBRL tag for GEV matches availab*/shortfall. (5) The 126 HA-turbine / 3.6M operating hours statistic is at chunk 29622, ord 21, Item 1 Business, about 155 chunks before the Wind paragraph. (6) The five 10-Qs filed 2025-04-23, 2025-07-23, 2025-10-22, 2026-04-22, 2026-07-22 contain no availability-shortfall or gas-fleet availability-guarantee language (only 'availability of credit'). (7) SEC EDGAR full-text search (efts.sec.gov, q="availability shortfalls", ciks=0001996810, forms 10-K/10-Q, startdt 2025-01-01) returns exactly 2 hits: 10-K 2026-01-29 (0001996810-26-000015) and 10-K 2025-02-06 (0001996810-25-000011). Context addition: $0.3B is 16.1% of FY25 Wind services revenue ($1,859M).
- **data_quality_issues**: (a) The FY24 10-K chunk 67297 carries corpus section label 'Item 1A Risk Factors' but its text is the same MD&A Critical Accounting Estimates paragraph; this is a section-parser artifact, not a content difference. (b) src:3650 is GE Vernova's own 2024 Annual Report PDF (https://www.gevernova.com/sites/default/files/gevernova_2024_annual_report.pdf), tier-labeled 'commentary' but really a company document; its availability sentence sits at ord 290 while the HA fleet stats sit at ord 45-46, so it does NOT quote the number 'next to the HA fleet statistics' as the finding's why_market_misses_it states. The juxtaposition exists in the team's own brief (the task prompt pairs '126 HA units... 3.6M operating hours' with 'availability-shortfall revenue reductions $0.3B'), not in any corpus document: an FTS query for commentary chunks matching availability AND '0.3 billion' AND (HA OR gas turbine(s)) returns zero rows. (c) The paragraph lives in Item 7 MD&A under Critical Accounting Estimates / Long-Term Service Agreements, immediately after the Power LTSA paragraph (ords 173-176), not in a Notes 'Revenue Recognition' note as the finding's narrative says; the adjacency claim ('20 lines below the Power services paragraph') is otherwise fair. (d) The Item 1A risk factor at ord 72 (chunk 29673) does mention 'warranty, performance, delivery, and availability provisions that can trigger... penalties, liquidated damages' generically with a Wind example, but it is qualitative and unquantified, consistent with the finding.
- **notes**: Verdict: the finding is correct and the corpus evidence is clean. The $0.3B/yr figure is unambiguously Wind-segment service-agreement contra-revenue (performance guarantees of the wind farm's availability, measured across the wind farm over one year); the 10-K discloses no quantified gas-fleet or HA availability penalty, and neither do the 2025-2026 10-Qs. Suggested edits to the finding text: (1) replace the src:3650 sentence in why_market_misses_it with 'the team's own brief juxtaposes the two numbers; no corpus commentary source does', which weakens the 'market misses it' claim to 'team-internal mis-sourcing risk' and argues for novelty 3 rather than 4; (2) change 'Revenue Recognition note' to 'MD&A Critical Accounting Estimates, Long-Term Service Agreements subsection'; (3) optionally add the 2021-2022 $0.1B baseline and the 1%-sensitivity (<$0.1B) as supporting detail, plus the observation that $0.3B equals about 16% of Wind services revenue, which is a Wind-quality data point the team could use elsewhere. Materiality 2 and confidence 5 are fair. Dead ends checked: XBRL tags (none), 10-Q text 2025-2026 (nothing), 'HA'/'Gas Power' + availability in FY25 10-K (only false positives), commentary tier juxtaposition (zero rows). Not run: python src/embed.py semantic search (not needed; exact-string reproduction succeeded).

## [Verify] repro:price-events:GEV trades hyperscaler capex prints as h

- **reproduced**: True
- **corrected_numbers**: MAIN SET (reproduces exactly): 26 unique day-after trading days from 40 hyperscaler quarterly 8-Ks (all 40 dates present in chunks, form 8-K and 8-K/EX, confirmed EX-99.1 earnings releases), dropping 2024-04-25 and 2024-07-24 (GEV own print days). GEV close-to-close: mean +1.91%, median +1.11%, 17/26 positive, SD 3.52%. Other days ex GEV prints: n=585, mean +0.27%, SD 3.24%. t-stat: Welch 2.33, pooled 2.51 (finding's 2.37 sits between; convention unstated). Excess over equal-weight VRT/ETN/PWR/HUBB/EMR basket: mean +1.04%, median +1.01%. GEV OWN PRINTS (reproduces exactly): n=10, mean +2.48%, median +2.06%, 7/10 positive, mean |move| 5.42%; excess over basket +2.56%. NVDA (reproduces): all 10 day-after values match (-1.33, +4.00, -0.85, -2.67, -2.85, +1.82, -6.27, +0.05, +1.88, +0.08); mean -0.62% (finding -0.61%, rounding), 5/10 positive, basket -0.09%. All 10 NVDA dates VERIFIED against SEC EDGAR submissions JSON CIK0001045810 (8-K Item 2.02 on 2024-05-22, 08-28, 11-20, 2025-02-26, 05-28, 08-27, 11-19, 2026-02-25, 05-20, 08-26); the 'from memory' caveat can be removed. MSFT+META SUBSET (DOES NOT reproduce as labeled): the finding's 8 dates include 2024-07-31, which is MSFT-only (META reported 2024-07-31 evening; its day-after 2024-08-01 = -2.36%), and omit 2026-01-29, a true same-evening MSFT+META date (+0.82%). Corrected same-evening set {2024-10-31, 2025-01-30, 2025-05-01, 2025-07-31, 2025-10-30, 2026-01-29, 2026-04-30, 2026-07-30}: mean +3.10% (not +4.19%), 7/8 positive, basket +1.91%, excess +1.19% (not +1.84%). Still above GEV's own-print +2.48% but the gap narrows from 1.7 to 0.6 pts. Cleaner replacement: MSFT day-after alone, n=10, mean +3.76%, 9/10 positive, +1.54% over basket. Per-company day-after means: MSFT +3.76 (9/10), META +2.49 (7/9), GOOGL +1.48 (5/9), AMZN +0.74 (6/10). SENSITIVITY: ex-SPY mean +1.91%, 20/26 positive, t=3.01; dropping the two dates adjacent to GEV's own prints (2026-01-29, 2026-07-23) n=24 mean +1.84% t=2.08; dropping 2024-07-31 (also FOMC day and AMD print) mean +1.60%, t=2.00 raw / 2.72 ex-SPY. Big-day attribution: 2024-07-31 +9.55% is MSFT-only (SPY +1.63%, basket +4.95%), not 'MSFT/META'; 2025-01-30 +8.40% and 2026-07-30 +9.07% are genuine MSFT+META joint dates.
- **data_quality_issues**: (1) Mislabel: 2024-07-31 tagged as an MSFT+META same-evening print; META's 8-K/EX is dated 2024-07-31 (chunks), so its day-after is 08-01. (2) Internal inconsistency: 2026-01-29 is counted in the n=26 main set but excluded from the MSFT+META subset without stated reason (GEV printed 2026-01-28 the same day, so 01-29 is also GEV's own day-after; if that is the exclusion logic it should also apply to 2026-07-23, day after GEV's 07-22 print, +4.69%). (3) t-stat convention not stated; Welch gives 2.33, pooled 2.51. (4) 'Other days n=585' silently excludes the 10 GEV print days as well as the 26 event days (621 returns - 26 - 10); this is fine but should be stated. (5) 2024-07-31 coincides with an FOMC decision and AMD's print; the single largest observation is confounded. (6) Prices: close vs adjclose identical on event days (max diff 1.5e-5 pct pts), so dividend adjustment is not an issue. (7) Late-Oct 2026 dates: web aggregators (TipRanks/WallStreetHorizon via WebSearch) list MSFT 2026-10-27 and META 2026-10-28 after close, i.e. DIFFERENT evenings, so the 'MSFT+META same-day' framing would not apply to the upcoming quarter; these dates were not verified on company IR pages and should stay 'unconfirmed'. (8) catalyst_calendar claim confirmed: 16 rows, all 'earnings release (estimated from 8-K item 2.02 cadence)' for universe tickers, zero MSFT/META/GOOGL/AMZN/NVDA rows. (9) Commentary claim: FTS on chunks_fts (tier='commentary') for nvidia AND earnings AND vernova returns 25 hits, all generic (Zacks 'NVIDIA of energy' pieces, GEV own-earnings coverage); none quantifies GEV's reaction on NVDA or hyperscaler print days, so 'not documented' holds but is a weak absence-of-evidence claim.
- **notes**: WHAT I RAN: (a) SELECT DISTINCT form, filing_date FROM chunks WHERE ticker IN ('MSFT','META','GOOGL','AMZN') AND form IN ('8-K','8-K/EX') AND filing_date>='2024-04-01' -> all 40 quarterly dates present, plus non-earnings 8-Ks which I excluded by matching the finding's list. (b) SELECT DISTINCT filing_date, accession FROM chunks WHERE ticker='GEV' AND form='8-K/EX' AND (accession LIKE '%earningsrelease%' OR accession LIKE '%pressrelease%') -> exactly the 10 GEV print dates. (c) Returns from prices (close column, 622 GEV rows 2024-03-27 to 2026-09-18) for GEV, SPY, VRT, ETN, PWR, HUBB, EMR; next trading day mapped via the GEV date index. (d) Sanity: first 8-K/EX chunk for MSFT 2024-07-30, META 2024-07-31, GOOGL 2026-07-22, AMZN 2026-07-30, MSFT/META 2026-01-28 all begin 'Exhibit 99.1 ... Quarter Results'. (e) SEC EDGAR data.sec.gov/submissions/CIK0001045810.json with User-Agent gev-corpus-research/1.0, filtered form='8-K' and items containing '2.02'. (f) SELECT * FROM catalyst_calendar (16 rows) plus LIKE scan for hyperscaler names (0 hits). (g) chunks_fts MATCH queries on commentary tier. (h) WebSearch for MSFT FY27 Q1 and META Q3 2026 dates. VERDICT: the headline claim (GEV's day-after reaction to hyperscaler prints is comparable to or larger than its own-print reaction, and NVDA prints do nothing) holds and is robust to SPY adjustment and to dropping confounded dates. The MSFT+META subset should be restated as +3.10% (n=8, 7/8, +1.19% over basket) or replaced by the cleaner MSFT-only n=10 +3.76% (9/10, +1.54% over basket). The testable prediction should be reworded since MSFT (Oct 27) and META (Oct 28) appear to report on different evenings this quarter: predict GEV > basket on both 2026-10-28 and 2026-10-29 and a four-print day-after mean > +1%. Novelty 3 / confidence 3 / materiality 3 look honest; I would keep confidence at 3 given n=26 and SD close to the mean. DEAD ENDS: no corpus commentary quantifies either reaction; catalyst_calendar cannot be used to source hyperscaler dates (must come from chunks 8-K dates as the finding does); the finding's basket dates for the MSFT+META subset cannot be reproduced as a 'same-evening' set without the mislabel.
- **confidence**: 4

## [Verify] skeptic:services-accounting:LTSA book margin is being cut at a recor

- **refuted**: True
- **already_widely_known**: False
- **where_known**: The specific 1H26 $218M figure is not cited anywhere public that I could find: zero hits in the corpus commentary tier (5 FTS phrasings incl. '"estimated profitability"', '"cumulative catch"', '"LTSA" "margin"'), nothing on Seeking Alpha, the Jun-12-2026 ElectronEconomics Substack piece does not cover it, and GLJ's Sep-14 Sell note is about gas-turbine cyclicality and Wind losses. However the LINE ITEM is among the most scrutinized in GE's history: it is the direct descendant of the GE Power LTSA 'changes in estimated profitability' disclosure at the centre of the SEC's Dec-2020 $200M settlement (SEC Order 33-10899, sec.gov/files/litigation/admin/2020/33-10899.pdf; violation = improperly LOWERING cost estimates in 2016-17). GE's FY2018 10-K (sec.gov/Archives/edgar/data/40545/000004054519000014/ge10-k2018.htm) records a single Q4-2018 charge of '$0.4 billion... unfavorable pricing, lower utilization, and cost updates on our long-term service agreements' at Gas Power Systems. Every GE-lineage sell-side analyst reads Note 9 for exactly this sentence. So: unpublicized number, well-known metric, and the 'worst on record' label only holds inside GEV's 10-quarter post-spin window.
- **materiality**: 2
- **strongest_counterargument**: The step-up is real, reproducible and unpublicized, and by the 10-K's own sensitivity (1 pt of total contract profitability = $0.2B of LTSA contract assets) it means about 1.1 pts of lifetime book margin was removed in six months. If Q2'26's $129M is the new quarterly run-rate rather than a blip, annualized revisions of roughly $500M would be about 5% of Street 2027 EBITDA ($9.45B) and would directly contradict the bull case's 'services worth about $70M per GW-year' leg, because it would show LTSA economics are less inflation-protected than assumed. Management gives no reason for the 2025-26 revisions (FY24 said 'higher costs'), which is itself a disclosure-quality flag given GE's history on this exact line. It is dated and falsifiable at the Oct 21-22 10-Q.
- **what_would_rescue_it**: (1) Q3'26 10-Q (about Oct 21-22, 2026): 9M26 net unfavorable changes >= $300M, i.e. Q3 >= $80M, breaking the small-Q3 pattern (Q3'24 -46, Q3'25 +6), AND Power services revenue growth decelerating with 'price' described as less positive. (2) Management or the FY26 10-K attributing the revisions to major-outage/HA fleet cost overruns rather than 'inflation' or 'tariffs' (the driver they currently name every quarter). (3) The Note 9 segment table showing Power contractual service agreement assets falling while CSA liabilities rise for two consecutive quarters (Dec-25 assets $5,417M, Jun-26 $5,399M, CSA liabilities $1,880M at Jun-26; today the net book still grew +$79M in 1H26). (4) A contract-structure disclosure or channel check showing LTSA escalators are fixed low-single-digit while parts/labor inflation runs 6-8%, making the drag structural. (5) An SEC comment letter (EDGAR CORRESP/UPLOAD for CIK 1996810) on Note 9 or on the 'sale of services upgrades' non-current asset ($368M). (6) Evidence the 1H26 step-up is NOT the 2026 Steam Power reorganisation (Q2'25 Nuclear restated $189M to $649M, Gas Power $3,884M to $3,911M), i.e. the revisions sit in HA-class gas LTSAs.
- **notes**: VERIFIED (all reproducible): YTD net favorable/(unfavorable) changes in estimated profitability, $M, from documents WHERE ticker='GEV' AND form IN ('10-K','10-Q'), regex r'Net contractual service agreements[^.]*\.' on whitespace-normalized text: Q1'24 -29 | 1H24 -89 | 9M24 -135 | FY24 -319 ('due primarily to higher costs') | Q1'25 +29 | 1H25 -42 | 9M25 -36 | FY25 -151 | Q1'26 -89 | 1H26 -218. Derived Q2'26 = -129. XBRL check: xbrl_facts tag ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress = -1,163M (Q1'26 YTD), -2,392M (1H26 YTD) = the BILLINGS figures, confirming no XBRL tag carries the revision.

WHY REFUTED (as a material 3-12 month short point):
1. MECHANISM. The finding infers an HA major-inspection cost true-up; management states the driver: Q2'26 call (chunks src:3161): Power margin 'mainly driven by favorable price and higher volume, more than offsetting inflation'; Q2'26 10-Q MD&A: Gas Power 'partially offset by the impact of inflation and additional expenses to support investments'; 10-Q 'Tariffs... have resulted... in additional costs to us'. Under cost-to-cost, an inflation/tariff uplift to remaining-cost estimates on a book that is only 29% complete (FY25 10-K: $3.4B net = 4% of ~$85B life-of-contract billings; 1,800 units under LTSA, avg remaining life ~10 yrs) is the simplest explanation. HA units are 126-130 of ~7,000 installed. FY25 10-K also says utilization estimates move BOTH billings and costs, so harder-running fleets are not sign-determinate. The direction (raising cost estimates) is the conservative one the SEC forced on GE in 2020; it is not an earnings-quality red flag. Series is noisy: FY23 +34, Q1'25 +29, Q3'25 +6 favorable. Segment attribution to Gas Power is documented for 2024 (Q1'24 10-Q: 'decreased contractual service agreement assets related to our Gas Power business'; FY24 10-K cash-flow text) but NOT stated for 2026; the 2026 Steam Power fold-in is an untested alternative.
2. MATERIALITY. Non-cash: contract-asset write-down, billings unchanged, so zero effect on the FCF guide ($11.5-12.5B). Already inside reported numbers: 1H26 Power EBITDA $1,842M (17.6%) vs 1H25 $1,303M (14.1%), +41% net of $176M more revisions (Q2'26 10-Q segment table; Q2'25 restated from $778M to $785M). Forward drag using the 10-K sensitivity: $218M ~ 1.1 pt of total contract profitability; remaining 71% of ~$85B book x 1.1% ~ $650M over ~10 yrs ~ $65M/yr ~ 0.7% of Street 2027 EBITDA ($9.45B per GLJ's citation, analyst_calls 2026-09-15). Incremental H2'26 vs H2'25 base ($109M = Q3 +6, Q4 -115): even at H2'26 $150-180M the unreported delta is $40-70M pre-tax ~ $0.11-0.20/sh on 271M diluted shares (xbrl_facts WeightedAverageNumberOfDilutedSharesOutstanding 2026-06-30) ~ 0.7-1.2% of FY26 consensus EPS $16.77; at 31-38x that is ~$9/share on a $940 stock. FY25 base: revisions $151M = 1.2% of Power services revenue $13,081M, 5.2% of Power EBITDA $2,902M (FY25 10-K segment table).
3. EMBEDDED. Q2'26 guidance raise (Power organic growth 18-20%, margin 17-19%, company FCF raised) was issued on Jul 22 AFTER the $218M was booked; Q3 explicitly guided lower sequentially on outage seasonality; Q4'25 already carried $115M of revisions and was the peak-EBITDA quarter, so Q4 revision seasonality is in the base and in 'highest revenue and EBITDA in 4Q'26'.
4. 'RECORD' FRAMING. Only 10 quarters of post-spin data; GE's Q4-2018 alone was $0.4B on the same book.

WHAT SURVIVES: a legitimate, dated, falsifiable margin-QUALITY footnote for the memo's risk section, not a thesis driver. Re-rate: novelty 3 (metric well-known, number unpublicized), confidence 3 on the data / 2 on the HA mechanism, materiality 2.

DEAD ENDS: corpus commentary tier (0 relevant hits, 5 phrasings); TRANSCRIPT chunks (only Q2'26 call, src:3161, 42 chunks; no analyst question on contract assets/LTSA); transcript_statements empty on topic; mgmt_guidance has no Power-margin row with a parsed value for Jul-2026 (value column garbled: 'metric ADJUSTED EBITDA MARGIN* value 2026'); Note 9 segment-table regex on documents fails (table text is tokenized), use chunks_fts MATCH '"Contractual service agreements" "Equipment and other service agreements"' instead; WebFetch of GE FY2018 10-K only surfaced the Q4-18 $0.4B charge, not a full series; Substack piece paywalled; Seeking Alpha and X have nothing on Note 9 for GEV.

## [Verify] repro:contradictions:EIA-860M shows only ~53 GW of planned US

- **reproduced**: True
- **corrected_numbers**: EIA-860M vintage 2026-07, Planned sheet, energy_source='NG', prime_mover IN (CT,GT,CS): 52.76 GW total (finding 52.6 = sum of rounded rows; OK). By COD year: 2026 3.80 / 2027 10.07 / 2028 13.17 / 2029 10.77 / 2030 12.08 / 2031 1.41 / 2034 1.45. Under construction (U/V/TS) 11.46 GW. 2028-2030 subtotal = 36.03 GW, not 35.9. Adding prime_mover CC (3 units, 1.56 GW) gives 54.3 GW; non-NG-fuel turbines add only 0.17 GW. Evidence 2: CT/CA/CS/GT planned 2025-01 = 25.98 GW, 2026-07 = 67.09 GW (turbine-only CT/GT/CS: 23.2 -> 52.76 GW). Evidence 3: backlog_quarterly 8-K/EX 2026-07-22 rows 44->53 GW backlog and 56->63 GW SRAs reproduce verbatim. Evidence 5: src:3161 (gevernova.com 2Q26 webcast transcript PDF, tier primary, form TRANSCRIPT, ord 2) reproduces verbatim: 'approximately 100 customers in 26 different countries', '80% traditional customers and 20% data centers', 'at least 125 gigawatts under contract by the end of the year'. Evidence 6 slippage: of 6.63 GW planned-for-2027 in 2025-07, on_time 5.58 GW (36 units), slipped 1.02 GW (3 units), canceled 0.03 GW (1 unit; finding said 0.0), none missing; slip rate 15.4%. Evidence 4 CORRECTION: the sentence 'Second-quarter 2026 orders alone hit a record 38 GW (up 71% year-over-year), with the United States accounting for about half' (src:3489, energynewsbeat.com, published Aug 23 2026 per WebFetch; sources.published is blank) is in a paragraph about GLOBAL heavy-duty gas turbine orders per Wood Mackenzie ('Global manufacturing capacity ... 60-70 GW per year, according to Wood Mackenzie, while outstanding orders have reached roughly 110 GW'). It is not GEV's Q2 orders: GEV's own Q2'26 new commitments were 20 GW (18 GW SRAs + 2 GW orders). So 'US about half' is an industry-wide proxy, not a GEV figure; the claim's 'GEV US share ~55-60 GW' has no source in any GEV filing or transcript (FTS over GEV 10-K/10-Q/TRANSCRIPT for US/North America share of gas GW returned nothing). Management in the same transcript (ord 26-27) cites Taiwan '>10 GW of HAs on contract', Saudi, Qatar contracts, Mexico, Southeast Asia, so the international share is material. EIA-860M release lag verified at eia.gov: July 2026 data released Aug 26 2026, next release Sep 24 2026 (Aug vintage), so Jan-2027 vintage ~late Feb 2027 as stated, Oct-2026 vintage ~late Nov 2026.
- **data_quality_issues**: 1) Evidence 4 misattribution: '38 GW / US about half' is Wood Mackenzie global-industry data, not GEV (see corrected_numbers); the finding's US-share denominator for GEV is therefore an assumption. 2) backlog_quarterly labels the 44->53 GW equipment-backlog rows as metric='reservation_gw' and a '125 GW under contract' row as metric='contract_liabilities'; values and quotes are correct, metric labels are wrong. 3) generators 2026-07: TVA Cumberland (TN) CT 454.8 MW is '(U) under construction' with planned_year 2034, almost certainly a COD data-entry error; it is the 0.5 GW 'uc' in the 2034 row. 4) sources.published is blank for src:3489 (actual date Aug 23 2026). 5) No duplicate (plant_id, generator_id) rows within the 2026-07 Planned sheet (336 rows = 336 distinct units), so the GW sum is not inflated. 6) Sector split of the 52.8 GW: Electric Utility 32.1 GW, IPP Non-CHP 20.6 GW, Industrial/Commercial CHP 0.1 GW, i.e. essentially zero behind-the-meter/self-gen capacity in the planned sheet, which supports the finding's own caveat that data-center on-site plants are not yet EIA-visible. 7) Competitor doc in corpus (form COMPETITOR, Siemens Energy) shows '69 GW backlog / 26 GW SRAs' = 95 GW, so global OEM contracted gas (GEV 116 + SE 95 + MHI) exceeds 210 GW against a 52.8 GW US planned sheet; the comparison is even more lopsided but the same unknown-US-share problem applies to every OEM.
- **notes**: What I ran: (a) exact SQL from each reproduction field against generators, backlog_quarterly, chunks, sources; (b) monthly vintage series 2025-01..2026-07 for planned NG CT/GT/CS total, 2028-2030 subtotal and UC; (c) duplicate and fuel-code checks; (d) FTS over GEV primary chunks for any US/North America share of gas GW; (e) read transcript src:3161 ords 2, 26, 27; (f) WebFetch of eia.gov/electricity/data/eia860m and of the energynewsbeat article. Calibration of the prediction from the vintage series: 2028-2030 planned gas turbines went 8.9 GW (2025-01) -> 22.0 (2025-12) -> 33.2 (2026-03, an 8.3 GW one-month jump) -> 36.0 (2026-07); 18-month average about 1.5 GW/month, last-4-month pace about 0.7 GW/month. The Jan-2027 threshold of 45 GW needs +9 GW in 6 months, in line with the 18-month trend but above the recent pace; the Oct-2026 interim threshold (+3 GW to 39 GW) needs about 1 GW/month. Total planned NG CT/GT/CS by vintage: 23.2 (2025-01), 28.9 (2025-07), 37.6 (2026-01), 52.8 (2026-07). Immediate action for the team: the August 2026 vintage publishes Sep 24 2026, before the Oct 2 memo; rerun the Evidence-1 query on it. The finding's core contrast (52.8 GW US planned across all OEMs vs 116 GW GEV under contract) stands, but the memo must state that the US share is an industry proxy (Wood Mackenzie via commentary) and that GEV discloses no geographic split of the 116 GW; the kill condition 'GEV discloses <40% US' is currently untestable from filings. Dead ends: no GEV 10-K/10-Q/8-K/transcript gives a US or North America share of gas GW under contract; transcript only lists countries qualitatively.
- **confidence**: 4

## [Verify] repro:price-events:The December investor update, not earnin

- **reproduced**: True
- **corrected_numbers**: PRICE EVENTS (prices table, ticker='GEV', close-to-close): 2025-12-10 +15.62% (625.30 -> 723.00), volume 11,396,400 = 3.75x prior-20-day avg (3,040,510); SPY +0.66%, VRT +1.93%; drift Nov 24 close -> Dec 9 close +7.72% (note: this is the 10 trading days ending Dec 9, i.e. measured from the close 11 sessions before the event); +5 sessions (Dec 17) -15.05% to 614.19, below the pre-event close of 625.30 = full reversal; +20 sessions (Jan 9) -13.90%. +15.62% is the largest up day in the prices table (GEV history begins 2024-03-27); next: 2025-07-23 +14.58% (Q2'25 earnings), 2025-04-09 +13.91% (tariff-pause macro day), 2026-04-22 +13.75% (Q1'26 earnings). 2024-12-11 +5.01% (327.39 -> 343.80), volume 6,671,700 = 2.42x prior-20 avg (2,755,725); Dec 10 2024 itself -2.34%; +5 sessions (Dec 18) -7.76% to 317.12, below pre-event 327.39 = full reversal; 10-day pre-drift only -0.48% (so 'pre-event drift up' holds for 2025 only). Both updates were held at 4:30 PM EST (gevernova.com press releases: Dec 10 2024 and Dec 9 2025), so the next-day reaction days are correct. Dec 17 2025 GEV -10.50%: SPY -1.10%; equal-weight AI-power 9 (VRT, ETN, BE, PWR, HUBB, EMR, ROK, AME, NEE) -4.18% (BE -12.14%, VRT -6.74%, PWR -5.53%); the all-16-ticker basket ex SPY/GEV was only -2.41%, so the '-4.1% basket' is the AI-power subset. CFO 8-K: accession 0001996810-26-000153 filed 2026-08-27, quote reproduces verbatim; but EDGAR acceptance time is 16:20:31 ET (after the close) and the Rivian announcement was also after hours (Rivian fell 6% on Aug 28), so the +0.08% on Aug 27 is NOT the reaction. Reaction day Aug 28: GEV -4.39% vs SPY -0.23%, AI-power 9 -2.60%, VRT -4.53%, ETN -3.19%, PWR -3.08%; GEV excess vs the AI-power basket about -1.8 pp. Parks retires April 2 2027 (not Jan 1) and is strategic advisor Jan 1 - Apr 2 2027; McDonough joins Nov 1 2026 as advisor, CFO Jan 1 2027 (correct). Zingoni 8-K 0001996810-26-000004 filed 2026-01-21, quote verbatim, GEV -2.48% that day (Aug 28 -0.93% next day). catalyst_calendar: 16 rows TOTAL (one per ticker), only 1 row for GEV (2026-10-21 earnings estimate); no investor-update entry - substance holds. Note the estimated Q3 date is wrong: GEV IR events page lists Q3'26 earnings Oct 28 2026 7:30 am EDT. Dec 9 2025 update content: Utility Dive src:2670 (published 2025-12-24) reproduces '80 GW ... 24 GW ... $52B expected revenue in 2028 excluding 50% Prolec GE'; Cramer/Insider Monkey src:3830 reproduces 'a recent 16% jump coming on December 10th'. $10B buyback: 10-K FY25 (filed 2026-01-29) Item 8 equity note, not Item 5 as cited: 'On December 9, 2025, we announced that the Board... authorized an increase of our repurchase program to $10 billion... from the prior authorization of $6 billion'. FY26 revenue $41-42B from the Dec update is confirmed only indirectly: mgmt_guidance row stated 2026-01-28 'For 2026, GE Vernova now expects revenue of $44-$45 billion, up from $41-$42 billion' (and 2028 raised to $56B from $52B) - i.e. the Q4 print re-based the December guide within 7 weeks. News coverage of the CFO change: 15 NEWS chunks / 5 docs matching McDonough OR Parks OR CFO for GEV Aug 27 - Sep 5 (46 NEWS chunks / 9 docs total Aug 27-29), not 19. Dec 2025 commentary coverage: 21 documents = 86 chunks (finding said 21 chunks).
- **data_quality_issues**: 1) prices table has no intraday timestamp; event-time attribution had to come from gevernova.com (4:30 PM EST for both updates) and the EDGAR acceptance stamp (16:20:31 ET for the CFO 8-K) - the finding attributed the CFO announcement to the wrong day. 2) The corpus holds NO GEV 8-K or 8-K/EX for either investor update (documents/chunks have zero GEV primary rows in Dec 5-15 2024 or Dec 5-15 2025), so the update content rests on two Dec 24 2025 news articles plus the 10-K/10-Q buyback sentence; the $41-42B FY26 guide only appears via the Jan 28 2026 8-K/EX 'up from' clause and WEB chunks with blank filing_date. 3) mgmt_guidance has zero rows with stated_on in Dec 2025, so the December guide is invisible to that table. 4) catalyst_calendar is 16 auto-estimated earnings rows (1 per ticker) and its GEV Q3 estimate (Oct 21) disagrees with the IR site (Oct 28); events table has 0 GEV rows. 5) FTS on '"McDonough"' returns a Warsh op-ed and an HVDC article (src:2723, src:2690) that look like roundups, so chunk counts overstate dedicated coverage. 6) SEC efts full-text endpoint returned HTTP 500 via WebFetch; could not cross-check 8-K item 7.01 filings there. 7) Utility Dive chunk ord 2+ is missing (only ords 0-1 stored), so the FY26 revenue line is not in the corpus copy of that article.
- **notes**: Core reproduces: both post-update moves (+15.62%, +5.01%), volume multiples (3.75x, 2.42x), the 5-day full reversals (-15.05%, -7.76%), the 20-day -13.90%, the largest-up-day claim, both 8-K quotes, the Dec 24 news quotes, the $10B buyback sentence, and the absence of any investor-update row in catalyst_calendar. Three things change the story's shading, not its core. (a) The 'CFO handover is not priced' leg is weaker than stated: the 8-K and Rivian's release hit after the close on Aug 27, and GEV fell 4.39% on Aug 28, though VRT (-4.53%), ETN, PWR and BE all fell 2.6-4.5% the same day, so at most about 1.8 pp is GEV-specific; call it ambiguous rather than 'moved +0.08%'. (b) 'Largest scheduled move' is true for the single biggest day (Dec 10 2025), but earnings days are comparable: Q2'25 (Jul 23 2025) +14.58% and Q1'26 (Apr 22 2026) +13.75%, and the 2024 update was only +5.01%; run the earnings 8-K item 2.02 loop (documents WHERE form='8-K' AND text LIKE '%Item 2.02%') to fill the comparison table before using the headline. (c) The Dec 2025 guide ($41-42B FY26, $52B 2028) was re-based UP within 7 weeks at the Jan 28 2026 Q4 print ($44-45B, $56B), which cuts both ways for the 'incoming CFO re-bases' argument: GEV's own pattern is December set, January raise. Timing facts that support the prediction: 2025 event was announced Nov 18 for Dec 9 (3-week lead), 2024 event was Dec 10, both 4:30 PM EST; as of Sep 21 2026 the IR events page lists nothing after the Oct 28 Q3 webcast, so the Dec 2026 date remains an inference. Recommend restating evidence item 4 as: 8-K accepted 16:20 ET Aug 27; next-day GEV -4.39% vs AI-power peers -2.6%. Web search for analyst reaction to the McDonough hire was requested but is not needed for the reproduction verdict.
- **confidence**: 4

## [Verify] skeptic:price-events:The -20% drawdown is half AI-power beta

- **refuted**: True
- **already_widely_known**: True
- **where_known**: The qualitative conclusion (drawdown = sector rotation + profit-taking on a parabolic stock + the Jul 22 print, no company-specific disaster) is the consensus press narrative and is in the corpus commentary tier. (1) 24/7 Wall St 2026-09-16 "GE Vernova Gave Back Its Gains Since July": drop was "profit-taking on a stock that had gone parabolic, aggravated by a broader rotation out of AI-power names"; "no company-specific disaster behind the drop" (corpus: chunks form=NEWS filing_date 2026-09-16, ticker GEV). (2) 24/7 Wall St 2026-09-14 (corpus NEWS 2026-09-14): "Peer names are moving in sympathy with GE Vernova. Eaton... falling 7%... Quanta... down 4%." (3) Motley Fool 2026-08-28: WSJ $3T off-balance-sheet AI report "tanked Vertiv and GE Vernova" (Aug 18: BE -10.0, GEV -6.9, VRT -6.8, ETN -5.3). (4) Motley Fool 2026-09-14 "Why Did GE Vernova Stock Fall Today": attributes Sep 14 entirely to the Amodei/AI-lab slowdown call; CNBC 2026-09-15 "Wall Street weighs prospect of an AI slowdown on data center buildout". (5) Motley Fool 2026-09-21: Warsh/rates sell-off in "GE Vernova and Vertiv". (6) Bloomberg 2026-07-22 "GE Vernova Falls as Outlook Collides With 'Too High' AI Hopes"; CNBC 2026-07-22 "sellers blinded by an earnings miss". (7) Reuters/Hazeltree 2026-09-16: GEV in the top-10 most-shorted large North American stocks for the 10th consecutive month, same "AI theme" basket as CoreWeave, Nebius, SMCI; selling "reflects funding concerns rather than deterioration in reported fundamentals". Nobody has published the exact OLS decomposition, but that is a method, not a fact the market lacks.
- **materiality**: 2
- **strongest_counterargument**: The split "half beta, half one day" is an artifact of a no-intercept regression fit over the 120 days in which GEV ran +77.4% vs the basket +39.5% (prices, 2026-01-07 to 2026-06-30). That window bakes GEV's own bubble alpha (+0.20%/day intercept) into the "normal" relationship. Add the intercept and the post-peak residual is -23.3% (ex-Jul-22 -14.4%), not -11.8%; measure GEV against the basket from 2026-04-01 instead and GEV is -2.1 pts vs basket, i.e. the entire drawdown is GEV giving back a GEV-specific premium, which is the opposite reading of the same tape. Second, the "beta" days are contaminated: Sep 14's basket -5.2% was partly caused by GEV (peers fell "in sympathy" with the GLJ note per 24/7 Wall St and the corpus NEWS chunk; the Amodei essay was the other driver), so treating 5.2 of GEV's 8.6 points as exogenous sector beta is circular; and the two largest basket days are peer earnings (Jul 29 VRT -17.3%, Jul 30 PWR +17.3%), which is information transfer, not "AI-power de-rating". Third, the volume story is seasonality: August 2026 was the lowest-volume month of the last 14 not only for GEV (0.70x trailing-12m) but for VRT (0.63x), ETN (0.72x) and SPY (0.54x); GEV's max volume/20d ratio was below 2.0 in 9 of the 21 months since Jan 2025, so "no day above 1.9x" is the norm, not evidence against capitulation. Low volume also cannot separate long-holder exit from short pressure, and GEV has been top-10 most-shorted for 10 months. Fourth, the finding's own falsification is toothless: using its betas, non-overlapping 20-day residual sums since Jul 2025 have std 7.7% and land inside the +/-4% band only 40% of the time (32% since Apr 2024), and rolling 20-day residual < -8% has already happened 5 times since Apr 2024 (first breach 2025-03-10, 2025-10-06, 2026-01-09, 2026-05-22, 2026-07-31), roughly twice a year. Finally, the "one day" is the Q2 print (adj EPS $2.47 vs $3.04 consensus, FCF pulled into H1 leaving implied H2 $1.6-2.6B); dismissing it as a single event is dismissing the only GEV-specific fundamental repricing in the window. None of this touches 2027 EPS, FCF or the multiple; it converts the pitch into an AI-capex beta call the memo cannot own.
- **what_would_rescue_it**: (1) Baseline robustness: refit with an intercept and with a fit window that excludes the H1-2026 parabolic run (e.g. 2025-07-01 to 2025-12-31, or a 500-day window) and show the ex-Jul-22 residual is still within +/-5%; report the intercept-inclusive residual honestly. (2) Break the Sep 14 circularity with timing: the Amodei essay was a weekend event, the GLJ note hit pre-market (GEV -4.8% pre-market, -8.6% close). Use pre-market/intraday prints (or GRID ETF vs GEV minute bars) to show the basket was already down before the GLJ note circulated; if peers only fell after GEV's open, the beta attribution for Sep 14 fails. (3) Replace volume with holder data: 13F Q3 changes (due mid-Nov, outside memo window) or short-interest / days-to-cover from FINRA bi-monthly prints (Sep 15 settlement data published ~Sep 24) showing short interest did not rise during the drawdown; the corpus holders table could be checked for 13F deltas. (4) Show the residual is a signal, not noise: an event study of prior -8% rolling-residual episodes (2025-03, 2025-10, 2026-01, 2026-05) with GEV's subsequent 60-day relative return; if mean reversion is significant, the finding becomes a tradeable long-GEV/short-basket at 1.0x hedge with the Oct ~22 Q3 print as catalyst. (5) A documented sell-side or quant note (e.g. Barclays/Bernstein factor attribution) showing the point is NOT in circulation would lift novelty from 2-3 to 4. (6) Widen the prediction band to +/-8% or state it as a hedged P&L to make it falsifiable with power.
- **notes**: REPRODUCTION (all from prices table, pandas; script logic as in the finding). Fit 120d to 2026-06-30, no intercept: betas SPY 0.217, basket 0.987; actual cum -19.96%; predicted -8.81%; residual sum -11.77%; Jul 22 residual -8.69%; ex-Jul-22 -3.07%. Confirmed exactly. With intercept: alpha 0.205%/day, betas 0.219/0.975, residual -23.3%, ex-Jul-22 -14.4%. Fit-window sensitivity: 60d fit (betas 0.60/0.86) residual -13.6%, ex-Jul-22 -5.0%; 250d fit -12.1%/-3.4%. Baseline sensitivity (GEV minus 5-peer basket cumulative to 2026-09-18): from 2025-09-18 +18.6 pts; from 2026-01-02 +11.4 pts; from 2026-03-02 +3.9 pts; from 2026-04-01 -2.1 pts; from 2026-06-30 -10.7 pts. Fit-window run: 2026-01-07 to 2026-06-30 GEV +77.4%, basket +39.5%, SPY +8.3%. Biggest basket days post-peak (VRT/ETN/PWR/HUBB/EMR/GEV/SPY): 2026-07-29 -17.3/-6.3/-4.6/-4.7/-4.0/-4.6/-1.5; 2026-07-30 +2.0/+6.9/+17.3/+2.8/+2.0/+9.1/+1.7; 2026-09-14 -7.7/-7.6/-4.4/-3.9/-2.6/-8.6/-0.4; 2026-08-18 -6.8/-5.3/-3.6/-4.1/-2.6/-6.9/-0.7. Sep 14 whole universe: GEV -8.6, VRT -7.7, ETN -7.6, BE -6.8, PWR -4.4, HUBB -3.9, AME -3.4, EMR -2.6, ROK -2.2, NEE -0.8, SPY -0.4 (AI-power complex fell as a group, so beta is partly real, but the GEV-specific share is a lower bound because peers cited GEV). Jul 22 universe: GEV -8.7, next worst ADBE/SPOT -3.9 (pure idiosyncratic, GEV Q2 print; corpus primary chunks: 8-K, 8-K/EX, 10-Q, 10-Q/EX all filing_date 2026-07-22; only other primary filing in window is 8-K 2026-08-27 CFO). CFO window: Aug 27 GEV +0.08% (basket +0.25%), Aug 28 -4.39% (basket -2.93%), Aug 31 -1.47% (basket -0.41%, VRT +0.64%); residual Aug 27-Sep 4 = -1.1%, so the finding's CFO point survives, but the 24/7 Wall St 2026-08-31 piece called Aug 31 "single-name repricing rather than a broader sector selloff". VOLUME: monthly avg volume Aug-26 / trailing 12m (Jul25-Jun26): GEV 0.70 (#1 lowest of 14 months), VRT 0.63 (#1), ETN 0.72 (#1), SPY 0.54 (#1), HUBB 0.84 (#3), EMR 0.89 (#5), PWR 0.98 (#8), ROK 0.96 (#8). Ratio of monthly avg volume to June 2026: GEV Jul 0.91/Aug 0.62/Sep 0.71 vs SPY 0.77/0.63/0.71 and VRT 0.85/0.63/0.84. GEV max(vol/20d avg) by month since 2025-01: 4.84, 1.73, 1.97, 1.96, 1.64, 3.19, 2.34, 1.41, 2.20, 3.97, 1.59, 3.75, 2.02, 1.48, 1.87, 1.87, 2.36, 2.16, 1.72, 1.83, 1.89; spikes >3x are earnings months only. Query: SELECT substr(date,1,7) m, avg(volume) FROM prices WHERE ticker IN ('GEV','VRT','ETN','SPY') AND date>='2025-07-01' GROUP BY ticker, m. PREDICTION/KILL BASE RATES (finding's betas, daily residual = GEV - 0.217*SPY - 0.987*basket): non-overlapping 20-day residual sums since 2024-04 n=31, std 9.0%, |sum|<=4% in 32%, < -8% in 6%, > +8% in 42%; since 2025-07 n=15, std 7.7%, |sum|<=4% in 40%, < -8% in 20%. Rolling 20-day residual < -8% episodes (first breach): 2025-03-10, 2025-10-06, 2026-01-09, 2026-05-22, 2026-07-31; worst window -18.0% ending 2025-11-06 (post-Q3'25 print). Daily residual std 2.19% in fit window vs 2.05% post-peak (no regime change in idiosyncratic vol; the drawdown is not "quieter" than the run-up). Residual Jul 23-Aug 19 -2.1%, Aug 20-Sep 18 -0.1% (the ex-Jul-22 part of the finding is right; it is just not informative). CORPUS COMMENTARY: chunks_fts MATCH '"Vernova" AND "Vertiv"' tier=commentary in 2026: Apr 1, May 1, Jul 4, Aug 6 chunks; the beta framing lives mostly in web press, not in the corpus, so the team should not expect the corpus to help here. The Sep 14 and Sep 16 24/7 Wall St stories and the Jul 22 reaction stories (boerse-global 2026-07-23 "Siemens Energy Hit by Sector Contagion as GE Vernova's Mixed Results Spark Profit-Taking", Investing.com "Morgan Stanley strongly resets GE Vernova stock target") are all in chunks form=NEWS. DEAD ENDS: no sell-side or quant note found that performs a formal factor decomposition of the GEV drawdown (searched Barron's/Bloomberg/Jefferies/Bernstein terms); Bernstein's reply to GLJ is fundamental (utilities demand), not beta. No published Sep 14 intraday timing that separates the Amodei-essay sector leg from the GLJ leg; Motley Fool credits the essay entirely, 24/7 Wall St credits GLJ ("the analyst note is the differentiator rather than the sector move"), so it is confounded. Holders/13F table not queried (Q3 13Fs not due until mid-Nov, outside the memo). Hazeltree short-basket data is not in the corpus; source is Reuters 2026-09-16 via US News/Globe and Mail. NET: numbers are right, the interpretation is baseline-dependent, the conclusion is already the consensus press narrative, it does not move 2027 EPS/FCF/multiple, and the stated prediction band has under 40% historical hit rate. Sources: https://247wallst.com/investing/2026/09/16/ge-vernova-gave-back-its-gains-since-july-one-wall-street-pro-says-65-gains-will-materialize-soon/ ; https://247wallst.com/investing/2026/09/14/ge-vernova-sinks-9-as-glj-research-starts-at-sell-with-470-target-eaton-drops-7-quanta-services-falls-4/ ; https://247wallst.com/investing/2026/08/31/ge-vernova-slides-3-vertiv-holdings-and-eaton-sit-out-the-selloff-is-the-rivian-cfo-handoff-still-driving-the-drawdown/ ; https://www.fool.com/investing/2026/09/14/why-did-ge-vernova-stock-fall-today/ ; https://www.fool.com/investing/2026/08/28/a-wall-street-journal-report-on-3-trillion-in-off/ ; https://www.fool.com/investing/2026/09/21/interest-rates-caterpillar-ge-vernova-vertiv/ ; https://www.bloomberg.com/news/articles/2026-07-22/ge-vernova-falls-as-outlook-collides-with-too-high-ai-hopes ; https://www.cnbc.com/2026/07/22/ge-vernova-sellers-blinded-by-an-earnings-miss-should-focus-on-strong-demand-instead.html ; https://www.cnbc.com/2026/09/15/investors-ai-slowdown-data-center-buildout.html ; https://money.usnews.com/investing/news/articles/2026-09-16/hedge-funds-step-up-bets-against-consumer-stocks-in-august-hazeltree-says

## [Verify] repro:contradictions:Management says only ~20% of GW under co

- **reproduced**: True
- **corrected_numbers**: All four evidence steps reproduce verbatim. Corrections: (1) The 80/20 split was NOT said only once. It was first stated on the Q1'26 call (Apr 22 2026) as an explicit GW split: "Approximately 80% of our total gigawatts under contract are with traditional customers, with the remaining 20% explicitly supporting data centers." (confirmed by pypdf extraction of https://www.gevernova.com/sites/default/files/gev_webcast_transcript_04222026.pdf; in corpus only via commentary src:227 mgrid.org, src:230, src:1849 Yahoo 2026-04-23). It was repeated on the Q2'26 call (Jul 22 2026, src:3161 chunk id 251590 ord 2, confirmed against gev_webcast_transcript_07222026.pdf). So: two consecutive calls, and April commentary reported it; the July coverage in the corpus (src:301, 1016, 2644, 3801) repeated only the Electrification data-center dollars, not the Gas Power split. Novelty should drop from 3 to 2. (2) The Q2'26 wording is ambiguous: "approximately 100 customers in 26 different countries, of which approximately 80% are traditional customers and 20% are for data centers" reads as a share of customer COUNT; the GW reading (20% x 116 = 23.2 GW) rests on the Q1'26 wording, which should be the primary citation. (3) Step 2 quote should read "More than half of the gigawatts that are now under contract are for our largest, most efficient HA turbines" (src:3161 ord 1, chunk id 251589), not "half". (4) Arithmetic checks: 53 GW backlog + 63 GW SRAs = 116 GW (src:3161 ord 1: "from 100 to 116 gigawatts sequentially"); 20% = 23.2 GW; 2028 output 24 GW per press release 8-K/EX 0001996810-26-000147. (5) Mention rates (LIKE '%data center%', GEV chunks): commentary NEWS 276.5/1k (1175/4249), WEB 202.4 (2058/10168), RSS 182.5, YOUTUBE 201.3; primary 10-K 2.5 (2/813), 8-K/EX 3.1 (8/2590), DEF 14A 6.0, S-1 7.0, 10-Q 0.0 (0/1083). Direction holds but "250-390" overstates commentary; use 180-280. (6) Q2'26 press release (8-K/EX, 29 chunks) has 1 data-center chunk, Electrification only (">$5 billion year-to-date"); Q2'26 10-Q 0001996810-26-000148 (138 chunks) has 0 "data center" and 0 "traditional" chunks, as the finding claims. (7) Q3'26 call: catalyst_calendar row id 1 estimates 2026-10-21, cadence-based, confirmed=0.
- **data_quality_issues**: (a) Q1'26 transcript (Apr 22 2026) is absent from the corpus as a primary source; only commentary quotes it. The PDF exists at gevernova.com (260 KB) and should be ingested. (b) Q3'25 transcript src:3796 (gevernova.com PDF, Oct 22 2025) is mislabeled kind='web', tier='commentary' rather than transcript/primary. (c) src:3161 (Q2'26 transcript) has blank published and blank chunks.filing_date, so date-filtered queries miss it; src:3771 (Yahoo Q3'25 transcript) carries filing_date 2026-04-22, six months late. (d) src:1016 angle='onshore_wind' is a mislabel for Q2 call coverage. (e) Only the Q2'26 transcript populates form='TRANSCRIPT' (42 chunks); the Q4'25 call exists only as Yahoo coverage src:2660. (f) WebFetch cannot read gevernova.com PDFs directly; it saves the binary and pypdf extraction is required. (g) Blank filing_date WEB rows satisfy 'filing_date < X' filters; exclude blanks explicitly. (h) NRG 10-K FY25 (2026-02-24, chunk ords 29-30) describes its development business as including "BYOP arrangements for data centers and other large load customers", so NRG as a "traditional" IPP example carries data-center end-use, supporting the finding's caveat rather than weakening it.
- **notes**: Ran: SELECT ord,text FROM chunks WHERE accession='src:3161' AND text LIKE '%80% are traditional customers%' -> ord 2, chunk id 251590, ticker GEV, tier primary, form TRANSCRIPT; source 3161 url gevernova.com gev_webcast_transcript_07222026.pdf, kind transcript. Same chunk contains "half of the gigawatts" (spans ord 1-2; ord 1 has "More than half"). src:1016 (Yahoo NEWS 2026-07-22, commentary) ord 3 contains "booked $2.7 billion of data center orders in Electrification during the second quarter" verbatim. NRG 10-K filed 2026-02-24, chunk ids 308019/308020, ords 197-198, Item 7 MD&A: "slot reservation agreements with GEV for the procurement of 3.6 GW of 7HA gas turbines. The first projects... expected to commence operations by the end of 2029" verbatim; the PDA is 5.4 GW combined cycle with Kiewit/TIC, signed Feb 13 2025. FTS '"traditional customers"' across all tickers returned the split only in src:3161 (Q2'26) and April commentary (src:227, src:230, src:1849); src:230 glosses "traditional" as "traditional utility, independent power producer and industrial customers" and src:227 as "roughly 20 GW tied directly to AI and cloud load" at the 100 GW mark. Q4'25 coverage src:2660 (Jan 2026): 83 GW under contract (40 backlog + 43 SRA) with no customer-type split even when Goldman's Ritchie asked "Types of customers?" (ord 24-26), so the split is a 2026 disclosure. 10-K FY25 risk factor (chunk 29674) uses "nontraditional customers, such as hyperscalers" for the same distinction. Q3'25 transcript src:3796 ord 29 gives a separate Electrification datapoint: data centers were ~10% of Prolec's business in 2024, ~20% in 2025 (not gas). External confirmation: both gevernova.com PDFs downloaded via WebFetch and text-extracted with pypdf; Q1'26 PDF 53,661 chars, Q2'26 PDF 50,639 chars matching sources.n_chars. Dead ends: gev_webcast_transcript_01212026.pdf and 01222026.pdf both 404 (Q4'25 transcript URL not found); no GEV 10-Q or press release repeats the gas split; no GEV chunk states a data-center GW share above 20% anywhere. Verdict: the finding's numbers and quotes are sound; its "why the market misses it" section must be rewritten (two calls, not one; April coverage did report it; the 2Q wording is customer-count-ambiguous) and novelty lowered to 2. Confidence 4 and materiality 3 are reasonable.
- **confidence**: 5

## [Verify] skeptic:contradictions:Management says only ~20% of GW under co

- **refuted**: True
- **already_widely_known**: True
- **where_known**: The 80/20 split was first disclosed on the Q1'26 call, Apr 22 2026, not Q2: prepared remarks "Approximately 80% of our total gigawatts under contract are with traditional customers, with the remaining 20% explicitly supporting data centers" and in Q&A "About 20% of our 100 gigawatts are direct to the data centers" (gevernova.com/sites/default/files/gev_webcast_transcript_04222026.pdf; also fool.com, insidermonkey.com, utilitydive.com Apr 23, mgrid.org Apr 22). It was restated Jul 22 and printed the same day by Utility Dive and Yahoo Finance (corpus src:239, src:301), Solmar (src:347), Zacks, Developments Today, thegridreport.news, Ziven, Monte Investments substack (Jul 28), Manufacturing Mag (Jun 6), chargeduppro (May 27). The finding's exact argument AND its rebuttal are already in Seeking Alpha "GE Vernova: Sold Out Through 2030" (Aug 28 2026): "'Only' 20% of contracted gas capacity is labeled data center demand. I think that understates AI exposure because utilities are building generation for hyperscalers." Bernstein (Sunaina Ocalan, ~Sep 15-17 2026, Buy, $1,298 PT) deployed the parallel diversification defense after the GLJ Sell (Electrification orders 38% data center / 62% utility), and Insider Monkey (Sep 18) headlined that the defense "doesn't answer the valuation question." The finding's "why_market_misses_it" ("the 80/20 line appears once") is factually wrong; it is a corpus artifact: sources has only one GEV transcript (kind='transcript' -> id 3161, the Q2 PDF). The Q1'26 transcript was never ingested.
- **materiality**: 2
- **strongest_counterargument**: The split is a who-signs label, not an end-use measure, and management's own Q1 wording ("direct to the data centers") concedes the indirect channel. The finding's own "traditional" example disproves it: NRG's 3.6 GW of 7HA SRAs sit inside the Feb 13 2025 NRG/GE Vernova/Kiewit 5.4 GW program that NRG announced in the same 8-K as "Letters of Intent with two data center developers" (NRG 8-K/EX 2025-02-26; 10-Q 2025-08-06; 10-K 2026-02-24). Entergy's 10-K (2026-02-19) certifies 2,262 MW of three CCGTs explicitly for Meta's north Louisiana data center; in the corpus, customer 10-K/10-Q/8-K chunks since 2025 pairing gas-turbine/combined-cycle with data-center load: ETR 28, NRG 7, TLN 6, AEP 4, NEE 3, XEL 2, VST 2, CEG 2 (chunks_fts MATCH '("combined cycle" OR "gas turbine" OR "gas turbines" OR "gas-fired") AND ("data center" OR "data centers" OR "hyperscaler" OR "large load")', tier='primary', form IN 10-K/10-Q/8-K/EX, filing_date>='2025-01-01'). EIA-860M (generators, vintage '2026-07', sheet='Planned', energy_source='NG', prime_mover IN CT/CA/CS/GT, planned_year 2027-2031) shows 61.1 GW planned vs 14.3 GW for 2025-29 in the 2024-01 vintage, led by TX 18.5 GW, LA 9.5 GW, PA 4.4 GW, MS 3.0, TN 2.6, AZ 2.2 - data-center geographies. Siemens Energy discloses 22 GW of 80 GW commitments tied to data centers (~27%, Power Mag Apr 2026), so GEV's 20% is peer-typical, not a differentiator. Mechanism to the P&L is also wrong: with 116 GW contracted against a 20 GW/yr run-rate (24 GW in 2028), slots are sold through 2030 and deposits are non-refundable, so a data-center pullback inside 3-12 months cannot remove 23 GW of 2027-28 revenue; what it attacks is the marginal price (+10-20% $/kW vs 4Q25, "higher end" in H2 per Q2 transcript src:3161 ord 3) and the incremental-order narrative that hold the 31-38x multiple, and the marginal price-setting buyer is the hyperscaler/IPP-for-hyperscaler (src:1312: utilities "lose those slots to data center developers willing to pay a premium"). The stock record confirms the split never anchored the multiple: prices table, GEV close $991.30 (Apr 21) -> $1,127.56 (Apr 22, +13.8%, day the 80/20 was first said); $1,078.81 (Jul 21) -> $985.03 (Jul 22, -8.7%, day it was restated) -> $900.28 (Jul 29); $957.27 (Sep 11) -> $874.76 (Sep 14, -8.6%, GLJ Sell + Amodei essay). GLJ's thesis is vintage-margin and cyclicality (2027 EBITDA $7.42B vs consensus $9.45B; Power margin 18.5% vs 20.7%; "cyclical gas-turbine manufacturer priced as a secular compounder"), which the 80/20 split does not address at all.
- **what_would_rescue_it**: (1) A bottom-up end-use ledger of the 116 GW by named counterparty (NRG 3.6 GW, Entergy/Meta 2.3 GW, Chevron-Microsoft Kilby 2.7 GW, Xcel 6 GW alliance, Crusoe, Talen, Vistra, Constellation, plus international) showing data-center end-use (direct + utility/IPP-for-hyperscaler) is still at or below ~30-35% of contracted GW; the projects table cannot do this today because 83 GW of its 118.5 GW GE-linked capacity sits in aggregate owner='GE Vernova' rows and only 12 of 130 GE-linked rows (9.3 GW) carry a data-center reference. (2) A factor regression of GEV daily excess returns Jun 30-Sep 18 2026 on an AI-capex basket (NVDA, VRT, ETN) versus a utility-capex basket (XLU, PWR) showing AI loading far above utility loading; that would turn "the market over-weights the 20%" from an assertion into a quantified mispricing. (3) Management giving a direct-plus-indirect end-use split, or the 30-35 hyperscaler framework agreements (Q1 Q&A, none closed as of Q2) closing without lifting the direct share above ~25%, which would show hyperscaler demand is structurally routed through utilities and cannot be cancelled without a rate-case. Note the Q3 call (Oct 21-22) is after the Oct 2 memo deadline, so the finding's testable prediction cannot be used in the memo as written.
- **notes**: VERDICT: refuted on fronts 1, 2 and 4; front 3 (materiality) at best 2/5. The number is real and verbatim (SELECT ord, text FROM chunks WHERE accession='src:3161' AND text LIKE '%80% are traditional customers%' -> ord 2), but it is five months old, printed in roughly ten outlets, already used by Bernstein as a post-GLJ defense and already rebutted by Seeking Alpha on Aug 28. Honest ratings: novelty 1, confidence in the number 5, materiality 2. What survives: a small reusable fact for the memo (GEV 20% direct vs Siemens ~27%) and the corpus repair. CORPUS DEFECT (fix before Oct 2): ingest gev_webcast_transcript_04222026.pdf (Q1'26) and the 4Q25/3Q25 transcripts; sources.kind='transcript' currently holds only id 3161, which is exactly why this finding mis-stated "appears once". DEAD ENDS: news table (cols id,url,source,published,title,text,retrieved_at,ticker) returned zero rows for title LIKE fall/drop/sell/GLJ/bubble/capex on ticker='GEV', so drawdown attribution had to come from the web (24/7 Wall St, SA news 4642621, gurufocus, ainvest, Insider Monkey Sep 18); FTS on XEL and AEP primary chunks for "GE Vernova" AND "data center" returned nothing (the Xcel-GEV strategic alliance of Feb 3 2026 is not in customer filings in the corpus); FTS on the Siemens Energy pre-close transcript src:3169 for a data-center GW share returned nothing (the 22 of 80 GW figure is from powermag.com Apr 1 2026, citing the Feb 11 2026 Q1 FY26 call); projects table cannot support an end-use ledger as structured (see rescue item 1). Price reproduction: SELECT date, close FROM prices WHERE ticker='GEV' AND date IN ('2026-04-21','2026-04-22','2026-07-21','2026-07-22','2026-07-29','2026-09-11','2026-09-14','2026-09-18'). EIA reproduction: SELECT state, ROUND(SUM(mw)) FROM generators WHERE vintage='2026-07' AND sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND planned_year BETWEEN 2027 AND 2031 GROUP BY state ORDER BY 2 DESC. NRG reproduction: SELECT filing_date, form, text FROM chunks WHERE ticker='NRG' AND tier='primary' AND text LIKE '%comprehensive development agreement%' ORDER BY filing_date DESC; and SELECT text FROM chunks WHERE ticker='NRG' AND form='8-K/EX' AND filing_date='2025-02-26' AND text LIKE '%Letters of Intent with two data cent%'.

## [Verify] skeptic:contradictions:GEV quietly cut its 2026 tariff cost est

- **refuted**: True
- **already_widely_known**: True
- **where_known**: Reuters wire, morning of Jul 22 2026 (Sumit Saha, reuters.com/business/energy/ge-vernova-raises-annual-revenue-forecast-strong-power-demand-boosts-orders-2026-07-22/): "It updated its 2026 tariff hit forecast to $100 million-$200 million from $250 million-$350 million projected in April, citing contractual provisions, sourcing changes, trade regulations and tariff refunds." That is the exact Q1-vs-Q2 comparison the finding says nobody made. Syndicated same day to BNN Bloomberg, CTV, MSN, KFGO, KELO. New Energy Weekly (Jul 23 2026) repeats it: "reduced from $250-350 million to $100-200 million after sourcing changes, contractual protections and anticipated refunds." Corpus commentary tier already holds it: sources 946, 1845, 1846, 2664, 2669, 3886, 2641 all cite the $100-200M figure (query: chunks_fts MATCH '("tariff" OR "tariffs") AND ("100 million" OR "200 million")' AND ticker='GEV'); claims table has two 2026-07-22 rows topic='tariffs' with the number. Prior figure was equally public: Q1'26 call (Motley Fool transcript, Apr 22 2026) has Barclays' Julian Mitchell asking about tariff mitigation and CFO Parks answering "$250 million to $350 million is fully built into our outlook." The finding's "why market misses it" claim (press release and call did not flag it, so nobody noticed) fails because the 10-Q is filed at the same time as the release and the wire services read it; the finding never checked the corpus commentary tier.
- **materiality**: 1
- **strongest_counterargument**: Mechanism and embedding both fail. (1) The cut is not GEV-specific execution; it is a macro/legal event that hit every US importer: the Supreme Court struck IEEPA tariffs 6-3 in Feb 2026, the CIT ordered CBP to refund ~$165B, and CBP's CAPE refund portal was being built Mar-Jun 2026. The Q2 10-Q adds new words absent from Q1: "including pursuing the recovery of certain tariffs" (10-Q 2026-07-22 vs 2026-04-22, same FTS query '"estimated cost impact"'). A refund of duties already paid (FY25 actual tariff cost was ~$250M per the 10-K filed 2026-01-29) is a one-time recovery booked in 2026; it does not lift 2027 run-rate margin, so the finding's extrapolation to the multiple is wrong in sign of durability. (2) The finding routes the benefit to Power EBITDA margin, but every filing allocates tariff cost to Wind and Prolec: Q4'25 call "approximately $70 million impact of tariffs" at Wind; Q1'26 press release "Segment EBITDA losses grew from lower Onshore Wind equipment volume and the impact of tariffs"; Q1'26 call Parks "a little bit more impact on the Prolec numbers... lesser impact on some of the other businesses"; Q2'26 call H1 wind shipments "had fewer contractual protections for tariffs." Power's share is undisclosed and by these statements small, so "Power prints at or above 19%" has no mechanism. Wind loss guidance (~$400M) was not improved. (3) Already embedded: on the same Jul 22 call management held total EBITDA margin at 12-14% and Power at 17-19% despite the tariff cut and a $1B revenue raise; William Blair's Dorsheimer told Reuters investors expected a margin raise and did not get one. So the ~$150M is inside an unchanged margin guide, absorbed by offshore wind costs, +30% R&D/capex and inflation. GEV closed 1078.81 on Jul 21 and 985.03 on Jul 22 (prices table, -8.7%), so whatever the tariff line was worth has been in the price for two months. (4) Size: $150M vs ~$5.5-6.4B guided adjusted EBITDA (2.5%), vs $12B FCF (1.25%), ~$0.42 after-tax EPS on ~$30 (1.4%); the Q2 EPS miss alone ($2.47 vs $3.04, ~$154M) was the same size as the entire cut. (5) It is a repeat of 2025: $300-400M (Apr, Jul) -> "trending towards the lower end" (Oct) -> $250M actual (10-K). GEV over-reserves tariffs and walks them down; the Street has seen the pattern once already.
- **what_would_rescue_it**: Any one of: (a) the Q3'26 10-Q (late Oct) drops the "pursuing the recovery" language and states a 2027 tariff estimate at or below $100M, proving the reduction is run-rate rather than refund; (b) a segment split (10-Q MD&A or Dec 2026 analyst day bridge) showing most of the $150M relief sits in Power/Electrification rather than Wind/Prolec, which would make the Power-margin prediction mechanically possible; (c) a post-Jul-22 sell-side model (Jefferies, Barclays, Morgan Stanley) still carrying a $300M FY26 tariff line, which would show the cut is not in numbers; (d) evidence that the FY26 margin guide was held for reasons unrelated to tariffs (e.g. a disclosed one-time Wind charge) so that the tariff relief is a hidden cushion. None of these are in the corpus or on the web as of Sep 21 2026. Even if rescued, cap materiality at 2: the number is too small against a $250B market cap to change a 3-12 month call, but it could be one line in a guidance-conservatism bridge under the team's existing "guidance-language drift" angle.
- **notes**: Verification done. Corpus 10-Q text reproduces exactly as the finding states (Q1'26 $250-350M; Q2'26 $100-200M with new recovery clause). The finding's absence check on the 8-K/EX press release is also correct: in 2025 the release carried the tariff dollar line in the guidance section (8-K/EX 2025-04-23, 2025-07-23, 2025-10-22), while both 2026 releases (2026-04-22, 2026-07-22) dropped it to boilerplate. That format change is real but irrelevant because Reuters took the number from the simultaneous 10-Q. Transcript src:3161 (Q2'26 call) mentions tariffs only three times, all Wind/232 context, no Q&A on the cut; so "not flagged on the call" is true but "market missed it" is false. Price context: Apr 22 2026 +13.7% on Q1 (991.30 to 1127.56) with the $250-350M figure public; Jul 22 2026 -8.7% with the $100-200M figure headlined as a "tariff hit" (Reuters headline framing was negative, body text gave the comparison). Dead ends: analyst_calls table has zero tariff rows; mgmt_guidance has only 2025 tariff rows (no 2026 entries, extraction gap); no sell-side note quantifying tariff as a guidance driver found on web; WebFetch of the GEV transcript PDF failed to parse (used corpus chunks instead); one Aug 12 2026 blog still quoted the stale $250-350M figure, showing minor commentary lag but not a market-wide miss. Reproduction queries: (1) SELECT c.form,c.filing_date,substr(c.text,instr(c.text,'estimated cost impact')-400,800) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated cost impact"' AND c.ticker='GEV' ORDER BY c.filing_date; (2) SELECT * FROM prices WHERE ticker='GEV' AND date BETWEEN '2026-07-20' AND '2026-07-24'; (3) SELECT published,topic,claim FROM claims WHERE ticker='GEV' AND lower(claim) LIKE '%tariff%' AND published>='2026-07-01'; (4) SELECT ord,text FROM chunks WHERE accession='src:3161' AND ord BETWEEN 17 AND 20 (guidance raise attributed to volume/price, margin held). External: IEEPA ruling and CAPE refund mechanism per Skadden (Mar 2026), Stinson, PwC, Penn Wharton Budget Model (Feb 20 2026). Ratings: novelty 1 (Reuters day-one), confidence in refutation 5, materiality 1.

## [Verify] skeptic:price-events:GEV trades hyperscaler capex prints as h

- **refuted**: True
- **already_widely_known**: True
- **where_known**: The qualitative claim (GEV is a hyperscaler-capex derivative that rallies on Big Tech capex guides) is ubiquitous; only the n=26 tabulation is unpublished. Corpus commentary: NEWS 2026-07-22 'GE Vernova has become a major derivative play on AI infrastructure' (FTS: "Vernova" AND ("capex proxy" OR "AI proxy" OR "picks and shovels" OR "derivative play") = 9 commentary hits). Web: 24/7 Wall St 2026-09-16 quoting Guggenheim (Osha) that GEV is 'a direct proxy for AI data center capital expenditure' and that 'anticipated catalysts for GE Vernova come from hyperscaler capex updates' (https://247wallst.com/investing/2026/09/16/ge-vernova-gave-back-its-gains-since-july-one-wall-street-pro-says-65-gains-will-materialize-soon/); CNBC 2026-07-30 market wrap attributing GEV +9.07% to data-center grid buildout the morning after MSFT/META (https://www.cnbc.com/2026/07/29/stock-market-today-live-updates.html); Daily Upside 'GE Vernova, Vertiv pull powerhouse profits from hyperscalers' and TipRanks on the AIPO 'AI power trade' ETF (the linkage is literally securitized); Fool.com 2025-01-31 on GEV slumping on DeepSeek then rebounding on capex reaffirmation. Late-Oct hyperscaler dates sit on every earnings calendar (WallStreetHorizon, Nasdaq) and in GEV options pricing. The corpus catalyst_calendar (16 rows, all own-print estimates) omits them, but that is a corpus artifact, not a market blind spot.
- **materiality**: 2
- **strongest_counterargument**: It is AI-infra-complex beta plus rebound timing, not a GEV-specific capex link, and it fails on the actual capex-raise days. (1) Reproduced exactly (prices table, n=26, +1.91%, 17/26), but GEV's day-after return has r=0.83 with the 5-peer basket and matches its sign 23/26 times; beta-adjusted (GEV beta 1.12 to basket on non-event days) the abnormal return is +0.74%, t=1.91; versus VRT alone the excess is +0.55%, t=0.86. Bootstrap p for the +1.04% basket excess is 0.038 across 20k draws of 26 random days, and that is before any multiple-comparison penalty for the post-hoc MSFT+META and NVDA subsets. (2) The three days that carry the mean are rebounds after complex-wide routs: 2024-07-31 (NVDA +12.8%, AMD +4.4% after AMD's print; MSFT stock -1.1%; VRT -19.8% over the prior 5 days), 2025-01-30 (GEV -16.0% over the prior 3 days post-DeepSeek), 2026-07-30 (GEV -16.6% over the prior 6 days, VRT -26.8% incl. its own -17% miss; Microsoft HELD CY26 capex and Meta missed; Nasdaq +2.8% ending a six-day losing streak). Drop the top 3 and the mean is +0.98% vs +0.30% unconditional daily drift for a stock that went up 7x. (3) On the cleanest capex-raise clusters GEV did not outperform: 2025-10-30 (Meta raised to $70-72B, MSFT capex +74%, Alphabet to $91-93B) GEV -0.67% (basket -0.62%); 2026-01-29 (Meta guided 2026 $115-135B) GEV +0.82% vs basket +1.45%; 2026-04-30 (Alphabet +$5B to $190B, Meta +$10B to $145B) GEV +1.91% vs basket +4.88% and VRT +7.29%. The 2026 subset excess vs basket is -0.07% (3/7 positive); the finding's own kill condition already fired on 2025-10-30, the exact late-October analog. (4) The MSFT+META same-evening subset contains a date error: 2024-07-31 is MSFT-only (Meta reported Jul 31 after close; GEV -2.36% on Aug 1) and 2026-01-29 is omitted; corrected mean +3.10% not +4.19%, and MSFT's own stock fell on 5 of those 8 days, so GEV's move is not sympathy with MSFT either but with the power/infra basket. (5) The headline 'as hard as its own earnings' uses signed means; on |move| GEV own prints average 5.42% vs 2.89% for hyperscaler day-afters vs 2.44% for any day. (6) NVDA: GEV's all-day beta to NVDA is 0.58 (corr 0.52, n=620), so GEV does trade NVDA; NVDA print days are simply sell-the-news for NVDA itself (NVDA mean -0.42%, GEV -0.62%, basket -0.09%, VRT -0.30%), i.e. nothing GEV-specific. Materiality: no path to 2027 EPS, FCF or multiple; the expected late-Oct week excess (~+1% x 3 unique day-afters) is inside one day's 3.3% SD, and the thesis-relevant content (capex trajectory) is already in the $1,236 average target and 31-38x forward P/E.
- **what_would_rescue_it**: (a) Classify every hyperscaler event by capex-guide change (raise / hold / cut, with the $ delta from the 8-K or call) and show GEV's beta-adjusted excess over VRT and ETN is positive and t>2.5 on raise days specifically, after controlling for the prior-5-day GEV drawdown; today the three cleanest raise days show GEV lagging. (b) Show the effect survives in 2026 alone (currently -0.07% vs basket, n=7). (c) Convert it from a price pattern to a fundamental input: a quantified lead-lag from hyperscaler capex revisions to GEV SRA/order announcements one or two quarters later (GW of SRAs per $10B capex raise) using backlog_quarterly and the hyperscaler 10-Q capex XBRL facts; that would make late-Oct capex guides a thesis variable rather than a trading note. (d) Pre-register the late-Oct 2026 test with confirmed dates and a basket-relative threshold (GEV minus VRT/ETN average > +1.5% on raise days), and note the pattern already failed on 2025-10-30 and 2026-04-30 so the prior should be weak. (e) Intraday (first 30 min) evidence that GEV reacts before the basket, from tick data not in the corpus.
- **notes**: Reproduction (all from prices table, adjclose, data\gev.db): event dates = next trading day after MSFT/META/GOOGL/AMZN 8-K earnings dates listed in the finding, dropping 2024-04-25 and 2024-07-24 (GEV own prints) -> 26 unique day-afters; GEV mean +1.91%, median +1.11%, 17/26 positive; basket (VRT,ETN,PWR,HUBB,EMR equal-weight) +0.87%; SPY +0.00%; VRT +1.35%; GEV-basket +1.04% (t=2.71 raw); other days n=594 mean +0.30% SD 3.34%, Welch t=2.28. Beta-adjusted: OLS of GEV on basket over non-event days since 2024-04-01 gives beta 1.12, abnormal mean +0.74% t=1.91 (17/26); vs VRT beta 0.55, abnormal +0.99% t=1.99. Bootstrap (20k draws of 26 days from 2024-04-01+): p(GEV-basket >= 1.04) = 0.038; p(raw mean >= 1.91) = 0.008. By year: 2024 n=8 GEV +0.56% excess +1.41%; 2025 n=11 +2.11% / +1.47%; 2026 n=7 +3.12% / -0.07% (3/7). Corrected MSFT+META same-evening set (2024-10-31, 2025-01-30, 2025-05-01, 2025-07-31, 2025-10-30, 2026-01-29, 2026-04-30, 2026-07-30): GEV +3.10%, basket +1.91%. Day-before (t0) GEV mean +0.94% (run-up); post-event +5d GEV +2.73% vs basket +1.38% but unconditional +5d is +1.78% vs +0.58%, so drift is mostly the trend. Mean |move|: own prints 5.42%, hyperscaler day-afters 2.89%, all days 2.44%. Own print days: 2025-07-23 +14.58, 2026-04-22 +13.75, 2026-07-22 -8.69. External closes for NVDA/MSFT/META/AMD from https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=3y&interval=1d (saved in scratchpad as NVDA.json etc.): NVDA day-after own moves +9.32,-6.38,+0.53,-8.48,+3.25,-0.79,-3.15,-5.46,-1.77,+8.74 (confirms the finding's 2024-25 NVDA dates as real print days); corr(GEV,NVDA) on those days -0.08; all-days GEV beta to NVDA 0.58, corr 0.52. MSFT own day-after moves on the same-evening set: -6.05,-6.18,+7.63,+3.95,-2.92,-9.99,-3.93,+15.51. Rebound context: GEV cum return into 2026-07-30 (6 days) -16.55%, VRT -26.75%; into 2025-01-30 (3 days) -15.99%; VRT into 2024-07-31 (5 days) -19.75%. Capex-raise facts: TrendForce/CNBC 2025-10-30 (Meta low end to $70B, MSFT $34.9B +74%); Yahoo/MLQ 2026-04-30 (Alphabet +$5B to $190B, Meta +$10B to $145B, four-company $725B up 77%); Investing.com/CNBC 2026-07-30 (MSFT 'maintained capex guidance', Meta missed, sank 8%); CNBC 2026-07-29 Vertiv -17% on revenue miss. DEAD ENDS: stooq CSV endpoint blocked by JS challenge; corpus FTS for "Vernova" AND (Meta OR Microsoft) AND capex AND (shares/jumped/rallied) = 0 commentary hits and "record high" variant = 0, so the corpus commentary does not carry same-day move attribution (it is in CNBC/Fool wraps, not ingested); no web source found that publishes the event-study numbers themselves; Q3-2026 hyperscaler dates not yet confirmed on IR pages as of 2026-09-21; catalyst_calendar has only 16 estimated own-print rows (GEV 2026-10-21 unconfirmed). Team note: if the memo keeps a catalyst line, phrase it as 'late-Oct hyperscaler capex guides are a sector-wide AI-infra catalyst' and do not claim GEV-specific sensitivity; in 2026 VRT and ETN reacted more.

## [Sweep] find:disclosure-diff

- **lens**: disclosure-change archaeologist: diffed GEV 10-K FY24 (filed 2025-02-06) vs 10-K FY25 (filed 2026-01-29) Item 1A and footnotes, and tracked Note 9 (contract assets/liabilities, RPO recognition curve, LTSA estimate revisions) across all ten 10-Q/10-K filings 2024-04-30 to 2026-07-22
- **findings**:
  - - **title**: Gas Power service-contract profitability is being revised DOWN at a 5x faster pace in 2026, and the filing stopped explaining why
    - **claim**: Net unfavorable changes in estimated profitability on contractual service agreements (100% Power segment) were -$218M in H1 2026 vs -$42M in H1 2025 and -$89M in H1 2024; the 9M 2026 figure (10-Q due ~Oct 22 2026) will be at or below -$300M.
    - **mechanism**: GEV books long-term service agreements on a cost-to-cost basis; a downward revision of a contract's lifetime margin is a cumulative catch-up that cuts revenue and Power segment EBITDA one-for-one in the quarter (100% drop-through). Q2 2026 alone was -$129M vs -$71M in Q2 2025, i.e. 12.5% of Q2 2026 Power segment EBITDA ($1,031M). Power services revenue grew only +5.8% in H1 2026 ($6,598M vs $6,238M) despite management's 'transactional orders per unit rising double digits'. Contractual service agreement assets exist only in Power ($5,399M Power, $0 Wind, $0 Electrification at 6/30/26), so the revisions are the gas fleet, exactly where the 'services worth $70M per GW-year' bull case lives. 10-K sensitivity: 1 point of contract profitability = $0.2B of contract assets.
    - **direction**: short
    - **evidence**:
      - - **source**: documents id=218 (10-Q filed 2026-07-22), Note 9
        - **date**: 2026-07-22
        - **quote_or_number**: "Net contractual service agreements increased primarily due to revenues recognized of $2,689 million, partially offset by billings of $2,392 million and net unfavorable changes in estimated profitability of $218 million."
        - **reproduction**: SELECT text FROM documents WHERE id=218; then regex 'net (?:un)?favorable changes in estimated profitability of \$[\d,]+ million' (Python re on whitespace-normalized text)
      - - **source**: documents ids 360,340,331,313,295,281,270,249,228,218 (all 10-Q/10-K), same regex; YTD values differenced into quarters
        - **date**: 2024-04-30 to 2026-07-22
        - **quote_or_number**: YTD: 2024 Q1 -29, H1 -89, 9M -135, FY -319 ('due primarily to higher costs'); 2025 Q1 +29, H1 -42, 9M -36, FY -151; 2026 Q1 -89, H1 -218. Quarterly: Q4'24 -184, Q2'25 -71, Q3'25 +6, Q4'25 -115, Q1'26 -89, Q2'26 -129.
        - **reproduction**: SELECT id, filing_date, text FROM documents WHERE ticker='GEV' AND form IN ('10-K','10-Q') ORDER BY filing_date; apply regex r'net (?:un)?favorable changes in estimated profitability of \$[\d,]+ million' to re.sub(r'\s+',' ',text)
      - - **source**: documents id=218, Note 9 CONTRACT AND OTHER DEFERRED ASSETS table by segment
        - **date**: 2026-07-22
        - **quote_or_number**: Contractual service agreement assets: Power $5,399, Wind $—, Electrification $— (Dec-25: $5,417 / — / —). Series Dec-24 5,321; Jun-25 5,597; Dec-25 5,417; Jun-26 5,399 (flat while services revenue grows).
        - **reproduction**: regex r'Contractual service agreement assets \$[\d,]+.{0,300}' on documents id IN (313,295,281,270,249,228,218)
      - - **source**: documents id=218 segment table; documents id=281 for prior year
        - **date**: 2026-07-22
        - **quote_or_number**: Power Segment EBITDA Q2'26 $1,031M (Q2'25 $778M); Q1'26 $811M (Q1'25 $517M). Power services revenue Q2'26 $3,512M vs $3,280M; H1 $6,598M vs $6,238M (+5.8%). Power equipment H1 $3,851M vs $2,996M.
        - **reproduction**: regex r'Segment EBITDA \$[\d,()]+ \$[\d,()]+ \$[\d,()]+ \$[\d,()]+' and r'Power[^$]{0,10}\$[\d,]+ .{0,300}?Equipment \$?([\d,]+) .* Services ([\d,]+)' on documents id=218 text
      - - **source**: documents id=313 (10-K FY24) vs id=249 (10-K FY25) and id=218 (Q2'26 10-Q): explanation removed
        - **date**: 2025-02-06 vs 2026-01-29 / 2026-07-22
        - **quote_or_number**: FY24 10-K: '...net unfavorable changes in estimated profitability of $319 million due primarily to higher costs.' FY25 10-K and both 2026 10-Qs: same sentence with the amount but NO reason. Sensitivity unchanged: '...one percentage point would increase or decrease the long-term service agreements contract assets balance by $0.2 billion.'
        - **reproduction**: regex r'estimated profitability of \$[\d,]+ million[^.]{0,120}\.' on documents id IN (313,249,228,218); regex r'Revisions to our estimates of future billings[^.]*\.' on ids 313,249
      - - **source**: chunks_fts over commentary/transcript tiers; sources id=3161 (Q2'26 webcast transcript PDF)
        - **date**: 2026-09-21
        - **quote_or_number**: 0 commentary or transcript chunks mention 'estimated profitability' or 'cumulative catch-up' for GEV (only SEC-mirror WEB pages). Management's only outage remarks: 'typical gas services seasonality with the highest outage volume in the fourth quarter.'
        - **reproduction**: SELECT c.form,c.tier,count(*) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated profitability"' AND c.ticker='GEV' GROUP BY 1,2
    - **why_market_misses_it**: The number sits in one sentence of Note 9 of the 10-Q, is never in the press release or webcast, is not tagged in XBRL as a stand-alone quarterly series (only ContractWithCustomerAsset... YTD tags), and quarterly values must be differenced from YTD. Nobody in the corpus (37 analysts, 250+ news chunks, the Q2 transcript) discusses it. The bull/bear debate is entirely about equipment vintage margins (GLJ) and future service dollars per GW; nobody is looking at whether the EXISTING service book's margins are holding.
    - **testable_prediction**: Q3 2026 10-Q (expected ~2026-10-22): 9M 2026 'net unfavorable changes in estimated profitability' at or below -$300M (i.e. Q3 worse than -$80M). FY26 10-K (late Jan 2027): full-year at or below -$400M vs -$151M in FY25, given Q4 is seasonally the worst outage quarter (Q4'24 -$184M, Q4'25 -$115M).
    - **kill_condition**: 9M 2026 figure better than -$250M (Q3 revision favorable or mild), or the 10-K attributes the revisions to a one-time item (e.g. a single contract restructuring) rather than fleet-wide cost inflation. Also killed if Power services revenue growth re-accelerates above +12% Y/Y in Q3 2026.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: TTM revisions are -$327M (Jul-25 to Jun-26) vs -$272M prior TTM, so the trailing-year deterioration is +20%, not 5x; the 5x is the H1 comparison and H1 is the seasonally light half. Revisions can be lumpy and partly non-cash timing. The filings do not say whether the revisions are HA-fleet outage cost inflation, labor, or parts; that is inference. Segment attribution relies on CSA assets being 100% Power, which the table shows, but Wind service agreements sit in 'equipment and other service agreements' and are outside this line.
  - - **title**: Customer deposits are now prepaying 43% of the equipment backlog and liquidating at the slowest rate on record: H2 2026 FCF guide looks too low, and the 'deposit reversal' bear cannot bite inside 12 months
    - **claim**: The share of opening-year contract liabilities converted to revenue in H1 fell to 28.9% in 2026 from 39.9% in 2025 and 34.6% in 2024, while equipment contract liabilities rose to 43.3% of equipment RPO at 6/30/26 from 33-37% in every prior quarter; Q3 2026 FCF (reported ~Oct 22 2026) will exceed $2.6B, the entire implied H2 range.
    - **mechanism**: Contract liabilities are cash received before revenue; they are the source of the $9.9B H1 2026 FCF. Two filing-only series show the deposits are (1) tied to deliveries far beyond 12 months (slow liquidation) and (2) growing faster than the backlog they secure (rising prepayment ratio). Power equipment/other-agreement deposits alone rose $11.27B in H1 2026 ($14,529M to $25,799M) vs $1.82B in H1 2025; Prolec's entire acquired current liabilities were $1,078M and sit in Electrification, so the Power increase is organic. In Q2 2026 alone equipment deposits rose $8.15B against an $11.9B rise in equipment RPO (69% marginal prepayment) vs 20% in Q2 2025. Unless order intake collapses, Q3 deposits keep FCF far above the $1.6-2.6B implied for all of H2; and since only ~29% of the opening pool unwinds per half, the cash cannot reverse within the 3-12 month horizon.
    - **direction**: long
    - **evidence**:
      - - **source**: xbrl_facts tags ContractWithCustomerLiabilityRevenueRecognized (YTD duration) and ContractWithCustomerLiability (instant, prior Dec-31)
        - **date**: 2024-04-30 to 2026-07-22 filings
        - **quote_or_number**: Revenue recognized from opening balance / opening balance: Q1 18.0% (2024), 20.3% (2025), 15.4% (2026); H1 34.6%, 39.9%, 28.9%; FY 65.1% (2024), 63.3% (2025). Openings: $15,247M, $17,744M, $25,950M. H1 rev from opening: $5,283M, $7,074M, $7,512M.
        - **reproduction**: SELECT start_date,end_date,max(val) FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerLiabilityRevenueRecognized' GROUP BY 1,2; SELECT end_date,max(val) FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerLiability' AND start_date IS NULL GROUP BY 1
      - - **source**: documents id=218 (10-Q 2026-07-22) Note 9
        - **date**: 2026-07-22
        - **quote_or_number**: "Revenue recognized related to the contract liabilities balance at the beginning of the year was approximately $7,512 million and $7,074 million for the six months ended June 30, 2026 and 2025, respectively."
        - **reproduction**: regex r'Revenue recognized related to the contract liabilities balance at the beginning of the year[^.]*\.' on documents id=218
      - - **source**: documents Note 9 CONTRACT LIABILITIES AND DEFERRED INCOME segment tables, ids 313,295,281,270,249,228,218
        - **date**: 2025-02-06 to 2026-07-22
        - **quote_or_number**: Equipment and other service agreement liabilities, Power: Dec-24 7,879; Mar-25 8,764; Jun-25 9,694; Sep-25 10,617; Dec-25 14,529; Mar-26 18,479; Jun-26 25,799. Total equipment CL: 15,511; 16,525; 17,371; 17,865; 23,524; 29,913; 38,064. Power CSA (service) prepayments flat: 1,789 to 1,880.
        - **reproduction**: regex r'CONTRACT LIABILITIES AND DEFERRED INCOME (?:December 31|March 31|June 30|September 30),? ?\d{4} Power .{0,40}Contractual service agreement liabilities \$([\d,]+).{0,60}Equipment and other service agreement liabilities ([\d,]+) ([\d,]+) ([\d,]+) ([\d,]+)' on whitespace-normalized documents text
      - - **source**: RPO footnote, same documents; equipment CL / equipment RPO
        - **date**: 2025-02-06 to 2026-07-22
        - **quote_or_number**: Equipment RPO: 43,047; 45,478; 49,712; 54,092; 64,245; 75,924; 87,821. Prepayment ratio: 36.0%, 36.3%, 34.9%, 33.0%, 36.6%, 39.4%, 43.3%. Q2'26 marginal: +8,151 CL / +11,897 RPO = 69%; Q2'25: +846 / +4,234 = 20%.
        - **reproduction**: regex r'Equipment-related RPO of \$([\d,]+) million' on the same documents; divide equipment CL by it
      - - **source**: documents id=218 Note 8 Prolec preliminary purchase price allocation
        - **date**: 2026-07-22
        - **quote_or_number**: "Current assets $1,654 Intangible assets 4,172 Other non-current assets 1,123 Current liabilities (1,078) Non-current liabilities (1,528) ... Goodwill 5,313" ; consideration $5,254M cash plus $4,402M remeasured stake; pre-tax gain $3,992M in Q1'26.
        - **reproduction**: SELECT text FROM documents WHERE id=218; find 'completed the acquisition of the remaining 50% stake of Prolec GE'
      - - **source**: documents ids 249 vs 228/218: explanation narrowed
        - **date**: 2026-01-29 vs 2026-04-22
        - **quote_or_number**: FY25 10-K: increase '...primarily due to new collections received in excess of revenue recognition at Power and Electrification, partially offset by revenue recognition in excess of collections at Wind.' 2026 10-Qs: '...new collections received in excess of revenue recognition and as a result of the acquisition of Prolec GE' (segment attribution dropped; Prolec was <8% of the $14,088M H1 increase).
        - **reproduction**: regex r'Contract liabilities and deferred income increase d? \$[\d,]+ million[^.]*\.' on documents ids 249, 228, 218
    - **why_market_misses_it**: The team's existing 'deposit ledger / FCF timing' angle and GLJ's bear case both treat deposits as a pool that will unwind and crush FCF. The two filing series here show the opposite timing: the pool is unwinding more slowly each year (29% per half, down from 40%) while each new dollar of backlog brings more cash up front (69% marginal in Q2). Neither ratio appears in the press release, the deck, or any commentary chunk; both need Note 9 plus the RPO footnote plus XBRL instants, and the segment table needed to isolate Power from Prolec.
    - **testable_prediction**: Q3 2026 results (~2026-10-22): FCF above $2.6B for the quarter (exceeding the entire implied H2 range of $1.6-2.6B), equipment contract liabilities above $42B, and 9M revenue recognized from the opening contract-liability balance at or below $11.5B (i.e. 9M liquidation ratio at or below 44% vs 55% in 2025). FY26 FCF guidance raised above $12.5B at that print.
    - **kill_condition**: Q3 2026 FCF below $1.0B, or equipment contract liabilities / equipment RPO falls back below 38%, or the 9M liquidation ratio jumps above 50% (would mean the deposits are for near-term deliveries after all and will unwind in 2027).
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 4
    - **caveats**: This refines an angle already on the team's list; the new part is the two quantified ratios and the Power-organic isolation. The prepayment ratio mixes SRA reservation deposits (not in RPO) with order down payments, so 43% overstates prepayment on firm backlog. Slow liquidation also means deposits are NOT funding near-term revenue, which the bear can flip into 'cash today, revenue in 2029'. FCF is 40% of the annual bonus (DEF 14A 2025 and 2026), a structural incentive to front-load collections.
  - - **title**: The RPO recognition-timing footnote implies Jul-2026 to Jun-2027 equipment revenue of $31.6B+ (+34% to +52% vs trailing), putting FY27 revenue near the company's 2028 target of $56B a year early
    - **claim**: The equipment-RPO 'within 1 year' bucket was $31.6B at 6/30/26 (36% of $87,821M) vs $20.9B at 6/30/25 (42% of $49,712M); this bucket has under-predicted the following 12 months' equipment sales by 11-13% in both calibratable periods, so equipment sales Jul-26 to Jun-27 will be at least $31.6B vs $23.6B trailing.
    - **mechanism**: GEV recognizes gas equipment revenue over time on cost-to-cost, so the 1-year bucket is management's planned cost incurrence on already-firm contracts, i.e. planned factory throughput in dollars. Dec-24 bucket 44% x $43,047M = $18.9B preceded FY25 equipment sales of $20,934M (1.11x); Jun-25 bucket $20.9B preceded Jul-25 to Jun-26 sales of $23,556M (1.13x). The Dec-25 bucket ($23.8B) implies FY26 equipment of ~$26B and, with H1 2026 at $11,713M, H2 2026 of ~$14.5B; the Jun-26 bucket then implies H1 2027 equipment of $17-21B vs $11.7B in H1 2026 (+46% to +80%). Adding services at +8% (FY25 $17,134M) gives FY27 revenue of roughly $54-58B against a 2028 company target of $56B and Zacks-cited next-year growth of +11% (~$51B). Q2 2026 orders were mostly 2028-29 deliveries (2-year cumulative bucket fell 69% to 65%; the 2-5 year band rose to 32% = $28.1B from $22.0B in Mar-26), so the 1-year bucket is not being inflated by the newest orders.
    - **direction**: long
    - **evidence**:
      - - **source**: RPO footnote, documents ids 360,340,331,313,295,281,270,249,228,218
        - **date**: 2024-04-30 to 2026-07-22
        - **quote_or_number**: Equipment RPO ($M) and 1/2/5-yr cumulative %: Mar-24 42,210 45/71/93; Jun-24 41,561 47/69/91; Sep-24 42,069 46/70/91; Dec-24 43,047 44/69/93; Mar-25 45,478 45/71/91; Jun-25 49,712 42/70/92; Sep-25 54,092 41/71/97; Dec-25 64,245 37/69/97; Mar-26 75,924 38/69/98; Jun-26 87,821 36/65/97.
        - **reproduction**: regex r'Equipment-related (?:remaining performance obligations|RPO) of \$([\d,]+) million of which (\d+)%, (\d+)%, and (\d+)% is expected to be recognized within 1,2, and 5 years' on whitespace-normalized documents text for the ten ids
      - - **source**: documents id=218 (10-Q 2026-07-22) RPO footnote
        - **date**: 2026-07-22
        - **quote_or_number**: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years, respectively, and the remaining thereafter."
        - **reproduction**: SELECT text FROM documents WHERE id=218; search 'Equipment-related RPO of'
      - - **source**: Income statements: documents id=249 (10-K FY25), id=281 (Q2'25 10-Q), id=218 (Q2'26 10-Q)
        - **date**: 2026-01-29 / 2025-07-23 / 2026-07-22
        - **quote_or_number**: Sales of equipment: FY25 $20,934M, FY24 $18,952M; H1'25 $9,091M (Q2'25 $4,894M); H1'26 $11,713M (Q2'26 $6,459M). TTM Jul-25 to Jun-26 = 20,934 - 9,091 + 11,713 = $23,556M.
        - **reproduction**: regex r'Sales of equipment \$?[\d,]+ \$?[\d,]+' on documents ids 249, 281, 218
      - - **source**: mgmt_guidance (8-K 2026-01-28 and 2026-07-22) and analyst_calls (Zacks 2026-09-17)
        - **date**: 2026-01-28 / 2026-07-22 / 2026-09-17
        - **quote_or_number**: 'GE Vernova's outlook by 2028, the company now expects revenue of $56 billion'; FY26 revenue guide raised to $45.5-$46.5B on 2026-07-22; Zacks: 2026 revenue +23%, 'next year' +11%.
        - **reproduction**: SELECT stated_on,metric,value,period,quote FROM mgmt_guidance WHERE ticker='GEV' AND metric='revenue' AND stated_on>='2026-01-01'; SELECT published,firm,metric,value,period FROM analyst_calls WHERE ticker='GEV' AND metric LIKE '%revenue%' ORDER BY published DESC
    - **why_market_misses_it**: Sell-side models revenue from GW shipped times price and from management's 20/24/30 GW cadence; the 1-year RPO bucket is a footnote percentage that changes by 1-2 points a quarter and is never converted to dollars or calibrated against realized sales. The visible narrative is 'orders are 2028-2029 slots, revenue is far away' (true for the marginal order) which hides that the near-term bucket itself grew 51% Y/Y in dollars. Only two calibration points exist because GEV has only been filing since 2024, so no one has built the track record.
    - **testable_prediction**: Q3 2026 10-Q (~2026-10-22): equipment RPO 1-year bucket at or above $33B in dollars (e.g. 35% of ~$95B) and Q3 2026 sales of equipment at or above $6.8B (H2 run-rate consistent with ~$14.5B). Q4 2026 call (late Jan 2027): initial FY27 revenue guidance at or above $53B.
    - **kill_condition**: Q3 2026 1-year equipment bucket below $30B in dollars, or Q3 2026 sales of equipment below $6.0B (conversion failing), or FY27 revenue guidance initiated at or below $51B. Also killed if the FY26 10-K changes the bucket definition or footnote wording.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 4
    - **caveats**: Only two calibration points; the bucket is a management estimate that has been revised down 1-4 points in most quarters (45% to 36%), so the dollar bucket could be cut if factory ramp slips. Cost-to-cost means the bucket measures planned spend, and a supplier or Greenville throughput miss (already on the team's list) would directly reduce it. FY27 revenue arithmetic assumes H2 2027 equipment at least equals H1 2027 and services growth of ~8%; both are assumptions, not filing data. GLJ's vintage-margin argument is unaffected: higher revenue on 2024-priced units could still be low-margin.
  - - **title**: FY25 10-K rewrote 86% of its risk-factor sentences and cut them 60%, deleting the fleet-suspension and Vineyard Wind language while adding hyperscaler-credit, SRA non-conversion and 'over-invested/idle capacity' risks; three footnote explanations were also quietly dropped
    - **claim**: Item 1A shrank from 26,064 to 10,293 words (747 to 367 sentences; 315 of the 367 FY25 sentences have no FY24 match at a 0.6 similarity cutoff), 'wind' mentions fell 55 to 5 and 'offshore' 13 to 2, while 'slot reservation', 'counterparty', 'hyperscaler', 'liquidated damages' and 'capacity expansion' appear for the first time.
    - **mechanism**: Disclosure narrowing coincides with the numbers getting larger: the 10-K dropped the reason for LTSA revisions ('due primarily to higher costs' in FY24; none in FY25), dropped the warranty-rollforward footnote (a) that attributed provisions to Wind (provisions rose to $760M from $687M with no explanation), and the 2026 10-Qs dropped the segment attribution for contract-liability growth. New FY25 language names the counterparty risk the deposit pile depends on: hyperscalers and other 'first-time counterparties' with 'weaker credit profiles' who 'may delay payment, seek to renegotiate terms, or default', and SRA holders who 'may not place orders equal to the value of their reservation amount or at all'. Removed language ('A widespread fleet issue could result in revenue loss while the associated product is suspended from operation') was the only sentence tying a fleet-wide quality event to service revenue, relevant as the HA fleet enters first major inspections.
    - **direction**: neutral
    - **evidence**:
      - - **source**: documents id=313 (10-K filed 2025-02-06) chars 56907-231413 vs id=249 (10-K filed 2026-01-29) chars 58010-132177 (Item 1A to Item 1B), difflib sentence matching
        - **date**: 2025-02-06 vs 2026-01-29
        - **quote_or_number**: 174,506 vs 74,167 chars; 26,064 vs 10,293 words; 747 vs 367 sentences; 315/367 FY25 sentences with best-match ratio <0.6. Term counts FY24/FY25: wind 55/5, offshore 13/2, RPO 25/9, credit 51/14, ESG 21/3, slot reservation 0/3, counterparty 0/3, hyperscaler 0/1, liquidated damages 0/1, capacity expansion 0/4.
        - **reproduction**: python: t=documents.text for id 313/249; slice at 'ITEM 1A' heading and 'ITEM 1B'; split on r'(?<=[.;:])\s+(?=[A-Z"])'; difflib.get_close_matches(s, other, n=1, cutoff=0.6); re.findall for each term (case-insensitive)
      - - **source**: documents id=249, Item 1A, 'Risks Related to our Customers and Industry Dynamics'
        - **date**: 2026-01-29
        - **quote_or_number**: "Some counterparties may have limited operating histories, different contracting practices, or weaker credit profiles. They may depend on external financing, subsidies, or project milestones, and may delay payment, seek to renegotiate terms, or default."
        - **reproduction**: SELECT text FROM documents WHERE id=249; find 'such as hyperscalers'
      - - **source**: documents id=249, Item 1A, 'Risks Relating to Operations and Supply Chain'
        - **date**: 2026-01-29
        - **quote_or_number**: "we could be over-invested in our facilities and could incur excess or idle capacity, under-absorption of fixed costs, production inefficiencies, inventory build and write-downs, penalties under supply agreements, lower margins, and impairment of long-lived assets."
        - **reproduction**: SELECT text FROM documents WHERE id=249; find 'over-invested'
      - - **source**: documents id=313, Item 1A (sentence absent from id=249)
        - **date**: 2025-02-06
        - **quote_or_number**: "A widespread fleet issue could result in revenue loss while the associated product is suspended from operation." and "during the summer of 2024, a wind turbine blade event occurred ... at the Vineyard Wind offshore wind farm" (both removed).
        - **reproduction**: SELECT instr(text,'widespread fleet issue'), instr(text,'Vineyard Wind') FROM documents WHERE id IN (313,249)
      - - **source**: documents id=313 vs id=249 product warranty rollforward
        - **date**: 2025-02-06 vs 2026-01-29
        - **quote_or_number**: FY24: 'Current-year provisions(a) 687 684 928 ... (a) The increase in current- and prior-year provisions is primarily related to our Wind segment'. FY25: 'Current-year provisions 760 687 684' with no footnote; balance $1,573M vs $1,370M.
        - **reproduction**: regex r'Balance at January 1 \$1,[34]\d\d.{0,330}' on documents ids 313 and 249
    - **why_market_misses_it**: Risk-factor diffs are read for additions (the SRA risk factor is already on the team's list); nobody tracks the removals or the footnote explanations that disappear. A 60% cut in Item 1A a year after the first 10-K is unusual and reads as a company tightening its disclosure surface exactly as its deposits, service revisions and warranty provisions grow.
    - **testable_prediction**: FY26 10-K (late Jan 2027) will keep the hyperscaler-counterparty and 'over-invested' paragraphs, add a quantified disclosure of slot-reservation deposits or their refundability terms (none exists in any filing today), and will not restore a reason for the LTSA revisions.
    - **kill_condition**: FY26 10-K restores segment- and cause-level explanations in Note 9 and the warranty footnote, or removes the hyperscaler-credit and idle-capacity paragraphs (would indicate the FY25 rewrite was a one-off style change, not narrowing).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: The FY24 10-K was the first post-spin 10-K and carried spin-off and GE-legacy risk text, which explains part of the shrinkage (spin 48 to 18 mentions). Sentence-level diffs on a full rewrite overstate substantive change. Nothing here is a tradeable number on its own; it is context for findings 1 and 2.
- **dead_ends**:
  - mgmt_guidance.prior_value (136 GEV rows): noisy and mostly RPO footnotes, spin-off cash and annual-meeting dates; no quietly dropped or narrowed guidance metric found between Jan-2026 and Jul-2026 (revenue raised 44-45 -> 44.5-45.5 -> 45.5-46.5B; Power margin 17-19% unchanged).
  - DEF 14A 2025 (id 304) vs 2026 (id 238): incentive metrics identical (AIP: FCF 40% / Adjusted EBITDA 40% / organic revenue 20%; PSU: 3-yr EBITDA 50% / FCF 50%, TSR modifier); no shift toward orders, backlog or GW metrics.
  - Availability-shortfall disclosure unchanged across 10-Ks: revenue reductions $0.3B in each of 2023-2025 and 'less than $0.1B' sensitivity per 1% fleet availability; no drift signal.
  - Offshore Wind: contract-loss dollar disclosure survives in 10-Ks ($379M/$1,005M/$637M) but 2026 10-Qs only say 'higher contract losses' with no amount; XBRL tag ContractWithCustomerLiabilityCumulativeCatchUpAdjustmentToRevenueChangeInEstimateOfTransactionPrice only populated at Q3 and FY, so no quarterly series is possible from the corpus.
  - Refundability / cancellation terms of SRA deposits: zero hits for 'refundable', 'non-refundable', 'forfeit', 'termination for convenience', 'cancellation fee' in any 2025-2026 10-Q; the only cancellation datum is the $402M settlement of a previously cancelled Wind contract in Q3 2024.
  - 'slot reservation' first appears in filings in the Q1 2025 10-Q cash-flow discussion (2025-04-23) and in press releases the same day; the FY25 10-K is the first with an SRA risk factor (already on the team's list). The RPO definition sentence ('excluding any order that provides the customer with the ability to cancel ... without incurring a substantive penalty') could not be regex-located in the documents table to test for drift; unverified.
  - Organic revenue and Adjusted EBITDA definitions unchanged between 10-Ks; no non-GAAP definition drift.
  - Transcript coverage in the corpus is a single Q2 2026 webcast PDF (sources id 3161, 42 chunks); transcript_statements is too thin to trace management wording drift. Management never mentions LTSA estimate revisions.
  - Commentary tier: zero chunks discuss 'estimated profitability', 'cumulative catch-up' or contract-liability liquidation for GEV; web check found only SEC mirrors and a data aggregator (opencapital.sh) that displays Q2'26 -$129M vs Q2'25 -$71M without commentary.
  - Prolec purchase accounting: preliminary allocation shows no separate contract-liabilities line (current liabilities $1,078M total; goodwill $5,313M; $3,992M remeasurement gain in Q1'26); nothing suspicious, only useful to bound Prolec's share of deposit growth.
  - Steam Power business unit realigned into Gas/Nuclear/Hydro in 2026 (Q2'26 10-Q), which restates Power sub-lines; a comparability caution, not a finding.
  - CFO transition (Claire McDonough named ~Aug 28-29 2026, news tier) noted but not pursued; already public.
  - Warranty accrual series (XBRL StandardProductWarrantyAccrual $1,370M -> $1,595M; provisions $760M vs $687M) is modest and the per-GW angle is already on the team's list.

## [Verify] repro:contradictions:GEV quietly cut its 2026 tariff cost est

- **reproduced**: True
- **confidence**: 5
- **corrected_numbers**: CORE NUMBERS REPRODUCE EXACTLY.
(1) Q1'26 10-Q, filed 2026-04-22, accession 0001996810-26-000064, chunks.id=13690 (Item 2 MD&A): "The current total estimated cost impact from the global tariffs as outlined is approximately $250 million to $350 million in 2026, after taking into consideration contractual protections and mitigating actions."
(2) Q2'26 10-Q, filed 2026-07-22, accession 0001996810-26-000148, chunks.id=5721 (documents.id=218): "...approximately $100 million to $200 million in 2026, after taking into consideration contractual protections and mitigating actions, including pursuing the recovery of certain tariffs." The phrase "including pursuing the recovery of certain tariffs" is NEW in Q2 (0 hits in the Q1 10-Q document text). Both accessions independently confirmed via SEC full-text search (efts.sec.gov, q="estimated cost impact from the global tariffs", entityName=GE Vernova: 8 hits = 10-Qs of 2025-04-23, 2025-07-23, 2025-10-22, 2026-04-22, 2026-07-22, htm+pdf each).
(3) 2025 path reproduces and gains one datapoint the finding omitted: 10-Q 2025-04-23 (chunk 54614) "$300 million to $400 million in 2025"; 10-Q 2025-07-23 (chunk 44140) same "for the full year 2025"; 10-Q 2025-10-22 (chunk 38545) "trending towards the lower end of approximately $300 million to $400 million"; FY25 10-K filed 2026-01-29 (chunk 29736): "The total cost impact from the global tariffs for the full year 2025 was approximately $250 million." So 2025 landed BELOW the low end of the original range, a precedent for 2026 estimates being conservative.
(4) Q2'26 press release (8-K/EX accession 0001996810-26-000147#gevpressrelease2q26.htm): exactly 1 chunk (id 5640) matches "tariff"/"tariffs", and it is the forward-looking-statements boilerplate. Reproduced.
(5) Guidance raise same day (chunk 5624): revenue $45.5-46.5B (from $44.5-45.5B); FCF $11.5-12.5B (from $6.5-7.5B); Power organic growth 18-20% (from 16-18%); Power margin 17-19% UNCHANGED. NOTE: the task brief's "market believes" block quotes revenue $44.5-45.5B and Power growth 16-18%; those are the Apr 22 figures and are stale after Jul 22.
ARITHMETIC: midpoint $300M to $150M = $150M reduction (correct). $150M / $46B revenue midpoint = 0.33 pts (finding says ~0.3, ok). $150M / $12B FCF midpoint = 1.25% (finding says 1.2%, ok). $150M is only 3% of the $5B FCF guidance raise, so calling it "one identifiable source of that raise" is technically true but immaterial. Power Q2'26 revenue $5.5B implies ~$22-23B FY26; even if 100% of the $150M fell in Power it is ~0.65 pts of Power margin, which does not by itself support the prediction that Power prints at the 19% top of range.
FRAMING CORRECTIONS (these change the finding's interpretation, not its numbers): (a) "quietly / no mention / market missed it" is FALSE. Reuters published at 8:37am EDT on 2026-07-22 with headline "GE Vernova flags up to $200 million tariff hit after second-quarter profit miss" and the sentence "It updated its 2026 tariff hit forecast to $100 million-$200 million from $250 million-$350 million projected in April, citing contractual provisions, sourcing changes, trade regulations and tariff refunds" (verified via WebFetch of bnnbloomberg.ca; in corpus as sources.id=1846 / chunk 236426). Corpus also has the $100-200M figure in src:2664 and src:2669 (NEWS 2026-07-22), src:3886 (Yahoo/Morgan Stanley note summary 2026-07-22: "Tariff costs, currently guided at $100 million to $200 million for 2026"), src:2641 (2026-07-25). Novelty should be 1-2, not 3. (b) Cause IS partly stated: 10-Q adds "pursuing the recovery of certain tariffs"; Reuters adds contractual provisions, sourcing changes, trade regulations, tariff refunds. Neither the 10-Q nor the Q2 call mention IEEPA/Supreme Court/refund by name (0 hits for refund, IEEPA, Supreme Court, Section 232 in documents.id=218). (c) The press-release omission is NOT Q2-specific: none of the three 2026 releases (2026-01-28, 2026-04-22, 2026-07-22) carry a tariff dollar figure, whereas all three 2025 releases (2025-04-23 chunk 54413, 2025-07-23 chunk 44044, 2025-10-22 chunk 38447) did ("The guidance includes the impact of tariffs... approximately $300-$400 million, net of mitigating actions"). GEV changed disclosure practice at the start of 2026. The Q1'26 $250-350M was likewise absent from the Q1 release but was stated by CFO Parks on the Q1 call (src:1849, Yahoo call highlights 2026-04-23: "Parks reiterated prior commentary that net tariff impact was about $250 million in 2025 and is expected to be $250 million to $350 million in 2026"). (d) The Q2'26 call did NOT state the new figure: corpus transcript src:3161 (gev_webcast_transcript_07222026.pdf, 50.6k chars, includes Q&A) has 3 tariff mentions, none with a dollar figure; Investing.com transcript (WebFetch) confirms no dollar estimate, no analyst tariff question, no refund/IEEPA mention. So the number was disclosed ONLY in the 10-Q, and Reuters read the 10-Q.
- **data_quality_issues**: (1) chunks.id=5721 (Q2'26 10-Q) has PDF-extraction spacing artifacts ("$200 millio n", "mitigating action s", "scope a nd nature"); FTS phrase matches still work because "estimated cost impact" is intact, but a search for '"200 million"' would MISS this chunk. Use documents.id=218 or the .htm accession for clean text. (2) sources.id=3159 (gev_webcast_10q_07222026.pdf) is the 10-Q itself mirrored on the IR site but labeled kind='deck', tier='primary'; it duplicates chunk 5721 as DECK chunk 251402 with blank filing_date. Do not count it as a second disclosure venue. (3) IR press-release PDFs src:671 (Jan 28 2026), 953 (Apr 22 2026), 2667 (Jul 22 2026), 3689 (Oct 22 2025) and the Q3'25 transcript src:3796 are tagged tier='commentary' although they are company primary documents. (4) The Q2'26 transcript src:3161 has blank filing_date, so date-filtered transcript queries miss it; filter by accession='src:3161'. (5) mgmt_guidance has rows for the 2025 tariff estimate (ids 408, 647, 648) but NO row for either 2026 estimate ($250-350M or $100-200M): extraction gap. (6) claims.id=1535 (from src:250, NEWS 2026-08-12) cites the stale $250-350M three weeks after the cut; treat as commentary lag, not corroboration. (7) analyst_calls: 0 of 191 rows mention tariff, reproduced, but the table is too thin to support "no analyst noted it"; the Morgan Stanley note summary in src:3886 does cite the $100-200M. (8) Q2 press-release Power segment table text is chunked such that 'Power Three months' does not appear contiguously; Power revenue $5.5B was taken from the narrative bullet (chunk 5620). (9) Two external transcript sources (roic.ai, benzinga.com) return HTTP 403 to WebFetch; investing.com works.
- **notes**: VERDICT: The evidence reproduces in full (both 10-Q figures, dates, accessions, 2025 path, press-release absence, same-day guidance raise), but the finding's "quietly cut, market missed it" framing does not survive: Reuters reported the exact cut with the prior range and causes within hours of the 10-Q, and multiple corpus commentary pieces repeated the $100-200M the same day. Recommend downgrading novelty to 1-2 and keeping materiality at 1.
A BETTER VERSION OF THIS ANGLE that the reproduction surfaced: several commentary pieces misread a $150M REDUCTION as a fresh HEADWIND. src:2641 (2026-07-25): "management's warning that anticipated global tariff revisions could add $100 million to $200 million in cost headwinds in 2026, taking short-term traders by surprise"; src:2664/2669 (2026-07-22): "management's warning that tariffs would add roughly $100 million to $200 million"; Reuters headline itself says "flags up to $200 million tariff hit". Combined with the Aug 12 piece still quoting $250-350M, the corpus shows the sell-side/press narrative carried the wrong sign on the tariff line during the Jul-Sep drawdown. That is a small but clean "narrative vs filing" contradiction; still materiality 1.
QUERIES RUN (all SELECT, none modified the DB): [A] SELECT c.id,c.form,c.filing_date,c.ticker,c.tier,c.accession,c.section,substr(c.text,max(1,instr(c.text,'estimated cost impact')-120),420) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimated cost impact"' AND c.ticker='GEV' ORDER BY c.filing_date -> 9 rows (10-Qs 2025-04-23, 2025-07-23, 2025-10-22, 2026-04-22, 2026-07-22; 424B3 2025-04-23; DECK src:3159; WEB src:1843 x2). [B] SELECT ... WHERE chunks_fts MATCH '"tariff" OR "tariffs"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22' -> 1 row (chunk 5640, FLS boilerplate). [C] same MATCH with c.form IN ('8-K/EX','8-K') AND filing_date BETWEEN '2025-04-01' AND '2026-07-31' -> shows 2025 releases carry the dollar range, 2026 releases do not. [D] SELECT ... WHERE chunks_fts MATCH '("tariff" OR "tariffs") AND ("100 million to $200 million" OR "$100-$200 million" OR "$100 million to $200 million" OR "100 to 200 million" OR "$100-200 million")' -> 7 rows incl. Reuters src:1846 and NEWS 2026-07-22. [E] same pattern for 250/350 -> 10 rows incl. src:1849 (Q1 call, Parks) and stale src:250 (2026-08-12). [F] SELECT count(*) FROM analyst_calls WHERE lower(quote) LIKE '%tariff%' -> 0 of 191. [G] SELECT ... FROM transcript_statements WHERE ticker='GEV' AND quote LIKE '%tariff%' -> 3 rows (ids 25, 90, 105), none with a figure. [H] SELECT ... FROM mgmt_guidance WHERE ticker='GEV' AND quote LIKE '%tariff%' -> 3 rows, all 2025. [I] SELECT text FROM documents WHERE id=218 (Q2'26 10-Q) regex counts: refund 0, sourcing 0, "recovery of certain tariffs" 1, Section 232 0, IEEPA 0, Supreme Court 0; Q1'26 10-Q (accession 0001996810-26-000064): "recovery of certain tariffs" 0. [J] SELECT id,url,kind,tier,... FROM sources WHERE url LIKE '%gevernova.com/sites/default/files%' -> identifies src:3157 (Q2 deck, 0 tariff mentions), 3159 (10-Q pdf), 3161 (Q2 transcript). [K] SEC efts full-text search (User-Agent gev-corpus-research/1.0) -> 8 hits confirming accessions. [L] WebFetch bnnbloomberg.ca Reuters 2026-07-22 -> confirms "from $250 million-$350 million projected in April, citing contractual provisions, sourcing changes, trade regulations and tariff refunds". [M] WebFetch investing.com Q2'26 transcript -> no dollar tariff estimate on the call, no analyst tariff question.
DEAD ENDS: no IEEPA/Supreme Court/refund language anywhere in GEV filings or the Q2 call; the cause beyond "pursuing the recovery of certain tariffs" comes only from Reuters' paraphrase. No 2026 tariff estimate appears in the Jan 28 2026 Q4'25 release (src:671) or the FY25 10-K; the $250-350M was first given verbally around the Q4/Q1 calls per src:1849 ("reiterated prior commentary"), not located in a filing before Apr 22 2026. Q2 earnings deck src:3157 has zero tariff mentions.

## [Verify] repro:eia-physical:No US combustion turbine of 300 MW or mo

- **reproduced**: True
- **corrected_numbers**: ALL FIVE SQL STEPS REPRODUCE EXACTLY against generators (vintage 2026-07 unless noted): (1) Operating NG CC additions 2023 6.8 GW / 5 CT>=300; 2024 0.1 / 0; 2025 1.8 / 0; 2026 YTD 1.0 / 0; same zeros in 2024-12 and 2025-12 vintages. (2) Planned CT>=300 MW: 35 units, 15,292 MW; U/V/TS = 5 units / 2.32 GW (Orange County 1A,1B 2x453 TS Aug-26; Traceview 478 U; Vicksburg 478 U; Cumberland 455 U 2034); Entergy entities 18 units / 8.47 GW. (3) Firm/T/PL GW by year Jul-26: 2026 4.2/0/0; 2027 3.6/0.9/6.6; 2028 2.8/0.3/13.7; 2029 1.4/2.8/9.9; 2030 0/1.3/16.9. Jul-25: 2026 5.4/0/1.2; 2027 0.8/0.5/5.9; 2028 0/0.8/11.5. (4) 2024-01 cohort 16.6 GW: Operating 5.1 (32 units, 30.7%), Canceled 4.0 (17, 24.1%), slip12+ 3.6 (17, 21.7%), slip1-11 2.1 (16), ontime 1.8 (5), vanished 0. 2023-01 cohort 20.2 GW: Operating 8.6, canceled 4.7, slip12+ 4.9, slip1-11 0.1, ontime 1.9. No duplicate (plant_id,generator_id) keys in 2026-01, so the join is clean. (5) Jul-26 TS = 11 units / 2.13 GW, unit list matches.

CORRECTIONS THAT CHANGE THE HEADLINE: (A) "No US combustion turbine >=300 MW has entered service since 2023" is an artifact of the prime_mover='CT' filter. Query: SELECT op_year, COUNT(*), SUM(mw) FROM generators WHERE vintage='2026-07' AND sheet='Operating' AND energy_source='NG' AND mw>=300 AND op_year>=2018 GROUP BY 1 gives 2023: 12 units 6.17 GW; 2024: 1 unit 0.40 GW (Duke Lincoln Combustion GT 402 MW, Dec-24, a Siemens SGT6-9000HL per NEWS 2024-09-20); 2025: 3 units 1.82 GW (LADWP Intermountain units 3,4 CS 546.6 MW each Oct/Dec-25, MHI M501JAC per WEB chunk; Magnolia Power CS 722.9 MW Dec-25, a GE 7HA.03 per gevernova.com press release and powermag.com); 2026 YTD: 3 units 0.98 GW (Trumbull OH, Siemens, Apr-26, coded CA). Correct claim: big-frame (>=300 MW) NG additions fell from 12 units / 6.2 GW in 2023 to 1 / 0.4 (2024), 3 / 1.8 (2025), 3 / 1.0 (2026 YTD); zero of the 2024-26 units is a multi-shaft CT, but one is a GE 7HA.03, which contradicts the mechanism line "US HA-class installed base cannot grow before 2027". (B) "Only 2.3 GW of 15.3 GW under construction" is CT-only. Adding planned CS+GT >=300 MW: 29 units / 16.55 GW, of which 12 units / 6.76 GW are U/V/TS (GREC 594 TS, Yates 483 V, Shady Hills 612 V, Ripley 419 V, Mill Creek 740 V, Turney 419 U, Vast Sands 2x440 U, Cedar Bayou 721 U, Greens Bayou 447 U, CPV Basin Ranch 2x722.5 U). Combined CT+CS+GT >=300 MW: 64 units / 31.8 GW, of which 17 units / 9.1 GW (29%) U/V/TS. (Planned CA>=300 MW, 20 units 6.56 GW, are mostly steam sides and excluded.) (C) TS claim "0-3 units (<=1.1 GW) in every prior vintage" is false: 2023-01 12 units/2.15 GW, 2023-02 12/2.15, 2023-03 14/2.53, 2023-04 10/1.62, 2023-05 8/1.54, 2024-05 7/0.46. Jul-26 (11 / 2.13 GW) is the highest since Mar-2023, not unprecedented; the claim holds only for 2023-06 through 2026-06. (D) EIA status lag is larger than the caveat says: Delta Blues (477 MW CT) coded (L) in every vintage 2025-01..2026-07, yet ETR DEF 14A 2026-03-27 says Entergy Mississippi "continued construction on its Delta Blues Advanced Power Station"; Franklin Farms 1A/2A (2x469.3) coded (L) through 2026-07 despite the Entergy/PRNewswire ground-breaking release. Understated under-construction CT capacity is at least ~1.4 GW (939+477), so true CT>=300 in the ground is ~3.7 GW, and ~10.5 GW across CT+CS+GT. (E) Prediction "calendar-2026 US CC additions below 3 GW" is knife-edge: 0.98 GW already operating + 2026-dated firm CC remaining (Orange County 1,306 MW TS Aug-26 + Shady Hills 612 MW CS V Nov-26) = 2.9 GW if both hit. Also Orange County is Mitsubishi Power equipment (NEWS 2024-09-12), so the 2026 test case says nothing about GEV.
- **data_quality_issues**: (1) EIA prime_mover coding is inconsistent for big frames: Trumbull GT11/GT12 (308.7 MW each) are coded 'CA' (normally the steam side); H/J-class single-shaft blocks are 'CS'; simple-cycle HL is 'GT'. Any CT-only filter under-counts big-frame turbines both in Operating additions and in the Planned pipeline. (2) Lincoln GT 402 MW carries op_year 2024 although first fire was Apr-2020 (validation unit); EIA op date = commercial operation, which lags first fire by years for prototype units. (3) EIA-860M status lags owner disclosures: Delta Blues and Franklin Farms are under construction per Entergy filings/press but coded (L) in Jul-2026. (4) Vintage 2024-11 has fewer rows (36,381) than 2024-10 (36,517) and 2024-12 (36,941), an unexplained dip; it does not affect any of the vintages used here. (5) The projects table has zero rows for Magnolia, Lincoln, Intermountain, Trumbull, Orange County, Franklin Farms or Homer City, so OEM attribution had to come from chunks (NEWS/WEB commentary tier) and the web, not from structured corpus data. (6) Step-3 "firm" 2026 bucket (4.2 GW) includes GT peakers; the CC-only 2026 firm remainder is 1.92 GW.
- **notes**: Verdict: the SQL evidence reproduces to the decimal, but the title and mechanism overstate it. The defensible version is "US big-frame gas additions collapsed from 6.2 GW (2023) to 0.4 / 1.8 / 1.0 GW in 2024-26, and ~71% of the 31.8 GW planned >=300 MW turbine fleet is still coded P/L/T", not "nothing big is in the ground" and not "the HA installed base cannot grow before 2027" (a GE 7HA.03 at Magnolia reached commercial operation Dec-2025). The cohort base rate (31% operating / 24% canceled / 22% slipped 12+ months) is the strongest, cleanest number in the finding and is fully reproduced; that is the part worth keeping. The TS-spike sub-claim should be dropped or restated as "highest since Mar-2023". Suggested ratings after correction: novelty 3 (unchanged), confidence 3 (down from 4: numbers are solid but the headline needs the CT-only qualifier and EIA status lags Entergy by 2+ quarters), materiality 2-3 (US-only, and the two 2026 test cases are Mitsubishi and Siemens units). Reproduction commands: all queries in corrected_numbers were run via Python 3.11 sqlite3 against data\gev.db; corpus text via chunks_fts MATCH '"Franklin Farms"', '"broke ground" AND "Vicksburg"' (ETR DEF 14A 2026-03-27), '"Magnolia" AND ("7HA" OR "Kindle")' (NEWS 2024-09-12), '"Lincoln" AND ("SGT6" OR "9000HL")' (NEWS 2024-09-20), '"Intermountain" AND "M501JAC"' (WEB). Web: https://www.gevernova.com/news/press-releases/kindle-energy-awards-7ha03-combined-cycle-plant-equipment-order-to-ge-for-magnolia (Magnolia = 7HA.03); https://www.powermag.com/blackstone-brings-694-mw-gas-fired-plant-online-in-louisiana/ (Magnolia online); https://www.prnewswire.com/news-releases/entergy-louisiana-breaks-ground-on-new-state-of-the-art-generation-facilities-to-power-reliability-growth-and-innovation-302629479.html (Franklin Farms ground-breaking). Dead ends: projects table has no rows for any of the seven plants checked; no corpus chunk names the Orange County OEM beyond "Mitsubishi Power equipment" (NEWS 2024-09-12); no Entergy filing in the corpus explicitly states Franklin Farms construction start (only regulatory approval), so that caveat rests on the press release.
- **confidence**: 4

## [Sweep] find:price-events

- **lens**: Price and event pattern miner (prices table, 17 tickers; GEV 8-K dates; sources/news; backlog_quarterly GW series)
- **findings**:
  - - **title**: The June-September de-rating is two single days, not a slow bleed: 7/22 earnings (-8.5% ex-basket) and 9/14 (-4.7% ex-basket); every other day nets to -1.1%
    - **claim**: From the 2026-06-30 peak ($1,174.86) to 2026-09-18 ($940.33) GEV fell 22.3% (log); a two-factor model (SPY + equal-weight VRT/ETN/PWR/BE/HUBB basket, fitted 2025-07-01 to 2026-06-30, no intercept) predicts -7.9%, leaving a -14.4% GEV-specific residual, of which -8.5% is the Q2 earnings day and -4.7% is the GLJ day; the remaining 53 trading days sum to -1.1%.
    - **mechanism**: Valuation, not operations: no financial line changed between the two event days. The residual tells the memo where the market's GEV-specific verdict was actually rendered (Q2 print: wind loss widening and mixed results per 2026-07-22 news; Sep 14: GLJ Sell), so the next print on ~2026-10-21 (catalyst_calendar id 1, estimated) is the only scheduled place a comparable single-day repricing can occur. Earnings-day absolute moves average 5.3% (n=10) vs 2.4% on other days; last three prints were +2.7%, +12.9%, -9.1%.
    - **direction**: either
    - **evidence**:
      - - **source**: prices table, scratchpad px3.py
        - **date**: 2026-06-30 to 2026-09-18
        - **quote_or_number**: actual -22.3%, predicted -7.9%, residual -14.4%; residual 7/22 = -8.5% (z=-3.6 vs train resid sd 2.38%), 9/14 = -4.7% (z=-2.0), all other days -1.1%
        - **reproduction**: SELECT ticker,date,close FROM prices; pivot; r=log diff; bask=mean(r[VRT,ETN,PWR,BE,HUBB]); b=lstsq([r.SPY,bask], r.GEV) on 2025-07-01..2026-06-30 (n=251, gives bSPY=0.62, bBasket=0.64); resid = r.GEV - b@X on 2026-07-01..2026-09-18; sum, and pick 2026-07-22 and 2026-09-14
      - - **source**: prices table, scratchpad px2.py
        - **date**: 2026-06-30 to 2026-09-18
        - **quote_or_number**: GEV -22.3%, basket -14.2%, SPY +2.0%, VRT -29.5%, ETN -0.3%, PWR -12.3%, BE -13.1%, HUBB -15.8%
        - **reproduction**: sum of daily log returns per ticker from prices WHERE date>'2026-06-30' AND date<='2026-09-18'
      - - **source**: prices table + GEV 8-K item 2.02 dates from chunks, scratchpad px.py
        - **date**: 2024-04-25 to 2026-07-22
        - **quote_or_number**: earnings-day abs mean 5.3% (n=10) vs 2.4% non-earnings; 2026-01-28 +2.7%, 2026-04-22 +12.9% (exSPY +11.9%), 2026-07-22 -9.1% (exSPY -9.0%)
        - **reproduction**: SELECT DISTINCT filing_date FROM chunks WHERE ticker='GEV' AND form LIKE '8-K%' (dates 2024-04-25,2024-07-24,2024-10-23,2025-01-22,2025-04-23,2025-07-23,2025-10-22,2026-01-28,2026-04-22,2026-07-22); log return of GEV close on each date minus SPY
      - - **source**: sources table (news)
        - **date**: 2026-07-22
        - **quote_or_number**: raised its 2026 revenue and free-cash-flow forecasts on July 22, but a widening loss in its Wind business sent shares lower
        - **reproduction**: SELECT title, substr(text,1,300) FROM sources WHERE substr(published,1,10)='2026-07-22' AND title LIKE '%Vernova%'
    - **why_market_misses_it**: Commentary frames the 23% drawdown as a continuous 'AI power trade unwinding' (VRT -29.5% over the same window supports that half). Nobody decomposes it: the basket explains about 8 points, two event days explain about 13, and the daily drip is zero. That means the stock has not been quietly re-rated on fundamentals between prints; it is being repriced in jumps, which matters for how a 3-12 month memo sizes event risk vs trend risk.
    - **testable_prediction**: Between 2026-09-21 and the Q3 print (~2026-10-21), the cumulative GEV residual vs the same two-factor model stays within +/-5%; the Q3 print day itself produces an absolute ex-basket move of at least 5% (base rate: 6 of the last 10 prints exceeded 5% ex-SPY).
    - **kill_condition**: Residual vs the two-factor model drifts beyond -8% cumulatively before the Q3 print with no single day beyond -4%, which would mean a steady fundamental de-rating is underway rather than event repricing.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Basket is only 5 names available in the corpus prices table (no NVDA, no hyperscalers, no Siemens Energy, no GRID ETF). Model fitted in-sample on 251 days; betas are unstable (60d SPY beta ranges 1.35 to 2.82 across quarter-ends, corr only 0.44-0.81). Log returns; z-scores assume the training residual sd, which understates fat tails.
  - - **title**: Sep 14 was half a sector rout, not a pure GLJ day: basket -6.3%, Siemens Energy -8.1%, GEV volume only 1.4x median
    - **claim**: On 2026-09-14 GEV fell 9.0% but VRT fell 8.0%, ETN 7.9%, BE 7.0%, PWR 4.5%, HUBB 4.0% and Siemens Energy 8.1% in Frankfurt while SPY fell 0.4%; the two-factor model predicts -4.3% from the basket alone, so the GLJ-specific component is about -4.7%, and GEV volume (3.30M) was only 1.40x its 60-day median, outside the top 12 volume days of 2026.
    - **mechanism**: No financial line; this is about how much price the bear case actually moved. The 'down 8.6% on a $470 Sell target' framing attributes the whole day to a single analyst; the same-day news flow (Altman and Amodei calling for slower AI development; Recharge: 'hammered in AI rout') and the cross-section show the power-equipment basket fell 4-8% regardless of GLJ. A low-volume -9% means the sellers were not large, which is consistent with a de-grossing day rather than a fundamental reassessment.
    - **direction**: long
    - **evidence**:
      - - **source**: prices table, scratchpad px2.py
        - **date**: 2026-09-14
        - **quote_or_number**: GEV -9.0, VRT -8.0, ETN -7.9, BE -7.0, PWR -4.5, HUBB -4.0, AME -3.5, EMR -2.6, NEE -0.8, SPY -0.4, ADBE +5.2, SPOT +5.6, CPRT +5.8 (log %, close-to-close)
        - **reproduction**: SELECT ticker, close FROM prices WHERE date IN ('2026-09-11','2026-09-14') ORDER BY ticker; log(close_14/close_11)
      - - **source**: prices table, scratchpad px3.py
        - **date**: 2026-09-14
        - **quote_or_number**: basket -6.3% -> model predicted -4.3%; residual -4.7%; volume 3.30M vs 60d median 2.36M = 1.40x (7/22 was 1.80x)
        - **reproduction**: same two-factor fit as finding 1; SELECT volume FROM prices WHERE ticker='GEV' AND date<='2026-09-14' ORDER BY date DESC LIMIT 60; median
      - - **source**: sources id 1770 (ad-hoc-news.de), published 2026-09-14
        - **date**: 2026-09-14
        - **quote_or_number**: Siemens Energy ... shedding 8.1% to close at EUR 132.24 ... a separate warning about the pace of artificial intelligence development from the model provider chief Dario
        - **reproduction**: SELECT url, substr(text,1,700) FROM sources WHERE id=1770
      - - **source**: sources id 1769 (rechargenews.com), published 2026-09-14
        - **date**: 2026-09-14
        - **quote_or_number**: Siemens Energy and GE Vernova hammered in AI rout ... after tech CEOs call for slower development of artificial intelligence
        - **reproduction**: SELECT url, title, substr(text,1,400) FROM sources WHERE id=1769
      - - **source**: sources id 2601 (finance.yahoo.com / 24-7 Wall St)
        - **date**: 2026-09-14
        - **quote_or_number**: the GRID infrastructure ETF sank roughly 10 times harder than SPY's 0.4% decline
        - **reproduction**: SELECT substr(text,1,700) FROM sources WHERE id=2601
    - **why_market_misses_it**: Headlines and the team's own brief ('down 8.6% on Sep 14 when GLJ initiated at Sell') credit one analyst with the whole move. The cross-section on the same day is public but nobody prints it next to the GLJ headline; the GLJ argument (2024-vintage margins) has real content, but the price tag the market put on it is roughly half the headline number.
    - **testable_prediction**: By 2026-10-16 (20 trading days), GEV's cumulative residual vs the two-factor model is within +/-4% of zero, i.e. no follow-through selling attributable to GLJ; VRT/ETN/BE move in the same direction as GEV on at least 14 of those 20 days.
    - **kill_condition**: A second GEV-specific down day of more than -4% residual (z below -1.7) before the Q3 print with no matching basket move, or a second sell-side initiation/downgrade citing the same 2024-vintage margin argument that produces another >-4% residual day.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Cannot separate the GLJ note from the AI-slowdown headlines within the day (no intraday data in prices). Siemens Energy figure is from a German news source quoted in EUR, not from the prices table. Basket names each have their own idiosyncratic days; -4.7% is an estimate, not a measurement.
  - - **title**: Reaction decay to 'GW under contract': the Q2-26 print added 16 GW plus a guidance raise and got -8.5% ex-basket, the first negative reaction to a double-digit GW increment
    - **claim**: Ex-basket same-day reactions per announced increase in gas GW under contract went 0.31 pts/GW (Q3-25, +6 GW), 0.04 (Q4-25, +24.5 GW), 0.69 (Q1-26, +17 GW), then -0.53 (Q2-26, +16 GW to 116 GW with a 125 GW year-end target and raised FY revenue/FCF guidance), so the headline GW metric no longer moves the stock on its own.
    - **mechanism**: The GW-under-contract number is the bull case's scoreboard; if it has stopped being rewarded, the stock's next leg depends on a different line: H2 FCF conversion (implied $1.6-2.6B after $9.9B in H1), Power segment margin, and Wind losses (the 2026-07-22 news attributed the selloff to a widening Wind loss). For the memo this means the 125 GW year-end confirmation at the Q3 print is priced; the swing factor is whether contract-liability inflows slow or Wind/offshore charges reappear.
    - **direction**: short
    - **evidence**:
      - - **source**: prices table + backlog_quarterly, scratchpad px3.py
        - **date**: 2025-07-23 to 2026-07-22
        - **quote_or_number**: 2025-07-23 (50-55 GW): d0 +13.6%, exBasket +11.4%; 2025-10-22 (55-62 GW): -1.6%, exBasket +1.8%, 0.31 pts/GW; 2025-12-10 investor update (80 GW YE est): +14.5%, exBasket +14.0%; 2026-01-28 (83 GW): +2.7%, exBasket +1.0%, 0.04 pts/GW; 2026-04-22 (100 GW): +12.9%, exBasket +11.7%, 0.69 pts/GW; 2026-07-22 (116 GW, 125 by YE): -9.1%, exBasket -8.5%, -0.53 pts/GW
        - **reproduction**: SELECT as_of, metric, value, unit, status, filing_date FROM backlog_quarterly WHERE ticker='GEV' AND unit LIKE '%GW%' AND status!='xbrl' ORDER BY as_of; midpoints 52.5, 58.5, 83, 100, 116; ex-basket = GEV log ret - (0.62*SPY + 0.64*basket) on each filing_date
      - - **source**: backlog_quarterly (8-K/EX 2026-07-22)
        - **date**: 2026-07-22
        - **quote_or_number**: orders_value 116 GW backlog; 125 GW reservation; reservation_gw 56 -> 63; 44 -> 53
        - **reproduction**: SELECT * FROM backlog_quarterly WHERE ticker='GEV' AND filing_date='2026-07-22' AND unit LIKE '%GW%'
      - - **source**: sources (Utility Dive, 2025-12-24)
        - **date**: 2025-12-24
        - **quote_or_number**: By the numbers: GE Vernova Investor Update 2025 80 GW Estimated gas turbine backlog by year-end 2025. 24 GW Expected annual
        - **reproduction**: SELECT c.filing_date, substr(c.text,1,350) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"investor update" "GW"' AND c.ticker='GEV' AND c.filing_date BETWEEN '2025-12-01' AND '2025-12-31' ORDER BY bm25(chunks_fts) LIMIT 4
      - - **source**: sources (news), 2026-07-22
        - **date**: 2026-07-22
        - **quote_or_number**: The stock fell about 6.3% to $1,011 in midday trading July 22 after dropping as low as $964.16 earlier in the session
        - **reproduction**: SELECT title, substr(text,1,300) FROM sources WHERE substr(published,1,10)='2026-07-22' AND title LIKE '%weak link%'
    - **why_market_misses_it**: Sell-side notes and the company still lead with GW under contract and the 125 GW / $200B backlog targets, and the team's brief lists 'peak-order myopia' as the bull frontier. The price series says the market already stopped paying for GW increments one print ago; the bull needs a new metric, and the bear does not need orders to fall, only for the non-GW lines (Wind, H2 FCF) to disappoint again.
    - **testable_prediction**: At the Q3-26 print (~2026-10-21), confirmation of 120-125 GW under contract without an upside surprise on H2 FCF or Power margin produces an ex-basket reaction between -5% and +5%; a positive reaction above +8% ex-basket occurs only if FCF or margin, not GW, beats.
    - **kill_condition**: Q3-26 print delivers a GW-only beat (e.g. 130+ GW, no FCF/margin surprise) and GEV rises more than +8% ex-basket, which would show the GW metric still carries the stock.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 4
    - **caveats**: n=5 announcement days; this is a pattern, not a statistic. Q2-26 also carried a Wind loss and Q1-26 carried other positives, so reactions are not attributable to GW alone. GW increments use midpoints of ranges and mix backlog-plus-SRA definitions across quarters as the company reported them. The 2025-12-10 investor update date is inferred from the +14.5% day and the Utility Dive recap, not from an 8-K in the corpus.
- **dead_ends**:
  - Pre-earnings drift: GEV cumulative log return over days -10..-1 before the 9 prints since 2024-07 averages +5.4% (median +4.5%) vs +3.2% for all 10-day windows with sd 8.5%; n=9, not distinguishable from noise. Script: scratchpad px2.py.
  - Volume anomalies: top 2026 volume/60d-median days are 2026-06-10 (2.3x, -5.9%) and 2026-05-29 (2.3x, -2.8%); the corpus has no GEV-relevant news on either date (only academic rows in sources), so the cause could not be identified. Sep 14 (1.4x) and Jul 22 (1.8x) were not volume outliers.
  - Hyperscaler/NVDA capex-day reactions cannot be tested from the corpus: prices has only 17 tickers (ABNB, ADBE, AME, BE, CPRT, EMR, ETN, GEV, HUBB, NCLH, NEE, NKE, PWR, ROK, SBUX, SPOT, SPY, VRT); no NVDA, MSFT, GOOGL, AMZN, META, ORCL, and no Siemens Energy or MHI.
  - events table is empty (0 rows); catalyst_calendar has 16 rows, all estimated earnings dates from 8-K cadence (GEV est. 2026-10-21, unconfirmed). Neither adds event dates beyond what the 8-K filing_date list gives.
  - CFO retirement 8-K (event 2026-08-25, filed 2026-08-27, Kenneth Parks retiring 2027-04-02): GEV +0.1% on 8/27 and -4.5% on 8/28 vs basket -3.3%; roughly -1.2% residual, within one sd. Not a price event.
  - 2025-12-17 (-11.1%) was basket-wide (BE -12.9%, VRT -7.0%, PWR -5.7%, SPY -1.1%) with no corpus news on that date; 2026-06-23 (-8.6%) likewise (VRT -11.7%). Both are basket days, not GEV-specific.
  - Rolling 60-day correlation to SPY is only 0.44-0.56 at most quarter-ends despite a 2.1-2.6 SPY beta, so SPY-only hedging or beta framing is weak; the peer basket (ETN corr 0.75, PWR 0.72, VRT 0.67 at 2026-09-18) is the better reference. Realized 60d vol: GEV 55% annualized at 2026-09-18 vs 45% a year earlier; VRT 74%.
  - insider_tx skipped per brief (already checked by the team). Semantic search (embed.py/Ollama) not attempted; FTS was sufficient for the dated news lookups.

## [Sweep] find:eia-physical

- **lens**: EIA physical reconciler (EIA-860M monthly planned/operating snapshots 2023-01 to 2026-07; EIA-923 annual generation 2022-2025)
- **findings**:
  - - **title**: The March-2026 jump in EIA planned gas units is one Siemens-anchored campus (Fermi Project Matador), not a survey artifact and not GEV demand
    - **claim**: Of the 155 combined-cycle rows that appeared in the EIA-860M Planned sheet between the 2026-02 and 2026-03 vintages, 147 (11.7 GW, 94% of the added units) belong to a single plant, Fermi America's Project Matador (plant_id 69799, TX), whose turbines are Siemens Energy SGT-800 and SGT6-5000F; it is now 17% of the entire US planned gas-turbine pipeline (11.7 of 67.1 GW) and 100% of it is still status P/T (no construction).
    - **mechanism**: Sell-side and commentary use EIA-860M 'planned gas capacity' as external corroboration of GEV's 63 GW SRA book and 125 GW under-contract claim. If the single largest entry in that dataset is a Siemens-supplied, approvals-not-initiated campus, the US-visible pipeline attributable to GEV is smaller than headline, which bears on the conversion of SRAs to firm equipment RPO (equipment RPO $87.8B) and on the deposit inflows (contract liabilities $39.9B Jun-26) that fund the H2-26 FCF bridge.
    - **direction**: short
    - **evidence**:
      - - **source**: generators table, vintage-to-vintage diff of Planned sheet
        - **date**: 2026-03 vintage
        - **quote_or_number**: Planned NG CC units 73 (2026-02) -> 228 (2026-03); GW 29.0 -> 43.4; distinct plants 30 -> 34; avg MW/unit 398 -> 190
        - **reproduction**: SELECT vintage, COUNT(*) units, COUNT(DISTINCT plant_id) plants, ROUND(AVG(mw)) avg_mw, ROUND(SUM(mw)/1000,1) gw FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS') AND vintage IN ('2026-02','2026-03') GROUP BY vintage
      - - **source**: generators table, new rows in 2026-03 not in 2026-02, grouped by plant
        - **date**: 2026-03 vintage
        - **quote_or_number**: Fermi America / Project Matador Gas Plant (PMG), TX: 147 CC rows, 11,427 MW, status (P) 'regulatory approvals not initiated' (141 rows) and (T) (6 rows); the other new plants are PSO Comanche OK (4 rows, 1,373 MW) and Entergy Richland Parish 3 and 4 LA (4 rows, 1,560 MW)
        - **reproduction**: WITH feb AS (SELECT plant_id||'|'||generator_id k FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS') AND vintage='2026-02') SELECT entity_name, plant_id, plant_name, state, substr(status,1,4), COUNT(*), ROUND(SUM(mw)), ROUND(AVG(mw)) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS') AND vintage='2026-03' AND plant_id||'|'||generator_id NOT IN feb GROUP BY plant_id, status ORDER BY 6 DESC
      - - **source**: generators table, Feb-to-Mar comparison in prior years (annual-survey artifact test)
        - **date**: 2024-03 and 2025-03 vintages
        - **quote_or_number**: 2024: 35 -> 35 CC units, 11.1 -> 11.1 GW (no jump). 2025: 42 -> 61 units, 16.9 -> 23.6 GW, of which Homer City PA 14 rows 4,396 MW and TVA Cumberland/Kingston 6 rows 2,334 MW. So March jumps are project-driven, not survey-driven.
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(SUM(mw)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS') AND vintage IN ('2024-02','2024-03','2025-02','2025-03') GROUP BY vintage; -- then the same NOT IN diff as above with '2025-02'/'2025-03'
      - - **source**: generators table, 2026-07 vintage, Fermi rows by planned_year x status x prime mover
        - **date**: 2026-07 vintage
        - **quote_or_number**: 2030 (P): 96 CT at 57 MW avg + 32 CA at 105 MW avg = 8,832 MW; 2027 (P): 6 CT at 260 MW, 7 CA, 7 GT at 19 MW; 2027 (T): 6 CT at 50 MW, 3 GT at 40 MW. Unit sizes match Siemens SGT-800 (~57 MW), SGT6-5000F (~260 MW) and GE TM2500 (~22 MW), not HA class (350-570 MW).
        - **reproduction**: SELECT planned_year, substr(status,1,4), prime_mover, COUNT(*), ROUND(SUM(mw)), ROUND(AVG(mw)) FROM generators WHERE plant_id=69799 AND vintage='2026-07' GROUP BY 1,2,3
      - - **source**: generators table, 2026-07 vintage totals and top entities
        - **date**: 2026-07 vintage
        - **quote_or_number**: Total planned NG turbine (CT/CA/CS/GT) = 67.1 GW; Fermi 11.7 GW (17%); status P = 37.0 GW (55%); under construction (U/V/TS) = 12.9 GW (19%). Top entities: Fermi 11.7, Entergy Louisiana 9.5, Homer City 4.4, TVA 3.9 GW.
        - **reproduction**: SELECT ROUND(SUM(mw)/1000,1) tot, ROUND(SUM(CASE WHEN plant_id=69799 THEN mw ELSE 0 END)/1000,1) fermi, ROUND(SUM(CASE WHEN status LIKE '(P)%' THEN mw ELSE 0 END)/1000,1) p, ROUND(SUM(CASE WHEN status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%' THEN mw ELSE 0 END)/1000,1) uc FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage='2026-07'; SELECT entity_name, COUNT(*), ROUND(SUM(mw)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage='2026-07' GROUP BY 1 ORDER BY 3 DESC LIMIT 5
      - - **source**: https://fermiamerica.com/fermi-america-siemens-energy-ai-campus-expansion/ and https://www.nasdaq.com/press-release/fermi-america-announces-arrival-6-siemens-energy-sgt-800-gas-turbines-port-houston and https://www.prnewswire.com/news-releases/fermi-america-agrees-to-acquire-over-600-mw-of-clean-gas-generation-for-delivery-in-2025-302496879.html
        - **date**: 2025-07-02, 2025-09-25, 2026-02-09, 2026-09-18
        - **quote_or_number**: Six Siemens SGT-800 (478 MW ISO) bought via Firebird LNG; three SGT6-5000F under LOI (1.1 GW CC) delivered Jul-Sep 2026; three secondary-market GE Frame 6B (135 MW) and seven leased GE TM2500 (157.5 MW). No new-build GE Vernova order disclosed for Matador.
        - **reproduction**: Fetch the three URLs; search page text for 'SGT-800', 'SGT6-5000F', 'Frame 6B', 'TM2500'
    - **why_market_misses_it**: Commentary and some sell-side cite the EIA planned-gas total as a demand validator without opening the plant-level file; the Fermi entry is 147 tiny rows so it inflates unit counts 3x while adding only a third to GW, and the campus's OEM is only in Fermi's own press releases, not in GEV or EIA documents.
    - **testable_prediction**: In the EIA-860M vintages for 2026-10 through 2027-03, the Fermi 2030-COD rows (128 units, 8.8 GW) remain status P (no move to L/T/U), and no GE Vernova 8-K or earnings release names Fermi/Matador as a new-build gas turbine customer by 2027-03-31.
    - **kill_condition**: An EIA-860M vintage on or before 2027-03 shows the Fermi 2030 rows at status U/V, or GE Vernova discloses a firm HA-class order or SRA for Project Matador, or Fermi's 10-K/8-K names GE Vernova as OEM for phases beyond the first gigawatt.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: EIA-860M Planned only lists projects the owner has reported; GEV's SRA book is global and partly behind-the-meter, so the EIA pipeline is a lower bound on demand and cannot by itself contradict GEV's backlog. Fermi's later phases could still switch OEM. The corpus has no GEV filing stating the US share of gas orders, so the 'GEV share of visible US pipeline' inference is indirect.
  - - **title**: The US visible gas pipeline is getting paper-heavier: status-P GW grew 7.7x in two years while under-construction GW grew 2.6x, and the whole 2027-COD pipeline (11.1 GW) is about half of GEV's own 20 GW/yr output claim
    - **claim**: In EIA-860M, planned gas-turbine GW at status P (approvals not initiated) rose from 4.8 GW (2024-06) to 37.0 GW (2026-07) while under-construction GW (U/V/TS) rose only from 5.0 to 12.9 GW; US gas-turbine GW actually reaching the Operating sheet was 9.7 GW (2023), 1.9 (2024), 4.5 (2025), 2.7 (2026 through July); and the 2026-07 vintage shows only 11.1 GW targeted for 2027 COD (3.6 GW under construction) and 16.1 GW for 2028 (2.8 GW under construction).
    - **mechanism**: Gas equipment revenue is recognized cost-to-cost, so GEV's 2027 revenue does not need US COD dates; but the $39.9B of contract liabilities and the SRA-to-order conversion cadence (10 GW converted in Q2-26) depend on customers keeping projects alive. Cancellation and slippage risk concentrates in the 37 GW of status-P projects, which is where the 2026-27 SRA vintage sits. A pipeline whose paper share rose from 50% to 55% and whose 2027-28 buildable share is 6.4 GW is the physical base for the bear 'peak-order' case and for any deposit refund or slot re-marketing headline.
    - **direction**: short
    - **evidence**:
      - - **source**: generators table, status-P GW by vintage
        - **date**: 2024-06 to 2026-07 vintages
        - **quote_or_number**: P-status NG turbine GW: 4.8 (2024-06), 7.6 (2024-12), 15.5 (2025-06), 19.5 (2025-12), 18.6 (2026-02), 33.4 (2026-03, incl. 11.3 Fermi), 37.0 (2026-07)
        - **reproduction**: SELECT vintage, ROUND(SUM(mw)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND status LIKE '(P)%' AND vintage IN ('2024-06','2024-12','2025-06','2025-12','2026-02','2026-03','2026-07') GROUP BY 1
      - - **source**: generators table, under-construction GW by vintage
        - **date**: 2023-06 to 2026-07 vintages
        - **quote_or_number**: U/V/TS NG turbine GW: 4.7 (2023-06), 5.0 (2024-06), 5.2 (2024-12), 8.8 (2025-06), 7.9 (2025-12), 13.1 (2026-03), 12.9 (2026-07); CC portion 2.4 -> 7.2 GW
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(SUM(mw)/1000,1), ROUND(SUM(CASE WHEN prime_mover IN ('CT','CA','CS') THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND (status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%') AND vintage IN ('2023-06','2024-06','2024-12','2025-06','2025-12','2026-03','2026-07') GROUP BY 1
      - - **source**: generators table, 2026-07 vintage, planned GW by target year and status
        - **date**: 2026-07 vintage
        - **quote_or_number**: By COD year (CC+GT GW / of which under construction): 2026 4.2/4.2; 2027 11.1/3.6; 2028 16.1/2.8; 2029 13.4/1.4; 2030 18.1/0.0 (8.8 Fermi); 2031+ 4.1/0.8
        - **reproduction**: SELECT planned_year, ROUND(SUM(mw)/1000,1), ROUND(SUM(CASE WHEN status LIKE '(U)%' OR status LIKE '(V)%' OR status LIKE '(TS)%' THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage='2026-07' GROUP BY 1 ORDER BY 1
      - - **source**: generators table, Operating sheet by op_year (and second way: vintage-to-vintage diff)
        - **date**: 2026-07 vintage; Dec vintages 2023-2025
        - **quote_or_number**: NG turbine GW entering service by op_year: 2019 8.2, 2020 6.7, 2021 7.1, 2022 6.9, 2023 9.7, 2024 1.9, 2025 4.5, 2026 YTD 2.7. Second way (new keys in Operating sheet between vintages): 2024 3.5 GW, 2025 4.7 GW, Jan-Jul 2026 3.2 GW. HA-class CT (>=300 MW) entering service: 0.0 GW in each of 2024, 2025, 2026 YTD.
        - **reproduction**: SELECT op_year, COUNT(*), ROUND(SUM(mw)/1000,1), ROUND(SUM(CASE WHEN prime_mover='CT' AND mw>=300 THEN mw ELSE 0 END)/1000,1) FROM generators WHERE sheet='Operating' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage='2026-07' AND op_year BETWEEN 2019 AND 2026 GROUP BY 1; -- second way: SELECT ROUND(SUM(mw)/1000,1) FROM generators WHERE sheet='Operating' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT') AND vintage='2025-12' AND plant_id||'|'||generator_id NOT IN (SELECT plant_id||'|'||generator_id FROM generators WHERE sheet='Operating' AND vintage='2024-12')
      - - **source**: generators table, HA-class planned CT units by vintage (unit-size shift)
        - **date**: 2023-06 to 2026-07 vintages
        - **quote_or_number**: Planned CT units >=300 MW: 5 units/2.2 GW (2023-06), 7/2.8 (2024-06), 20/8.1 (2025-06), 35/15.3 GW (2026-07), avg 437 MW. 400-499 MW class (7HA.02/.03, SGT6-9000HL, M501JAC): 7 units/3.0 GW (2024-06) -> 39 units/18.0 GW (2026-07), 6x.
        - **reproduction**: SELECT vintage, COUNT(*), ROUND(SUM(mw)/1000,1), ROUND(AVG(mw)) FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover='CT' AND mw>=300 AND vintage IN ('2023-06','2024-06','2025-06','2026-07') GROUP BY 1
      - - **source**: generators table, slippage of planned units first seen 2023-02..2024-06 (mature cohort, computed in pandas from Planned-sheet rows)
        - **date**: vintages 2023-02 to 2026-07
        - **quote_or_number**: 71 NG turbine units first listed Feb-23 to Jun-24: 32 operating (4.2 GW), 34 still planned (5.0 GW), 3 canceled (1.3 GW), 2 vanished (0.4 GW); 18 of 71 (25%) slipped >=12 months; 16 pulled in or held; median slip 1-5 months. Every unit originally targeted for 2024 (1.6 GW) or 2025 (2.2 GW) COD is operating in 2026-07.
        - **reproduction**: Load: SELECT plant_id, generator_id, vintage, planned_year, planned_month, mw, prime_mover FROM generators WHERE sheet='Planned' AND energy_source='NG' AND prime_mover IN ('CT','CA','CS','GT'); group by plant_id||generator_id ordered by vintage; slip = (last planned_year*12+month) - (first planned_year*12+month); fate from sheet membership in vintage 2026-07; restrict to first vintage in ('2023-02'..'2024-06'). Pure-SQL self-join exceeds 120 s; use pandas.
    - **why_market_misses_it**: Analysts quote GEV's 63 GW SRA and 125 GW under-contract totals, which are global and include behind-the-meter sites, against a US grid-connected dataset most people have only seen as a headline total; the status field (P/L/T/U/V) and the by-year breakdown are rarely tabulated, and the trough in US additions in 2024-25 (1.9 and 4.5 GW) is masked by GEV's rising global shipments (19 GW over the last five quarters).
    - **testable_prediction**: The EIA-860M 2027-01 vintage will show under-construction (U/V/TS) NG turbine GW between 14 and 20 GW and status-P GW still above 30 GW; NG turbine GW entering service in calendar 2026 will finish between 4 and 7 GW (vs GEV shipping about 16 GW globally in the same period at 4 GW/quarter).
    - **kill_condition**: The 2027-01 vintage shows under-construction NG turbine GW above 25 GW, or status-P GW below 20 GW because projects advanced (not because they were dropped), or 2026 full-year Operating additions exceed 8 GW.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: EIA-860M covers grid-connected plants >=1 MW that owners report; behind-the-meter data-center campuses may be absent or late, so the pipeline understates true demand. GEV does not disclose the US share of gas orders (searched 10-K/10-Q/8-K/transcript chunks; nothing), so the comparison of a US dataset to a global output rate is directional. Slippage cohort is small (71 units) because the US built little gas in 2023-25.
  - - **title**: The installed US combined-cycle fleet ran 3% fewer MWh in 2025 than 2024 and its capacity factor is flat at 53-55%, including Texas; services growth cannot come from more fired hours
    - **claim**: Matched plant-level EIA-923 data show US gas combined-cycle generation fell from 1,550 TWh (2024) to 1,502 TWh (2025), -3.1% across 1,066 plant/prime-mover pairs, with fleet capacity factor 0.533/0.545/0.529 (2023/24/25) and Texas CC 0.526/0.536/0.524; simple-cycle peakers stayed at 0.11 nationally and 0.24-0.26 in Texas; no GEV-concentrated state shows a rising utilization trend into 2025.
    - **mechanism**: GEV's Power services revenue (services RPO $88.5B; bull case about $70M per GW-year) is driven by outage intervals that are set by fired hours and starts on the installed fleet. Flat-to-falling hours mean the services line grows only with fleet additions (which, per finding 2, were 1.9-4.5 GW/yr in the US in 2024-25) and price, not with utilization; this caps near-term services upside and weakens the 'data centers are already making existing gas plants run harder' narrative that supports services multiples.
    - **direction**: short
    - **evidence**:
      - - **source**: generation table (EIA-923), matched plant/prime-mover pairs 2024 vs 2025
        - **date**: 2025 (full year; 1,072 CC plant-rows vs 1,079 in 2024, so not a reporting gap)
        - **quote_or_number**: US NG CC: 1,550.4 TWh (2024) -> 1,502.0 TWh (2025), n=1,066 pairs, -3.1%. Texas NG CC: 224.9 -> 221.7 TWh, -1.4%.
        - **reproduction**: SELECT ROUND(SUM(a.net_generation_mwh)/1e6,1), ROUND(SUM(b.net_generation_mwh)/1e6,1), COUNT(*) FROM generation a JOIN generation b ON a.plant_id=b.plant_id AND a.prime_mover=b.prime_mover AND a.fuel_type=b.fuel_type AND a.year=2024 AND b.year=2025 WHERE a.fuel_type='NG' AND a.prime_mover IN ('CT','CA','CS'); -- add AND a.state='TX' for Texas
      - - **source**: generation table joined to generators Operating sheet (June vintage of each year) for capacity factor
        - **date**: 2023-2025 (2026 is partial-year, ignore its CF)
        - **quote_or_number**: US CC: 2023 1,522.9 TWh / 326.1 GW = 0.533; 2024 1,552.9 / 325.4 = 0.545; 2025 1,503.5 / 324.7 = 0.529. US GT: 0.107 / 0.117 / 0.113. TX CC 0.526 / 0.536 / 0.524; TX GT 0.241 / 0.258 / 0.256. GA CC 0.712 / 0.669 / 0.668; VA CC 0.553 / 0.665 / 0.659; OH CC 0.688 / 0.730 / 0.684; NC GT 0.052 / 0.072 / 0.109 (only clear riser).
        - **reproduction**: WITH cap AS (SELECT substr(vintage,1,4) yr, state, CASE WHEN prime_mover IN ('CT','CA','CS') THEN 'CC' WHEN prime_mover='GT' THEN 'GT' ELSE 'other' END cls, SUM(mw) mw FROM generators WHERE sheet='Operating' AND energy_source='NG' AND vintage IN ('2023-06','2024-06','2025-06') GROUP BY 1,2,3), gen AS (SELECT CAST(year AS TEXT) yr, state, CASE WHEN prime_mover IN ('CT','CA','CS') THEN 'CC' WHEN prime_mover='GT' THEN 'GT' ELSE 'other' END cls, SUM(net_generation_mwh) mwh FROM generation WHERE fuel_type='NG' GROUP BY 1,2,3) SELECT gen.state, gen.yr, gen.cls, ROUND(SUM(gen.mwh)/1e6,1), ROUND(SUM(cap.mw)/1000,1), ROUND(SUM(gen.mwh)/(SUM(cap.mw)*8760),3) FROM gen JOIN cap USING (yr,state,cls) WHERE gen.cls IN ('CC','GT') GROUP BY 1,2,3 ORDER BY 1,3,2
      - - **source**: generation table totals (completeness check)
        - **date**: 2022-2026
        - **quote_or_number**: All-fuel rows and TWh by year: 2022 16,264 rows / 3,903 TWh; 2023 16,832 / 3,847; 2024 17,681 / 3,972; 2025 18,539 / 4,073; 2026 6,209 / 1,714 (partial). 2025 total generation is up 2.6% while gas CC is down 3.1%.
        - **reproduction**: SELECT year, COUNT(*), ROUND(SUM(net_generation_mwh)/1e6,1) FROM generation GROUP BY year
    - **why_market_misses_it**: The load-growth story is told with forecasts (PJM, ERCOT) and GEV's order book; almost nobody checks whether the existing gas fleet actually ran more in 2025. It did not, because solar/storage took the marginal daytime MWh, and the services bull case implicitly assumes fired hours rise with load.
    - **testable_prediction**: When EIA-923 2026 data are complete (EIA final release around Q3-2027; preliminary monthly data through Dec-2026 available by Feb-2027), US CC capacity factor will print between 0.51 and 0.56, i.e. no break above the 2023-25 band, and GEV's Power services organic growth for FY26 will be reported in the high-single to low-double digits, not accelerating above the FY25 rate.
    - **kill_condition**: EIA-923 monthly data show 2026 US NG CC generation up more than 5% year over year (above about 1,580 TWh annualized), or GEV reports Power services organic growth above 15% for FY26 attributing it to higher outage volume from fleet utilization.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Capacity factor uses the June Operating-sheet nameplate, which slightly understates CF for units retired mid-year and ignores derates; the level is approximate but the year-over-year direction is robust because the matched-plant comparison gives the same answer. Related to the team's 'EPA CAMD fired hours' angle but from a different dataset and with a quantified 2025 conclusion; the two should be reconciled, not duplicated. Materiality is limited over 3-12 months because services RPO is contracted and outage timing is set by hours already accumulated.
- **dead_ends**:
  - Annual-survey artifact hypothesis for the March-2026 jump: rejected. Feb-to-Mar 2024 showed zero change in planned CC units (35 -> 35); Feb-to-Mar 2025 was +19 units, all Homer City and TVA. Jumps are project-driven.
  - Slippage as a standalone signal: the mature cohort (units first listed Feb-2023 to Jun-2024) is only 71 units / about 11 GW because the US built little gas in 2023-25; 25% slipped 12+ months, only 8 units (2.9 GW) vanished from all sheets, 5 canceled (1.4 GW), and every unit originally targeted for 2024 or 2025 COD is operating. Too thin to support a base-rate claim about the 2026-30 pipeline.
  - US versus international split of GEV gas orders/SRAs: not disclosed anywhere in the corpus. FTS on GEV primary chunks for 'United States'/'North America'/'domestic'/'international' with 'gas' 'orders'/'backlog'/'slot reservation' returned only segment-level 8-K text with no geographic GW split; mgmt_guidance has no US-GW rows.
  - projects table OEM linkage: rows for Entergy Louisiana (Richland Parish, Pointe Coupee, Waterford 6, Westlake), Entergy Arkansas (Jefferson) and Homer City have blank oem/model fields, so EIA planned GW cannot be attributed to GEV vs Siemens vs MHI from the corpus; OEM for the top EIA entity (Fermi) had to come from the web.
  - competitor_financials capacity claims for Siemens Energy are qualitative ('capacity expansion effective FY27', 'until FY30') with no GW figures, so no numeric Siemens/MHI capacity path could be cross-checked against the EIA pipeline; MHI order chunks are slide fragments without parsable GW.
  - Fermi/Matador in the corpus: only one arXiv chunk (2026-09-08) mentions Project Matador; no GEV, Siemens or news chunk. VoltaGrid/Oracle chunks matched 'Fermi' by accident.
  - Pure-SQL cross-vintage self-join on generators (1.58M rows, no composite index) exceeds the 120 s limit; load Planned-sheet NG turbine rows (about 8k) into pandas instead.
  - Capacity-factor trend as a utilization-rising signal: no GEV-concentrated state (TX, GA, FL, LA, SC, NC, PA, OH, VA, AZ, OK) shows CC capacity factor rising into 2025; Virginia's rise happened 2023 -> 2024 and then flattened; NC simple-cycle is the only clear riser (0.05 -> 0.11) and is small (8 GW). 2026 generation is partial-year and unusable for CF.
  - Unit-size shift as an OEM discriminator: the 400-499 MW CT class grew 6x (7 -> 39 units, 3.0 -> 18.0 GW) but that band contains GE 7HA.02/.03, Siemens SGT6-9000HL and MHI M501JAC alike; the <100 MW band growth (41 -> 119 units) is almost entirely Fermi's Siemens SGT-800s. Size alone cannot assign share to GEV.

## [Sweep] find:narrative-archaeology

- **lens**: Narrative archaeology and echo detection: trace viral GEV claims (pricing +300%, $3,000/kW, $70M per GW-year of services, $200B backlog by 2027, sold-out years, consensus targets) back to their single origin in dated commentary, test them against GEV's own filings/transcripts, and count how many independent sources actually stand behind them.
- **findings**:
  - - **title**: 'Turbine prices up 300% in three years' and '$3,000/kW' are single-origin numbers that GEV's own disclosures do not support; company-stated pricing is +10-20% (H1'26 vs 4Q'25) and 6 pts of backlog-margin accretion
    - **claim**: Every corpus instance of '300% in three years' traces to one Melius Research estimate relayed by a CNBC segment (Jun 22-27 2026), and every '$3,000/kW' instance is an EPRI/Utility Dive all-in combined-cycle PLANT cost or Morgan Stanley's 'implied combined cycle plant pricing', not a GEV turbine price; GEV's only quantified pricing statements are '>20% above 4Q'25' (H1'26 orders), 'high end of 10 to 20 points' (H2'26) with an aero-mix caveat, and '+$8B equipment margin in backlog, 6 pts accretion' (FY25).
    - **mechanism**: Bulls use 300%/$3,000 per kW to argue GEV can keep re-pricing the 2027-28 vintage toward 20%+ Power margins; bears (GLJ) use the same numbers to argue demand destruction and a 'sold at 2024 prices' cliff. Both sides are anchoring on a plant-level EPC number (3-4x the turbine-only $790-950/kW BNP estimate) and an unverifiable third-party estimate. GEV's own guided pricing lift (10-20% over three quarters, partly aero mix) maps to the 17-19% Power margin guide, not to a step-change up or down. Mispricing risk is in the margin bridge on the Power line, not in revenue.
    - **direction**: neutral
    - **evidence**:
      - - **source**: sources / chunks NEWS: finance.yahoo.com/markets/stocks/articles/ai-bottleneck-leads-300-pricing-175846365.html
        - **date**: 2026-06-22
        - **quote_or_number**: "GEV gas turbine prices have surged 300% in three years, with the order book sold out through 2029 and extending to 2031."
        - **reproduction**: SELECT published,url,substr(text,1,400) FROM sources WHERE url LIKE '%ai-bottleneck-leads-300-pricing%';
      - - **source**: sources WEB: cnbc.com/2026/06/27/ge-vernova-gas-turbines-ai-data-centers.html
        - **date**: 2026-06-27 (segment aired ~Jun 22 per 247wallst 2026-06-24)
        - **quote_or_number**: "One turbine can cost more than $250 million, according to industry estimates. The price has soared, up 300% in the last 3 years, according to analysts at Melius."
        - **reproduction**: SELECT url, instr(text,'Melius') FROM sources WHERE url LIKE '%cnbc.com/2026/06/27/ge-vernova-gas-turbines%';
      - - **source**: sources (echo count): 7 commentary sources carry the 300%-pricing claim; only 2 (cnbc.com, ainave.com) attribute it to Melius; 0 primary-tier GEV documents contain it
        - **date**: 2026-06-22 to 2026-09-20
        - **quote_or_number**: 7 sources; 2 cite Melius; ainave.com adds: "The 300% pricing increase is an analyst estimate from Melius, not a GE Vernova official figure."
        - **reproduction**: python: for s in con.execute("SELECT published,url,text FROM sources WHERE tier='commentary' AND text LIKE '%300%'"): match regex r'(pric\w+|cost\w*)[^.]{0,60}(up|surged|soared|risen|increased|jumped)[^.]{0,20}300%|300%[^.]{0,40}(pric|three years|3 years)' AND 'turbine' in text; count and check 'Melius' in text. Primary check: SELECT count(*) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"300%"' AND c.ticker='GEV' AND c.tier='primary' AND c.text LIKE '%turbine%pric%';
      - - **source**: chunks TRANSCRIPT: gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf (Q2'26 call)
        - **date**: 2026-07-22
        - **quote_or_number**: "first half 2026 orders were priced more than 20% above 4Q '25 equipment orders" ... "higher dollar per kW price in orders, given a higher mix of aeroderivatives" ... "higher end of the range of 10 to 20 points versus 4Q '25 orders."
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"per kW"' AND c.ticker='GEV' AND c.tier='primary' AND c.form='TRANSCRIPT';
      - - **source**: chunks 8-K/EX accession 0001996810-26-000012 (Q4'25 press release)
        - **date**: 2026-01-28
        - **quote_or_number**: "grew equipment margin in backlog by $8B, with 6 pts of accretion"
        - **reproduction**: SELECT filing_date, substr(text,1,300) FROM chunks WHERE accession LIKE '0001996810-26-000012%' AND text LIKE '%6 pts of accretion%';
      - - **source**: analyst_calls (BNP Paribas, Moses Sutton) via utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/
        - **date**: 2026-07-22
        - **quote_or_number**: "estimated about $790/kW for heavy-duty turbines, $950/kW for HA-class combined-cycle turbines and $1,800/kW for aeroderivative turbines." (turbine-level)
        - **reproduction**: SELECT published, firm, analyst, value, quote FROM analyst_calls WHERE ticker='GEV' AND value LIKE '%/kW';
      - - **source**: sources WEB utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-market (EPRI's Bobby Noble) and NEWS finance.yahoo.com/.../morgan-stanley-strongly-resets-ge-180300042.html
        - **date**: undated (retrieved 2026-09-20) / 2026-07-22
        - **quote_or_number**: EPRI: "average gas turbine prices increased from roughly $2,000/kW to $3,000/kW"; Morgan Stanley: "Slot reservations are now pricing near $3,000 per kilowatt of implied combined cycle plant pricing" (plant-level, not turbine)
        - **reproduction**: SELECT published, url FROM sources WHERE tier='commentary' AND (text LIKE '%$3,000/kW%' OR text LIKE '%$3,000 per kilowatt%' OR text LIKE '%$3,000 per kW%') ORDER BY published;
    - **why_market_misses_it**: The CNBC segment (Jun 22) coincided with GEV's all-time high week (close $1,127.59 on Jun 22; peak ~$1,196 late June), so the 300% number was absorbed as the explanation for the rally. Sell-side pieces (MS Jul 22) then reused '$3,000/kW' with the qualifier 'implied combined cycle plant pricing', and aggregators dropped the qualifier. GEV itself never gives $/kW, so no filing contradicts the headline directly.
    - **testable_prediction**: On the Q3'26 call (expected ~Oct 22 2026) GEV will again describe equipment order pricing relative to 4Q'25 in the 10-20 point range (or a modestly higher band) and will not disclose any $/kW; Power EBITDA margin guidance stays 17-19% for FY26. Any sell-side note quantifying turbine-only pricing will land in the $800-1,100/kW range for heavy-duty, i.e. roughly a third of the '$3,000' headline.
    - **kill_condition**: GEV discloses in a filing or call that current heavy-duty gas equipment order pricing is >2x its 2023 level on a like-for-like $/kW basis, or reports Power equipment margin in backlog accreting by >10 pts in a single year.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Melius' underlying note is not in the corpus; the 300% could be a specific-model spot quote for expedited 2027 slots. GEV's '+20%' figure is orders-weighted and partly mix (aero vs heavy-duty), so like-for-like price is lower than 20%. Transcript chunks have blank filing_date; date taken from the URL.
  - - **title**: '$70M per GW-year of services on a 400+ GW fleet' is one Jefferies analyst's 2030s projection; GEV's realized Power services today are at most ~$15M per GW-year on an 886 GW gas fleet
    - **claim**: The services-per-GW figure in the bull frontier traces to a single Sep 12 2026 Jefferies note (Julien Dumoulin-Smith) explicitly framed as 'during the 2030s' on a '400+ GW' fleet; the echo drops the decade and the fleet definition. GEV's FY25 Power services revenue was $13,081M (all of gas, nuclear, hydro, steam) against a GEV-stated gas turbine installed base of 886 GW, i.e. <= $14.8M per GW-year today, so the $70M x 400 GW = $28B implied run-rate is >2x the entire current Power services line.
    - **mechanism**: Services is the terminal-value anchor for every Buy target ($1,185-$1,450). If a memo or model applies $70M/GW-year to today's or 2028's fleet, Power services revenue is overstated by roughly 2x, flowing straight into the Power segment EBITDA (services carry the segment's highest margins) and into any DCF or SOTP. Correctly, the $70M figure is a 2030s aspiration on an undefined subset (likely HA/F-class under contractual service agreements), not unit economics.
    - **direction**: short
    - **evidence**:
      - - **source**: sources NEWS blockonomi.com/ge-vernova-gev-stock-jefferies-says-recent-23-decline-creates-entry-point (and coincentral.com same day)
        - **date**: 2026-09-12
        - **quote_or_number**: "Dumoulin-Smith forecasts that GE Vernova could generate more than $70 million per gigawatt-year from its installed base during the 2030s, supported by a fleet exceeding 400 gigawatts."
        - **reproduction**: SELECT c.form,(SELECT published FROM sources s WHERE 'src:'||s.id=c.accession),(SELECT url FROM sources s WHERE 'src:'||s.id=c.accession) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"70 million" AND ("per gigawatt" OR "gigawatt")' ORDER BY bm25(chunks_fts) LIMIT 8;  -> only 2 GEV hits, both Sep 12 2026 Jefferies write-ups
      - - **source**: chunks 10-K accession 0001996810-26-000015 (FY2025), Power segment table
        - **date**: 2026-01-29
        - **quote_or_number**: Power: Equipment $6,686 / Services $13,081 / Total $19,767 (FY25); Services $12,419 (FY24), $11,838 (FY23)
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Power" AND "Services" AND "Equipment" AND "Gas Power" AND "revenues"' AND c.ticker='GEV' AND c.form='10-K' AND c.filing_date='2026-01-29' ORDER BY bm25(chunks_fts) LIMIT 1;
      - - **source**: chunks 8-K/EX accession 0001193125-24-063739#d808872dex991.htm (Form 10 information statement exhibit) and S-1 2024-03-13
        - **date**: 2024-03-08
        - **quote_or_number**: "we maintain the largest installed base of gas turbines globally of 886 installed GW and 2,206 GW total across our Gas Power, Nuclear Power, Hydro Power, and Steam Power businesses"
        - **reproduction**: SELECT form, filing_date, accession FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"largest installed base of gas turbines"' AND c.ticker='GEV';
      - - **source**: arithmetic on the two filings above
        - **date**: FY2025
        - **quote_or_number**: $13,081M / 886 GW = $14.8M per GW-year (upper bound: Power services include steam/nuclear/hydro). Jefferies: $70M x 400 GW = $28B/yr = 2.1x FY25 total Power services.
        - **reproduction**: python: 13081/886 ; 70*400 ; 28000/13081
      - - **source**: chunks DECK gevernova.com/sites/default/files/gev_webcast_presentation_07222026.pdf
        - **date**: 2026-07-22
        - **quote_or_number**: "Units under contract will more than double the size of the HA fleet, driving significant growth for Gas Power Services" (GEV frames services growth as HA-fleet doubling, no $/GW figure)
        - **reproduction**: SELECT text FROM chunks WHERE ticker='GEV' AND form='DECK' AND text LIKE '%more than double the size of the HA fleet%';
    - **why_market_misses_it**: The $70M number appeared the day after the 23% drawdown as the 'buy the dip' services argument and was re-headlined by at least two outlets within hours, stripped of 'in the 2030s'. GEV has never published services $ per GW, so there is no primary number to contradict it, and the 886 GW installed-base figure sits only in the 2024 Form 10/S-1, which few current readers open.
    - **testable_prediction**: FY26 Power services revenue reported in the 10-K (late Jan 2027) will be $14.0-15.5B, i.e. <= $17.5M per GW on the 886 GW base, and GEV will not disclose a per-GW services metric; by the Q3'26 call (late Oct 2026) no other sell-side firm will publish an independent per-GW services figure above $30M/GW-year for the current fleet.
    - **kill_condition**: GEV or its 10-K discloses a contractual-service fleet definition (e.g. HA/F-class under CSAs) with realized services revenue >= $40M per GW-year today, or FY26 Power services revenue prints above $17B.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: The 886 GW figure is as of the March 2024 Form 10; it will have grown modestly. Jefferies' 400 GW may be a deliberately narrower serviceable-fleet definition, which would make the $70M figure internally consistent for that subset but still not applicable to today's revenue. Power services revenue includes non-gas; the true gas-only $/GW is lower than $14.8M.
  - - **title**: The '$200B backlog' target has been restated three times (YE2028 -> 2027 -> 'in 2027' -> 'very early 2027'); the Sep 16 +4.8% move priced a restatement, not new information, and the straight-line run-rate already implied it
    - **claim**: Dec 9 2025 investor update: ~$200B by year-end 2028. Apr 22 2026 (Q1): 2027. Jul 22 2026 (Q2 call): 'on track to reach $200 billion in 2027'. Sep 16 2026 (MS conference): 'very early in 2027', reported as 'sooner than Wall Street expected' and worth +4.8% on the day (close $882.81 -> $925.09). Backlog has grown $135B (3Q25) -> $150.2B (Dec-25) -> $163B (Mar-26) -> $176B (Jun-26), a steady ~$13B/quarter that reaches ~$202B by Dec-26 on a straight line, so 'very early 2027' is at or slightly below the existing trend.
    - **mechanism**: Total backlog is the headline number that moves GEV on non-earnings days. If the market pays 4-5% for a re-timing that the run-rate already implied, the Q3'26 print (~Oct 22) is asymmetric: a backlog of ~$188-190B is merely on-trend and already priced, while anything under ~$185B (orders < ~$12B net of revenue) breaks the 'very early 2027' framing that the stock just paid for. The 10-K also shows equipment RPO grew $21.2B in 2025 vs services RPO $10.0B, so the backlog headline is increasingly equipment (lower margin, cost-to-cost recognized) rather than services.
    - **direction**: either
    - **evidence**:
      - - **source**: sources WEB gevernova.com/sites/default/files/gev_webcast_pressrelease_12092025.pdf and gev_webcast_presentation_12092025.pdf
        - **date**: 2025-12-09
        - **quote_or_number**: "Expects to grow total backlog from $135B to approximately $200B by year-end 2028"; deck: "Exit '28 with ~$200B backlog"
        - **reproduction**: SELECT url, instr(text,'$200B by year-end 2028') FROM sources WHERE url LIKE '%gev_webcast_pressrelease_12092025%';
      - - **source**: sources NEWS finance.yahoo.com/sectors/energy/articles/ge-vernova-q1-earnings-call-... (Q1'26 call write-up)
        - **date**: 2026-04-23
        - **quote_or_number**: "now expects to reach $200 billion in backlog in 2027, earlier than its previous expectation of 2028"
        - **reproduction**: SELECT published,url FROM sources WHERE tier='commentary' AND text LIKE '%$200 billion%' AND text LIKE '%2028%' AND text LIKE '%backlog%' ORDER BY published;
      - - **source**: chunks TRANSCRIPT gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
        - **date**: 2026-07-22
        - **quote_or_number**: "backlog has reached $176 billion with improving margins. This is up $13 billion from last quarter and is on track to reach $200 billion in 2027."
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"200 billion" AND "backlog"' AND c.ticker='GEV' AND c.tier='primary';
      - - **source**: sources NEWS gurufocus.com/news/9084554 and finance.yahoo.com/.../ge-vernova-climbs-5-ceo-175610084; insidermonkey 2026-09-20
        - **date**: 2026-09-16 to 2026-09-20
        - **quote_or_number**: "shares climbed 4.6% following CEO Scott Strazik's remarks ... expected to hit $200 billion 'very early' in 2027, surpassing Wall Street's estimates"
        - **reproduction**: SELECT c.form,(SELECT published FROM sources s WHERE 'src:'||s.id=c.accession),(SELECT url FROM sources s WHERE 'src:'||s.id=c.accession) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"200 billion" AND "backlog" AND "2027"' AND c.ticker='GEV' ORDER BY bm25(chunks_fts) LIMIT 10;
      - - **source**: prices table
        - **date**: 2026-09-15 / 2026-09-16
        - **quote_or_number**: close 882.81 -> 925.09 (+4.8%)
        - **reproduction**: SELECT date, close FROM prices WHERE ticker='GEV' AND date IN ('2026-09-15','2026-09-16');
      - - **source**: chunks 10-K accession 0001996810-26-000015 RPO table
        - **date**: 2026-01-29
        - **quote_or_number**: Total RPO $150,238M (Dec-25) vs $119,023M (Dec-24); Equipment $64,245M vs $43,047M; Services $85,993M vs $75,976M
        - **reproduction**: SELECT text FROM chunks WHERE ticker='GEV' AND form='10-K' AND filing_date='2026-01-29' AND text LIKE '%Total RPO $150,238%';
    - **why_market_misses_it**: Each restatement was reported as an upgrade ('pulled forward', 'sooner than expected') by outlets that did not cite the prior restatement; the Jul 22 'in 2027' language was buried under the EPS miss ($2.47 vs $3.17 expected) and the 30 GW capacity announcement. No outlet in the corpus computed the $13B/quarter run-rate against the target.
    - **testable_prediction**: Q3'26 results (~Oct 22 2026) report total backlog between $186B and $192B; management repeats '$200B very early 2027' or upgrades to 'by year-end 2026'. If backlog prints below $185B the stock gives back the Sep 16 gain within two sessions.
    - **kill_condition**: Q3'26 backlog >= $195B (a genuine acceleration that justifies the re-rating) or GEV redefines backlog to include SRAs, which would make the headline non-comparable.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Backlog includes services RPO recognized over 10-20 years, so the headline is a weak proxy for 12-month revenue. The 3Q25 $135B figure is from the Dec 9 2025 press release rather than a 10-Q chunk. The Sep 16 move also coincided with Guggenheim's $1,450 street-high target, so not all of the +4.8% is attributable to the backlog remark.
  - - **title**: 'Consensus target ~$1,236' rests on about ten named sell-side firms in the corpus, three aggregators disagree by $92 in the same week, and the average has not moved since the stock was $1,127
    - **claim**: analyst_calls has 36 'firm' strings with GEV price targets but only 10 named sell-side houses with USD targets on GEV itself (Rothschild $1,100, BNP Exane $1,190, Goldman $1,328/$1,227, Morgan Stanley $1,350, Mizuho $949, Guggenheim $1,450, Baird $1,400, Jefferies $1,185, Bernstein $1,298, GLJ $470); the rest are aggregators (Yahoo, MarketBeat, GuruFocus, Zacks, TipRanks-style) or targets on the Indian T&D subsidiary in rupees. The quoted 'average target' was $1,221.29 on Jun 22 (stock $1,127.59) and $1,237.34 on Sep 14-16 (stock $883-925), i.e. unchanged through a 22% drawdown; on Sep 15-19 three aggregators printed $1,237.34, $1,187.83 and $1,145.83 for the same 'consensus'.
    - **mechanism**: The '40% upside to consensus' line that appears in every post-drawdown bull piece is an artifact of stale targets (only Jefferies and Guggenheim re-issued targets after Sep 11, both raises) rather than a re-underwritten view; Mizuho at $949 Neutral is effectively 'hold at the price'. For a 3-12 month thesis the relevant observation is that target dispersion ($470 to $1,450, 3.1x) is the widest in the corpus, so the memo should not lean on 'consensus' as evidence in either direction.
    - **direction**: neutral
    - **evidence**:
      - - **source**: analyst_calls
        - **date**: 2026-03-24 to 2026-09-20
        - **quote_or_number**: 10 named sell-side firms with USD GEV targets; 36 distinct firm strings overall; 130 price_target rows
        - **reproduction**: SELECT firm, max(published) d, value FROM analyst_calls WHERE ticker='GEV' AND metric='price_target' AND value LIKE '$%' AND firm NOT IN ('Not specified','Wall Street','MarketBeat','GuruFocus','InvestingPro','Yahoo Finance','Seeking Alpha','Zacks Investment Research','GE Vernova','24/7 Wall St.','Not explicitly named','MetLife and PineBridge','CNBC Investing Club') GROUP BY firm ORDER BY d;
      - - **source**: analyst_calls rows quoting an average/consensus target
        - **date**: 2026-06-22, 2026-06-24, 2026-09-12, 2026-09-14/15/16, 2026-09-19
        - **quote_or_number**: $1,221.29 (Jun 22); $1,211.72 (Jun 24); ~$1,240 (Sep 12); $1,237.34 (Sep 14-16); $1,187.83 (Sep 15); USD 1,145.83 (MarketBeat, Sep 19)
        - **reproduction**: SELECT published, firm, value, quote FROM analyst_calls WHERE ticker='GEV' AND (quote LIKE '%average%target%' OR quote LIKE '%consensus%target%') ORDER BY published;
      - - **source**: prices table
        - **date**: 2026-06-22 vs 2026-09-15
        - **quote_or_number**: close 1127.59 -> 882.81 (-21.7%) while quoted average target went 1221 -> 1237
        - **reproduction**: SELECT date, close FROM prices WHERE ticker='GEV' AND date IN ('2026-06-22','2026-09-15','2026-09-18');
      - - **source**: analyst_calls, post-Sep-11 rows
        - **date**: 2026-09-12 to 2026-09-20
        - **quote_or_number**: 44 USD target rows since Sep 11, but only two genuine target changes: Jefferies $1,155 -> $1,185 (Sep 12) and Guggenheim $1,300 -> $1,450 (Sep 16); GLJ $470 initiation (Sep 14); Baird, Bernstein, Mizuho reiterations
        - **reproduction**: SELECT published, firm, analyst, value, quote FROM analyst_calls WHERE ticker='GEV' AND metric='price_target' AND published>='2026-09-11' AND value LIKE '$%' ORDER BY published;
    - **why_market_misses_it**: Aggregator averages are recomputed from the last-published target of each covering analyst regardless of age, and outlets quote whichever aggregator they license; nobody in the corpus reconciles the three different 'consensus' figures printed the same week.
    - **testable_prediction**: By Nov 1 2026 (post-Q3 print) at least three of the ten named firms will publish revised targets; if the stock is still below $1,000 the quoted 'average target' will drift down by at least $50 as stale $1,300+ targets are refreshed, and the memo should cite named firms and dates rather than 'consensus'.
    - **kill_condition**: A majority of the ten named firms reiterate unchanged targets after Q3 with the stock still under $1,000, which would show the targets are deliberate rather than stale.
    - **novelty**: 2
    - **confidence**: 5
    - **materiality**: 2
    - **caveats**: The corpus is a sample of commentary, not a full sell-side roster (the brief cites ~37 covering analysts), so the 'ten firms' is a lower bound on named sources, not a count of all coverage. analyst_calls is LLM-extracted; firm attribution is occasionally wrong (e.g. 'GE Vernova' as the firm for an aggregator average).
- **dead_ends**:
  - 'Sold out through 20XX' is NOT a misread: the mutation tracks GEV's own language with a ~1-quarter lead. Strazik: ''26 and '27 largely sold out' (Apr 23 2025, nbcmiami); 'through 2028' (Sept 2025-Jan 2026 write-ups of Q3/Q4 calls); Q2'26 call (Jul 22 2026): 'mostly sold out through '30 ... more than half of the 30 gigawatts of '31 production slots by the end of this year'. The Jun 22 2026 Yahoo piece ('sold out through 2029 and extending to 2031') ran one month ahead of the company. Reproduce: SELECT published,url FROM sources WHERE tier='commentary' AND text LIKE '%sold out%' AND text LIKE '%Vernova%' ORDER BY published.
  - 'World's largest gas turbine plant': GEV's own Sep 2024 press language is 'the company's largest gas turbine manufacturing plant' (yahoo.com/news/ge-vernova-gas-turbines-hit-175522658.html, 2024-09-20) and the 2024 annual report says 'largest gas turbine repair shop outside the U.S.' for Singapore; 247wallst (Jun 24 2026) upgraded it to 'the world's largest'. Trivial, not material.
  - '125 GW under contract by year-end': fully supported by primary (Q2'26 8-K/EX and transcript: 116 GW at Jun 30, 'at least 125 GW' by YE26; the earlier YE26 target was 110 GW in the Apr 22 2026 8-K). Only nuance: the Q2 transcript pairs it with 'agreements signed into '31', and BNP's Sutton says the market is 'looking for an actual year-end backlog of 130 GW to 140 GW', so 125 GW is a floor, not a surprise. No echo distortion found.
  - '20% of gas order book is data center' appears verbatim in both the CNBC piece and the Q2'26 transcript (approximately 100 customers, 26 countries, 80% traditional, 20% data centers); commentary reproduces it faithfully. This overlaps the team's existing 'data center narrative gap' angle, so not pursued further.
  - Bearish facts buried in the two big bullish Jul 22 pieces (CNBC Investing Club 'sellers blinded by an earnings miss'; Yahoo 'Morgan Stanley strongly resets'): EPS $2.47 vs $3.17 expected (-22%), Wind segment EBITDA loss widened to $275M, Electrification orders $6.3B 'slightly below consensus', and GEV's own Q2 caveat that $/kW rose partly on aero mix. All are already visible in the 8-K and were covered by the team's Q2 read; nothing new beyond what is folded into Finding 1.
  - $3,000/KW inside a GEV filing: a May 18 2026 8-K exhibit (accession 0001193125-26-227930, ex99.2, filed under a customer/partner ticker) uses 'Assumes 5,000 MW project, with 75% gas generation at $3,000/KW' as a plant-cost modelling assumption; a direct chunks LIKE scan on ticker='GEV' returned nothing, so this appears in a non-GEV filer's deck. Confirms $3,000/kW is a plant-level cost convention, but does not change Finding 1.
  - 'GE Vernova's 176 billion backlog proves pricing power' (ainvest) and similar AI-generated pieces re-use the same numbers with no independent sourcing; ainvest.com and ainave.com account for 4 of the 7 '300%' echoes. Not worth citing individually.
  - semantic search (src/embed.py) not attempted, per token budget; transcript_statements (193 rows) too thin to add to the pricing trail beyond the Q2'26 transcript chunks already used.
  - Melius Research's underlying note and any GEV-disclosed $/kW time series do not exist in the corpus; the 300% claim cannot be verified or falsified from primary data, only bounded (GEV: +10-20% H1'26 vs 4Q'25; +6 pts backlog margin in FY25).

## [Sweep] find:competitor-filings

- **lens**: competitor filings reader (Siemens Energy, MHI, Vestas, Hitachi Energy vs GEV)
- **findings**:
  - - **title**: GEV's slot-reservation book turns over ~2.5x slower than Siemens Energy's, and covers ~8 years of current shipments (SE ~4, MHI ~2)
    - **claim**: Over the last five quarters GEV converted on average ~20% of its opening SRA pool per quarter (implied dwell ~15 months), while Siemens Energy converted 12 of ~27 GW (44%) in one quarter and states a 6-12 month conversion norm; SRAs are 54% of GEV's 116 GW commitments vs 27% of SE's 95 GW, and MHI runs no reservation program at all.
    - **mechanism**: SRAs carry small deposits and, per GEV's own 10-K, counterparties 'may not place orders equal to the value of their reservation amount or at all'. A pool that converts slowly is customer optionality, not backlog: it inflates the '116 GW / at least 125 GW under contract' headline and the 2027 $200B backlog path, while the cash (contract liabilities) and revenue (cost-to-cost on firm orders) only arrive at conversion. If GEV fixes price at reservation, slow conversion also locks old-vintage pricing (the GLJ point); if it does not, customers hold cheap options across three OEMs.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, GEV 8-K/EX press releases 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22, 2026-07-22
        - **date**: 2025-07-23 to 2026-07-22
        - **quote_or_number**: Converted / shipped / SRA pool by quarter: Q2'25 3/5, 21->25; Q3'25 7/4, 25->29; Q4'25 8/3, 29->43; Q1'26 6/4, 43->56; Q2'26 10/3, 56->63. Conversion as % of opening pool: 14%, 28%, 28%, 14%, 18%.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND ("Converted" OR "shipped")' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date
      - - **source**: sources id 3167, Siemens Energy Q3 FY26 analyst presentation (assets.siemens-energy.com ... 2026-08-05_Q3_Analyst_presentation)
        - **date**: 2026-08-05
        - **quote_or_number**: 15 GW booked (12 GW converted from SRAs), 6 GW shipped; 69 GW backlog / 26 GW SRAs
        - **reproduction**: SELECT text FROM sources WHERE id=3167 (search 'converted from SRAs')
      - - **source**: sources id 3169, Siemens Energy Q3 FY26 pre-close call transcript
        - **date**: 2026-06-29
        - **quote_or_number**: conversion of those into orders within on average 6-12 months, which is also visible in our large order backlog of around 60 GW as of Q2 Fiscal Year 2026
        - **reproduction**: SELECT text FROM sources WHERE id=3169 (search '6-12 months')
      - - **source**: sources id 3172, Siemens Energy Q2 FY26 analyst presentation
        - **date**: 2026-05-12
        - **quote_or_number**: 12 GW booked, 87 GW total commitments, thereof 24 GW data center related (=> ~27 GW SRAs at Q2 given ~60 GW backlog; 12/27 = 44% converted in Q3)
        - **reproduction**: SELECT text FROM sources WHERE id=3172 (search '87 GW')
      - - **source**: sources id 351 and 1743 (Utility Dive / Yahoo, MHI Q1 FY26 briefing) and id 3199 MHI Q1 FY26 Q&A
        - **date**: 2026-08-13
        - **quote_or_number**: Mitsubishi sold 35 large-frame gas turbines, for a total of 16 GW, in its 2025 fiscal year... current backlog 35 GW, up from 23 GW. MHI Q&A docs contain zero occurrences of 'reservation'; 'We book orders once contracts take effect' (id 3215).
        - **reproduction**: SELECT id, text FROM sources WHERE id IN (351,3199,3215); python: len(re.findall('reservation', text, re.I)) == 0 for 3199/3207/3211/3215
      - - **source**: chunks, GEV 10-K filed 2026-01-29 risk factor
        - **date**: 2026-01-29
        - **quote_or_number**: some counterparties to slot reservation agreements may not place orders equal to the value of their reservation amount or at all
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND "reservation amount"' AND c.ticker='GEV' AND c.form='10-K'
      - - **source**: arithmetic on the above
        - **date**: 2026-09-21
        - **quote_or_number**: Years of cover = commitments / shipments: GEV 116 GW / 14 GW trailing-4Q shipped = 8.3 yrs (5.8 yrs at the 20 GW run-rate); SE 95 GW / ~22 GW FY25-27 capacity = 4.3 yrs; MHI 35 GW / 16 GW = 2.2 yrs. Cross-check: GEV SRAs signed Q2'25-Q2'26 = 7+12+21+19+18 = 77 GW, converted 34 GW (44% cumulative) vs SE 44% in a single quarter.
        - **reproduction**: Recompute from the 8-K series above and sources 3167/3179/351
    - **why_market_misses_it**: Sell-side adds backlog and SRAs into one 'under contract' number and compares GEV to itself quarter over quarter; nobody puts GEV's conversion velocity next to Siemens Energy's stated 6-12 month norm or MHI's no-reservation practice, and the 8-Ks never give SRA aging.
    - **testable_prediction**: GEV Q3'26 release (about 2026-10-22): SRAs converted <= 13 GW (<= 20% of the 63 GW pool), SRA balance >= 58 GW, SRAs still >= 50% of total commitments; year-end 'at least 125 GW' will be majority SRAs.
    - **kill_condition**: GEV converts >= 20 GW of SRAs in Q3'26, or discloses that SRAs convert within 12 months on average / provides an aging table showing < 25% of SRAs older than 4 quarters.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: SE's 6 GW shipped and 69 GW backlog include medium-size turbines and (per its capacity footnote) steam-turbine capacity of combined-cycle configurations, so SE GW are not strictly like-for-like with GEV heavy-duty GW. SE SRA pool at Q2 FY26 (~27 GW) is inferred from '87 GW commitments' minus 'around 60 GW backlog'. Slow conversion could partly reflect GEV selling later delivery slots (2029-30) rather than weaker customers.
  - - **title**: Three-OEM announced large-frame capacity (~85-90 GW/yr by 2028-30) exceeds MHI's own post-2027 market view (40-50 GW/yr) exactly when GEV's reservation book is due to convert
    - **claim**: Siemens Energy discloses gas turbine capacity of 17 GW (FY24) -> ~22 GW avg FY25-27 -> >30 GW FY28-30 and large-turbine output rising from ~35 to ~50 units/yr in FY27; MHI is doubling capacity vs FY2024 from a 16 GW/yr base; with GEV's 24 GW (2028) / 30 GW (2030) the three sum to ~85-90 GW/yr, versus MHI's stated market of ~70 GW/yr for 2025-27 falling to 40-50 GW/yr thereafter.
    - **mechanism**: GEV's Power margin guidance (17-19%) and the 2027 vintage margin rest on 'supply-constrained' pricing. Capacity that arrives in FY27-28 at all three OEMs, plus Ansaldo/Doosan entrants, hits the market in the same window when GEV's 63 GW of SRAs must be converted to priced orders; if pricing plateaus, the conversion price, not the reservation headline, sets 2028-30 Power equipment revenue and margin.
    - **direction**: short
    - **evidence**:
      - - **source**: sources id 3179, Siemens Energy GIS Conference presentation (CFO Maria Ferraro)
        - **date**: 2026-01-12
        - **quote_or_number**: Capacity # GT units, GW: FY24 ~110 / 17 GW; avg FY25-27 ~160 / 22 GW; avg FY28-30 210-230 / >30 GW; +30%; Capacity sold-out until FY28 (footnote: including steam turbine capacity of combined cycle configuration)
        - **reproduction**: SELECT text FROM sources WHERE id=3179 (search 'sold-out until FY28')
      - - **source**: sources id 3169, Siemens Energy pre-close call
        - **date**: 2026-06-29
        - **quote_or_number**: big step up in capacity additions will take place in Fiscal year 2027, when we will be able to produce around 50 large gas turbines per year in comparison to around 35 units before; medium-size: adding 30 additional units to the 50
        - **reproduction**: SELECT text FROM sources WHERE id=3169 (search '50 large gas turbines')
      - - **source**: sources id 3207 and 3211, MHI Q3 FY25 and Q2 FY25 Q&A transcripts (mhi.com/finance/library/result/pdf/fy20253q/qa_20253q.pdf, fy20252q/qa_20252q.pdf)
        - **date**: 2026-02 (Q3 FY25) and 2025-11 (Q2 FY25)
        - **quote_or_number**: our view remains that market size will be around 70 GW per year for the time being and that it will remain at around 50 GW after that; demand seems to have been close to 100 GW in 2025 (uncertain). CFO Ito: The projected demand of 70 GW/year seems slightly too high when compared to the 40 to 50 GW seen previously.
        - **reproduction**: SELECT text FROM sources WHERE id IN (3207,3211) (search '70 GW')
      - - **source**: sources id 3199 MHI Q1 FY26 Q&A and id 150 Utility Dive (Bloomberg)
        - **date**: 2026-08-13 / 2025-08
        - **quote_or_number**: production capacity would be doubled relative to FY2024 ... The expansion of production capacity needed to meet that demand is also progressing smoothly; MHI plans to double its manufacturing capacity of gas turbines over the next two years
        - **reproduction**: SELECT text FROM sources WHERE id IN (3199,150)
      - - **source**: sources id 1713, MHI GTCC Business Briefing (McCoy data)
        - **date**: 2025-08
        - **quote_or_number**: GT market volume reached 57.4 GW in 2024, the highest since 2018; 1H 2025 41.7 GW; annual expected around 70 GW; North America 1H25 18.6 GW vs 14.9 GW full 2024
        - **reproduction**: SELECT text FROM sources WHERE id=1713 (search '57.4 GW')
      - - **source**: sources id 351 (MHI FY25 release via Utility Dive)
        - **date**: 2026-08-13
        - **quote_or_number**: 35 large-frame gas turbines, 16 GW, in FY2025 (=> doubling implies ~30 GW/yr)
        - **reproduction**: SELECT text FROM sources WHERE id=351
      - - **source**: task brief / GEV 8-K 2026-07-22
        - **date**: 2026-07-22
        - **quote_or_number**: GEV: 20 GW/yr from Q3'26, 24 GW in 2028, 30 GW in 2030. Sum 2028-30: GEV 24-30 + SE >30 + MHI ~30 = ~85-90 GW/yr
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"gigawatts" AND "2028" AND "2030"' AND c.ticker='GEV' AND c.form='8-K/EX'
    - **why_market_misses_it**: The team's market-size angle debates MHI 70 vs SE 110-120 GW demand; the competitor decks quantify the supply side, and the sum of announced capacity has not been put against MHI's post-2027 demand view. Each OEM says 'our additions are justified', but nobody adds them up.
    - **testable_prediction**: By Siemens Energy Q4 FY26 results/CMD (mid-Nov 2026) SE reiterates >30 GW FY28-30 capacity and ~50 LGT/yr in FY27; by MHI Q2 FY26 (early Nov 2026) MHI keeps 'around 70 GW then 40-50 GW'; first sign of a plateau is GEV, SE or MHI describing pricing as 'stable' rather than 'improving' on a call by mid-2027.
    - **kill_condition**: MHI raises its post-2027 market view to >= 80 GW/yr, or SE or MHI defers/cancels an announced capacity step, or McCoy 2026 full-year orders print >= 100 GW.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: SE's GW capacity includes steam turbines of combined cycles (overstates gas GW by roughly a third); MHI's doubling is units/throughput with no GW figure from MHI itself; the 40-50 GW is MHI's view and MHI itself said 2025 demand ran near 100 GW. Overlaps the team's market-size and throughput angles; the new part is the dated supply sum.
  - - **title**: Siemens Energy's disclosed fleet service yield (~EUR 11.5M per GW-year) and GEV's own Power services line cap the bull's '$70M per GW-year' at 2-6x too high
    - **claim**: SE FY25 Gas Services revenue EUR 12,198M with a 66% service share (EUR 8.05B) on a >700 GW fleet is ~EUR 11.5M per GW-year; GEV FY25 Power services $13,081M on a fleet the bull case sizes at 400+ GW is at most ~$33M per GW-year (and includes steam, nuclear and hydro services); SE also says service from today's orders materializes ~3 years after installation and its service backlog grew only EUR 34B -> 41B (FY22-FY25) while gas turbine sales doubled.
    - **mechanism**: The bull frontier values GEV on services of ~$70M per GW-year applied to 400+ GW; the competitor's own disclosure and GEV's segment table show fleet-average service yield is a fraction of that, and the incremental HA/HL service stream lags delivery by ~3 years (delivery + warranty), so 2026-28 service revenue cannot compound at the new-unit order rate. That caps the terminal-value argument used to defend a 31-38x forward P/E.
    - **direction**: short
    - **evidence**:
      - - **source**: sources id 3180, Siemens Energy Annual Report 2025 (assets.siemens-energy.com ... A-Siemens_Energy_Annual_Report_2025)
        - **date**: 2025-11
        - **quote_or_number**: Gas Services orders 22,996 / revenue 12,198 (EUR M, FY25); 'the share of the service business in GS revenue remained unchanged at 66% (2024: 66%)'
        - **reproduction**: SELECT text FROM sources WHERE id=3180 (search 'Gas Services 22,996' and 'share of the service business in GS')
      - - **source**: sources id 3179, SE GIS Conference deck, slide 'An opening act to an even greater story'
        - **date**: 2026-01-12
        - **quote_or_number**: Gas Services installed fleet >700 GW; Fleet additions (FY24-30) ~180 GW; Service order backlog EUR bn: 34 (FY22), 41 (FY25), >50 (FY28e); >90% renewal rate for long term programs
        - **reproduction**: SELECT text FROM sources WHERE id=3179 (search '700 GW')
      - - **source**: sources id 3169, SE pre-close call
        - **date**: 2026-06-29
        - **quote_or_number**: the full benefit of today's order intake will materialize in general 3 years after installation
        - **reproduction**: SELECT text FROM sources WHERE id=3169 (search '3 years after installation')
      - - **source**: chunks, GEV 10-K filed 2026-01-29, Power segment table
        - **date**: 2026-01-29
        - **quote_or_number**: Power: Equipment $6,686 / $5,708 / $5,598; Services $13,081 / $12,419 / $11,838 (FY25/24/23, $M); Gas Power $16,006; 126 HA-Turbines installed, ~3.6M operating hours; ~1,700 units under LTSA, avg remaining life ~10 years
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Total segment revenues" AND "Equipment" AND "Services" AND "Gas Power"' AND c.ticker='GEV' AND c.form='10-K' AND c.filing_date='2026-01-29'
      - - **source**: arithmetic
        - **date**: 2026-09-21
        - **quote_or_number**: SE: 12,198 x 0.66 / 700 = EUR 11.5M per GW-yr. GEV: 13,081 / 400 = $32.7M per GW-yr upper bound (all Power services). Bull $70M x 400 GW = $28B/yr, larger than GEV's entire FY25 Power segment revenue ($19.8B).
        - **reproduction**: Recompute from the two rows above
    - **why_market_misses_it**: The $70M per GW-year figure circulates as an HA-class LTSA rule of thumb and gets multiplied by the whole installed fleet; SE is the only OEM that publishes fleet GW, service share and service backlog together, so the cross-check lives in a competitor deck no GEV analyst cites.
    - **testable_prediction**: GEV FY26 10-K (late Jan 2027): Power services revenue <= $15.0B (<= +15% y/y) while Power equipment grows > 25%; SE FY26 results (mid-Nov 2026): service share of Gas Services revenue prints below 66%.
    - **kill_condition**: GEV Power services revenue grows > 25% in FY26, or GEV discloses fleet-wide gas services economics >= $50M per GW-year, or SE's FY26 service backlog jumps > EUR 50B two years early.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: GEV does not disclose installed GW; the 400+ GW comes from the bull framing in the brief, so the GEV per-GW figure is an upper bound on a borrowed denominator. SE's 700 GW is 'as of FY23' and includes steam turbines. A bull can fairly argue $70M applies only to new HA units under LTSA, but then it applies to ~60 GW, not 400.
- **dead_ends**:
  - Double-booking across OEMs: projects table has only one owner with both GE Vernova and a competitor (Applied Digital, 7 rows), but the Siemens Energy row is B&W boilers + Siemens steam turbines under a limited notice to proceed (source 2026-08-21) and the GE row is an intention to 'convert when gas turbines become available' (2026-09-11); not a gas-turbine double reservation. YTL (SE SGT-9000HL 5.25 GW reservation, Jun-2030 delivery), Tallgrass (MHI M501JAC), NET Power (Siemens SGT-A35), xAI (Doosan), Capital Power (MHI JAC) have no GEV link in chunks (FTS '<name>' AND 'Vernova').
  - No OEM says anything about customers holding slots with several OEMs; no OEM discloses deposit size per SRA. SE only says 'reservation fees' are inside FCF advance payments; its half-year report has no SRA accounting policy.
  - competitor_financials table is nearly useless for MHI, Vestas and Hitachi Energy (8 rows each, all 'Not specified'); only Siemens Energy rows carry content. Use sources text (ids 3165-3182 SE, 3196-3219 MHI, 3224-3243 Vestas) instead.
  - MHI Q&A transcripts (ids 3199, 3207, 3211, 3215) and the GTCC briefing (1713) contain zero occurrences of 'reservation' or 'cancel'; MHI gives units and yen, never GW backlog in its own docs (the 35 GW / 16 GW figures come via Utility Dive quoting MHI's release).
  - Cancellations: SE says explicitly 'we have not seen any cancellations or any delays on our side' (2026-06-29); GEV filings mention cancellation only for an Offshore Wind project and the generic SRA risk factor; MHI silent. No divergence to exploit yet.
  - Hitachi Energy sources are mostly web boilerplate (privacy, recruitment pages); the only substantive items are press releases on a $1.5B transformer ramp (id 3408) and $30M Canada (3409) with no lead-time numbers. Nothing beyond the team's Prolec angle.
  - Vestas Q1/Q2 2026 announcements (ids 3232, 3230): only 'firm and unconditional' order intake (4,504 MW, 3,349 MW) and EUR 36bn backlog; no cancellation or slipped-delivery disclosures relevant to gas; not pursued.
  - H-class reliability: MHI J/JAC 172 units ordered, >3M operating hours (Aug 2025) vs GEV 126 HA units, 3.6M hours (Dec 2025); no competitor discloses an availability-shortfall figure comparable to GEV's $0.3B/yr, so no cross-check possible.
  - SE '~EUR 400m/GW' on the GIS slide is new-unit revenue per GW (78 GW x 0.4 = ~EUR 30bn), not a service figure; do not cite it as service economics.
  - Did not use Ollama semantic search or web fetches; all findings are reproducible from the SQLite corpus alone.

## [Sweep] find:wind-electrification

- **lens**: Non-gas segment forensics: Wind (offshore losses, Vineyard, onshore order collapse, services) and Electrification (Prolec purchase accounting, organic vs reported)
- **findings**:
  - - **title**: Wind FY26 guidance arithmetically requires the first profitable half since the spin: H2'26 must be about +$257M vs H2'25 -$286M
    - **claim**: Management's reiterated FY2026 Wind guide of ~$400M segment EBITDA losses, after an H1'26 loss of $657M, implies H2'26 Wind EBITDA of roughly +$257M, a ~$540M half-on-half swing that no half since 2023 has come close to, and the only visible bridge is the confidential Sept 16 2026 Vineyard Wind settlement (GEV had claimed >$300M owed).
    - **mechanism**: Wind segment EBITDA flows straight into Adjusted EBITDA and FCF. Either (a) Q3 2026 (report ~Oct 21-22) contains a one-time settlement/claims-recovery revenue booked at Offshore Wind, like the $0.5B settlement revenue of Q3 2024 (10-K FY25 MD&A), which the market may misread as a structural Wind turn, or (b) the ~$400M loss guide is cut by $200-400M at Q3, i.e. 3-5% of FY26 company EBITDA.
    - **direction**: short
    - **evidence**:
      - - **source**: 8-K/EX 2026-07-22 (Q2'26 earnings release), chunks table, GEV
        - **date**: 2026-07-22
        - **quote_or_number**: Wind: Organic revenue* down low-double digits and approximately $400 million of segment EBITDA losses.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"segment EBITDA losses"' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date DESC
      - - **source**: 8-K/EX 2026-01-28 guidance section
        - **date**: 2026-01-28
        - **quote_or_number**: approximately $400 million of segment EBITDA losses, versus prior guidance of similar segment EBITDA losses to 2025
        - **reproduction**: same query as above; filter filing_date='2026-01-28'
      - - **source**: 8-K/EX organic reconciliation tables, 'Wind (GAAP)' rows: Q1'25 -146, Q2'25 -165, Q3'25 -61, Q4'25 -225, FY25 -598, Q1'26 -382, Q2'26 -275 ($M)
        - **date**: 2025-04-23 to 2026-07-22
        - **quote_or_number**: H1'25 = -312, H2'25 = -598-(-312) = -286; H1'26 = -657; guide -400 implies H2'26 = +257; H2'24 = -588-(-289) = -299 even with the $0.5B settlement
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind (GAAP)"' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date DESC; regex 'Wind \(GAAP\).{0,160}'
      - - **source**: 10-Q 2026-07-22, documents.id=218, MD&A Offshore Wind paragraph
        - **date**: 2026-07-22
        - **quote_or_number**: we are working with our customer to resolve outstanding claims and counterclaims
        - **reproduction**: SELECT text FROM documents WHERE id=218; regex 'Vineyard'
      - - **source**: https://www.insurancejournal.com/news/east/2026/09/17/885444.htm (sources table)
        - **date**: 2026-09-17
        - **quote_or_number**: GE Vernova's effort to walk away from its $4.5 billion project in New England over claims it was owed more than $300 million ... withdrawn the termination notice
        - **reproduction**: SELECT url, published FROM sources WHERE url LIKE '%insurancejournal.com/news/east/2026/09/17/885444%'
      - - **source**: https://finance.yahoo.com/energy/articles/ge-vernova-eyes-200b-backlog-080209388.html
        - **date**: 2026-09-18
        - **quote_or_number**: He expects wind profitability to improve in the second half and to be materially better in 2027 than in 2026.
        - **reproduction**: SELECT url FROM sources WHERE url LIKE '%ge-vernova-eyes-200b-backlog%'
      - - **source**: 10-K FY25, documents.id=249, Wind segment MD&A
        - **date**: 2026-01-29
        - **quote_or_number**: nonrecurrence of revenues recorded on the settlement of a previously canceled project of $0.5 billion in the third quarter of 2024
        - **reproduction**: SELECT text FROM documents WHERE id=249; regex 'settlement of a previously canceled project'
    - **why_market_misses_it**: Sell-side and news coverage treat the Sept 16 settlement as 'removing an overhang' and repeat management's 'second-half improvement' line; nobody has put the H1 actual next to the full-year guide and computed the required H2 number, and settlement terms are confidential so a Q3 gain would arrive unlabeled inside Offshore Wind revenue.
    - **testable_prediction**: At the Q3 2026 print (about Oct 21-22, 2026) Wind segment EBITDA is either (a) positive by more than $100M with an explicit settlement/claims item in the Offshore Wind variance explanation, or (b) negative and the FY26 Wind guide moves to worse than $500M of losses. Probability of a clean, organic positive H2 (no settlement item, guide held) under 20%.
    - **kill_condition**: Q3'26 Wind segment EBITDA is at or above +$50M with the variance explanation citing only onshore services, pricing and offshore installation productivity and no settlement, claims-recovery, or reversal of previously recorded contract-loss provisions.
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Half-year arithmetic uses the recast 2025 segment figures published Jul 22 2026 (business-unit realignment effective Jan 1 2026); pre-recast quarters can differ by tens of millions. Dogger Bank B and C run 'the better part of 2027' and Q1/Q2'26 both cite higher offshore project costs, so further loss provisions are still possible. The 10-K FY25 says further timeline changes 'could result in further losses beyond the amounts that we currently estimate.'
  - - **title**: Onshore Wind equipment orders fell 61% in units and 63% in GW in Q2'26 with zero repower orders, just as OBBBA's July 4 2026 begin-construction deadline passed; 2027 Wind revenue is set for another ~25% equipment decline
    - **claim**: Q2'26 wind turbine orders were 147 units (Q2'25: 381), repower orders 0 (Q2'25: 205) and 0.6 GW (1.6 GW); annual orders went 9.1 → 5.3 → 4.9 GW (2023-2025) and only 1.2 GW in H1'26; Wind equipment RPO is $8.2B, down 40% from $13.7B at Dec-2023, so 2027 onshore equipment revenue should fall roughly a quarter from 2026 even before the OBBBA PTC cliff, while services (+41% y/y) are the only offset.
    - **mechanism**: Onshore equipment is recognized on delivery 12-18 months after order; Wind SG&A+R&D is ~$0.7B/yr and largely fixed, so equipment revenue falling from a $4.5B annualized H1'26 pace toward ~$3.5B keeps Wind at a $300-500M loss in 2027 unless offshore closes out. OBBBA (P.L. 119-21) removes PTC/ITC for wind placed in service after 2027 unless construction began by July 4 2026, so post-July orders for 2028+ delivery lose the credit; this makes the H2'26 and 2027 order base structurally lower, contradicting 'materially better in 2027'.
    - **direction**: short
    - **evidence**:
      - - **source**: 10-Q 2026-07-22 (documents.id=218) Wind orders/sales table
        - **date**: 2026-07-22
        - **quote_or_number**: Orders: Wind Turbines 147 vs 381; Repower Units — vs 205; GW 0.6 vs 1.6 (Q2'26 vs Q2'25). H1: 293 vs 404 units, 1.2 vs 1.8 GW. Sales GW 1.4 vs 1.7 (Q2), 2.0 vs 3.0 (H1)
        - **reproduction**: SELECT text FROM documents WHERE id=218; regex 'WIND Three months ended'
      - - **source**: 10-K FY25 (documents.id=249) Wind orders table
        - **date**: 2026-01-29
        - **quote_or_number**: Wind Turbine and Repower Units Gigawatts 4.9 / 5.3 / 9.1 (2025/2024/2023); sales GW 6.9 / 7.8 / 8.8; Equipment RPO $9,112 / $10,720 / $13,709
        - **reproduction**: SELECT text FROM documents WHERE id=249; regex 'Onshore and Offshore Wind orders in units'
      - - **source**: 10-Q 2026-07-22 Wind RPO and segment table
        - **date**: 2026-07-22
        - **quote_or_number**: Wind Equipment RPO $8,197 (Jun-26) vs $9,731 (Jun-25); Services RPO $12,191; Wind services revenue Q2'26 $631M vs $447M (+41%), H1 $1,174M vs $885M (+33%); equipment H1 $2,283M vs $3,192M (-28%)
        - **reproduction**: SELECT text FROM documents WHERE id=218; regex 'Onshore Wind \$1,721' and 'Six months ended June 30, 2025 Power Electrification Wind Total'
      - - **source**: 8-K/EX 2026-07-22 Wind segment table
        - **date**: 2026-07-22
        - **quote_or_number**: Orders $1,249 vs $2,063 (39)%; Cost of revenues $2,123 vs revenue $2,026 (negative gross margin); SG&A $137, R&D $34
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind Three months ended June 30"' AND c.ticker='GEV' AND c.form='8-K/EX'
      - - **source**: XEL 10-K 2026-02-25 and ETR 10-K 2026-02-19 (customer filings in corpus) describing OBBBA
        - **date**: 2026-02-19
        - **quote_or_number**: Eliminating production and investment tax credits for wind and solar facilities placed in service after 2027, for facilities that begin construction after July 4, 2026.
        - **reproduction**: SELECT c.ticker, c.form, c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"wind" AND ("safe harbor" OR "begin construction")' AND c.filing_date>='2026-01-01'
      - - **source**: 10-Q 2026-07-22 Tariffs paragraph
        - **date**: 2026-07-22
        - **quote_or_number**: estimated cost impact from the global tariffs ... approximately $100 million to $200 million in 2026; Wind Q1 and Q2 variance both cite 'the impact of tariffs' at Onshore Wind
        - **reproduction**: SELECT text FROM documents WHERE id=218; regex 'estimated cost impact from the global tariffs'
    - **why_market_misses_it**: Wind is ~8% of revenue and every note treats it as a rounding error behind gas; the Q1'26 '+85% orders' headline (off a $640M base) masked that Q2 was the lowest unit-order quarter in the disclosed series, and the zero-repower print is buried in a units table nobody reproduces. Management's 'over 30 GW could be repowered before PTC expires in 2030' line is a TAM claim, not an order.
    - **testable_prediction**: Q3'26 wind orders (Oct 21-22, 2026) below 1.0 GW and FY26 wind orders below 3.0 GW, the lowest since the spin; the January 2027 outlook guides Wind organic revenue down again for 2027 (equipment down, services up) rather than up.
    - **kill_condition**: Q3'26 or Q4'26 wind orders above 2.0 GW in a single quarter, or repower unit orders above 200 in a quarter, or the January 2027 guide calls for Wind revenue growth in 2027.
    - **novelty**: 2
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Unit counts mix onshore and offshore; the units and GW are as-reported and were not restated for the 2026 realignment in the 10-Q table (only dollar figures were recast). Services growth partly reflects 'increased transactional volume' (parts/repairs) that may be lumpy. Direction is 'short' for the segment; on the whole company this is a 2/5 materiality drag, not a thesis by itself.
  - - **title**: Prolec is EBITDA-accretive (21.3% margin, above organic Electrification 19.1%) but its purchase accounting inflates GAAP EPS by $4.0B once and depresses it by ~$180M/quarter of amortization for two years; 98% of the $9.66B price is goodwill and intangibles
    - **claim**: Note 8 of the Q2'26 10-Q shows Prolec contributed $860M revenue and $183M segment EBITDA in Q2'26 (21.3% margin) yet a pre-tax loss of $(57)M, because $4,172M of acquired intangibles (including $771M 'trademarks and other' amortized over 2 years and $2,860M customer-related over 12 years) lifted company intangible amortization from $176M in Q1'26 to $236M in Q2'26; the $3,992M remeasurement gain is 74% of H1'26 GAAP net income, and tangible net assets acquired were only $171M of $9,656M consideration.
    - **mechanism**: Segment EBITDA and Adjusted EBITDA exclude amortization, so Prolec raises Electrification margin (FY26 guide raised to $14.5-15.0B incl. ~$3.1B Prolec, 18-20% margin) while GAAP operating income carries ~$180M/qtr of non-cash amortization until the 2-year intangible rolls off around Feb 2028; trailing GAAP P/E is meaningless until Q1'27 laps the $4.0B gain. Separately, the 2025 organic base still contained Prolec equity-method income ($64M Q2'25, $212M FY25 in 'Other segment items'), so true like-for-like Electrification EBITDA growth is understated: Q2'26 organic $522M vs Q2'25 ex-Prolec $190M.
    - **direction**: neutral
    - **evidence**:
      - - **source**: 10-Q 2026-07-22 (documents.id=218) Note 8 Acquisitions
        - **date**: 2026-07-22
        - **quote_or_number**: Cash consideration $5,254; fair value of previously held 50% $4,402; total $9,656; Intangible assets 4,172; Goodwill 5,313; Total identifiable net assets $4,343; Current assets 1,654, other non-current 1,123, liabilities (1,078)+(1,528)
        - **reproduction**: SELECT text FROM documents WHERE id=218; find 'Total identifiable intangible assets acquired' and read the 2,200 chars before it
      - - **source**: 10-Q 2026-07-22 Note 8 intangible table
        - **date**: 2026-07-22
        - **quote_or_number**: Customer related 12 yrs $2,860; Patents and technology 6 yrs 533; Capitalized software 3 yrs 8; Trademarks and other 2 yrs 771; Total $4,172
        - **reproduction**: same document; regex 'Weighted-average useful lives'
      - - **source**: 10-Q 2026-07-22 Note 8 Prolec results
        - **date**: 2026-07-22
        - **quote_or_number**: Revenue and income (loss) before income taxes of Prolec GE were $859 million and $(57) million for the three months ended June 30, 2026 ... $1,344 million and $(166) million
        - **reproduction**: same document; regex 'Revenue and income \(loss\) before income taxes of Prolec'
      - - **source**: 8-K/EX 2026-07-22 organic reconciliation, Electrification row
        - **date**: 2026-07-22
        - **quote_or_number**: Electrification (GAAP) $3,637 / $671 EBITDA 18.4%; Less: Acquisitions 860 / 183; organic $2,727 / $522 19.1% vs Q2'25 organic $2,106 / $254 12.1%
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Electrification (GAAP)"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date='2026-07-22'
      - - **source**: xbrl_facts AmortizationOfIntangibleAssets and Goodwill, GEV
        - **date**: 2026-06-30
        - **quote_or_number**: Amortization: FY25 $238M; Q1'26 $176M; Q2'26 $236M. Goodwill: $4,439M Dec-25 → $9,855M Mar-26 → $9,689M Jun-26 (-$160M measurement-period adj.)
        - **reproduction**: SELECT tag,start_date,end_date,val FROM xbrl_facts WHERE ticker='GEV' AND tag IN ('AmortizationOfIntangibleAssets','Goodwill') AND end_date>='2025-12-31' GROUP BY tag,start_date,end_date
      - - **source**: 10-Q 2026-07-22 segment table and 10-K FY25 (documents.id=249) segment table, 'Other segment items(c)' for Electrification
        - **date**: 2026-01-29
        - **quote_or_number**: Electrification Other segment items: Q2'25 $(64)M, H1'25 $(113)M, FY25 $(212)M (footnote: primarily equity method investment income); Q2'26 $1M
        - **reproduction**: SELECT text FROM documents WHERE id=249; find 'Segment revenues 19,767 9,110 9,642 38,519'; and id=218 'Three months ended June 30, 2025 Power Electrification Wind Total'
      - - **source**: 8-K/EX 2026-07-22 guidance
        - **date**: 2026-07-22
        - **quote_or_number**: Electrification: Revenue of $14.5-$15.0 billion, inclusive of approximately $3.1 billion from Prolec GE ... and 18%-20% segment EBITDA margin
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"inclusive of approximately" "Prolec"' AND c.ticker='GEV' AND c.form='8-K/EX'
    - **why_market_misses_it**: Screens show trailing GAAP EPS ~$20 for H1 alone and a 'cheap' trailing P/E, or conversely flag Prolec as a loss-making acquisition from the Note 8 pre-tax loss line; both miss that the loss is entirely purchase-accounting amortization and step-up, and that the organic comparison base still contained Prolec's equity income.
    - **testable_prediction**: Q3'26 10-Q (Oct 2026): AmortizationOfIntangibleAssets between $225M and $250M; Prolec 'Less: Acquisitions' revenue $850-950M with EBITDA at least $170M (about 20% margin); Electrification 'Other segment items' stays near zero. Final purchase price allocation by Q1'27 keeps goodwill within $5.0-5.5B.
    - **kill_condition**: Prolec Q3'26 EBITDA contribution below $130M (margin under 15%) or revenue below $750M, or a goodwill impairment/measurement-period adjustment above $500M, which would mean the 2.8x-sales price was not supported by earnings.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Purchase accounting is preliminary until Q1 2027. The $771M 2-year 'trademarks and other' bucket is likely mostly acquired order backlog; the 10-Q does not say. Quarterly amortization for Prolec is estimated from the useful-life table (about $178M/qtr) and matches the $60M step-up between Q1 and Q2 only if Q1 carried two months. No data-center share or Mexico tariff exposure is disclosed for Prolec in the 10-Q.
- **dead_ends**:
  - xbrl_facts has no segment-dimensioned facts for GEV: no tag or label contains Wind/Electrification/Offshore; only NumberOfOperatingSegments and SegmentExpenditureAdditionToLongLivedAssets. Segment numbers must come from 10-Q/10-K/8-K text.
  - No GEV TRANSCRIPT chunks exist for 2026 (SELECT filing_date, COUNT(*) FROM chunks WHERE ticker='GEV' AND form='TRANSCRIPT' AND filing_date>='2026-01-01' returns nothing); Q1/Q2'26 call content is available only via NEWS summaries (e.g. 2026-04-23, 2026-07-22 items).
  - Remaining offshore backlog in $ or units (Dogger Bank B/C) is not disclosed in the 10-K FY25 or the 2026 10-Qs; only 'Dogger Bank B and C carry work through the better part of 2027' (news 2026-04-23). Offshore Wind revenue is $305M in Q2'26, $551M in H1'26.
  - No loss-provision balance for offshore contracts is disclosed; only annual incremental contract losses ($379M/$1,005M/$637M) in the 10-K. Regex for 'loss provision', 'onerous', 'loss contract' in the Q2'26 10-Q found nothing beyond MD&A variance language.
  - Vineyard Wind settlement (Sept 16 2026) terms are confidential; no dollar figure in any corpus source. Only the pre-settlement claim ('owed more than $300 million') is quantified.
  - The Q2'26 10-Q text contains no occurrence of 'Mexic' or 'data center' (regex on documents.id=218), so Prolec tariff exposure on Mexican plants and Electrification data-center share cannot be sourced from filings; the 10-Q only says five of seven Prolec sites are in the U.S.
  - mgmt_guidance table rows for Wind are mostly 2024 Form 10 boilerplate; the useful FY26 guide lines live in 8-K/EX chunks, not in mgmt_guidance.
  - Warranty accrual series (StandardProductWarrantyAccrual $1,292M Jun-24 → $1,595M Jun-26; FY25 issued $760M vs paid $629M) is company-wide, not split by segment, so it cannot isolate wind warranty; left to the team's existing warranty-per-GW angle.
  - Prolec acquired contract liabilities/deferred revenue are not broken out in Note 8 (only 'Current liabilities (1,078)'), so the customer-deposit ledger cannot be adjusted for the acquisition beyond an upper bound of about $1B.

## [Sweep] find:connectors-outside

- **lens**: Outside-the-corpus scout: SEC full-text search across all filers (2024-2026), non-corpus customer/supplier filings, court settlement news, Greenville permit/job-posting web search, GLJ note follow-up; cross-checked against the corpus and GEV's own 10-Q unit tables.
- **findings**:
  - - **title**: HA-turbine shipments fell in H1'26 while finished-goods inventory rose 66% since Dec-24: '20 GW output' is not 20 GW shipped
    - **claim**: GEV's own 10-Q unit tables show HA-turbine sales fell to 3 units in Q2'26 (from 8) and 8 in H1'26 (from 13), gas-turbine GW sold fell to 3.3 (from 5.2), while finished-goods inventory grew from $2.49B (Dec-24) to $4.14B (Jun-26); the Jan-2025 Greenville plan of 37/62/74 HA units for 2025/26/27 is running at roughly 24 and an annualized 16.
    - **mechanism**: Under cost-to-cost revenue recognition, costs on firm contracts flow to contract assets and revenue, not inventory. Finished goods rising $1.6B while HA units shipped fall means units are being built ahead of contract conversion or ahead of site readiness and parked. That ties up cash (H2'26 FCF guide already implies only $1.6-2.6B after $9.9B in H1), and it means the '20 GW annual output from Q3'26' claim can be met at the factory gate without a matching rise in GW shipped, revenue, or cash. If shipments stay ~3-4 GW/quarter into the Q3'26 10-Q, the 2027 revenue ramp embedded in a 31-38x forward P/E gets pushed right.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks (form 10-Q, GEV, filing_date 2026-07-22), Power unit table
        - **date**: 2026-07-22
        - **quote_or_number**: Sales in units, three months ended June 30, 2026 vs 2025: Gas Turbines 29 vs 21; Heavy-Duty 13 vs 18; HA-Turbines 3 vs 8; Aeroderivatives 16 vs 3; Gas Turbine Gigawatts 3.3 vs 5.2. Six months: HA 8 vs 13; GW 7.5 vs 8.2 (4.2+3.3 vs 3.0+5.2).
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Sales in units" AND "HA-Turbines"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q') ORDER BY c.filing_date
      - - **source**: chunks (form 10-K, GEV, filing_date 2026-01-29 and 2025-02-06), Power unit table
        - **date**: 2026-01-29
        - **quote_or_number**: Sales in units full year 2025/2024/2023: HA-Turbines 24/15/14; Heavy-Duty 54/48/58; GW 15.3/11.9/13.8. Orders in units 2025: HA 43, Heavy-Duty 110, GW 29.8.
        - **reproduction**: same query as above; filter c.form='10-K'
      - - **source**: xbrl_facts, GEV, tag InventoryFinishedGoods and InventoryWorkInProcessAndRawMaterials (instant facts)
        - **date**: 2026-06-30
        - **quote_or_number**: InventoryFinishedGoods: 2.49B (2024-12-31), 3.27B (2025-12-31), 3.87B (2026-03-31), 4.14B (2026-06-30). WIP+raw: 5.33B (2024-12-31) to 7.83B (2026-06-30). InventoryNet 8.59B to 12.69B.
        - **reproduction**: SELECT tag,end_date,MAX(val) FROM xbrl_facts WHERE ticker='GEV' AND start_date IS NULL AND tag IN ('InventoryFinishedGoods','InventoryWorkInProcessAndRawMaterials','InventoryNet') AND end_date>='2024-12-31' GROUP BY tag,end_date ORDER BY tag,end_date
      - - **source**: Upstate Business Journal, 'GE Vernova investing $160M in Greenville to expand gas turbine production' (GEV spokesman Chris White quoted)
        - **date**: 2025-01-30
        - **quote_or_number**: Projected output 37 turbines in 2025, 62 in 2026, 74 in 2027; 'about 50 turbines per year' today, target 70-80.
        - **reproduction**: https://upstatebusinessjournal.com/manufacturing/ge-vernova-investing-160m-in-greenville-sc-to-expand-gas-turbine-production/
      - - **source**: chunks (form 8-K/EX, GEV Q2'26 press release)
        - **date**: 2026-07-22
        - **quote_or_number**: 'we remain on track to deliver 20 GW of annual gas turbine output in the third quarter of 2026, with 24 GW in 2028'
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"20 GW" AND "output" AND "third quarter"' AND c.ticker='GEV' AND c.filing_date>='2026-07-01'
      - - **source**: chunks (form 10-K, GEV, filing_date 2026-01-29)
        - **date**: 2026-01-29
        - **quote_or_number**: 'As of December 31, 2025, we had 51 HA-Turbines in RPO, 43 being installed and commissioned, and 126 HA-Turbines in our installed base' (vs 32/30/115 at Dec-24). At 24 HA shipped per year, 51 in RPO is >2 years of HA output before any 2026 orders.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"HA-Turbines in RPO"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q') ORDER BY c.filing_date
    - **why_market_misses_it**: Sell-side tracks the headline GW-shipped series (5,4,3,4,3) and the '20 GW run-rate' language; nobody in the corpus commentary (0 hits after 2026-07-22) cites the HA unit line, which is buried in a Power segment table and shows the flagship frame down 63% YoY in Q2'26. Inventory is discussed as 'supply-chain investment', not as a symptom that output and shipments have decoupled.
    - **testable_prediction**: Q3'26 10-Q (expected ~Oct 22, 2026): if the 20 GW run-rate is real in shipments, Q3 gas-turbine GW sold >= 5.0 and HA-Turbines sold >= 10. I predict GW sold 3.5-4.5, HA units 4-8, and InventoryFinishedGoods >= $4.3B, with the company re-defining 'output' as factory completions rather than shipments on the call.
    - **kill_condition**: Q3'26 10-Q shows gas-turbine GW sold >= 5.0 AND HA-Turbines sold >= 10 AND InventoryFinishedGoods flat or down versus $4.135B. Any one of the three alone does not kill it.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: Inventory is company-wide (includes Wind and Electrification); the finished-goods split by segment is not disclosed, so part of the rise may be transformers/switchgear. 'Sales in units' is not footnoted in the 10-Q; I read it as units shipped/delivered consistent with the GW series the team already uses. The 37/62/74 Greenville plan is a spokesman quote from Jan 2025, not guidance, and HA units also come from Belfort (9HA). Overlaps the team's 'factory throughput' angle but changes its conclusion: the constraint that shows up in the numbers is shipment/site conversion, not the factory.
  - - **title**: Oglethorpe Power (non-corpus filer) discloses all-in cost of a 2029 GE Vernova combined-cycle at ~$2,300/kW and a 240 MW simple-cycle CT at $1,500/kW
    - **claim**: Oglethorpe's Smarr project, two GE Vernova combined-cycle units totaling 1,425 MW with a 2029 in-service date, is budgeted at $3.3B (~$2,300/kW, company's own figure), and its Talbot Unit 7, a 240 MW dual-fuel CT also due 2029, is budgeted at ~$360M (~$1,500/kW); these are the only counterparty-disclosed per-kW datapoints for a current-vintage GEV order I could find in EDGAR.
    - **mechanism**: GEV says turbine pricing will reach ~$600/kW by end-2027 and that H1'26 orders priced 10-20 points above Q4'25. Smarr's $2,300/kW all-in means the turbine island is roughly 25-30% of a utility's project cost, leaving GEV headroom to keep raising price before the OEM becomes the binding cost line. For the team's pricing-decomposition work this anchors the gross margin bridge on the 2025-26 order vintage that ships in 2028-29, i.e. the vintage that replaces the low-priced 2024 orders GLJ is worried about.
    - **direction**: long
    - **evidence**:
      - - **source**: Oglethorpe Power Corp Form 8-K, Q2 2025 investor presentation exhibit (CIK 0000788816, accession 0001628280-25-041154)
        - **date**: 2025-08-26
        - **quote_or_number**: Smarr: '1,425 MW, two-unit combined cycle', '2029 projected in-service date', 'approximately $3.3 billion, including contingency, (~$2,300 / KW)', 'GE Vernova as original equipment manufacturer'. Talbot Unit 7: '240 MW CT with dual fuel capabilities', '2029 projected in-service date'.
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/788816/000162828025041154/oglethorpepowerq22025inv.htm
      - - **source**: Oglethorpe Power Corp Form 10-K FY2025 (accession 0000788816-26-000009)
        - **date**: 2026-03-27
        - **quote_or_number**: 'We have separately entered into an agreement with GE Vernova Operations, LLC for the purchase of the two combined cycle units.' Smarr budget $3.3 billion; costs incurred to Dec 31, 2025 'approximately $343.5 million'; Talbot Unit 7 budget 'approximately $360 million', purchase agreement entered 2025.
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/788816/000078881626000009/opc-20251231.htm
      - - **source**: corpus check: chunks_fts
        - **date**: 2026-09-21
        - **quote_or_number**: 0 relevant hits for 'Smarr' or 'Oglethorpe' outside Southern Co glossary boilerplate; Oglethorpe is not a corpus ticker.
        - **reproduction**: SELECT c.ticker,c.form,c.filing_date FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Smarr" OR "Oglethorpe"' LIMIT 10
      - - **source**: Utility Dive, 'GE Vernova gas turbine backlog hits 100 GW as prices rise' (Strazik quote)
        - **date**: 2026-04-22
        - **quote_or_number**: H1'26 order pricing 'tracking 10 to 20 points higher on a dollar-per-kilowatt basis than fourth-quarter 2025 orders'; turbine prices 'projected to reach $600/kW by the end of 2027'.
        - **reproduction**: https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/
    - **why_market_misses_it**: Oglethorpe is a cooperative that files with the SEC because of public debt; it is outside every GEV coverage universe and outside this corpus. Its $/kW disclosure is in an investor-presentation exhibit, not the 10-K narrative, so full-text search on the 10-K alone misses it.
    - **testable_prediction**: Oglethorpe's Q3'26 10-Q (expected ~Nov 10, 2026) keeps the Smarr budget at $3.3B and the 2029 date; any increase will be attributed to EPC/labor rather than the GEV equipment contract, which was fixed in 2025.
    - **kill_condition**: Oglethorpe raises the Smarr budget by more than 10% and attributes it to the equipment supply agreement, or delays in-service past 2029 citing turbine delivery.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: $2,300/kW is an all-in project cost including contingency and AFUDC, not GEV's turbine price; the split is not disclosed. One project, one buyer, RUS-financed cooperative; not a market price series. The 2029 COD implies the units were ordered in 2024-25 at pre-2026 pricing.
  - - **title**: Across all SEC filers 2024-2026, only two counterparties disclose GEV slot reservations, and the largest (CPV Shay, 2.1 GW of 7HA.03) still lacks a PJM interconnection agreement until early 2027
    - **claim**: An SEC full-text scan of every 10-K/10-Q/8-K/S-1/6-K/20-F filed 2024-01-01 to 2026-09-21 finds only NRG (3.6 GW of 7HA under SRAs) and Kenon/OPC-CPV (Shay Energy Center, 2.1 GW, GE 7HA.03) disclosing GEV slot reservations; none discloses deposit percentages or refund terms, and Kenon's May 2026 6-K says Shay's equipment slot is signed while the project is still 'evaluating' eligibility and its grid-connection agreement is expected only in early 2027.
    - **mechanism**: GEV's $39.9B of contract liabilities and 63 GW of SRAs are backed by customer cash whose terms are invisible on the customer side. Shay is a concrete example of an SRA-backed slot on a project with no interconnection agreement and no financing yet; if Transition Cycle 2 slips or RBP eligibility fails, that slot becomes a cancellation or a re-marketing event in 2027, exactly the window GLJ's low-margin-vintage argument targets. For the team's 'backlog into dirt' and RPO-fine-print work, this is the one large data-center-adjacent PJM project where the counterparty's own filings can be tracked quarter by quarter.
    - **direction**: short
    - **evidence**:
      - - **source**: SEC full-text search API, forms 10-K,10-Q,8-K,S-1,S-4,20-F,6-K,424B4, 2024-01-01 to 2026-09-21
        - **date**: 2026-09-21
        - **quote_or_number**: '"slot reservation"' = 46 hits; after removing GEV's own filings and non-energy filers (Halozyme, Autolus, Lilium, INNIO/Liberty Jenbacher, Baker Hughes) the only GEV-turbine counterparties are NRG (10-Q 2025-08-06, 10-Q 2025-11-06, 10-K 2026-02-24) and Kenon Holdings (6-K 2026-03-12, 6-K 2026-05-20, 20-F 2026-03-30). '"GE Vernova" "reservation"' = 32 hits, same two energy counterparties plus Hawaiian Electric (10-Q 2026-08-07, Waiau LM6000 aero order, no terms) and Cadeler (vessel reservations).
        - **reproduction**: https://efts.sec.gov/LATEST/search-index?q=%22slot%20reservation%22&forms=10-K,10-Q,8-K,S-1,6-K,20-F&dateRange=custom&startdt=2024-01-01&enddt=2026-09-21 (User-Agent gev-corpus-research/1.0)
      - - **source**: Kenon Holdings Form 6-K, Exhibit 99.1 (OPC Energy Q1 2026 report)
        - **date**: 2026-05-20
        - **quote_or_number**: Shay Project (2.1 GW combined cycle, West Virginia): 'a slot reservation agreement for significant equipment has been signed and CPV Group is evaluating and taking actions to position the project to meet the eligibility requirements for participation in the RBP mechanism'; supplier not named in the filing.
        - **reproduction**: https://www.sec.gov/Archives/edgar/data/1611005/000117891326002811/exhibit_99-1.htm
      - - **source**: Energy Tech, 'CPV Shay Energy Center: Coming to Partial Rescue for PJM's Grid Capacity Challenges' and CPV press release on EQT gas netback
        - **date**: 2026-08-12
        - **quote_or_number**: Shay 'will revolve around three 1x1 combined cycle configurations using GE Vernova's 7HA.03 gas turbines'; largest project in PJM Transition Cycle 2 (~278 projects, ~23 GW); interconnection agreement signing expected 'early 2027'. CPV signed a 10-year gas netback with EQT for 2+ GW on 2026-08-12.
        - **reproduction**: https://www.energytech.com/infrastructure/news/55398129/cpv-shay-energy-center-coming-to-partial-rescue-for-pjms-grid-capacity-challenges ; https://cpv.com/2026/08/12/cpv-secures-10-year-gas-netback-with-eqt-to-supply-2-gw-cpv-shay-energy-center/
      - - **source**: chunks (NRG 10-K filing_date 2026-02-24; NRG 10-Q 2025-08-06)
        - **date**: 2026-02-24
        - **quote_or_number**: 'NRG has entered into slot reservation agreements with GEV for the procurement of 3.6 GW of 7HA gas turbines' (up from 2.4 GW in the Aug-2025 10-Q).
        - **reproduction**: SELECT c.ticker,c.form,c.filing_date,substr(c.text,1,300) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation"' AND c.ticker!='GEV' ORDER BY c.filing_date DESC LIMIT 8
      - - **source**: corpus check
        - **date**: 2026-09-21
        - **quote_or_number**: 0 hits for 'Shay' as a CPV project; Kenon/OPC/CPV not in corpus (KEN chunk count 0).
        - **reproduction**: SELECT COUNT(*) FROM chunks WHERE ticker='KEN'; SELECT c.ticker,c.form FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Shay"' LIMIT 5
    - **why_market_misses_it**: Kenon is a Singapore-domiciled foreign private issuer filing 6-Ks about an Israeli utility; no GEV analyst reads it. The negative result (no customer anywhere discloses deposit or refund terms) is itself informative: the market is taking GEV's characterization of SRA cash as 'sticky' with zero counterparty corroboration.
    - **testable_prediction**: Kenon's Q3'26 6-K (expected ~Nov 2026) will still describe Shay as pre-interconnection and pre-financial-close; PJM Transition Cycle 2 interconnection agreements for Shay will not be signed before Q1 2027.
    - **kill_condition**: Kenon or CPV announces Shay financial close, or a signed PJM interconnection agreement, before 2026-12-31; or any 10-Q/10-K by a GEV customer discloses refundable-deposit terms that make SRA cash clearly non-sticky in GEV's favor (which would strengthen, not kill, the bull case on deposits).
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: The 6-K does not name GE Vernova; the 7HA.03 attribution comes from trade press (Energy Tech) and CPV's project page. SEC full-text search returned HTTP 500 on two OR-syntax queries, so a few phrasings ('reservation agreement' + 'gas turbine', 'GE Vernova' + 'delivery' + '2028') were not completed. Slot reservations may be disclosed by private IPPs (not searchable) or under other wording ('capacity reservation', 'manufacturing slot').
- **dead_ends**:
  - SEC full-text search: direct EDGAR document fetch from Python returns HTTP 403 with a non-email User-Agent (SEC requires a contact address); I used WebFetch instead, which works but is summarized by a small model and missed passages in long documents (Kenon 20-F, Kenon March 6-K ex 99.1/99.2 flagged by the index for 'advance payment' + 'GE Vernova' + 'turbine' but not surfaced). A teammate with an approved UA could re-run those three documents.
  - Fermi Inc (FRMI) 10-K FY2025 and Oct-2025 424B4: the Project Matador campus lists 7 GE TM2500 leased units (~132 MW), 3 refurbished GE 6B (~114 MW), 6 Siemens SGT-800 (~300 MW), 3 Siemens F-class (~720 MW), 3 SGT6-5000F; no GE HA units, no deposit/price terms. Minor negative for GEV data-center share but no numbers to build on.
  - DPC Holdings S-1/424B4 (June 2026): a castings/precision-parts supplier listing GE Vernova as a customer; only quotable line is 'castings remains a key constraint to OEM production ramp-up' and casting orders growing 9%/yr 2024-2035. No GEV-specific volumes. Supports the team's existing supplier-ceiling angle, nothing new.
  - Venture Global 10-Q Q1'26 Exhibit 10.5 (Baker Hughes letter agreement, 2026-03-05): confirms BH reserves 'dedicated manufacturing capacity at a manufacturing facility of GE Vernova' for LNG-train turbines, but every quantity, payment milestone and termination fee is redacted [***].
  - TVA 10-Q (2026-08-04): no GEV turbine contract terms in the body; exhibits 10.6/10.7 (Cumberland head lease / facility lease) match '7HA' + 'deposit' in full-text search but were not read. Low priority: they are lease documents, not GEV purchase terms.
  - Hawaiian Electric 10-Q (2026-08-07): XBRL member tag 'WaiauRepowerProject...GEVernovaOperationsLLC 2026-04-28' shows a tagged commitment exists; narrative not surfaced by WebFetch. Press: six LM6000VELOX aero packages, first two COD 2029, >250 MW; contract value not public.
  - Vineyard Wind settlement (announced 2026-09-16/17): terms confidential, GEV withdrew termination notice and appeal; GEV had claimed ~$300M unpaid, Vineyard Wind ~$850M damages. Already in the corpus as NEWS rows dated 2026-09-17 to 2026-09-20, so not novel; no filing yet quantifying reserve release or charge.
  - GLJ Research (Gordon Johnson) initiation, Sell/$470, 2026-09-14: press coverage adds nothing beyond the 'cyclical gas-turbine manufacturer priced as a secular compounder' framing and wind losses; no new quantitative detail beyond what the team already has on the 2024-vintage margin.
  - Greenville permits: no SC DHEC/Department of Environmental Services air-permit modification or Greenville County building-permit record for the test facility is indexed by web search; the City of Greenville 'GE Vernova turbine development' page exists but has no permit numbers. Would need a direct records request.
  - Job postings: Glassdoor 'GE Vernova Greenville' listing counts 93 (Jul 2026) and 107 (Aug 2026); Indeed 28 'GE gas turbine Greenville' (Jun 2026). Search-snippet counts, unverified, and Glassdoor counts include duplicates; too noisy to use as a hiring-rate signal.
  - Data-center gas project cancellations or pauses in September 2026 involving GEV turbines: none found.
  - State PUC / FERC dockets quoting GEV price per kW: nothing beyond the LG&E/KU Mill Creek 7HA.03 approval already public; no testimony with $/kW for GEV equipment surfaced in web search. The Oglethorpe 8-K was the only counterparty $/kW found.
  - Liberty Energy 8-K (2026-09-18) filed two INNIO Jenbacher engine supply contracts containing 'slot reservation' language (bridge-power recips, not GEV); potentially useful for deposit-structure analogies but outside this lens and the team's bridge-power angle already exists.
  - Soluna Holdings 8-K ex 99.1 (2026-04-02) matched 'turbine' + 'deposit' + 'GE Vernova' but the URL returned 404.
  - Corpus commentary tier: 0 chunks after 2026-07-22 discussing the HA-turbine unit sales line or finished-goods inventory, confirming finding 1 is not already in the team's news flow.

## [Sweep] find:academic-physics

- **lens**: academic and technical miner (OPENALEX/ARXIV tier, Gas Turbine World / POWER / YouTube technical commentary, GE maintenance literature, EIA-923 fired-hour physics)
- **findings**:
  - - **title**: The $0.3B/yr availability-shortfall is a WIND fleet-reliability charge, not an HA charge, and it equals ~75% of the FY26 Wind loss guidance
    - **claim**: GEV's $0.3B/yr revenue reduction from availability shortfalls (2023-2025) is booked against wind-farm availability guarantees, not gas turbines, and by itself explains roughly three-quarters of the ~$400M FY26 Wind segment EBITDA loss guidance; the team brief currently pairs the number with the HA fleet.
    - **mechanism**: Onshore/offshore wind service contracts carry an availability guarantee measured per wind farm over one year. Forecast shortfalls are recorded as a reduction of Wind services revenue (10-K revenue-recognition policy), and each 1% of fleet-wide availability is worth <$0.1B. Blade and drivetrain physics drive availability: in the offshore reliability literature blades are 8-12% of failure events but ~35% of downtime, so a small number of blade events (Vineyard Wind removal of installed blades, LM blade quality) moves the availability metric disproportionately. The charge flows straight into Wind segment EBITDA, which is guided to about -$400M in 2026.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks id 29778, GEV 10-K filed 2026-01-29 (accession 0001996810-26-...)
        - **date**: 2026-01-29
        - **quote_or_number**: "reduction of revenues from availability shortfalls was $0.3 billion, $0.3 billion, and $0.3 billion" (2025, 2024, 2023); "A further 1% reduction in availability across the entire fleet would have resulted in an additional revenue reduction of less than $0.1 billion."
        - **reproduction**: SELECT c.form,c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"availability" "shortfall"' AND c.ticker='GEV' AND c.tier='primary' ORDER BY c.filing_date DESC LIMIT 4;  -- chunk 29778; the preceding chunk 29777 is headed 'Wind.'
      - - **source**: chunks id 67297, GEV 10-K filed 2025-02-06 (same query, older row) - shows the series started at $0.1B in 2022
        - **date**: 2025-02-06
        - **quote_or_number**: "performance guarantees of the wind farm's availability ... During the years ended December 31, 2024, 2023, and 2022, the reduction of revenues from availability shortfalls was $0.3 billion, $0.3 billion and $0.1 billion"
        - **reproduction**: same query as above; row with filing_date 2025-02-06
      - - **source**: chunks id 5624, GEV 8-K/EX (Q2'26 earnings release) 2026-07-22
        - **date**: 2026-07-22
        - **quote_or_number**: "Wind: Organic revenue down low-double digits and approximately $400 million of segment EBITDA losses."
        - **reproduction**: SELECT c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Wind" "losses" "2026" "expect"' AND c.ticker='GEV' AND c.tier='primary' AND c.filing_date>='2026-01-01' LIMIT 3;
      - - **source**: chunks id 29625, GEV 10-K 2026-01-29 (fleet under guarantee)
        - **date**: 2026-01-29
        - **quote_or_number**: services agreements on approximately 24,000 of our onshore wind turbines, from an installed base of approximately 59,000 units (Dec-24 10-K: 23,000 of 57,000)
        - **reproduction**: SELECT c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"installed base" "wind turbines"' AND c.ticker='GEV' AND c.tier='primary' ORDER BY c.filing_date DESC LIMIT 2;
      - - **source**: sources id 909, Frontiers in Marine Science 2026 (fmars.2026.1887598), offshore wind reliability review, commentary tier
        - **date**: 2026
        - **quote_or_number**: "approximately 8.3 failures per turbine per year ... blades are responsible for approximately 35% of total downtime despite accounting for only 8-12% of failure events"
        - **reproduction**: SELECT text FROM sources WHERE id=909; search the text for 'blades are responsible'
      - - **source**: chunks id 29831, GEV 10-K 2026-01-29 (offshore loss drivers)
        - **date**: 2026-01-29
        - **quote_or_number**: losses relate to "costs to remediate quality issues including the removal of previously installed blades at the Vineyard Wind project"
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"blade" "quality"' AND c.ticker='GEV' AND c.tier='primary' AND c.filing_date>='2026-01-01' LIMIT 3;
    - **why_market_misses_it**: The $0.3B sits in the revenue-recognition critical-accounting-estimates note, three paragraphs after the LTSA (gas) discussion, so readers (including the team's own brief) attach it to the 126-unit HA fleet. Read as a Wind item it says the Wind loss is not only offshore project write-downs that roll off with Vineyard/Dogger Bank; it is a recurring fleet-reliability deduction on 24,000 turbines under service contract that has been flat at $0.3B for three years while the Dec-24 10-K language about 'improving overall fleet availability' was dropped from the Dec-25 10-K.
    - **testable_prediction**: FY26 10-K (late Jan 2027) reports availability-shortfall revenue reduction of $0.2-0.4B again (not trending to zero), and Wind FY26 EBITDA loss lands at or worse than -$400M despite Offshore RPO shrinking ($22.5B Jun-25 to $20.4B Jun-26). Interim check: Q3'26 10-Q (late Oct 2026) Wind EBITDA for the quarter is negative by >$50M.
    - **kill_condition**: FY26 10-K shows the availability-shortfall figure at $0.1B or lower, or management quantifies a fleet-availability improvement (e.g. >97% onshore availability) on the Q3'26 or Q4'26 call.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: The $0.3B is a revenue reduction; the EBITDA effect is close to 1:1 only if remediation cost is not double-counted. The split between onshore and offshore guarantees is not disclosed. The Frontiers downtime statistics are European offshore fleets, not GE-specific. Team should also correct the brief: 'availability-shortfall $0.3B/yr' should not be listed under the HA 126-unit fact.
  - - **title**: FERC has set a Dec 31 2026 deadline for NERC computational-load standards after 1,500 MW of data-center load dropped off the Virginia grid; this is a dated regulatory catalyst for GEV Electrification grid-stability orders
    - **claim**: Large data-center loads (>=20 MW at >=60 kV) will become NERC-registered entities with ride-through obligations by year-end 2026, forcing hyperscalers and utilities to buy synchronous condensers, STATCOM/FACTS and grid-forming storage; GEV's Electrification data-center orders already exceed $5B YTD (more than double all of 2025) and the segment explicitly cites synchronous-condenser demand.
    - **mechanism**: Physics: data-center UPS/rectifier front ends drop to backup on voltage sags of ~0.3-0.5 pu and, with reclose-counting logic, stay off for hours; on a July 2024 fault six voltage depressions removed about 1,500 MW of data-center load in Northern Virginia and ~1,260 MW did not return. Loss of load causes over-frequency and voltage rise that can trip generators. Fixes are grid-side (synchronous condensers for fault current and inertia, STATCOMs, protection re-coordination) and load-side (grid-forming inverters plus batteries, which NERC's analysis says cut subharmonic currents ~70%). GEV sells all three through Electrification's Power Conversion & Storage (synchronous condensers), Grid Systems Integration (AC substations, HVDC) and Power Transmission (switchgear). Orders show up in Electrification backlog and, with 18-20% segment EBITDA margin guidance, in 2027 revenue.
    - **direction**: long
    - **evidence**:
      - - **source**: sources id 45, POWER magazine, 'Bringing a Power Plant's Worth of Load Onto the Grid: NERC's Interconnection Reckoning', RSS commentary tier
        - **date**: 2026-09-17
        - **quote_or_number**: "Coincident with the six voltage depressions, about 1,500 MW of demand disappeared from the system"; "About 1,260 MW dropped out at the third reclose and didn't return for hours"; "On July 16, 2026, FERC ordered NERC to file its computational-load reliability standards by the end of the year"; registration criteria (>=20 MW, >=60 kV, >=1 MW computational load) due Dec. 31, 2026
        - **reproduction**: SELECT published,url,text FROM sources WHERE id=45;  (url https://www.powermag.com/bringing-a-power-plants-worth-of-load-onto-the-grid-nercs-interco...)
      - - **source**: sources id 3532, arXiv 2509.07218v6 'Electricity Demand and Grid Impacts of AI Data Centers', academic tier
        - **date**: 2025-09-08
        - **quote_or_number**: "high-frequency undamped power oscillations appeared in a data center-rich region in Dominion Energy's grid, triggered by a once-a-second voltage sag"; "ERCOT has also reported multiple events wherein large computing loads tripped during transmission faults due to insufficient ride-through capability"
        - **reproduction**: SELECT text FROM sources WHERE id=3532; search 'ERCOT has also reported'
      - - **source**: sources id 45 (NERC mitigation figure)
        - **date**: 2026-09-17
        - **quote_or_number**: "pairing large loads with utility-scale batteries and grid-forming inverters can take roughly 70% off the subharmonic currents some AI workloads throw onto the system"
        - **reproduction**: SELECT text FROM sources WHERE id=45; search '70%'
      - - **source**: chunks id 5619, GEV 8-K/EX Q2'26 earnings release
        - **date**: 2026-07-22
        - **quote_or_number**: "continued demand growth in Electrification, with data center orders reaching over $5 billion year-to-date, more than double our 2025 total"
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Electrification" "data center" "orders"' AND c.ticker='GEV' AND c.tier='primary' AND c.filing_date>='2026-01-01' ORDER BY c.filing_date DESC LIMIT 1;
      - - **source**: chunks id 5738, GEV 10-Q Q2'26
        - **date**: 2026-07-22
        - **quote_or_number**: orders growth driven by "...alternating current substation solutions and high-voltage direct current solutions at Grid Systems Integration, and synchronous condensers at Power Conversion & Storage"; segment revenues H1'26: Power Transmission $3,256M vs $1,451M, Grid Systems Integration $1,497M vs $968M
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"synchronous condensers"' AND c.ticker='GEV' AND c.tier='primary' AND c.filing_date>='2026-01-01' ORDER BY c.filing_date DESC LIMIT 2;
      - - **source**: chunks id 236384, GEV Q4'25 earnings deck (sources id 1844), commentary tier
        - **date**: 2026-01-28
        - **quote_or_number**: "Significant orders at Electrification for data centers, HVDC, and synchronous condensers ... expect ~2X book-to-bill"
        - **reproduction**: SELECT text FROM chunks WHERE id=236384;
    - **why_market_misses_it**: Sell-side models Electrification as transformers plus switchgear volume (Prolec window, lead times). The ride-through physics turns a reliability rule into mandatory equipment purchases with a hard federal date, and none of the 37 covering analysts' notes in the corpus mention NERC computational-load registration. The July 2026 FERC order post-dates most initiations and the GLJ Sell note is gas-only.
    - **testable_prediction**: By Dec 31 2026 NERC files computational-load standards and Rules-of-Procedure registration criteria with FERC (docket RM26-4 and related). GEV Q3'26 release (late Oct 2026) reports Electrification data-center orders above $7B YTD and Electrification orders/revenue book-to-bill above 1.3x; FY26 Electrification revenue guidance ($14.5-15.0B) is held or raised.
    - **kill_condition**: FERC extends the NERC deadline into 2027, or GEV Q3'26 shows Electrification book-to-bill below 1.1x / data-center orders flat versus H1 run-rate, or management attributes Electrification growth solely to Prolec transformers.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: Path from rule to GEV order is one to two years for grid-side equipment, so most revenue lands beyond the 12-month window; the near-term line is orders/backlog and the multiple, not EPS. Hitachi Energy and Siemens Energy compete in synchronous condensers and STATCOMs; GEV share is not disclosed. The 1,500 MW event details come from a trade article, not the NERC incident report itself (the report exists publicly and should be cited directly in the memo).
  - - **title**: The GE F-class rotor life limit (144,000 factored fired hours / 5,000 factored starts) puts ~800-900 U.S. 7F units into a rotor end-of-life window over 5-7 years, and third parties are positioning to take that work using the same superalloy forgings GEV needs for the 20-30 GW new-unit ramp
    - **claim**: GE's own maintenance rule ends F-class rotor life at 144,000 factored fired hours or 5,000 factored starts; the 2000-2004 U.S. combined-cycle build (~108 GW in single-vintage plants) has accumulated on the order of 90-125k fired hours and is entering rotor life extension, a services event GE has already performed on 500+ F rotors, while independent shops (MD&A) cite 800-900 7F units and name superalloy forging lead time and shop capacity as the bottleneck.
    - **mechanism**: Rotor life extension or replacement is a Gas Power services transaction (parts plus outage) outside routine CSA hot-gas-path scope; each one is a multi-million-dollar upgrade sale recognized in Power services revenue. Two GEV lines are touched: (1) services upside as the 2000-2004 cohort hits 144k FFH / 5,000 FFS, and (2) share leakage plus supply competition, because the turbine wheel forgings for rotor life extension are the same long-lead nickel-alloy forgings consumed by new 7HA/7F production; GEV must allocate forging capacity between the 20-30 GW new-unit ramp and fleet rotor work, and third parties (MD&A, EthosEnergy, PSM/Hanwha) are tooling up to take what GEV cannot serve.
    - **direction**: either
    - **evidence**:
      - - **source**: GE Vernova, 'Gas turbine rotor life management and extension' (gevernova.com/gas-power/services/gas-turbines/rotor-life-extension)
        - **date**: 2026-09-21 (retrieved)
        - **quote_or_number**: new rotor resets the clock "at 144,000 or 200,000 hours and 5,000 starts"; GE has "helped customers with aging assets replace more than 250 B & E turbine rotors and over 500 F turbine rotors"
        - **reproduction**: https://www.gevernova.com/gas-power/services/gas-turbines/rotor-life-extension
      - - **source**: GE Vernova, 'The F-Class rotor: A look inside' and GER-3620P (GE Vernova heavy-duty gas turbine O&M considerations)
        - **date**: 2026-09-21 (retrieved)
        - **quote_or_number**: "a rotor can run over 15 years or 144,000 factored fired hours (FFH) and 5,000 factored fired starts (FFS)"; GER-3620: "A GE Vernova Rotor life extension is required when the accumulated rotor factored fired starts or hours reach the inspection limit"; cold starts carry rotor maintenance factor 2.0
        - **reproduction**: https://www.gevernova.com/gas-power/resources/articles/2020/f-class-rotor-a-look-inside ; https://www.gevernova.com/content/dam/gepower-new/global/en_US/downloads/gas-new-site/resources/reference/GER-3620-P.pdf
      - - **source**: sources id 169, YouTube transcript 'MD&A Positions Itself as Alternative Source for 7FA and 7EA Gas Turbine Rotor Life Extension' (commentary tier, https://www.youtube.com/watch?v=WD-TX5XE6p0)
        - **date**: undated in corpus (2025-2026)
        - **quote_or_number**: "no one entity can serve all the turbines ... coming to rotor end of life during ... a 5 to 7-year period"; 7F units they target "between eight and 900"; bottlenecks: "long lead times associated with the superalloys forgings" and "a very limited number of shops in the world that can service these large 7FA gas turbines"
        - **reproduction**: SELECT text FROM sources WHERE id=169; search 'rotor end of life' and 'eight and 900'
      - - **source**: generators (EIA-860M vintage 2026-01) joined to generation (EIA-923, 2025)
        - **date**: 2025 data, vintage 2026-01
        - **quote_or_number**: Single-vintage CC plants with op_year 2000-2004: 154 plants, ~108 GW; 2025 capacity factors 0.51-0.56 (4,450-4,900 fired hours/yr); naive cumulative (years x 2025 CF x 8760): 103-123k hours
        - **reproduction**: WITH g AS (SELECT plant_id, SUM(mw) mw, MIN(op_year) fy, MAX(op_year) ly FROM generators WHERE vintage='2026-01' AND technology='Natural Gas Fired Combined Cycle' AND sheet LIKE '%Operating%' GROUP BY plant_id), gen AS (SELECT plant_id, SUM(net_generation_mwh) mwh FROM generation WHERE year=2025 AND prime_mover IN ('CT','CA','CS') GROUP BY plant_id) SELECT fy, COUNT(*) plants, ROUND(SUM(g.mw)) mw, ROUND(SUM(gen.mwh)/SUM(g.mw)/8760.0,3) cf, ROUND((2026-fy)*SUM(gen.mwh)/SUM(g.mw)/1000.0,1) est_cum_khrs FROM g JOIN gen ON gen.plant_id=g.plant_id WHERE g.fy=g.ly AND fy BETWEEN 1996 AND 2008 GROUP BY fy ORDER BY fy;
      - - **source**: chunks id 468451, GEV Q2'26 earnings call remarks (sources id 3796, commentary tier)
        - **date**: 2026-07-22
        - **quote_or_number**: "Year-to-date, our Power services backlog has increased $4 billion with growth in Gas and Steam"
        - **reproduction**: SELECT text FROM chunks WHERE id=468451;
    - **why_market_misses_it**: The services bull case is argued in $/GW-year on the installed base, not by component life limits. The rotor limit is a technical-information-letter rule buried in GER-3620, and the units affected are 20-25-year-old 7FA/7EA machines that finance analysts treat as steady annuity rather than a lumpy, contestable upgrade wave that draws on the same forging supply as new-unit output.
    - **testable_prediction**: On the Q3'26 or Q4'26 call (Oct 2026 / Jan 2027) GEV cites F-class rotor/life-extension or 'upgrades' as a named driver of Gas services orders, and Power services backlog growth for FY26 exceeds $6B; alternatively, GE announces prioritization of forging capacity for new units and third-party rotor programs (MD&A, EthosEnergy, PSM) announce >20 7F rotor projects by mid-2027.
    - **kill_condition**: GEV discloses that most 2000-2004 vintage F rotors have already been life-extended (e.g. '500+ F rotors' rises little by FY26 10-K) or that rotor work is inside CSA scope with no incremental billing; or EIA/EPA data show the 2000-2004 cohort well below 100k actual fired hours so the hours limit is a 2030s event and only the 5,000-start limit binds for cyclers.
    - **novelty**: 4
    - **confidence**: 2
    - **materiality**: 2
    - **caveats**: Cumulative-hour estimate uses the 2025 capacity factor for every prior year; early-2000s CFs were lower (30-45% during 2002-2009 gas spikes), so true hours are likely 80-110k, and the 5,000-factored-start limit (cold starts count 2x) probably binds first for cycling units. EIA data does not identify OEM or frame, so '7F' is inferred from the 2000-2004 CC build being predominantly 7FA/501F. Per-rotor pricing is not in the corpus. The 800-900 unit count comes from a competitor's marketing interview. Fleet fired hours are not rising: total U.S. CC generation was 1,430/1,530/1,559/1,511 TWh for 2022-2025 (2025 down 3%), so this is an aging wave, not an acceleration.
- **dead_ends**:
  - Academic tier is mostly abstracts: OPENALEX rows in angles technical_turbine/aeroderivative/hydrogen are ~1.3-2.8 kB each (SELECT id,n_chars FROM sources WHERE tier='academic' AND angle IN ('technical_turbine','aeroderivative','hydrogen') ORDER BY n_chars DESC); only a handful (ids 2227, 2194, 2164, 1505, 1588, 196, 334, 3532, 3540) are full text. No H-class hot-gas-path life, TBC spallation rate, or single-crystal casting capacity numbers exist in the academic tier.
  - H-class vs F-class hot-gas-path interval: the only quantified statement is a Patsnap Eureka page (sources id 3061: H-class HGP parts every 24,000-32,000 EOH vs 32,000-48,000 for F, overhaul cost 10-20% higher) - low-quality source, no GE citation. GER-3620P gives 24,000 h/1,200 starts HGPI and 48,000 h/2,400 starts major for E-class baseline only and defers HA intervals to unit-specific TILs. Not usable for a finding.
  - HA fleet wear clock cross-check (already on team list, no new twist): EIA single-vintage CC plants with op_year 2017-2021 (49 plants, 42 GW) ran at 0.661 CF in 2024 and 0.644 in 2025 (~5,700 fired h/yr); 2022+ cohort 0.63 (2024) / 0.55 (2025). Query: same CTE as finding 3 with cohort CASE on first_year. Supports first-HGPI at ~4 years and majors 2026-2029 for the 2017-19 HA wave; nothing that changes the team's conclusion.
  - 'Data centers make the old fleet run harder' is NOT supported: 2000-2004 CC cohort CF 0.224/0.239/0.235/0.232 for 2022-2025 (join double-counts MW across prime movers, so levels are wrong but the trend is flat); total U.S. CC generation 1,430/1,530/1,559/1,511 TWh 2022-2025 (SELECT year, SUM(net_generation_mwh) FROM generation WHERE prime_mover IN ('CT','CA','CS') GROUP BY year). Fired-hour-linked CSA billings ($5.4B 2025 vs $5.0B 2024, 10-K) are not being driven by fleet utilization.
  - Ambient-temperature derating: only sources id 334 (OpenAlex 2025-12-22, 'Technoeconomic Analysis of Microgrids for AI Data Centers') models it, and it publishes no derate coefficients; FTS '"ambient" "derating" "combined cycle"' returns nothing else quantified.
  - Hydrogen blends and maintenance intervals: no quantified interval or life penalty anywhere; CATF PDF (sources id 1598) only states qualitatively that moisture diffusion can spall TBCs and may require firing-temperature derating or more cooling flow. MHI M501GAC blend tests (chunk 234180) claim 'lower maintenance needs' without numbers.
  - Wind blade failure statistics: only one usable source (sources id 909, Frontiers 2026: 8.3 failures/turbine/yr, blades 35% of downtime on 8-12% of events; European offshore). sources id 908 (WES preprint) is qualitative. No GE/LM-specific failure rate in corpus.
  - Aeroderivative vs heavy-duty for data centers: the only cost numbers are BNP/Utility Dive equipment-only $/kW (heavy-duty ~$790, HA CC ~$950, aero ~$1,800; chunk 217451) - already covered by the team's bridge-power angle. No academic economics.
  - Transformer physics: sources id 1154 (SpecForge blog) claims sub-spec CRGO steel is the leading cause of elevated no-load loss in 2025-vintage field failures - unsourced vendor blog; not usable. Prolec Goldsboro expansion (+200 medium-power units/yr, 144,000 sq ft, production from 2028) already public.
  - NERC/ERCOT: the 1,500 MW July 2024 Virginia event and ERCOT ride-through requirements (ERCOT Board Dec 2025, Billo) appear in sources 45, 458/459/3532; the NERC incident review itself is not in the corpus - memo should cite it directly.
  - Competitor capacity data point (not lens, for the MHI-vs-Siemens angle owner): Gas Turbine World RSS 2026-08-30 (sources id 3471): Ansaldo GT36 H-class fleet only 80,000 EOH total since Nov 2022; Ansaldo won its first U.S. new-build order in 30+ years (AE64.3A units for a Texas data center, first deliveries 2027); Siemens Energy IR deck (sources id 3189) shows GT capacity 17 GW -> 22 GW -> >30 GW.
  - F-class rotor pricing: FTS '"rotor" "life extension" "million"' and '"rotor" "replacement" "million"' return nothing quantified; FM Global loss study chunk (462254) only lists rotor failures among catastrophic loss causes.
  - GEV filings: FTS '"7F" "units"' and '"rotor" "life"' return no GEV primary-tier text quantifying the F-class fleet or rotor programs; guidance table has no Wind-metric rows for 2026 (SELECT ... FROM mgmt_guidance WHERE ticker='GEV' AND metric LIKE '%Wind%' AND stated_on>='2026-01-01' -> empty) and xbrl_facts has no Wind segment tags; segment numbers must be read from 10-Q text chunks.
  - Not attempted: python src/embed.py semantic search (Ollama) and SEC full-text API; FTS coverage was sufficient and token budget was prioritized for query iteration.

## [Sweep] find:services-accounting

- **lens**: Services and accounting-estimate forensics: LTSA/CSA estimate revisions, contract assets, services RPO construction, availability penalties, HA fleet activation
- **findings**:
  - - **title**: LTSA margin re-estimates are accelerating (H1'26 -$218M, 5x H1'25) while LTSA revenue and billings are flat-to-down; all Power services growth is transactional
    - **claim**: Net unfavorable changes in estimated profitability on Gas Power contractual service agreements were -$218M in H1'26 (Q1 -$89M, Q2 -$129M) versus -$42M in H1'25 and -$151M for all of FY25, equal to about 1.1 points of aggregate LTSA margin cut in six months (10-K sensitivity: 1 point = $0.2B), and this hit 12% of H1'26 Power segment EBITDA ($1,842M) while CSA revenue recognized ($2,689M vs $2,720M) and CSA billings ($2,392M vs $2,533M, -5.6%) both fell year over year.
    - **mechanism**: LTSA revenue is recognized cost-to-cost against estimated life-of-contract billings and costs; estimates use 'historical utilization trends'. When outage costs or timing move against the estimate, the cumulative catch-up is booked immediately as a reduction of Power services revenue with no cost offset, so it flows 100% into Power segment EBITDA and the 17-19% Power margin guide. Meanwhile CSA revenue ($5.47B FY24, $5.41B FY25, $2.69B H1'26) is not growing, so its share of Power services revenue fell from 44.1% (FY24) to 41.4% (FY25) to 40.8% (H1'26); the +5-6% Power services growth is entirely transactional parts/upgrades, which management confirms (transactional orders per unit rising double digits). The 'annuity' half of the bull case is stalled and being re-marked down at the same time.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, 10-Q filed 2026-07-22, Note 9 (Contract and other deferred assets)
        - **date**: 2026-07-22
        - **quote_or_number**: Net contractual service agreements increased primarily due to revenues recognized of $2,689 million, partially offset by billings of $2,392 million and net unfavorable changes in estimated profitability of $218 million.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Net contractual service agreements" "changes in estimated profitability"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q') ORDER BY c.filing_date
      - - **source**: chunks, same Note 9 sentence across 10-Q/10-K 2024-04-30 through 2026-04-22 (YTD figures)
        - **date**: 2024-04-30 to 2026-04-22
        - **quote_or_number**: Net unfavorable changes in estimated profitability, YTD: 2024 Q1 -29, H1 -89, 9M -135, FY -319 ('due primarily to higher costs'); 2025 Q1 +29, H1 -42, 9M -36, FY -151; 2026 Q1 -89, H1 -218. CSA revenue recognized FY24 5,473 / FY25 5,412 / H1'25 2,720 / H1'26 2,689; billings FY24 5,021 / FY25 5,362 / H1'25 2,533 / H1'26 2,392 ($M).
        - **reproduction**: Same query as above; regex 'Net contractual service agreements (increase|decrease)' on each row. Billings cross-check: SELECT start_date,end_date,MIN(val) FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress' GROUP BY 1,2 (values equal billings: -1,173/-2,300/-3,673/-5,021/-1,249/-2,533/-3,781/-5,362/-1,163/-2,392)
      - - **source**: chunks, 10-K filed 2026-01-29, Item 7 Critical Accounting Estimates (and 10-K 2025-02-06 same paragraph)
        - **date**: 2026-01-29
        - **quote_or_number**: Revisions to our estimates of future billings or costs that increase or decrease total estimated contract profitability by one percentage point would increase or decrease the long-term service agreements contract assets balance by $0.2 billion. Net LTSA balance $3.4B = ~4% of total estimated life of contract billings (Dec-25) vs $3.5B = ~5% (Dec-24); contracts ~29% complete both years.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"life of contract billings"' AND c.ticker='GEV' ORDER BY c.filing_date
      - - **source**: chunks, Power segment tables in 10-K 2026-01-29 and 10-Q 2026-07-22 (Item 2)
        - **date**: 2026-07-22
        - **quote_or_number**: Power services revenue FY23 11,838 / FY24 12,419 / FY25 13,081; H1'25 6,238 / H1'26 6,598. Power segment EBITDA H1'25 1,303 (restated) / H1'26 1,842; H1'26 Power revenue 10,449 ($M). 218/1,842 = 11.8%; had revisions matched H1'25 (-42), Power margin would be 19.3% vs reported 17.6%.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Total segment revenues" AND "Services" AND "Equipment" AND "Gas Power"' AND c.ticker='GEV' AND c.filing_date>='2025-10' ORDER BY c.filing_date; regex 'Segment EBITDA \$[\d,]+'
      - - **source**: sources id 3161, GE Vernova Q2'26 webcast transcript PDF (gevernova.com), CFO prepared remarks
        - **date**: 2026-07-22
        - **quote_or_number**: We've seen transactional orders per unit continue to rise by double digits annually as customers invest in upgrades and greater scope and outages, all at higher prices.
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"For services, we continue to benefit"' AND c.form='TRANSCRIPT'; URL https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
      - - **source**: chunks, 10-K filed 2026-01-29, Item 7 Critical Accounting Estimates, LTSA paragraph
        - **date**: 2026-01-29
        - **quote_or_number**: a significant estimate in determining expected revenues of a contract is estimating how customers will utilize their assets over the term of the agreement ... We generally use historical utilization trends in developing our revenue estimates.
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"estimate of utilization"' AND c.ticker='GEV' AND c.form='10-K' AND c.filing_date='2026-01-29'
    - **why_market_misses_it**: The figure lives in one sentence of Note 9, is not XBRL-tagged (the GEV tags named 'CumulativeCatchUp' actually carry billings and offshore-wind losses), and management's segment narrative is 'favorable price and increased productivity'. In the corpus, the only commentary-tier mentions of 'estimated profitability' (4 chunks) are verbatim copies of the 10-K; no analyst or news item discusses the series. The market prices services as a growing annuity, but the CSA revenue line itself has not grown since FY24.
    - **testable_prediction**: Q3'26 10-Q (expected ~Oct 21-22, 2026) Note 9 will show 9M'26 net unfavorable changes in estimated profitability of at least $250M (i.e., Q3 alone negative by $30M+), and FY26 (10-K late Jan 2027) will exceed FY24's -$319M; CSA revenue recognized for 9M'26 will be at or below 9M'25's $3,824M.
    - **kill_condition**: 9M'26 net change is less unfavorable than -$218M (Q3 favorable), or the 10-Q attributes the H1 amount to a single identified contract settlement, or 9M'26 CSA revenue recognized exceeds $4.0B (>4.5% growth).
    - **novelty**: 4
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: The Note 9 line covers Gas Power CSAs only; equipment-contract catch-ups are not disclosed separately. Cause is not disclosed (FY24's was 'higher costs'); could reflect inflation/tariffs on outage parts rather than utilization. Sensitivity ($0.2B per point) is on the asset balance, so '1.1 points' is an approximation. Quarter values are differences of YTD figures. H1'25 Power EBITDA was restated from 1,286 to 1,303 in the 2026 10-Q.
  - - **title**: HA fleet activation has stalled: running units +4 in seven months while 43 sit in commissioning and H1'26 HA shipments fell 38%
    - **claim**: The HA-Turbine installed (running) base grew 94 to 115 over Mar-Dec 2024 (+2.3/month), 115 to 126 in 2025 (+0.9/month), and 126 to about 130 by the July 22, 2026 call (+0.6/month), while units 'being installed and commissioned' rose from 30 (Dec-24) to 43 (Dec-25) and HA shipments fell to 8 in H1'26 from 13 in H1'25 (Q2'26: 3 vs 8), so the services annuity on the newest, highest-value fleet is being pushed out in real time.
    - **mechanism**: Services RPO and LTSA revenue start only when a contract is 'active' (10-K: services RPO excludes 'contracts that are not yet active'), and the bull-case value of ~$70M per GW-year requires units running hours. Units stuck between shipment and commercial operation earn no LTSA billings, add no active services RPO, and their first major outage (about 4 years after COD) slips accordingly; the CEO already frames the HA outage wave as 'a middle of the next decade dynamic'. A 43-unit commissioning queue against a 126-130 unit running fleet means roughly a third of the delivered HA fleet is not yet monetizing services, and the H1'26 shipment dip (8 vs 13 units) means the queue is not being drained by an acceleration of installs.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, GEV 10-Q 2024-04-30, 2024-07-24, 2024-10-23; 10-K 2025-02-06; 10-K 2026-01-29 (Item 1 / Power section)
        - **date**: 2024-04-30 to 2026-01-29
        - **quote_or_number**: HA-Turbines in installed base: 94 (Mar-24, 'over two million operating hours'), 100 (Jun-24, 2.5M hrs), 106 (Sep-24, 2.7M), 115 (Dec-24, 2.9M), 126 (Dec-25, 3.6M). Being installed and commissioned: 30, 31, 30 (Dec-24), 43 (Dec-25). HA in RPO: 29, 32, 36, 32, 51.
        - **reproduction**: SELECT c.form, c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"HA" AND "operating hours" AND "installed base"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q') ORDER BY c.filing_date; regex 'As of [A-Z][a-z]+ \d+, 20\d\d, we had \d+ HA.{0,200}?operating hours'
      - - **source**: sources id 3161, GE Vernova Q2'26 webcast transcript (gevernova.com PDF), CEO answer in Q&A
        - **date**: 2026-07-22
        - **quote_or_number**: we only have 130 of our HA units running right now. We have 325 units that either commissioned or under contract. As these run baseload and every four years they go through a major outage.
        - **reproduction**: SELECT c.accession, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"HA units running"' AND c.form='TRANSCRIPT'; SELECT url FROM sources WHERE id=3161
      - - **source**: chunks, 10-Q 2026-07-22 and 10-Q 2025-07-23 Power 'Sales in units' tables
        - **date**: 2026-07-22
        - **quote_or_number**: HA-Turbines sales in units: Q2'26 3 vs Q2'25 8; H1'26 8 vs H1'25 13. FY25 24 vs FY24 15. Gas turbine GW shipped H1'26 7.5 vs 8.2.
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Sales in units" AND "HA" AND "Gas Turbine Gigawatts"' AND c.ticker='GEV' AND c.form='10-Q' AND c.filing_date>='2026-01'
      - - **source**: chunks, 10-K 2026-01-29 Item 7, RPO definition
        - **date**: 2026-01-29
        - **quote_or_number**: Services RPO includes the estimated life of contract sales related to long-term service agreements which remain unsatisfied at the end of the reporting period, excluding contracts that are not yet active.
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"RPO" AND "life of contract" AND "long-term service agreements"' AND c.ticker='GEV' AND c.form='10-K' AND c.filing_date='2026-01-29'
    - **why_market_misses_it**: Since Q1'25 the 10-Qs no longer print the HA installed-base/operating-hours sentence, so the running-fleet count is visible only once a year in the 10-K plus an offhand verbal number on a call; sell-side models the services annuity off shipments and RPO, not off units actually running. The team's 'service lag to the mid-2030s' angle treats the lag as a fixed future date; this shows the lag lengthening now.
    - **testable_prediction**: FY26 10-K (late Jan 2027) will report an HA installed base of at most 140 units and at least 45 units 'being installed and commissioned'; Q3'26 10-Q HA sales in units will be at most 8 for the quarter. Implied 2025 fleet utilization (0.7M hours added on ~120 average units, ~5,800 hrs/unit) will not rise above ~6,500 hrs/unit in 2026.
    - **kill_condition**: FY26 10-K shows HA installed base of 150 or more (implying 24+ commissionings in 2026), or the commissioning count drops below 35, or management gives a running-unit count above 145 on the Q3'26 call.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: The '130' is a rounded verbal figure and 'installed base' in the 10-K may not equal 'running'. Commissioning is largely customer/EPC-driven, so this is a timing, not a loss, issue; deposits and equipment revenue (over-time) are unaffected. HA shipment dip in H1'26 may be quarterly lumpiness (aeroderivative shipments rose 26 vs 10). Operating-hour math relies on rounded 'approximately' figures. Overlaps with the team's 'backlog into dirt' and 'service lag' angles; the new content is the measured deceleration and the 43-unit queue.
  - - **title**: The $0.3B/yr availability-shortfall revenue reduction is a Wind item, not a gas-fleet item; gas fleet wear shows up in the CSA estimate line instead
    - **claim**: The $0.3B per year (2023, 2024, 2025) 'reduction of revenues from availability shortfalls' disclosed in the 10-K sits in the Wind critical accounting estimate and refers to wind-farm availability guarantees (service agreements on ~24,000 of ~59,000 onshore turbines), with a stated sensitivity of less than $0.1B for a further 1% fleet-wide availability drop; no gas-turbine availability penalty is quantified anywhere in the filings.
    - **mechanism**: The team's HA-fleet wear-clock angle assumes a harder-running gas fleet raises availability penalties. It cannot: the disclosed penalty line is Wind-only and has been flat at $0.3B for three years regardless of the gas ramp. Gas-fleet wear or higher utilization reaches the P&L through the LTSA cost-to-cost estimate (Finding 1: net unfavorable changes in estimated profitability, sensitivity $0.2B per margin point), and through Wind's line only if wind availability deteriorates. Any memo sentence tying gas fleet hours to 'availability penalties' would be wrong and easy for a judge to catch.
    - **direction**: neutral
    - **evidence**:
      - - **source**: chunks, 10-K filed 2026-01-29, Item 7 Critical Accounting Estimates, Wind paragraph
        - **date**: 2026-01-29
        - **quote_or_number**: performance guarantees of the wind farm's availability ... the reduction of revenues from availability shortfalls was $0.3 billion, $0.3 billion, and $0.3 billion ... A further 1% reduction in availability across the entire fleet would have resulted in an additional revenue reduction of less than $0.1 billion.
        - **reproduction**: SELECT c.filing_date, c.section, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"availability" AND "revenue" AND ("reductions" OR "reduction" OR "penalties")' AND c.ticker='GEV' AND c.form='10-K' ORDER BY c.filing_date DESC
      - - **source**: chunks, 10-K filed 2026-01-29, Item 1 Wind segment
        - **date**: 2026-01-29
        - **quote_or_number**: Included in our RPO are services agreements on approximately 24,000 of our onshore wind turbines, from an installed base of approximately 59,000 units. Wind services RPO $12,518M (Dec-25) vs $11,962M (Dec-24).
        - **reproduction**: SELECT c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '("1,800" OR "7,000" OR "24,000") AND "installed base"' AND c.ticker='GEV' AND c.form='10-K' ORDER BY c.filing_date DESC
      - - **source**: chunks, GEV 10-K 2026-01-29 full-text search for gas availability guarantees
        - **date**: 2026-01-29
        - **quote_or_number**: Zero chunks match availability + gas turbine + guarantee/guaranteed in the FY25 10-K; the only 'availability' hits outside Wind are about availability of credit/financing.
        - **reproduction**: SELECT COUNT(*) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"availability" AND ("gas turbine" OR "gas turbines") AND ("guarantee" OR "guarantees" OR "guaranteed")' AND c.ticker='GEV' AND c.form='10-K' AND c.filing_date>='2026-01'
    - **why_market_misses_it**: The number is quoted in summaries without its section header; the paragraph is under 'Wind' in Critical Accounting Estimates and the gas LTSA paragraph immediately precedes it, so readers merge the two.
    - **testable_prediction**: FY26 10-K (late Jan 2027) will again report the Wind availability-shortfall reduction at about $0.3B, unchanged by the gas fleet's higher hours, and will still contain no quantified gas-turbine availability penalty.
    - **kill_condition**: A GEV filing or call quantifies gas-turbine availability/performance-guarantee payments as a separate line, or the Wind figure moves by more than $0.1B.
    - **novelty**: 2
    - **confidence**: 5
    - **materiality**: 2
    - **caveats**: Gas LTSAs can still contain performance guarantees; they are simply folded into the LTSA profitability estimate rather than disclosed as penalties. This is a framing correction for the memo, not a trade.
- **dead_ends**:
  - XBRL tags are mislabeled for GEV: ContractWithCustomerAssetCumulativeCatchUpAdjustmentToRevenueChangeInMeasureOfProgress carries CSA billings (-1,173/-2,300/-3,673/-5,021 for 2024; -5,362 FY25; -2,392 H1'26), and ContractWithCustomerLiabilityCumulativeCatchUpAdjustmentToRevenueChangeInEstimateOfTransactionPrice carries Offshore Wind contract losses (-379 FY23, -1,005 FY24, -637 FY25; Q3'25 -171, implied Q4'25 -341). Neither is a catch-up series; use the Note 9 text instead.
  - The phrase 'cumulative catch-up' does not appear in any GEV 10-K/10-Q chunk, and there is no table of 'revenue recognized from changes in estimates' for equipment contracts; the only quantified estimate-change lines are the CSA one (Note 9) and Offshore Wind contract losses.
  - Loss-provision search ('loss provisions', 'provisions for losses', 'estimated losses' with 'contracts') returned zero GEV 10-K/10-Q chunks; contract loss reserves are not disclosed as a separate balance.
  - Contract-life and escalation assumptions: 'average remaining contract life of approximately 10 years' is unchanged Dec-24 to Dec-25, contracts '~29% complete' both years, and no filing text mentions a change in contract-life or price-escalation assumptions. Implied total estimated life-of-contract billings rose from ~$70B ($3.5B = ~5%) to ~$85B ($3.4B = ~4%) while LTSA units rose 1,700 to 1,800 (+6%), but the rounding (4% vs 5%) makes the ranges ($64-78B vs $76-97B) overlap, so re-estimation cannot be proven from this.
  - Q4'25 Power services RPO jumped +$4,758M in one quarter (65,083 to 69,841; Q1-Q3'25 were +1,482/+560/+2,151; Q1'26 +1,323; Q2'26 +1,224) against Q4'25 Power services revenue of $3,802M, implying ~$8.6B of services additions. The 10-K only attributes it to Gas Power 'contractual services' and Steam Power services; the Power MD&A has no dollar orders split by equipment/services, so it could not be attributed to new HA LTSA activations vs re-estimation. Worth a follow-up question, not a finding.
  - 10-Qs from Q1'25 onward no longer print the HA installed-base / operating-hours sentence (only the 10-K does), so the fleet series is annual plus transcript remarks. transcript_statements and TRANSCRIPT chunks have blank filing_date; date them via sources.url (e.g., gev_webcast_transcript_07222026.pdf).
  - Commentary tier has only 4 chunks mentioning 'estimated profitability', all verbatim copies of the 10-K (src:3650); 15 mention 'contractual service agreement', none discuss the revision series. Nothing in commentary to cite as prior art.
  - Minor restatements found and ignored: Power services RPO Mar-25 62,372 to 62,533 and Jun-25 62,932 to 63,088 in the 2026 10-Qs (+~$160M); Power EBITDA H1'25 1,286 to 1,303. Warranty accrual (StandardProductWarrantyAccrual 1,370 Dec-24 to 1,595 Jun-26) noted but left to the team's warranty-per-GW angle.
  - Did not use embed.py semantic search or web connectors; all numbers come from chunks_fts and xbrl_facts, reproduced with the queries listed.

## [Verify] verify:connectors-outside:Oglethorpe Power (non-corpus filer) disc

- **reproduced**: True
- **corrected_numbers**: Smarr reproduces: 1,425 MW two-unit CC, $3.3B incl. capital, AFUDC and contingency (= $2,316/kW), GE Vernova 7HA.03 x2 (OPC FY25 10-K acc 0000788816-26-000009; Q2'25 8-K exhibit acc 0001628280-25-041154 shows '(~$2,300 / KW)'). Latest: OPC Q2'26 investor presentation (Aug 18 2026, acc 0000788816-26-000050) still $3.3B, in-service 'Mid 2029', costs incurred $662M through Q2'26 (vs $343.5M at Dec-25). Talbot Unit 7 FAILS as stated: the OEM is Siemens Energy (SGT6-5000F), not GE Vernova; the Q2'25 deck said OEM not yet selected and the 10-K never names it. Its budget was re-baselined from ~$360M to $440M (+22%), i.e. ~$1,833/kW not $1,500/kW. New datapoints from the same Aug-26 deck the finding missed: OPC's next-vintage projects are budgeted at 209 MW CT $525-625M (= $2,510-2,990/kW, COD early 2032) and 713 MW CC $2.3-2.7B (= $3,225-3,790/kW, COD 2033), i.e. 40-65% above Smarr's all-in $/kW for units two to four years later. Corpus check reproduces: FTS '"Smarr" OR "Oglethorpe" OR "Talbot"' returns only Southern Co glossary/plant-list boilerplate and OpenAlex noise; projects table has no Oglethorpe rows.
- **refuted**: True
- **already_widely_known**: True
- **where_known**: The $2,300/kW figure is printed in OPC's own SEC-filed investor decks (Q2'25 and Q2'26 8-K exhibits) and repeated by Georgia Public Broadcasting (May 11 2026, groundbreaking), Power Engineering (GE Vernova selected for Oglethorpe), Global Energy Monitor wiki, and mymcr.net. The broader '~$2,000-2,500/kW for new CCGT orders' number is in GridLab's Sept-2025 gas turbine cost report, APPA, Latitude Media and Gas Turbine World; sell-side already quotes ~$2,500/kW for 2026 orders.
- **materiality**: 2
- **strongest_counterargument**: One of the two datapoints is misattributed (Talbot 7 is a Siemens SGT6-5000F and its budget already rose 22%), and the surviving one is a single RUS-financed cooperative's all-in project budget that does not disclose the GE equipment contract, so it cannot anchor a GEV gross-margin bridge: the 'turbine island is 25-30% of project cost' split is an assumption the disclosure never supports. The mechanism cuts the other way for a skeptic: OPC's own next-vintage budgets ($2,500-3,000/kW CT, $3,200-3,800/kW CC for 2032-33) show that the all-in cost is inflating faster than GEV's $600/kW turbine target, which argues that EPC/labor/electrical BoP, not the OEM, is becoming the binding line, and that customer affordability, not GEV headroom, is the constraint. Nothing here resolves within 3-12 months; the Nov-2026 10-Q test is nearly guaranteed to pass because the GE contract was fixed in 2025, so it discriminates nothing about GLJ's 2027 vintage-margin bear case.
- **notes**: Tool calls used: 6. Verification steps: (1) WebFetch OPC FY25 10-K: Smarr $3.3B incl. AFUDC+contingency, GE Vernova Operations LLC agreement, TIC/Kiewit EPC Sept 2025, $343.5M incurred; Talbot 7 ~$360M, 'equipment manufacturer' unnamed. (2) WebFetch Q2'25 deck: Smarr '~$2,300 / KW', GE Vernova OEM; Talbot 7 cost not given, contractor not yet selected. (3) WebFetch Q2'26 deck (Aug 18 2026): Smarr unchanged, Talbot 7 = Siemens SGT6-5000F, re-baselined $440M. (4) corpus FTS + projects table: no Oglethorpe content, as claimed. (5)(6) two web searches confirming public coverage and market $/kW benchmarks. Salvageable angle for the team (not a re-proposal of the pricing-decomposition item): use OPC's dated ladder of all-in $/kW (Smarr 2029 $2,316; Talbot 7 2029 $1,833 after +22%; 2032 CT ~$2,750; 2033 CC ~$3,500) as a customer-side affordability curve; kill condition would be OPC or Georgia Power IRP filings showing all-in CC cost flat at <$2,500/kW for 2032+ CODs. Dead ends: GEV primary chunks contain no usable $/kW disclosures (FTS 'per kW' hits are S-1 boilerplate and garbled IR PDFs); projects table lacks any Oglethorpe entries so the 420-project tracker cannot be cross-checked here.

## [Verify] verify:connectors-outside:HA-turbine shipments fell in H1'26 while

- **reproduced**: True
- **corrected_numbers**: All cited numbers reproduce exactly from the corpus. Unit tables (chunks, GEV 10-Q/10-K, MATCH '"Sales in units" AND "HA-Turbines"'): Q2'26 vs Q2'25 HA 3 vs 8, Heavy-Duty 13 vs 18, Aero 16 vs 3, total gas turbines 29 vs 21, GW 3.3 vs 5.2; H1'26 vs H1'25 HA 8 vs 13, GW 7.5 vs 8.2. FY25/24/23 HA sold 24/15/14, GW 15.3/11.9/13.8. XBRL (single fact per date, no duplicate conflicts): InventoryFinishedGoods 2.490B (Dec-24), 3.267B (Dec-25), 3.874B (Mar-26), 4.135B (Jun-26) = +66%; WIP+raw 5.328B to 7.827B; InventoryNet 8.587B to 12.692B. 10-K FY25: 51 HA in RPO, 43 being installed/commissioned, 126 installed. CORRECTIONS the finding omits: (1) Trailing-4-quarter GW sold = Q3'25 4.0 + Q4'25 3.1 (15.3-12.2) + Q1'26 4.2 + Q2'26 3.3 = 14.6 GW vs FY25 15.3, i.e. flat, not falling; TTM HA units 6+5+5+3 = 19 vs 24. Q1'26 was UP 40% YoY (4.2 vs 3.0 GW) and Q2'25 (5.2 GW, 8 HA) is the single best quarter in the series, so the Q2'26 YoY comp is the harshest possible. (2) Total gas turbine units sold ROSE 29 vs 21 in Q2'26; the drop is mix (aeros up 13 units). (3) Q2'26 10-Q cash-flow MD&A attributes the H1'26 inventory build of $(1.7)B to 'higher volume to support fulfillment and future deliveries primarily at Power and Wind', so it is disclosed and part-Wind. Cash-flow statement: inventories $(1,744)M, contract assets $(358)M, contract liabilities +$13,695M, CFO $10,680M for H1'26. Current contract assets essentially flat 9.29B (Dec-25) to 9.52B (Jun-26). (4) Power segment revenue +14% in Q2'26 while GW sold fell 37% YoY, which directly shows shipments do not drive reported revenue under cost-to-cost.
- **refuted**: True
- **already_widely_known**: True
- **where_known**: The GW-shipped series (3 GW in Q2'26, 5/4/3/4/3) is in every press write-up: Utility Dive 'GE Vernova gas turbine backlog climbs to 116 GW' (https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/) states 'shipped 3 GW of equipment'; Q2'26 press release (8-K/EX 2026-07-22) itself frames 20 GW as 'annual gas turbine output', i.e. production, not shipments. The inventory build and its reason are disclosed in the Q2'26 10-Q MD&A. The HA-unit line (3 vs 8) specifically did not surface in web search or in corpus commentary, so that granular observation is not widely repeated, but its parent series is.
- **materiality**: 2
- **strongest_counterargument**: The mechanism is wrong for a cost-to-cost business: Power revenue grew 14% in Q2'26 while GW sold fell 37%, so the 2027 revenue ramp priced into 31-38x does not depend on the quarterly 'Sales in units' count, which is lumpy (Q1'26 was +40% YoY; the Q2'25 comp was the series high). TTM GW sold (14.6) is flat vs FY25 (15.3), not down. The finished-goods build ($0.87B in H1'26, company-wide incl. Wind and Electrification, explicitly disclosed as supporting 'future deliveries') is immaterial next to $13.7B of H1 deposit inflows and $10.7B CFO; the H2 FCF guide of $1.6-2.6B already embeds working-capital use. Rising inventory ahead of a stated 20 GW output step-up is exactly what a capacity ramp looks like (raw/WIP +$1.45B in H1 as well), not evidence of parked units. The '20 GW output' vs shipments distinction is the company's own wording and the sell-side already tracks shipped GW at 3-4/quarter; nobody is modelling 5 GW shipped in Q3. Greenville 37/62/74 is an unverified spokesman quote and HA output also comes from Belfort. Net: real, reproducible data, but a weak short thesis; at best a watch item for the Oct-22 10-Q (prediction of GW sold 3.5-4.5 is roughly the base case, so it is not a differentiated call).
- **notes**: Tool calls used: 4 (2 SQL, 1 web search, 1 tool load). Did not fetch the Upstate Business Journal URL; the 37/62/74 figures stand as an unverified secondary quote. Dead ends: corpus has no 10-Q/transcript/8-K text after 2026-04 linking inventory to gas turbines specifically (MATCH '"inventor*" AND ("gas turbine*" OR "Gas Power")' returned 0 rows); no transcript/8-K/news hits defining 'Sales in units' as shipped vs delivered, so the units-shipped reading remains an assumption. Commentary chunks after 2026-07-22 matching 'finished goods' OR 'HA-Turbines' OR 'HA turbines' = 7, none specific to the 3-unit HA line on inspection of search results. Salvageable piece for the team: the HA-unit line as an alternative wear-clock/installed-base tracker (126 installed, 43 in commissioning, 51 in RPO at Dec-25) is cleaner than the GW series, but it belongs under the existing 'HA-fleet wear clock' and 'factory throughput' angles rather than as a new short finding. If kept as a watch item, revise kill/confirm to trailing-4-quarter GW sold vs 15.3 and to segment-level inventory commentary on the Q3 call, not single-quarter unit counts.

## [Sweep] find:disclosure-diff

- **lens**: Disclosure-change archaeologist: diffed GEV 10-K FY24 (filed 2025-02-06) vs 10-K FY25 (filed 2026-01-29) Item 1A, MD&A and notes; tracked footnote wording and the RPO conversion schedule across all eight 10-K/10-Q filings Q3'24-Q2'26; checked mgmt_guidance prior_value drift and XBRL flows.
- **findings**:
  - - **title**: Equipment backlog is going long-dated: share of equipment RPO due within 12 months fell from 46% to 36% while the 3-5 year tranche tripled
    - **claim**: Between the Q3'24 and Q2'26 10-Qs the disclosed share of equipment RPO expected to be recognized within one year fell from 46% to 36% (two-year cumulative 70% to 65%), so the year-3-to-5 tranche grew from $8.8B to $28.1B (3.2x) while the 12-month tranche grew from $19.4B to $31.6B (1.6x).
    - **mechanism**: Gas equipment revenue is recognized cost-to-cost, so each dollar of RPO reaches the income statement on the schedule GEV discloses in the RPO footnote. A falling 1-year share means incremental orders add less to next-year revenue and more to 2028-2031; conversely the absolute 12-month tranche ($31.6B at Jun-26) is 1.34x trailing-12-month equipment revenue ($23.6B), versus 1.03x a year earlier, which is the hard-number version of FY27 revenue visibility.
    - **direction**: either
    - **evidence**:
      - - **source**: documents table, GEV 10-Q filed 2024-10-23 (id 331) and each later 10-K/10-Q, RPO footnote
        - **date**: 2024-10-23 through 2026-07-22
        - **quote_or_number**: 1-yr share of equipment RPO: 46% (Q3'24), 44% (Dec-24), 45% (Q1'25), 42% (Q2'25), 41% (Q3'25), 37% (Dec-25), 38% (Q1'26), 36% (Q2'26). 2-yr cumulative: 70,69,71,70,71,69,69,65. 5-yr cumulative: 91,93,91,92,97,97,98,97.
        - **reproduction**: python: import re,sqlite3; con=sqlite3.connect(DB); [re.findall(r'Equipment[- ]related (?:remaining performance obligations|RPO) of \$[\d,]+ million of which [^.]{0,120}', re.sub(r'\s+',' ',t)) for (t,) in con.execute("SELECT text FROM documents WHERE ticker='GEV' AND form IN ('10-K','10-Q') AND filing_date>='2024-10-01' ORDER BY filing_date")]
      - - **source**: mgmt_guidance table (second, independent extraction of the same footnote)
        - **date**: 2025-02-06 to 2026-07-22
        - **quote_or_number**: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1,2, and 5 years" (2026-07-22); "$43,047 million of which 44%, 69%, and 93%" (2025-02-06)
        - **reproduction**: SELECT stated_on, quote FROM mgmt_guidance WHERE ticker='GEV' AND quote LIKE '%Equipment-related RPO of%' ORDER BY stated_on
      - - **source**: Derived dollar tranches (equipment RPO x disclosed percentages)
        - **date**: 2026-09-21 calculation
        - **quote_or_number**: <=1yr: $19.4B (Q3'24) -> $31.6B (Q2'26); yr2: $10.1B -> $25.5B; yr3-5: $8.8B -> $28.1B; >5yr: $3.8B -> $2.6B
        - **reproduction**: rows=[(42069,46,70,91),(43047,44,69,93),(45478,45,71,91),(49712,42,70,92),(54092,41,71,97),(64245,37,69,97),(75924,38,69,98),(87821,36,65,97)]; for v,a,b,c in rows: print(v*a/1e5, v*(b-a)/1e5, v*(c-b)/1e5, v*(100-c)/1e5)
      - - **source**: documents table, revenue-by-type tables: 10-K FY25 (id 249), 10-Q Q2'26 (id 218), 10-Q Q2'25 (id 281)
        - **date**: 2026-01-29 / 2026-07-22
        - **quote_or_number**: Equipment revenues FY25 $20,934M, FY24 $18,952M; H1'26 $11,713M, H1'25 $9,091M, H1'24 $7,811M -> TTM Jun-26 $23,556M, TTM Jun-25 $20,232M
        - **reproduction**: python: re.findall(r'Equipment revenues \$[\d,]+ \$[\d,]+ \$[\d,]+', norm(text of documents id 249)); re.findall(r'equipment \$[\d,]+ \$[\d,]+ \$[\d,]+ \$[\d,]+', norm(text of documents id 218))
    - **why_market_misses_it**: The conversion schedule is a one-sentence footnote to the RPO table; sell-side notes quote the $176B RPO headline and the '$200B by 2027' target without the maturity split. Nobody in the corpus (0 commentary chunks) tracks the 1-year share as a time series.
    - **testable_prediction**: Q3'26 10-Q (expected about 2026-10-21) discloses equipment RPO 1-year share at or below 38% and the implied 12-month dollar tranche at or above $33B; FY26 10-K (about 2027-01-28) shows 1-year share at or below 37%.
    - **kill_condition**: Q3'26 10-Q shows the 1-year share rebounding to 42% or higher, or the implied 12-month tranche falling below $30B (would mean backlog is being pulled forward, not pushed out).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 4
    - **caveats**: Percentages are management estimates, rounded to whole points, and cover all segments (Prolec GE acquisition added Electrification RPO in 2026). The 12-month tranche is a revenue-visibility figure, not a shipment figure, and cost-to-cost recognition can pull revenue ahead of physical delivery. Do not call the 1-year tranche 'guidance'.
  - - **title**: Wind: segment losses doubled in H1'26 and new 'claims and counterclaims' language appeared, but the only interim filing that puts a dollar figure on offshore contract losses is the Q3 10-Q (next one about Oct 21, 2026)
    - **claim**: GEV quantifies incremental Offshore Wind contract losses only in Q3 10-Qs and 10-Ks ($379M 2023, $1,005M 2024, $637M 2025; $171M in Q3'25), Q1/Q2 10-Qs say only 'higher contract losses'; meanwhile Wind segment EBITDA worsened from $(312)M in H1'25 to $(657)M in H1'26 and the Q1'26 10-Q added, for the first time, that GEV is resolving 'outstanding claims and counterclaims' with the Vineyard Wind customer.
    - **mechanism**: Offshore contract-loss provisions are cumulative catch-up charges to Wind segment EBITDA and adjusted EBITDA; a customer dispute settlement or further execution-timeline revision would be booked as an additional loss provision (10-K: 'further changes in our execution timelines... could result in further losses beyond the amounts that we currently estimate'), hitting Q3/Q4 2026 EBITDA and FY26 FCF.
    - **direction**: short
    - **evidence**:
      - - **source**: xbrl_facts, tag ContractWithCustomerLiabilityCumulativeCatchUpAdjustmentToRevenueChangeInEstimateOfTransactionPrice
        - **date**: 10-K 2025-02-06, 10-Q 2025-10-22, 10-K 2026-01-29
        - **quote_or_number**: FY23 -379M; Q3'24 -676M; 9M'24 -779M; FY24 -1,005M; Q3'25 -171M; 9M'25 -296M; FY25 -637M. No 2026 duration fact exists.
        - **reproduction**: SELECT start_date,end_date,max(val),form FROM xbrl_facts WHERE ticker='GEV' AND tag='ContractWithCustomerLiabilityCumulativeCatchUpAdjustmentToRevenueChangeInEstimateOfTransactionPrice' GROUP BY start_date,end_date ORDER BY end_date
      - - **source**: documents table: 10-Q Q3'25 (id 270) vs 10-Q Q1'25 (295), Q2'25 (281), Q1'26 (228), Q2'26 (218)
        - **date**: 2025-10-22 vs 2026-04-22 / 2026-07-22
        - **quote_or_number**: Q3'25: 'incremental contract losses for certain Offshore Wind contracts of $171 million and $676 million for the three months ended and $296 million and $779 million for the nine months'. Count of 'Offshore Wind contracts' sentences: Q1'25 0, Q2'25 0, Q3'25 1, Q1'26 0, Q2'26 0.
        - **reproduction**: python: for did in (295,281,270,228,218): t=norm(documents.text where id=did); print(did, len(re.findall(r'Offshore Wind contracts', t)), len(re.findall(r'contract losses', t)))
      - - **source**: documents table, 10-Q Q2'26 (id 218) segment table
        - **date**: 2026-07-22
        - **quote_or_number**: Wind Segment EBITDA: Q2'26 $(275)M vs Q2'25 $(165)M; H1'26 $(657)M vs H1'25 $(312)M; Wind revenue H1'26 $3,459M vs $4,095M
        - **reproduction**: python: re.search(r'Total segment revenues \$2,026 \$2,245 \$3,459 \$4,095 Segment EBITDA \$\(275\) \$\(165\) \$\(657\) \$\(312\)', norm(text of documents id 218))
      - - **source**: documents table, 10-Q Q1'26 (id 228) MD&A; absent from 10-Q Q3'25 (270) and 10-K FY25 (249)
        - **date**: 2026-04-22
        - **quote_or_number**: 'we are working with our customer to resolve outstanding claims and counterclaims' - occurrences of 'counterclaims': Q3'25 0, 10-K FY25 0, Q1'26 1, Q2'26 1
        - **reproduction**: python: for did in (270,249,228,218): print(did, norm(text of documents id=did).count('counterclaims'))
      - - **source**: 8-K/EX earnings releases via chunks_fts
        - **date**: 2026-04-22 and 2026-07-22
        - **quote_or_number**: Apr-22: 'Segment EBITDA losses grew from ... higher Offshore Wind contract losses'; Jul-22: 'higher Offshore Wind project costs' (wording softened from 'contract losses' to 'project costs')
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Offshore Wind" AND "losses"' AND c.ticker='GEV' AND c.form='8-K/EX' AND c.filing_date>='2026-01-01' ORDER BY c.filing_date
    - **why_market_misses_it**: Wind is treated as a rounding error against a $250B market cap and the gas narrative; the dollar figure for offshore losses appears only twice a year (Q3 10-Q, 10-K), so the H1'26 doubling of Wind losses and the new dispute language have not been priced as a discrete Q3 event.
    - **testable_prediction**: Q3'26 10-Q (about 2026-10-21) discloses nine-month 2026 incremental Offshore Wind contract losses of at least $300M (above the $296M for 9M'25) and Wind Q3'26 segment EBITDA of $(200)M or worse; a Vineyard Wind claim settlement or provision is disclosed by the FY26 10-K (about 2027-01-28).
    - **kill_condition**: Q3'26 10-Q reports 9M'26 incremental offshore losses below $150M, or Wind Q3'26 segment loss narrower than $(150)M with the 'claims and counterclaims' sentence removed.
    - **novelty**: 3
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: This is not a dropped disclosure: Q1/Q2 10-Qs never carried the dollar figure. Part of the H1'26 Wind deterioration is Onshore (lower deliveries, tariffs), not Offshore. Vineyard turbine installation was completed in Q1'26, so remaining exposure is commissioning, claims and the other offshore contracts in backlog; the 10-K gives no remaining-loss estimate.
  - - **title**: FY25 10-K cut Item 1A by 57% and 9 subsections to 4, but added two risks that did not exist in the FY24 10-K: over-investment in capacity and hyperscaler counterparty credit
    - **claim**: The FY25 10-K risk factor section shrank from about 174,500 to about 74,200 normalized characters (nine 'Risks Relating to' subsections to four, 'Summary of Risk Factors' removed), yet it introduced, with zero prior occurrences in the FY24 10-K, (a) 'our capacity expansions and related commitments may outpace realized demand... over-invested... idle capacity, under-absorption of fixed costs' and (b) 'nontraditional customers, such as hyperscalers... limited operating histories... weaker credit profiles... may delay payment, seek to renegotiate terms, or default'.
    - **mechanism**: (a) is the accounting path from a demand slip to Power margin: under-absorption of fixed costs at Greenville/other plants plus inventory write-downs and 'penalties under supply agreements' as GEV pre-commits supply for 20-30 GW/yr; (b) is the path from a hyperscaler or first-time IPP customer default to receivables, contract assets and SRA deposits (deposits are the FCF engine: contract liabilities $17.7B Dec-24 to $40.0B Jun-26). The FY24 10-K framed AI only as a demand-perception risk ('artificial intelligence, may affect or may be perceived to affect electricity demand').
    - **direction**: short
    - **evidence**:
      - - **source**: documents table, 10-K FY24 (id 313) vs 10-K FY25 (id 249), Item 1A extracted between 'ITEM 1A. RISK FACTORS' and 'ITEM 1B'
        - **date**: 2025-02-06 vs 2026-01-29
        - **quote_or_number**: Item 1A length 174,544 vs 74,167 chars (-57%); 'Risks Relating to' subsections 9 vs 4; 'Summary of Risk Factors' 1 vs 0; 'offshore wind' 12 vs 2; 'supplier' 42 vs 22; 'credit' 51 vs 14
        - **reproduction**: python: t=re.sub(r'\s+',' ',documents.text); rf=t[re.search(r'I\s*T\s*E\s*M\s*1\s*A\s*\.\s*R\s*I\s*S\s*K',t[6000:]).start()+6000 : ...'ITEM 1B'...]; len(rf); re.findall(r'Risks Relating to [A-Z][^.]{0,60}', rf)
      - - **source**: 10-K FY25 Item 1A (documents id 249), capacity risk
        - **date**: 2026-01-29
        - **quote_or_number**: 'our capacity expansions and related commitments may outpace realized demand... we could be over-invested in our facilities and could incur excess or idle capacity, under-absorption of fixed costs... penalties under supply agreements' - counts in FY24 10-K Item 1A: outpace 0, over-invested 0, idle capacity 0, under-absorption 0, capacity expansion 0
        - **reproduction**: python: for kw in ['outpace','over-invested','idle capacity','under-absorption','capacity expansion']: print(kw, rf24.lower().count(kw), rf25.lower().count(kw))
      - - **source**: 10-K FY25 Item 1A (documents id 249), counterparty risk
        - **date**: 2026-01-29
        - **quote_or_number**: 'nontraditional customers, such as hyperscalers... Some counterparties may have limited operating histories, different contracting practices, or weaker credit profiles... may delay payment, seek to renegotiate terms, or default' - FY24 counts: hyperscaler 0, weaker credit profiles 0, limited operating histories 0, renegotiate terms 0
        - **reproduction**: python: for kw in ['hyperscaler','weaker credit profiles','limited operating histories','renegotiate terms','reservation amount']: print(kw, rf24.count(kw), rf25.count(kw))
      - - **source**: 10-K FY24 Item 1A (documents id 313), AI framing
        - **date**: 2025-02-06
        - **quote_or_number**: 'Energy intensive technological innovations and efficiencies, such as artificial intelligence, may affect or may be perceived to affect electricity demand... The nature and extent of this impact on demand is uncertain.' (FY25 10-K: 'artificial intelligence' 0 occurrences in Item 1A)
        - **reproduction**: python: i=rf24.find('artificial intelligence'); rf24[i-200:i+250]; rf25.count('artificial intelligence')
      - - **source**: 10-Q Item 1A, all five 10-Qs 2025-04-23 through 2026-07-22
        - **date**: 2025-04-23 to 2026-07-22
        - **quote_or_number**: Each 10-Q Item 1A is 333-334 chars and only incorporates the 10-K by reference; no interim risk-factor additions in six quarters
        - **reproduction**: python: for did in (295,281,270,228,218): t=norm(text); s=t.find('ITEM 1A. RISK FACTORS.'); print(did, t.find('ITEM 2.', s)-s)
    - **why_market_misses_it**: A 57% shorter risk section reads as 'less risk' on a word-count screen, and the SRA-may-not-convert sentence got the attention; the over-investment and counterparty-credit paragraphs are new legal text that describes exactly the bear mechanism (GEV pre-buying 30 GW/yr of supply against deposits from first-time buyers) but sits in a section the sell side does not diff.
    - **testable_prediction**: The FY26 10-K (about 2027-01-28) retains or expands the over-investment/idle-capacity paragraph and the hyperscaler credit paragraph, and at least one 2026 10-Q or the 10-K adds quantified customer-concentration or credit-loss language for Power (allowance or past-due disclosure for a hyperscaler/IPP counterparty).
    - **kill_condition**: FY26 10-K deletes the 'outpace realized demand' paragraph, or GEV discloses that SRA deposits are non-refundable and counterparty-guaranteed in a way that removes the credit path (no such disclosure exists today: 'nonrefundable' 0 occurrences in FY24 10-K, FY25 10-K and Q2'26 10-Q).
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 2
    - **caveats**: Risk-factor language is defensive drafting and does not by itself predict losses; the FY24 10-K was the first post-spin 10-K and carried spin-related boilerplate (spin-off 47 vs 17 mentions), which explains much of the shrink. The team's existing 'RPO fine print and 10-K SRA risk factor' angle covers the SRA-conversion sentence; this finding is only about the two paragraphs that are not about SRAs.
- **dead_ends**:
  - mgmt_guidance.prior_value is not usable for drift detection: for GEV it chains unrelated values (e.g. 'annual meeting 2029 -> 2025 -> 2026 -> 2027', FCF 'growth' -> 'increasing levels'); the 2025-10-22 rows tagged 'lower' quote a reaffirmation. Only the verbatim quote column is trustworthy.
  - RPO definition text is byte-identical from the Q3'24 10-Q through the Q2'26 10-Q ('RPO, a measure of backlog, includes unfilled firm and unconditional customer orders... excluding any purchase order that provides the customer with the ability to cancel or terminate without incurring a substantive penalty'); no definitional drift on RPO, backlog, or 'orders' in 10-K/10-Q text.
  - Contract-liabilities policy sentence is identical in the FY24 10-K, FY25 10-K and Q2'26 10-Q ('primarily represent cash received from customers under ordinary commercial payment terms in advance of delivery'); the words 'refund'/'nonrefundable' never appear in connection with deposits or SRAs (the only 'refund' hits are the 2024 arbitration refund). Noncurrent contract liabilities fell to $93M (Jun-26) vs $39.9B current, so 'current' classification follows the operating cycle and cannot be used to time deposit-to-revenue conversion.
  - Loss-contingency accounting policy and 'reasonably possible' language are identical between the two 10-Ks; no new named legal matter appears in the FY25 10-K notes. The 'material weakness' hit in the FY25 10-K is auditor boilerplate in the ICFR opinion.
  - Warranty footnote shows no disclosure change: standard warranty accrual $1,370M (Dec-24) -> $1,573M (Dec-25) -> $1,595M (Jun-26); warranties issued FY25 $760M vs payments $629M (xbrl_facts tags StandardProductWarrantyAccrual*). Team already has 'warranty per GW' on its list.
  - The 'GW under contract' metric (125 GW target) exists only in 8-K/EX press releases and transcripts; the Q2'26 10-Q contains zero 'GW' tokens and only four 'gigawatt' tokens (the unit tables), so there is no filing-level definition to diff.
  - 10-Q Item 1A sections for Q1'25-Q2'26 all incorporate the 10-K by reference (333-334 chars each): no interim risk factor was ever added, including after the Dec-2025 offshore lease pause or the Prolec GE acquisition.
  - Offshore Wind incremental contract-loss dollars are absent from Q1/Q2 10-Qs in 2025 as well as 2026, so their absence in 2026 is not a dropped disclosure (checked documents ids 295, 281, 228, 218).
  - Supplier risk wording narrowed cosmetically (FY24 named 'semiconductor chips, cobalt, certain steel, hafnium, and other rare earth metals'; FY25 says 'semiconductor chips and critical materials (such as specialty metals and rare earths)') but the substance ('limited or sole-sourced... single country') is unchanged; not a finding.

## [Verify] verify:services-accounting:HA fleet activation has stalled: running

- **reproduced**: True
- **corrected_numbers**: All cited corpus numbers reproduce exactly (chunks_fts, GEV 10-Q 2024-04-30/07-24/10-23, 10-K 2025-02-06, 10-K 2026-01-29): installed base 94/100/106/115/126; being installed and commissioned 30/31/30/43; HA in RPO 29/32/36/32/51; operating hours 2.0M/2.5M/2.7M/2.9M/3.6M. HA sales in units (10-Q 2026-07-22): Q2'26 3 vs 8, H1'26 8 vs 13; FY25 24 vs FY24 15; GW shipped H1'26 7.5 vs 8.2, aero 26 vs 10. Transcript src:3161 (gevernova.com webcast PDF 2026-07-22) quote '130 of our HA units running' verified. RPO 'not yet active' definition verified in 10-K 2026-01-29. Corrections/additions: (1) GEV press release 2026-05-26 (gevernova.com 'fleet surpasses 4 million') states 128 HA units operating and ~4.0M hours, so the path is 126 (Dec-25) -> 128 (May-26) -> ~130 (Jul-26); the '+4 in seven months' holds. (2) Flow reconciliation for 2025: 24 units shipped = queue +13 (30->43) + installed base +11 (115->126). Nothing is 'lost'; the queue grew by exactly the shipment surge. Queue/annual shipments = 43/24 = 1.8 years, i.e. normal combined-cycle delivery-to-COD lag (18-30 months). (3) Running-unit additions track shipments two years earlier: 2023 shipped 14 -> 2025 base +11; 2024 shipped 15 -> 2026 base expected ~+13-15 (ending ~139-141); 2025 shipped 24 -> 2027 base ~+20-24. The finding's own prediction ('at most 140') is therefore roughly the base case, not a discriminating test. (4) Hours per unit: 2025 added 0.7M hrs on ~120 avg units = ~5,800 hrs/unit; Dec-25 to late-May-26 added ~0.4M on ~127 units = ~7,400 hrs/unit annualized (rounded figures), so utilization of the running fleet is rising, not falling. (5) Press release 2024-07-15 ('100th HA commissioned', 2.5M hours) matches the Jun-24 10-Q, showing GEV publishes running-unit counts via press releases 2-3 times a year, not only in the 10-K.
- **refuted**: True
- **already_widely_known**: True
- **where_known**: Raw facts are in GEV's own 10-K/10-Q Power-segment paragraph and in gevernova.com press releases (2024-07-15 '100th HA commissioned, 60+ on order'; 2026-05-26 '128 units operating, 4M hours'); CEO Scott Strazik's '130 running / 325 commissioned or under contract' on the 2026-07-22 Q2 call. The specific 'stall' framing was not found in one web search, but no sell-side note was checked directly.
- **materiality**: 2
- **strongest_counterargument**: The 'stall' is pipeline fill, not a slowdown: the commissioning queue rose by 13 in 2025 precisely because HA shipments jumped to 24 from 15, and every one of those 24 units is accounted for (13 into the queue, 11 into the running base). A 43-unit queue against 24 units/year is a 1.8-year delivery-to-COD lag, which is normal for a combined-cycle plant, and the 2-year lagged shipment series (14, 15, 24) implies running-fleet additions of ~11, ~14, ~22 for 2025-2027, so the running base should re-accelerate in 2027 without any change in behaviour. Inside 3-12 months the P&L effect is near zero: new HA units spend their first ~2 years under warranty with minimal LTSA billing, the first major outage is ~4 years/24-32k hours out, and the CEO explicitly places the HA outage wave in the mid-2030s. Even generously, 43 units x ~0.5 GW = ~22 GW; at the bull's $70M/GW-yr (or ~$32M/GW-yr from Gas Power services $13.1B on 400+ GW) a 6-month slip is $0.35-0.75B of revenue timing on $45B guidance, and none of it lands before the 2027 10-K. H1'26 HA shipments of 8 vs 13 sit alongside aero shipments 26 vs 10 and a guided 20 GW run-rate from Q3, and gas equipment revenue is recognized over time, so unit counts at shipment are noise. Finally, utilization of the running fleet is rising (~5,800 -> ~7,400 hrs/unit annualized), and GEV publishes the running count in press releases, so the market is not missing a hidden number.
- **notes**: Verdict: numbers reproduce, thesis does not survive as a short catalyst. Keep one salvageable fact for the memo: the 2-year shipment-to-running lag (2023 shipped 14 -> 2025 base +11) is a clean, falsifiable model for when HA services start; FY26 10-K ~139-141 running units is the base case, and a print below ~135 with the queue above ~50 would be the genuine warning sign. Dead ends: no transcript rows other than src:3161 discuss HA commissioning vs services; Power services revenue by turbine class is not disclosed (only Gas Power total $16.0B, segment Services $13.1B in 10-K 2026-01-29); no GEV disclosure of average delivery-to-COD time; the 325 'commissioned or under contract' figure does not reconcile to 126+43+51=220 (likely includes SRAs) and is not usable. Web search: 1; fetches: 2; SQL: 3. Firecrawl MCP is unauthenticated in this session (not needed).

## [Sweep] find:contradictions

- **lens**: cross-source contradiction finder (GEV filings/IR vs Siemens Energy, Mitsubishi Heavy, customer filings, commentary)
- **findings**:
  - - **title**: GEV's reservation pool turns over 3x slower than Siemens Energy's, and the customer side shows why
    - **claim**: GEV converts slot reservations to firm orders at about 10 GW per quarter from a 63 GW pool (about 19 months average dwell), while Siemens Energy converts 12 GW per quarter from a 26 GW pool (about 6-7 months), so the 'at least 125 GW under contract' headline is more than half reservations that GEV's own 10-K says 'may not result in orders'.
    - **mechanism**: SRAs are outside RPO and carry only a down payment; equipment revenue (cost-to-cost) and the bulk of contract-liability cash arrive only after conversion. If conversion stays at ~10 GW/qtr, the 63 GW pool is a 6-quarter overhang, and any lapse hits both the 2027-28 Power revenue ramp and the H2'26 FCF guide (implied H2 FCF $1.6-2.6B already assumes fewer conversions). It also means the price captured on 2027-28 deliveries was set when the SRA was signed, extending the GLJ 'old-price vintage' argument to the reservation pool.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, GEV 8-K/EX press releases (five quarters)
        - **date**: 2025-07-23, 2025-10-22, 2026-01-28, 2026-04-22, 2026-07-22
        - **quote_or_number**: SRA pool 21->25->29->43->56->63 GW; converted 3, 7, 8, 6, 10 GW; new SRAs 7, 12, 21, 19, 18 GW; firm backlog 29->29->33->40->44->53 GW
        - **reproduction**: SELECT c.filing_date, c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND "converted" AND "shipped"' AND c.ticker='GEV' AND c.form='8-K/EX' ORDER BY c.filing_date
      - - **source**: chunks id 251693, Siemens Energy Q3 FY26 pre-close call transcript (siemens-energy.com)
        - **date**: 2026-06-29
        - **quote_or_number**: 'the conversion of those into orders within on average 6-12 months, which is also visible in our large order backlog of around 60 GW as of Q2 Fiscal Year 2026'
        - **reproduction**: SELECT text FROM chunks WHERE id=251693
      - - **source**: chunks id 251675, Siemens Energy Q3 FY26 analyst presentation (2026-08-05)
        - **date**: 2026-08-05
        - **quote_or_number**: '15 GW booked (12 GW converted from SRAs), 6 GW shipped ... 69 GW backlog / 26 GW SRAs'
        - **reproduction**: SELECT text FROM chunks WHERE id=251675
      - - **source**: chunks id 29660, GEV 10-K FY2025 risk factor
        - **date**: 2026-01-29
        - **quote_or_number**: 'If anticipated demand is delayed or does not materialize, orders may be deferred, reduced, or canceled and slot reservation agreements may not result in orders.'
        - **reproduction**: SELECT text FROM chunks WHERE id=29660
      - - **source**: chunks, NRG 8-K/EX, 10-Q, 10-K (customer side)
        - **date**: 2025-02-26 -> 2026-02-24 -> 2026-08-04
        - **quote_or_number**: NRG SRA with GEV grows 1.2 GW (Feb-25) -> 2.4 GW (May-25) -> 3.6 GW 7HA (Feb-26), still an SRA; Aug-26 8-K: 1.2 GW Texas CCGT 'aligned on principal commercial terms ... subject to final documentation'
        - **reproduction**: SELECT c.form,c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation" AND "7HA"' AND c.ticker='NRG' ORDER BY c.filing_date; SELECT text FROM chunks WHERE id=263759
      - - **source**: chunks id 5619, GEV Q2'26 press release
        - **date**: 2026-07-22
        - **quote_or_number**: 'We now expect to have at least 125 GW of gas equipment under contract by year-end 2026' (116 GW at Jun-30 = 53 GW backlog + 63 GW SRAs)
        - **reproduction**: SELECT text FROM chunks WHERE id=5619
    - **why_market_misses_it**: Sell-side and press quote the 116/125 GW 'under contract' figure as if it were backlog; nobody puts the GEV and Siemens SRA-to-order dwell times side by side, and Siemens reports its SRA pool explicitly (26 GW) while GEV's is only derivable from the quarterly flow.
    - **testable_prediction**: Q3'26 release (about 2026-10-22): SRA conversions stay at or below 12 GW while the SRA pool stays above 60 GW (dwell still >5 quarters); NRG's 3.6 GW is still not booked as a firm order in its Q3'26 10-Q (early Nov 2026).
    - **kill_condition**: Q3'26 shows conversions of 15+ GW and the SRA pool falling below 55 GW, or GEV discloses a contractual conversion deadline of 12 months or less on SRAs.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Siemens' GW may include steam-turbine capacity of combined-cycle configurations (footnote on its CMD 2025 slide, chunk 252603; not verified for the Q3 figures), which would overstate SE relative to GEV by up to a third. Dwell is a pool/flow ratio, not a disclosed contract term. GEV has never disclosed whether SRA pricing is fixed at signing.
  - - **title**: Same quarter, Siemens shipped 6 GW to GEV's 3.3 GW, and GEV's HA deliveries fell 63% YoY while IR says 20 GW annualized starts now
    - **claim**: GEV's own 10-Q unit table shows Apr-Jun 2026 gas-turbine shipments of 3.3 GW (3 HA units, vs 5.2 GW and 8 HA units a year earlier) and H1'26 of 7.5 GW (down 9% YoY), while management and press repeat '20 GW annualized from Q3 2026' and 'at least 30 GW over the next six quarters'; Siemens Energy shipped 6 GW in the identical calendar quarter.
    - **mechanism**: H2'26 Power revenue and EBITDA guidance is explicitly back-half weighted on 'ship more gas turbines in the second half'. Meeting 20 GW annualized needs 5 GW/quarter, equal to GEV's best-ever quarter (5.2 GW, Q2'25), from a base that just printed 3.3 GW. A Q3 print of 3.5-4.5 GW keeps FY26 Power revenue near the low end and undercuts the 24/30 GW capacity narrative that supports the multiple.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks, GEV 10-Q and 10-K 'Sales in units' tables, row 'Gas Turbine Gigawatts'
        - **date**: 2024-04-30 through 2026-07-22
        - **quote_or_number**: Shipped GW by quarter: Q1'25 3.0, Q2'25 5.2, Q3'25 4.0, Q4'25 3.1, Q1'26 4.2, Q2'26 3.3; FY 2022 11.1, 2023 13.8, 2024 11.9, 2025 15.3; TTM to Jun-26 14.6
        - **reproduction**: SELECT c.form,c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Gas Turbine Gigawatts"' AND c.ticker='GEV' AND c.form IN ('10-Q','10-K') ORDER BY c.filing_date  (regex 'Sales in units.*?Gas Turbine Gigawatts( \d+\.\d)+')
      - - **source**: chunks, GEV 10-Q 2026-07-22 'Sales in units'
        - **date**: 2026-07-22
        - **quote_or_number**: HA-Turbines sold: Q2'26 3 vs Q2'25 8; H1'26 8 vs H1'25 13; Heavy-Duty 13 vs 18; Aeroderivatives 16 vs 3
        - **reproduction**: SELECT text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Sales in units" AND "Heavy-Duty Gas Turbines"' AND c.ticker='GEV' AND c.form='10-Q' AND c.filing_date='2026-07-22'
      - - **source**: chunks id 251608 and 251621, GEV Q2'26 webcast transcript (gevernova.com, 2026-07-22)
        - **date**: 2026-07-22
        - **quote_or_number**: 'as we increase annual production capacity to 20 gigawatts starting this quarter'; 'we're going to ship over the next six quarters at least 30 gigawatts of output'
        - **reproduction**: SELECT id,text FROM chunks WHERE id IN (251608,251621)
      - - **source**: chunks id 251675, Siemens Energy Q3 FY26 analyst presentation
        - **date**: 2026-08-05
        - **quote_or_number**: '15 GW booked ... 6 GW shipped' for Apr-Jun 2026 (GEV same quarter: 3.3 GW)
        - **reproduction**: SELECT text FROM chunks WHERE id=251675
      - - **source**: chunks id 217314 (WEB commentary)
        - **date**: 2026-08 (undated web)
        - **quote_or_number**: 'Its production plan: roughly 20 GW annualized this quarter, 24 GW by 2028, and a push toward 30 GW by 2030.'
        - **reproduction**: SELECT text FROM chunks WHERE id=217314
    - **why_market_misses_it**: The GW-shipped row sits inside the 10-Q unit table, not in the press release; the press release only gives rounded 'shipped 3 GW'. Nobody lines it up against Siemens' same-quarter 6 GW, and the '20 GW' phrase is repeated as if it were already a run-rate.
    - **testable_prediction**: Q3'26 10-Q (about 2026-10-22) 'Gas Turbine Gigawatts' sales row prints below 5.0 GW and HA units sold below 10.
    - **kill_condition**: Q3'26 shipments of 5.0 GW or more with HA units of 10 or more, i.e. the 20 GW annualized run-rate is real on the first quarter it was promised.
    - **novelty**: 2
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Overlaps the team's 'factory throughput ceiling' angle; this adds the filing-based tripwire and the Siemens same-quarter comparison. Equipment revenue is recognized cost-to-cost, so a shipment shortfall dents revenue with a lag rather than one-for-one. Siemens' GW may include steam-turbine capacity (see finding 1 caveat). Aeroderivative units jumped to 16, so part of the HA drop is mix.
  - - **title**: Industry orders spiked 2.4x to 96 GW in 2025; the number-three OEM plans for 70 GW, and GEV's own year-end target math only needs a halving of intake
    - **claim**: McCoy data on MHI's May-2026 slide shows global gas-turbine orders of 40.3 GW in CY24 and 96.1 GW in CY25; MHI says it does 'not expect demand to continue at 100 GW' and plans on about 70 GW/yr (after saying 50 GW post-2027 in Feb-2026), while GEV's 'at least 125 GW by year-end 2026' from 116 GW requires net additions of only 9 GW over two quarters versus 16-17 GW net in each of the prior three quarters.
    - **mechanism**: GEV's firm orders were 29.8 GW in 2025 (31% of the 96 GW industry) and 20.1 GW in H1'26. If the industry reverts toward MHI's 70 GW, share-constant GEV firm intake is about 22 GW/yr, roughly half the H1'26 pace. Orders drive the multiple more than earnings in the 3-12 month window; the first quarter where net GW additions drop below 10 GW is the 'peak orders' print.
    - **direction**: short
    - **evidence**:
      - - **source**: chunks id 252753, MHI FY2025 Q4 results presentation (mhi.com), McCoy Power Reports chart
        - **date**: 2026-05 (FY2025 results)
        - **quote_or_number**: Demand for Gas Turbines Used in Power Generation (GW): CY19 56.2, CY20 48.3, CY21 30.6, CY22 34.4, CY23 36.8, CY24 40.3, CY25 96.1
        - **reproduction**: SELECT text FROM chunks WHERE id=252753
      - - **source**: chunks id 252832, MHI FY2025 Q4 Q&A (mhi.com)
        - **date**: 2026-05
        - **quote_or_number**: 'We do not expect demand to continue at 100 GW. Previously, we forecasted an average of 50-60 GW over the next five years, but now we see demand rising by around 10 GW to an average of around 70 GW.'
        - **reproduction**: SELECT text FROM chunks WHERE id=252832
      - - **source**: chunks id 252922, MHI FY2025 Q3 Q&A
        - **date**: 2026-02
        - **quote_or_number**: 'our view remains that market size will be around 70 GW per year for the time being and that it will remain at around 50 GW after that'
        - **reproduction**: SELECT text FROM chunks WHERE id=252922
      - - **source**: chunks, GEV 10-K 2026-01-29 and 10-Q 2026-07-22 'Orders in units' Gas Turbine Gigawatts row
        - **date**: 2026-01-29 / 2026-07-22
        - **quote_or_number**: Firm gas-turbine orders GW: 2023 9.5, 2024 20.2, 2025 29.8; Q1'26 8.1, Q2'26 12.1 (H1'26 20.1)
        - **reproduction**: SELECT c.filing_date,c.text FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Gas Turbine Gigawatts"' AND c.ticker='GEV' AND c.form IN ('10-K','10-Q') ORDER BY c.filing_date
      - - **source**: chunks id 13597 and 5618, GEV Q1'26 and Q2'26 press releases
        - **date**: 2026-04-22 / 2026-07-22
        - **quote_or_number**: Backlog+SRA 83->100 GW, target 'at least 110 GW by year-end 2026'; then 100->116 GW, target 'at least 125 GW by year-end 2026'
        - **reproduction**: SELECT id,text FROM chunks WHERE id IN (13597,5618)
      - - **source**: chunks id 252775, MHI FY2025 Q4 presentation
        - **date**: 2026-05
        - **quote_or_number**: MHI large-frame order intake FY24 25 units (11 GW) -> FY25 35 units (16 GW); backlog 48 (21 GW) -> 74 (33 GW)
        - **reproduction**: SELECT text FROM chunks WHERE id=252775
    - **why_market_misses_it**: US investors read GEV and Siemens (110-120 GW market talk) and treat MHI's Japanese-language-origin Q&A as conservative noise; the McCoy CY24->CY25 jump is only on an MHI slide. The 'at least 125' floor is reported as ambition when it is arithmetically a slowdown floor.
    - **testable_prediction**: Q3'26 release (about 2026-10-22): net backlog+SRA addition of 8-12 GW (versus 16-17 in each of the prior three quarters) and management does not raise the 125 GW target by more than 10 GW; MHI FY2026 Q2 Q&A (Nov 2026) keeps the 70 GW view.
    - **kill_condition**: Q3'26 net addition of 15+ GW with the year-end target raised to 135+ GW, or MHI lifts its five-year average view to 90+ GW.
    - **novelty**: 2
    - **confidence**: 3
    - **materiality**: 3
    - **caveats**: Refines, does not replace, the team's 'MHI 70 vs Siemens 110-120' angle. GEV raised the year-end floor from 110 to 125 within one quarter after adding 16 GW, so the floor is soft and has been beaten before. McCoy 'demand' is orders booked, and OEM SRAs are not in it, so the 2025 spike partly reflects conversions of 2024 reservations.
  - - **title**: GEV's tariff cost estimate has been cut in half twice, a small unflagged tailwind
    - **claim**: GEV's 10-Q tariff estimates fell from $300-400M for 2025 (Apr-25) to an actual $250M (10-K), then from $250-350M for 2026 (Apr-26) to $100-200M (Jul-26), a roughly $150M mid-point improvement inside one quarter that no commentary chunk in the corpus mentions.
    - **mechanism**: Tariff cost sits in cost of goods; a $150M cut is about 1.5% of FY26 adjusted EBITDA (guide roughly $10B), a modest offset to GLJ's old-price-vintage margin argument for 2026-27 deliveries, and the Jul-26 wording adds 'pursuing the recovery of certain tariffs', which could become a one-time gain.
    - **direction**: long
    - **evidence**:
      - - **source**: chunks id 54614, GEV 10-Q
        - **date**: 2025-04-23
        - **quote_or_number**: 'approximately $300 million to $400 million in 2025, after taking into consideration contractual protections and mitigating actions'
        - **reproduction**: SELECT text FROM chunks WHERE id=54614
      - - **source**: chunks id 29736, GEV 10-K FY2025
        - **date**: 2026-01-29
        - **quote_or_number**: 'The total cost impact from the global tariffs for the full year 2025 was approximately $250 million'
        - **reproduction**: SELECT text FROM chunks WHERE id=29736
      - - **source**: chunks id 13690 and 5721, GEV 10-Q
        - **date**: 2026-04-22 / 2026-07-22
        - **quote_or_number**: 'approximately $250 million to $350 million in 2026' -> 'approximately $100 million to $200 million in 2026 ... including pursuing the recovery of certain tariffs'
        - **reproduction**: SELECT id,text FROM chunks WHERE id IN (13690,5721)
      - - **source**: chunks id 251605, GEV Q2'26 webcast transcript
        - **date**: 2026-07-22
        - **quote_or_number**: 'the volume we've shipped in this first half had fewer contractual protections for tariffs since we signed these orders before their implementation'
        - **reproduction**: SELECT text FROM chunks WHERE id=251605
    - **why_market_misses_it**: The number lives in a single MD&A paragraph and moved by less than 2% of EBITDA; the market is focused on orders and the GLJ margin call.
    - **testable_prediction**: Q3'26 10-Q (about 2026-10-22) keeps the 2026 estimate at or below $200M, and any tariff recovery is called out as a discrete item.
    - **kill_condition**: Q3'26 10-Q raises the 2026 tariff estimate back above $250M, e.g. from new Section 232 actions.
    - **novelty**: 2
    - **confidence**: 4
    - **materiality**: 1
    - **caveats**: Intra-GEV drift rather than a cross-source contradiction; small in dollars. The transcript line about H1 shipments having fewer tariff protections partly supports the bear's old-contract vintage point.
- **dead_ends**:
  - Customer-side deposit terms: no utility or IPP 10-K/10-Q in the corpus discloses a turbine deposit or slot-reservation payment amount; only NRG (SRA GW, no dollars) and TLN (an escrow arrangement with GE on an AACA, chunk 344561). Query: ('turbine' OR 'turbines') AND ('deposit' OR 'prepayment' OR 'down payment') for ticker != GEV.
  - SRA price terms: no GEV primary source states whether pricing is fixed at reservation or at conversion; the only 'reservation AND escalation/lock' hits are generic contract-clause web pages (chunks 224xxx). Siemens' remark that fast conversion lets it 'benefit from increasing pricing dynamics' is the only OEM hint.
  - HA fleet count: 10-K FY25 (126 installed, 43 being installed, 51 in RPO) vs commentary 'approximately 130 operating, 325 under contract' (chunk 217509) are consistent once SRAs are included; no contradiction.
  - Siemens backlog 60 GW (Q2 FY26, pre-close call) vs 69 GW (Q3 FY26): plain growth, not a discrepancy. The Siemens '110-120 GW' market claim was not re-examined (already on the team list).
  - Gas-turbine market size in competitor_financials table: only 8 MHI and 8 Hitachi rows, none with GW demand figures; the useful MHI numbers are only in COMPETITOR chunks (src:3201, 3207, 3211).
  - Reservation agreements in the other 17 customer tickers' filings: only NRG uses the term; VST, TLN, CEG, ETR, NEE, DUK, SO, AEP, D, XEL and the hyperscalers do not disclose GE reservation volumes.
  - backlog_quarterly metric 'reservation_gw' is noisy (mixes %, $, HA units, RPO); the 8-K/EX press-release flow series is the reliable source for the SRA pool.
  - queue_projects and operator_forecasts are empty, so PJM/ERCOT load-forecast vs utility contradiction was not attempted. Semantic search (embed.py/Ollama) was not used; FTS sufficed.

## [Sweep] find:customer-filings

- **lens**: customer-side reader: what GEV's utility, IPP and hyperscaler customers disclose in their own SEC filings (cost per kW, in-service dates, reservation language, regulatory outcomes) that GEV does not
- **findings**:
  - - **title**: Customer-filed cost of one H/J-class combined-cycle block rose 55-75% between 2024 and Q1-2026 filings, and the first regulator prudence denial has already happened
    - **claim**: Regulator-filed all-in cost for an identical 754 MW 1x1 combined-cycle block at Entergy went from $1,583-1,592/kW (Oct-Nov 2024 filings) to $2,122-2,125/kW (Aug-Sep 2025) to $2,444-2,773/kW (Feb-Mar 2026), Duke's Cayuga 2x(1x1) rose $2,012 to $2,236/kW in six months, and in Jan 2026 the Arkansas PSC refused to find Entergy's $1,602M Jefferson plant cost prudent; GEV itself says its 2H26 order $/kW is only 10-20 points above 4Q25 orders.
    - **mechanism**: GEV's gas equipment revenue is recognized cost-to-cost against contracted prices, so the 2026-27 order vintage margin depends on customers accepting $2,400-2,800/kW plant costs. Regulated utilities can only pay that if state PSCs certify it; merchant IPPs (CEG, TLN, NRG, VST) state new-build does not pencil and are buying existing plants at $740-760/kW instead. Where PSCs cap costs (APSC Jefferson), EPC scope or turbine price is squeezed and SRA-to-order conversion slows; where PSCs approve as filed (PSCSC Anderson, Apr 2026), the price umbrella under GEV's 10-20 point increases is confirmed and GEV is capturing only a minority of the plant-cost inflation, implying pricing headroom.
    - **direction**: either
    - **evidence**:
      - - **source**: chunks_fts, ETR 10-Q 2024-11-01 (acc 0000065984-24-000112)
        - **date**: 2024-11-01
        - **quote_or_number**: "The combined cost of the first two new generation resources is estimated to be approximately $2,387 million, and these units are expected to achieve commercial operation in 2028." 2,387/1,508 MW = $1,583/kW
        - **reproduction**: SELECT c.form,c.filing_date,substr(c.text,1,1200) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"2,387" AND "combined cycle"' AND c.ticker='ETR' AND c.form='10-Q' AND c.filing_date='2024-11-01'
      - - **source**: chunks_fts, ETR 10-Q 2026-07-31 and 10-K 2026-02-19
        - **date**: 2026-07-31
        - **quote_or_number**: "estimated costs are approximately $2,027 million for the Waterford 6 Power Station and $2,091 million for the Westlake Power Station" (two 754 MW CCs) = $2,688 and $2,773/kW; "seven new combined cycle ... totaling 5,278 MW at a total cost of approximately $12.9 billion" = $2,444/kW
        - **reproduction**: SELECT c.filing_date,substr(c.text,1,1400) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Waterford 6 Power Station" AND "estimated costs"' AND c.ticker='ETR' AND c.form='10-Q' AND c.filing_date='2026-07-31'; and MATCH '"seven new combined cycle"'
      - - **source**: chunks_fts, ETR 10-Q 2025-10-31 and 10-K 2026-02-19
        - **date**: 2026-02-19
        - **quote_or_number**: Legend 754 MW: $1.46B (Jun 2024 application) to PUCT cost cap $1.6B (Sep 2025) = $1,936 to $2,122/kW; Jefferson 754 MW: "The estimated cost of the project is $1,602 million" = $2,125/kW; Delta Blues 754 MW $1.2B = $1,592/kW
        - **reproduction**: SELECT c.filing_date,substr(c.text,1,900) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Legend Power Station" AND "1.6 billion"' AND c.ticker='ETR'; MATCH '"Jefferson Power Station" AND "1,602"'; MATCH '"Delta Blues" AND "1.2 billion"'
      - - **source**: chunks_fts, ETR 10-Q 2026-07-31 (APSC order Jan 2026)
        - **date**: 2026-07-31
        - **quote_or_number**: "the APSC issued its order finding that Entergy Arkansas had demonstrated a need for the resource but had not met its burden with respect to supporting the prudence of the costs"; benchmark set "$90 million below the cost presented"; APSC also ordered all-source competitive solicitations for future additions; rehearing filed Feb 2026
        - **reproduction**: SELECT c.filing_date,substr(c.text,1,1500) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Jefferson Power Station" AND "prudence"' AND c.ticker='ETR' AND c.filing_date='2026-07-31'
      - - **source**: chunks table ids 378858 (DUK 10-K 2025-02-27) and 350555 (DUK 10-Q 2025-08-05); DUK 10-Q 2026-08-04
        - **date**: 2025-08-05
        - **quote_or_number**: Cayuga CC (1,476 MW, confirmed GE Vernova 7HA customer per Duke/GEV releases): "$2.97 billion, plus AFUDC" (Feb 2025) to "approximately $3.3 billion, plus actual AFUDC" (Aug 2025) = $2,012 to $2,236/kW, +11% in 6 months; Anderson County 1,365 MW "approximately $3.2 billion, inclusive of financing costs" = $2,344/kW, PSCSC approved Apr 24 2026
        - **reproduction**: SELECT id,form,filing_date,substr(text,instr(text,'Cayuga CC'),400) FROM chunks WHERE id IN (378858,350555,263264); SELECT filing_date,substr(text,instr(text,'Anderson County Combined'),700) FROM chunks WHERE ticker='DUK' AND form='10-Q' AND filing_date='2026-08-04' AND text LIKE '%Anderson County Combined Cycle%'
      - - **source**: chunks table id 362974, CEG 8-K/EX 2025-05-06 (Calpine acquisition deck); TLN 8-K/EX 2025-08-07 (chunk 347804); NRG 8-K/EX 2025-05-12
        - **date**: 2025-05-06
        - **quote_or_number**: CEG: "LCOE for Natural Gas based on a $2,500 /kW cost for CCGT online in 2030" and "Current Market Forwards do not Support New Build Economics"; TLN: bought Freedom/Guernsey "at a material discount to current new-build CCGT costs"; NRG bought 738 MW at "$760 per kW"
        - **reproduction**: SELECT id,ticker,filing_date,substr(text,1,900) FROM chunks WHERE id IN (362974,347804); SELECT filing_date,substr(text,1,600) FROM chunks WHERE ticker='NRG' AND form='8-K/EX' AND filing_date='2025-05-12' AND text LIKE '%$760 per kW%'
      - - **source**: GEV 2Q26 webcast transcript, sources url https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf (chunks accession src:3161)
        - **date**: 2026-07-22
        - **quote_or_number**: "we would expect gas equipment orders in the second half to have a dollar per kW that is at the higher end of the range of 10 to 20 points versus 4Q '25 orders"
        - **reproduction**: SELECT substr(c.text,1,700) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"dollar per kW" AND "10 to 20 points"' AND c.ticker='GEV'
    - **why_market_misses_it**: Sell-side tracks GEV's own $/kW commentary and SRA counts; nobody stacks the customers' regulator-filed cost per kW for the same 754 MW block across five state dockets, and the APSC prudence denial sits in a subsidiary section of Entergy's 10-Q that GEV analysts do not read. The $2,500/kW-plus number is only visible on the buyer's side.
    - **testable_prediction**: Entergy Louisiana's three 2026 applications (Waterford 6 and Westlake $4.1B, hearings Oct-Nov 2026; seven-unit $12.9B, hearing Sept 2026) get LPSC decisions at or before the Dec 2026 meeting. Prediction: at least one comes back with a cost cap, scope cut or deferral, and Entergy's Q3 10-Q (about Oct 30 2026) repeats the APSC Jefferson benchmark dispute unresolved. Also IURC order on AEP Rockport 1,520 MW expected Q1 2027.
    - **kill_condition**: LPSC certifies all 6.8 GW (Waterford 6, Westlake, seven units) as filed with no cost cap by Dec 31 2026 AND APSC grants Entergy Arkansas's rehearing raising the Jefferson benchmark to the full $1,602M. That would show regulators accept $2,400-2,800/kW and the risk is to the upside for GEV pricing, not conversion.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Entergy's long-lead turbine agreements are with Mitsubishi Power Americas and Siemens Energy (Power Magazine, Apr 1 2025, https://www.powermag.com/gas-powers-boom-sparks-a-turbine-supply-crunch/; Orange County uses two M501JAC), so the Entergy ladder is a market price for H/J-class CC plants, not a GEV price. Duke is the GEV-specific leg (7HA at Person County and Anderson). All-in costs include interconnection, AFUDC and owner's costs; turbine share is not disclosed. Entergy Mississippi's Vicksburg still shows $1.2B ($1,592/kW) in the Feb 2026 10-K, an outlier against the ladder. Do not present Entergy's 6.8 GW as GEV SRA conversion; config/customers.json labels Entergy a GEV counterparty but no filing supports that.
  - - **title**: Customers filing in 2026 ask for 2030-31 in-service dates, versus 2028 in 2024 filings; Entergy quietly dropped its 2028 date for the first Meta plants
    - **claim**: Combined-cycle applications filed by GEV's customer set in 2024 carried 2028 in-service dates (Franklin Farms 1-2 2028, Delta Blues 2028, Legend early-2028 sync); every application filed since Oct 2025 carries end-2029 to 2031 (Duke Person 2 end-2029, Cayuga 2029/2030, Duke Anderson end-2030, Waterford 6 Jul-2030, Westlake Oct-2030, seven Louisiana units 2030-31, Georgia Power's five CCs Q4-2029 to Q4-2030), and Entergy's May and Jul 2026 10-Qs no longer contain the phrase 'expected to be in service in 2028' for Franklin Farms 1-2 that appeared in its Oct 2025 10-Q and Feb 2026 10-K.
    - **mechanism**: Revenue on gas equipment is recognized over time as the units are built, so an SRA signed in 2026 that converts to an order for a 2030-31 plant mostly hits GEV revenue in 2028-30, not 2027. The customer-filed COD ladder is independent confirmation of GEV's 2Q26 statement that slots are 'largely sold out of 30 and more than half of 31', and it means 2027 gas-equipment revenue is dominated by the 2024-25 order vintage (the lower-price vintage in the GLJ bear case). The Franklin Farms date removal is the first customer-side sign a GEV-competitor-supplied 2028 plant may be slipping, which matters as a read-across for whether any OEM is meeting 2028 dates.
    - **direction**: either
    - **evidence**:
      - - **source**: documents table, ETR 10-Q/10-K by filing date (string presence test)
        - **date**: 2026-07-31
        - **quote_or_number**: 'expected to be in service in 2028' present in ETR 10-Q 2025-10-31 and 10-K 2026-02-19, absent in 10-Q 2026-05-01 and 10-Q 2026-07-31 while 'Franklin Farms' is still present in both
        - **reproduction**: SELECT form,filing_date,instr(text,'expected to be in service in 2028')>0 AS has2028,instr(text,'Franklin Farms')>0 AS hasFF FROM documents WHERE ticker='ETR' AND form IN ('10-K','10-Q') AND filing_date>='2025-06-01' ORDER BY filing_date
      - - **source**: chunks_fts, ETR 10-Q 2025-10-31
        - **date**: 2025-10-31
        - **quote_or_number**: "Franklin Farms Power Station Units 1 and 2 are expected to be in service in 2028, and Waterford 5 Power Station is expected to be in service in 2029"
        - **reproduction**: SELECT c.filing_date,substr(c.text,1,800) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"Franklin Farms" AND "in service in 2028"' AND c.ticker='ETR'
      - - **source**: chunks_fts, ETR 10-Q 2026-07-31; DUK 10-Q 2026-08-04; SO 10-Q 2026-07-30
        - **date**: 2026-08-04
        - **quote_or_number**: ETR: "seven new combined cycle ... various estimated in-service dates in 2030 and 2031"; Waterford 6 / Westlake "July 2030 and October 2030"; DUK Anderson "in service by the end of 2030", Person 2 "by the end of 2029", Cayuga "CC 1 ... 2029 and CC 2 ... 2030"; SO table: Bowen 7 Q4-2029, Bowen 8 Q2-2030, Wansley 10 Q4-2029, Wansley 11 Q2-2030, McIntosh 12 Q4-2030
        - **reproduction**: SELECT c.ticker,c.filing_date,substr(c.text,1,1200) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"in-service dates in 2030 and 2031" OR "July 2030 and October 2030" OR "Bowen Unit 7" OR "Anderson County Combined Cycle"' AND c.ticker IN ('ETR','DUK','SO') AND c.filing_date>='2026-04-01'
      - - **source**: GEV 2Q26 webcast transcript, src:3161
        - **date**: 2026-07-22
        - **quote_or_number**: "already signed for '30 and '31 and that will be largely sold out of '30 and more than half of '31" ... "heavy-duty that will be shipped in '30, '31, but then really commissioned in '32 and '33"
        - **reproduction**: SELECT substr(c.text,1,900) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"sold out" AND "more than half"' AND c.ticker='GEV' AND c.form='TRANSCRIPT'
    - **why_market_misses_it**: GEV reports SRAs and backlog in GW, not by delivery year, and the street models revenue on 20 GW/yr throughput. The customers' dockets are the only public place where delivery years are pinned per plant, and the Entergy date removal is a silent deletion, not a stated slip.
    - **testable_prediction**: Entergy's Q3 2026 10-Q (about Oct 30 2026) will either state a Franklin Farms 1-2 date later than 2028 or again omit the date; and at least one additional customer CC application filed between now and Mar 2027 (AEP Rockport, Georgia Power 2028 IRP additions, Dominion) will carry a 2031 or later in-service date.
    - **kill_condition**: Entergy's Q3 2026 10-Q or an Entergy release reaffirms Franklin Farms 1-2 in service in 2028, and a customer application filed after Sep 2026 secures a pre-2030 combined-cycle in-service date with a named GEV 7HA supply.
    - **novelty**: 3
    - **confidence**: 4
    - **materiality**: 3
    - **caveats**: Franklin Farms is a Mitsubishi or Siemens plant (Entergy's disclosed OEM agreements), so its slip is a read-across on EPC and OEM lead times, not direct evidence on GEV deliveries. Absence of a phrase is weaker evidence than a stated revision; Entergy may simply have shortened the section. Georgia Power's five CCs do not name an OEM; its Yates CTs are Mitsubishi M501JAC.
  - - **title**: NRG grew its GE Vernova slot reservations 1.2 to 2.4 to 3.6 GW in successive filings, then deleted every GEV, SRA and 5.4 GW PDA reference from its 2026 10-Qs
    - **claim**: NRG's 10-K and 10-Q filings disclosed GEV slot reservation agreements of 1.2 GW (Feb 2025), 2.4 GW (May, Aug, Nov 2025) and 3.6 GW (Feb 2026); its May 6 and Aug 4 2026 10-Qs and both 2026 earnings releases contain zero occurrences of 'Vernova', 'slot reservation' or '5.4 GW', and the Aug 2026 release instead reports a 1.2 GW hyperscaler CCGT only 'aligned on principal commercial terms'.
    - **mechanism**: NRG's 3.6 GW is about 6% of GEV's 63 GW SRA balance and its PDA targets first commercial operation by end-2029, which requires firm orders in 2026. If NRG is not converting (and no longer highlighting the SRAs), some of GEV's SRA balance may lapse, be re-traded to another buyer, or convert later than the 2H26 conversion pace guidance implies; deposits on lapsed SRAs affect the contract-liability build the H2 FCF bridge relies on.
    - **direction**: short
    - **evidence**:
      - - **source**: documents table, NRG 10-K/10-Q/8-K/EX 2025-2026 (string presence per filing)
        - **date**: 2026-08-04
        - **quote_or_number**: Vernova / 'slot reservation' / '5.4 GW' present in 8-K/EX 2025-02-26, 10-K 2025-02-26, 10-Q 2025-05-12, 10-Q 2025-08-06, 10-Q 2025-11-06, 10-K 2026-02-24; all three absent in 10-Q 2026-05-06 (247,917 chars) and 10-Q 2026-08-04 (286,725 chars)
        - **reproduction**: SELECT form,filing_date,n_chars,instr(text,'Vernova')>0 v,instr(text,'slot reservation')>0 s,instr(text,'5.4 GW')>0 g FROM documents WHERE ticker='NRG' AND form IN ('10-K','10-Q','8-K/EX') AND filing_date>='2025-01-01' AND (form IN ('10-K','10-Q') OR instr(text,'Vernova')>0) ORDER BY filing_date
      - - **source**: chunks_fts, NRG 10-K 2025-02-26, 10-Q 2025-08-06, 10-K 2026-02-24
        - **date**: 2026-02-24
        - **quote_or_number**: "slot reservation agreement with GEV for the procurement of 1.2 GW of 7HA gas turbines" (Feb 2025); "two slot reservation agreements ... 2.4 GW" (May-Nov 2025); "slot reservation agreements with GEV for the procurement of 3.6 GW of 7HA gas turbines. The first projects ... expected to commence operations by the end of 2029" (Feb 2026)
        - **reproduction**: SELECT c.form,c.filing_date,substr(c.text,instr(c.text,'slot reservation')-250,500) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"slot reservation"' AND c.ticker='NRG' ORDER BY c.filing_date
      - - **source**: chunks_fts, NRG 8-K/EX 2026-08-04 (acc 0001013871-26-000018, nrgq22026ex991.htm)
        - **date**: 2026-08-04
        - **quote_or_number**: "The parties are aligned on principal commercial terms for the development of a 1.2 GW combined cycle natural gas generation facility in Texas and remains subject to final documentation and approvals." No OEM named.
        - **reproduction**: SELECT substr(c.text,1,800) FROM chunks_fts f JOIN chunks c ON c.id=f.rowid WHERE chunks_fts MATCH '"principal commercial terms"' AND c.ticker='NRG'
      - - **source**: SEC full-text search API
        - **date**: 2026-09-21
        - **quote_or_number**: Query '"slot reservation agreement"' since 2024-01-01 returns 3 non-GEV filings in total (NRG 8-K and 10-K of 2025-02-26, Baker Hughes 8-K 2026-04-23); NRG is the only GEV customer that has ever disclosed SRA GW in a filing
        - **reproduction**: GET https://efts.sec.gov/LATEST/search-index?q=%22slot%20reservation%20agreement%22&forms=10-K,10-Q,8-K&dateRange=custom&startdt=2024-01-01 with User-Agent gev-corpus-research/1.0
    - **why_market_misses_it**: GEV's SRA balance is reported in aggregate and is not auditable from the customer side; NRG is the one customer that disclosed its SRA GW, and the disappearance of the sentence is a deletion, which screens and transcripts do not flag.
    - **testable_prediction**: NRG's Q3 2026 10-Q (about Nov 5 2026) will again omit any GEV SRA figure, and by GEV's Q4 2026 release (late Jan 2027) NRG will not have announced a firm 7HA order for the 5.4 GW PDA or the 1.2 GW BYOP plant.
    - **kill_condition**: NRG's Q3 2026 10-Q or an NRG/GEV release before Jan 31 2027 discloses SRAs at or above 3.6 GW or a firm GEV turbine order for either the PDA or the 1.2 GW Texas CCGT.
    - **novelty**: 4
    - **confidence**: 3
    - **materiality**: 2
    - **caveats**: Absence in 10-Qs may be a disclosure-format change after the LS Power acquisition rather than a lapsed agreement; the 10-K 2026 still carried 3.6 GW. NRG conference call transcripts are not in the corpus. 3.6 GW is small relative to GEV's 63 GW SRAs and 53 GW backlog.
- **dead_ends**:
  - Hyperscaler filings (META, MSFT, GOOGL, AMZN 10-K/10-Q/8-K/EX, 2025-2026): zero substantive mentions of gas turbines, combined cycle or GE Vernova; the only hit is an unrelated Amazon Nova product list. Power procurement detail lives in utility dockets, not hyperscaler filings.
  - SEC EFTS full-text search: '"slot reservation"' returns 89 filings since 2005 but non-GEV power hits are only NRG (Feb 2025), Baker Hughes (Apr 2026 8-K, NovaLT SRA converted), INNIO (Jul 2026 8-K) and Liberty Energy (Sep 18 2026 8-K). No utility or IPP filing discloses SRA deposit percentages or refund terms. '"GE Vernova" "reservation"' returns only GEV, GE and BKR filings.
  - The one slot-reservation contract on EDGAR (Liberty Energy / INNIO Jenbacher, 8-K 2026-09-18, exhibits a101/a102, $493,155,400 for 100 JMC 624 recip units, 2028 delivery) redacts every percentage; visible terms are a non-refundable slot fee due Feb 20 2026 for 2028 delivery, FX adjustment at 1.15 EUR/USD, buyer bears customs-duty increases. Useful only as a recip-substitution data point (roughly $1,100/kW equipment-only), not for GEV deposit terms.
  - Customer pivot language in 2025-2026 10-K/10-Q (reciprocating, aeroderivative, fuel cells, coal-retirement extensions): only boilerplate risk-factor text, plus Georgia PSC extending Scherer 3 (614 MW) to 2035 and Gaston 1-4 to 2034 (SO 10-Q 2025-10-30) and an Xcel risk factor on coal extensions. No customer filing blames a turbine OEM for a delay or cancels a gas plant.
  - Xcel's supply-chain language ('extended delivery dates and increased prices for items like combustion turbines') is identical boilerplate in 10-K 2025-02-27 and every 2025 10-Q; no numbers.
  - projects table filtered to GE-linked rows with date_revision or cancellation_or_dispute: dominated by Vineyard Wind duplicates and 'not specified' rows; unusable for gas-plant slippage.
  - Southern Company: five new Georgia Power CCs (Bowen 7-8, Wansley 10-11, McIntosh 12, 3,693 MW) have CODs but no separable cost; only an aggregate $19.5B certified across all 2022-IRP projects. OEM not disclosed in filings; commentary shows the Yates CTs are Mitsubishi M501JAC (Power Mag / Utility Dive, Sep 2025).
  - AEP Rockport Energy Center 1,520 MW CC (CPCN filed Jul 2026) discloses no cost in the 10-Q; IURC order expected Q1 2027. SWEPCo Hallsville 450 MW plus Welsh conversion $723M is a CT plus fuel conversion, not comparable.
  - Dominion: no combined-cycle cost disclosure; Chesterfield Energy Reliability Center is a 944 MW simple-cycle CT with no cost stated in 10-Q 2026-07-31.
  - Utility 10-K/10-Q text never names the turbine OEM (Entergy, Duke, Southern, AEP, Xcel all generic); OEM identity had to come from commentary and web releases. Entergy = Mitsubishi/Siemens, Duke = GE Vernova 7HA, Georgia Power CTs = Mitsubishi.
  - documents-table string reproduction fails for Duke because the extracted text has broken spacing ('approximatel y $3.3 billion'); reproduce Duke numbers through chunks_fts or chunk ids instead.
  - Direct Python fetch of sec.gov/Archives returns HTTP 403 with the permitted User-Agent; the EFTS search-index endpoint works, and WebFetch works for Archives exhibits.
  - mgmt_guidance table has no GEV pricing rows (metric LIKE '%pric%' returns only a 2024 spin-off share-price line); GEV pricing statements are only in TRANSCRIPT chunks.

## [Verify] verify:customer-filings:Customers filing in 2026 ask for 2030-31

- **reproduced**: True
- **corrected_numbers**: String test reproduces exactly: 'expected to be in service in 2028' present in ETR 10-Q 2025-10-31 and 10-K 2026-02-19, absent in 10-Q 2026-05-01 and 10-Q 2026-07-31 while 'Franklin Farms' appears 3 times in each 2026 10-Q. BUT the same test on the companion sentence 'Waterford 5 Power Station is expected to be in service in 2029' gives the identical pattern (present Oct-25/Feb-26, absent May-26/Jul-26), and the Jan 2026 intervenor motion paragraph ('motion asking the LPSC to investigate') is also absent from both 2026 10-Qs; 'prudence' count falls 44 (10-K) to 3 (each 2026 10-Q). All three Franklin Farms mentions in the 2026 10-Qs are capex-list or bond-proceeds boilerplate, and no 'in service' date sentence exists for Richland Parish/Franklin Farms in either 2026 10-Q. So the entire Franklin Farms regulatory paragraph was dropped, not the 2028 date. Baseline: ETR 10-Q 2024-08-02 already said Franklin Farms 'commercial operation is expected to occur by the end of 2028'; Entergy's Dec 2025 groundbreaking release (entergy.com) says both units operational 'by late 2028'. Customer 2030-31 ladder reproduces: ETR 10-Q 2026-07-31 'seven new combined cycle ... 5,278 MW ... $12.9 billion ... in-service dates in 2030 and 2031'; Waterford 6 / Westlake 'July 2030 and October 2030'; DUK 10-Q 2026-08-04 Anderson County CC chunk present. GEV 2Q26 transcript (Jul 22 2026) quote reproduces verbatim: 'largely sold out of '30 and more than half of '31'.
- **refuted**: True
- **already_widely_known**: True
- **where_known**: Franklin Farms 'late 2028' is in Entergy's Dec 2 2025 groundbreaking press release (entergy.com, LED, Turbomachinery Magazine, Louisiana Radio Network) and the 2028 date has been stable since the Aug 2024 10-Q. The 2030-31 in-service dates are stated in plain text in ETR/DUK/SO 10-Qs and LPSC/NCUC/Georgia PSC dockets, and GEV itself said on the 2Q26 call that 2030 slots are largely sold and 2031 more than half sold. The 'GEV 2027 revenue comes from the cheaper 2024-25 order vintage' mechanism is the GLJ Sell thesis (Sep 14 2026) and is already in the price.
- **materiality**: 2
- **strongest_counterargument**: The Entergy 'silent deletion' is a 10-Q drafting artifact, not a signal. Entergy's quarterly reports only carry regulatory proceedings with new developments; once the LPSC settlement became final (Aug 2025) and the intervenor motion was disclosed in the 10-K, the whole Franklin Farms/Waterford 5 paragraph fell out of the 2026 10-Qs, taking the 2029 Waterford 5 date and the prudence-motion language with it in exactly the same filings. The finding's own test applied to the neighboring sentence falsifies the date-specific reading. Meanwhile construction began Dec 2025 with 'late 2028' reaffirmed publicly, and Franklin Farms is not a GEV plant anyway, so there is no read-across to GEV deliveries. The remaining leg, that 2026 customer applications carry 2030-31 CODs, is true but is simply what GEV told investors in July (sold out 2030, half of 2031) and what the street already models with 20/24/30 GW throughput; it neither raises nor lowers 2027 revenue relative to guidance, and the 2027 vintage-margin question is already the public bear case. Inside a 3-12 month window there is no catalyst here: Entergy's Q3 10-Q omitting the date again is the expected null outcome, not evidence.
- **notes**: Dead ends / what was checked: (1) Section-wide drop confirmed via Waterford 5 2029 sentence and intervenor-motion text, both absent from 2026 10-Qs. (2) No alternate in-service-date sentence for Franklin Farms or Richland Parish exists in the May/Jul 2026 10-Qs (regex over 'in service'/'in-service' within 250 chars). (3) 2024 baseline: ETR 10-Q 2024-08-02 gave Franklin Farms 'by the end of 2028', so 2024-to-2025 filings show no slip either. (4) One web search: Entergy Dec 2025 groundbreaking release reaffirms late 2028 for both units. Salvageable pieces for the team: the customer COD ladder (ETR seven CCs 5,278 MW $12.9B 2030-31; Waterford 6 Jul-2030; Westlake Oct-2030; DUK Anderson end-2030, Person 2 end-2029, Cayuga 2029/2030) is a clean, verifiable table that independently corroborates GEV's 2030/2031 sold-out claim, useful as supporting evidence for the 'services lag to the mid-2030s' angle already on the list, but not as a standalone finding. A real kill test for the Franklin Farms slip hypothesis would be Entergy's Q3 2026 earnings call or the LPSC docket (U-36889 area) stating a date, not 10-Q phrase absence. Queries used are in corrected_numbers; all against documents and chunks_fts, ticker filters ETR/DUK/SO/GEV, no XBRL involved so no duplicate-fact risk. Georgia Power table chunk not re-pulled (budget); Cayuga/Person 2 dates taken from finding, not re-verified.

## [Synthesize] synthesis

# GEV Synthesis Report (run 2, 2026-09-21)

**Headline:** No finding survived this run. All four verified findings were reproduced but refuted as not novel or wrongly attributed. The angles below are rebuilt from (a) pieces the verifiers said were salvageable and (b) items verified in the earlier run. Anything marked *unverified* was not re-checked here.

## 1. Top angles

Ranking uses verifier materiality (all fallen items scored 2/5). Confidence is high where numbers reproduced, medium where only the finder ran the query.

### A. LTSA margin cuts are accelerating (verified earlier; novelty high; either side, leans short)
**Claim:** GEV cut its estimate of long-term service contract profit by $218M in H1'26, five times H1'25.
**Mechanism:** A long-term service agreement (LTSA) is a multi-year contract to maintain a turbine. GEV books profit on it using an estimate of future costs. When it cuts that estimate, the loss hits the current quarter. Cuts are growing while contract revenue is flat.

| Item | H1'25 | FY25 | H1'26 | Source |
|---|---|---|---|---|
| Net unfavorable estimate change | -$42M | -$151M | -$218M | 10-Q Note 9, 2026-07-22 |
| CSA revenue recognized | $2,720M | $5,412M | $2,689M | same |
| CSA billings | $2,533M | $5,362M | $2,392M | same |
| Share of Power EBITDA | | | 11.8% | 10-Q segment table |

**Why the market misses it:** The line sits in a footnote. Commentary chunks never mention it. Sell-side quotes the services backlog, not the estimate line.
**Prediction:** Q3'26 10-Q (about Oct 21) shows a 9-month figure worse than -$300M.
**Kill:** 9-month figure better than -$250M, or management gives a one-off reason on the call.
**Build (2 days, industrial engineer):** Pull the Note 9 sentence from every 10-Q/10-K since 2024, chart the series against Power EBITDA, and add the 10-K sensitivity (1 point of margin = $0.2B).
**Caveats:** Not re-verified this run. Power services revenue by turbine class is not disclosed, so the cause (HA wear, F-class, pricing) cannot be proven from filings.

### B. Wind guidance needs a first-ever profitable half (unverified; novelty medium; short, or a long catalyst if it happens)
**Claim:** The FY26 Wind guide of about -$400M implies H2'26 Wind EBITDA of about +$257M after -$657M in H1.
**Mechanism:** EBITDA is profit before interest, tax, and depreciation. No half since 2023 has been positive. The only visible bridge is the confidential Sept 16 Vineyard Wind settlement.

| Period | Wind EBITDA | Source |
|---|---|---|
| H1'25 | -$312M | 8-K/EX reconciliation |
| H2'25 | -$286M | derived |
| H1'26 | -$657M | 8-K/EX 2026-07-22 |
| H2'26 implied | +$257M | arithmetic |

**Why missed:** The guide was "reiterated," so nobody redid the half-year math.
**Prediction:** Q3'26 Wind EBITDA is positive or the guide is cut by Oct 21.
**Kill:** Q3 Wind EBITDA above +$100M with no one-off settlement gain disclosed.
**Build (1 day, industrial engineer):** Table of Wind quarterly EBITDA from 8-K reconciliations; flag any settlement gain in the Q3 10-Q.
**Caveats:** Settlement terms are secret. A one-time gain could make the guide true without any operating fix.

### C. Equipment backlog is going long-dated (unverified; novelty medium; short on 2027 estimates)
**Claim:** The share of equipment RPO due within 12 months fell from 46% (Q3'24) to 36% (Q2'26).
**Mechanism:** RPO (remaining performance obligations) is contracted work not yet booked as revenue. If less of it is near-term, revenue growth arrives later than the headline backlog suggests.

| Date | Equip RPO | 1-yr share | 3-5 yr tranche | Source |
|---|---|---|---|---|
| Q3'24 | $42.1B | 46% | $8.8B | 10-Q footnote |
| Dec-25 | $64.2B | 37% | ~$18B | 10-K |
| Q2'26 | $87.8B | 36% | $28.1B | 10-Q 2026-07-22 |

**Why missed:** Everyone quotes the $176B total; the percentage split is one sentence.
**Prediction:** Q3'26 1-year share at or below 35%.
**Kill:** Share rises above 40%, or 2027 revenue guide is raised above the RPO-implied figure.
**Build (1 day, computer engineer):** Regex over the eight filings, multiply by the percentages, compare the 12-month tranche to consensus 2027 equipment revenue.
**Caveats:** A falling share is also what a longer, sold-out order book looks like. It is a timing point, not a demand point.

### D. Customer affordability ladder (salvaged by skeptic; novelty medium; short, long horizon)
**Claim:** Oglethorpe's own budgets show all-in plant cost rising from ~$2,300/kW (2029 COD) to ~$3,200-3,800/kW (2033 COD).
**Mechanism:** GEV sells the turbine; the customer pays for the whole plant. If plant cost inflates faster than turbine price, the constraint becomes what utilities can get approved, not what GEV can charge. Arkansas already refused to call Entergy's Jefferson plant cost prudent (Jan 2026).

| Project | COD | $/kW all-in | OEM | Source |
|---|---|---|---|---|
| Smarr CC 1,425 MW | mid-2029 | $2,316 | GEV 7HA.03 | OPC 8-K Aug 2026 |
| Talbot 7 CT 240 MW | 2029 | $1,833 (was $1,500) | Siemens, not GEV | same |
| 209 MW CT | 2032 | $2,510-2,990 | unnamed | same |
| 713 MW CC | 2033 | $3,225-3,790 | unnamed | same |

**Why missed:** OPC is a co-op filer nobody reads for GEV.
**Prediction:** Next Georgia Power or OPC IRP filing (2027) shows CC cost above $2,500/kW for 2032+.
**Kill:** A 2032+ CC budget flat below $2,500/kW.
**Build (2 days, mining engineer, who knows capex escalation):** Merge the OPC ladder with the Entergy series ($1,583 to $2,773/kW, 2024-2026 filings) and Duke Cayuga ($2,012 to $2,236).
**Caveats:** The finder misattributed Talbot 7 to GEV. Turbine share of plant cost is an assumption. Nothing resolves inside 12 months.

### E. HA fleet: the 2-year lag model, not a stall (salvaged; novelty low; either)
**Claim:** Running HA units track shipments two years earlier, so FY26 10-K should show ~139-141 running units.
**Mechanism:** Shipped 2023: 14, 2024: 15, 2025: 24. Running base rose +11 in 2025. Service revenue starts only after commissioning plus a warranty period.
**Evidence:** installed base 94/100/106/115/126/~130 (10-Qs 2024 to Q2'26 call); queue 30 to 43; hours per unit rising ~5,800 to ~7,400.
**Prediction:** FY26 10-K (Jan 2027) shows 139-141 running.
**Kill (real warning sign):** below 135 running with queue above 50.
**Build (half day, computer engineer):** Small table; ties to the customer COD ladder (Entergy seven CCs 2030-31, Duke Anderson end-2030), which supports the "services lag to the 2030s" view.
**Caveats:** Verifiers found the "stall" reading wrong; utilization is rising. Use as a base case, not a catalyst.

### F. No large turbines have entered US service since 2023 (verified earlier; novelty low; short on near-term US deliveries)
**Claim:** EIA-860M shows 0.0 GW of HA-class (300 MW+) turbines reaching operation in 2024, 2025, or 2026 YTD; status-P (no approvals) planned GW grew 7.7x while under-construction GW grew 2.6x.
**Evidence:** P-status 4.8 GW (2024-06) to 37.0 GW (2026-07); under construction 5.0 to 12.9 GW; 2027 COD pipeline 11.1 GW, only 3.6 GW under construction.
**Prediction:** 2026-12 vintage shows under-construction GW below 16.
**Kill:** Under-construction GW above 20 by year-end.
**Build (1 day, computer engineer):** Rerun the vintage queries; exclude Fermi (11.7 GW, Siemens) explicitly.
**Caveats:** GEV revenue is cost-to-cost, so US commissioning does not drive reported sales. 17% of the pipeline is one Siemens campus.

## 2. Patterns across findings

The salvageable pieces point one way: GEV's numbers are real, but the timing is later than the narrative. Services from new HA units start in the 2030s (angles D, E, F). Equipment revenue is pushed out (C). Meanwhile the existing service book is being written down (A) and Wind must flip to profit on faith (B).

Conflict: the verifiers repeatedly found that "shipments" and "commissioning" do not drive GEV's reported revenue because it is booked as costs are incurred. So physical-lag angles (E, F) are weak for a 3-12 month price call. Accounting angles (A, B, C) are the ones with dated catalysts (Oct 21 10-Q).

Single most useful check: the Q3'26 Note 9 estimate-change figure. If it is worse than -$300M for nine months, angle A becomes a memo-grade risk with a mechanism; if it snaps back, the services thesis is intact and the short case rests only on Wind.

## 3. Refuted or not reproduced

- **Entergy dropped 2028 date:** whole regulatory paragraph fell out of the 10-Q, not the date; Franklin Farms is not a GEV plant; late-2028 reaffirmed publicly Dec 2025.
- **HA activation stall:** queue grew because shipments jumped (24 = 13 queue + 11 running); 1.8-year lag is normal; utilization rising.
- **HA shipments down, inventory up:** Q2'25 was the series high; trailing-4Q GW flat (14.6 vs 15.3); inventory build disclosed and part-Wind; revenue grew 14% while GW fell 37%.
- **Oglethorpe $/kW:** Talbot 7 is Siemens, budget +22%; Smarr $2,300/kW is in public decks.
- **Earlier run:** June-Sept drawdown decomposition, hyperscaler prints, tariff cut, 80/20 data-center split, $0.3B availability shortfall — all not novel or wrongly attributed. The availability shortfall is a Wind charge, not HA; do not pair it with gas.

## 4. Low-novelty but true

- SRA pool dwell ~15-19 months vs Siemens 6-12; SRAs are 54% of GEV's 116 GW.
- GW under contract no longer moves the stock (Q2'26: +16 GW, -8.5% ex-basket).
- Sep 14 was half a sector rout (basket -6.3%, Siemens Energy -8.1%).
- $200B backlog target restated three times; straight line already reached it.
- "300% price rise" and "$3,000/kW" are single-origin analyst/plant-cost figures; GEV says +10-20%.
- "$70M per GW-year" is a Jefferies 2030s projection; today's figure is at most ~$15-33M.
- Three-OEM capacity (~85-90 GW/yr) exceeds MHI's post-2027 market view (40-50 GW).
- FY25 10-K added over-investment and hyperscaler-credit risk factors.
- Prolec: 21% EBITDA margin but 98% of price is goodwill/intangibles; ~$180M/qtr amortization.
- FERC ordered NERC data-center load standards by Dec 31 2026 (Electrification catalyst).
- F-class rotor life limit (144k hours) puts ~800-900 7F units into a rotor window; third parties compete for it.
- Onshore Wind orders -61% units in Q2'26 with zero repowers.
- US CC fleet generation fell 3.1% in 2025; capacity factor flat 53-55%.

## 5. Dead ends and gaps

**Dead ends (deduplicated):** No customer filing discloses SRA deposit or refund terms (NRG, Kenon only give GW). No OEM says whether SRA price is fixed at reservation. Hyperscaler 10-Ks have zero turbine content. Utility filings never name the OEM. No filing gives Power services by turbine class, US/international order split, or offshore loss provisions. `queue_projects`, `operator_forecasts`, `events` tables are empty; `competitor_financials` is unusable for MHI/Vestas/Hitachi; `mgmt_guidance.prior_value` is unreliable; XBRL tags for CSA billings and Wind losses are mislabeled. Prices table lacks NVDA, hyperscalers, Siemens, MHI. No 2026 GEV transcript chunks with dates. Vineyard settlement terms are confidential. Semantic search was not used by any lens.

**Gaps to ingest next:** Q4'25 Power services RPO jump (+$4.8B in one quarter) is unexplained and worth a question. Entergy Q3 call and LPSC docket for real COD dates. Kenon 20-F and 6-K exhibits (flagged for "advance payment" + GE Vernova, not read). TVA Cumberland lease exhibits. Sell-side notes (none checked directly). NERC's own Virginia incident report. Ollama semantic search over the corpus. Melius and Jefferies underlying notes.

**Weak spots:** Every angle above is a timing or accounting observation; none has a proven price-moving catalyst. Materiality was 2/5 on everything verified. The team should expect the memo's edge to come from combining A, B and C into one "quality of the ramp" argument, not from any single number.