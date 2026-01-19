from minio import Minio
import os
from dotenv import load_dotenv

from storage.read_minio import read_one_weather_object
from etl.transform_weather import transform_weather
from etl.load_weather import load_weather

load_dotenv()

client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

BUCKET = os.getenv("MINIO_BUCKET")

def run_etl_all():
    objects = client.list_objects(BUCKET, recursive=True)

    for obj in objects:
        raw = read_one_weather_object(obj.object_name)
        transformed = transform_weather(raw)
        transformed["source_object"] = obj.object_name

        load_weather(transformed)

if __name__ == "__main__":
    run_etl_all()
    print("Automated ETL completed")