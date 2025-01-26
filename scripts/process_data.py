import os
import pandas as pd

def process_weather_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_weather_data.csv')
    df_to_transform = pd.read_csv(os.path.abspath(file_path))
    
    # Apply transformations to 'time' and 'date' columns
    df_to_transform['time'] = df_to_transform['time'].apply(lambda x: x.split('T')[1])
    df_to_transform['date'] = df_to_transform['date'].apply(lambda x: x.split('T')[0])
    
    # Specify the path for the new CSV file
    output_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_weather_data.csv')
    
    # Write the transformed DataFrame to a new CSV file
    df_to_transform.to_csv(output_file, index=False)
    
    print(f"Transformed data has been written to '{output_file}'.")
