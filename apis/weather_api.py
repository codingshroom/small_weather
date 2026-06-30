from datetime import date
import requests

from apis.get_api_key import get_api_key
from apis.coordinates_api import coordinates_api_call


def get_weather_response(date, latitude, longitude):
    weather_url = "https://archive-api.open-meteo.com/v1/archive"
    response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "start_date": date,
            "end_date": date,
            "hourly": "temperature_2m",
        },
    )
    return response


def get_weather_data(response):
    weather_data = response.json()
    times = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    return times, temperatures


def weather_api_call(date="2026-06-05", city=None):
    api_key = get_api_key("WEATHER_API")
    latitude, longitude = coordinates_api_call(city)
    response = get_weather_response(date, latitude, longitude)
    times, temperatures = get_weather_data(response)
    return zip(times, temperatures)


def main():
    weather_data = weather_api_call(date.today())
    for time, temp in weather_data:
        print(time, temp)


if __name__ == "__main__":
    main()

