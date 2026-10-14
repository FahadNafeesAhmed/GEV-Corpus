"""Spreadsheet datasets: EIA-860M monthly generator inventory (every vintage),
EIA-923 generation and fuel, and the LBNL interconnection-queue dataset.

    python ingest_tabular.py --check          probe URLs, download nothing
    python ingest_tabular.py --since 2023-01  vintages to keep
    python ingest_tabular.py --skip-923

These are worth more than another article: 860M lists every proposed generator
with technology, MW and planned operating month, and each monthly vintage is
kept so a planned date that keeps moving shows up as a series. EIA does NOT
publish the turbine OEM - GEV exposure at a plant comes from project documents.
"""
from __future__ import annotations

import argparse
import io
import re
import time
import zipfile

import requests

from common import RAW, already, connect, log, mark

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GEV-research-corpus"}
S = requests.Session()
S.headers.update(UA)

MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august",
          "september", "october", "november", "december"]
EIA860M = "https://www.eia.gov/electricity/data/eia860m/xls/{month}_generator{year}.xlsx"
EIA860M_ARCHIVE = "https://www.eia.gov/electricity/data/eia860m/archive/xls/{month}_generator{year}.xlsx"
EIA923 = "https://www.eia.gov/electricity/data/eia923/xls/f923_{year}.zip"
EIA923_ARCHIVE = "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_{year}.zip"

GAS_TECH = re.compile(r"natural gas|combined cycle|combustion turbine|gas turbine", re.I)


def fetch(url: str, timeout: int = 180):
    """GET following redirects, and insist the body is a real spreadsheet/zip.
    EIA answers old vintage URLs with a 301; the redirect target is sometimes an
    HTML page, which must never be cached and parsed as an xlsx."""
    try:
        r = S.get(url, timeout=timeout, allow_redirects=True)
        if not r.ok or len(r.content) < 10_000:
            return None
        if r.content[:2] != b"PK":          # xlsx and zip both start with the PK zip magic
            log(f"    not a spreadsheet at {r.url[:90]} (content-type {r.headers.get('content-type','?')[:40]})")
            return None
        return r
    except Exception:
        return None


def cached(name: str, url: str):
    path = RAW / "tabular" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_bytes()
    r = fetch(url)
    if r is None:
        return None
    path.write_bytes(r.content)
    return r.content


def _num(v):
    try:
        if v is None or (isinstance(v, float) and v != v):
            return None
        return float(v)
    except Exception:
        return None


def _int(v):
    n = _num(v)
    return int(n) if n is not None else None


def _col(df, *names):
    """First column whose lowercase name contains any of the given fragments."""
    cols = {c.lower().strip(): c for c in df.columns}
    for n in names:
        for lc, orig in cols.items():
            if n in lc:
                return orig
    return None


# --------------------------------------------------------------- EIA-860M

def ingest_860m(con, vintage: str, data: bytes) -> int:
    import pandas as pd
    total = 0
    for sheet in ("Operating", "Planned", "Retired", "Canceled or Postponed"):
        try:
            df = pd.read_excel(io.BytesIO(data), sheet_name=sheet, skiprows=2)
        except Exception:
            continue
        c = {
            "entity": _col(df, "entity name"), "pid": _col(df, "plant id"),
            "pname": _col(df, "plant name"), "state": _col(df, "plant state"),
            "gid": _col(df, "generator id"), "tech": _col(df, "technology"),
            "pm": _col(df, "prime mover"), "es": _col(df, "energy source code"),
            "mw": _col(df, "nameplate capacity"), "status": _col(df, "status"),
            "py": _col(df, "planned operation year"), "pmo": _col(df, "planned operation month"),
            "oy": _col(df, "operating year"), "om": _col(df, "operating month"),
            "sector": _col(df, "sector"),
        }
        if not c["pid"] or not c["gid"]:
            continue
        rows = []
        for _, r in df.iterrows():
            pid = _int(r.get(c["pid"]))
            if pid is None:
                continue
            rows.append((vintage, sheet,
                         str(r.get(c["entity"], "")) if c["entity"] else "",
                         pid, str(r.get(c["pname"], "")) if c["pname"] else "",
                         str(r.get(c["state"], "")) if c["state"] else "",
                         str(r.get(c["gid"], "")),
                         str(r.get(c["tech"], "")) if c["tech"] else "",
                         str(r.get(c["pm"], "")) if c["pm"] else "",
                         str(r.get(c["es"], "")) if c["es"] else "",
                         _num(r.get(c["mw"])) if c["mw"] else None,
                         str(r.get(c["status"], "")) if c["status"] else "",
                         _int(r.get(c["py"])) if c["py"] else None,
                         _int(r.get(c["pmo"])) if c["pmo"] else None,
                         _int(r.get(c["oy"])) if c["oy"] else None,
                         _int(r.get(c["om"])) if c["om"] else None,
                         str(r.get(c["sector"], "")) if c["sector"] else ""))
        con.executemany(
            """INSERT OR IGNORE INTO generators
               (vintage, sheet, entity_name, plant_id, plant_name, state, generator_id,
                technology, prime_mover, energy_source, mw, status, planned_year,
                planned_month, op_year, op_month, sector)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
        total += len(rows)
    con.commit()
    return total


def run_860m(con, since: str, check: bool) -> None:
    y0, m0 = int(since[:4]), int(since[5:7])
    now = time.localtime()
    vintages = []
    y, m = y0, m0
    while (y, m) <= (now.tm_year, now.tm_mon):
        vintages.append((y, m))
        m += 1
        if m > 12:
            y, m = y + 1, 1
    log(f"EIA-860M: {len(vintages)} monthly vintages from {since}")
    if check:
        # EIA is slow to answer HEAD; probe a few vintages, follow redirects, and
        # report where they actually land instead of the 301 itself.
        vintages = vintages[:2] + vintages[-2:]
    for y, m in vintages:
        v = f"{y}-{m:02d}"
        if already(con, "eia860m", v):
            continue
        name = f"{MONTHS[m-1]}_generator{y}.xlsx"
        url = EIA860M.format(month=MONTHS[m-1], year=y)
        if check:
            try:
                r = S.head(url, timeout=30, allow_redirects=True)
                landed = r.url if r.url != url else ""
                log(f"  {v}: HTTP {r.status_code}  {landed[:90]}")
            except Exception as exc:
                log(f"  {v}: {type(exc).__name__}")
            continue
        data = cached(name, url) or cached(name, EIA860M_ARCHIVE.format(month=MONTHS[m-1], year=y))
        if not data:
            mark(con, "eia860m", v, "skip", "not published / unreachable")
            continue
        n = ingest_860m(con, v, data)
        mark(con, "eia860m", v, "ok", f"{n} rows")
        gas = con.execute("""SELECT COUNT(*) FROM generators WHERE vintage=? AND sheet='Planned'
                             AND (technology LIKE '%Gas%' OR technology LIKE '%Combined Cycle%'
                                  OR technology LIKE '%Combustion Turbine%')""", (v,)).fetchone()[0]
        log(f"  {v}: {n:,} generator rows ({gas:,} planned gas units)")
        time.sleep(1)


# --------------------------------------------------------------- EIA-923

def ingest_923(con, year: int, data: bytes) -> int:
    import pandas as pd
    total = 0
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        names = [n for n in z.namelist() if "Schedules_2_3_4_5" in n and n.endswith((".xlsx", ".xls"))]
        if not names:
            return 0
        raw = z.read(names[0])
    try:
        df = pd.read_excel(io.BytesIO(raw), sheet_name=0, skiprows=5)
    except Exception:
        return 0
    c = {"pid": _col(df, "plant id"), "pname": _col(df, "plant name"), "state": _col(df, "plant state"),
         "pm": _col(df, "reported\nprime mover", "prime mover"),
         "fuel": _col(df, "reported\nfuel type code", "fuel type code"),
         "gen": _col(df, "net generation\n(megawatthours)", "net generation"),
         "mmbtu": _col(df, "total fuel consumption\nmmbtu", "total fuel consumption mmbtu")}
    if not c["pid"]:
        return 0
    rows = []
    for _, r in df.iterrows():
        pid = _int(r.get(c["pid"]))
        if pid is None:
            continue
        rows.append((year, pid, str(r.get(c["pname"], "")) if c["pname"] else "",
                     str(r.get(c["state"], "")) if c["state"] else "",
                     str(r.get(c["pm"], "")) if c["pm"] else "",
                     str(r.get(c["fuel"], "")) if c["fuel"] else "",
                     _num(r.get(c["gen"])) if c["gen"] else None,
                     _num(r.get(c["mmbtu"])) if c["mmbtu"] else None))
    con.executemany(
        """INSERT OR IGNORE INTO generation
           (year, plant_id, plant_name, state, prime_mover, fuel_type,
            net_generation_mwh, fuel_consumed_mmbtu) VALUES (?,?,?,?,?,?,?,?)""", rows)
    con.commit()
    return len(rows)


def run_923(con, years: list[int], check: bool) -> None:
    for y in years:
        if already(con, "eia923", str(y)):
            continue
        url = EIA923.format(year=y)
        if check:
            try:
                r = S.head(url, timeout=30, allow_redirects=True)
                log(f"  923 {y}: HTTP {r.status_code}")
            except Exception as exc:
                log(f"  923 {y}: {type(exc).__name__}")
            continue
        data = cached(f"f923_{y}.zip", url) or cached(f"f923_{y}.zip", EIA923_ARCHIVE.format(year=y))
        if not data:
            mark(con, "eia923", str(y), "skip", "unreachable")
            continue
        n = ingest_923(con, y, data)
        mark(con, "eia923", str(y), "ok", f"{n} rows")
        log(f"  EIA-923 {y}: {n:,} plant/fuel rows")


# --------------------------------------------------------------- LBNL queue

LBNL_PAGES = ["https://emp.lbl.gov/queues", "https://emp.lbl.gov/interconnection_costs",
              "https://emp.lbl.gov/publications/queued-2025-edition-characteristics"]


def run_lbnl(con, check: bool) -> None:
    """Crawl LBNL's own pages for the dataset link first; DuckDuckGo is only a
    supplement because it rate-limits and a failed search must not mean no data."""
    cands: list[str] = []
    for pg in LBNL_PAGES:
        try:
            html = S.get(pg, timeout=60).text
            cands += [m if m.startswith("http") else "https://emp.lbl.gov" + m
                      for m in re.findall(r'href="([^"]+\.(?:xlsx|xls|csv))"', html, re.I)]
        except Exception:
            continue
    try:
        from ddgs import DDGS
        with DDGS() as d:
            hits = list(d.text("site:emp.lbl.gov queued up interconnection queue data xlsx", max_results=10))
        cands += [h.get("href", "") for h in hits if h.get("href", "").lower().endswith((".xlsx", ".xls", ".csv"))]
    except Exception as exc:
        log(f"  LBNL search supplement unavailable: {type(exc).__name__}")
    cands = [u for u in dict.fromkeys(cands) if "lbl.gov" in u]
    log(f"  LBNL candidate files: {len(cands)}")
    for u in cands[:5]:
        log(f"    {u[:100]}")
    for url in cands[:2]:
        vintage = url.rsplit("/", 1)[-1][:60]
        if already(con, "lbnl", vintage):
            continue
        if check:
            log(f"  would fetch {url}")
            continue
        data = cached("lbnl_" + vintage, url)
        if not data:
            continue
        import pandas as pd
        try:
            df = pd.read_excel(io.BytesIO(data), sheet_name=0) if not url.endswith(".csv") \
                else pd.read_csv(io.BytesIO(data))
        except Exception as exc:
            log(f"  LBNL parse failed: {type(exc).__name__}")
            continue
        c = {"qid": _col(df, "queue id", "q_id", "queue_id"), "region": _col(df, "region", "entity"),
             "state": _col(df, "state"), "type": _col(df, "type_clean", "resource", "fuel", "type"),
             "mw": _col(df, "mw1", "capacity", "mw"), "status": _col(df, "q_status", "status"),
             "req": _col(df, "q_date", "queue date", "request"), "cod": _col(df, "prop_date", "proposed", "cod"),
             "wd": _col(df, "wd_date", "withdrawn")}
        rows = []
        for _, r in df.iterrows():
            rows.append((vintage, str(r.get(c["qid"], "")) if c["qid"] else "",
                         str(r.get(c["region"], "")) if c["region"] else "",
                         str(r.get(c["state"], "")) if c["state"] else "",
                         str(r.get(c["type"], "")) if c["type"] else "",
                         _num(r.get(c["mw"])) if c["mw"] else None,
                         str(r.get(c["status"], "")) if c["status"] else "",
                         str(r.get(c["req"], ""))[:10] if c["req"] else "",
                         str(r.get(c["cod"], ""))[:10] if c["cod"] else "",
                         str(r.get(c["wd"], ""))[:10] if c["wd"] else "", ""))
        con.executemany(
            """INSERT OR IGNORE INTO queue_projects
               (dataset_vintage, queue_id, region, state, project_type, mw, status,
                request_date, proposed_cod, withdrawn_date, raw) VALUES (?,?,?,?,?,?,?,?,?,?,?)""", rows)
        con.commit()
        mark(con, "lbnl", vintage, "ok", f"{len(rows)} rows")
        log(f"  LBNL {vintage}: {len(rows):,} queue rows")


def summarize(con) -> None:
    v = con.execute("SELECT COUNT(DISTINCT vintage), MIN(vintage), MAX(vintage) FROM generators").fetchone()
    log(f"generators: {v[0]} vintages {v[1]} -> {v[2]}, {con.execute('SELECT COUNT(*) FROM generators').fetchone()[0]:,} rows")
    log(f"generation (923): {con.execute('SELECT COUNT(*) FROM generation').fetchone()[0]:,} rows")
    log(f"queue_projects: {con.execute('SELECT COUNT(*) FROM queue_projects').fetchone()[0]:,} rows")


def run(con, since: str = "2023-01", skip_923: bool = False, check: bool = False, deadline=None):
    run_860m(con, since, check)
    if not skip_923:
        run_923(con, list(range(2022, time.localtime().tm_year + 1)), check)
    run_lbnl(con, check)
    summarize(con)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--since", default="2023-01")
    p.add_argument("--skip-923", action="store_true")
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    con = connect()
    run(con, a.since, a.skip_923, a.check)
    con.close()


if __name__ == "__main__":
    main()
