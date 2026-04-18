from fastapi import FastAPI
import uvicorn

from .api.v1.db import get_engine, ping_db

app = FastAPI(title="ReadMe Backend", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/db")
def health_db() -> dict[str, str]:
    engine = get_engine()
    ping_db(engine)
    return {"status": "ok"}
