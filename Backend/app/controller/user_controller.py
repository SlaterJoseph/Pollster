from fastapi import APIRouter, HTTPException, status, Depends
from app.services.user_service import create_user, get_username_password, get_email_password, get_user_by_id
from app.models.user_model import User, LoginUser, CreateUser 
from sqlmodel import Session
from app.config.db_config import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: CreateUser, session: Session = Depends(get_session())) -> User:
    """
    Route to register a new user
    :param session: Database session
    :param user: The user payload
    :return: The UserResponse object
    """
    try:
        return create_user(user, session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=User, status_code=status.HTTP_200_OK)
def login_user(user: LoginUser) -> User:
    """
    Route to authenticate and login a user
    :param user: The login credentials containing either username or email, and password
    :return: The UserResponse object of the authenticated user
    """
    try:
        return login_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(user_id: int) -> User:
    """
    Route to get a specific user
    :param user_id: The user id
    :return: The UserResponse object
    """
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user