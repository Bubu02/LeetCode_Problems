# Write your MySQL query statement below
SELECT 'High Salary' AS category,
        COUNT(income) AS accounts_count FROM Accounts
WHERE income>50000
UNION
SELECT 'Average Salary' AS category,
        COUNT(income) AS accounts_count FROM Accounts
WHERE income>=20000 AND income<=50000
UNION
SELECT 'Low Salary' AS category,
        COUNT(income) AS accounts_count FROM Accounts
WHERE income<20000

-- SELECT a2.category, COUNT(a2.category) AS accounts_count
-- FROM Accounts a1
-- LEFT JOIN (
--     SELECT account_id,
--         income,
--         CASE
--         WHEN income<20000 THEN 'Low Salary'
--         WHEN income>=20000 AND income<=50000 THEN 'Average Salary'
--         -- WHEN income>50000 THEN 'High Salary'
--         ELSE 'High Salary'
--         END AS category
-- FROM Accounts
-- ) a2
-- ON a1.account_id=a2.account_id
-- GROUP BY a2.category;

