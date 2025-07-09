from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, le=10.0, description="CGPA must be between 0.0 and 10.0", default=7.0)
    
new_student = {'name': 'Rajan', 'email': 'abc@gmail.com'}

student = Student(**new_student)

print(student)
print(type(student.age))