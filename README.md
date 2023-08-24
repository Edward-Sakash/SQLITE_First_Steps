### Exercise 01: How to save data in Database system(DB)

Lets try to create student table with 2 attributes/columns called student_name and course_name. Store some values and read the database in the terminal. Compare this with previous way of storing data in short sentence and let the teacher know.

- Step 01: import SQlite3 database and connect with a test database
- Step 02: try to create a student table with SQL query like below:

```
CREATE TABLE tableName
column_name1 data_type not null,
column_name2 data_type not null;

```

Step 03: Insert values in database like below query

```
INSERT INTO tableName
(column1, column2)\
(value1, value 2);
```

Step 04: Read the table from database(db)
use below query to read, here \* means all

```
SELECT * FROM tableName;
```

Step 05: close database connection

- Your result may be look like that:

```
Result from DB for student table:  [{'student_name': 'Adel', 'course_name': 'fbw12'}]
```
