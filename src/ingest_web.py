"""Pull every angle from the open web into `sources`: arXiv, OpenAlex (IEEE index),
DuckDuckGo web + news, YouTube transcripts, RSS. No API keys, no paid services,
no hosted model - discovery is local search, so it costs nothing to run all night.

    python ingest_web.py                      # every angle, every source
    python ingest_web.py --angle offshore_wind --kinds web youtube
    python ingest_web.py --deadline-min 90    # stop cleanly after 90 minutes

Sources carry a `tier` (primary / academic / commentary) because the mismatch
engine has to know whether a claim comes from a 10-K or a Substack.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

from common import ROOT, connect, log

ANGLES_PATH = ROOT / "config" / "angles.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GEV-research-corpus"}
S = requests.Session()
S.headers.update(UA)

TIER = {"arxiv": "academic", "openalex": "academic", "web": "commentary",
        "news": "commentary", "youtube": "commentary", "rss": "commentary"}


def load_angles() -> dict:
    return json.loads(ANGLES_PATH.read_text(encoding="utf-8"))


# Pages on these domains change over time (forecasts, project pages, IR events),
# so they are re-checked daily; everything else weekly.
LIVING_DOMAINS = ("pjm.com", "ercot.com", "nerc.com", "eia.gov", "gevernova.com",
                  "siemens-energy.com", "mhi.com", "vestas.com", "hitachi", "ferc.gov",
                  "emp.lbl.gov")
TTL_DAYS_DEFAULT = 7
TTL_DAYS_LIVING = 1


def needs_refresh(con, url: str) -> bool:
    """True if we have never fetched this URL, or it is older than its TTL.
    Replaces the old 'skip if seen' rule, which froze every forecast page at its
    first fetch."""
    row = con.execute("SELECT last_checked, retrieved_at FROM sources WHERE url=?",
                      (url,)).fetchone()
    if row is None:
        return True
    last = row[0] or row[1] or ""
    if not last:
        return True
    ttl = TTL_DAYS_LIVING if any(d in url for d in LIVING_DOMAINS) else TTL_DAYS_DEFAULT
    try:
        age_days = (time.time() - time.mktime(time.strptime(last[:19], "%Y-%m-%dT%H:%M:%S"))) / 86400
    except Exception:
        return True
    return age_days >= ttl


def store(con, *, url, kind, angle, title, published, text, meta=None,
          tier: str | None = None) -> bool:
    """Insert a new source, or - if the URL is known and its content changed -
    bump the version and keep the old text in source_versions. Returns True when
    new text was stored."""
    if not url or not text or len(text) < 300:
        return False
    h = hashlib.sha1(text.encode("utf-8", "ignore")).hexdigest()
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    tier = tier or TIER.get(kind, "commentary")
    row = con.execute("SELECT id, content_hash, version FROM sources WHERE url=?",
                      (url,)).fetchone()
    if row is None:
        con.execute(
            """INSERT INTO sources
               (url, kind, tier, angle, title, published, text, n_chars, meta, retrieved_at,
                content_hash, first_seen, last_checked, version)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,1)""",
            (url, kind, tier, angle, (title or "")[:400], (published or "")[:32], text,
             len(text), json.dumps(meta or {})[:2000], now, h, now, now))
        con.execute(
            """INSERT OR IGNORE INTO source_versions
               (url, version, content_hash, title, text, n_chars, retrieved_at)
               VALUES (?,1,?,?,?,?,?)""",
            (url, h, (title or "")[:400], text, len(text), now))
        return True
    sid, old_hash, ver = row
    if old_hash == h:
        con.execute("UPDATE sources SET last_checked=? WHERE id=?", (now, sid))
        return False
    ver = (ver or 1) + 1
    con.execute(
        """UPDATE sources SET text=?, n_chars=?, title=?, content_hash=?, last_checked=?,
                              retrieved_at=?, version=? WHERE id=?""",
        (text, len(text), (title or "")[:400], h, now, now, ver, sid))
    con.execute(
        """INSERT OR IGNORE INTO source_versions
           (url, version, content_hash, title, text, n_chars, retrieved_at)
           VALUES (?,?,?,?,?,?,?)""",
        (url, ver, h, (title or "")[:400], text, len(text), now))
    log(f"    updated (v{ver}): {url[:80]}")
    return True


def clean(html: str) -> str:
    try:
        import trafilatura
        return trafilatura.extract(html, include_comments=False, include_tables=True) or ""
    except Exception:
        return ""


PDF_MAX_PAGES = 200


def pdf_text(data: bytes, max_pages: int = PDF_MAX_PAGES) -> str:
    """Text from a PDF. pypdf first; pdfplumber as a fallback when pypdf yields
    almost nothing (scanned layouts, odd encodings). The page cap is logged when
    hit instead of silently truncating a 300-page report."""
    text = ""
    if data[:4] != b"%PDF":
        return ""                       # HTML behind a .pdf link; pypdf would only complain
    try:
        import pypdf
        r = pypdf.PdfReader(io.BytesIO(data))
        n = len(r.pages)
        if n > max_pages:
            log(f"    pdf has {n} pages; reading first {max_pages}")
        text = "\n".join((p.extract_text() or "") for p in r.pages[:max_pages])
        if len(text) >= 200 * min(n, max_pages):
            return text
    except Exception:
        pass
    try:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            alt = "\n".join((p.extract_text() or "") for p in pdf.pages[:max_pages])
        if len(alt) > len(text):
            return alt
    except Exception:
        pass
    return text


# --------------------------------------------------------------- arXiv

def arxiv(con, angle, query, limit) -> int:
    # AND of terms, not an exact phrase: '"gas turbine lead times 2026"' as a literal
    # phrase matched no abstract at all and returned zero for every query.
    terms = [t for t in re.split(r"\s+", query.strip()) if len(t) > 2]
    q = "+AND+".join("all:" + requests.utils.quote(t) for t in terms) or "all:" + requests.utils.quote(query)
    url = ("http://export.arxiv.org/api/query?search_query=" + q
           + f"&max_results={limit}&sortBy=relevance")
    r = S.get(url, timeout=60)
    if not r.ok:
        return 0
    ns = {"a": "http://www.w3.org/2005/Atom"}
    n = 0
    for e in ET.fromstring(r.content).findall("a:entry", ns):
        link = (e.findtext("a:id", "", ns) or "").strip()
        title = " ".join((e.findtext("a:title", "", ns) or "").split())
        summary = " ".join((e.findtext("a:summary", "", ns) or "").split())
        pub = (e.findtext("a:published", "", ns) or "")[:10]
        text = f"{title}\n\n{summary}"
        # Full text: arXiv PDFs are free. Cap pages so one 300-page thesis can't eat the budget.
        pdf_url = link.replace("/abs/", "/pdf/")
        try:
            pr = S.get(pdf_url, timeout=90)
            if pr.ok and pr.headers.get("content-type", "").startswith("application/pdf"):
                body = pdf_text(pr.content)
                if len(body) > len(text):
                    text = f"{title}\n\n{summary}\n\n{body}"
        except Exception:
            pass
        if store(con, url=link, kind="arxiv", angle=angle, title=title, published=pub,
                 text=text, meta={"query": query}):
            n += 1
        time.sleep(0.5)          # arXiv asks for ~1 req / 3s on the API; PDFs are fine
    time.sleep(3)
    return n


# --------------------------------------------------------------- OpenAlex

def _oa_abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


def openalex(con, angle, query, limit) -> int:
    url = ("https://api.openalex.org/works?search=" + requests.utils.quote(query)
           + f"&per-page={limit}&sort=relevance_score:desc&mailto=research@example.com"
           + "&filter=from_publication_date:2019-01-01")
    r = S.get(url, timeout=60)
    if not r.ok:
        return 0
    n = 0
    for w in r.json().get("results", []):
        title = w.get("title") or ""
        abstract = _oa_abstract(w.get("abstract_inverted_index"))
        src = ((w.get("primary_location") or {}).get("source") or {})
        venue = src.get("display_name") or ""
        publisher = (src.get("host_organization_name") or "")
        text = f"{title}\n\nVenue: {venue}\n\n{abstract}"
        oa_url = (w.get("open_access") or {}).get("oa_url")
        if oa_url and oa_url.lower().endswith(".pdf"):
            try:
                pr = S.get(oa_url, timeout=90)
                if pr.ok and "pdf" in pr.headers.get("content-type", ""):
                    body = pdf_text(pr.content)
                    if len(body) > 500:
                        text += "\n\n" + body
            except Exception:
                pass
        if store(con, url=w.get("id") or w.get("doi") or "", kind="openalex", angle=angle,
                 title=title, published=(w.get("publication_date") or "")[:10], text=text,
                 meta={"query": query, "venue": venue, "publisher": publisher,
                       "ieee": "ieee" in (publisher + venue).lower(),
                       "cited_by": w.get("cited_by_count")}):
            n += 1
    time.sleep(1)
    return n


# --------------------------------------------------------------- DuckDuckGo

def fetch_page(url: str) -> tuple[str, str]:
    try:
        r = S.get(url, timeout=45, allow_redirects=True)
        if not r.ok:
            return "", ""
        ctype = r.headers.get("content-type", "")
        if "pdf" in ctype:
            return pdf_text(r.content), ""
        html = r.text
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
        return clean(html), (m.group(1).strip() if m else "")
    except Exception:
        return "", ""


def ddg(con, angle, query, limit, kind) -> int:
    from ddgs import DDGS
    n = 0
    try:
        with DDGS() as d:
            hits = list(d.news(query, max_results=limit)) if kind == "news" \
                else list(d.text(query, max_results=limit))
    except Exception as exc:
        # DDG rate-limits hard. One long back-off and one retry; a second failure
        # skips this query rather than stalling the whole angle.
        log(f"    ddg {kind} error: {type(exc).__name__} - backing off 75s, one retry")
        time.sleep(75)
        try:
            with DDGS() as d:
                hits = list(d.news(query, max_results=limit)) if kind == "news" \
                    else list(d.text(query, max_results=limit))
        except Exception:
            return 0
    for h in hits:
        url = h.get("href") or h.get("url") or ""
        if not url or not needs_refresh(con, url):
            continue
        text, title = fetch_page(url)
        if store(con, url=url, kind=kind, angle=angle, title=h.get("title") or title,
                 published=(h.get("date") or "")[:10], text=text,
                 meta={"query": query, "source": h.get("source", "")}):
            n += 1
        time.sleep(1.5)
    time.sleep(4)                 # DDG rate-limits aggressively; be polite
    return n


# --------------------------------------------------------------- YouTube

def youtube(con, angle, query, limit) -> int:
    import yt_dlp
    from youtube_transcript_api import YouTubeTranscriptApi
    opts = {"quiet": True, "no_warnings": True, "extract_flat": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(opts) as y:
            res = y.extract_info(f"ytsearch{limit}:{query}", download=False)
    except Exception as exc:
        log(f"    youtube search error: {type(exc).__name__}")
        return 0
    api = YouTubeTranscriptApi()
    n = 0
    for e in res.get("entries", []) or []:
        vid = e.get("id")
        url = f"https://www.youtube.com/watch?v={vid}"
        if not vid or not needs_refresh(con, url):
            continue
        try:
            tr = api.fetch(vid)
            text = " ".join(s.text for s in tr)
        except Exception:
            continue              # no captions - nothing to index
        if store(con, url=url, kind="youtube", angle=angle, title=e.get("title"),
                 published="", text=text,
                 meta={"query": query, "channel": e.get("uploader") or e.get("channel"),
                       "duration": e.get("duration")}):
            n += 1
        time.sleep(1)
    return n


# --------------------------------------------------------------- RSS

def rss(con, feeds: list[str]) -> int:
    import feedparser
    n = 0
    for feed in feeds:
        try:
            f = feedparser.parse(feed)
        except Exception:
            continue
        for e in f.entries[:40]:
            url = e.get("link") or ""
            if not url or not needs_refresh(con, url):
                continue
            # RSS bodies are often truncated; fetch the page for full text
            text, _t = fetch_page(url)
            if len(text) < 300:
                text = clean(e.get("summary", "") or "") or (e.get("summary", "") or "")
            if store(con, url=url, kind="rss", angle="feed", title=e.get("title"),
                     published=(e.get("published", "") or "")[:16], text=text,
                     meta={"feed": feed}):
                n += 1
            time.sleep(1)
    return n


# --------------------------------------------------------------- driver

def run(con, angles: dict, only: list[str] | None, kinds: list[str],
        deadline: float | None = None) -> dict:
    lim = angles["per_query_limits"]
    totals = {k: 0 for k in ("arxiv", "openalex", "web", "news", "youtube", "rss")}

    if "rss" in kinds and (not deadline or time.time() < deadline):
        log("  RSS feeds")
        totals["rss"] += rss(con, angles.get("rss_feeds", []))
        con.commit()

    for ang in angles["angles"]:
        if only and ang["id"] not in only:
            continue
        if deadline and time.time() > deadline:
            log("  deadline reached - stopping web ingest cleanly")
            break
        log(f"  ANGLE {ang['id']}: {ang['label']}")
        for q in ang["queries"]:
            if deadline and time.time() > deadline:
                break
            got = {}
            try:
                if "arxiv" in kinds:
                    got["arxiv"] = arxiv(con, ang["id"], q, lim["arxiv"])
                if "openalex" in kinds:
                    got["openalex"] = openalex(con, ang["id"], q, lim["openalex"])
                if "web" in kinds:
                    got["web"] = ddg(con, ang["id"], q, lim["web"], "web")
                if "news" in kinds:
                    got["news"] = ddg(con, ang["id"], q, lim["news"], "news")
                if "youtube" in kinds:
                    got["youtube"] = youtube(con, ang["id"], q, lim["youtube"])
            except Exception as exc:
                log(f"    query failed ({type(exc).__name__}): {q[:50]}")
            con.commit()
            for k, v in got.items():
                totals[k] += v
            log(f"    {q[:58]:<60} " + "  ".join(f"{k}={v}" for k, v in got.items()))
    return totals


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--angle", nargs="*")
    p.add_argument("--kinds", nargs="*", default=["rss", "arxiv", "openalex", "web", "news", "youtube"])
    p.add_argument("--deadline-min", type=float)
    a = p.parse_args()
    con = connect()
    deadline = time.time() + a.deadline_min * 60 if a.deadline_min else None
    t = run(con, load_angles(), a.angle, a.kinds, deadline)
    log("web ingest totals: " + "  ".join(f"{k}={v}" for k, v in t.items()))
    n = con.execute("SELECT COUNT(*), SUM(n_chars) FROM sources").fetchone()
    log(f"sources table: {n[0]:,} documents, {(n[1] or 0):,} chars")
    con.close()


if __name__ == "__main__":
    main()
