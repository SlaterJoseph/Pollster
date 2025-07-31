from app.utils.env_handler import env_config
from passlib.context import CryptContext

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)