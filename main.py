from scripts.fetch_data import fetch_weather_data

def main():
    city = "Berlin"
    country = "DE"

    print("Fetching weather data...")
    weather_data = fetch_weather_data(city, country)

    if weather_data:
        print("Weather Data:", weather_data)
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
