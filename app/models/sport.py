from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sport(Base):
    __tablename__ = 'sport'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tournament_id = Column(Integer, ForeignKey('tournament.id'))
    created_at = Column(DateTime, default=func.now())
