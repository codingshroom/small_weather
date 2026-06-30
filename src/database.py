import sqlite3


def insert_into(cursor, connection, table, columns, values):
    columns_as_string = ", ".join(c for c in columns)
    qmarks = ", ".join("?" for _ in columns)
    statement = f"""
        INSERT INTO {table} ({columns_as_string})
        VALUES ({qmarks})
        """
    cursor.execute(statement, tuple(values))
    connection.commit()


def select_from(cursor, connection, table, columns=["*"], condition=1):
    columns_as_string = ", ".join(c for c in columns)
    statement = f"""
        SELECT {columns_as_string}
        FROM {table}
        WHERE {condition}
    """
    cursor.execute(statement)
    rows = cursor.fetchall()
    return rows


def main():
    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            rows = select_from(cursor, connection, "moonphases")
            print(rows)

            insert_into(cursor, connection, "moonphases", ["stage", "illumination"], ("waxing", 54))

            rows = select_from(cursor, connection, "moonphases")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


if __name__ == "__main__":
    main()

