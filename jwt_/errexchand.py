from fastapi_sqlalchemy import db
from fastapi import HTTPException
import main
from email_validator import validate_email
from models import a10,a11,a12,a1,a5,a6

def exchand(status_c, detail_c):
    raise HTTPException(status_c ,detail_c)

def cache(key, data):
    main.redis_connection().set(key, data, ex=300)

def ceckmail(user):
    try:
        validate_email(user.email)
    except ValueError:
        raise HTTPException(status_code=400,detail="Invalid email address")

def return_(a,b):
    return db.session.query(a).filter_by(id=b).first()

def get_all_data(table):
    return db.session.query(table).all()

def setMtM(base,MtM,e_id):
    for i in MtM:
        if base==a10:
            set=base(employe_id=e_id,end_knowledge=i)
        elif base==a11:
            set=base(employe_id=e_id,vocational_training=i)
        elif base==a12:
            set=base(employe_id=e_id,professional_education=i)
        db.session.add(set)
    db.session.commit()

def addTolist(a1,a5,a6,employe_schema,a,b,c):
    for i in db.session.query(a1).all():
        if i.id in employe_schema.end_knowledge:
            a.append(i.knowledge_part)
    for i in db.session.query(a5).all():
        if i.id in employe_schema.vocational_training:
            b.append(i.vocational_training)
    for i in db.session.query(a6).all():
        if i.id in employe_schema.professional_education:
            c.append(i.professional_education)

def addTolist_2(a1,a5,a6,a,b,c):
    for i in db.session.query(a1).all():
        if i.id in a:
            a.append(i.knowledge_part)
            a.remove(i.id)
    for i in db.session.query(a5).all():
        if i.id in b:
            b.append(i.vocational_training)
            a.remove(i.id)
    for i in db.session.query(a6).all():
        if i.id in c:
            c.append(i.professional_education)
            a.remove(i.id)

def get_list_rows(all_employes):
    for employe in all_employes:
        temporary_knowledge=[]
        for each_end_knowlege in db.session.query(a10).all():
            if employe.id==each_end_knowlege.employe_id:
                temporary_knowledge.append(db.session.query(a1).filter_by(id=each_end_knowlege.end_knowledge).first().knowledge_part)
        employe.end_knowledge=temporary_knowledge
        temporary_vocational_training=[]
        for each_vocational_training in db.session.query(a11).all():
            if employe.id==each_vocational_training.employe_id:
                temporary_vocational_training.append(db.session.query(a5).filter_by(id=each_vocational_training.vocational_training).first().vocational_training)
        employe.vocational_training=temporary_vocational_training
        temporary_professional_education=[]
        for each_professional_education in db.session.query(a12).all():
            if employe.id==each_professional_education.employe_id:
                temporary_professional_education.append(db.session.query(a6).filter_by(id=each_professional_education.professional_education).first().professional_education)
        employe.professional_education=temporary_professional_education