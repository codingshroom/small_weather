import sqlite3


def insert_into(connection, table, types, values):
    statement = f"""
        INSERT INTO {table} ({type for type in types})
        VALUES ({"?, " for _ in types})
        """
    cursor.execute(statement, tuple(values))
    connection.commit()


def select_from(table, columns=["*"], condition=1):
    statement = f"""
        SELECT {column for column in columns}
        FROM table
        WHERE {condition}
    """
    cursor.execute(statement)
    rows = cursor.fetchall()
    return rows

