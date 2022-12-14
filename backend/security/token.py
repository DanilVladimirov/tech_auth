import passlib.context
import jose.jwt
import datetime as dt
from models import user_models
from settings import settings


pwd_context = passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(user: user_models.User, expires_delta: dt.timedelta) -> str:
    to_encode = {"exp": dt.datetime.utcnow() + expires_delta, "sub": user.username}
    return jose.jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


async def set_and_get_tokens(user: user_models.User) -> dict[str, str]:
    access_token_expires = dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(user, expires_delta=access_token_expires)

    return {
        "token_type": "bearer",
        "access_token": access_token,
        "username": user.username,
    }


def get_decoded_token(token: str) -> dict:
    return jose.jwt.decode(
        token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )
