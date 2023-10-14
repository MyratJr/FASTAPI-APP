from sqlalchemy import select
from fastapi_sqlalchemy import db
from fastapi import HTTPException
import main
from email_validator import validate_email

def exchand(status_c, detail_c):
    raise HTTPException(status_c ,detail_c)

def cache(key, data):
    main.redis_connection().set(key, data, ex=300)

def ceckmail(user):
    try:
        validate_email(user.email)
    except ValueError:
        raise HTTPException(status_code=400,detail="Invalid email address")
    
def for_list(a,b,c,d):
    if b=='end_knowledge':
        m=a.end_knowledge
    elif b=='vocational_training':
        m=a.vocational_training
    elif b=='professional_education':
        m=a.professional_education
    for i in m:
        print(':::::::::::',i,type(i))
        end_knowledge1=db.session.query(c).filter_by(id=i).first()
        q1=end_knowledge1.employes+[a.id]
        end_knowledge1.employes=q1
        d.append(i)
        db.session.commit()

def ber(z,a,b,c,a1,b1,c1,a2,b2,c2):
    for_list(z,a,b,c)
    for_list(z,a1,b1,c1)
    for_list(z,a2,b2,c2)

def return_(a,b):
    return db.session.query(a).filter_by(id=b).first()

def categories_for_response(a,z,b):
    for i in range(0,len(a)):
        o1=db.session.query(z).filter_by(id=a[i]).first()
        a.remove(a[i])
        if b=="knowledge_part":
            a.insert(i,o1.knowledge_part)
        elif b=="vocational_training":
            a.insert(i,o1.vocational_training)
        if b=="professional_education":
            a.insert(i,o1.professional_education)

def ugrat(a,b,c,a1,b1,c1,a2,b2,c2):
    categories_for_response(a,b,c)
    categories_for_response(a1,b1,c1)
    categories_for_response(a2,b2,c2)

def select_need_column(table_name):
    cleaned_data = [{key: value for key, value in row.__dict__.items() if key != 'employes'} for row in table_name]
    return cleaned_data

def get_all_data(table):
    return db.session.query(table).all()