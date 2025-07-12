-- Problem: Second Highest Salary
-- Link: https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) as SecondHighestSalary;

-- another solution
SELECT coalesce((
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
), null) as SecondHighestSalary;


/*
Notes:
    - Scalar Subquery:
        - A scalar subquery is a subquery used inside a SELECT clause or elsewhere that always returns exactly one value (either a real value or NULL if no rows).

    - Why Use It Here?
        - We need to ensure the query always returns a row—even if the second highest salary does not exist. A scalar subquery solves this by returning NULL instead of no result.
    - Syntax:
        SELECT (SELECT ...) AS alias_name;
        - No need for FROM or * in the outer query.
    - COALESCE is optional here because the scalar subquery will naturally return NULL if no value is found.
    - We can still use COALESCE for clarity or default values.
*/
