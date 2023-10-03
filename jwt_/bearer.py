from fastapi_sqlalchemy import db
import jwt
from datetime import datetime,timedelta
from passlib.context import CryptContext
from config import*
from models import user as USER
from fastapi import Request,HTTPException,Depends

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    return "Bearer "+encoded_jwt

def get_username_from_token(token):
    try:
        decoded_token = jwt.decode(token,JWT_SECRET_KEY, ALGORITHM)
        username = decoded_token["sub"]
        return username
    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")

def is_logged_in(request:Request):
    authorization = request.headers.get("Authorization")
    if authorization:
        if authorization.startswith("Bearer "):
            token = authorization.split("Bearer ")[1]
            return(get_username_from_token(token))
        else:
            raise HTTPException(status_code=401,detail="Unknown token")
    else:
        return False
    
def is_admin_superuser(result:bool=Depends(is_logged_in)):
    if result is False:
        raise HTTPException(status_code=401,detail="Any user have not logged in.")
    update_user =db.session.query(USER).filter_by(username=result).first()
    return update_user.is_superuser is True