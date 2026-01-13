import json
import os
import io
from datetime import datetime
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
BUCKET = os.getenv("MINIO_BUCKET")

client = Minio(
    MINIO_ENDPOINT,
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False
)

def upload_raw_weather(data, city):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    timestamp = datetime.utcnow().strftime("%H-%M-%S")

    object_name = (
        f"city={city.lower()}/"
        f"date={today}/"
        f"weather_{timestamp}.json"
    )

    payload = json.dumps(data).encode("utf-8")
    payload_stream = io.BytesIO(payload)

    client.put_object(
        bucket_name=BUCKET,
        object_name=object_name,
        data=payload_stream,
        length=len(payload),
        content_type="application/json"
    )

    print(f"Uploaded to MinIO: {object_name}")