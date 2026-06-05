import requests

from lat_lon_api import get_api_key, get_city, get_lat_lon_response, get_lat_lon


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


def get_times_temps(response):
    weather_data = response.json()
    times = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    return times, temperatures


def response_to_json(response):
    string_data = response.read().decode("utf-8")
    json_data = json.loads(string_data)
    return json_data



def main():
    api = get_api_key("WEATHER_API")
    city = get_city()
    response = get_lat_lon_response(api, city)
    latitude, longitude = get_lat_lon(response)
    response = get_weather_response("2026-06-05", latitude, longitude)
    times, temperatures = get_times_temps(response)
    print("")
    for hour, temp in zip(times, temperatures):
        print(hour, ": ", temp)


if __name__ == "__main__":
    main()

