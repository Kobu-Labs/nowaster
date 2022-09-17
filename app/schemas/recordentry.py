from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RecordEntryBase(BaseModel):
    category: str
    description: Optional[str] = None


class CreateRecordEntry(RecordEntryBase):
    ...


class RecordEntryInDb(RecordEntryBase):
    id: int
    start_date: datetime

    class Config:
        orm_mode = True
