from fastapi import FastAPI
from users.api import router as user_api


app = FastAPI()

app.include_router(user_api, tags=["user"], prefix="/user")


@app.get("/")
async def root():
    return {"message": "Hello World"}
