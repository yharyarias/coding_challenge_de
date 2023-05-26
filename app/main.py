from data_type import DataType
import mysql_helper as db
import csv_manager as mgr

mydb = db.MySQLHelper()  # MySQLHelper instance
mydb.connect()  # Establish the database connection

csv_manager = mgr.CSVManager()  # CSVManager instance

def insertEmployees(employees):
    """
    Insert employees data into the database.

    employees: List of employee data to insert.

    """
    try:
        if len(employees) >= 1:
            mydb.insertBatchEmployees(employees)  # Insert employee data in batches into the database
    except Exception as e:
        print("Error inserting data:", e)

def insertDepartmens(departments):
    """
    Insert departments data into the database.

    departments: List of department data to insert.

    """
    try:
        if len(departments) >= 1:
            mydb.insertBatchDepartments(departments)  # Insert department data in batches into the database
    except Exception as e:
        print("Error inserting data:", e)

def insertJobs(jobs):
    """
    Insert jobs data into the database.

    jobs: List of job data to insert.

    """
    try:
        if len(jobs) >= 1:
            mydb.insertBatchJobs(jobs)  # Insert job data in batches into the database
    except Exception as e:
        print("Error inserting data:", e)


employees = csv_manager.readCsv('data/hired_employees.csv', DataType.HIRED_EMPLOYEES)  # Read employee data from a CSV file
insertEmployees(employees)  # Insert hired_employees data into the database


jobs = csv_manager.readCsv('data/jobs.csv', DataType.JOBS)  # Read jobs data from a CSV file
insertJobs(jobs)  # Insert jobs data into the database


departments = csv_manager.readCsv('data/departments.csv', DataType.DEPARTMENTS)  # Read departments data from a CSV file
insertDepartmens(departments)  # Insert departments data into the database

mydb.disconnect()  # Close the database connection