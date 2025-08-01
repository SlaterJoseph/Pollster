from contextlib import asynccontextmanager

from fastapi import FastAPI
import os

from app.utils.env_handler import env_config
from app.config.db_config import get_engine
from app.controller import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    env = os.getenv("APP_ENV", "dev")
    env_config.adjust_env(env)
    get_engine()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(poll_router)

@app.get("/")
async def root():
    return {"message": "Poll Platofrm API is running!"}
