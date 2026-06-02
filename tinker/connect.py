import sqlite3


try:
    with sqlite3.connect("test.db") as conn:
        print("Opened SQLite database successfully.")
except sqlite3.OperationalError as e: 
    print("Failed to open database:", e)


cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT PRIMARY KEY, name TEXT NOT NULL, age INT NOT NULL);")

cursor.execute("INSERT INTO test (id, name, age) VALUES( 1, two, 3);")

