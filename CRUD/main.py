
from fastapi import FastAPI, HTTPException
from model import employee
from typing import List

employees_db: List[employee] = []

app = FastAPI()


# 1. Read all employees
@app.get("/employees", response_model=List[employee])
def get_employees():
    return employees_db


# 2. Read a specific employee
@app.get("/employees/{emp_id}", response_model=employee)
def get_employee(emp_id: int):
    for emp in employees_db:
        if emp.id == emp_id:
            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# 3. Add an employee
@app.post("/employees", response_model=employee)
def add_employee(new_emp: employee):
    for emp in employees_db:
        if emp.id == new_emp.id:
            raise HTTPException(
                status_code=400,
                detail="Employee already exists"
            )

    employees_db.append(new_emp)
    return new_emp


# 4. Update an employee
@app.put("/update_employee/{emp_id}", response_model=employee)
def update_employee(emp_id: int, updated_employee: employee):

    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:

            if updated_employee.id != emp_id:
                raise HTTPException(
                    status_code=400,
                    detail="Employee ID cannot be changed"
                )

            employees_db[index] = updated_employee
            return updated_employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# 5. Delete an employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):

    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:
            del employees_db[index]

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
