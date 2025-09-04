-- Problem: Customer Who Visited but Did Not Make Any Transactions
-- Link: https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

-- PostgreSQL
select customer_id, count(*) count_no_trans from visits V left join transactions T on V.visit_id = T.visit_id where transaction_id is null group by customer_id;

-- MySQL
select customer_id, count(*) count_no_trans from visits V left join transactions T on V.visit_id = T.visit_id where transaction_id is null group by customer_id;


/*

Notes:

    - The LEFT JOIN will include NULLs for non-matching rows after the join.
    - Then I should do the null-check after the join, using WHERE.

    - ON:	Match rows during JOIN (before join result is formed)
    - WHERE:	Filter rows after JOIN (before aggregation)
    - GROUP BY:	Group rows for aggregation
    - HAVING:	Filter after aggregation


    COUNT(*)

        - Counts all rows, including those with NULL values in any column.

        - Common when you don’t care which column has values.

        - ✅ Useful for total row count after joins.

    COUNT(column_name)

        - Counts non-NULL values only in the specified column.

        - ❗ If the column contains NULL, those rows are excluded from the count.

        - ✅ Useful when you're only interested in rows with actual data in that column.

    Invalid Usage: COUNT(table_alias.*)

        - ❌ Not valid syntax.

        - You must use either COUNT(*) or COUNT(alias.column).

    In LEFT JOIN cases:

        - Use COUNT(joined_table.column) to:

            - Count only matched rows (non-null).

            - Avoid counting rows with no matches (i.e., when the joined column is NULL).

        - Use COUNT(*) if you want to count every left-side row, even if the join failed.



*/