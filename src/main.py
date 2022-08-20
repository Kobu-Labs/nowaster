from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/entries/active")
def get_active(db: Session = Depends(get_db)) -> Optional[schemas.TrackEntry]:
    return crud.get_active(db)


@app.get("/entries/", response_model=List[schemas.TrackEntry])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_track_entries(db)
    return users


@app.get("/entries/{category}", response_model=List[schemas.TrackEntry])
def read_user(category: str, db: Session = Depends(get_db)):
    entries = crud.get_track_entries_by_category(db, category=category)
    if entries is None:
        raise HTTPException(status_code=404, detail="No entries with given category")
    return entries


@app.post("/entries/", response_model=schemas.TrackEntry)
def create_entry(track_entry: schemas.TrackEntryCreate, db: Session = Depends(get_db)):
    return crud.create_track_entry(db=db, track_entry_create=track_entry)
