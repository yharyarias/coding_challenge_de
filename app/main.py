import mysql_helper as db
import csv_manager as mgr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from data_type import DataType

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

mydb = db.MySQLHelper()
mydb.connect()

csv_manager = mgr.CSVManager()



@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/employees")
def insertEmployees(employees):
    try:
        if len(employees) >= 1:
            mydb.insertBatchEmployees(employees)
    except Exception as e:
        print("Error inserting data:", e)
@app.get("/departments")
def insertDepartmens(departments):
    try:
        if len(departments) >= 1:
            mydb.insertBatchDepartments(departments)
    except Exception as e:
        print("Error inserting data:", e)
@app.get("/jobs")
def insertJobs(jobs):
    try:
        if len(jobs) >= 1:
            mydb.insertBatchJobs(jobs)
    except Exception as e:
        print("Error inserting data:", e)

departments = csv_manager.readCsv('data/departments.csv', DataType.DEPARTMENTS)
insertDepartmens(departments)

jobs = csv_manager.readCsv('data/jobs.csv', DataType.JOBS)
insertJobs(jobs)

employees = csv_manager.readCsv('data/hired_employees.csv', DataType.HIRED_EMPLOYEES)
insertEmployees(employees)

mydb.disconnect()