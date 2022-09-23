from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class SolidEntry(Base):
    __tablename__ = "SolidEntry"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    description = Column(String)
