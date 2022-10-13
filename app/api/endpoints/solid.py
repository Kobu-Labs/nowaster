from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import solidentry as crud
from app.deps import get_db
from app.models.solidentry import SolidEntry
from app.schemas.solidentry import SolidEntryCreate, SolidEntryInDb

router = APIRouter()


@router.get("/entry/solid/active")
def get_active_entry(local_time: datetime, db: Session = Depends(get_db)) -> Optional[SolidEntry]:
    return crud.get_active_entry(db, local_time)


@router.get("/entry/solid", response_model=List[SolidEntryInDb])
def get_all_entries(db: Session = Depends(get_db)) -> List[SolidEntry]:
    return crud.get_all_entries(db)


@router.post("/entry/solid", response_model=SolidEntryInDb)
def create_new_entry(
    track_entry: SolidEntryCreate, db: Session = Depends(get_db)
) -> SolidEntry:
    return crud.create_new_entry(db=db, entry=track_entry)


@router.delete("/entry/solid", response_model=SolidEntryInDb)
def delete_active_entry(db: Session = Depends(get_db)) -> None:
    crud.delete_active_entry(db=db)
