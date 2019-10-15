from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    scored_goals = Column(Integer)
    conceded_goals = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('tournament.id'))
    assigned_team = Column(String(255))
    created_at = Column(DateTime, default=func.now())
