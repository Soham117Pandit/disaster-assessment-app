from flask import Flask, jsonify
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)   # ✅ app is created HERE
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def home():
        return jsonify({"status": "server running"})

    # ✅ import AFTER app is created
    from routes.relief import relief_bp
    from routes.damage import damage_bp

    # ✅ register AFTER import
    app.register_blueprint(relief_bp)
    app.register_blueprint(damage_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

