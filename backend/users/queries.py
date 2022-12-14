from sqlalchemy import orm
from models import user_models


def get_user(username: str, db: orm.Session) -> user_models.User:
    return (
        db.query(user_models.User)
        .where(user_models.User.username == username)
        .with_entities(user_models.User.username, user_models.User.hash_password)
        .one_or_none()
    )
