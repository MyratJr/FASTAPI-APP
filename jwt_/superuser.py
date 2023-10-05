from fastapi import APIRouter,HTTPException,Response,Depends
from schemas import users,change_user_info
from .bearer import is_admin_superuser,hash_password
from models import user as USER
from fastapi_sqlalchemy import db
from .errexchand import exchand

router=APIRouter(prefix='/admin')

@router.get("/users",response_model=list[users])
def get_all_users(is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        All_Users=db.session.query(USER).all()
        return All_Users
    exchand(403,"Only available for superusers")

@router.delete('/delete/{id}')
def deleteuser(id:int,is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        if not db.session.query(USER).filter_by(id=id).first():
            exchand(404,"User not found")
        update_user =db.session.query(USER).filter_by(id=id).first()
        db.session.delete(update_user)
        db.session.commit()
        return Response(status_code=204)
    exchand(403,"Only available for superusers")

@router.post("/Update_User/{id}",response_model=users)
def update_user(id:int,will_update_user_scema:change_user_info,is_admin_superuser1:bool=Depends(is_admin_superuser)):
    if is_admin_superuser1:
        if not db.session.query(USER).filter_by(id=id).first():
            raise HTTPException(status_code=404, detail="User not found")
        update_user =db.session.query(USER).filter_by(id=id).first()
        update_user.email=will_update_user_scema.email
        update_user.username=will_update_user_scema.username
        update_user.hashed_password=hash_password(will_update_user_scema.password)
        update_user.is_active=will_update_user_scema.is_active
        update_user.is_superuser=will_update_user_scema.is_superuser
        update_user.is_verified=will_update_user_scema.is_verified
        db.session.commit()
        return update_user
    exchand(403,"Only available for superusers")