from pydantic import BaseModel
import datetime
from typing import List

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

class change_user_info(BaseModel):
    email: str
    username: str
    password:str
    is_active: bool
    is_superuser: bool
    is_verified: bool

class users(sub_users):
    id: int
    registered_at: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed=True

class otp_schema(BaseModel):
    OTP:int

class input_employe(BaseModel):
    id:int
    name_surname:str
    nation:int
    age:int
    sex:int
    new_degree:int
    knowledge:int

class update_employe(input_employe):
    end_knowledge:List[int]
    vocational_training:List[int]
    professional_education:List[int]