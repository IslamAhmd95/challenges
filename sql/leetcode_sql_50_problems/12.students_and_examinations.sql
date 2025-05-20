-- Problem: Students and Examinations
-- Link: https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select s.student_id, s.student_name, su.subject_name, count(e.student_id) attended_exams from students s cross join subjects su left join Examinations e on s.student_id = e.student_id and su.subject_name = e.subject_name group by s.student_id, s.student_name, su.subject_name order by s.student_id, su.subject_name;


-- MySQL
select s.student_id, s.student_name, su.subject_name, count(e.student_id) attended_exams from students s cross join subjects su left join Examinations e on s.student_id = e.student_id and su.subject_name = e.subject_name group by s.student_id, s.student_name, su.subject_name order by s.student_id, su.subject_name;



/*
Notes:

    1. CROSS JOIN generates all (student, subject) pairs — even when no exams are taken.

    2. LEFT JOIN on Examinations:
    - Ensures we preserve the full (student × subject) grid.
    - We join ON both student_id and subject_name to count accurately.

    3. COUNT(e.student_id) skips NULLs → correctly counts exams attended.
    - COUNT(*) would count all rows, even those with no matching exam (would overcount).

    4. GROUP BY must include all selected non-aggregated columns:
    - s.student_id, s.student_name, su.subject_name
    - MySQL may allow incomplete GROUP BY if ONLY_FULL_GROUP_BY is off, but that’s non-standard.
    - PostgreSQL requires full GROUP BY — stricter and more SQL-compliant.
*/
