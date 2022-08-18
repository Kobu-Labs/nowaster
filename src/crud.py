from datetime import datetime, timedelta 
from typing import List, Optional

from sqlalchemy.orm import Session
from . import models, schemas


def get_track_entry_by_id(db: Session, track_id: int) -> Optional[models.TrackEntry]:
    return db.query(models.TrackEntry).filter(models.TrackEntry.id == track_id).first()

def get_track_entries_by_category(db: Session, category: str) -> List[models.TrackEntry]:
    return db.query(models.TrackEntry).filter(models.TrackEntry.category == category).all()

def get_track_entries(db: Session) -> List[models.TrackEntry]:
    return db.query(models.TrackEntry).all()

def create_track_entry(db: Session, track_entry_create: schemas.TrackEntryCreate) -> models.TrackEntry:
    start_date = datetime.now()
    end_date = datetime.now() + timedelta(hours=track_entry_create.duration)
    track_entry = models.TrackEntry(**track_entry_create.dict(), start_date=start_date, end_date=end_date)
    db.add(track_entry)
    db.commit()
    db.refresh(track_entry)
    return track_entry

