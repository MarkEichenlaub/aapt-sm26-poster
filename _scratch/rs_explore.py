"""Explore Redshift for enrollment/submission tables."""
import os, sys
from dotenv import load_dotenv
import psycopg2

load_dotenv(r"C:\Users\Mark Eichenlaub\github\eigennode\scripts\.env")

conn = psycopg2.connect(
    host=os.environ["REDSHIFT_HOST"],
    port=int(os.environ.get("REDSHIFT_PORT", "5439")),
    dbname=os.environ["REDSHIFT_DBNAME"],
    user=os.environ["REDSHIFT_USER"],
    password=os.environ["REDSHIFT_PASSWORD"],
    options="-c statement_timeout=120000",
)
cur = conn.cursor()

q = sys.argv[1] if len(sys.argv) > 1 else "tables"

if q == "tables":
    pat = sys.argv[2] if len(sys.argv) > 2 else "%enroll%"
    cur.execute("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_name ILIKE %s
        ORDER BY table_schema, table_name
    """, (pat,))
    for r in cur.fetchall():
        print(f"{r[0]}.{r[1]}")
elif q == "cols":
    schema, table = sys.argv[2].split(".")
    cur.execute("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = %s AND table_name = %s
        ORDER BY ordinal_position
    """, (schema, table))
    for r in cur.fetchall():
        print(f"{r[0]}  {r[1]}")
elif q == "sql":
    cur.execute(sys.argv[2])
    for r in cur.fetchall():
        print("\t".join(str(x) for x in r))

conn.close()
