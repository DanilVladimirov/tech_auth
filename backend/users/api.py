import fastapi as fa
import response_codes
from users import helpers
from fastapi import APIRouter
from schemas import user_schemas
from schemas import token_schemas
from security import token
from core import database
from sqlalchemy import orm
from users import queries

router = APIRouter()


@router.post(
    "/sign-up",
    response_model=user_schemas.GetUser,
    responses={
        **response_codes.RESPONSE_400,
        **response_codes.RESPONSE_404,
    },
    summary="Sign up.",
)
async def sign_up_user(
    request: user_schemas.SignUpUser, db: orm.Session = fa.Depends(database.get_db)
):
    return helpers.create_user(request.username, request.password, db)


@router.post(
    "/get-access-token",
    response_model=token_schemas.GetAccessToken,
    responses={
        **response_codes.RESPONSE_400,
        **response_codes.RESPONSE_404,
    },
    summary="Get access token.",
)
async def get_access_token(
    request: user_schemas.LoginUser, db: orm.Session = fa.Depends(database.get_db)
):
    user = queries.get_user(request.username, db)

    if user is None:
        raise fa.HTTPException(404, detail="user not found")

    if not token.verify_password(request.password, user.hash_password):
        raise fa.HTTPException(400, detail="username or password is not valid")

    return await token.set_and_get_tokens(user)
