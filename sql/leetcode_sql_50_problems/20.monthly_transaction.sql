-- Problem: Monthly Transactions I
-- Link: https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select 
TO_CHAR(trans_date, 'YYYY-MM') AS month,
country, 
count(*) as trans_count,
count(
    case
        when state = 'approved' then 1
    end
) as approved_count,
sum(amount) as trans_total_amount,
sum(
    case
        when state = 'approved' then amount
        else 0
    end
) as approved_total_amount
from transactions group by month, country;



-- MySQL
select 
DATE_FORMAT(trans_date, '%Y-%m') AS month,
country, 
count(*) as trans_count,
count(
    case
        when state = 'approved' then 1
    end
) as approved_count,
sum(amount) as trans_total_amount,
sum(
    case
        when state = 'approved' then amount
        else 0
    end
) as approved_total_amount
from transactions group by month, country;

