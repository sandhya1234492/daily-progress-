# SQL Day 5: Database Keys

### 1. What is a key in SQL?
**Answer:** A key is a column or set of columns used to identify rows or connect related tables. Keys help keep data unique and maintain relationships between tables.

### 2. What is a primary key?
**Answer:** A primary key uniquely identifies each row in a table. Its values must be unique and cannot be `NULL`. A table has one primary-key constraint, which may contain one column or multiple columns.

### 3. What is a foreign key?
**Answer:** A foreign key is a column or set of columns that refers to a key—usually the primary key—in another table. It helps ensure that a relationship points to an existing row. A foreign key may be `NULL` if the column allows it.

### 4. What is a candidate key?
**Answer:** A candidate key is a minimal column or set of columns that can uniquely identify every row. A table can have multiple candidate keys; one is selected as the primary key.

### 5. What is a super key?
**Answer:** A super key is any column or combination of columns that uniquely identifies every row. It can include extra columns, unlike a candidate key, which must be minimal.

### 6. What is an alternate key?
**Answer:** An alternate key is a candidate key that was not chosen as the table's primary key. It can still be constrained to have unique values.

### 7. What is a composite key?
**Answer:** A composite key uses two or more columns together to identify a row uniquely. For example, an `Enrollment` table might use `(student_id, course_id)` so a student can enroll in a course only once.

### 8. What is the difference between a primary key and a foreign key?
**Answer:** A primary key identifies rows within its own table and must be unique and non-`NULL`. A foreign key links to a key in another (or the same) table; its values may repeat, and may be `NULL` when allowed.

### 9. What is the difference between a candidate key and a primary key?
**Answer:** Candidate keys are all the minimal choices that could uniquely identify a row. The primary key is the one candidate key selected as the table's main identifier; the other candidate keys are alternate keys.

### 10. Why are keys important in a database?
**Answer:** Keys prevent unintended duplicate identities, make it possible to relate records across tables, and help enforce data integrity. For example, a foreign key can prevent an order from referring to a customer that does not exist.
