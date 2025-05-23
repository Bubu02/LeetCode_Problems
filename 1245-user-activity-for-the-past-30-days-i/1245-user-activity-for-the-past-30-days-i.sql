# Write your MySQL query statement below
SELECT DISTINCT(activity_date) AS day,
        COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date> '2019-06-27' 
AND activity_date BETWEEN DATE('2019-07-27') - INTERVAL 30 DAY AND DATE('2019-07-27')
GROUP BY day;