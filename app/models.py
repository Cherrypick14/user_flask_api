from flask_sqlalchemy import SQLAlchemy
from app import app

db= SQLAlchemy(app)

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(70), nullable=False)
    username= db.Column(db.String(100),unique=True, nullable=False)
    company= db.Column(db.String(70), nullable=False)
    jobtitle = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __rep__(self):
        return '<User  %r>' % self.username

