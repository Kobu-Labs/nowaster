from fastapi import APIRouter, FastAPI

from app.api.api import api_router

root_router = APIRouter()
app = FastAPI()

app.include_router(api_router)
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
