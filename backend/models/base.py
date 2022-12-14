from core import database
import sqlalchemy as sa
import sqlalchemy.dialects
import uuid


class BaseModel(database.Base):
    __abstract__ = True

    id: uuid.UUID = sa.Column(
        sa.dialects.postgresql.UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=sa.text("gen_random_uuid()"),
    )
