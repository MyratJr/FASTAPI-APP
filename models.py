from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from datetime import datetime
import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM
import psycopg2

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

# --------------------------------------------------------------------------------
class employe_age_between_enum(enum.Enum):
    a='18 ýaşa çenli'
    b='18-20 ýaş'
    c='21-22 ýaş'
    d='23-24 ýaş'
    e='25-29 ýaş'
    f='30-34 ýaş'
    g='35-39 ýaş'
    h='40-49 ýaş'
# --------------------------------------------------------------------------------
class employe_knowledge_enum(enum.Enum):
    a="ýokary okuw mekdebinden soňky hünäri"
    b="ýokary hünär"
    c="orta hünär"
    d="başlangyç hünär"
    e="umumy orta"
    f="esasy orta"
# --------------------------------------------------------------------------------
class employe_nation_enum(enum.Enum):
    a="türkmen"
    b="özbek"
    c="rus"
    d="buluj"
    e="azerbaýjan"
    f="gazak"
    g="ermeni"
    h="tatar"
    i="beýleki milletler"
# --------------------------------------------------------------------------------
class employe_sex_enum(enum.Enum):
    a="erkek"
    b="zenan"
    c="başga"
# --------------------------------------------------------------------------------
class employe_new_degree_enum(enum.Enum):
    a="Ýolbaşçy"
    b="Hünärmen"
    c="Beýleki gullukçylar"
    d="Işçiler"
# --------------------------------------------------------------------------------
class a5(Base):
    __tablename__='employe_vocational_training'
    id = Column(Integer, primary_key=True)
    vocational_training=Column(String,nullable=False)

class a6(Base):
    __tablename__='employe_professional_education'
    id = Column(Integer, primary_key=True)
    professional_education=Column(String,nullable=False)

class a1(Base):
    __tablename__='employe_end_knowledge'
    id = Column(Integer, primary_key=True)
    knowledge_part=Column(String,nullable=False)
# --------------------------------------------------------------------------------
class a9(Base):
    __tablename__='employe'
    id = Column(Integer, primary_key=True)
    name_surname=Column(String,nullable=False)
    nation=Column(ENUM(employe_nation_enum))
    age=Column(ENUM(employe_age_between_enum))
    sex=Column(ENUM(employe_sex_enum))
    new_degree=Column(ENUM(employe_new_degree_enum))
    knowledge=Column(ENUM(employe_knowledge_enum))
# --------------------------------------------------------------------------------
# MANYTOMANYRELATIONSHIP
class a10(Base):
    __tablename__='ManyToManyEmployeEnd_knowledge'
    id=Column(Integer, primary_key=True)
    employe_id=Column(Integer)
    end_knowledge=Column(Integer)

class a11(Base):
    __tablename__='ManyToManyEmploye_vocational_training'
    id=Column(Integer, primary_key=True)
    employe_id=Column(Integer)
    vocational_training=Column(Integer)

class a12(Base):
    __tablename__='ManyToManyEmploye_professional_education'
    id=Column(Integer, primary_key=True)
    employe_id=Column(Integer)
    professional_education=Column(Integer)
# --------------------------------------------------------------------------------