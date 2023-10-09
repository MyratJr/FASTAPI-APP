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