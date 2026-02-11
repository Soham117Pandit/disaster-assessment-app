from flask import Blueprint, jsonify
from database.models import DamageReport, Area

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/overview")
def overview():
    reports = DamageReport.query.order_by(DamageReport.final_score.desc()).all()

    data = []
    for r in reports:
        area = Area.query.get(r.area_id)
        data.append({
            "area": area.name,
            "damage_type": r.damage_type,
            "severity": r.severity,
            "people_affected": r.people_affected,
            "score": r.final_score
        })

    return jsonify(data)
