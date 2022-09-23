from typing import Generator

from sqlalchemy.orm import sessionmaker

from app.db import SessionLocal


def get_db() -> Generator[sessionmaker, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
