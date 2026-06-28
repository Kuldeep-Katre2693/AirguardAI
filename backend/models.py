from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from backend.database import Base

class City(Base):

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    city_name = Column(
        String,
        unique=True,
        nullable=False
    )

    state = Column(
        String,
        nullable=False
    )

    latitude = Column(
        Float
    )

    longitude = Column(
        Float
    )

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import relationship

class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    city_id = Column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False
    )

    record_date = Column(
        Date,
        nullable=False
    )

    temperature = Column(Float)
    humidity = Column(Float)
    rainfall = Column(Float)
    wind_speed = Column(Float)
    city = relationship("City")

class AQIRecord(Base):
     __tablename__ = "aqi_records"

     id = Column(
        Integer,
        primary_key=True,
        index=True
    )

     city_id = Column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False
    )

     record_date = Column(
        Date,
        nullable=False
    )

     aqi = Column(Float)
     pm25 = Column(Float)
     pm10 = Column(Float)
     no2 = Column(Float)
     so2 = Column(Float)
     co = Column(Float)
     o3 = Column(Float)
     city = relationship("City")

