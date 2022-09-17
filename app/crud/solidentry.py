from datetime import datetime, timedelta
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.solidentry import SolidEntry
from app.schemas.solidentry import SolidEntryCreate


def get_active(db: Session) -> Optional[SolidEntry]:
    return (
        db.query(SolidEntry)
        .filter(
            SolidEntry.start_date <= datetime.now(),
            datetime.now() <= SolidEntry.end_date,
        )
        .first()
    )


def get_track_entry_by_id(db: Session, track_id: int) -> Optional[SolidEntry]:
    return db.query(SolidEntry).filter(SolidEntry.id == track_id).first()


def get_track_entries_by_category(db: Session, category: str) -> List[SolidEntry]:
    return db.query(SolidEntry).filter(SolidEntry.category == category).all()


def get_track_entries(db: Session) -> List[SolidEntry]:
    return db.query(SolidEntry).all()


def create_track_entry(db: Session, track_entry_create: SolidEntryCreate) -> SolidEntry:
    print(track_entry_create)
    start_date = datetime.now()
    end_date = datetime.now() + timedelta(minutes=track_entry_create.duration)
    track_entry = SolidEntry(
        **track_entry_create.dict(), start_date=start_date, end_date=end_date
    )
    db.add(track_entry)
    db.commit()
    db.refresh(track_entry)
    return track_entry


def abort_active(db: Session) -> None:
    db.query(SolidEntry).filter(
        SolidEntry.start_date <= datetime.now(),
        datetime.now() <= SolidEntry.end_date,
    ).delete()
    db.commit()
