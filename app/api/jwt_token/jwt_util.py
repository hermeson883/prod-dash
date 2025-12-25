import os
import jwt
from app.models.get_user import LoginFormUser
from datetime import datetime, timedelta
from dotenv import load_dotenv
import json

load_dotenv()

class JWTUtil():
    
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        self.the_algorithm = os.getenv("THE_ALGORITHM")
        self.time_limit = datetime.utcnow() + timedelta(
            minutes= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        )

    def create_encode(self, username: str):
        token = jwt.encode(
            {
                "user": username,
                "exp": self.time_limit
            },
            self.secret_key,
            self.the_algorithm
        )


        return {
            "token": token,
            "exp": self.time_limit.isoformat()
        }