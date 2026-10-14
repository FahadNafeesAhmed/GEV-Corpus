# The public database

`gev_public.db` is a single SQLite file, about 2.1 GB, built from the private research database by `scripts/build_public_db.py` on 14 October 2026. It is too large for this repository and is distributed separately.

Download: _link to be added by the maintainer after upload_.

Open it with any SQLite client, with Python's built-in `sqlite3`, or in a browser with Datasette (`datasette data/gev_public.db`). The table `public_build` inside the file records how it was built and the row count of every table.

## Tables

| Table | Rows | What it holds |
|---|---|---|
| `filings` | 17,744 | EDGAR filing index for the universe and its peers (18 tickers). |
| `documents` | 9,715 | Full text of each ingested filing: 10-K, 10-Q, 8-K, proxy statements, registration statements, annual reports to shareholders. |
| `chunks` | 426,164 | Passages of about 1,500 characters cut on SEC item boundaries, with ticker, form, date and section. 418,597 come from filings and 7,567 from the pipeline's own research notes. |
| `chunks_fts` | | FTS5 full-text index over `chunks` (Porter stemming). |
| `xbrl_facts` | 339,610 | Facts from the SEC XBRL company-facts API, with tag, unit, period, fiscal year and accession. |
| `insider_tx` | 7,603 | Form 4 transactions. |
| `guidance` | 4,005 | Guidance statements extracted from filings by the local model, with quote and period. |
| `mgmt_guidance` | 1,087 | Guidance history derived from `guidance`: metric, value, period, direction, prior value. |
| `risk_items` | 385 | Risk factors extracted from filings, with category and severity. |
| `claims` | 3,982 | Claims extracted from research, web and competitor sources: topic, stance, whether a number is present, and the supporting quote. |
| `extractions` | 6,311 | Raw extractor output per chunk (JSON payload, extractor name, model, timing). |
| `insights` | 16 | Insight cards from disagreement testing: claim, support and opposition counts, what would falsify it, catalyst date. |
| `analyst_calls` | 191 | Analyst statements captured from published summaries, with firm, metric, value and date. |
| `competitor_financials` | 251 | Segment figures for competitors taken from their own reports. |
| `transcript_statements` | 193 | Statements from an earnings call, by topic and speaker role. |
| `backlog_quarterly` | 6,930 | Remaining performance obligations, contract liabilities and related metrics by quarter, from filing notes. |
| `generators` | 1,575,165 | EIA-860M monthly generator inventory, every vintage. |
| `generation` | 75,525 | EIA-923 generation data. |
| `projects` | 420 | Power and data-centre projects collected from public sources. |
| `comps_inputs` | 271 | Comparables inputs from XBRL and derived from them. |
| `sources` | 4,122 | Web, news, academic, competitor and operator sources: URL, title, date, kind and tier. Stored text is kept only for the pipeline's own notes. |
| `source_versions` | 4,147 | Version history of those sources (same text rule). |
| `catalyst_calendar` | 16 | Dated events watched by the thesis. |
| `ingest_log` | 6,472 | Pipeline log. |
| `events`, `queue_projects`, `operator_forecasts` | 0 | Present in the schema, unused in this build. |
| `public_build` | | How this copy was built. |

The schema is defined in `src/common.py`.

## What was removed, and why

| Removed | Reason | How to get it back |
|---|---|---|
| `prices` (daily closes for 18 tickers) | Vendor terms do not allow redistribution. | `python src/ingest_market.py` re-downloads them. |
| `embeddings` (177 thousand vectors) | Regenerable; 545 MB. | `python src/embed.py` with `nomic-embed-text`. |
| Bloomberg-sourced rows in `sources` | Licensed data. | Not available. |
| LinkedIn-sourced rows in `sources` | Personal data. | Not available. |
| Yahoo-sourced rows in `comps_inputs` | Vendor terms. | Recomputed by `src/derive.py`. |
| Stored text of third-party sources | Copyright. URL, title and date remain. | `python src/ingest_web.py` re-fetches them. |
| Web, news, academic and competitor passages in `chunks` | Same. | Rebuilt by `src/build_index.py` after re-fetching. |

Local file paths in the pipeline's own notes were replaced with relative or generic ones. The underlying public data, SEC filings and EIA tables, is unchanged.
