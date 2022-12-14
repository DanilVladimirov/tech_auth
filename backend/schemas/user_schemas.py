import pydantic


class LoginUser(pydantic.BaseModel):
    username: pydantic.constr(max_length=255, min_length=1)
    password: pydantic.constr(max_length=255, min_length=1)


class SignUpUser(pydantic.BaseModel):
    username: pydantic.constr(max_length=255, min_length=1)
    password: pydantic.constr(max_length=255, min_length=1)


class GetUser(pydantic.BaseModel):
    username: str

    class Config:
        orm_mode = True
