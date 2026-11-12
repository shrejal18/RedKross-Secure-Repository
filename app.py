"""Fictional sample service for defensive security training."""

from flask import Flask, request, jsonify

app = Flask(__name__)

MAX_DISPLAY_NAME_LENGTH = 80
ALLOWED_PROFILE_FIELDS = {"display_name"}


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "northstar-training"
    })


@app.post("/profile")
def profile():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({"error": "A valid JSON object is required"}), 400

    unexpected_fields = set(payload.keys()) - ALLOWED_PROFILE_FIELDS

    if unexpected_fields:
        return jsonify({"error": "Unexpected fields provided"}), 400

    if "display_name" not in payload:
        return jsonify({"error": "display_name is required"}), 400

    display_name = payload["display_name"]

    if not isinstance(display_name, str):
        return jsonify({"error": "display_name must be text"}), 400

    display_name = display_name.strip()

    if not display_name:
        return jsonify({"error": "display_name cannot be empty"}), 400

    if len(display_name) > MAX_DISPLAY_NAME_LENGTH:
        return jsonify({"error": "display_name too long"}), 400

    return jsonify({"display_name": display_name})


if __name__ == "__main__":
    app.run()