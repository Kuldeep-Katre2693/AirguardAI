import pandas as pd
from backend.database import SessionLocal
from backend.models import AQIRecord
from backend.models import City


def load_aqi(city_name, csv_path):

    db = SessionLocal()

    city = db.query(City).filter(
        City.city_name == city_name
    ).first()

    df = pd.read_csv(csv_path)

    df["date"] = pd.to_datetime(df["date"]).dt.date

    for _, row in df.iterrows():

       record = AQIRecord(

          city_id=city.id,

          record_date=row["date"],

          aqi=row["aqi"],

          pm25=row["pm25"],

          pm10=row["pm10"],

          no2=row["no2"],

          so2=row["so2"],

          co=row["co"],

          o3=row["o3"]

        )

       db.add(record)

    db.commit()
    print(f"Successfully imported {len(df)} AQI records.")

    db.close()


if __name__ == "__main__":

    load_aqi(
        "Nagpur",
        "data/raw/aqi/nagpur_aqi.csv"
    )