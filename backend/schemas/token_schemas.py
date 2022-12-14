import pydantic
import typing as t


class TokenPayload(pydantic.BaseModel):
    sub: t.Optional[str] = None
    token_type: t.Optional[str] = None


class GetAccessToken(pydantic.BaseModel):
    token_type: str
    access_token: str
