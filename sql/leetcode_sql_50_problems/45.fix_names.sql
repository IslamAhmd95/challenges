-- Problem: Fix Names in a Table
-- Link: https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select user_id, 
concat(upper(substr(name, 1, 1)), lower(substring(name, 2))) 
name from users order by user_id;


/*
Notes:
    - Both SUBSTR() and SUBSTRING() are functionally equivalent in most SQL dialects (MySQL, PostgreSQL).
    - Syntax:
        SUBSTR(string, start_position, length)
        SUBSTRING(string, start_position, length)
    - In both functions:
        - The string index is 1-based (first character is position 1).
        - If you omit the third argument (length), it returns the substring from the starting position to the end.
            - lower(substring(name, 2) = lower(substring(name, 2, length(name))
*/
