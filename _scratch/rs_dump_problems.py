"""Dump latest problem versions for physics collections to JSONL."""
import os, json
from dotenv import load_dotenv
import psycopg2

load_dotenv(r"C:\Users\Mark Eichenlaub\github\eigennode\scripts\.env")

conn = psycopg2.connect(
    host=os.environ["REDSHIFT_HOST"],
    port=int(os.environ.get("REDSHIFT_PORT", "5439")),
    dbname=os.environ["REDSHIFT_DBNAME"],
    user=os.environ["REDSHIFT_USER"],
    password=os.environ["REDSHIFT_PASSWORD"],
    options="-c statement_timeout=300000",
)
cur = conn.cursor()

COLLECTIONS = {405: "MCH", 268: "I2P", 539: "MS"}

cur.execute("""
    SELECT collection_id, lesson, problem_id, "order"
    FROM aops3.crypt_collections_problems
    WHERE collection_id IN (405, 268, 539)
      AND deleted_at IS NULL AND is_active = 1
    ORDER BY collection_id, lesson, "order"
""")
assignments = cur.fetchall()
pids = sorted({r[2] for r in assignments})
print(f"{len(assignments)} assignments, {len(pids)} unique problems")

pmap = {}
CHUNK = 500
for i in range(0, len(pids), CHUNK):
    chunk = pids[i:i+CHUNK]
    ph = ",".join(["%s"] * len(chunk))
    cur.execute(f"""
        SELECT problem_id, version, problem_text, solution_text, hints,
               answer, answer_type, problem_type
        FROM aops3.crypt_problem_versions
        WHERE problem_id IN ({ph})
        ORDER BY problem_id, version DESC
    """, chunk)
    for r in cur.fetchall():
        if r[0] not in pmap:  # latest version only
            pmap[r[0]] = r

out = r"C:\Users\Mark Eichenlaub\github\aapt-sm26-poster\_scratch\problems.jsonl"
with open(out, "w", encoding="utf-8") as f:
    for coll, lesson, pid, order in assignments:
        v = pmap.get(pid)
        if not v:
            continue
        rec = {
            "course": COLLECTIONS[coll], "lesson": lesson, "order": order,
            "problem_id": pid, "problem_type": v[7], "answer_type": v[6],
            "answer": v[5], "hints": v[4],
            "problem_text": v[2], "solution_text": v[3],
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("wrote", out)
conn.close()
