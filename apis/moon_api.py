import time
import json
import http.client
from lalo import get_api_key

from dotenv import load_dotenv


def get_response(api_key, timestamp=int(time.time())):
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


def get_moon(response):
    string_data = response.read().decode("utf-8")
    json_data = json.loads(string_data)
    moon_data = json_data["moon"]
    stage = moon_data["stage"]
    illumination = moon_data["illumination"]
    emoji = moon_data["emoji"]
    return stage, illumination, emoji


def main():
    api_key = get_api_key("MOON_API")
    response = get_response(api_key)
    print(get_moon(response))


if __name__ == "__main__":
    main()

