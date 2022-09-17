from fastapi import APIRouter, FastAPI

from app.api.api import api_router

root_router = APIRouter()
app = FastAPI()

app.include_router(api_router)
app.include_router(root_router)

