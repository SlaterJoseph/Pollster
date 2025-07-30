from fastapi import FastAPI
import os

from app.utils.env_handler import adjust_env
from app.config.db_config import create_db_and_tables

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Poll Platofrm API is running!"}

@app.on_event('startup')
async def startup_event():
    env = os.getenv("APP_ENV", "dev")
    adjust_env(env)
    create_db_and_tables()