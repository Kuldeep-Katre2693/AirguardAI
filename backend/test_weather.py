from backend.database import SessionLocal
from backend.models import WeatherRecord

db = SessionLocal()

records = db.query(WeatherRecord).limit(5).all()

for r in records:

    print(

        r.record_date,

        r.temperature,

        r.humidity

    )