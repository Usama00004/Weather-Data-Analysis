from scripts.fetch_data import fetch_weather_data


def main():
    city = "Berlin"
    country = "DE"

    print("Fetching weather data...")
    # weather_data = fetch_weather_data(city, country)
    fetch_weather_data()
   
if __name__ == "__main__":
    main()
