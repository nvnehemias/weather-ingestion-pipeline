from src.constants import cities
from src.extract import extract_weather 
from src.transform import transform_data 
from src.quality import validate_quality 
from src.load import load_data 

def run_pipeline():
    print("Starting Weather Data Pipeline...")
    raw_data = []

    # Step 1: Extract
    for city, coords in cities.items():
        print(f"Fetching data for {city}")
        record = extract_weather(city, coords["lat"],coords["long"])
        raw_data.append(record)

    # Step 2: Transform
    df_clean = transform_data(raw_data)

    # Step 3: Data Quality Assertion
    validate_quality(df_clean)

    # Step 4: Load
    load_data(df_clean)

    print("Pipeline finished cleanly!")


if __name__ == "__main__":
    run_pipeline()
