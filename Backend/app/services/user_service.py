from sqlalchemy.sql.selectable import SelectBase

from app.models.user_model import User, CreateUser, ReturnUser
from sqlmodel import select, Session
from app.security.password import hash_password, verify_password
from fastapi import status, HTTPException

def create_user(user: CreateUser, session: Session) -> ReturnUser:
    """
    Create a new account
    :param user: The user payload
    :param session: The db session
    :return: The return user payload
    """
    new_user = User(username=user.username, email=user.email, created_at=user.created_at, password=hash_password(user.password))
    session.add(new_user)
    return ReturnUser.model_validate(new_user)

def get_username_password(username: str, password: str, session: Session) -> ReturnUser:
    """
    Login account using username
    :param username: The username of the account
    :param password: The password of the account
    :param session: The db session
    :return: The return user payload
    """
    statement = select(User).where(User.name == username)
    return verify_account(statement, password, session)

def get_email_password(email: str, password: str, session: Session) -> ReturnUser:
    """
    Login account using username
    :param email: The email of the account
    :param password: The password of the account
    :param session: The db session
    :return: The return user payload
    """
    statement = select(User).where(User.email == email)
    return verify_account(statement, password, session)

def verify_account(statement: SelectBase[User], password: str, session: Session) -> ReturnUser:
    """
    Verifying the password is correct, and the user exists
    :param statement: The SQL query
    :param password: The password of the user
    :param session: The db session
    :return: The return user payload
    """
    results = session.exec(statement)
    user = results.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if verify_password(password, user.password):
        return ReturnUser.model_validate(user)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password")
