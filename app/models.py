from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Users sql table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    high_score_easy = db.Column(db.Integer, default=0)
    high_score_normal = db.Column(db.Integer, default=0)
    high_score_hard = db.Column(db.Integer, default=0)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)



    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Population data sql table
class Location(db.Model):
    __tablename__ = "WORLD"
    City = db.Column(db.String(64), primary_key = True)
    Country = db.Column(db.String(64))
    Population = db.Column(db.Integer)

    def __repr__(self):
        return '<Location {}>'.format(self.City)