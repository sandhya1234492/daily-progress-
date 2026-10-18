What are data types in SQL?
Data types define the kind of values a column can store, such as numbers, text, dates, or booleans. They help keep data consistent and make SQL operations efficient.

What is the difference between INT and VARCHAR?
INT is a numeric data type used for whole numbers, such as 1, 25, 1000.
VARCHAR is a variable-length text data type used for strings like names, emails, and addresses.
Example:
- INT: 101
- VARCHAR: 'Alice'

What is the difference between CHAR and VARCHAR?
CHAR is a fixed-length string type. If you define CHAR(10), it always stores 10 characters, padding with spaces if needed.
VARCHAR is a variable-length string type. It stores only the characters entered, up to the maximum length you set.
Example:
- CHAR(5): 'A   '
- VARCHAR(5): 'A'

What is the purpose of the DATE data type?
The DATE data type stores calendar dates in a standard format such as YYYY-MM-DD, for example 2026-10-18. It is used for values like birth dates, order dates, and event dates.

Which data type is suitable for storing:
- Student names -> VARCHAR
- Student IDs -> INT (if numeric IDs) or VARCHAR (if IDs contain letters or leading zeros)
- Email addresses -> VARCHAR
- Salaries -> DECIMAL(10,2) or NUMERIC (best for money values)
- Dates of birth -> DATE

Quick summary:
- INT = whole numbers
- VARCHAR = text with variable length
- CHAR = fixed-length text
- DATE = date only (no time)
- DECIMAL/NUMERIC = exact decimal values like money