import os
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI
from dotenv import load_dotenv
from jwt_.superuser import router as superuser_router
from jwt_.users import router as users_router
import redis
from fastapi_swagger2 import FastAPISwagger2
from employe.employe import shared_router

app = FastAPI()

FastAPISwagger2(app)

def redis_connection():
    return redis.Redis()

app.include_router(superuser_router)
app.include_router(users_router)
app.include_router(shared_router)

load_dotenv('.env')

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])