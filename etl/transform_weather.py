from datetime import datetime

def transform_weather(raw_data: dict) -> dict:
    """
    Transform raw OpenWeather JSON into analytics-ready structure.
    """

    transformed = {
        "city": raw_data.get("name"),
        "temperature_c": raw_data.get("main", {}).get("temp"),
        "humidity": raw_data.get("main", {}).get("humidity"),
        "wind_speed": raw_data.get("wind", {}).get("speed"),
        "weather_timestamp": datetime.utcfromtimestamp(
            raw_data.get("dt")
        ).isoformat(),
        "ingested_at": raw_data.get("ingested_at")
    }
    return transformed