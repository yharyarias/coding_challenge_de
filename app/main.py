import os
import mysql_helper as db
import csv_manager as mgr
from data_type import DataType
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

mydb = db.MySQLHelper()  # MySQLHelper instance
mydb.connect()  # Establish the database connection


csv_manager = mgr.CSVManager()  # CSVManager instance

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

SAVE_DIRECTORY = "data"


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