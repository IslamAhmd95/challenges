-- Problem: Restaurant Growth
-- Link: https://leetcode.com/problems/restaurant-growth/?envType=study-plan-v2&envId=top-sql-50



-- MySQL
select a.visited_on, sum(b.amount) amount, round(sum(b.amount) / 7, 2) average_amount
from
(select distinct visited_on from Customer) a 
join Customer b
-- on b.visited_on between date_sub(a.visited_on, interval 6 day) and a.visited_on
on datediff(a.visited_on, b.visited_on) between 0 and 6
group by a.visited_on
having count(distinct b.visited_on) = 7
order by a.visited_on;

-- another solution
with daySum as
(
    select visited_on, sum(amount) amount from Customer group by visited_on
)
select a.visited_on, sum(b.amount) amount, round(avg(b.amount), 2) average_amount
from daySum a join daySum b
on b.visited_on between date_sub(a.visited_on, interval 6 day) and a.visited_on
group by a.visited_on
having count(distinct b.visited_on) = 7
order by a.visited_on;



-- PostgreSQL
select a.visited_on, sum(b.amount) amount, round(sum(b.amount::decimal) / 7, 2) average_amount
from
(select distinct visited_on from Customer) a 
join Customer b
on a.visited_on - b.visited_on between 0 and 6
group by a.visited_on
having count(distinct b.visited_on) = 7
order by a.visited_on;


-- another solution
with daySum as
(
    select visited_on, sum(amount) amount from Customer group by visited_on
)
select a.visited_on, sum(b.amount) amount, round(avg(b.amount::decimal), 2) average_amount
from daySum a join daySum b
on a.visited_on - b.visited_on between 0 and 6
group by a.visited_on
having count(distinct b.visited_on) = 7
order by a.visited_on;



/*
Notes:
    - Why Use SUM() / 7 Instead of AVG() in the Restaurant Growth Problem:
        - The goal is to calculate the **average daily total amount** over each 7-day period.
        - The data may have **multiple rows for the same day** because each customer visit creates a separate row (same visited_on date).
        - Using AVG(amount) would incorrectly compute the **average per transaction (row)** instead of the **average per day**.
        - Correct approach ➔ SUM all amounts in the 7-day window ➔ then divide by 7 (number of days).
    
    - Date Difference:
        - In **MySQL** ➔ use `DATEDIFF()` or `DATE_SUB()`.
        - In **PostgreSQL** ➔ simple date subtraction: `date1 - date2`.
*/
