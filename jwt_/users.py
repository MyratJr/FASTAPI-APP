from datetime import timedelta
from schemas import User_Schema,login_,otp_schema
from fastapi import Depends, HTTPException,APIRouter
from models import user as USER
from jwt_.bearer import verify_password_,create_access_token,hash_password,is_logged_in
from jwt_.errexchand import exchand, cache
from random import randint
from tasks.router import get_dashboard_report
from fastapi_sqlalchemy import db
import main

router=APIRouter(prefix='/user')

@router.post("/signup")
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
        
@router.post("/verify_account")
def verify_account(OTP:otp_schema):
    try:
        cache_otp=(main.redis_connection.get('otp')).decode("utf-8")
    except AttributeError:
        raise HTTPException(status_code=403,detail="OTP code time expred")
    if OTP.OTP==int(cache_otp):
        email=(main.redis_connection.get('detail')).decode("utf-8")
        password=(main.redis_connection.get('password')).decode("utf-8")
        username=(main.redis_connection.get('username')).decode("utf-8")
        new_user=USER(email=email, username=username, hashed_password=hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        return {"email":email,"username":username}
    exchand(401,"Incorrect OTP code")

@router.post("/token")
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

@router.post("/logout")
def logout(is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        exchand(401,"You are not logged in.")
    exchand(200,"You have been logged out successfully.")