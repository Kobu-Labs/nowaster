from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import solidentry as crud
from app.deps import get_db
from app.models.solidentry import SolidEntry as SolidEntryModel
from app.schemas.solidentry import SolidEntry, SolidEntryCreate

router = APIRouter()


@router.get("/entries/active")
def get_active(db: Session = Depends(get_db)) -> Optional[SolidEntryModel]:
    return crud.get_active(db)


@router.get("/entries/", response_model=List[SolidEntry])
def read_users(db: Session = Depends(get_db)) -> List[SolidEntryModel]:
    users = crud.get_track_entries(db)
    return users


@router.get("/entries/{category}", response_model=List[SolidEntry])
def read_user(category: str, db: Session = Depends(get_db)) -> List[SolidEntryModel]:
    entries = crud.get_track_entries_by_category(db, category=category)
    if not entries:
        raise HTTPException(status_code=404, detail="No entries with given category")
    return entries


@router.post("/entries/", response_model=SolidEntry)
def create_entry(
    track_entry: SolidEntryCreate, db: Session = Depends(get_db)
) -> SolidEntryModel:
    return crud.create_track_entry(db=db, track_entry_create=track_entry)


@router.delete("/active/", response_model=SolidEntry)
def abort_active(db: Session = Depends(get_db)) -> None:
    crud.abort_active(db=db)
