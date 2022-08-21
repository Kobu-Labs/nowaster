from sqlalchemy import Column, DateTime, Float, Integer, String

from .database import Base

__all__ = ["TrackEntry", "Base"]


class TrackEntry(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    duration = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    description = Column(String)
