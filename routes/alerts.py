from flask import Blueprint, request, jsonify
from extensions import db
from database.models import Alert

alerts_bp = Blueprint("alerts", __name__, url_prefix="/alerts")

@alerts_bp.route("/create", methods=["POST"])
def create_alert():
    data = request.json

    alert = Alert(
        disaster_type=data["disaster_type"],
        severity=data["severity"],
        area_id=data["area_id"]
    )

    db.session.add(alert)
    db.session.commit()

    return jsonify({"message": "Alert created successfully"})
