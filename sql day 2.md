# SQL Day 2 Questions and Answers

1. Write a query to create a database named college.
   Answer:
   ```sql
   CREATE DATABASE college;
   ```
   Explanation: This command creates a new database named `college` in the MySQL server, where you can store tables and data.

2. Write a query to select the college database.
   Answer:
   ```sql
   USE college;
   ```
   Explanation: `USE` selects the database for the current session so that all subsequent table operations are performed inside it.

3. Create a table named Students with the following columns: student_id, student_name, age, email, department.
   Answer:
   ```sql
   CREATE TABLE Students (
       student_id INT PRIMARY KEY,
       student_name VARCHAR(100),
       age INT,
       email VARCHAR(100),
       department VARCHAR(50)
   );
   ```
   Explanation: This statement creates a table named `Students` with columns for student ID, name, age, email, and department. `student_id` is the primary key, which uniquely identifies each row.

4. Write a query to display the structure of the Students table.
   Answer:
   ```sql
   DESC Students;
   ```
   OR
   ```sql
   DESCRIBE Students;
   ```
   Explanation: `DESC` or `DESCRIBE` shows the column names, data types, nullability, and key information of the table.

5. Write a query to display all tables in the current database.
   Answer:
   ```sql
   SHOW TABLES;
   ```
   Explanation: This command displays all tables existing in the currently selected database.

6. Write a query to add a column named phone to the Students table.
   Answer:
   ```sql
   ALTER TABLE Students
   ADD phone VARCHAR(15);
   ```
   Explanation: `ALTER TABLE` modifies the structure of an existing table and `ADD` inserts a new column named `phone`.

7. Write a query to modify the data type of the age column.
   Answer:
   ```sql
   ALTER TABLE Students
   MODIFY age INT;
   ```
   Explanation: `MODIFY` changes the column definition. In this example, `age` remains an integer but can be modified to a different size or type if needed.

8. Write a query to rename the Students table to Student_Details.
   Answer:
   ```sql
   ALTER TABLE Students
   RENAME TO Student_Details;
   ```
   Explanation: This command renames the existing table from `Students` to `Student_Details` without losing the data.

9. Write a query to remove the phone column from the table.
   Answer:
   ```sql
   ALTER TABLE Student_Details
   DROP COLUMN phone;
   ```
   Explanation: `DROP COLUMN` removes the specified column from the table structure.

10. Write a query to delete the Student_Details table.
    Answer:
    ```sql
    DROP TABLE Student_Details;
    ```
    Explanation: `DROP TABLE` removes the entire table and all its data permanently from the database.

11. Write a query to insert a new student record into the Students table.
    Answer:
    ```sql
    INSERT INTO Students (student_id, student_name, age, email, department)
    VALUES (101, 'Riya Sharma', 20, 'riya@gmail.com', 'Computer Science');
    ```
    Explanation: This statement inserts one row of data into the `Students` table.

12. Write a query to display all records from the Students table.
    Answer:
    ```sql
    SELECT * FROM Students;
    ```
    Explanation: `SELECT *` fetches every column and every row from the table.

13. Write a query to display only the student_name and department columns.
    Answer:
    ```sql
    SELECT student_name, department
    FROM Students;
    ```
    Explanation: This query retrieves only the selected columns instead of all table data.

14. Write a query to update a student’s email address.
    Answer:
    ```sql
    UPDATE Students
    SET email = 'riya.sharma@college.com'
    WHERE student_id = 101;
    ```
    Explanation: `UPDATE` modifies existing data and `WHERE` ensures only the matching student record is affected.

15. Write a query to delete a student record by student_id.
    Answer:
    ```sql
    DELETE FROM Students
    WHERE student_id = 101;
    ```
    Explanation: This removes only the row where `student_id` equals 101. Without `WHERE`, all rows would be deleted.

Summary:
- `CREATE` is used to build a database or table.
- `USE` selects the database.
- `ALTER` modifies an existing table structure.
- `DROP` permanently deletes a table or database object.
- `SELECT` retrieves data.
- `INSERT`, `UPDATE`, and `DELETE` manage records in the table.
