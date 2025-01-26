import requests
from scripts.config import URL
import pandas as pd
import os

def fetch_weather_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'country-coord.csv')
    df_coordinates = pd.read_csv(os.path.abspath(file_path))

    # Get the latitude and longitude columns
    latitudes = df_coordinates['Latitude']
    longitudes = df_coordinates['Longitude']
    country = df_coordinates['Country']

    # Base URL for Open-Meteo API
    weather_data_list = []
    
    # Loop through the latitudes and longitudes and call the API for each pair
    for latitude, longitude in zip(latitudes, longitudes):
        formatted_url = URL.format(latitude=latitude, longitude=longitude)
        response = requests.get(formatted_url)
        
        if response.status_code == 200:
            # Process the response if the request is successful
            data = response.json()
            current_weather = data.get('current_weather', {})
            if current_weather:
                weather_data = {  
                    'latitude': latitude,
                    'longitude': longitude,
                    'time': current_weather.get('time'),
                    'date' : current_weather.get('time'),
                    'temperature': current_weather.get('temperature'),
                    'windspeed': current_weather.get('windspeed'),
                    'winddirection': current_weather.get('winddirection')
                }
                weather_data_list.append(weather_data)
            else:
                print("Failed to fetch weather data.")    
             
        else:
            print(f"Failed to retrieve data for {latitude}, {longitude}. Status code: {response.status_code}")
    
    # Convert the weather data list into a DataFrame
    weather_df = pd.DataFrame(weather_data_list)

    # Specify the file path for the CSV
    output_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_weather_data.csv')

    # Write DataFrame to CSV
    weather_df.to_csv(output_file, index=False)

    print(f"Weather data has been written to '{output_file}'.")

