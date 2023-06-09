import os
import mysql_helper as db
import csv_manager as mgr
from data_type import DataType
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import utils.df_utils as utils


SAVE_DIRECTORY = "data"

mydb = db.MySQLHelper()  # MySQLHelper instance
csv_manager = mgr.CSVManager()  # CSVManager instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    file_path = os.path.join(SAVE_DIRECTORY, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(file_bytes)

    csv_manager = mgr.CSVManager()

    print(file_path)
    if 'departments' in file_path:
        departments = csv_manager.readCsv(file_path, DataType.DEPARTMENTS)
        mydb.insertBatchDepartments(departments)
        return {"filename": file.filename, "saved_path": file_path, "departments": len(departments)}
    elif 'jobs' in file_path:
        jobs = csv_manager.readCsv(file_path, DataType.JOBS)
        mydb.insertBatchJobs(jobs)
        return {"filename": file.filename, "saved_path": file_path, "jobs": len(jobs)}
    elif 'hired_employees' in file_path:
        employees = csv_manager.readCsv(file_path, DataType.HIRED_EMPLOYEES)
        mydb.insertBatchEmployees(employees)
        return {"filename": file.filename, "saved_path": file_path, "employees": len(employees)}
    else:
        print("No match file")

@app.get("/departments_hired_employees/")
async def get_department_job_hires():
    try:
        data = mydb.get_department_job_hires(2021)
        print(data)
        if data is None:
            return processResult(data, msg=None)
        else:
            df = utils.convertToDataFrame(['department','','job','q1','q2','q3','q4'], data)
            df = utils.parseColumnsToInt(['q1','q2','q3','q4'], df)
            json = utils.toJson(df)
            return processResult(json)
    except:
        return processResult(None, msg="Error getting data")

@app.get("/departments_job/")
async def get_department_employees_hired():
    try:
        data = mydb.get_departments_hired_employees(2021)
        print(data)
        if data is None:
            return processResult(data, msg=None)
        else:
            df = utils.convertToDataFrame(['id','department','hired'], data)
            df = utils.parseColumnsToInt(['hired'], df)
            json = utils.toJson(df)
            return processResult(json)
    except:
        return processResult(None, msg="Error getting data")


def processResult(data, msg = None):
    if data is None:
        msg = "Query doesn't retrieve any data"
    return {"success":data is not None, "error": msg, "data": data}