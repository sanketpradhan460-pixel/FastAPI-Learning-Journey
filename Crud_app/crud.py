from sqlalchemy.orm import Session
import models,schemas



def get_employees(db:Session):
    return db.query(models.Employee).all()


def get_employee(db:Session,emp_id:int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def create_employee(db:Session,emp:schemas.EmployeeCreate):
    db_employee=models.Employee(
        name=emp.name,
        email=emp.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db:Session,emp_id:int,employee:schemas.EmployeeUpdate):
    db_emp=db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_emp:
        db_emp.name=employee.name
        db_emp.email=employee.email
        db.commit()
        db.refresh(db_emp)
    return db_emp


def delete_employee(db:Session,emp_id:int):
    db_emp=db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if db_emp:
        db.delete(db_emp)
        db.commit()

    return db_emp