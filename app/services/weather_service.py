import httpx
from app.config import settings

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

async def get_weather_from_api(city: str) -> dict:
    params = {
        "unitGroup": "metric",
        "key": settings.visual_crossing_api_key,
        "contentType": "json"
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(f"{BASE_URL}/{city}", params=params)

    if response.status_code == 404:
        raise ValueError("City not found")

    response.raise_for_status()  # Maneja 401, 429, 500, etc.

    return response.json()
