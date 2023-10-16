from fastapi import APIRouter,Request
from jwt_.errexchand import exchand,return_,ugrat,ber,select_need_column,get_all_data
from models import *
from schemas import input_employe
from fastapi_sqlalchemy import db

shared_router = APIRouter()

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

@shared_router.get("/add_employe")
def add_employe_get():
    o1 = get_all_data(a4)
    o2 = get_all_data(a2)
    o3 = get_all_data(a7)
    o4 = get_all_data(a8)
    o5 = get_all_data(a3)
    o6 = select_need_column(db.session.query(a1).all())
    o7 = select_need_column(db.session.query(a5).all())
    o8 = select_need_column(db.session.query(a6).all())
    return [o1,o2,o3,o4,o5,o6,o7,o8]

@shared_router.get("/get_employes")
def get_employes():
    all_employes=db.session.query(a9).all()
    for employe in all_employes:
        temporary_knowledge=[]
        for each_end_knowlege in db.session.query(a1).all():
            if f'{employe.id}' in each_end_knowlege.employes:
                temporary_knowledge.append(each_end_knowlege.knowledge_part)
        employe.end_knowledge=temporary_knowledge
    return all_employes
