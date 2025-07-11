-- Problem: Exchange Seats
-- Link: https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
select id,
(
    case
        when id % 2 = 0 then lag(student) over(order by id)
        else coalesce(lead(student) over(order by id), student)
    end
) student
from Seat;



-- another solution
with new_seats as
(
    select id old_id, 
    (
        case
            when id % 2 != 0 and id < max(id) over() then id + 1
            when id % 2 = 0 then id - 1
            else id
        end

    ) new_id

    from Seat
)
select new_id as id, student from new_seats S1 join Seat S2 on S1.old_id = S2.id order by new_id;





/*
Notes:
    - MAX(id) OVER () gives the global max without ordering ➔ useful for checking the last seat.
    - MAX() OVER (ORDER BY col) ➔ Calculates a cumulative (running) maximum, not the global max.
    | id | `MAX(id) OVER (ORDER BY id)` | Explanation                 |
    | -- | ---------------------------- | --------------------------- |
    | 1  | 1                            | First row: max is 1 so far. |
    | 2  | 2                            | Max of (1,2) = 2.           |
    | 3  | 3                            | Max of (1,2,3) = 3.         |
    | 4  | 4                            | Max of (1,2,3,4) = 4.       |
    | 5  | 5                            | Max of (1,2,3,4,5) = 5.     |

*/

