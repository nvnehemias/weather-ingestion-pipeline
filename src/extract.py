import requests 
from datetime import datetime 

def extract_weather(city: str, lat: float, lon: float) -> dict:
    """
    
    Fetch current weather metrics from Open-Meteo API for a given location 

    """

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url, timeout = 10)
    response.raise_for_status()

    data = response.json()["current_weather"]
    data["city"] = city 
    data["ingested_at"] = datetime.utcnow().isoformat()

    return data 