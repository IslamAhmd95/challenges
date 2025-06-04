-- Problem: Average Selling Price
-- Link: https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select P.product_id, 
    round(
        coalesce(
            sum(P.price * U.units)::decimal / nullif(sum(U.units), 0)
        , 0)
    , 2) average_price
from Prices P left join UnitsSold U on P.product_id = U.product_id and U.purchase_date between P.start_date and P.end_date group by P.product_id;


-- MySQL
select P.product_id, 
    round(
        coalesce(
            sum(P.price * U.units) / nullif(sum(U.units), 0)
        , 0)
    , 2) average_price
from Prices P left join UnitsSold U on P.product_id = U.product_id and U.purchase_date between P.start_date and P.end_date group by P.product_id;



/*
Notes:
    
    - Use NULLIF(denominator, 0) to avoid division by zero errors.
    - Not every "average" is solved using AVG().
        - Use AVG() when each row has equal weight.
        - Use SUM(...) / SUM(...) when you're calculating a weighted average (like price × quantity).
    - In PostgreSQL, int / int = int unless you cast one side to a decimal/float.
        Use ::decimal, ::numeric, or CAST(... AS decimal) to ensure proper float division.

    - MySQL will automatically promote to float if any side is decimal — but PostgreSQL will not.
*/