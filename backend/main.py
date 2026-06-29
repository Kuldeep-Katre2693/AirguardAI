from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.cities import router as cities_router
from backend.routers.weather import router as weather_router
from backend.routers.forecast import router as forecast_router
from backend.routers.dashboard import router as dashboard_router

app = FastAPI(
    title="AirGuard AI",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cities_router)
app.include_router(weather_router)
app.include_router(forecast_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "AirGuard AI Backend Running",
        "status": "healthy"
    }