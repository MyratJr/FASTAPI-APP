from pydantic import BaseModel
import datetime

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