from fastapi import APIRouter, Query, HTTPException
from app.models.weather import WeatherResponse
from app.services.weather_service import get_weather_from_api

router = APIRouter()

@router.get(
    "/weather",
    response_model=WeatherResponse
)
def get_weather(
    city: str = Query(..., min_length=2, description="City name or code")
):
    try:
        data = get_weather_from_api(city)

        today = data["days"][0]

        return WeatherResponse(
            city=city,
            temperature=today["temp"],
            description=today["conditions"]
        )

    except ValueError:
        raise HTTPException(status_code=404, detail="City not found")

    except Exception:
        raise HTTPException(status_code=503, detail="Weather service unavailable")
