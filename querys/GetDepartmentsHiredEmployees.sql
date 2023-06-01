CREATE DEFINER=`globant_client`@`%` PROCEDURE `GetDepartmentsHiredEmployees`(IN p_year INT)
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
