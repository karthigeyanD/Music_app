from fastapi import FastAPI

from app.core.config import settings
from app.database.connection import Base, engine

import app.models

app = FastAPI(
    title=settings.APP_NAME,
    description="Music Streaming Application API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():

    return {
        "message": "Welcome to Music Streaming API",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }