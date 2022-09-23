from datetime import datetime
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


def get_by_id(db: Session, track_id: int) -> Optional[SolidEntry]:
    return db.query(SolidEntry).filter(SolidEntry.id == track_id).first()


def get_all_by_category(db: Session, category: str) -> List[SolidEntry]:
    return db.query(SolidEntry).filter(SolidEntry.category == category).all()


def get_all(db: Session) -> List[SolidEntry]:
    return db.query(SolidEntry).all()


def create(db: Session, entry: SolidEntryCreate) -> SolidEntry:
    track_entry = SolidEntry(**entry.dict())
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
