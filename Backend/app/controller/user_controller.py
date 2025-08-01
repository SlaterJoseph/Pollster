from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from pydantic import ValidationError

from app.services.user_service import create_user, get_username_password, get_email_password
from app.models.user_model import User, LoginUser, CreateUser, ReturnUser
from app.config.db_config import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=ReturnUser, status_code=status.HTTP_201_CREATED)
async def register_user(user: CreateUser, session: Session = Depends(get_session)) -> ReturnUser:
    """
    Route to register a new user
    :param session: Database session
    :param user: The user payload
    :return: The UserResponse object
    """
    try:
        user = await create_user(user, session)
        await session.commit()
        return user
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/login", response_model=User, status_code=status.HTTP_200_OK)
def login_user(user: LoginUser, session: Session = Depends(get_session)) -> ReturnUser:
    """
    Route to authenticate and login a user
    :param session: Database session
    :param user: The login credentials containing either username or email, and password
    :return: The UserResponse object of the authenticated user
    """
    try:
        if user.username is not None:
            user = get_username_password(user.username, user.password, session)
        elif user.email is not None:
            user = get_email_password(user.email, user.password, session)
        else:
            raise ValueError

        session.commit()
        return user
    except HTTPException as e:
        raise e
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Either username or email required")
