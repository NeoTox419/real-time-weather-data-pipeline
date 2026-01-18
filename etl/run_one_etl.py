from storage.read_minio import read_one_weather_object
from etl.transform_weather import transform_weather
from etl.load_weather import load_weather

OBJECT_NAME = "city=kolkata/date=2026-01-13/weather_17-00-47.json"

if __name__ == "__main__":
    raw = read_one_weather_object(OBJECT_NAME)
    transformed = transform_weather(raw)
    load_weather(transformed)

    print("ETL completed for one record")
