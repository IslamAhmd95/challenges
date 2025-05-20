-- Problem: Rising Temperature
-- Link: https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

-- PostgreSQL
select w1.id Id from weather w1 join weather w2 on (w1.recordDate::date - w2.recordDate::date) = 1 and w1.temperature > w2.temperature;
-- another solution using window functions
select id Id from (select id, temperature, lag(temperature) over(order by recordDate) prev_temp, recordDate, lag(recordDate) over(order by recordDate) prev_date from weather) two_days_weather WHERE (two_days_weather.recordDate::date - two_days_weather.prev_date::date) = 1 and
two_days_weather.temperature > two_days_weather.prev_temp;


-- MySQL
select w1.id Id from weather w1 join weather w2 on datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > W2.temperature;
-- another solution using window functions
select id Id from (select id, temperature, lag(temperature) over(order by recordDate) prev_temp, recordDate, lag(recordDate) over(order by recordDate) prev_date from weather) two_days_weather WHERE
datediff(two_days_weather.recordDate, two_days_weather.prev_date) = 1 and
two_days_weather.temperature > two_days_weather.prev_temp;



/*
 Notes:

    Be careful what you order by in window functions:

        - Use ORDER BY recordDate, not id, to ensure you're comparing temperatures across consecutive dates, not IDs.

        - id is arbitrary and may not reflect actual time sequence.

    JOIN vs Window Functions:

        - You can solve the problem by self-joining the table (comparing one row to the previous day's row).

        - Alternatively, use LAG() to get previous row’s values based on date order.

    Use DATEDIFF() (MySQL) or subtraction (PostgreSQL) to check consecutive days:

        - DATEDIFF(date1, date2) = 1 (MySQL)

        - (date1 - date2) = 1 (PostgreSQL)

        - Avoid just checking IDs — focus on actual date intervals.

    Placing conditions in ON vs WHERE:

    - Putting temperature > prev_temp in the ON clause helps limit unnecessary joins early on.

    - In INNER JOIN, ON vs WHERE usually gives same result, but ON is more efficient in join filtering.

    - ON in a LEFT JOIN:
        - Used during the join to decide which rows from the right table match.
        - If no match is found, you still get the left table's row, with NULLs for the right.
        - It's about matching the rows between tables

    - WHERE after the LEFT JOIN:
        - Applies after the join has finished. If you write WHERE right_table.col = something, and the right table row is NULL (because it didn’t match), that row gets removed, and it becomes like an INNER JOIN.
        - It's about filtering result after join
*/


--///////////////////////////////////////////////////////////////////////////////////////////////


/*
🧩 Practice a similar problem (PostgreSQL / MySQL compatible)

Problem:
    You are given two tables:

    Employees(id, name)

    Attendance(id, emp_id, date, status) — where status can be 'present' or 'absent'.

    Goal:
    Write a query to find all employees who were present today but were absent yesterday.
*/

-- PostgreSQL
SELECT E.id, E.name
FROM Employees E
JOIN Attendance A1 ON E.id = A1.emp_id
JOIN Attendance A2 ON A1.emp_id = A2.emp_id 
  AND (A1.date::date - A2.date::date) = 1
WHERE A1.status = 'present'
  AND A2.status = 'absent';

-- MySQL
SELECT E.id, E.name
FROM Employees E
JOIN Attendance A1 ON E.id = A1.emp_id
JOIN Attendance A2 ON A1.emp_id = A2.emp_id 
  AND DATEDIFF(A1.date, A2.date) = 1
WHERE A1.status = 'present'
  AND A2.status = 'absent';
