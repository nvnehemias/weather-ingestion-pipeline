from src.database import engine 
from src.constants import parquet_path 

def load_data(df):
    df.to_sql("stg_weather_current", engine, if_exists = "append", index = False)
    df.to_parquet(parquet_path, index = False)
    