import pandas as pd
from src.database import engine 
from src.constants import parquet_path 

def load_data(df: pd.DataFrame):

    """
    
    Load validated DataFrame into PostgreSQL table and export Parquet backup.
    
    """

    # 1. Store in PostgreSQL database table
    df.to_sql("stg_weather_current", engine, if_exists = "append", index = False)
    print(f" Sucessfully appended {len(df)} rows to PostgreSQL table 'stg_weather_current'.")

    # 2. Export local Parquet snapshot
    df.to_parquet(parquet_path, index = False)
    print(f"Sucessfully written snapshot to '{parquet_path}'. ")
    
