from scripts.fetch_data import fetch_weather_data
from scripts.process_data import process_weather_data
from scripts.export_data import insert_data_into_snowflake


def main():

    print("Fetching weather data...")
    fetch_weather_data()

    print("transforming weather data...")   
    process_weather_data()

    print("Exporting transformed data to snowflake...")
    insert_data_into_snowflake()  

   
if __name__ == "__main__":
    main()
