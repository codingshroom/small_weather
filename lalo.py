import sys
import requests

from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY", "")

if not API_KEY:
    raise RuntimeError("API_KEY not set. Check .env")


if len(sys.argv) > 0:
    city = sys.argv[0]
else:
    city = "Accra"

url = f"http://api.openweathermap.org/geo/1.0/direct"

r = requests.get(url, params={"q":city, "limit":1, "appid": API_KEY})
data = r.json()

lat = data[0]["lat"]
lon = data[0]["lon"]

print(lat, lon)
