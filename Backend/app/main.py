from contextlib import asynccontextmanager

from fastapi import FastAPI
import os

from app.utils.env_handler import env_config
from app.config.db_config import create_db_and_tables
from app.controller import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    env = os.getenv("APP_ENV", "dev")
    env_config.adjust_env(env)
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(poll_router)

@app.get("/")
async def root():
    return {"message": "Poll Platofrm API is running!"}
