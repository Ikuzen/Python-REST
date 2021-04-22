import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    size = Column(Integer, nullable=False)
    tournament_type = Column(String(20), default='single-elimination')
    organizer_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "size": self.size,
                "tournament_type": self.tournament_type}

    def __init__(self, name=None, size=None, tournament_type=None, organizer_id=None):
        self.name = name
        self.size = size
        self.tournament_type = tournament_type
        self.organizer_id = organizer_id

    def __repr__(self):
        return '<User %r>' % self.username
