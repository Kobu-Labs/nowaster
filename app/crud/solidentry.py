from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.solidentry import SolidEntry
from app.schemas.solidentry import SolidEntryCreate


def get_active_entry(db: Session) -> Optional[SolidEntry]:
    return (
        db.query(SolidEntry)
        .filter(
            SolidEntry.start_date <= datetime.now(),
            datetime.now() <= SolidEntry.end_date,
        )
        .first()
    )


def get_all_entries(db: Session) -> List[SolidEntry]:
    return db.query(SolidEntry).all()


def create_new_entry(db: Session, entry: SolidEntryCreate) -> SolidEntry:
    track_entry = SolidEntry(**entry.dict())
    db.add(track_entry)
    db.commit()
    db.refresh(track_entry)
    return track_entry


def delete_active_entry(db: Session) -> None:
    db.query(SolidEntry).filter(
        SolidEntry.start_date <= datetime.now(),
        datetime.now() <= SolidEntry.end_date,
    ).delete()
    db.commit()
