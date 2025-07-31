from app.models.user_model import User, CreateUser, LoginUser
from sqlmodel import select, Session

def create_user(user: CreateUser, session: Session) -> User:
    new_user = User(username=user.username, email=user.email, created_at=user.created_at)

def get_username_password(username: str, hashed_password: str, session: Session) -> bool:
    pass

def get_email_password(username: str, hashed_password: str, session: Session) -> bool:
    pass