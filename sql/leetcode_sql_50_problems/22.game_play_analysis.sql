-- Problem: Game Play Analysis IV
-- Link: https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL
with first_two_logs as
(
    select *, row_number() over(partition by player_id order by event_date) rn from Activity
)
select round(count(*) / (select count(distinct player_id) from Activity), 2) fraction
from first_two_logs l1 join first_two_logs l2 
ON l1.player_id = l2.player_id 
where l1.rn = 1 and l2.rn = 2 
and DATEDIFF(l2.event_date, l1.event_date) = 1;



-- PostgreSQL
with first_two_logs as
(
    select *, row_number() over(partition by player_id order by event_date) rn from Activity
)
select round(count(*)::decimal / (select count(distinct player_id) from Activity), 2) fraction
from first_two_logs l1 join first_two_logs l2 
ON l1.player_id = l2.player_id 
where l1.rn = 1 and l2.rn = 2 
and l2.event_date = l1.event_date + INTERVAL '1 day';




/*
Notes:
    Difference Between DISTINCT and DISTINCT ON (PostgreSQL)
    
        1️⃣ DISTINCT
            Removes duplicate rows based on the combination of columns specified.

            You can use it with one or more columns:

                `SELECT DISTINCT player_id, event_date FROM Activity;`
                → This will return unique pairs of player_id and event_date.

            It can also be used with COUNT() to count unique values:

                SELECT COUNT(DISTINCT player_id) FROM Activity;
                → Counts the number of unique player IDs.

        2️⃣ DISTINCT ON (PostgreSQL only)
            Used to get only the first row per group, based on the column(s) inside the parentheses.

            Syntax:

                SELECT DISTINCT ON (column1, column2) * FROM table
                ORDER BY column1, column2, some_other_column;
            It returns one row per group, determined by the columns in DISTINCT ON (...), and
            the ORDER BY decides which row is picked first from each group.

            You can write DISTINCT ON (column) * with or without a comma, but the correct and clean syntax is:

                SELECT DISTINCT ON (column) * FROM table;
                → No comma after DISTINCT ON (...). Writing DISTINCT ON (column), * is not correct syntax.

        📌 Comparison to ROW_NUMBER():
            DISTINCT ON (...) in PostgreSQL behaves similarly to using ROW_NUMBER() in MySQL or standard SQL:

                SELECT * FROM (
                    SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
                    FROM Activity
                ) sub
                WHERE rn = 1;
                Both give you the first row per group, ordered by your chosen column(s).
*/

-- first solution
select distinct on (a1.player_id) from activity a1 join activity a2 on a1.player_id = a2.player_id
where a2.event_date = a1.event_date + INTERVAL '1 day';


-- second solution
with first_two_logs as
(
    select *, row_number() over(partition by player_id order by event_date) rn from activity
)
select l1.player_id from first_two_logs l1 join first_two_logs l2
on l1.player_id = l2.player_id 
where l1.rn = 1 and l2.rn = 2
and l2.event_date = l1.event_date + INTERVAL '1 day';


WITH first_two_logs AS (
  SELECT *, row_number() OVER (PARTITION BY player_id ORDER BY event_date) rn
  FROM activity
)
SELECT l1.player_id
FROM first_two_logs l1
JOIN first_two_logs l2 ON l1.player_id = l2.player_id
WHERE l1.rn = 1 AND l2.rn = 2
AND DATEDIFF(l2.event_date, l1.event_date) = 1;
