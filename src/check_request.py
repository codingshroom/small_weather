import sqlite3

from src.database import select_from, insert_into
from apis.coordinates_api import coordinates_api_call
from apis.moon_api import moon_api_call
from apis.weather_api import weather_api_call


def open_database():
    try:
        with sqlite3.connect("data/database.db") as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()
            return cursor, connection

    except sqlite3.OperationalError as e:
        print("Failed to open database", e)
        return None, None


def request_data(table, profile_name, city_name, date):
    profileID = get_profile(profile_name)
    cityID = get_city(city_name)
    moonphase = get_moon(date)
    weather_data = get_weather(cityID, date)
    store_request(profileID, cityID, date)
    return joined_data


def get_profile(profile_name)
    # check DB for profile_name, if missing: insert into table 'profiles', return profileID
    return profileID


def get_city(city_name):
    # check DB for cityname, if missing: call coordinates_api, insert city, lat, lon to table 'cities', return cityID
    return cityID


def get_moon(date):
    # check DB via date, if missing: call moon_api, insert date + moonphase into dates & moonphases respectively, return moon_data
    return moon_data


def get_weather(cityID, date):
    # check DB for weather_data, if missing: get coordinates from table 'cities', call weather_api, return requested weather_data for city + date
    return weather_data


def store_request(profile, cityID, date):
    # insert request into table 'requests' if not already contained
    return



def main():
    cursor, connection = open_database()
    requested_data = request_data("cities", "Johnny", "Berlin", "2026-06-30")
    print(requested_data)


if __name__ == "__main__":
    main()

