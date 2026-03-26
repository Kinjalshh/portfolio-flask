from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file

app = Flask(__name__)

# ── DB helper ──────────────────────────────────────────
def get_db():
    """Create and return a new MySQL connection."""
    return mysql.connector.connect(
        host     = os.getenv("DB_HOST",     "localhost"),
        user     = os.getenv("DB_USER",     "root"),
        password = os.getenv("DB_PASSWORD", ""),
        database = os.getenv("DB_NAME",     "portfolio_db")
    )

def init_db():
    """Auto-create the messages table if it doesn't exist."""
    try:
        conn   = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                name       VARCHAR(100)  NOT NULL,
                email      VARCHAR(150)  NOT NULL,
                message    TEXT          NOT NULL,
                created_at TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ messages table ready")
    except Exception as e:
        print(f"❌ DB init error: {e}")

# ── Routes ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    data    = request.get_json()
    name    = (data.get("name")    or "").strip()
    email   = (data.get("email")   or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"error": "All fields are required."}), 400

    try:
        conn   = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True}), 200

    except Exception as e:
        print(f"DB error: {e}")
        return jsonify({"error": "Database error. Please try again."}), 500


# ── Start ──────────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
