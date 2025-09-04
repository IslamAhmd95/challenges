-- Problem: Replace Employee ID With The Unique Identifier
-- Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50
-- my rate: easy

-- PostgreSQL
select E.name, EU.unique_id from employees E left join EmployeeUNI EU on E.id = EU.id;

-- MySQL
select E.name, EU.unique_id from employees E left join EmployeeUNI EU on E.id = EU.id;


/*
Notes:

1. Natural Join: A NATURAL JOIN automatically joins tables on columns with the same name and data type in both tables.

    SELECT E.name, EU.unique_id FROM employees E NATURAL LEFT JOIN EmployeeUNI EU;
    In this case, since both tables have id, the join will automatically be made on id.

    - Downsides of NATURAL JOIN
        - It hides the join condition — less readable
        - If schema changes (e.g., both tables later may have created_at column), behavior changes unexpectedly
        - Not considered a best practice in production SQL
        - Better to be explicit with ON condition.


2. Using JOIN ... USING

    SELECT E.name, EU.unique_id FROM employees E LEFT JOIN EmployeeUNI EU USING (id);
    USING (id) means:
        - Join on column id
        - id will appear once in the result, not E.id and EU.id
        
*/