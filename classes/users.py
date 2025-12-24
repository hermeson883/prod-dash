from classes.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, primary_key=False, index=True, nullable=False)
    username = Column(String, primary_key=False, index=True, nullable=False, unique=True)
    password = Column(String, primary_key=False, index=True, nullable=False)
