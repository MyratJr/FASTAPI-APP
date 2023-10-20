from fastapi_sqlalchemy import db
from fastapi import HTTPException
import main
from email_validator import validate_email
from models import a10,a11,a12

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