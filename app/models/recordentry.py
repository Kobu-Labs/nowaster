from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class RecordEntry(Base):
    __tablename__ = "TimedEntry"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    description = Column(String)
