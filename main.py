from scripts.fetch_data import fetch_weather_data
from scripts.process_data import process_weather_data


def main():

    print("Fetching weather data...")
    fetch_weather_data()

    print("transforming weather data...")   
    process_weather_data()
   
if __name__ == "__main__":
    main()
