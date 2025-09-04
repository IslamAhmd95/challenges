-- Problem: Invalid Tweets
-- Link: https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=top-sql-50
-- my rate: easy

-- PostgreSQL
select tweet_id from tweets where char_length(content) > 15;

-- MySQL
select tweet_id from tweets where char_length(content) > 15;


/*

Notes:

CHAR_LENGTH(s)	: Returns the number of characters in the string s

LENGTH(s)	:   Returns the number of bytes used to store the string s

*/