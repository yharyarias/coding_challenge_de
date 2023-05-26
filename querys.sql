-- Drop all tables

DROP TABLE IF EXISTS `hired_employees`;
DROP TABLE IF EXISTS `departments`;
DROP TABLE IF EXISTS `jobs`;

-- Create table departments
CREATE TABLE departments (
  id INT PRIMARY KEY,
  department VARCHAR(45)
);

-- Create table jobs
CREATE TABLE jobs (
  id INT PRIMARY KEY,
  job VARCHAR(45)
);

-- Create table hired_employees
CREATE TABLE hired_employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  datetime DATETIME(6),
  department_id INT,
  job_id INT
);


--GetDepartmentJobHires procedures

--Number of employees hired for each job and department in 2021 divided by quarter. The
-- table must be ordered alphabetically by department and job.

-- SELECT
--    d.department,
--    '',
--    j.job,
--    SUM(IF(QUARTER(he.datetime) = 1, 1, 0)) AS Q1,
--    SUM(IF(QUARTER(he.datetime) = 2, 1, 0)) AS Q2,
--    SUM(IF(QUARTER(he.datetime) = 3, 1, 0)) AS Q3,
--    SUM(IF(QUARTER(he.datetime) = 4, 1, 0)) AS Q4
--  FROM
--    hired_employees he
--    INNER JOIN departments d ON he.department_id = d.id
--    INNER JOIN jobs j ON he.job_id = j.id
--  WHERE
--    YEAR(he.datetime) = 2021
--  GROUP BY
--    d.department,
--    j.job
--  ORDER BY
--    d.department,
--    j.job;

CREATE PROCEDURE `GetDepartmentJobHires`(IN p_year INT)
BEGIN
  SELECT
    d.department,
    '',
    j.job,
    SUM(IF(QUARTER(he.datetime) = 1, 1, 0)) AS Q1,
    SUM(IF(QUARTER(he.datetime) = 2, 1, 0)) AS Q2,
    SUM(IF(QUARTER(he.datetime) = 3, 1, 0)) AS Q3,
    SUM(IF(QUARTER(he.datetime) = 4, 1, 0)) AS Q4
  FROM
    hired_employees he
    INNER JOIN departments d ON he.department_id = d.id
    INNER JOIN jobs j ON he.job_id = j.id
  WHERE
    YEAR(he.datetime) = p_year
  GROUP BY
    d.department,
    j.job
  ORDER BY
    d.department,
    j.job;
END


--GetDepartmentsHiredEmployees procedures

--Number of employees hired for each job and department in 2021 divided by quarter. The
-- table must be ordered alphabetically by department and job.

--SELECT
--    d.id AS id,
--    d.department AS department,
--    COUNT(he.id) AS hired
--  FROM
--    departments d
--    INNER JOIN hired_employees he ON d.id = he.department_id
--  WHERE
--    YEAR(he.datetime) = p_year
--  GROUP BY
--    d.id,
--    d.department
--  HAVING
--    COUNT(he.id) > (
--      SELECT AVG(employees_hired) AS mean_employees_hired
--      FROM (
--        SELECT
--          department_id,
--          COUNT(id) AS employees_hired
--        FROM
--          hired_employees
--        WHERE
--          YEAR(datetime) = 2021
--        GROUP BY
--          department_id
--      ) AS avg_table
--    )
--  ORDER BY
--    hired DESC;

CREATE PROCEDURE `GetDepartmentsHiredEmployees`(IN p_year INT)
BEGIN
  SELECT
    d.id AS id,
    d.department AS department,
    COUNT(he.id) AS hired
  FROM
    departments d
    INNER JOIN hired_employees he ON d.id = he.department_id
  WHERE
    YEAR(he.datetime) = p_year
  GROUP BY
    d.id,
    d.department
  HAVING
    COUNT(he.id) > (
      SELECT AVG(employees_hired) AS mean_employees_hired
      FROM (
        SELECT
          department_id,
          COUNT(id) AS employees_hired
        FROM
          hired_employees
        WHERE
          YEAR(datetime) = p_year
        GROUP BY
          department_id
      ) AS avg_table
    )
  ORDER BY
    hired DESC;
END