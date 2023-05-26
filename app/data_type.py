from enum import Enum

class DataType(Enum):
    """
    Enum class representing different data types available in this example.

    HIRED_EMPLOYEES: Represents the data type for hired_employees.csv file
    DEPARTMENTS: Represents the data type for departments.csv file
    JOBS: Represents the data type for jobs.csv file

    """
    HIRED_EMPLOYEES = 1
    DEPARTMENTS = 2
    JOBS = 3