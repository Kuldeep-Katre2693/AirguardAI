from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import City
from backend.schemas import CityResponse

router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


@router.get("/", response_model=list[CityResponse])
def get_cities():

    db: Session = SessionLocal()

    try:
        cities = db.query(City).all()
        return cities

    finally:
        db.close()