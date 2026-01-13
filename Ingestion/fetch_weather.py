import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from storage.minio_upload import upload_raw_weather

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Kolkata"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

def fetch_weather():
    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()
    data["ingested_at"] = datetime.utcnow().isoformat()

    return data

if __name__ == "__main__":
    weather_data = fetch_weather()
    upload_raw_weather(weather_data, CITY)