"""Integration test — wymaga postgres na localhost:5432 (services w GHA)."""
import os
import psycopg2


def test_postgres_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        dbname=os.environ["POSTGRES_DB"],
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    assert cur.fetchone()[0] == 1
    conn.close()
