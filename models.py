from sqlalchemy import Column,String,Integer
from database import Base

class Student(Base):
    __tablename__='Students'

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String,index=True)
    age=Column(Integer,index=True)
    gender=Column(String,index=True)
    year=Column(String,index=True)