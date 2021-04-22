import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    birthdate = Column(DateTime, unique=True)
    joined_at = Column(DateTime, default=datetime.date.today())
    password = Column(String(80))
    tournaments = relationship('Tournament', backref='user', lazy=True)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "birthdate": self.birthdate,
                "joined_at": self.joined_at}

    def __init__(self, username=None, password=None, birthdate=None):
        self.username = username
        self.password = password
        self.birthdate = birthdate

    def __repr__(self):
        return '<User %r>' % self.username
