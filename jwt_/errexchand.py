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
        end_knowledge1=db.session.query(c).filter_by(id=i).first()
        q1=end_knowledge1.employes+[a.id]
        end_knowledge1.employes=q1
        d.append(i)
        db.session.commit()

def return_(a,b):
    return db.session.query(a).filter_by(id=b).first()
