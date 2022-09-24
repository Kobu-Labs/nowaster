from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import solidentry
from app.models.recordentry import RecordEntry
from app.models.solidentry import SolidEntry
from app.schemas.recordentry import CreateRecordEntry
from app.schemas.solidentry import SolidEntryCreate


def create_new_entry(db: Session, entry_schema: CreateRecordEntry) -> RecordEntry:
    start_date = datetime.now()
    entry = RecordEntry(**entry_schema.dict(), start_date=start_date)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_active_entry(db: Session) -> List[RecordEntry]:
    return db.query(RecordEntry).all()


def finish_entry(db: Session) -> SolidEntry:
    # TODO: this currently doesnt support more active record entries,
    # or rather which active entry will be finished is undefined if theres more than one
    entry = db.query(RecordEntry).one_or_none()
    if entry is None:
        raise HTTPException(404)

    solid_entry = SolidEntryCreate(
        category=entry.category,
        description=entry.description,
        start_date=entry.start_date,
        end_date=datetime.now(),
    )
    result = solidentry.create_new_entry(db, solid_entry)
    ok = db.query(RecordEntry).filter(RecordEntry.id == entry.id).delete()
    if not ok:
        print("ERROR DELETING THE ENTRY")
    db.commit()
    return result
