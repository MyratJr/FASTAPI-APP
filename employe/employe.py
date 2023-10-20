from fastapi import APIRouter
from jwt_.errexchand import exchand,return_,get_all_data,setMtM,addTolist
from models import *
from schemas import input_employe
from fastapi_sqlalchemy import db

shared_router = APIRouter()

@shared_router.get("/add_employe")
def add_employe_get():
    o1 = get_all_data(a4)
    o2 = get_all_data(a2)
    o3 = get_all_data(a7)
    o4 = get_all_data(a8)
    o5 = get_all_data(a3)
    o6 = get_all_data(a1)
    o7 = get_all_data(a5)
    o8 = get_all_data(a6)
    return [o1,o2,o3,o4,o5,o6,o7,o8]

@shared_router.post("/add_employe")
def add_employe(employe_schema:input_employe):
    check_user=db.session.query(a9).filter_by(id=employe_schema.id).first()
    if check_user is not None:
        exchand(400,"Employe already exists")
    new_employe=a9(id=employe_schema.id,
                    name_surname=employe_schema.name_surname,
                    nation=employe_schema.nation,
                    age=employe_schema.age,
                    sex=employe_schema.sex,
                    new_degree=employe_schema.new_degree,
                    knowledge=employe_schema.knowledge)
    db.session.add(new_employe)
    db.session.commit()
    setMtM(a10,employe_schema.end_knowledge,employe_schema.id)
    setMtM(a11,employe_schema.vocational_training,employe_schema.id)
    setMtM(a12,employe_schema.professional_education,employe_schema.id)
    a=[];b=[];c=[]
    addTolist(a1,a5,a6,employe_schema,a,b,c)
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


@shared_router.get("/get_employes")
def get_employes():
    all_employes=db.session.query(a9).all()
    get_list_rows(all_employes)
    return all_employes

@shared_router.get('/get_employe/{id}')
def get_employe(id:int):
    employe=db.session.get(a9,id)
    if employe is None:
        exchand(404,'Employe not found')
    return employe