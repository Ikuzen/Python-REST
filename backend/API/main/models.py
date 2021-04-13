import datetime

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    birthdate = db.Column(db.DateTime, unique=True)
    joined_at = db.Column(db.DateTime, default=datetime.date.today())
    password = db.Column(db.String(80))

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "birthdate": self.birthdate,
                "password" : self.password,
                "joined_at":self.joined_at}

    def __init__(self, username=None, password=None, birthdate=None):
        self.username = username
        self.password = password
        self.birthdate = birthdate

    def __repr__(self):
        return '<User %r>' % self.username