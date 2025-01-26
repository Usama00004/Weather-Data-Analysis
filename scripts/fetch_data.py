import requests
from scripts.config import API_KEY, BASE_URL


def fetch_weather_data(city, country):
    """Fetch weather data from the API for a specific city and country."""
    url = f"{BASE_URL}/weather?q={city},{country}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None