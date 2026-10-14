# Verify (REPRODUCE): electrification-q3-orders

_Research input only: facts, arithmetic, sources. Bloomberg data cited as "Bloomberg, 2026-10-01" (academic licence, keep inside the project folder). Checker role: try to kill the candidate._

## Verdict

- Reproduced: YES. Every cited number was recomputed from the primary files. Two small corrections (below).
- Survives: NO. The corrected centre gap is still large (-17% to -20%), but the candidate's error band is too narrow. An honest band on "our value" is about +/-30%, wider than the gap, and the Street figure sits inside it.
- Why it fails in one line: the CEO gave a SHARE (about 20%), not a LEVEL. The share only becomes a dollar figure after you assume the non-data-centre level, and that level has swung between $3.6B and $6.3B over the last four quarters.

## 1. Street value: reproduced

| Item | Candidate | Recomputed | Source |
|---|---|---|---|
| Q3 2026 Electrification orders, mean | 6,498 | 6,498.11 | Bloomberg, 2026-10-01: `segment_quarterly.json` key `Orders||Electrification|2026 Q3`; same cell in `01-eeo-company-specific.xlsx` (field IS_ORDERS_RECEIVED_VALUE, segment row) |
| Low / median / high | 5,775 / 6,307 / 7,498 | 5,774.85 / 6,306.68 / 7,498.40 | Bloomberg, 2026-10-01: `06_modl.xlsx`, period 2026:Q3 |
| Q4 2026 mean | 7,492 | 7,491.97 | same JSON |
| H2 2026 | 14.0B | 13,990 | sum |
| RPO-implied Q3 orders | 6,316 | 46,998.4 - 44,563 + 3,880.7 = 6,316.1 | same JSON (RPO and revenue rows) |
| Definition match | assumed | Bloomberg "2026 Q2 (Rep)" = 6,347 = the company's segment-table "Orders" | Q2 release, 8-K exhibit 0001996810-26-000147 |

Flags on the Street figure:
- Broker count is not in the export (per-broker cells are blank). Arithmetic on mean / median / low / high rules out 2, 3 and 4 contributors (n=3 would give a mean of 6,527; n=4 would give 6,472), so there are at least 5. Against 35-36 brokers on the EBITDA line, this is a thin consensus.
- No estimate dates. It is not possible to tell whether these brokers updated after the 2026-09-16 conference.
- Mean and median differ by 3% (6,498 vs 6,307). The gap should be quoted against both.

## 2. Company inputs: reproduced, one correction

| Item | Candidate | Recomputed | Source |
|---|---|---|---|
| Q1 2026 orders | 7,112 | 7,112 | 8-K exhibit 0001996810-26-000063, segment table |
| Q2 2026 orders | 6,347 | 6,347 | 8-K exhibit 0001996810-26-000147, segment table |
| H1 2026 | 13,460 | 13,459 by sum; the release prints 13,460 | same |
| Data-centre orders Q1 | about 2.4B | $2.4B ("booked $2.4 billion in equipment orders to support data centers") | Q1 release, same exhibit |
| Data-centre orders Q2 | not stated (2.6-3.0B implied) | **$2.7B** ("In 2Q, we booked $2.7 billion of data center orders in Electrification") | Q2 call transcript, `sources` id 3161 |
| Data-centre orders H1 | 5,000-5,380 | **5,100** (2.4 + 2.7; each rounded to +/-0.05B) = 37.9% of H1 | computed |
| "almost 40%", "more like 20% ... in 3Q and 4Q" | quoted | Confirmed word for word in the company transcript PDF (gevernova.com, Morgan Stanley Laguna conference, 2026-09-16; fetched 2026-10-01). The PDF is not in gev.db; only news summaries are (`sources` id 681) | company transcript |
| India HVDC | Q4, almost $1.5B | Confirmed: "won't cut in as an order until the fourth quarter ... almost a $1.5 billion transaction" | same transcript |
| Q3 2025 orders | 5,110, no Prolec | 5,110; included $1.6B Saudi synchronous condensers | 8-K exhibit 0001996810-25-000159 |
| Prolec consolidation date | not stated | "commencing on February 2, 2026" (so Q1 2026 holds about two months) | 10-Q 0001996810-26-000148 |
| Prolec + currency in orders | about 0.9B | Q1: 7,112 - 3,366 x 1.86 = 851; Q2: 6,347 - 3,283 x 1.66 = 897 | releases (organic growth rates) |
| Report-day moves | +1.5 / -4.5 / +3.1 / +14.6 / +13.75 / -8.69; +4.8 on 09-16 | +1.46 / -4.45 / +3.07 / +14.58 / +13.75 / -8.69; +4.79 | gev.db `prices` |
| H2 total orders needed for "$200B very early 2027" | 44.6-48.6B vs Street 45.4B | (195,000 to 199,000) - 176,300 + 25,908 = 44,608-48,608; Street 45,403 | Bloomberg JSON; Q2 release |

Other statements in the same transcript that bear on the number (all confirmed):
- "the orders we expect to see in the third quarter" and "a very strong third quarter orders performance" (company total, tied to gas slot reservations converting).
- "growing the backlog, both the Electrification backlog and the data center backlog, in 3Q, 4Q, but maybe not at the same run rate as the first half".
- "I expect us to continue to grow our backlog in a very healthy way in both 3Q and 4Q in Electrification."
- "Electrification can be a little bit more lumpy, both with data centers and, frankly, the non-data center business".
- Q2 call guide for Q3: "continued solid equipment orders with healthy margins"; Q3 revenue $3.8-4.0B.

## 3. The candidate's arithmetic: reproduced, centre corrected slightly

Non-data-centre orders = segment orders less data-centre orders.

| | Q1 2026 | Q2 2026 | H1 average |
|---|---|---|---|
| Orders | 7,112 | 6,347 | 6,730 |
| Data centre | 2,400 | 2,700 | 2,550 |
| Non-data-centre | 4,712 | 3,647 | 4,180 (candidate used 4,130) |

Q3 orders = non-data-centre / (1 - share):

| Non-data-centre base | Share 15% | Share 20% | Share 25% |
|---|---|---|---|
| 3,647 (Q2 level) | 4,291 | 4,559 | 4,863 |
| 4,180 (H1 average) | 4,917 | **5,224** | 5,573 |
| 4,712 (Q1 level) | 5,544 | 5,890 | 6,283 |

- Corrected centre 5,224 (candidate 5,160). Gap: -19.6% vs mean, -17.2% vs median (candidate -20.6% vs mean).
- Candidate's own figures check: 4,130 / 0.80 = 5,163; 3,600 / 0.80 = 4,500; 4,700 / 0.80 = 5,875; 4,130 / 0.75 = 5,507; 4,700 / 0.75 = 6,267.
- What the Street needs at a 20% share: non-data-centre of 5,198 (mean) or 5,045 (median). Or, with non-data-centre at 4,180, a data-centre share of 36% (mean) or 34% (median).

## 4. Why the band is wider than the gap (the kill)

### 4a. The base is two data points, and they are the two lowest of the last four

Non-data-centre orders, last four quarters ($M). Data-centre orders in 2025: about $0.5B in H1, about $0.9B through Q3, "over $2 billion" for the year (news summaries `sources` src:3496 and src:1853; Q4 2025 call, `sources` id 2660). So about 0.4B in Q3 2025 and about 1.1B in Q4 2025. These 2025 splits are approximate.

| Quarter | Orders | Data centre | Non-data-centre | With Prolec added pro forma (about 0.9B a quarter; +0.3B for the missing month in Q1 2026) |
|---|---|---|---|---|
| Q3 2025 | 5,110 | about 400 | about 4,710 | about 5,610 |
| Q4 2025 | 7,424 | about 1,100 | about 6,320 | about 7,220 |
| Q1 2026 | 7,112 | 2,400 | 4,712 | about 5,010 |
| Q2 2026 | 6,347 | 2,700 | 3,647 | 3,647 |
| Mean | | | 4,848 | 5,373 |
| Standard deviation (share of mean) | | | 1,104 (23%) | 1,482 (28%) |

Q3 orders at a 20% share from each base:

| Base | Non-data-centre | Q3 orders | vs Street mean 6,498 |
|---|---|---|---|
| H1 2026 average (the candidate's choice) | 4,180 | 5,224 | -19.6% |
| Four-quarter average, as reported | 4,848 | 6,060 | -6.7% |
| Four-quarter average, Prolec pro forma | 5,373 | 6,717 | +3.4% |
| Range of the four quarters | 3,647 to 6,320 | 4,559 to 7,905 | -30% to +22% |

The whole gap comes from choosing a two-quarter base instead of a four-quarter base. Nothing in the filings says which is right.

### 4b. Quarterly Electrification orders are very lumpy

Orders by quarter (releases, as first reported): 2023: 3,856 / 5,011 / 2,143 / 2,193. 2024: 3,571 / 4,823 / 2,510 / 4,786. 2025: 3,393 / 3,338 / 5,110 / 7,424. 2026: 7,112 / 6,347.

- Each quarter divided by the average of the two before it (12 observations): minimum 0.48, lower quartile 0.66, median 1.03, upper quartile 1.61, maximum 1.76. Standard deviation of the log ratio 0.45.
- The candidate lets the non-data-centre base move only -13% / +13% (3,600 to 4,700). History says one quarter routinely moves 35-50% against the prior two.
- Q3 divided by the H1 average: 0.48 (2023), 0.60 (2024), 1.52 (2025; 1.04 without the $1.6B Saudi order). The Street is at 0.97 (mean) and 0.94 (median) for 2026. This supports the DIRECTION (Q3 is often the seasonal low) but not a number: three observations, spread 0.48 to 1.52.

### 4c. The spoken remark does not fix a level

- "More like 20% ... in 3Q and 4Q" is a share, and may describe the half rather than each quarter.
- A 20% share with data-centre orders at half the H1 pace (about 1.3B) gives 6.5B, which is the Street mean. A 20% share with data-centre orders at 1.0B gives 5.0B. The transcript says only that data-centre orders will run below the $2.5B quarterly pace. Both readings fit.
- The same speaker said the non-data-centre business is lumpy too.

### 4d. Corrected band

| Quantity | Value |
|---|---|
| Our value, centre (candidate's method, corrected input) | 5,224 |
| Candidate's band | 4,500-5,875 (-14% / +12% on our value) |
| Honest band (non-data-centre base 3,647-6,320, share 20%) | 4,559-7,905 |
| Honest band with share 15-25% | about 4,290-8,430 |
| One-standard-deviation band from the four-quarter series | +/-23% to +/-28% on the base; about +/-30% once share uncertainty (+/-6%) is added |
| Gap vs Street mean / median | -19.6% / -17.2% |

The gap (17-20%) is smaller than the band (about 30%). The Street mean and median both sit inside the band. Test failed.

## 5. What does hold up (for anyone who still wants the line as a dated check)

- The inputs are real, public and exactly quoted. The arithmetic is right.
- Direction lean: below the Street is more likely than above. Reasons: the CEO chose to pre-warn two weeks before quarter end; Q3 has been the seasonal low in two of three years; the India HVDC order is confirmed for Q4, not Q3; the Street needs a non-data-centre quarter above both H1 quarters if the 20% share is taken literally.
- It is a lean, not a number. It cannot carry a thesis: no revenue, EBITDA or cash effect inside the horizon (the candidate says this itself), and the remark has been public since 2026-09-16 (stock +4.79% that day).
- Read-out on 2026-10-28: segment table "Orders". Below 5,775 = under every contributing broker. The year-ago comparison in that release will be the recast figure (H1 2025 was recast from 6,731 to 6,649, so Q3 2025 may print slightly below 5,110).

## 6. Corrections to carry forward

1. Data-centre orders in Q2 2026 are disclosed: $2.7B (Q2 call). H1 = $5.1B, not a 5.0-5.38 range. Centre moves from 5,160 to 5,224.
2. Quote the gap against the median as well: -17.2%.
3. Street contributor count is unknown (at least 5); estimate dates unknown.
4. Prolec is consolidated from 2026-02-02, so Q1 2026 holds about two months of it.
5. The band must include the four-quarter non-data-centre range (3.6-6.3B), not only the two H1 quarters.
