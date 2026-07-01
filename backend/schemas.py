from pydantic import BaseModel
from datetime import datetime


class CityResponse(BaseModel):
    id: int
    city_name: str
    state: str
    latitude: float
    longitude: float

    model_config = {
        "from_attributes": True
    }


class WeatherResponse(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    rainfall: float
    record_date: str


class AirQualityResponse(BaseModel):
    aqi: float


class ForecastResponse(BaseModel):
    ds: datetime
    yhat: float
    yhat_lower: float
    yhat_upper: float

class DashboardResponse(BaseModel):
    city: CityResponse
    weather: WeatherResponse
    air_quality: AirQualityResponse
    forecast: list[ForecastResponse]