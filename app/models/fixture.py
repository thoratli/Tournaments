from sqlalchemy import Column, DateTime, Boolean, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Fixture(Base):
    __tablename__ = 'fixture'
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournament.id'))
    home_id = Column(Integer, ForeignKey('team.id'))
    home_score = Column(Integer)
    away_id = Column(Integer, ForeignKey('team.id'))
    away_score = Column(Integer)
    played = Column(Boolean)
    created_at = Column(DateTime, default=func.now())
