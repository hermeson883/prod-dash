from pydantic import BaseModel

class LoginFormUser(BaseModel):
    username: str
    password: str