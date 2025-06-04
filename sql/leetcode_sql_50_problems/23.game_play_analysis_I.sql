-- Problem: Game Play Analysis I
 
-- Description:
/*
Find the player_ids who logged in again on the next day after their first login.

A login is defined as a record in the `Activity` table.
You must find players who logged in exactly the day after their first login.
Return one row per player who satisfies this condition.

Table: Activity
Columns:
  player_id (int)
  device_id (int)
  event_date (date)
  games_played (int)
*/



-- MySQL
WITH first_two_logs AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) rn
    FROM Activity
)
SELECT l1.player_id
FROM first_two_logs l1
JOIN first_two_logs l2 ON l1.player_id = l2.player_id
WHERE l1.rn = 1 AND l2.rn = 2
AND DATEDIFF(l2.event_date, l1.event_date) = 1;




-- PostgreSQL
-- PostgreSQL Solution using ROW_NUMBER()
WITH first_two_logs AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) rn
    FROM Activity
)
SELECT l1.player_id
FROM first_two_logs l1
JOIN first_two_logs l2 ON l1.player_id = l2.player_id
WHERE l1.rn = 1 AND l2.rn = 2
AND l2.event_date = l1.event_date + INTERVAL '1 day';


-- PostgreSQL Solution using DISTINCT ON
SELECT DISTINCT ON (a1.player_id) a1.player_id
FROM activity a1
JOIN activity a2 ON a1.player_id = a2.player_id
WHERE a2.event_date = a1.event_date + INTERVAL '1 day'
ORDER BY a1.player_id, a1.event_date;
