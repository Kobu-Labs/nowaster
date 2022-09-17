from fastapi import APIRouter

from app.api.endpoints import record, solid

api_router = APIRouter()

api_router.include_router(solid.router)
api_router.include_router(record.router)
