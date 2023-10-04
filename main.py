import os
from datetime import timedelta
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import User_Schema, User_Schema2, login_
from fastapi import FastAPI, Depends
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
    redis_connection.set(key, data, ex=60)
# ,response_model=User_Schema2
@app.post("/signup")
def signup(user:User_Schema,is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        existing_user =db.session.query(USER).filter_by(email=user.email).first()
        if existing_user:
            exchand(409,"Email already registered")
        else:
            cache('detail',user.email)
            get_dashboard_report(user.username,user.email,randint(1000,9999))
            return {"detail":"We sent OTP to your gmail account, verify your account"}
            
            # print((redis_connection.get('detail')).decode("utf-8"))
            # new_user=USER(email=user.email, username=user.username, hashed_password=hash_password(user.password))
            # db.session.add(new_user)
            # db.session.commit()
            # return user
    else:
        exchand(403,"You are already logged in.")

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