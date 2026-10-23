# SQL Day 7: SELECT Queries

The examples use a `Students` table with columns such as `student_name`, `age`, and `department_id`.

## 1. What is the purpose of the `SELECT` command?

**Answer:** `SELECT` retrieves data from one or more tables. You specify which columns to return after the command.

```sql
SELECT student_name
FROM Students;
```

This returns the `student_name` value for each row in `Students`.

## 2. How do you display all columns from the `Students` table?

**Answer:**

```sql
SELECT *
FROM Students;
```

The asterisk (`*`) means all columns. For production queries, naming only the columns you need is often clearer and more efficient.

## 3. How do you display only student names and ages?

**Answer:**

```sql
SELECT student_name, age
FROM Students;
```

Listing the column names returns only those columns, in the order shown.

## 4. How do you display unique department IDs?

**Answer:**

```sql
SELECT DISTINCT department_id
FROM Students;
```

`DISTINCT` removes duplicate values from the results.

## 5. How do you find the student name or names with the highest age?

**Answer:**

```sql
SELECT student_name, age
FROM Students
WHERE age = (SELECT MAX(age) FROM Students);
```

The subquery finds the greatest age, and the outer query returns every student with that age, including ties.

## 6. How do you display the first five student records?

**Answer:**

```sql
SELECT *
FROM Students
LIMIT 5;
```

`LIMIT 5` caps the result at five rows. Without an `ORDER BY` clause, which five rows appear is not guaranteed.

## 7. How do you display student names in alphabetical order?

**Answer:**

```sql
SELECT student_name
FROM Students
ORDER BY student_name ASC;
```

`ORDER BY` sorts the results. `ASC` means ascending order and is the default.

## 8. How do you display students in descending order of age?

**Answer:**

```sql
SELECT student_name, age
FROM Students
ORDER BY age DESC;
```

`DESC` sorts from highest age to lowest age.

## 9. How do you display students older than 18?

**Answer:**

```sql
SELECT student_name, age
FROM Students
WHERE age > 18;
```

`WHERE` filters rows to keep only those that satisfy the condition.

## 10. How do you count the number of students?

**Answer:**

```sql
SELECT COUNT(*) AS student_count
FROM Students;
```

`COUNT(*)` returns the number of rows, and `AS student_count` gives the result column a readable name.
