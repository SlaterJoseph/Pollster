from fastapi import APIRouter, HTTPException, status
from app.services.user_service import create_user, get_user_by_id
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: User) -> User:
    """
    Route to register a new user
    :param user: The user payload
    :return: The UserResponse object
    """
    try:
        return create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User)
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