from fastapi import FastAPI
from app.config.db_config import create_db_and_tables
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Poll Platofrm API is running!"}

if __name__ == "__main__":
    create_db_and_tables()