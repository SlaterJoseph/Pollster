from sqlmodel import SQLModel, create_engine, Session
from app.models import comment_model, poll_model, poll_options_model, response_model, user_model

DATABASE_URL = ""

# Remove echo true when deploying
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

