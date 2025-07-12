-- Problem: Patients With a Condition
-- Link: https://leetcode.com/problems/patients-with-a-condition/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select * from Patients where conditions like 'DIAB1%' or conditions like '% DIAB1%';


/*
Notes:
    - % in SQL LIKE means “Zero or more characters” (could be letters, numbers, spaces, punctuation, anything)
    - If you want to specifically check for a space, you must include a literal space
        `
            WHERE name LIKE '% DIAB1%'   -- ensures a space before 'DIAB1'
        `
*/
