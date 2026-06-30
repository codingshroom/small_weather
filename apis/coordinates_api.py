import sys
import requests

from apis.get_api_key import get_api_key


def get_city(city=None):
    if not city:
        if len(sys.argv) > 1:
            city = sys.argv[1]
        else:
            city = "Accra"
    return city


def get_coordinates_response(api_key, city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q":city, 
        "limit":1, 
        "appid":api_key
    }

    response = requests.get(url, params=params)
    return response


def get_coordinates(response):
    data = response.json()

    latitude = data[0]["lat"]
    longitude = data[0]["lon"]

    return latitude, longitude


def coordinates_api_call(city=None):
    api_key = get_api_key("WEATHER_API")
    city = get_city(city)
    response = get_coordinates_response(api_key, city)
    latitude, longitude = get_coordinates(response)
    return latitude, longitude



def main():
    lat, lon = coordinates_api_call("Berlin")
    print(lat, lon)


if __name__ == "__main__":
    main()

