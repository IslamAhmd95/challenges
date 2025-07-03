-- Problem: User Activity for the Past 30 Days I
-- Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select activity_date as day, count(distinct user_id) active_users from activity where activity_date between '2019-06-28' and '2019-07-27' group by activity_date;



/*
Notes:
    - Use `WHERE` to filter raw data.
    - HAVING is for filtering aggregated results.
    - GROUP BY should use the actual column name (activity_date), not the alias (day).
*/