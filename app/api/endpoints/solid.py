from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import solidentry as crud
from app.deps import get_db
from app.models.solidentry import SolidEntry 
from app.schemas.solidentry import SolidEntryInDb, SolidEntryCreate

router = APIRouter()


@router.get("/entries/active")
def get_active(db: Session = Depends(get_db)) -> Optional[SolidEntry]:
    return crud.get_active(db)


@router.get("/entries/", response_model=List[SolidEntryInDb])
def read_users(db: Session = Depends(get_db)) -> List[SolidEntry]:
    users = crud.get_all(db)
    return users


@router.get("/entries/{category}", response_model=List[SolidEntryInDb])
def read_user(category: str, db: Session = Depends(get_db)) -> List[SolidEntry]:
    entries = crud.get_all_by_category(db, category=category)
    if not entries:
        raise HTTPException(status_code=404, detail="No entries with given category")
    return entries


@router.post("/entries/", response_model=SolidEntryInDb)
def create_entry(
    track_entry: SolidEntryCreate, db: Session = Depends(get_db)
) -> SolidEntry:
    return crud.create(db=db, entry=track_entry)


@router.delete("/active/", response_model=SolidEntryInDb)
def abort_active(db: Session = Depends(get_db)) -> None:
    crud.abort_active(db=db)
