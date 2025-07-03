-- Problem: Classes With at Least 5 Students
-- Link: https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select class from courses group by class having count(student) >= 5;



/*
Notes:
    - WHERE filters rows, not groups.
    - COUNT(student) is an aggregate function, which works after grouping, so it must go in HAVING.
*/