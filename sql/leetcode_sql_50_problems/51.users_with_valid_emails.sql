-- Problem: Find Users With Valid E-Mails
-- Link: https://leetcode.com/problems/find-users-with-valid-e-mails/description/


-- MySQL
SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c');


-- PostgreSQL
SELECT *
FROM Users
WHERE mail ~ '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$';


/*
Notes:
    - MySQL Solution
        - 'c' → case-sensitive
        - ^[a-zA-Z] → must start with a letter
        - [a-zA-Z0-9._-]* → valid prefix characters
        - @leetcode\\.com$ → exact domain match, case-sensitive

    - PostgreSQL Solution
        - `^` anchors the start of the string
        - `[A-Za-z]` ensures the first character is a letter
        - `[A-Za-z0-9._-]*` allows allowed characters in the prefix
        - `@leetcode\.com$` ensures the email ends exactly with @leetcode.com (case-sensitive)
        - `~` in PostgreSQL is the case-sensitive regex match operator


    | Symbol     | Meaning                                 | Example                       |     |                  |
    | ---------- | --------------------------------------- | ----------------------------- | --- | ---------------- |
    | `^`        | Start of string                         | `^a` means "starts with a"    |     |                  |
    | `$`        | End of string                           | `a$` means "ends with a"      |     |                  |
    | `[A-Za-z]` | One **letter** (uppercase or lowercase) | `[0-9]` for digit             |     |                  |
    | `*`        | 0 or more of the previous character     | `a*` → `""`, `a`, `aaa`       |     |                  |
    | `+`        | 1 or more of the previous character     | `a+` → `a`, `aaa` (not empty) |     |                  |
    | `.`        | Any single character                    | `a.b` matches `acb`, `a1b`    |     |                  |
    | `\.`       | A literal period `.`                    | `@leetcode\.com`              |     |                  |
    | \`         | \`                                      | OR                            | \`a | b`means`a`or`b\` |
    | `()`       | Grouping                                | `(abc)+` repeats the group    |     |                  |

*/
