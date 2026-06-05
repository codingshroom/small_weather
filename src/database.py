import sqlite3


def insert_into(connection, table, columns, values):
    columns_as_string = ", ".join(c for c in columns)
    qmarks = ", ".join("?" for _ in columns)
    statement = f"""
        INSERT INTO {table} ({columns_string})
        VALUES ({qmarks})
        """
    cursor.execute(statement, tuple(values))
    connection.commit()


def select_from(table, columns=["*"], condition=1):
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
    pass


if __name__ == "__main__":
    main()

