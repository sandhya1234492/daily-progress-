# SQL Day 1 Questions and Answers

1. What is SQL?
   SQL (Structured Query Language) is a standard language used to communicate with databases. It is used to create, read, update, and delete data stored in relational databases.

2. What is a database?
   A database is an organized collection of data that can be stored, managed, and accessed efficiently. Examples include MySQL, PostgreSQL, Oracle, and SQL Server.

3. What is a table in SQL?
   A table is a structured set of data arranged in rows and columns. It stores related information in a database, such as a Students table or Employee table.

4. What are rows and columns?
   - Rows are records or individual entries in a table.
   - Columns are fields or attributes that define the data type and structure of each record.

5. What is the difference between SQL and MySQL?
   - SQL is the language used to query and manage databases.
   - MySQL is a relational database management system (RDBMS) that uses SQL to interact with data.
   In simple terms, SQL is the language, and MySQL is one of the database systems that supports it.

6. What are the different types of SQL commands?
   SQL commands are mainly categorized as:
   - DDL (Data Definition Language): CREATE, ALTER, DROP
   - DML (Data Manipulation Language): INSERT, UPDATE, DELETE
   - DQL (Data Query Language): SELECT
   - DCL (Data Control Language): GRANT, REVOKE
   - TCL (Transaction Control Language): COMMIT, ROLLBACK, SAVEPOINT

7. What is the difference between DDL, DML, DQL, DCL, and TCL?
   - DDL: Defines and changes the structure of database objects like tables.
   - DML: Manipulates data inside the tables.
   - DQL: Retrieves data from the database.
   - DCL: Controls access and permissions to the database.
   - TCL: Manages transactions, ensuring data consistency and integrity.

8. What is the purpose of the CREATE command?
   The CREATE command is used to create database objects such as databases, tables, indexes, or views. Example: CREATE TABLE Students (...);

9. What is the difference between DROP, DELETE, and TRUNCATE?
   - DROP: Removes the entire table or database object permanently from the database.
   - DELETE: Removes specific rows from a table based on a condition.
   - TRUNCATE: Removes all rows from a table but keeps the table structure intact.
   Difference summary:
   - DROP = remove structure
   - DELETE = remove selected records
   - TRUNCATE = remove all records quickly

10. What is the purpose of the SELECT command?
   The SELECT command is used to retrieve data from one or more tables. It is the most commonly used SQL command for querying data. Example: SELECT * FROM Students;

