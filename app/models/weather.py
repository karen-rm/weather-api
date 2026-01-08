from pydantic import BaseModel, Field

class WeatherResponse(BaseModel):
    city: str = Field(..., description="City name or code")
    temperature: float = Field(..., description="Temperature in Celsius")
    description: str = Field(..., description="Weather condition description")
