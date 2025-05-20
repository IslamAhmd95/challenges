-- Problem: Article Views
-- Link: https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50

-- PostgreSQL
select distinct(author_id) id from views where author_id = viewer_id order by id;

-- MySQL
select distinct(author_id) id from views where author_id = viewer_id order by id;