import sqlite3

# Step 01: Connect to Database
conn = sqlite3.connect('test.db')

# Step 02: Create Student Table
conn.execute('''
    CREATE TABLE IF NOT EXISTS student (
        student_name TEXT NOT NULL,
        course_name TEXT NOT NULL
    );
''')

# Step 03: Insert Values into the Table
conn.execute('''
    INSERT INTO student (student_name, course_name)
    VALUES ('Adel', 'fbw12');
''')

# Commit the changes
conn.commit()

# Step 04: Read and Display Data from Table
cursor = conn.execute('SELECT * FROM student;')
result = cursor.fetchall()

# Print the result
print("Result from DB for student table:", result)

# Step 05: Close Database Connection
conn.close()
