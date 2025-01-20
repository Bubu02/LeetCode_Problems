# Write your MySQL query statement below
-- SELECT employee_id,
--         department_id,
--         CASE WHEN COUNT(employee_id)>1 THEN 'Y'
--         ELSE 'N' END AS primary_flag
-- FROM Employee
-- GROUP BY employee_id

SELECT employee_id, department_id
FROM Employee
WHERE (primary_flag='Y'AND employee_id IN(
    SELECT employee_id FROM Employee
    GROUP BY employee_id
    HAVING COUNT(employee_id)>1
))
OR
(primary_flag='N'AND employee_id NOT IN(
    SELECT employee_id FROM Employee
    GROUP BY employee_id
    HAVING COUNT(employee_id)>1
))