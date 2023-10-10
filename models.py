from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey,Table
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

class a1(Base):
    __tablename__='employe_end_knowledge'
    id = Column(Integer, primary_key=True)
    knowledge_part=Column(String,nullable=False)

class a2(Base):
    __tablename__='employe_age_between'
    id = Column(Integer, primary_key=True)
    age_between=Column(String,nullable=False)

class a3(Base):
    __tablename__='employe_knowledge'
    id = Column(Integer, primary_key=True)
    knowledge=Column(String,nullable=False)

class a4(Base):
    __tablename__='employe_nation'
    id = Column(Integer, primary_key=True)
    nation=Column(String,nullable=False)

class a5(Base):
    __tablename__='employe_vocational_training'
    id = Column(Integer, primary_key=True)
    vocational_training=Column(String,nullable=False)

class a6(Base):
    __tablename__='employe_professional_education'
    id = Column(Integer, primary_key=True)
    professional_education=Column(String,nullable=False)

class a7(Base):
    __tablename__='employe_sex'
    id = Column(Integer, primary_key=True)
    sex=Column(String,nullable=False)

class a8(Base):
    __tablename__='employe_new_degree'
    id = Column(Integer, primary_key=True)
    degree=Column(String,nullable=False)

class a9(Base):
    __tablename__='employe'
    id = Column(Integer, primary_key=True)
    name_surname=Column(String,nullable=False)
    nation=Column(ForeignKey("employe_nation.id"), nullable=False)
    age=Column(ForeignKey("employe_age_between.id"), nullable=False)
    sex=Column(ForeignKey("employe_sex.id"), nullable=False)
    new_degree=Column(ForeignKey("employe_new_degree.id"), nullable=False)
    end_knowledge=Column(ForeignKey("employe_end_knowledge.id"), nullable=False)
    knowledge=Column(ForeignKey("employe_knowledge.id"), nullable=False)
    vocational_training=Column(ForeignKey("employe_vocational_training.id"), nullable=False)
    professional_education=Column(ForeignKey("employe_professional_education.id"), nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    roles = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    users = relationship("User", back_populates="roles")