from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EntryBase(BaseModel):
    category: str
    duration: float
    description: Optional[str] = None


class SolidEntryCreate(EntryBase):
    ...


class SolidEntry(EntryBase):
    id: int
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True
