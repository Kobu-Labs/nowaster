from fastapi import APIRouter, FastAPI

from app.api.api import api_router
from app.db import Base, engine


Base.metadata.create_all(bind=engine)

root_router = APIRouter()
app = FastAPI()

app.include_router(api_router)
app.include_router(root_router)

