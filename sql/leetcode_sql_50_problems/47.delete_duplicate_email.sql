-- Problem: Delete Duplicate Emails
-- Link: https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=top-sql-50



-- MySQL & PostgreSQL
DELETE FROM Person
WHERE id NOT IN (
  SELECT id FROM (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
  ) AS temp
);


-- MySQL
delete p1
from Person p1 join Person p2
on p1.email = p2.email and p1.id > p2.id;


-- PostgreSQL
delete from person where id in 
(
    select p2.id from person p1 join person p2 on p1.email = p2.email and p2.id > p1.id
)



/*
Notes:
    - DELETE FROM Person WHERE id NOT IN (
        SELECT id FROM (
            SELECT MIN(id) AS id
            FROM Person
            GROUP BY email
        ) AS temp
    );
        - SELECT MIN(id) gives the lowest ID for each email.
        - The outer query deletes any id not among those.
        - Wrapping the inner subquery with temp avoids read/write conflict in MySQL.
        - Portable across MySQL & PostgreSQL.
*/
