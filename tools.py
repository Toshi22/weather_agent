import requests
import os
from langchain_classic.tools import tool
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@tool
def get_weather(city: str) -> str:
    """Get current weather for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Could not fetch weather data."
    
    data = response.json()
    
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    return f"""
    Weather in {city}:
    Temperature: {temp}°C
    Condition: {description}
    Humidity: {humidity}%
    """