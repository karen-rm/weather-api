import requests
from app.config import settings

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def get_weather_from_api(city: str) -> dict:
    response = requests.get(
        f"{BASE_URL}/{city}",
        params={
            "unitGroup": "metric",
            "key": settings.visual_crossing_api_key,
            "contentType": "json"
        },
        timeout=10
    )

    if response.status_code == 404:
        raise ValueError("City not found")

    if response.status_code != 200:
        raise RuntimeError("Weather provider error")

    return response.json()
