from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    students = relationship("Student", back_populates="city")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    age = Column(Integer)
    salary = Column(Float)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    index_number = Column(String, unique=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    date_of_birth = Column(Date)
    status = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="students")
