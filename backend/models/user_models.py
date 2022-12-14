import sqlalchemy as sa
from core import database


class User(database.Base):
    __tablename__ = "user"

    username: str = sa.Column(sa.String(length=255), primary_key=True, index=True)
    hash_password: str = sa.Column(sa.Text(), nullable=False)
