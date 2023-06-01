CREATE DEFINER=`globant_client`@`%` PROCEDURE `GetDepartmentJobHires`(IN p_year INT)
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