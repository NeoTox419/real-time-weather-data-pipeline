import json
import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

BUCKET = os.getenv("MINIO_BUCKET")

def read_one_weather_object(object_name: str) -> dict:
    response = client.get_object(BUCKET, object_name)
    try:
        data = json.loads(response.read().decode("utf-8"))
        return data
    finally:
        response.close()
        response.release_conn()
