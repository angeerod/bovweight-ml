from flask import Blueprint, request, jsonify
from .predictor import estimate_weight

bp = Blueprint("api", __name__)


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    required = ["height_cm", "length_cm", "girth_cm"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    try:
        weight = estimate_weight(
            float(data["height_cm"]),
            float(data["length_cm"]),
            float(data["girth_cm"]),
        )
        return jsonify({"estimated_weight_kg": round(weight, 2)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 422
