import sqlite3

from src.database import select_from, insert_into
from apis.coordinates_api import coordinates_api_call
from apis.moon_api import moon_api_call
from apis.weather_api import weather_api_call


def data_exists(cursor, connection, table, **data):
    '''
        How to use:
        data_exists(cursor, connection, table, **data)

        tablename           **data
        ------------------------------
        cities:             cityName
        dates:              date
        moonphases:         stage, illumination
        profiles:           profileName
        requests:           profileID, cityID, date
        weatherdata:        cityID, date, hour, temperature, rainProbability, rainAmount
    '''
    condition_string = " AND ".join(f"{key} = '{value}'" for key, value in data.items())
    exists = select_from(cursor, connection, table, columns=["1"], condition=condition_string)
    return bool(exists)


def prep_city(cityname):
    lat, lon = coordinates_api_call(cityname)
    return [lat, lon]


def prep_moon(timestamp):
    stage, illumination = moon_api_call(timestamp)
    return [stage, illumination]


def prep_weather(cityID, date, **data):
    lat, lon = request_data("cities", date=date, **data)
    temperatures = weather_api_call(lat, lon, date)
    return tempeartures


def api_selector(table, **data):
    match table:
        case "cities":
            return prep_city(**data)
        case "moonphases":
            return prep_moon(**data)
        case "weatherdata":
            return prep_weather(**data)
        case _:
            return None


def request_data(table, **data):
    '''
        how to use request_data(table, **data):

        table = cities:         **data = cityname
        table = moonphases:     **data = timestamp
        table = weatherdata:    **data = date, cityID
    '''
    try:
        with sqlite3.connect("data/test.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            # breakpoint()
            exists = data_exists(cursor, connection, table, **data)

            if not exists:
                api_call = api_selector(table, **data)
                columns = [key for key, _ in data.items()]
                values = [value for _, value in data.items()]
                if table == "weatherdata":
                    for i in range(len(weatherdata)):
                        temperature = weatherdata[i]
                        # columns add hour, temperature, rainProbability, rainAmount
                        # values add i, 1, 0, 0
                        # then:
                        insert_into(cursor, connection, table, columns, values)
                else:
                    # columns add data from api_call()
                    # values add data from api_call()
                    insert_into(cursor, connection, table, columns, values)

            rows = select_from(cursor, connection, table)
            return rows

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)



def main():
#    rows = request_data("weatherdata", cityID=2, date="2026-06-30", hour=3)
#    print(rows)
    weather = api_selector("weatherdata", cityID=1, date="2026-06-30", hour=3, temperature=1, rainProbability=0, rainAmount=0)
    print(weather)


if __name__ == "__main__":
    main()

