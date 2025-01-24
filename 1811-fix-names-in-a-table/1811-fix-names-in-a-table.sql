# Write your MySQL query statement below
-- UPDATE Users
-- SET name = CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2)))
-- ORDER BY user_id;

SELECT user_id,
        CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2))) AS name
FROM Users
ORDER BY user_id;