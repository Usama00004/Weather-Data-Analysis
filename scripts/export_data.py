import os
import snowflake.connector
import pandas as pd


def insert_data_into_snowflake():
    # Snowflake connection parameters
    conn = snowflake.connector.connect(
        user='',
        password='',
        account='',
        warehouse='COMPUTE_WH',
        database='WEATHER_DATABASE',
        schema='PUBLIC',
        role='ACCOUNTADMIN'
    )

    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Read the transformed data CSV file
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_weather_data.csv')
        df_to_export = pd.read_csv(os.path.abspath(file_path))

        # Iterate over the DataFrame rows
        for _, row in df_to_export.iterrows():
            # Parameterized query for safe insertion
            query = """
                INSERT INTO WEATHER_DATA (latitude, longitude, time, date, temperature, windspeed, winddirection)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            # Execute the query with parameters
            cursor.execute(query, (
                row['latitude'],
                row['longitude'],
                row['time'],
                row['date'],
                row['temperature'],
                row['windspeed'],
                row['winddirection']
            ))

        print("Data inserted successfully into Snowflake.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


insert_data_into_snowflake()
