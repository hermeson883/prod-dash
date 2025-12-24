from app.models.get_user import LoginFormUser

class Users(LoginFormUser):
    id: int
    name: str