from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import recordentry as crud
from app.deps import get_db
from app.models.recordentry import RecordEntry
from app.models.solidentry import SolidEntry
from app.schemas.recordentry import CreateRecordEntry, RecordEntryInDb
from app.schemas.solidentry import SolidEntryInDb

router = APIRouter()


@router.post("/entry/record/", response_model=RecordEntryInDb)
def create_new_entry(
    entry_schema: CreateRecordEntry, db: Session = Depends(get_db)
) -> RecordEntry:
    return crud.create_new_entry(db=db, entry_schema=entry_schema)


@router.get("/entry/record/active", response_model=List[RecordEntryInDb])
def get_active_entry(db: Session = Depends(get_db)) -> List[RecordEntry]:
    return crud.get_active_entry(db)


@router.post("/entry/record/finish", response_model=SolidEntryInDb)
def finish_entry(db: Session = Depends(get_db)) -> SolidEntry:
    return crud.finish_entry(db)
