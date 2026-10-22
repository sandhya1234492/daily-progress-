# SQL Day 6: Inserting Data

### 1. What is the purpose of the `INSERT INTO` command?
**Answer:** `INSERT INTO` adds one or more new rows to a database table.

### 2. Write a query to insert one student record into the `Students` table.
**Answer:**
```sql
INSERT INTO Students (student_id, name, age)
VALUES (1, 'Asha', 20);
```

### 3. Write a query to insert multiple student records into the `Students` table.
**Answer:**
```sql
INSERT INTO Students (student_id, name, age)
VALUES
    (2, 'Ravi', 21),
    (3, 'Mina', 19),
    (4, 'Dev', 22);
```

### 4. Why should you specify column names in an `INSERT` statement?
**Answer:** Listing column names makes it clear which value goes into each column. It also avoids relying on the table's column order and lets you omit columns that have defaults or allow `NULL`.

### 5. Can we insert data into selected columns only? Give an example.
**Answer:** Yes. Name only the columns you want to provide values for. Other columns must allow `NULL`, have a default, or be generated automatically.
```sql
INSERT INTO Students (student_id, name)
VALUES (5, 'Lina');
```

### 6. What must be true about the number and order of columns and values?
**Answer:** When column names are specified, there must be one value for each listed column, in the same order.
```sql
INSERT INTO Students (student_id, name, age)
VALUES (6, 'Noah', 20);
```

### 7. How do you insert a row using values for every column without listing column names?
**Answer:** Provide values in the table's defined column order. This is less clear and can break if the table structure changes, so listing columns is usually recommended.
```sql
INSERT INTO Students
VALUES (7, 'Isha', 18);
```

### 8. How can you insert a row using a query instead of literal values?
**Answer:** Use `INSERT INTO ... SELECT` to insert the rows returned by a query. The selected columns must match the target columns in count and compatible types.
```sql
INSERT INTO Alumni (student_id, name)
SELECT student_id, name
FROM Students
WHERE graduated = TRUE;
```

### 9. What happens if an inserted value violates a constraint?
**Answer:** The database rejects the insert if it violates a constraint such as a primary key, unique, foreign key, or `NOT NULL` constraint. Correct the value or provide a valid related record before retrying.

### 10. How can you check that a row was inserted?
**Answer:** Query the table using a value that identifies the row, such as its primary key.
```sql
SELECT student_id, name, age
FROM Students
WHERE student_id = 1;
```
