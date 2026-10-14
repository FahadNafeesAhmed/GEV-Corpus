"""Primary documents outside EDGAR, all tier='primary', all versioned:

  ir           GE Vernova investor site: earnings transcripts, decks, investor-day
               material, conference appearances
  competitors  Siemens Energy, Mitsubishi Heavy Industries / Mitsubishi Power,
               Vestas, Hitachi Energy (segment-level inside Hitachi reports)
  operators    PJM, ERCOT, NERC load forecasts and capacity reports - every year
               kept, since the point is comparing forecast vintages to outcomes
  customers    named GEV customers that file with the SEC: their 8-K/10-K/10-Q,
               fed through the existing EDGAR path so exhibits are included

    python ingest_primary.py --check
    python ingest_primary.py --only ir operators
"""
from __future__ import annotations

import argparse
import json
import re
import time

import requests

from common import ROOT, Fetcher, connect, load_config, log, mark, already
from ingest_web import clean, needs_refresh, pdf_text, store

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GEV-research-corpus"}
S = requests.Session()
S.headers.update(UA)

CUSTOMERS_PATH = ROOT / "config" / "customers.json"

# Landing pages to crawl one level deep for documents. Sites change their URL
# structure; discovery via a site-restricted search is the fallback for each.
SITES = {
    "ir": {
        "company": "GE Vernova", "kind_default": "ir",
        "pages": ["https://www.gevernova.com/investors",
                  "https://www.gevernova.com/investors/events-and-presentations",
                  "https://www.gevernova.com/investors/financial-information",
                  "https://www.gevernova.com/news"],
        "searches": ["site:gevernova.com earnings call transcript",
                     "site:gevernova.com investor presentation pdf",
                     "site:gevernova.com investor day",
                     "GE Vernova earnings call transcript Q1 Q2 Q3 Q4 2025 2026"],
        "doc_re": re.compile(r"transcript|presentation|earnings|investor|results|webcast|prepared remarks", re.I),
    },
    "siemens_energy": {
        "company": "Siemens Energy", "kind_default": "competitor",
        "pages": ["https://www.siemens-energy.com/global/en/home/investor-relations.html",
                  "https://www.siemens-energy.com/global/en/home/investor-relations/financial-results.html"],
        "searches": ["site:siemens-energy.com quarterly statement pdf Gas Services Grid Technologies",
                     "site:siemens-energy.com earnings release presentation",
                     "Siemens Energy capital market day presentation Gas Services orders"],
        "doc_re": re.compile(r"quarter|Q[1-4]|half|annual|results|presentation|statement|report", re.I),
    },
    "mhi": {
        "company": "Mitsubishi Heavy Industries", "kind_default": "competitor",
        "pages": ["https://www.mhi.com/finance/library/result/",
                  "https://www.mhi.com/finance/library/presentation/"],
        "searches": ["site:mhi.com financial results presentation energy systems GTCC orders",
                     "Mitsubishi Power gas turbine orders results presentation pdf"],
        "doc_re": re.compile(r"result|presentation|financial|report|earnings", re.I),
    },
    "vestas": {
        "company": "Vestas", "kind_default": "competitor",
        "pages": ["https://www.vestas.com/en/investor/financial-reports",
                  "https://www.vestas.com/en/investor"],
        "searches": ["site:vestas.com interim financial report pdf", "Vestas quarterly presentation pdf order intake"],
        "doc_re": re.compile(r"interim|annual|report|presentation|Q[1-4]", re.I),
    },
    "hitachi": {
        "company": "Hitachi Energy", "kind_default": "competitor",
        "pages": ["https://www.hitachi.com/IR-e/library/", "https://www.hitachienergy.com/news"],
        "searches": ["site:hitachi.com IR presentation Hitachi Energy segment orders transformers",
                     "Hitachi Energy investment capacity expansion transformers announcement"],
        "doc_re": re.compile(r"presentation|result|financial|report|Energy", re.I),
    },
    "pjm": {
        "company": "PJM", "kind_default": "operator",
        "pages": ["https://www.pjm.com/planning/resource-adequacy-planning/load-forecast-dev-process",
                  "https://www.pjm.com/library/reports-notices/load-forecast"],
        "direct": [f"https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/{y}-load-report.pdf"
                   for y in range(2019, 2027)]
                  + [f"https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/{y}-load-report.ashx"
                     for y in range(2019, 2027)],
        "searches": ["site:pjm.com load forecast report pdf",
                     "site:pjm.com data center load forecast accuracy report",
                     "site:pjm.com long-term load forecast large load adjustments"],
        "doc_re": re.compile(r"load|forecast|data.?center|large load|capacity|reliability", re.I),
    },
    "ercot": {
        "company": "ERCOT", "kind_default": "operator",
        "pages": ["https://www.ercot.com/gridinfo/load/forecast", "https://www.ercot.com/gridinfo/resource"],
        "searches": ["site:ercot.com long-term load forecast report pdf",
                     "site:ercot.com capacity demand and reserves report CDR",
                     "ERCOT large load interconnection queue data center GW"],
        "doc_re": re.compile(r"load|forecast|CDR|capacity|demand|reserve|large load", re.I),
    },
    "nerc": {
        "company": "NERC", "kind_default": "operator",
        "pages": ["https://www.nerc.com/pa/RAPA/ra/Pages/default.aspx"],
        "searches": ["site:nerc.com Long-Term Reliability Assessment pdf",
                     "NERC LTRA data center load growth summer reliability assessment pdf"],
        "doc_re": re.compile(r"reliability|assessment|LTRA|load|summer|winter", re.I),
    },
}

GROUPS = {"ir": ["ir"], "competitors": ["siemens_energy", "mhi", "vestas", "hitachi"],
          "operators": ["pjm", "ercot", "nerc"]}


SPREADSHEET_EXT = (".xlsx", ".xls", ".xlsb", ".csv")


def sheet_text(data: bytes, name: str, max_rows: int = 400) -> str:
    """Render a spreadsheet as searchable text, sheet by sheet. Operator forecast
    files (ERCOT's monthly peak forecast, PJM's XLSX tables) were being skipped
    entirely because the crawler only understood PDF and HTML."""
    import io
    try:
        import pandas as pd
        if name.lower().endswith(".csv"):
            frames = {"csv": pd.read_csv(io.BytesIO(data))}
        else:
            engine = "pyxlsb" if name.lower().endswith(".xlsb") else None
            frames = pd.read_excel(io.BytesIO(data), sheet_name=None, engine=engine)
    except Exception as exc:
        log(f"    spreadsheet parse failed for {name[:60]}: {type(exc).__name__}")
        return ""
    parts = []
    for sheet, df in frames.items():
        df = df.dropna(how="all").dropna(axis=1, how="all")
        if df.empty:
            continue
        parts.append(f"SHEET {sheet} ({len(df)} rows x {len(df.columns)} cols)")
        parts.append(" | ".join(str(c) for c in df.columns))
        for _, row in df.head(max_rows).iterrows():
            parts.append(" | ".join("" if (isinstance(v, float) and v != v) else str(v) for v in row.tolist()))
        if len(df) > max_rows:
            parts.append(f"... {len(df) - max_rows} more rows")
    return "\n".join(parts)


def fetch_doc(url: str) -> tuple[str, str]:
    try:
        r = S.get(url, timeout=90, allow_redirects=True)
        if not r.ok:
            return "", ""
        ctype = r.headers.get("content-type", "").lower()
        name = url.rsplit("/", 1)[-1].split("?")[0]
        low = url.lower()
        if low.endswith(SPREADSHEET_EXT) or "spreadsheet" in ctype or "excel" in ctype or "csv" in ctype:
            return sheet_text(r.content, name), name
        if r.content[:4] == b"%PDF":
            return pdf_text(r.content), name
        if "pdf" in ctype or low.endswith(".pdf"):
            # labelled as PDF but is not one (login wall, 404 page) - do not feed it to pypdf
            return "", ""
        html = r.text
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
        return clean(html), (m.group(1).strip() if m else "")
    except Exception:
        return "", ""


def links_on(url: str) -> list[str]:
    try:
        html = S.get(url, timeout=60).text
    except Exception:
        return []
    out = []
    base = re.match(r"https?://[^/]+", url).group(0)
    for href in re.findall(r'href=["\']([^"\']+)["\']', html, re.I):
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("javascript:"):
            continue
        if href.startswith("//"):
            href = "https:" + href
        elif href.startswith("/"):
            href = base + href
        elif not href.startswith("http"):
            href = url.rsplit("/", 1)[0] + "/" + href
        out.append(href.split("#")[0])
    return list(dict.fromkeys(out))


def kind_for(site: dict, url: str, title: str) -> str:
    t = (url + " " + (title or "")).lower()
    if site["kind_default"] == "ir":
        if "transcript" in t or "prepared remarks" in t:
            return "transcript"
        if "presentation" in t or ".pdf" in t or "deck" in t:
            return "deck"
        return "ir"
    return site["kind_default"]


def crawl_site(con, key: str, check: bool, deadline=None) -> int:
    site = SITES[key]
    cands: list[str] = list(site.get("direct", []))
    for pg in site["pages"]:
        cands += [u for u in links_on(pg) if site["doc_re"].search(u)]
    try:
        from ddgs import DDGS
        with DDGS() as d:
            for q in site["searches"]:
                cands += [h.get("href", "") for h in d.text(q, max_results=15)]
                time.sleep(2)
    except Exception as exc:
        log(f"    search discovery failed for {key}: {type(exc).__name__}")
    # keep on-domain or PDF results, drop obvious noise
    dom = re.sub(r"^https?://(www\.)?", "", site["pages"][0]).split("/")[0].split(".")[0]
    cands = [u for u in dict.fromkeys(cands)
             if u and (dom in u or u.lower().endswith((".pdf",) + SPREADSHEET_EXT))
             and not re.search(r"\.(png|jpg|gif|svg|css|js|woff2?)$", u, re.I)]
    log(f"  {key}: {len(cands)} candidate documents")
    if check:
        for u in cands[:12]:
            log(f"    {u[:100]}")
        return 0
    n = 0
    empty = 0
    for u in cands:
        if deadline and time.time() > deadline:
            break
        if not needs_refresh(con, u):
            continue
        text, title = fetch_doc(u)
        if len(text) < 500:
            empty += 1
            if empty <= 3:
                # say WHY a site yields nothing, instead of a silent zero (NERC, ERCOT on run 2)
                try:
                    probe = S.get(u, timeout=45, allow_redirects=True, stream=True)
                    log(f"    empty: HTTP {probe.status_code} {probe.headers.get('content-type','?')[:30]} "
                        f"{len(probe.content) if probe.status_code < 400 else 0}B  {u[:80]}")
                    probe.close()
                except Exception as exc:
                    log(f"    empty: {type(exc).__name__}  {u[:80]}")
            continue
        kind = kind_for(site, u, title)
        if store(con, url=u, kind=kind, angle=key, title=title, published="", text=text,
                 meta={"company": site["company"]}, tier="primary"):
            n += 1
        time.sleep(1)
    con.commit()
    log(f"  {key}: {n} documents stored/updated")
    return n


def run_customers(con, check: bool, deadline=None) -> int:
    """Named GEV customers that file with the SEC, via the existing EDGAR path."""
    import ingest_sec
    cfg = load_config()
    fetch = Fetcher(cfg)
    try:
        doc = json.loads(CUSTOMERS_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        log(f"  customers.json unreadable: {exc}")
        return 0
    r = fetch.get("https://www.sec.gov/files/company_tickers.json")
    lookup = {}
    if r:
        for v in r.json().values():
            lookup[v["ticker"]] = (str(v["cik_str"]).zfill(10), v["title"])
    n = 0
    for c in doc["customers"]:
        if deadline and time.time() > deadline:
            break
        t = c["ticker"]
        if t not in lookup:
            log(f"  {t}: not an SEC filer / not found - skip")
            continue
        cik, name = lookup[t]
        tk = {"ticker": t, "cik": cik, "name": name, "tier": "D", "since": doc.get("since", "2024-01-01")}
        if check:
            log(f"  {t} {cik} {name[:40]} ({c.get('why','')})")
            continue
        log(f"  CUSTOMER {t} - {name[:50]}")
        try:
            ingest_sec.fetch_index(con, fetch, tk)
            ingest_sec.fetch_documents(con, fetch, cfg, tk)
            n += 1
        except Exception as exc:
            log(f"  {t} failed: {type(exc).__name__}")
    return n


def run(con, only: list[str] | None, check: bool, deadline=None) -> dict:
    out = {}
    groups = only or ["ir", "competitors", "operators", "customers"]
    for g in groups:
        log(f"PRIMARY: {g}")
        if g == "customers":
            out[g] = run_customers(con, check, deadline)
            continue
        for key in GROUPS.get(g, [g]):
            out[key] = crawl_site(con, key, check, deadline)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--only", nargs="*")
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    con = connect()
    run(con, a.only, a.check)
    con.close()


if __name__ == "__main__":
    main()
