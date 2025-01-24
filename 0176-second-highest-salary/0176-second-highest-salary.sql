# Write your MySQL query statement below
SELECT MAX(salary) AS SEcondHighestSalary FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)