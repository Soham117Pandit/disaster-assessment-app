from extensions import db

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    risk_level = db.Column(db.String(50))

def __repr__(self):
        return f"<Area {self.name}>"
