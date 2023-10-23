from fastapi import APIRouter
from jwt_.errexchand import *
from models import *
from schemas import input_employe,input_employe_for_id
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
def add_employe(employe_schema:input_employe_for_id):
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

@shared_router.put('/update_employe/{id}')
def update_employe(upgrade_employe_schema:input_employe,id:int):
    check_user=db.session.query(a9).filter_by(id=id).first()
    if check_user is None:
        exchand(400,"Employe not exists")
    for attr,value in upgrade_employe_schema:
        setattr(check_user,attr,value)
    delete_ManyToManyRows(a10,id,upgrade_employe_schema.end_knowledge,'end_knowledge')
    update_ManyToManyTables(upgrade_employe_schema.end_knowledge,a10,id,'end_knowledge',a1)
    delete_ManyToManyRows(a11,id,upgrade_employe_schema.vocational_training,'vocational_training')
    update_ManyToManyTables(upgrade_employe_schema.vocational_training,a11,id,'vocational_training',a5)
    delete_ManyToManyRows(a12,id,upgrade_employe_schema.professional_education,'professional_education')
    update_ManyToManyTables(upgrade_employe_schema.professional_education,a12,id,'professional_education',a6)
    db.session.commit()
    return upgrade_employe_schema

@shared_router.delete('/delete_employe/{id}')
def delete_employe(id:int):
    employe = db.session.query(a9).filter_by(id=id).first()
    if employe is None:
        exchand(404,"Employe not found")
    db.session.delete(employe)
    delete_MtM(a10,id)
    delete_MtM(a11,id)
    delete_MtM(a12,id)
    db.session.commit()
    return f'{employe.name_surname} deleted'

@shared_router.get('/all_employe_age_between')
def get_all_employe_age_between():
    age_betweens=db.session.query(a2).all()
    return age_betweens

@shared_router.get('/all_employe_knowledge')
def get_all_employe_knowledge():
    employe_knowledges=db.session.query(a3).all()
    return employe_knowledges

@shared_router.get('/all_employe_nation')
def get_all_employe_nation():
    employe_nation=db.session.query(a4).all()
    return employe_nation

@shared_router.get('/all_employe_vocational_training')
def get_all_employe_vocational_training():
    employe_vocational_training=db.session.query(a5).all()
    return employe_vocational_training

@shared_router.get('/all_employe_professional_education')
def get_all_employe_professional_education():
    employe_professional_education=db.session.query(a6).all()
    return employe_professional_education

@shared_router.get('/all_employe_sex')
def get_all_employe_sex():
    employe_sex=db.session.query(a7).all()
    return employe_sex

@shared_router.get('/all_employe_new_degree')
def get_all_employe_new_degree():
    employe_new_degree=db.session.query(a8).all()
    return employe_new_degree