from pydantic import BaseModel
from typing import Optional

class AddStudent(BaseModel):
    name:str
    age:int
    gender:str
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str] =None
    age:Optional[int]=None
    gender:Optional[str]=None
    year:Optional[str]=None