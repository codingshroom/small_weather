import sqlite3

from src.database import select_from, insert_into


'''
    How to use data_exists():

    cities:         cityName
    dates:          date
    moonphases:     stage, illumination
    profiles:       profileName
    requests:       profileID, cityID, date
    weatherdata:    cityID, date, hour, temperature, rainProbability, rainAmount
'''


def data_exists(cursor, connection, table, **data):
    condition_string = " AND ".join(f"{key} = '{value}'" for key, value in data.items())
    exists = select_from(cursor, connection, table, columns=["1"], condition=condition_string)
    return bool(exists)


def test_blank(table, **data):
    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            exists = data_exists(cursor, connection, table, **data)
            print(exists)

            if not exists:
                columns = [key for key, _ in data.items()]
                values = [value for _, value in data.items()]
                insert_into(cursor, connection, table, columns, values)

            rows = select_from(cursor, connection, table)
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


def main():
    test_blank("weatherdata", cityID=2, date="2026-06-30", hour=1, temperature=21, rainProbability=60, rainAmount=4)


if __name__ == "__main__":
    main()

