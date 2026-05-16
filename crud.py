from sqlalchemy.orm import Session
import models
import schemas

# City CRUD
def get_cities(db: Session):
    return db.query(models.City).all()

def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()

def get_cities_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.name.ilike(f"%{name}%")).all()

def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(**city.model_dump())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def update_city(db: Session, city_id: int, city: schemas.CityCreate):
    db_city = db.query(models.City).filter(models.City.id == city_id).first()
    if db_city:
        for key, value in city.model_dump().items():
            setattr(db_city, key, value)
        db.commit()
        db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = db.query(models.City).filter(models.City.id == city_id).first()
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city

# Employee CRUD
def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees_by_firstname(db: Session, name: str):
    return db.query(models.Employee).filter(models.Employee.firstname.ilike(f"%{name}%")).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        for key, value in employee.model_dump().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

# Student CRUD
def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, student_identifier: str):
    # Try ID first, then Index Number
    if student_identifier.isdigit():
        student = db.query(models.Student).filter(models.Student.id == int(student_identifier)).first()
        if student: return student
    return db.query(models.Student).filter(models.Student.index_number == student_identifier).first()

def get_students_by_firstname(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.firstname.ilike(f"%{name}%")).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_identifier: str, student: schemas.StudentCreate):
    db_student = get_student(db, student_identifier)
    if db_student:
        for key, value in student.model_dump().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_identifier: str):
    db_student = get_student(db, student_identifier)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
