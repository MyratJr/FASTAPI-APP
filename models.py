from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

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

class BookAuthor(Base):
    __tablename__ = 'book_authors'
    book_id = Column(ForeignKey('books.id'), primary_key=True)
    author_id = Column(ForeignKey('authors.id'), primary_key=True)
    blurb = Column(String, nullable=False)
    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")

    # proxies
    author_name = association_proxy(target_collection='author', attr='name')
    book_title = association_proxy(target_collection='book', attr='title')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship("BookAuthor", back_populates="book")

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("BookAuthor", back_populates="author")