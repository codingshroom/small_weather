import sqlite3

from src.database import select_from, insert_into


def check_profile(cursor, connection, profile_name):
    if not select_from(cursor, connection, "profiles", columns=["1"], condition=f"profileName = '{profile_name}'"):
        return False
    return True



def main():
    date = "2026-05-09"
    city = "Berlin"
    profile = "Kel"

    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            profile_exists = check_profile(cursor, connection, profile)
            print(profile_exists)

            if not profile_exists:
                insert_into(cursor, connection, "profiles", ["profileName"], [profile])

            rows = select_from(cursor, connection, "profiles")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)

    


if __name__ == "__main__":
    main()

