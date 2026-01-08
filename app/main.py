from fastapi import FastAPI
from app.routes import health, weather 

app = FastAPI(title="Weather API")

app.include_router(health.router)
app.include_router(weather.router)

