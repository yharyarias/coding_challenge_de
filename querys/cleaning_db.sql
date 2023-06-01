CREATE DATABASE IF NOT EXISTS `globant`;
USE `globant`;

DROP TABLE IF EXISTS `hired_employees`;
DROP TABLE IF EXISTS `departments`;
DROP TABLE IF EXISTS `jobs`;

CREATE TABLE departments (
  id INT PRIMARY KEY,
  department VARCHAR(45)
);

-- Crear la tabla jobs
CREATE TABLE jobs (
  id INT PRIMARY KEY,
  job VARCHAR(45)
);

-- Crear la tabla hired_employees
CREATE TABLE hired_employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  datetime DATETIME(6),
  department_id INT,
  job_id INT
);