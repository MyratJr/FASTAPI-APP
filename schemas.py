from pydantic import BaseModel
import datetime
from sqlalchemy import Boolean

class User_Schema2(BaseModel):
    email:str
    username: str

    class Config:
        orm_mode = True

class User_Schema(User_Schema2):
    password: str

    class Config:
        orm_mode = True

class login_(BaseModel):
    username:str
    password:str

class sub_users(BaseModel):
    email: str
    username: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        orm_mode = True
        arbitrary_types_allowed=True

class users(sub_users):
    id: int
    registered_at: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed=True
