from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tournament(Base):
    __tablename__ = 'tournament'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    total_players = Column(Integer)
    total_rounds = Column(Integer)
    password = Column(String(255))
    played_games = Column(Integer)
    created_at = Column(DateTime, default=func.now())
