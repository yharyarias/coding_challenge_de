from datetime import date
from pydantic import BaseModel


class Rechired_employees(BaseModel):
    id_employee: int
    name: str
    datatime: date
    departments_id: int
    job_id: int

    class Config:
        orm_mode = True

class Departments(BaseModel):
    id_deparment: int
    department: str

    class Config:
        orm_mode = True


class Jobs(BaseModel):
    id_job: int
    job: str

    class Config:
        orm_mode = True
