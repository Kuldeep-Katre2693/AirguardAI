from fastapi import FastAPI

from backend.routers.cities import router as cities_router
from backend.routers.weather import router as weather_router
from backend.routers.forecast import router as forecast_router

app = FastAPI(
    title="AirGuard AI",
    version="1.0.0"
)

app.include_router(cities_router)
app.include_router(weather_router)
app.include_router(forecast_router)

@app.get("/")
def home():
    return {
        "message": "AirGuard AI Backend Running",
        "status": "healthy"
    }