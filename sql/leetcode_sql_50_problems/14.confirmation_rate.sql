-- Problem: Confirmation rate
-- Link: https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50


-- PostgreSQL
select S.user_id, 
cast(round(
        coalesce(
            avg(
                CASE
                    when action = 'confirmed' then 1
                    else 0
                end
            )
        , 0)
    , 2) as decimal(4, 2)) confirmation_rate
from Signups S LEFT JOIN Confirmations C ON S.user_id = C.user_id group by S.user_id;


-- MySQL
select S.user_id, 
cast(round(
        coalesce(
            avg(
                CASE
                    when action = 'confirmed' then 1
                    else 0
                end
            )
        , 0)
    , 2) as decimal(4, 2)) confirmation_rate
from Signups S LEFT JOIN Confirmations C ON S.user_id = C.user_id group by S.user_id;



/*
Notes:

    1. AVG(CASE WHEN condition THEN 1 ELSE 0 END)
        - Used to compute ratio of condition being true instead of (count(confirmed values) / count(*))
        - e.g., confirmation rate = confirmed / total

    2. ROUND(..., 2) returns numeric
        - Rounds a number to 2 decimal places
        - May return 1 instead of 1.00 unless casted

    3. Use CAST(... AS DECIMAL(4, 2)) to force 2 decimal display
        - CAST(... AS DECIMAL(p, s))
            - p = total digits
            - s = digits after decimal
            - e.g., DECIMAL(4, 2) can store up to 99.99

    4. COALESCE handles NULLs for users with no confirmations
        - COALESCE(value, fallback)
            - Returns `value` unless it's NULL
            - Used to handle cases with no confirmations (NULL avg)
            - Without it, some users would get NULL instead of 0.00
*/
