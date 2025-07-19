from datetime import datetime
from typing import Optional

from ..models.user_model import UserCreate, UserResponse

user_storage = []
user_id_counter = 1

def create_user(user: UserCreate) -> UserResponse:
    """
    Creating new user
    :param user: The user payload being created
    :return: The UserResponse object
    """
    global user_id_counter

    if get_user_by_username(user.username):
        raise ValueError("Username already exists")

    new_user = UserResponse(
        id=user_id_counter,
        username=user.username,
        password=user.password,
        email=user.email,
        created_at=datetime.now(),
        polls_voted=[]
    )

    user_storage.append(new_user)
    user_id_counter += 1
    return new_user


def get_user_by_username(username: str) -> Optional[UserResponse]:
    """
    Getting account info from username
    :param username: Users username
    :return: Either None or UserResponse object
    """
    for user in user_storage:
        if user.username == username:
            return user
        return None

def get_user_by_email(email: str) -> Optional[UserResponse]:
    """
    Getting account info from email
    :param email: Users email
    :return: Either None or UserResponse object
    """
    for user in user_storage:
        if user.email == email:
            return user
        return None

def get_user_by_id(id: int) -> Optional[UserResponse]:
    """
    Getting account info from id
    :param id: Users id
    :return: Either none or UserResponse object
    """
    for user in user_storage:
        if user.id == id:
            return user
        return None
