import json
import http.client

from apis.get_api_key import get_api_key


def get_moon_response(api_key, timestamp):
    url = "moon-phase.p.rapidapi.com"
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "moon-phase.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    connection = http.client.HTTPSConnection("moon-phase.p.rapidapi.com")
    connection.request("GET", f"/advanced?lat=0&lon=0&timestamp={timestamp}", headers=headers)

    response = connection.getresponse()
    
    return response


def get_moon_data(response):
    string_data = response.read().decode("utf-8")
    json_data = json.loads(string_data)
    moon_data = json_data["moon"]
    stage = moon_data["stage"]
    illumination = moon_data["illumination"]
    emoji = moon_data["emoji"]
    return [stage, illumination, emoji]


def moon_api_call(timestamp):
    api_key = get_api_key("MOON_API")
    response = get_moon_response(api_key, timestamp)
    moon_data_list = get_moon_data(response)
    return moon_data_list


def main():
    print(moon_api_call())


if __name__ == "__main__":
    main()

