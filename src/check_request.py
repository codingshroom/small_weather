import sqlite3

from src.database import select_from, insert_into, ljoin_select
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


def request_data(cursor, connection, table, profileName, cityName, date):
    profileID = get_profile(profileName)
    cityID = get_city(cityName)
    moonphase = get_moon(date)
    weather_data = get_weather(cityID, date)
    store_request(profileID, cityID, date)
    return joined_data


def get_profile(cursor, connection, profileName)
    exists = select_from(cursor, connection, "profiles", columns=["1"], condition=f"profileName = {profileName}")
    if not exists:
        insert_into(cursor, connection, "profiles", ["profileName"], [profileName])
    profileID = select_from(cursor, connection, "profiles", columns=["profileID"], condition=f"profileName = {profileName}")
    return profileID


def get_city(cursor, connection, cityName):
    exists = select_from(cursor, connection, "cities", columns=["1"], condition=f"cityName = {cityName}")
    if not exists:
        lat, lon = coordinates_api_call(cityName)
        insert_into(cursor, connection, "profiles", ["cityName", "latitude", "longitude"], [cityName, lat, lon])
    cityID = select_from(cursor, connection, "cities", condition=f"cityName = {cityName}")
    return cityID, latitude, longitude


def get_moon(cursor, connection, date):
    exists = select_from(cursor, connection, "dates", columns=["1"], condition=f"date = {date}")
    if not exists:
        stage, illumination = moon_api_call(date)
        insert_into(cursor, connection, "moonphases", ["stage", "illumination"], [stage, illumination])
    moon_data = ljoin_select(cursor, connection, table="dates", join_table="moonphases", on="dates.moonID = moonphases.moonID", ["stage", "illumination"], [stage, illumination])
    return moon_data


def get_weather(cursor, connection, cityID, date):
    # check DB for weather_data, if missing: get coordinates from table 'cities', call weather_api, return requested weather_data for city + date
    exists = select_from(cursor, connection, "weatherdata", columns=["1"], condition=f"cityID = {cityID} AND date = {date}")
    if not exists:
        lat, lon = select_from(cursor, connection, "cities", columns=["latitude", "longitude"], condition=f"cityID = {cityID}")
        # weather api-call
        insert_into(cursor, connection, "weatherdata", [], [])
    weather_data = ljoin_select(cursor, connection, table="dates", join_table="moonphases", on="dates.moonID = moonphases.moonID", ["stage", "illumination"], [stage, illumination])
    return weather_data


def store_request(cursor, connection, profileID, cityID, date):
    exists = select_from(cursor, connection, "requests", columns=["1"], condition=f"profileID = {profileID} AND cityID = {cityID} AND date = {date}")
    if not exists:
        insert_into(cursor, connection, "requests", ["profileID", "cityID", "date"], [profileID, cityID, date])
    return



def main():
    cursor, connection = open_database()
    requested_data = request_data("cities", "Johnny", "Berlin", "2026-06-30")
    print(requested_data)


if __name__ == "__main__":
    main()

