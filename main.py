from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="School/Company Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- City Endpoints ---

@app.get("/cities/", response_model=List[schemas.City])
def read_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)

@app.get("/cities/search/{name}", response_model=List[schemas.City])
def search_cities(name: str, db: Session = Depends(get_db)):
    return crud.get_cities_by_name(db, name)

@app.get("/cities/{id}", response_model=schemas.City)
def read_city(id: int, db: Session = Depends(get_db)):
    db_city = crud.get_city(db, id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@app.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db, city)

@app.put("/cities/{id}", response_model=schemas.City)
def update_city(id: int, city: schemas.CityCreate, db: Session = Depends(get_db)):
    db_city = crud.update_city(db, id, city)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@app.delete("/cities/{id}")
def delete_city(id: int, db: Session = Depends(get_db)):
    db_city = crud.delete_city(db, id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return {"message": "City deleted successfully"}

# --- Employee Endpoints ---

@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/search/{name}", response_model=List[schemas.Employee])
def search_employees(name: str, db: Session = Depends(get_db)):
    return crud.get_employees_by_firstname(db, name)

@app.get("/employees/{id}", response_model=schemas.Employee)
def read_employee(id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.put("/employees/{id}", response_model=schemas.Employee)
def update_employee(id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# --- Student Endpoints ---

@app.get("/students/", response_model=List[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/search/{name}", response_model=List[schemas.Student])
def search_students(name: str, db: Session = Depends(get_db)):
    return crud.get_students_by_firstname(db, name)

@app.get("/students/{identifier}", response_model=schemas.Student)
def read_student(identifier: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, identifier)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{identifier}", response_model=schemas.Student)
def update_student(identifier: str, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, identifier, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{identifier}")
def delete_student(identifier: str, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, identifier)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
