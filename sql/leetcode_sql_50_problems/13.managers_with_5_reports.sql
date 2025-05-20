-- Problem: Managers with at least 5 direct reports
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select E.name from employee E join employee R on E.id = R.managerId group by E.id, E.name having count(*) >= 5;

-- MySQL
select E.name from employee E join employee R on E.id = R.managerId group by E.id, E.name having count(*) >= 5;



/*
Notes:

    1- Why GROUP BY E.id, E.name?

        - SQL requires all non-aggregated SELECT columns to appear in GROUP BY.
        - Even if we're only selecting E.name, we group by E.id too because:
            - E.id is the primary key
            - E.name is not guaranteed to be unique
        - GROUP BY both ensures correctness and compatibility across PostgreSQL/MySQL.
*/