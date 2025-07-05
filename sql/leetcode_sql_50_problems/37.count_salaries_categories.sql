-- Problem: Count Salary Categories
-- Link: https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with cats as
(
SELECT 'Low Salary' AS category
UNION ALL
SELECT 'Average Salary'
UNION ALL
SELECT 'High Salary'
),
accounts_cats as
(
    select
    (
        CASE 
        WHEN income < 20000 THEN 'Low Salary'
        WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
        WHEN income > 50000 THEN 'High Salary'
    END

    ) as category
    from Accounts
)
select C.category, coalesce(count(AC.category), 0) accounts_count from cats C left join accounts_cats AC on C.category = AC.category group by C.category;



/*
Notes:
    - By using multiple SELECT statements with UNION or UNION ALL, you are creating a virtual table that doesn’t exist in the database.
    - This temporary result behaves just like a real table—you can JOIN with it, GROUP BY, filter, etc.

        SELECT 'ahmed' AS name
        UNION ALL
        SELECT 'mohamed'
        UNION ALL
        SELECT 'islam';

        result:
        
        | name    |
        | ------- |
        | ahmed   |
        | mohamed |
        | islam   |

   

    - UNION ALL: Combines multiple SELECT results into one table (adds rows, not columns) and **keeps duplicates** (no filtering).
    
    - UNION: Combines multiple SELECT results into one table (adds rows, not columns) but **removes duplicates** automatically.

    - In UNION or UNION ALL, the **alias (column name)** is determined by the **first SELECT statement only**:
          SELECT 'Low Salary' AS category
          UNION ALL
          SELECT 'High Salary';  -- no need to alias again

    - Both UNION and UNION ALL require:
        1. The **same number of columns** in each SELECT.
        2. The **columns to have compatible data types**.

    - If both SELECT queries return columns with the **same name and type**, no alias is needed.
    - The final result will use the column name from the **first SELECT**.
        -- With duplicates:
        SELECT name FROM Customers
        UNION ALL
        SELECT name FROM Suppliers;

        -- Without duplicates:
        SELECT name FROM Customers
        UNION
        SELECT name FROM Suppliers;
*/

