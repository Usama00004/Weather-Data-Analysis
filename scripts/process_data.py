import os
import pandas as pd


def data_processor():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw_weather_data.csv')
    df_to_transform = pd.read_csv(os.path.abspath(file_path))


