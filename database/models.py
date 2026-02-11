from datetime import datetime
from extensions import db


# ----------------------------
# AREA / ZONE
# ----------------------------
class Area(db.Model):
    __tablename__ = "area"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    risk_level = db.Column(db.String(20))  # Low / Medium / High


# ----------------------------
# DISASTER ALERT
# ----------------------------
class Alert(db.Model):
    __tablename__ = "alert"

    id = db.Column(db.Integer, primary_key=True)
    disaster_type = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    area_id = db.Column(db.Integer, db.ForeignKey("area.id"))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# DAMAGE REPORT (DM-4 CORE)
# ----------------------------
class DamageReport(db.Model):
    __tablename__ = "damage_report"

    id = db.Column(db.Integer, primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey("area.id"))
    damage_type = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    people_affected = db.Column(db.Integer)

    confidence_score = db.Column(db.Integer)
    final_score = db.Column(db.Integer)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------
# NEEDS
# ----------------------------
class Need(db.Model):
    __tablename__ = "need"

    id = db.Column(db.Integer, primary_key=True)
    damage_report_id = db.Column(db.Integer, db.ForeignKey("damage_report.id"))

    medical = db.Column(db.Boolean, default=False)
    food = db.Column(db.Boolean, default=False)
    shelter = db.Column(db.Boolean, default=False)
    rescue = db.Column(db.Boolean, default=False)
