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
    temperatures = weather_data["hourly"]["temperature_2m"]
    return temperatures


def weather_api_call(latitude, longitude, date="2026-06-05"):
    api_key = get_api_key("WEATHER_API")
    response = get_weather_response(date, latitude, longitude)
    temperatures = get_weather_data(response)
    return temperatures


def main():
    lat = 5
    lon = 3
    weather_data = weather_api_call(lat, lon, date.today())
    for i in range(len(weather_data)):
        print(f"hour: {i}  temp: {weather_data[i]}")


if __name__ == "__main__":
    main()

