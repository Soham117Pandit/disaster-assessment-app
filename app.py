from flask import Flask, jsonify
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def home():
        return jsonify({"status": "server running"})

    # 🔹 TEST ROUTE FOR SQLITE
    from database.models import Area

    @app.route("/create-area")
    def create_area():
        area = Area(name="Hostel A", risk_level="High")
        db.session.add(area)
        db.session.commit()
        return {"message": "Area created"}

    # 🔹 CREATE TABLES
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
