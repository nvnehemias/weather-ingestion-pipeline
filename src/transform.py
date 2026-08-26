import pandas as pd 

def transform_data(raw_records: list) -> pd.DataFrame:

    """
    
    Clean, reorder, and typecast raw API dictionary payloads into a DataFrame.
    
    """

    df = pd.DataFrame(raw_records)

    # Standardize column naming convention
    df = df.rename(columns = {

        "temperature": "temp_celsius",
        "windspeed": "wind_speed_kmh",
        "winddirection": "wind_direction_deg",
        "weathercode": "weather_code"

    })

    # Select and order required columns 
    columns_order = ["city", "temp_celsius", "wind_speed_kmh", "wind_direction_deg", "weather_code", "time", "ingested_at"]

    df = df[columns_order]

    # Enforce data types
    df["temp_celsius"] = df["temp_celsius"].astype(float)
    df["wind_speed_kmh"] = df["wind_speed_kmh"].astype(float)

    return df