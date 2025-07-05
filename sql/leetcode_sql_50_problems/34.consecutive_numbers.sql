-- Problem: Consecutive Numbers
-- Link: https://leetcode.com/problems/consecutive-numbers/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
with consecutive_numbers as
(
select num, 
lag(num) over(order by id) prev_num,
lead(num) over(order by id) next_num
from logs
)
select num ConsecutiveNums from consecutive_numbers where prev_num = num and num = next_num group by num;





/*
Notes:
    - What works for 4+ Consecutive Numbers ?
    `
    WITH numbered_logs AS 
    (
        SELECT *, 
                ROW_NUMBER() OVER (ORDER BY id) AS rn
        FROM logs
    )
    SELECT num
    FROM numbered_logs
    GROUP BY num, rn - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id)
    HAVING COUNT(*) >= 4;

    `
    - The difference between the two ROW_NUMBERs is the same for rows in the same consecutive block.


| id | num | ROW\_NUMBER() (by id) | ROW\_NUMBER() (partition by num) | Difference |
| -- | --- | --------------------- | -------------------------------- | ---------- |
| 1  | 3   | 1                     | 1                                | 0          |
| 2  | 3   | 2                     | 2                                | 0          |
| 3  | 3   | 3                     | 3                                | 0          |
| 4  | 2   | 4                     | 1                                | 3          |
| 5  | 2   | 5                     | 2                                | 3          |
| 6  | 5   | 6                     | 1                                | 5          |


*/