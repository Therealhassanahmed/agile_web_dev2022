from app import db

class Location(db.Model):
    __tablename__ = "WORLD"
    City = db.Column(db.String(64), primary_key = True)
    Country = db.Column(db.String(64))
    Population = db.Column(db.Integer)

    def __repr__(self):
        return '<Location {}>'.format(self.City)