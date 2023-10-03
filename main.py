import os
from datetime import timedelta
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import User_Schema, User_Schema2, login_, users, sub_users
from fastapi import FastAPI, HTTPException, Depends, Response, Request
from models import user as USER
from dotenv import load_dotenv
from jwt_.bearer import verify_password_,create_access_token,hash_password,is_logged_in, is_admin_superuser
from tasks.router import router

app = FastAPI()

app.include_router(router)

load_dotenv('.env')

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.post("/signup",response_model=User_Schema2)
def signup(user:User_Schema,is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        existing_user =db.session.query(USER).filter_by(email=user.email).first()
        if existing_user:
            raise HTTPException(status_code=409, detail="Email already registered")
        else:
            new_user=USER(email=user.email, username=user.username, hashed_password=hash_password(user.password))
            db.session.add(new_user)
            db.session.commit()
            return user
    else:
        raise HTTPException(status_code=403, detail="User is already logged in.")
    
@app.get("/users",response_model=list[users])
def get_all_users(is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        All_Users=db.session.query(USER).all()
        return All_Users
    raise HTTPException(status_code=403, detail="Only available for superusers")

@app.delete('/delete/{id}')
def deleteuser(id:int,is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        if not db.session.query(USER).filter_by(id=id).first():
            raise HTTPException(status_code=404, detail="User not found")
        update_user =db.session.query(USER).filter_by(id=id).first()
        db.session.delete(update_user)
        db.session.commit()
        return Response(status_code=204)
    raise HTTPException(status_code=403, detail="Only available for superusers")

@app.post("/Update_User/{id}",response_model=users)
def update_user(id:int,will_update_user_scema:sub_users,is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        if not db.session.query(USER).filter_by(id=id).first():
            raise HTTPException(status_code=404, detail="User not found")
        update_user =db.session.query(USER).filter_by(id=id).first()
        update_user.email=will_update_user_scema.email
        update_user.username=will_update_user_scema.username
        update_user.is_active=will_update_user_scema.is_active
        update_user.is_superuser=will_update_user_scema.is_superuser
        update_user.is_verified=will_update_user_scema.is_verified
        db.session.commit()
        return update_user
    raise HTTPException(status_code=403, detail="Only available for superusers")

@app.post("/token")
def login(form_data:login_,is_logged:bool=Depends(is_logged_in)):
    if is_logged:
        raise HTTPException(status_code=403,detail="You are already logged in. Please log out before logging in again.")
    user=db.session.query(USER).filter_by(username=form_data.username).first()
    if user is None:
        raise HTTPException(status_code=401,detail="Incorrect username or password")
    if verify_password_(form_data.password,user):
        access_token=create_access_token(
            data={"sub":form_data.username},expires_delta=timedelta(hours=10)
        )
        return {"access_token":access_token, "token_type":"bearer"}
    else:
        raise HTTPException(status_code=401,detail="Incorrect username or password")

@app.post("/logout")
def logout(is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        raise HTTPException(status_code=401,detail="Any user have not logged in.")
    return {'detail':"You have been logged out successfully."}