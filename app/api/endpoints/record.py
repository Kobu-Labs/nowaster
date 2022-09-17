from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import recordentry as crud
from app.deps import get_db
from app.models.recordentry import RecordEntry
from app.schemas.recordentry import CreateRecordEntry, RecordEntryInDb

router = APIRouter()


@router.post("/timed/", response_model=RecordEntryInDb)
def create_timed_entry(
    entry_schema: CreateRecordEntry, db: Session = Depends(get_db)
) -> RecordEntry:
    return crud.create_timed_entry(db=db, entry_schema=entry_schema)


@router.get("/timed/active", response_model=List[RecordEntryInDb])
def get_active_timed(db: Session = Depends(get_db)) -> List[RecordEntry]:
    return crud.get_active_timed(db)


# @router.post("/timed/{entry_id}", response_model = RecordEntry)
# def finish_timed_entry(entry_id: int, db: Session = Depends(get_db)) -> None:
#     return crud.finish_timed_entry(db, entry_id)
