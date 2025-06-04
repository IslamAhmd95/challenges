-- Problem: Queries quality and percentage 
-- Link: https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL & MySQL
select query_name,
round(avg(cast(rating as decimal) / position), 2) quality,
round(avg(
    case
        when rating < 3 then 1
        else 0
    end
) * 100.0 ,2) poor_query_percentage
from Queries group by query_name;



/*
Notes:
    Why CAST(rating AS DECIMAL) is needed in PostgreSQL but optional in MySQL:

        ✅ In MySQL:
        
            MySQL is more lenient.

            If you divide two integers like rating / position, MySQL automatically promotes the result to a decimal if needed.

            So even without the CAST, MySQL gives you a correct decimal result.

        🚫 In PostgreSQL:

            PostgreSQL is stricter.

            If both rating and position are integers, rating / position will return an integer by default (it truncates the decimal part).

            That means 5 / 2 → returns 2, not 2.5, unless you explicitly cast one side to a decimal.

            So, to get the correct average with decimal precision, you must cast:
            CAST(rating AS DECIMAL) or just rating * 1.0 / position.
*/