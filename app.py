from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# ── Routes ─────────────────────────────────────────────
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

    # Just print instead of saving
    print(f"Name: {name}, Email: {email}, Message: {message}")

    return jsonify({"success": True}), 200


# ── Start ──────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
