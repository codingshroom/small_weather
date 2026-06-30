import time
import sqlite3

from src.database import insert_into, select_from
from apis.get_api_key import get_api_key
from apis.coordinates_api import coordinates_api_call
from apis.moon_api import moon_api_call
from apis.weather_api import weather_api_call


def main():
    current_timestamp = int(time.time())
    moon_data = moon_api_call(current_timestamp)

    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            rows = select_from(cursor, connection, "moonphases")
            print(rows)

            insert_into(cursor, connection, "moonphases", ["stage", "illumination"], moon_data)

            rows = select_from(cursor, connection, "moonphases")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


if __name__ == "__main__":
    main()

