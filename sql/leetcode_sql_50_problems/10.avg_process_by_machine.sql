-- Problem: Average Time of Process per Machine
-- Link: https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

-- PostgreSQL
select A1.machine_id, round(avg(A2.timestamp - A1.timestamp)::numeric, 3) processing_time from Activity A1 join Activity A2 on A1.machine_id = A2.machine_id and A1.process_id = A2.process_id and A1.activity_type = 'start' and A2.activity_type = 'end' group by A1.machine_id;

-- MySQL
select A1.machine_id, round(avg(A2.timestamp - A1.timestamp), 3) processing_time from Activity A1 join Activity A2 on A1.machine_id = A2.machine_id and A1.process_id = A2.process_id and A1.activity_type = 'start' and A2.activity_type = 'end' group by A1.machine_id;


/*
Notes:
    - We have to use ::numeric in postgresql to convert the interval to a numeric value
    - The interval is a data type in SQL that represents a duration of time like "2 days, 4 hours, 1 day 3 hours 25 seconds" which is not a number
    - AVG(interval) works, but ROUND() doesn't support intervals.
    - So you must cast the result of AVG(...) to numeric to round it.
    "
    a2.timestamp - a1.timestamp       -- interval
    AVG(a2.timestamp - a1.timestamp) -- still interval
    ROUND(..., 3)                    -- requires numeric
    "
    - To convert an INTERVAL to seconds (as a number), use:
    "EXTRACT(EPOCH FROM end_time - start_time)"
    - EPOCH means total seconds.

    - a2.timestamp - a1.timestamp gives you an INTERVAL.
    - EXTRACT(EPOCH FROM ...) converts that interval to seconds (as a double precision number).
    - AVG(...) averages the seconds.
    - ROUND(..., 3) rounds the result to 3 decimal places.
    - ::numeric ensures compatibility with ROUND.

    - To get time in hours, divide the EPOCH (in seconds) by 3600.
    - To get time in minutes, divide the EPOCH (in seconds) by 60.
*/