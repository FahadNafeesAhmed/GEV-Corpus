"""Embed corpus chunks with a local Ollama embedding model.

    python embed.py --ticker GEV
    python embed.py --all --batch 64

Vectors are stored as raw float32 BLOBs in SQLite. There is deliberately no
vector database: at ~215k chunks x 768 dims this is ~630 MB, and a brute-force
numpy dot product over it takes well under a second. Vector databases earn their
keep at tens of millions of vectors, not hundreds of thousands.
"""
from __future__ import annotations

import argparse
import json
import struct
import time
import urllib.request

from common import connect, log

OLLAMA_EMBED = "http://localhost:11434/api/embed"
MODEL = "nomic-embed-text"


def embed_batch(texts: list[str], model: str, timeout: int = 180):
    body = json.dumps({"model": model, "input": texts, "keep_alive": "30m"}).encode()
    req = urllib.request.Request(OLLAMA_EMBED, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read()).get("embeddings") or []


def pack(vec) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def unpack(blob: bytes):
    return struct.unpack(f"{len(blob)//4}f", blob)


def run(con, ticker: str | None, batch: int, model: str, limit: int | None = None,
        deadline: float | None = None) -> int:
    sql = """SELECT c.id, c.ticker, c.text FROM chunks c
             LEFT JOIN embeddings e ON e.chunk_id = c.id
             WHERE e.chunk_id IS NULL"""
    params: list = []
    if ticker and ticker != "ALL":
        sql += " AND c.ticker = ?"
        params.append(ticker)
    sql += " ORDER BY c.id"
    if limit:
        sql += f" LIMIT {int(limit)}"
    rows = con.execute(sql, params).fetchall()
    if not rows:
        log("  embeddings: nothing to do")
        return 0

    log(f"  embedding {len(rows):,} chunks with {model} (batch {batch})")
    done = 0
    t0 = time.time()
    for i in range(0, len(rows), batch):
        if deadline and time.time() > deadline:
            log("  embeddings: deadline reached, stopping cleanly")
            break
        part = rows[i:i + batch]
        texts = [r[2][:2000] for r in part]
        try:
            vecs = embed_batch(texts, model)
        except Exception as exc:
            log(f"    embed error ({type(exc).__name__}); retrying once in 10s")
            time.sleep(10)
            try:
                vecs = embed_batch(texts, model)
            except Exception as exc2:
                log(f"    embed failed again: {str(exc2)[:90]} - skipping batch")
                continue
        if len(vecs) != len(part):
            log(f"    length mismatch ({len(vecs)} vs {len(part)}) - skipping batch")
            continue
        for (cid, tick, _txt), v in zip(part, vecs):
            con.execute(
                "INSERT OR REPLACE INTO embeddings(chunk_id,ticker,model,dim,vec) VALUES (?,?,?,?,?)",
                (cid, tick, model, len(v), pack(v)))
        done += len(part)
        if (i // batch) % 20 == 0:
            con.commit()
            rate = done / max(time.time() - t0, 1)
            eta = (len(rows) - done) / max(rate, 1e-6) / 60
            log(f"    {done:,}/{len(rows):,}  {rate:.0f}/s  ETA {eta:.0f}m")
    con.commit()
    log(f"  embeddings: {done:,} chunks in {(time.time()-t0)/60:.1f} min")
    return done


def search(con, query: str, ticker: str | None, k: int, model: str):
    """Brute-force cosine similarity. No index, no vector DB - it is fast enough."""
    import numpy as np
    qv = embed_batch([query], model)[0]
    q = np.array(qv, dtype=np.float32)
    q /= (np.linalg.norm(q) + 1e-9)

    sql = """SELECT e.chunk_id, e.vec, c.ticker, c.form, c.filing_date, c.section, c.text
             FROM embeddings e JOIN chunks c ON c.id = e.chunk_id"""
    params: list = []
    if ticker and ticker != "ALL":
        sql += " WHERE e.ticker = ?"
        params.append(ticker)
    rows = con.execute(sql, params).fetchall()
    if not rows:
        print("no embeddings yet - run: python embed.py --ticker GEV")
        return

    mat = np.frombuffer(b"".join(r[1] for r in rows), dtype=np.float32)
    mat = mat.reshape(len(rows), -1)
    mat = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
    scores = mat @ q
    for idx in np.argsort(-scores)[:k]:
        _cid, _v, tick, form, fdate, section, text = rows[idx]
        snippet = " ".join(text.split())[:260]
        print(f"--- {scores[idx]:.3f}  {tick}  {form}  {fdate}  [{section[:48]}]")
        print(f"    {snippet}\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", default="GEV")
    p.add_argument("--all", action="store_true")
    p.add_argument("--batch", type=int, default=64)
    p.add_argument("--limit", type=int)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--search")
    p.add_argument("-k", type=int, default=8)
    a = p.parse_args()

    con = connect()
    if a.search:
        search(con, a.search, None if a.all else a.ticker, a.k, a.model)
    else:
        run(con, None if a.all else a.ticker, a.batch, a.model, a.limit)
    con.close()


if __name__ == "__main__":
    main()
