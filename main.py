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

app = FastAPI()

app.include_router(superuser_router)

load_dotenv('.env')

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.post("/signup",response_model=User_Schema2)
def signup(user:User_Schema,is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        existing_user =db.session.query(USER).filter_by(email=user.email).first()
        if existing_user:
            exchand(409,"Email already registered")
        else:
            new_user=USER(email=user.email, username=user.username, hashed_password=hash_password(user.password))
            db.session.add(new_user)
            db.session.commit()
            return user
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