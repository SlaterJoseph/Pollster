from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Poll Platofrm API is running!"}