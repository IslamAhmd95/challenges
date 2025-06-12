-- Problem: Number of Unique Subjects Taught by Each Teacher
-- Link: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select teacher_id, count(distinct subject_id) cnt from Teacher group by teacher_id;