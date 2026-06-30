import sqlite3

from src.database import select_from, insert_into


def check_profile(cursor, connection, profile_name):
    if not select_from(cursor, connection, "profiles", columns=["1"], condition=f"profileName = '{profile_name}'"):
        return False
    return True


def check_moonphase(cursor, connection, stage, illumination):
    stage_exists = select_from(cursor, connection, "moonphases", columns=["1"], condition=f"stage = '{stage}'") 
    illumination_exists = select_from(cursor, connection, "moonphases", columns=["1"], condition=f"illumination = '{illumination}'") 

    if stage_exists and illumination_exists:
        return True
    return False


def check_city(cursor, connection, city_name):
    if not select_from(cursor, connection, "cities", columns=["1"], condition=f"cityName = '{city_name}'"):
        return False
    return True


def check_date(cursor, connection, date):
    if not select_from(cursor, connection, "dates", columns=["1"], condition=f"date = '{date}'"):
        return False
    return True


def test_date():
    date = "2026-06-30"
    moonID = 18

    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            date_exists = check_date(cursor, connection, date)
            print(date_exists)

            if not date_exists:
                insert_into(cursor, connection, "dates", ["date", "moonID"], [date, moonID])

            rows = select_from(cursor, connection, "dates")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


def test_city():
    city = "Berlin"
    lat = 5
    lon = 666

    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            city_exists = check_city(cursor, connection, city)
            print(city_exists)

            if not city_exists:
                insert_into(cursor, connection, "cities", ["cityName", "latitude", "longitude"], [city, lat, lon])

            rows = select_from(cursor, connection, "cities")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)


def test_profile():
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


def test_moonphase():
    stage = "waxing"
    illumination = "34"

    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            moonphase_exists = check_moonphase(cursor, connection, stage, illumination)
            print(moonphase_exists)

            if not moonphase_exists:
                insert_into(cursor, connection, "moonphases", ["stage", "illumination"], [stage, illumination])

            rows = select_from(cursor, connection, "moonphases")
            print(rows)

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)



def main():
    test_date()


if __name__ == "__main__":
    main()

