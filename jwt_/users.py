from datetime import timedelta
from schemas import User_Schema,login_,otp_schema,input_employe
from fastapi import Depends, HTTPException,APIRouter
from models import user as USER
from models import *
from .bearer import verify_password_,create_access_token,hash_password,is_logged_in
from .errexchand import exchand, cache,ceckmail,for_list,return_,categories_for_response,ugrat,ber
from random import randint
from tasks.router import get_dashboard_report
from fastapi_sqlalchemy import db
import main

router=APIRouter(prefix='/user')

@router.post("/signup")
def signup(user:User_Schema,is_logged:bool=Depends(is_logged_in)):
    ceckmail(user)
    if is_logged is False:
        existing_user =db.session.query(USER).filter_by(email=user.email).first()
        if existing_user:
            exchand(409,"Email already registered")
        else:
            OTP=randint(100000,999999)
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
        cache_otp=(main.redis_connection().get('otp')).decode("utf-8")
    except AttributeError:
        raise HTTPException(status_code=403,detail="No OTP code or OTP code time expired")
    if OTP.OTP==int(cache_otp):
        main.redis_connection().delete('otp')
        email=(main.redis_connection().get('detail')).decode("utf-8")
        password=(main.redis_connection().get('password')).decode("utf-8")
        username=(main.redis_connection().get('username')).decode("utf-8")
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

@router.post("/add_employe")
def add_employe(employe_schema:input_employe):
    new_employe=a9(id=employe_schema.id,
                    name_surname=employe_schema.name_surname,
                    nation=employe_schema.nation,
                    age=employe_schema.age,
                    sex=employe_schema.sex,
                    new_degree=employe_schema.new_degree,
                    knowledge=employe_schema.knowledge)
    db.session.add(new_employe)
    db.session.commit()
    a=[];b=[];c=[]
    ber(employe_schema,
        'end_knowledge',a1,a,
        'vocational_training',a5,b,
        'professional_education',a6,c)
    ugrat(a,a1,"knowledge_part",
            b,a5,"vocational_training",
            c,a6,"professional_education")
    return {"id":employe_schema.id,
            "name_surname":employe_schema.name_surname,
            "natio":return_(a4,employe_schema.nation).nation,
            "age":return_(a2,employe_schema.age).age_between,
            "sex":return_(a7,employe_schema.sex).sex,
            "new_degree":return_(a8,employe_schema.new_degree).degree,
            "knowledge":return_(a3,employe_schema.knowledge).knowledge,
            "end_knowledge":a,
            "vocational_training":b,
            "professional_education":c}

@router.get("/add_employe")
def add_employe_get():
    o1 = db.session.query(a4).all()
    o2 = db.session.query(a2).all()
    o3 = db.session.query(a7).all()
    o4 = db.session.query(a8).all()
    o5 = db.session.query(a3).all()
    o6 = db.session.query(a1).all()
    o7 = db.session.query(a5).all()
    o7 = db.session.query(a6).all()