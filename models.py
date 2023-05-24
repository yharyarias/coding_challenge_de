from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base
import models


class Rechired_employees(Base):
    __tablename__ = "Rechired_employees"

    id_employee = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    datatime = Column(String(100), index=True)
    departments_id = Column(Integer, models.ForeignKey("Departments.id_department"))
    job_id = Column(Integer, models.ForeignKey("Jobs.id_job"))

class Departments(Base):
    __tablename__ = "Departments"

    id_deparment = Column(Integer, primary_key=True, index=True)
    department = Column(String(255), index=True)

class Jobs(Base):
    __tablename__ = "Jobs"

    id_job = Column(Integer, primary_key=True, index=True)
    job = Column(String(255), index=True)
