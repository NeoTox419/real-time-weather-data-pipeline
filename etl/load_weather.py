import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DB_URL)

def load_weather(transformed_data: dict):
    query = text("""
        INSERT INTO weather_fact (
            city,
            temperature_c,
            humidity,
            wind_speed,
            weather_timestamp,
            ingested_at
        )
        VALUES (
            :city,
            :temperature_c,
            :humidity,
            :wind_speed,
            :weather_timestamp,
            :ingested_at
        )
    """)

    with engine.begin() as conn:
        conn.execute(query, transformed_data)
