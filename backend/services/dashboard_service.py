from backend.database import SessionLocal
from backend.models import City, WeatherRecord, AQIRecord
from backend.services.forecast_service import forecast_service


def dashboard_service(city_name: str):

    db = SessionLocal()

    city = (
        db.query(City)
        .filter(City.city_name == city_name)
        .first()
    )

    if city is None:
        db.close()
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

    print(city.id)

    db.close()
    
    return {
      "city": city.city_name,
      "aqi": aqi.aqi,
      "temperature": weather.temperature,
      "humidity": weather.humidity,
      "wind_speed": weather.wind_speed,
      "rainfall": weather.rainfall,
      "record_date": str(weather.record_date),
      "forecast": forecast
}