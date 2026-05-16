from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional, List

class CityBase(BaseModel):
    name: str

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    salary: float

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


class StudentBase(BaseModel):
    index_number: str = Field(pattern=r'^BB\d{6}$')
    firstname: str
    lastname: str
    date_of_birth: date
    status: str
    phone_number: str = Field(pattern=r'^\+ \d{3} \d{2} \d{3} \d{3}$')
    email: EmailStr
    city_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    city: Optional[City] = None

    class Config:
        from_attributes = True
