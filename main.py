import os
from datetime import timedelta
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import User_Schema, User_Schema2, login_,otp_schema
from fastapi import FastAPI, Depends, HTTPException
from models import user as USER
from dotenv import load_dotenv
from jwt_.bearer import verify_password_,create_access_token,hash_password,is_logged_in
from jwt_.superuser import router as superuser_router
from jwt_.errexchand import exchand
import redis
from random import randint
from tasks.router import get_dashboard_report
from fastapi.responses import Response

redis_connection = redis.Redis()

app = FastAPI()

app.include_router(superuser_router)

load_dotenv('.env')

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

def cache(key, data):
    redis_connection.set(key, data, ex=300)

@app.post("/signup")
def signup(user:User_Schema,is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        existing_user =db.session.query(USER).filter_by(email=user.email).first()
        if existing_user:
            exchand(409,"Email already registered")
        else:
            OTP=randint(1000,9999)
            cache('detail',user.email)
            cache('otp',OTP)
            cache('password',user.password)
            cache('username',user.username)
            get_dashboard_report(user.username,user.email,OTP)
            return {"detail":"We sent OTP to your gmail account, verify your account"} 
    else:
        exchand(403,"You are already logged in.")
        
@app.post("/verify_account")
def verify_account(OTP:otp_schema):
    try:
        cache_otp=(redis_connection.get('otp')).decode("utf-8")
    except AttributeError:
        raise HTTPException(status_code=403,detail="OTP code time expred")
    if OTP.OTP==int(cache_otp):
        email=(redis_connection.get('detail')).decode("utf-8")
        password=(redis_connection.get('password')).decode("utf-8")
        username=(redis_connection.get('username')).decode("utf-8")
        new_user=USER(email=email, username=username, hashed_password=hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        return {"email":email,"username":username}
    exchand(401,"Incorrect OTP code")

@app.post("/token")
def login(form_data:login_,is_logged:bool=Depends(is_logged_in)):
    if is_logged:
        exchand(403,"You are already logged in. Please log out before logging in again.")
    user=db.session.query(USER).filter_by(username=form_data.username).first()
    if user is None:
        exchand(401,"Incorrect username or password")
    if verify_password_(form_data.password,user):
        access_token=create_access_token(
            data={"sub":form_data.username},expires_delta=timedelta(hours=10)
        )
        return {"access_token":access_token, "token_type":"bearer"}
    else:
        exchand(401,"Incorrect username or password")

@app.post("/logout")
def logout(is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        exchand(401,"You are not logged in.")
    exchand(200,"You have been logged out successfully.")