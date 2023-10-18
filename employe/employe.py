from fastapi import APIRouter,Request
from jwt_.errexchand import exchand,return_,ugrat,ber,select_need_column,get_all_data,get_list_rows,salam
from models import *
from schemas import input_employe,salammyrat
from fastapi_sqlalchemy import db
    # for j in db.session.query(a5).all():
    #     if f'{employe.id}' in j.employes and j.id not in update_form.vocational_training:
    #         j.employes.remove(f'{employe.id}')
    #     elif f'{employe.id}' not in j.employes and j.id in update_form.vocational_training:
    #         j.employes.append(f'{employe.id}')
    #     db.session.commit()
    # for j in db.session.query(a6).all():
    #     if f'{employe.id}' in j.employes and j.id not in update_form.professional_education:
    #         j.employes.remove(f'{employe.id}')
    #     elif f'{employe.id}' not in j.employes and j.id in update_form.professional_education:
    #         j.employes.append(f'{employe.id}')
    #         db.session.commit()
    # db.session.commit()
shared_router = APIRouter()

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
    salam(employe)
    return employe

# @shared_router.put("/update_employe/{id}")
# def update_employe(id:int,update_form:update_employe):
#     employe=db.session.get(a9,id)
#     if employe is None:
#         exchand(404,'Employe not found')
#     employe.name_surname=update_form.name_surname
#     employe.nation=update_form.nation
#     employe.age=update_form.age
#     employe.sex=update_form.sex
#     employe.new_degree=update_form.new_degree
#     employe.knowledge=update_form.knowledge
#     for j in db.session.query(a1).all():
#         if f'{employe.id}' in j.employes and j.id not in update_form.end_knowledge:
#             j.employes.remove(f'{employe.id}')
#             j.employes=j.employes
#             print(j.employes)
#         elif f'{employe.id}' not in j.employes and j.id in update_form.end_knowledge:
#             j.employes.append(f'{employe.id}')
#             j.employes=j.employes
#             print(j.employes)
#         db.session.commit()
#     return {"detail":f'{update_form.id} successfully updated!!!'}