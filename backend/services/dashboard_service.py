from backend.database import SessionLocal
from backend.models import City, WeatherRecord, AQIRecord
from backend.services.forecast_service import forecast_service
from backend.schemas import (
    DashboardResponse,
    CityResponse,
    WeatherResponse,
    AirQualityResponse,
    ForecastResponse,
)


def dashboard_service(city_name: str):

    db = SessionLocal()

    try:

        city = (
            db.query(City)
            .filter(City.city_name == city_name)
            .first()
        )

        if city is None:
            raise Exception("City not found")

        weather = (
            db.query(WeatherRecord)
            .filter(WeatherRecord.city_id == city.id)
            .order_by(WeatherRecord.record_date.desc())
            .first()
        )

        aqi = (
            db.query(AQIRecord)
            .filter(AQIRecord.city_id == city.id)
            .order_by(AQIRecord.record_date.desc())
            .first()
        )

        forecast = forecast_service(
            city=city.city_name,
            days=5
        )

        city_data = CityResponse(
            id=city.id,
            city_name=city.city_name,
            state=city.state,
            latitude=city.latitude,
            longitude=city.longitude,
        )

        weather_data = WeatherResponse(
            temperature=weather.temperature,
            humidity=weather.humidity,
            wind_speed=weather.wind_speed,
            rainfall=weather.rainfall,
            record_date=str(weather.record_date),
        )

        air_quality_data = AirQualityResponse(
            aqi=aqi.aqi
        )

        forecast_data = [
            ForecastResponse(**item)
            for item in forecast
        ]

        return DashboardResponse(
            city=city_data,
            weather=weather_data,
            air_quality=air_quality_data,
            forecast=forecast_data,
        )

    finally:
        db.close()