from fastapi import FastAPI, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.models.get_user import LoginFormUser
from classes.database import SessionLocal
from classes.users import Users
from typing import Annotated
from app.api.jwt_token.jwt_util import JWTUtil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(user_login_data: Annotated[LoginFormUser, Form()]):

    db = SessionLocal()
    user = db.query(Users).filter(Users.username == user_login_data.username).first()

    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Usuário inexistente"
        )

    
    jwt_helper = JWTUtil()

    encoded_data = jwt_helper.create_encode(user_login_data.username)

    return {
        "username": user.username,
        "token": encoded_data["token"],
        "expired_date": encoded_data["exp"]
    }