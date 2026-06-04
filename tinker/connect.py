import sqlite3


try:
    with sqlite3.connect("data/test.db") as connect:
        print("Created/Opened SQLite database successfully.")
except sqlite3.OperationalError as e: 
    print("Failed to open database:", e)


cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO test (id, name, age) 
    VALUES (?, ?, ?)
    """,
    (1, "two", 3)
)

connect.commit()

cursor.execute("""
    SELECT *
    FROM test
""")


rows = cursor.fetchall()
print(rows)

