import sys
import requests

from dotenv import load_dotenv
import os


def get_api_key():
    load_dotenv()

    api_key = os.getenv("WEATHER_API", "")

    if not api_key:
        raise RuntimeError("WEATHER_API not set. Check .env")
    
    return api_key


def get_city():
    if len(sys.argv) > 1:
        city = sys.argv[1]
    else:
        city = "Accra"
    return city


def get_response(api_key, city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q":city, 
        "limit":1, 
        "appid":api_key
    }

    response = requests.get(url, params=params)
    return response


def get_lat_lon(response):
    data = response.json()

    lat = data[0]["lat"]
    lon = data[0]["lon"]

    return lat, lon


def main():
    api_key = get_api_key()
    city = get_city()
    response = get_response(api_key, city)
    lat, lon = get_lat_lon(response)
    print(f"{city=}")
    print(f"{lat=}")
    print(f"{lon=}")


if __name__ == "__main__":
    main()

