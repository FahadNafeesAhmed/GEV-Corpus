"""Shared config, HTTP session, and SQLite schema for the GEV corpus."""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import time
import threading
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = ROOT / "raw"
CONFIG_PATH = ROOT / "config" / "config.json"
UNIVERSE_PATH = ROOT / "config" / "universe.json"
DB_PATH = DATA / "gev.db"

# The subject of the pitch. Everything else in the universe exists for comparison.
CIK = "0001996810"
CIK_INT = 1996810
TICKER = "GEV"


def load_universe() -> list[dict]:
    """Ticker coverage config. Falls back to GEV alone if the file is missing."""
    try:
        doc = json.loads(UNIVERSE_PATH.read_text(encoding="utf-8"))
        rows = doc["tickers"]
        for r in rows:
            r.setdefault("since", doc.get("since", "2021-01-01"))
        return rows
    except Exception as exc:
        log(f"universe.json unreadable ({exc}); falling back to GEV only")
        return [{"ticker": TICKER, "cik": CIK, "name": "GE Vernova Inc.",
                 "tier": "A", "role": "subject", "since": "2000-01-01"}]


def universe_by_tier(*tiers: str) -> list[dict]:
    return [t for t in load_universe() if t["tier"] in tiers]

DEFAULT_CONFIG = {
    # SEC's fair-access policy asks for a real contact. A bare agent gets a hard
    # 403; a descriptive one works. Put a real email here to avoid being blocked.
    "sec_user_agent": "GEV Equity Research Project research-contact@example.com",
    "sec_requests_per_second": 5.0,
    "max_filing_bytes": 40_000_000,
    "chunk_chars": 1500,
    "chunk_overlap": 200,
    "forms_full_text": ["10-K", "10-Q", "8-K", "DEF 14A", "DEFA14A", "S-1", "S-1/A",
                        "424B3", "424B5", "10-12B", "10-12B/A", "ARS", "11-K", "SD"],
}


def load_config() -> dict:
    cfg = dict(DEFAULT_CONFIG)
    if CONFIG_PATH.exists():
        try:
            cfg.update(json.loads(CONFIG_PATH.read_text(encoding="utf-8")))
        except Exception as exc:  # a broken config should not kill an overnight run
            log(f"config unreadable ({exc}); using defaults")
    return cfg


def write_default_config() -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG, indent=2), encoding="utf-8")


# Log output is redirected to a file on Windows, whose default encoding cannot
# represent every character in a paper title; one query died of that on run 2.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def log(msg: str) -> None:
    ts = time.strftime("%H:%M:%S")
    try:
        print(f"[{ts}] {msg}", flush=True)
    except UnicodeEncodeError:
        print(f"[{ts}] {msg.encode('ascii', 'replace').decode()}", flush=True)


class RateLimiter:
    """Simple thread-safe minimum-interval limiter (SEC allows 10 req/s; we use less)."""

    def __init__(self, per_second: float):
        self.interval = 1.0 / max(per_second, 0.1)
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self) -> None:
        with self._lock:
            delta = time.monotonic() - self._last
            if delta < self.interval:
                time.sleep(self.interval - delta)
            self._last = time.monotonic()


class Fetcher:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.limiter = RateLimiter(cfg["sec_requests_per_second"])
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": cfg["sec_user_agent"],
            "Accept-Encoding": "gzip, deflate",
        })

    def get(self, url: str, tries: int = 4, timeout: int = 60, headers: dict | None = None):
        """GET with rate limiting and backoff. Returns a Response or None."""
        for attempt in range(tries):
            self.limiter.wait()
            try:
                r = self.session.get(url, timeout=timeout, headers=headers)
                if r.status_code == 200:
                    return r
                if r.status_code in (403, 429, 503):
                    wait = 2 ** attempt
                    log(f"  HTTP {r.status_code} on {url[:80]} - backing off {wait}s")
                    time.sleep(wait)
                    continue
                log(f"  HTTP {r.status_code} on {url[:80]} - giving up")
                return None
            except Exception as exc:
                wait = 2 ** attempt
                log(f"  {type(exc).__name__} on {url[:80]} - retry in {wait}s")
                time.sleep(wait)
        return None


SCHEMA = """
CREATE TABLE IF NOT EXISTS filings (
    accession     TEXT PRIMARY KEY,
    form          TEXT,
    filing_date   TEXT,
    report_date   TEXT,
    primary_doc   TEXT,
    url           TEXT,
    items         TEXT,
    size          INTEGER,
    fetched_at    TEXT
);
CREATE INDEX IF NOT EXISTS ix_filings_form ON filings(form, filing_date);

CREATE TABLE IF NOT EXISTS documents (
    id            INTEGER PRIMARY KEY,
    accession     TEXT,
    form          TEXT,
    filing_date   TEXT,
    url           TEXT,
    n_chars       INTEGER,
    text          TEXT,
    UNIQUE(accession, url)
);

CREATE TABLE IF NOT EXISTS chunks (
    id            INTEGER PRIMARY KEY,
    accession     TEXT,        -- SEC accession, or 'src:<sources.id>' for web content
    form          TEXT,
    filing_date   TEXT,
    section       TEXT,
    ord           INTEGER,
    text          TEXT
);
CREATE INDEX IF NOT EXISTS ix_chunks_acc ON chunks(accession);
CREATE INDEX IF NOT EXISTS ix_chunks_section ON chunks(section);

CREATE TABLE IF NOT EXISTS xbrl_facts (
    id            INTEGER PRIMARY KEY,
    taxonomy      TEXT,
    tag           TEXT,
    label         TEXT,
    unit          TEXT,
    start_date    TEXT,
    end_date      TEXT,
    fy            INTEGER,
    fp            TEXT,
    form          TEXT,
    accession     TEXT,
    frame         TEXT,
    val           REAL,
    UNIQUE(tag, unit, start_date, end_date, accession, frame)
);
CREATE INDEX IF NOT EXISTS ix_facts_tag ON xbrl_facts(tag, end_date);

CREATE TABLE IF NOT EXISTS prices (
    date   TEXT PRIMARY KEY,
    open   REAL, high REAL, low REAL, close REAL, volume REAL, adjclose REAL
);

CREATE TABLE IF NOT EXISTS insider_tx (
    id            INTEGER PRIMARY KEY,
    accession     TEXT,
    filed_date    TEXT,
    owner         TEXT,
    role          TEXT,
    tx_date       TEXT,
    security      TEXT,
    code          TEXT,
    acq_disp      TEXT,
    shares        REAL,
    price         REAL,
    shares_after  REAL,
    UNIQUE(accession, tx_date, security, code, shares, price)
);

CREATE TABLE IF NOT EXISTS holders (
    id            INTEGER PRIMARY KEY,
    accession     TEXT,
    filed_date    TEXT,
    form          TEXT,
    holder        TEXT,
    shares        REAL,
    pct           REAL,
    UNIQUE(accession, holder)
);

CREATE TABLE IF NOT EXISTS news (
    id            INTEGER PRIMARY KEY,
    url           TEXT UNIQUE,
    source        TEXT,
    published     TEXT,
    title         TEXT,
    text          TEXT,
    retrieved_at  TEXT
);

CREATE TABLE IF NOT EXISTS ingest_log (
    source     TEXT,
    key        TEXT,
    status     TEXT,
    detail     TEXT,
    ts         TEXT,
    PRIMARY KEY (source, key)
);

-- LLM extractions. One row per (chunk, extractor). `payload` holds the model's
-- JSON; `ok` records whether it parsed, so a re-run can retry only the failures.
CREATE TABLE IF NOT EXISTS extractions (
    id          INTEGER PRIMARY KEY,
    ticker      TEXT,
    chunk_id    INTEGER,
    extractor   TEXT,
    model       TEXT,
    ok          INTEGER,
    payload     TEXT,
    elapsed_ms  INTEGER,
    ts          TEXT,
    UNIQUE(chunk_id, extractor)
);
CREATE INDEX IF NOT EXISTS ix_extr ON extractions(extractor, ticker, ok);

-- Flattened, queryable view of what the extractors found.
CREATE TABLE IF NOT EXISTS guidance (
    id          INTEGER PRIMARY KEY,
    ticker      TEXT,
    chunk_id    INTEGER,
    accession   TEXT,
    form        TEXT,
    filing_date TEXT,
    metric      TEXT,
    value       TEXT,
    period      TEXT,
    direction   TEXT,
    quote       TEXT
);
CREATE INDEX IF NOT EXISTS ix_guid ON guidance(ticker, filing_date);

CREATE TABLE IF NOT EXISTS risk_items (
    id          INTEGER PRIMARY KEY,
    ticker      TEXT,
    chunk_id    INTEGER,
    accession   TEXT,
    form        TEXT,
    filing_date TEXT,
    category    TEXT,
    summary     TEXT,
    severity    TEXT,
    quote       TEXT
);
CREATE INDEX IF NOT EXISTS ix_risk ON risk_items(ticker, filing_date, category);

-- Checkable claims from non-filing sources. The mismatch engine compares these
-- against guidance/risk_items/xbrl_facts: same topic, different tier, different number.
CREATE TABLE IF NOT EXISTS claims (
    id          INTEGER PRIMARY KEY,
    ticker      TEXT,
    chunk_id    INTEGER,
    accession   TEXT,          -- 'src:<id>'
    kind        TEXT,          -- ARXIV | OPENALEX | WEB | NEWS | YOUTUBE | RSS
    published   TEXT,
    topic       TEXT,
    claim       TEXT,
    stance      TEXT,
    has_number  INTEGER,
    quote       TEXT
);
CREATE INDEX IF NOT EXISTS ix_claims ON claims(ticker, topic, stance);

-- Embeddings, stored as raw float32 blobs. 6k vectors is far too few to justify
-- a vector database; brute-force cosine in numpy is sub-millisecond.
CREATE TABLE IF NOT EXISTS embeddings (
    chunk_id  INTEGER PRIMARY KEY,
    ticker    TEXT,
    model     TEXT,
    dim       INTEGER,
    vec       BLOB
);

-- Everything that is not an SEC filing: papers, articles, transcripts, feeds.
-- `tier` is what lets the mismatch engine weigh a 10-K against a Substack.
CREATE TABLE IF NOT EXISTS sources (
    id           INTEGER PRIMARY KEY,
    url          TEXT UNIQUE,
    kind         TEXT,          -- arxiv | openalex | web | news | youtube | rss | ir
    tier         TEXT,          -- primary | academic | commentary
    angle        TEXT,
    title        TEXT,
    published    TEXT,
    text         TEXT,
    n_chars      INTEGER,
    meta         TEXT,
    retrieved_at TEXT
);
CREATE INDEX IF NOT EXISTS ix_sources_kind ON sources(kind, angle);

-- Version history for web sources. A forecast page that changes monthly must be
-- a dated series, not a single frozen fetch.
CREATE TABLE IF NOT EXISTS source_versions (
    id            INTEGER PRIMARY KEY,
    url           TEXT,
    version       INTEGER,
    content_hash  TEXT,
    title         TEXT,
    text          TEXT,
    n_chars       INTEGER,
    retrieved_at  TEXT,
    UNIQUE(url, version)
);

-- Quarterly backlog / deposits / cash-timing series, one row per stated figure.
CREATE TABLE IF NOT EXISTS backlog_quarterly (
    id INTEGER PRIMARY KEY, ticker TEXT, chunk_id INTEGER, accession TEXT, form TEXT,
    filing_date TEXT, as_of TEXT, metric TEXT, value TEXT, unit TEXT, period TEXT,
    status TEXT, quote TEXT
);
CREATE INDEX IF NOT EXISTS ix_backlog ON backlog_quarterly(ticker, metric, filing_date);

-- Management language from transcripts, so wording can be diffed quarter to quarter.
CREATE TABLE IF NOT EXISTS transcript_statements (
    id INTEGER PRIMARY KEY, ticker TEXT, chunk_id INTEGER, accession TEXT, event_date TEXT,
    topic TEXT, speaker_role TEXT, statement TEXT, is_analyst_followup INTEGER,
    qualification TEXT, quote TEXT
);
CREATE INDEX IF NOT EXISTS ix_transcript ON transcript_statements(ticker, topic, event_date);

-- Customer-side project evidence: the seven fields from the audit, plus provenance.
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY, chunk_id INTEGER, accession TEXT, source_kind TEXT, source_date TEXT,
    owner TEXT, project_name TEXT, location TEXT, oem TEXT, model TEXT, turbine_count TEXT,
    capacity_mw TEXT, commitment_status TEXT, financing_permits TEXT,
    equipment_delivery_date TEXT, commercial_operation_date TEXT, date_revision TEXT,
    cancellation_or_dispute TEXT, quote TEXT
);
CREATE INDEX IF NOT EXISTS ix_projects ON projects(owner, project_name);

-- Dated market expectations. Three separate tables on purpose: a few public
-- analyst calls are not consensus, and price targets are not operating forecasts.
CREATE TABLE IF NOT EXISTS analyst_calls (
    id INTEGER PRIMARY KEY, ticker TEXT, chunk_id INTEGER, accession TEXT, published TEXT,
    analyst TEXT, firm TEXT, metric TEXT, value TEXT, period TEXT, stated_on TEXT, quote TEXT
);
CREATE TABLE IF NOT EXISTS mgmt_guidance (
    id INTEGER PRIMARY KEY, ticker TEXT, stated_on TEXT, metric TEXT, value TEXT, period TEXT,
    direction TEXT, prior_value TEXT, guidance_id INTEGER, quote TEXT
);
CREATE TABLE IF NOT EXISTS comps_inputs (
    id INTEGER PRIMARY KEY, ticker TEXT, as_of TEXT, metric TEXT, value REAL, unit TEXT, source TEXT,
    UNIQUE(ticker, as_of, metric, source)
);

-- Competitor segment figures from their own reports (non-EDGAR issuers).
CREATE TABLE IF NOT EXISTS competitor_financials (
    id INTEGER PRIMARY KEY, chunk_id INTEGER, accession TEXT, source_date TEXT, company TEXT,
    segment TEXT, metric TEXT, value TEXT, unit TEXT, period TEXT, quote TEXT
);
CREATE INDEX IF NOT EXISTS ix_compfin ON competitor_financials(company, segment, metric);

-- EIA-860M generator inventory, every monthly vintage kept so planned dates can
-- be watched slipping. EIA does not publish the turbine OEM; that comes from
-- project documents, never from this table.
CREATE TABLE IF NOT EXISTS generators (
    id INTEGER PRIMARY KEY, vintage TEXT, sheet TEXT, entity_name TEXT, plant_id INTEGER,
    plant_name TEXT, state TEXT, generator_id TEXT, technology TEXT, prime_mover TEXT,
    energy_source TEXT, mw REAL, status TEXT, planned_year INTEGER, planned_month INTEGER,
    op_year INTEGER, op_month INTEGER, sector TEXT,
    UNIQUE(vintage, sheet, plant_id, generator_id)
);
CREATE INDEX IF NOT EXISTS ix_gen ON generators(plant_id, generator_id, vintage);

-- EIA-923 plant-level generation and fuel, annual files.
CREATE TABLE IF NOT EXISTS generation (
    id INTEGER PRIMARY KEY, year INTEGER, plant_id INTEGER, plant_name TEXT, state TEXT,
    prime_mover TEXT, fuel_type TEXT, net_generation_mwh REAL, fuel_consumed_mmbtu REAL,
    UNIQUE(year, plant_id, prime_mover, fuel_type)
);

-- LBNL / operator interconnection queues, each dataset vintage kept.
CREATE TABLE IF NOT EXISTS queue_projects (
    id INTEGER PRIMARY KEY, dataset_vintage TEXT, queue_id TEXT, region TEXT, state TEXT,
    project_type TEXT, mw REAL, status TEXT, request_date TEXT, proposed_cod TEXT,
    withdrawn_date TEXT, raw TEXT,
    UNIQUE(dataset_vintage, region, queue_id)
);

-- Grid-operator forecast figures, with the vintage of the forecast that stated them.
CREATE TABLE IF NOT EXISTS operator_forecasts (
    id INTEGER PRIMARY KEY, operator TEXT, report TEXT, vintage TEXT, region TEXT,
    target_year INTEGER, metric TEXT, value REAL, unit TEXT, source_url TEXT, quote TEXT
);

-- The deliverable: each candidate advantage with both sides of the evidence and a
-- falsification condition. Nothing without a falsification condition is an insight.
CREATE TABLE IF NOT EXISTS insights (
    id INTEGER PRIMARY KEY, claim TEXT, topic TEXT, stance TEXT,
    supporting TEXT, opposing TEXT, definitions TEXT, financial_relevance TEXT,
    market_expectation TEXT, falsification TEXT, catalyst_date TEXT,
    confidence TEXT, n_support INTEGER, n_oppose INTEGER, created_at TEXT
);

CREATE TABLE IF NOT EXISTS catalyst_calendar (
    id INTEGER PRIMARY KEY, date TEXT, event TEXT, ticker TEXT, source TEXT, confirmed INTEGER,
    UNIQUE(date, event, ticker)
);

CREATE TABLE IF NOT EXISTS events (
    id          INTEGER PRIMARY KEY,
    ticker      TEXT,
    event_date  TEXT,
    event_type  TEXT,
    accession   TEXT,
    detail      TEXT,
    UNIQUE(ticker, event_date, event_type, accession)
);
"""

# Columns added after the first version of the schema shipped. Each is applied
# only if missing, so an existing database upgrades in place without a rebuild.
# Indexes that reference columns MIGRATIONS adds, so they must be created AFTER
# the migration pass - not inside SCHEMA, or a fresh database fails on first run.
#
# Both exist because SQLite treats NULL as DISTINCT in a UNIQUE constraint. XBRL
# balance-sheet facts carry start_date=NULL and Form 4 rows carry NULL price or
# shares, so the table-level UNIQUE let every re-run duplicate them. COALESCE
# makes the key total and the ingest idempotent.
POST_MIGRATION = [
    # Chunk identity must survive a rebuild. With this index, build_index upserts on
    # (accession, ord) instead of DELETE+INSERT, so ids never move and downstream
    # tables (extractions, guidance, embeddings) are never orphaned again.
    "CREATE UNIQUE INDEX IF NOT EXISTS ux_chunks_acc_ord ON chunks(accession, ord)",
    "CREATE INDEX IF NOT EXISTS ix_chunks_key ON chunks(chunk_key)",
    """CREATE UNIQUE INDEX IF NOT EXISTS ux_facts ON xbrl_facts(
        COALESCE(ticker,''), tag, COALESCE(unit,''), COALESCE(start_date,''),
        COALESCE(end_date,''), COALESCE(accession,''), COALESCE(frame,''))""",
    """CREATE UNIQUE INDEX IF NOT EXISTS ux_insider ON insider_tx(
        COALESCE(ticker,''), COALESCE(accession,''), COALESCE(tx_date,''),
        COALESCE(security,''), COALESCE(code,''), COALESCE(shares,-1),
        COALESCE(price,-1))""",
]

MIGRATIONS = [
    ("chunks", "tier", "TEXT"),
    ("chunks", "kind", "TEXT"),
    ("chunks", "chunk_key", "TEXT"),
    ("guidance", "is_forward", "INTEGER"),
    ("sources", "content_hash", "TEXT"),
    ("sources", "first_seen", "TEXT"),
    ("sources", "last_checked", "TEXT"),
    ("sources", "version", "INTEGER"),
    ("operator_forecasts", "chunk_id", "INTEGER"),
    ("operator_forecasts", "accession", "TEXT"),
    # thesis.py wrote the model's verdict into `stance` and then SELECTed `verdict`;
    # the first card phase died on "no such column: verdict". Separate columns.
    ("insights", "verdict", "TEXT"),
    ("prices", "adjclose", "REAL"),
    ("prices", "ticker", "TEXT"),
    ("filings", "ticker", "TEXT"),
    ("documents", "ticker", "TEXT"),
    ("chunks", "ticker", "TEXT"),
    ("xbrl_facts", "ticker", "TEXT"),
    ("insider_tx", "ticker", "TEXT"),
    ("news", "ticker", "TEXT"),
]


def connect() -> sqlite3.Connection:
    DATA.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH, timeout=60)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=NORMAL")
    con.executescript(SCHEMA)
    for table, col, decl in MIGRATIONS:
        cols = {r[1] for r in con.execute(f"PRAGMA table_info({table})")}
        if cols and col not in cols:
            con.execute(f"ALTER TABLE {table} ADD COLUMN {col} {decl}")
            # everything ingested before the universe existed was GE Vernova
            if col == "ticker":
                con.execute(f"UPDATE {table} SET ticker='{TICKER}' WHERE ticker IS NULL")
    # prices was keyed on date alone when it held a single ticker
    pk = [r[1] for r in con.execute("PRAGMA table_info(prices)") if r[5]]
    if pk == ["date"]:
        con.executescript("""
            CREATE TABLE IF NOT EXISTS prices_v2 (
                ticker TEXT, date TEXT, open REAL, high REAL, low REAL,
                close REAL, volume REAL, adjclose REAL, PRIMARY KEY (ticker, date));
            INSERT OR IGNORE INTO prices_v2 (ticker,date,open,high,low,close,volume,adjclose)
                SELECT COALESCE(ticker,'GEV'),date,open,high,low,close,volume,adjclose FROM prices;
            DROP TABLE prices;
            ALTER TABLE prices_v2 RENAME TO prices;""")
    for stmt in POST_MIGRATION:
        try:
            con.execute(stmt)
        except sqlite3.IntegrityError as exc:
            # duplicates already present - report rather than fail the whole run
            log(f"could not create unique index (existing duplicates): {exc}")
    con.commit()
    return con


def mark(con, source: str, key: str, status: str, detail: str = "") -> None:
    con.execute(
        "INSERT OR REPLACE INTO ingest_log(source,key,status,detail,ts) VALUES (?,?,?,?,?)",
        (source, key, status, detail[:500], time.strftime("%Y-%m-%dT%H:%M:%S")),
    )
    con.commit()


def already(con, source: str, key: str) -> bool:
    row = con.execute(
        "SELECT status FROM ingest_log WHERE source=? AND key=?", (source, key)
    ).fetchone()
    return bool(row and row[0] == "ok")


_WS = re.compile(r"[ \t ]+")
_NL = re.compile(r"\n{3,}")


def html_to_text(raw: bytes) -> str:
    """Extract readable text from a filing, stripping inline-XBRL plumbing."""
    from bs4 import BeautifulSoup
    import warnings
    try:
        from bs4 import XMLParsedAsHTMLWarning
        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    except Exception:
        pass

    soup = BeautifulSoup(raw, "lxml")

    # Inline XBRL hides a large machine-readable header in the document; drop it,
    # otherwise every filing starts with hundreds of fasb.org URIs.
    # find_all() returns a fixed list. When a hidden ancestor is decomposed, bs4
    # clears the __dict__ of every descendant - so a descendant that is later in
    # the same list raises AttributeError on .get(). Toppan Merrill and Donnelley
    # filings nest hidden blocks, which is why ~10% of customer exhibits failed.
    for tag in soup.find_all(["script", "style"]):
        try:
            tag.decompose()
        except AttributeError:
            continue
    for name in ("ix:header", "ix:hidden"):
        for tag in soup.find_all(name):
            try:
                tag.decompose()
            except AttributeError:
                continue
    for tag in soup.find_all(style=True):
        try:
            style = (tag.get("style") or "").replace(" ", "").lower()
        except AttributeError:
            continue                    # already gone with a decomposed ancestor
        if "display:none" in style or "visibility:hidden" in style:
            try:
                tag.decompose()
            except AttributeError:
                continue

    text = soup.get_text("\n", strip=True)
    text = _WS.sub(" ", text)
    text = _NL.sub("\n\n", text)
    return tidy_spacing(text)


# Inline XBRL wraps every reported number in its own tag, so naive text extraction
# yields "$ 176,284 million" and "June 30, 2026 ,". Left alone this breaks exact
# search ("$176,284" matches nothing) and makes quotes look paraphrased.
_SP_AFTER_SYM = re.compile(r"([$£€(])\s+")
_SP_BEFORE_PUNCT = re.compile(r"\s+([,.;:%)\]])")
_SP_IN_NUM = re.compile(r"(\d)\s+([,.])\s*(\d)")


def tidy_spacing(text: str) -> str:
    text = _SP_IN_NUM.sub(r"\1\2\3", text)
    text = _SP_AFTER_SYM.sub(r"\1", text)
    text = _SP_BEFORE_PUNCT.sub(r"\1", text)
    return text.strip()


def filing_url(accession: str, doc: str, cik: str | int = CIK_INT) -> str:
    acc = accession.replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{doc}"
