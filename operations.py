from sqlalchemy.orm import Session
from models import Student
from schemas import AddStudent,UpdateStudent


def get_students(database: Session, limit: int = None):
    query = database.query(Student)

    if limit:
        query = query.limit(limit)

    return query.all()


def get_student(database: Session, student_id: int):
    return database.query(Student).filter(Student.id == student_id).first()


def add_student(database: Session, student: AddStudent):
    new_student = Student(
        name=student.name,
        age=student.age,
        gender=student.gender,
        year=student.year
    )

    database.add(new_student)
    database.commit()
    database.refresh(new_student)

    return new_student

def update(database:Session,id:int,student:UpdateStudent):
    existing_student=database.query(Student).filter(Student.id==id).first()

    if not existing_student:
        return None
    if student.name is not None:
        existing_student.name=student.name
    if student.age is not None:
        existing_student.age=student.age
    if student.gender is not None:
        existing_student.gender=student.gender
    if student.year is not None:
        existing_student.year=student.year

    database.commit()
    database.refresh(existing_student)

    return existing_student

def delete(database:Session,id:int):
    del_student=database.query(Student).filter(Student.id==id).first()

    if not del_student:
        return None
    database.delete(del_student)
    database.commit()

    return del_student