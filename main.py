from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_database
from schemas import AddStudent,UpdateStudent,UserCreate,UserLogin
from authentication import password_verify,create_token,get_current_user
import operations

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{"Message":"Run Successfully"}

@app.post("/register")
def register(user:UserCreate,database:Session=Depends(get_database)):
    existing_user=operations.get_user(database,user.user_name)

    if existing_user:
         raise HTTPException(status_code=400,detail="User already exists")
    operations.create_user(database,user)
    return {"Message":"User registered Successfully"}

@app.post("/login")
def login(user:UserLogin,database:Session=Depends(get_database)):
    existing_user=operations.get_user(database,user.user_name)

    if not existing_user:
        raise HTTPException(status_code=400,detail="Invalid user or password")

    if not password_verify(user.password,existing_user.password):
        raise HTTPException(status_code=401,detail="Invalid user or password")

    token=create_token(existing_user.user_name)

    return {
        "Access Token":token,
        "Token type":"Bearer"
    }

@app.get("/students")
def get_students(limit: int = None,database: Session = Depends(get_database),current_user:str=Depends(get_current_user)):
    return operations.get_students(database, limit)

@app.get("/student/{id}")
def get_student(id: int,database: Session = Depends(get_database),current_user:str=Depends(get_current_user)):
    student = operations.get_student(database, id)

    if not student:
        return {"message": "Student not found"}
    return student

@app.post("/add_student")
def add_student(student: AddStudent,database: Session = Depends(get_database),current_user:str=Depends(get_current_user)):
    return operations.add_student(database, student)

@app.put("/update{id}")
def update(student:UpdateStudent,id:int,database:Session=Depends(get_database),current_user:str=Depends(get_current_user)):
    updated_student=operations.update(database,id,student)
    if not updated_student:
        return {"message":"Student not found"}
    return updated_student

@app.delete("/delete{id}")
def delete(id:int,database:Session=Depends(get_database),current_user:str=Depends(get_current_user)):
    deleted_student=operations.delete(database,id)
    if not deleted_student:
        return {"Message":"Student not found"}
    return {"Message":"Deleted successfully","Student":deleted_student}

