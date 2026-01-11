# Real-Time Weather Data Pipeline

A real-time data engineering project that ingests live weather data from the OpenWeather API, stores raw JSON data in MinIO (S3-compatible), performs ETL transformations, loads processed data into PostgreSQL, and visualizes insights using Power BI.

## Tech Stack
- Python
- OpenWeather API
- MinIO (S3)
- PostgreSQL
- Power BI

## Architecture
Weather API → Python Ingestion → MinIO → ETL → PostgreSQL → Power BI