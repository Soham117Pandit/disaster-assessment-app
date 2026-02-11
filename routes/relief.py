from flask import Blueprint, jsonify

relief_bp = Blueprint("relief", __name__, url_prefix="/relief")

@relief_bp.route("/test")
def test():
    return jsonify({"message": "relief working"})
