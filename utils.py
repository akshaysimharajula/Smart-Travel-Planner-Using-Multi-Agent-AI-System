import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY not found in environment")

def fetch_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    res = requests.get(url).json()

    if res.get("cod") != 200:
        return "Weather data not available"

    return f"{res['main']['temp']}°C, {res['weather'][0]['description']}"