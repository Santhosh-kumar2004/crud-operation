from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, get_database
from schemas import AddStudent,UpdateStudent
import operations

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/students")
def get_students(limit: int = None,database: Session = Depends(get_database)):
    return operations.get_students(database, limit)

@app.get("/student/{id}")
def get_student(id: int,database: Session = Depends(get_database)):
    student = operations.get_student(database, id)

    if not student:
        return {"message": "Student not found"}
    return student

@app.post("/add_student")
def add_student(student: AddStudent,database: Session = Depends(get_database)):
    return operations.add_student(database, student)

@app.put("/update{id}")
def update(student:UpdateStudent,id:int,database:Session=Depends(get_database)):
    updated_student=operations.update(database,id,student)
    if not updated_student:
        return {"message":"Student not found"}
    return updated_student

@app.delete("/delete{id}")
def delete(id:int,database:Session=Depends(get_database)):
    deleted_student=operations.delete(database,id)
    if not deleted_student:
        return {"Message":"Student not found"}
    return {"Message":"Deleted successfully","Student":deleted_student}

