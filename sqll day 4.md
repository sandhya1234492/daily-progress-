# SQL Day 4: Constraints — Questions and Answers

1. What are constraints in SQL?
   Answer: Constraints are rules applied to table columns to control what data can be stored. They help keep data valid and consistent.
   Example:
   ```sql
   CREATE TABLE Students (
       student_id INT PRIMARY KEY,
       name VARCHAR(100) NOT NULL
   );
   ```
   Explanation: `PRIMARY KEY` and `NOT NULL` are constraints that enforce rules on the table.

2. What is the purpose of the NOT NULL constraint?
   Answer: `NOT NULL` requires a column to have a value. A row cannot be inserted or updated with `NULL` in that column.
   Example:
   ```sql
   name VARCHAR(100) NOT NULL
   ```
   Explanation: Every student row must include a name. An empty string is still a value; `NOT NULL` only disallows `NULL`.

3. What is the purpose of the UNIQUE constraint?
   Answer: `UNIQUE` prevents duplicate values in a column or a combination of columns.
   Example:
   ```sql
   email VARCHAR(150) UNIQUE
   ```
   Explanation: This prevents two rows from having the same email address. How a database handles multiple `NULL` values in a unique column can vary by database system.

4. What is the purpose of the PRIMARY KEY constraint?
   Answer: A `PRIMARY KEY` uniquely identifies each row in a table. Its values must be unique and cannot be `NULL`.
   Example:
   ```sql
   student_id INT PRIMARY KEY
   ```
   Explanation: Each student needs a distinct, non-null ID that can be used to find that student's row.

5. What is the purpose of the FOREIGN KEY constraint?
   Answer: A `FOREIGN KEY` links a column in one table to a key in another table and helps ensure that the referenced row exists.
   Example:
   ```sql
   CREATE TABLE Enrollments (
       enrollment_id INT PRIMARY KEY,
       student_id INT,
       FOREIGN KEY (student_id) REFERENCES Students(student_id)
   );
   ```
   Explanation: An enrollment can refer only to a `student_id` that exists in the `Students` table (unless the foreign-key column is allowed to be `NULL`).

6. What is the purpose of the CHECK constraint?
   Answer: `CHECK` restricts values according to a condition.
   Example:
   ```sql
   age INT CHECK (age >= 0)
   ```
   Explanation: This rule allows only ages that are zero or greater. CHECK support and behavior can differ among database systems.

7. What is the purpose of the DEFAULT constraint?
   Answer: `DEFAULT` supplies a value for a column when an `INSERT` statement does not provide one.
   Example:
   ```sql
   status VARCHAR(20) DEFAULT 'active'
   ```
   Explanation: If a new row omits `status`, the database uses `'active'`. Supplying `NULL` explicitly is not the same as omitting the column.

8. What is the difference between PRIMARY KEY and UNIQUE?
   Answer: Both enforce uniqueness, but a table can have only one primary key constraint, and its columns cannot contain `NULL`. A table can have multiple `UNIQUE` constraints. Whether a unique column permits one or multiple `NULL` values depends on the database system.
   Explanation: Use a primary key to identify rows; use unique constraints for other values that must not be duplicated, such as email addresses.

9. Can a table have multiple PRIMARY KEY constraints?
   Answer: No. A table can have only one primary key constraint. However, that primary key can be made up of multiple columns; this is called a composite primary key.
   Example:
   ```sql
   PRIMARY KEY (student_id, course_id)
   ```
   Explanation: The combination of `student_id` and `course_id` must be unique, even if each value can appear in many rows on its own.

10. Can a table have multiple UNIQUE constraints?
    Answer: Yes. A table can have multiple `UNIQUE` constraints on different columns or combinations of columns.
    Example:
    ```sql
    CREATE TABLE Users (
        user_id INT PRIMARY KEY,
        email VARCHAR(150) UNIQUE,
        username VARCHAR(50) UNIQUE
    );
    ```
    Explanation: This makes each email and each username unique, independently of the other.

Quick summary:
- `NOT NULL` requires a value.
- `UNIQUE` prevents duplicate values.
- `PRIMARY KEY` uniquely identifies each row.
- `FOREIGN KEY` links related tables.
- `CHECK` enforces a condition.
- `DEFAULT` supplies a value when one is omitted.
