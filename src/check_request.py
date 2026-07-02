import sqlite3

from src.database import select_from, insert_into
from apis.coordinates_api import coordinates_api_call
from apis.moon_api import moon_api_call
from apis.weather_api import weather_api_call


'''
    How to use data_exists():

    tablename           **kwargs
    ------------------------------
    cities:             cityName
    dates:              date
    moonphases:         stage, illumination
    profiles:           profileName
    requests:           profileID, cityID, date
    weatherdata:        cityID, date, hour, temperature, rainProbability, rainAmount
'''
def data_exists(cursor, connection, table, **data):
    condition_string = " AND ".join(f"{key} = '{value}'" for key, value in data.items())
    exists = select_from(cursor, connection, table, columns=["1"], condition=condition_string)
    return bool(exists)


def prep_city(cityname):
    lat, lon = coordinates_api_call(cityname)
    return [lat, lon]


def prep_moon(timestamp):
    return moon_api_call(timestamp)


def prep_weather(date, city):
    return weather_api_call(date, city)


def api_selector(table, *args):
    match table:
        case "cities":
            return prep_city(*args)
        case "moonphases":
            return prep_moon()
        case "weatherdata":
            return prep_weather()
        case _:
            return None


def request_data(table, **data):
    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            exists = data_exists(cursor, connection, table, **data)

            if not exists:
                api_call = api_selector(table)
                columns = [key for key, _ in data.items()]
                values = [value for _, value in data.items()]
                insert_into(cursor, connection, table, columns, values)

            rows = select_from(cursor, connection, table)
            return rows

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)



def main():
    rows = request_data("weatherdata", cityID=2, date="2026-06-30", hour=3)
    print(rows)


if __name__ == "__main__":
    main()

