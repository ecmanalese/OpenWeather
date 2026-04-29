import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
CITY_NAME = 'Manila'
COUNTRY_CODE = 'PH'

def get_geo_coordinates():
    API_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME},{COUNTRY_CODE}&limit=1&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(API_URL)
    return response.json()[0]['lat'], response.json()[0]['lon']

def get_weather_data():
    part = ''
    lat, lon = get_geo_coordinates()
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(API_URL)
    return response.json()

print(get_weather_data())