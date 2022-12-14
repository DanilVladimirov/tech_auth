import fastapi as fa
import pydantic
import jose.jwt
import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.exc
from security import token
from schemas import token_schemas
from models import user_models
from psycopg2 import errorcodes


async def get_current_user(auth_token: str, db: sa.orm.Session) -> user_models.User:
    try:
        payload = token.get_decoded_token(auth_token)
        token_data = token_schemas.TokenPayload(**payload)

        return (
            db.query(user_models.User)
            .filter(user_models.User.username == token_data.sub)
            .one()
        )
    except (jose.jwt.JWTError, pydantic.ValidationError, sa.exc.NoResultFound):
        raise fa.HTTPException(
            status_code=401,
            detail="Auth token is not valid. Try login again.",
        )


def create_user(username: str, password: str, db: sa.orm.Session) -> user_models.User:
    try:
        new_user = user_models.User(username=username, hash_password=token.get_password_hash(password))

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except sa.exc.DBAPIError as ex:
        if ex.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            raise fa.HTTPException(status_code=400, detail="this username is already taken")
        else:
            raise
