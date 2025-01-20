# Write your MySQL query statement below
SELECT e1.employee_id,
        e1.name,
        COUNT(e2.reports_to) AS reports_count,
        ROUND(AVG(e2.age),0) AS average_age
FROM Employees e1
JOIN Employees e2
ON e1.employee_id=e2.reports_to
GROUP BY e1.employee_id,e1.name
ORDER BY e1.employee_id

-- SELECT *
-- FROM Employees e
-- WHERE reports_to IN (
--     SELECT reports_to
--     FROM Employees
--     WHERE reports_to<>'null'
-- )