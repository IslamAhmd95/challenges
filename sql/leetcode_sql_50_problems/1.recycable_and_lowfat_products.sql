-- Problem: Recyclable and Low Fat Products
-- Link: https://leetcode.com/problems/recyclable-and-low-fat-products/description/
-- my rate: easy

-- PostgreSQL
SELECT product_id FROM products WHERE low_fats='Y' AND recyclable='Y';

-- MySQL
SELECT product_id FROM products WHERE low_fats='Y' AND recyclable='Y';