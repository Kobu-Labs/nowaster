from collections.abc import Callable
from typing import Optional
from fastapi import APIRouter, FastAPI
from sqlalchemy import create_engine
from starlette.types import Scope, Receive, Send

from app.api.api import api_router
from app.db import SessionLocal, Base
from config import settings

class Nowaster:
    __root_router = APIRouter()
    __app = FastAPI()

    def __init__(
        self, postprocess_db_url: Optional[Callable[[str], str]] = None
    ) -> None:
        self.__app.include_router(api_router)
        self.__app.include_router(self.__root_router)

        if postprocess_db_url is None:
            db_url = settings.database_url
        else:
            db_url = postprocess_db_url(settings.database_url)
        engine = create_engine(db_url)
        Base.metadata.create_all(bind=engine)
        SessionLocal.configure(bind=engine)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        await self.__app(scope, receive, send)
