import pandas as pd

from backend.database import SessionLocal
from backend.models import City, WeatherRecord

db = SessionLocal()

city = db.query(City).filter(
    City.city_name == "Nagpur"
).first()

df = pd.read_csv("data/raw/weather/nagpur_weather.csv")

df["time"] = pd.to_datetime(df["time"]).dt.date

for _, row in df.iterrows():

    weather = WeatherRecord(

        city_id=city.id,

        record_date=row["time"],

        temperature=row["temperature_2m_mean"],

        humidity=row["relative_humidity_2m_mean"],

        rainfall=row["precipitation_sum"],

        wind_speed=row["wind_speed_10m_max"]

    )

    db.add(weather)

db.commit()

db.close()

print("Weather Imported")