CREATE TABLE IF NOT EXISTS weather_fact (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature_c REAL,
    humidity INTEGER,
    wind_speed REAL,
    weather_timestamp TIMESTAMP,
    ingested_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_weather_city_time
ON weather_fact (city, weather_timestamp);
