import openmeteo_requests
import requests

import pandas as pd
from lat_lon_api import get_api_key, get_city, get_lat_lon_response, get_lat_lon


def get_weather_response_2(date, latitude, longitude):
    weather_url = "https://archive-api.open-meteo.com/v1/archive"
    weather_data = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "start_date": date,
            "end_date": date,
            "hourly": "temperature_2m",
        },
    ).json()

    times = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    return times, temperatures



def get_weather_response(lat, lon):
    openmeteo = openmeteo_requests.Client()

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
    }
    responses = openmeteo.weather_api(url, params = params)
    return responses[0]


def response_to_json(response):
    string_data = response.read().decode("utf-8")
    json_data = json.loads(string_data)
    return json_data



def main():
    api = get_api_key("WEATHER_API")
    city = get_city()
    response = get_lat_lon_response(api, city)
    latitude, longitude = get_lat_lon(response)
    times, temperatures = get_weather_response_2("2026-06-05", latitude, longitude)
    print("")
    for time, temperature in zip(times, temperatures):
        print(time, ": ", temperature)


if __name__ == "__main__":
    main()

