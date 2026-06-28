from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import WeatherRecord

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
def get_weather(limit: int = 10):

    db: Session = SessionLocal()

    try:
        weather = (
            db.query(WeatherRecord)
            .limit(limit)
            .all()
        )

        return weather

    finally:
        db.close()