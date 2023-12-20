from fastapi import FastAPI

from src.api import api_router
from .config import APP_NAME, APP_VERSION, APP_CONTACT

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    openapi_url="/docs/json",
    docs_url="/docs",
    redoc_url="/redoc",
    contact=APP_CONTACT,
)

app.include_router(api_router)
