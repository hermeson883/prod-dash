from fastapi import FastAPI, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.models.get_user import LoginFormUser
from classes.database import SessionLocal
from classes.users import Users
from typing import Annotated

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
    print("recebi a requisicao")
    db = SessionLocal()
    user = db.query(Users).filter(user_login_data.username == Users.username).first()


    if not user:
        return HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Usuário inexistente"
        )

    return user