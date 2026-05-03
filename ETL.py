import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
CITY_NAME = 'Manila'
COUNTRY_CODE = 'PH'

def get_geo_coordinates():
    GEO_API_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME},{COUNTRY_CODE}&limit=5&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(GEO_API_URL)
    return response.json()[0]['lat'], response.json()[0]['lon']

def get_weather_data():
    lat, lon = get_geo_coordinates()
    WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
    response = requests.get(WEATHER_API_URL)
    return response.json()

def weather_data_to_dataframe(weather_data):
    df = pd.DataFrame({
        'city': weather_data['name'],
        'country': weather_data['sys']['country'],
        'measurement_unit': 'Metric',
        'temperature': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
        'temp_max': weather_data['main']['temp_max'],
        'temp_min': weather_data['main']['temp_min'],
        'pressure_hPa': weather_data['main']['pressure'],
        'humidity_': weather_data['main']['humidity'],
        'weather_description': weather_data['weather'][0]['description']
    }, index=[0])
    return df
    
#print(get_weather_data())
print(weather_data_to_dataframe(get_weather_data()))