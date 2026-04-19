from fastapi import FastAPI
import uvicorn

from .api.v1.api import api_router

app = FastAPI(title="ReadMe Backend", version="0.1.0")

app.include_router(api_router, prefix="/api/v1")
