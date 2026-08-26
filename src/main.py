from src.constrants import cities
from src.extract import extract_weather 
from src.transform import transform_data 
from src.quality import validate_quality 
from src.load import load_data 

def run_pipeline():
    print("Starting Weather Data Pipeline...")
    raw_data = []

    # Step 1: Extract