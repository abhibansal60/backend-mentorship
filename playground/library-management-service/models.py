from pydantic import BaseModel, Field, BeforeValidator
from datetime import datetime
from datetime import timedelta
from typing import List, Optional
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]

class Book(BaseModel):
    name: str
    author: str
    issueDate: datetime = datetime.today()
    issuedUntilDate: datetime = datetime.today() + timedelta(days=30)

class StudentModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    fullName: str = Field()
    ofClass: int = Field()
    books: List[Book]

class UpdateStudentModel(BaseModel):
    fullName: Optional[str] = None
    ofClass: Optional[int] = None
    books: Optional[List[Book]] = []

class StudentCollection(BaseModel):
    students: List[StudentModel]