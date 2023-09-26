import jwt
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from config import*
from fastapi import Request

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def hash_password(password):
    return password_context.hash(password)

def verify_password_(password,user):
    try:
        password_check=password_context.verify(password, user.hashed_password)
        return password_check
    except:
        return False

def create_access_token(data:dict,expires_delta:timedelta):
    to_encode=data.copy()
    expire=datetime.utcnow()+expires_delta
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def get_username_from_token(token):
    decoded_token = jwt.decode(token,JWT_SECRET_KEY, ALGORITHM)
    username = decoded_token["sub"]
    return username

def is_logged_in(request:Request):
    if request.cookies.get('token'):
        return(get_username_from_token(request.cookies.get('token')))
    else:
        return False