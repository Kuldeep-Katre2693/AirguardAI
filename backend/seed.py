from backend.database import SessionLocal
from backend.models import City

db = SessionLocal()

cities = [

    City(
        city_name="Nagpur",
        state="Maharashtra",
        latitude=21.1458,
        longitude=79.0882
    ),

    City(
        city_name="Mumbai",
        state="Maharashtra",
        latitude=19.0760,
        longitude=72.8777
    ),

    City(
        city_name="Pune",
        state="Maharashtra",
        latitude=18.5204,
        longitude=73.8567
    ),

    City(
        city_name="Delhi",
        state="Delhi",
        latitude=28.6139,
        longitude=77.2090
    ),

    City(
        city_name="Bengaluru",
        state="Karnataka",
        latitude=12.9716,
        longitude=77.5946
    )

]

db.add_all(cities)

db.commit()