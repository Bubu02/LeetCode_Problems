# Write your MySQL query statement below
SELECT p.product_name, o.unit
FROM Products p
JOIN (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE MONTH(order_date)=02 AND YEAR(order_date)=2020
    GROUP BY product_id
    HAVING SUM(unit) >=100
) o
ON p.product_id=o.product_id