from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker()
Base = declarative_base()
