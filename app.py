from flask import Flask, render_template, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ── DATABASE CONFIG ─────────────────────────────
DATABASE_URL = os.environ.get("DATABASE_URL")

# Fix for Render PostgreSQL URL
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ── MODEL (TABLE) ───────────────────────────────
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(150))
    message = db.Column(db.Text)

# ── ROUTES ──────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"error": "All fields are required."}), 400

    try:
        new_msg = Message(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()
        return jsonify({"success": True}), 200

    except Exception as e:
        print(f"DB error: {e}")
        return jsonify({"error": "Database error"}), 500


# ── INIT DB (RUN ONCE) ──────────────────────────
@app.route("/init-db")
def init_db():
    db.create_all()
    return "Database created!"

# ── START ───────────────────────────────────────
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
