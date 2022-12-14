import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.ext.declarative
import sqlalchemy
import traceback
from settings import settings

DB_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = sqlalchemy.create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = sa.orm.sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = sa.ext.declarative.declarative_base()


def get_db():
    """Get db Session"""

    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
    finally:
        db.close()
