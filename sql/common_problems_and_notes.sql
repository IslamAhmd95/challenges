/*
Q1. Basic SELECT
Given a table employees(id, name, salary, department_id),
Write a query to return all employees whose salary is greater than the average salary in their department.
*/
with department_highest as 
(
    select *, avg(salary) over (partition by department_id) dept_avg_salary from employees
)
select * from department_highest where salary > dept_avg_salary;



/*
Q2. Aggregation
Table: orders(order_id, customer_id, amount, order_date)
Find the total sales amount per customer in 2024 and show only those customers whose total exceeded $10,000.
*/
select customer_id, sum(amount) total_sales
from orders
where order_date between '2024-01-01' and '2024-12-31'
group by customer_id
having sum(amount) > 10000;



/*
Q3. JOIN
We have:
customers(customer_id, name, country)
orders(order_id, customer_id, amount)
Write a query to find customers who placed no orders.
*/
select c.* from customer c left join orders o on c.customer_id = o.customer_id where o.order_id is null;



/*
Q4. Subquery
Table: products(product_id, product_name, price)
Find the second most expensive product.
*/
select * from 
    (
        select *, row_number() over (order by price desc) row_num from products
    ) highest_price 
where row_num = 2;
-- another solution but without subquery
select * from products order by price desc offset 1 limit 1;



/*
Q5. Window Function
Table: sales(id, product_id, sale_date, amount)
Write a query to return each product’s sales and also show the rank of each sale amount within that product (highest = rank 1).
*/
select product_id, amount, sale_date,
       rank() over (partition by product_id order by amount desc) as sale_rank
from sales;



/*
DISTINCT ON (PostgreSQL-specific)
Table: transactions(id, customer_id, amount, created_at)
Get each customer’s most recent transaction.
*/
select distinct on (customer_id) * from transaction order by created_at desc;



/*
Q7. HAVING Clause
Table: students(id, name, grade)
Find grades that have more than 5 students scoring above 90.
my note: I think students table needs one more column which is (score)
*/
select grade from students where score > 90 group by grade having count(grade) > 5;



/*
Q8. Schema Constraint
Write the SQL to create a table books with:
book_id as primary key,
title not null,
price must be greater than 0,
published_date defaulting to current date.
*/
create table IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) CHECK(price > 0),
    published_date DATE DEFAULT CURRENT_DATE
);



/*
Q9. Complex Query
We have a table attendance(id, student_id, class_date, status) where status = ‘Present’ or ‘Absent’.
Write a query to find the students who were absent 3 or more consecutive days.
*/
with absent_students as
(
    select student_id, class_date,
    row_number() over(partition by student_id order by class_date) rn
    from attendance
    where status = 'Absent'
) 
select student_id from absent_students group by student_id, (class_date - rn) having count(*) >= 3;




/* 
Q10. Optimization / Indexing
Suppose you have a table logs(id, user_id, action, created_at).
You frequently query by user_id and created_at range.
👉 What index (or indexes) would you create to optimize performance?
*/
create index idx_logs on logs (user_id, created_at);


-----------------------------------------------------------------------------------

-- Advanced SQL Practice Set


/*
Q1. Consecutive Absences (Gaps and Islands)

Table: attendance(student_id, class_date, status)
Find all absence streaks (start_date, end_date, streak_length) per student where the streak length is 3 days or more.
👉 Use the (date - row_number) trick.
*/

with absence_streaks as 
(
    select student_id, class_date,
    row_number() over (partition by student_id order by class_date) rn
    from attendance
    where status = 'Absent'
)
select student_id,
min(class_date) start_date,
max(class_date) end_date,
count(*) streak_length
from absence_streaks group by student_id, (class_date - rn * INTERVAL '1 day')
having count(*) >= 3; 



/*
Q2. Latest Order per Customer (De-duplication)

Table: orders(order_id, customer_id, order_date, amount)
Get the latest order (all columns) per customer.
👉 Solve this two ways:
- Using ROW_NUMBER().
- Using DISTINCT ON (Postgres).
*/

-- Using ROW_NUMBER().
select order_id, customer_id, order_date, amount from
(
    select *,
    row_number() over (partition by customer_id order by order_date desc) rn
    from orders
) latest_orders
where rn = 1;
-- Using DISTINCT ON (Postgres).
select distinct on (customer_id) * from orders order by customer_id, order_date desc;



/*
Q3. Sales Drop Detection (LAG)

Table: daily_sales(sale_date, sales)
- Find all dates where sales dropped compared to the previous day.
- Show: sale_date, sales, prev_sales, drop_amount.
*/

with drop_sales as 
(
    select *,
    lag(sales) over (order by sale_date) prev_sales
    from daily_sales
) 
select sale_date, sales, prev_sales,
prev_sales - sales as drop_amount
from drop_sales where prev_sales > sales;



/*
Q4. Cumulative Purchases

Table: orders(order_id, customer_id, amount, order_date)
For each customer, show their cumulative spending over time, ordered by order_date.
*/

with cumulative_spending as 
(
    select *,
    sum(amount) over (partition by customer_id order by order_date rows between unbounded preceding and current row) total_spending
    from orders
)
select * from cumulative_spending;



/*
Q5. Gaps in Attendance (Missing Dates)

Table: attendance(class_date)
Find all dates where attendance was missing (i.e., a gap in class_date).
👉 Use LAG() with INTERVAL '1 day'.
*/

with prev_classes as 
(
    select class_date,
    lag(class_date) over (order by class_date) prev_date
    from attendance
)
select generate_series(prev_date + INTERVAL '1 day', class_date - INTERVAL '1 day', INTERVAL '1 day') missing_dates from prev_classes where class_date > prev_date + INTERVAL '1 day';



/*
Q6. Conditional Aggregation

Table: students(id, name, grade)
Count how many students passed (grade ≥ 50) and how many failed (grade < 50) in a single query.
*/

select 
sum(case when grade >= 50 then 1 end) passed,
sum(case when grade < 50 then 1 end) failed
from students;



/*
Q7. Pivoting with CASE

Table: attendance(student_id, status)
Return one row per student with:

- present_days = number of “Present” records
- absent_days = number of “Absent” records
*/

select student_id,
sum(case when status='Present' then 1 end) present_days,
sum(case when status='Absent' then 1 end) absent_days
from attendance group by student_id;



/*
Q8. Null-Handling

Table: payments(payment_id, customer_id, amount, discount)

    - Sometimes discount is NULL.
    - If NULL, treat it as 0.
    - Show: customer_id, total_amount, total_discount, net_amount.

👉 Use COALESCE or IFNULL.
*/

select customer_id,
sum(amount) total_amount,
sum(coalesce(discount, 0)) total_discount,
sum(amount) - sum(coalesce(discount, 0)) net_amount
from payments;



/*
Q9. Avoid Divide-by-Zero (NULLIF)

Table: exam_results(student_id, total_marks, max_marks)
Calculate percentage as (total_marks / max_marks) * 100.
⚠ But sometimes max_marks = 0. Avoid division by zero using NULLIF.
*/

select *, (total_marks / nullif(max_marks, 0)) * 100 marks_percentage from exam_results;



/*
Q10. Rounding & Formatting

Table: orders(order_id, amount)
Show:

    - amount,
    - amount_rounded (to 2 decimal places),
    - amount_ceiling (always round up).

👉 Use ROUND(), CEIL() (or CEILING()).
*/

select amount, round(amount, 2) amount_rounded, ceiling(amount) amount_ceiling from orders;



/*
Q11. Self-Join Pairs

Table: students(id, name, class_id)
Find all unique pairs of students in the same class.
👉 Use a self join with s1.id < s2.id.
*/

select s1.name first_student, s2.name second_student from students s1 join students s2
on s1.class_id = s2.class_id and s2.id > s1.id;



/*
Q12. Set Comparison

Tables:

registration(student_id)
attendance(student_id)

Find students who registered but never attended.
👉 Use EXCEPT (or LEFT JOIN alternative if not Postgres).
*/

-- using except
select student_id from registration
except
select student_id from attendance;
-- using left join
select r.student_id from registration r left join attendance a on r.student_id = a.student_id where a.student_id is null;



/*
Q13. Consecutive Purchases + Running Total

Table: purchases(id, customer_id, purchase_date, amount)

- Detect streaks where a customer made purchases on 3 or more consecutive days.
- Within each streak, show the cumulative spending using SUM() OVER.
*/

with streaks as 
(
    select customer_id, purchase_date, amount,
    row_number() over (partition by customer_id order by purchase_date) rn
    from purchases
),
islands as 
(
    select customer_id, purchase_date, amount,
    (purchase_date - rn * INTERVAL '1 day') grp
    from streaks
),
grouped as 
(
    select customer_id,
    min(purchase_date) start_date,
    max(purchase_date) end_date,
    sum(amount) streak_total_amount,
    count(*) streak_length
    from islands
    group by customer_id, grp
    having count(*) >= 3
)
select customer_id, start_date, end_date, streak_total_amount, streak_length,
    sum(streak_total_amount) over (partition by customer_id order by start_date) cumulative_total_over_streaks
    from grouped;
    order by customer_id, start_date;



/*
Q14. Consecutive Absences

Table: attendance(student_id, class_date, status)

- status can be 'Present' or 'Absent'.
- We want to detect streaks where a student was absent for 2 or more consecutive days.
- For each streak, show:

    - student_id
    - start_date (first absence day)
    - end_date (last absence day)
    - streak_length

- Also calculate a running total of absences across all streaks for each student.
*/

with streaks as 
(
    select student_id, class_date,
    row_number() over(partition by student_id order by class_date) rn
    from attendance
    where status = 'Absent'
),
islands as 
(
    select student_id, class_date,
    (class_date - rn * INTERVAL '1 day') grp
    from streaks
),
grouped as 
(
    select student_id,
    min(class_date) start_date,
    max(class_date) end_date,
    count(*) streak_length
    from islands
    group by student_id, grp
    having count(*) >= 2
)
select *, sum(streak_length) over (partition by student_id order by start_date) cumulative_absence from grouped order by student_id, start_date;









/*

Common SQL Tricks for Problem Solving:

    1. When we want to detect consecutive events (like absences, purchases, logins, etc.), a useful trick is:

        (class_date - row_number() / rank() over(...))

        - row_number() always increases by 1 each row.
        - For consecutive dates, the gap between the actual date and rn remains constant.
        - When a "break" in dates happens, the constant shifts, creating a new group.

        class_date   rn   (class_date - rn)
        -----------  --   -----------------
        2025-01-01   1    2024-12-31
        2025-01-02   2    2024-12-31
        2025-01-03   3    2024-12-31
        2025-01-06   4    2025-01-02
        2025-01-07   5    2025-01-02

        Notice how consecutive dates (1st, 2nd, 3rd Jan) share the same value (2024-12-31).
        Non-consecutive dates fall into a different bucket (2025-01-02).


    2. ROW_NUMBER() for De-duplication

        - Purpose: Get the latest row per group (remove duplicates).
        - Idea: Assign row numbers by ORDER BY, keep only the first.
        - (offset & limit) way Only works for the entire result set, not per group like ROW_NUMBER()
        - Example: Get latest order per customer.

        SELECT * FROM 
        (
            SELECT o.*, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date DESC) AS rn FROM orders o
        ) t
        WHERE rn = 1;


    3. LAG() / LEAD() for Comparing Rows

        - Purpose: Compare a row to its previous/next row.
        - Example: Find days where sales dropped compared to yesterday.

        SELECT order_date, sales, LAG(sales) OVER(ORDER BY order_date) AS prev_sales
        FROM daily_sales
        WHERE sales < LAG(sales) OVER(ORDER BY order_date);


    4. Cumulative Sums with SUM() OVER

        - Purpose: Running totals, moving averages, progress tracking.
        - Example: Cumulative sales per customer.

        SELECT customer_id, order_date,
        SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date) AS cumulative_sales
        FROM orders;


    5. "Gaps and Islands" Problem

        - Purpose: Identify ranges of consecutive values (islands) or missing ones (gaps).
        - Trick: Use ROW_NUMBER() difference like in (1), or LAG() to detect gaps.
        - Example: Find missing dates in attendance.

        SELECT class_date FROM 
        (
            SELECT class_date,
            LAG(class_date) OVER(ORDER BY class_date) AS prev_date
            FROM attendance
        ) t
        WHERE class_date > prev_date + INTERVAL '1 day';



    6. Conditional Aggregation

        - Purpose: Count / sum based on conditions in the same query.
        - Example: Count passed vs failed students.

        SELECT 
        SUM(CASE WHEN grade >= 50 THEN 1 ELSE 0 END) AS passed,
        SUM(CASE WHEN grade < 50 THEN 1 ELSE 0 END) AS failed
        FROM students;


    7. DISTINCT ON (Postgres-specific)

        - Purpose: Get the "first row" per group in one step.
        - DISTINCT ON → Postgres shortcut for "first row per group".
        - Example: Get latest order per customer (shorter than ROW_NUMBER).

        SELECT DISTINCT ON (customer_id) * FROM orders
        ORDER BY customer_id, order_date DESC;


    8. Self Join for Pairs

        - Purpose: Find pairs of rows in the same table (e.g., friends, matches).
        - Example: Find pairs of students in same class.

        SELECT s1.name, s2.name FROM students s1
        JOIN students s2 ON s1.class_id = s2.class_id AND s1.id < s2.id;


    9. EXCEPT / INTERSECT

        - Purpose: Compare sets directly.
        - Example: Find students who registered but never attended.

        SELECT student_id FROM registration
        EXCEPT
        SELECT student_id FROM attendance;


    10. Pivoting with CASE

        - Purpose: Convert rows → columns.
        - Example: Count attendance per status.

        SELECT student_id,
        SUM(CASE WHEN status='Present' THEN 1 END) AS present_days,
        SUM(CASE WHEN status='Absent' THEN 1 END) AS absent_days
        FROM attendance
        GROUP BY student_id;



Other Notes:

    1. INTERVAL represents a time duration (not a timestamp).

        SELECT NOW() + INTERVAL '1 day';    -- adds 1 day
        SELECT NOW() - INTERVAL '2 hours';  -- subtracts 2 hours
        SELECT INTERVAL '1 year 2 months';  -- 1 year and 2 months

    2. Better write (date - rn * interval '1 day').

    3. Dividing any number by NULL in SQL results in NULL.
*/
