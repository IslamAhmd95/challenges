-- Problem: Percentage of Users Attended a Contest
-- Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL & MySQL
WITH contest_percentages AS (
  SELECT contest_id, 
         ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(*) FROM users), 2) AS percentage
  FROM register
  GROUP BY contest_id
)
SELECT *
FROM contest_percentages
ORDER BY percentage DESC, contest_id ASC;
