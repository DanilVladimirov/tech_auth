import fastapi as fa
import fastapi.security
from core import database
from sqlalchemy import orm
from users import helpers as user_helpers

oauth2 = fa.security.OAuth2PasswordBearer(
    tokenUrl=f"/user/access-token",
)


async def get_user_from_token(
    auth_token: str = fa.Depends(oauth2), db: orm.Session = fa.Depends(database.get_db)
):
    return await user_helpers.get_current_user(auth_token, db)
