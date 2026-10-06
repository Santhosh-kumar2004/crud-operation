from sqlalchemy import Column,String,Integer
from database import Base

class Student(Base):
    __tablename__='Students'

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String,index=True)
    age=Column(Integer,index=True)
    gender=Column(String,index=True)
    year=Column(String,index=True)


class User(Base):
    __tablename__='Users'

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    user_name=Column(String,unique=True,index=True)
    password=Column(String,index=True)