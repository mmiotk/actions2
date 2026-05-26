import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


def get_db():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=int(os.environ.get("POSTGRES_PORT", "5432")),
        user=os.environ.get("POSTGRES_USER", "app"),
        password=os.environ.get("POSTGRES_PASSWORD", "secret"),
        dbname=os.environ.get("POSTGRES_DB", "shop"),
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
