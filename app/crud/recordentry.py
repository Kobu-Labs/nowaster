from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from app.models.recordentry import RecordEntry
from app.schemas.recordentry import CreateRecordEntry, RecordEntryInDb

# from app.schemas.solidentry import SolidEntryCreate


def create_timed_entry(db: Session, entry_schema: CreateRecordEntry) -> RecordEntry:
    start_date = datetime.now()
    entry = RecordEntry(**entry_schema.dict(), start_date=start_date)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_active_timed(db: Session) -> List[RecordEntry]:
    return db.query(RecordEntry).all()


# def finish_timed_entry(db: Session, entry_id: int)-> None:
#     entry = db.query(RecordEntry).filter(RecordEntry.id == entry_id).one_or_none()
#     if entry is None:
#         return
#
#     end_date = datetime.now()
#     duration = (end_date - entry.start_date).total_seconds() // 60
#     solid_entry = SolidEntryCreate()
#     fixed_entry = schemas.FixedEntry(
#         category=entry.category,
#         duration=duration,
#         start_date=entry.start_date,
#         end_date=end_date,
#         description=entry.description
#     )
#     db.add(fixed_entry)
