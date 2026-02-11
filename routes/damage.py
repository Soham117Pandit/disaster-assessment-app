from flask import Blueprint, jsonify

damage_bp = Blueprint("damage", __name__, url_prefix="/damage")

@damage_bp.route("/test")
def test():
    return jsonify({"message": "damage module working"})
