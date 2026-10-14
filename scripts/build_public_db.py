"""Build the public, redistributable copy of the research corpus.

Rules (see the repository README):
- keep: SEC text and XBRL facts (public domain), EIA/PJM-derived tables, and every table the
  pipeline derived itself (claims, extractions, guidance, insights, analyst calls, ...)
- drop: prices (vendor terms), embeddings (regenerable), Bloomberg rows (licensed),
  LinkedIn-sourced rows (personal data), and the stored text of every third-party web source
  (URL, title and date stay; only the pipeline's own notes keep their text)
- rebuild the full-text index on the kept chunks, replace local file paths, VACUUM.

Usage: python scripts/build_public_db.py [destination.db]
"""
import pathlib
import re
import sqlite3
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "gev.db"

# usage: build_public_db.py [destination.db] [--replace WORD=REPLACEMENT ...]
# --replace swaps a whole word, case-insensitively, in every text column; pass it from the
# shell (for example the machine's user name) so nothing personal is written into this file.
_args = sys.argv[1:]
REPLACES = []
_dst = None
_i = 0
while _i < len(_args):
    if _args[_i] == "--replace" and _i + 1 < len(_args) and "=" in _args[_i + 1]:
        REPLACES.append(tuple(_args[_i + 1].split("=", 1)))
        _i += 2
    else:
        _dst = _args[_i]
        _i += 1
DST = pathlib.Path(_dst) if _dst else ROOT / "data" / "gev_public.db"

KEEP_WHOLE = [
    "filings", "documents", "xbrl_facts", "insider_tx", "guidance", "risk_items", "events",
    "projects", "queue_projects", "generators", "generation", "operator_forecasts",
    "mgmt_guidance", "catalyst_calendar", "backlog_quarterly", "extractions", "claims",
    "insights", "analyst_calls", "competitor_financials", "transcript_statements", "ingest_log",
]
FILTERED = {
    "chunks": "kind IN ('sec','research')",
    "comps_inputs": "COALESCE(source,'') <> 'yahoo'",
}
DROPPED = ["prices", "embeddings", "news", "holders", "chunks_fts"]
OWN_KINDS = "('research','model')"

# Local file paths of any Windows user profile become relative or generic. No names are needed.
PATH_RULES = [
    (re.compile(r"[A-Za-z]:(?:[\\/]|\\\\)+Users(?:[\\/]|\\\\)+[^\\/\s\"'<>|]+(?:[\\/]|\\\\)+Citadel Stock Pitch(?:[\\/]|\\\\)+gev-corpus(?:[\\/]|\\\\)*"), ""),
    (re.compile(r"[A-Za-z]:(?:[\\/]|\\\\)+Users(?:[\\/]|\\\\)+[^\\/\s\"'<>|]+(?:[\\/]|\\\\)+Citadel Stock Pitch(?:[\\/]|\\\\)*"), "<local>/"),
    (re.compile(r"[A-Za-z]:(?:[\\/]|\\\\)+Users(?:[\\/]|\\\\)+[^\\/\s\"'<>|]+"), "<home>"),
    # Git-Bash style /c/Users/<name>
    (re.compile(r"/[a-z]/Users/[^\\/\s\"'<>|]+"), "<home>"),
    # tool session folders under the home directory
    (re.compile(r"<home>(?:[\\/]|\\\\)+AppData(?:[\\/]|\\\\)+Local(?:[\\/]|\\\\)+Temp(?:[\\/]|\\\\)+[^\s\"'<>|)]*"), "<scratch>"),
    (re.compile(r"<home>(?:[\\/]|\\\\)+\.[A-Za-z]+(?:[\\/]|\\\\)+projects(?:[\\/]|\\\\)+[^\s\"'<>|)]*"), "<session-files>"),
    # a session id that encodes a user path
    (re.compile(r"C--Users-user-\\/\s\"'<>|]+"), "C--Users-user"),
]


def scrub_text(s):
    for rx, rep in PATH_RULES:
        s = rx.sub(rep, s)
    for word, rep in REPLACES:
        s = re.sub(r"(?i)\b" + re.escape(word) + r"\b", rep, s)
    return s


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def main():
    if DST.exists():
        DST.unlink()
    DST.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DST)
    con.execute("PRAGMA journal_mode=OFF")
    con.execute("PRAGMA synchronous=OFF")
    con.execute("PRAGMA cache_size=-400000")
    con.execute("ATTACH DATABASE ? AS src", (str(SRC),))
    ddl = {r[0]: r[1] for r in con.execute(
        "SELECT name, sql FROM src.sqlite_master WHERE type='table' AND sql IS NOT NULL")}
    counts = {}

    def copy(table, where=None, select=None):
        con.execute(ddl[table])
        sel = select or f"SELECT * FROM src.{table}" + (f" WHERE {where}" if where else "")
        con.execute(f"INSERT INTO main.{table} {sel}")
        con.commit()
        counts[table] = con.execute(f"SELECT COUNT(*) FROM main.{table}").fetchone()[0]
        log(f"{table}: {counts[table]:,} rows")

    for t in KEEP_WHOLE:
        if t in ddl:
            copy(t)
    for t, where in FILTERED.items():
        copy(t, where=where)

    copy("sources", select=f"""
        SELECT id, url, kind, tier, angle, title, published,
               CASE WHEN kind IN {OWN_KINDS} THEN text ELSE NULL END AS text,
               n_chars, meta, retrieved_at, content_hash, first_seen, last_checked, version
        FROM src.sources
        WHERE kind <> 'bloomberg' AND COALESCE(url,'') NOT LIKE '%linkedin.com%'""")
    copy("source_versions", select=f"""
        SELECT v.id, v.url, v.version, v.content_hash, v.title,
               CASE WHEN (SELECT s.kind FROM src.sources s WHERE s.url = v.url LIMIT 1) IN {OWN_KINDS}
                    THEN v.text ELSE NULL END AS text,
               v.n_chars, v.retrieved_at
        FROM src.source_versions v
        WHERE COALESCE(v.url,'') NOT LIKE '%linkedin.com%'
          AND NOT EXISTS (SELECT 1 FROM src.sources s WHERE s.url = v.url AND s.kind = 'bloomberg')""")

    log("indexes")
    kept = set(counts)
    for name, tbl, sql in con.execute(
            "SELECT name, tbl_name, sql FROM src.sqlite_master WHERE type='index' AND sql IS NOT NULL"):
        if tbl in kept:
            con.execute(sql)
    con.commit()

    log("path scrub")
    touched = 0
    for t in kept:
        cols = [r[1] for r in con.execute(f"PRAGMA table_info({t})")
                if (r[2] or "").upper() in ("TEXT", "") and r[1] not in ("vec", "block")]
        for c in cols:
            where = " OR ".join([f"{c} LIKE '%Users%'"] + [f"{c} LIKE ?" for _ in REPLACES])
            rows = con.execute(f"SELECT rowid, {c} FROM {t} WHERE {where}",
                               [f"%{w}%" for w, _ in REPLACES]).fetchall()
            for rid, val in rows:
                new = scrub_text(val)
                if new != val:
                    con.execute(f"UPDATE {t} SET {c} = ? WHERE rowid = ?", (new, rid))
                    touched += 1
    con.commit()
    log(f"path scrub: {touched:,} cells changed")

    log("full-text index")
    con.execute(ddl["chunks_fts"])
    con.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    con.commit()

    con.execute("CREATE TABLE public_build (key TEXT PRIMARY KEY, value TEXT)")
    con.executemany("INSERT INTO public_build VALUES (?,?)", [
        ("built_at", time.strftime("%Y-%m-%d %H:%M")),
        ("dropped_tables", ", ".join(DROPPED)),
        ("chunks_kept", "kind in ('sec','research'); web, news, academic and competitor chunks removed"),
        ("sources_text", "stored text kept only for the pipeline's own notes; third-party text "
                         "replaced by NULL, URL/title/date kept"),
        ("excluded_rows", "Bloomberg-sourced rows; LinkedIn-sourced rows; Yahoo-sourced comps rows; "
                          "prices; embeddings"),
    ] + [(f"rows_{k}", str(v)) for k, v in counts.items()])
    con.commit()
    con.execute("DETACH DATABASE src")
    log("vacuum")
    con.execute("VACUUM")
    con.close()
    log(f"done: {DST} {DST.stat().st_size/1e6:,.0f} MB")


if __name__ == "__main__":
    main()
