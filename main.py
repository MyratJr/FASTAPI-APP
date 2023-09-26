import os
from datetime import timedelta
from fastapi.security import  OAuth2PasswordRequestForm
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import User_Schema, User_Schema2
from fastapi import FastAPI, HTTPException, Depends, Response
from models import user as USER
from dotenv import load_dotenv
from jwt_.bearer import verify_password_,create_access_token,hash_password,is_logged_in

app = FastAPI()

load_dotenv('.env')

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.post("/signup",response_model=User_Schema2)
def signup(user:User_Schema):
    existing_user =db.session.query(USER).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        new_user=USER(email=user.email, username=user.username, hashed_password=hash_password(user.password))
        db.session.add(new_user)
        db.session.commit()
        return user

@app.post("/token")
def login(response: Response,form_data:OAuth2PasswordRequestForm=Depends(),is_logged:bool=Depends(is_logged_in)):
    if is_logged:
        raise HTTPException(status_code=403,detail="You are already logged in. Please log out before logging in again.")
    user =db.session.query(USER).filter_by(username=form_data.username).first()
    if verify_password_(form_data.password,user):
        access_token=create_access_token(
            data={"sub":form_data.username},expires_delta=timedelta(minutes=30,hours=5)
        )
        response.set_cookie("token", access_token, secure=True, samesite="Strict")
        return {"access_token":access_token, "token_type":"bearer"}
    else:
        raise HTTPException(status_code=400,detail="Incorrect username or password")

@app.get('/al')
def get_current_user(is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        raise HTTPException(status_code=401,detail="Any user have not logged in.")
    return {'User':is_logged}

@app.post("/logout")
def logout(response: Response,is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        raise HTTPException(status_code=401,detail="Any user have not logged in.")
    response.delete_cookie("token")
    return {'detail':"You have been logged out successfully."}