from backend.database import SessionLocal

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

from fastapi import Depends
from sqlalchemy.orm import Session
from backend.dependencies import get_db

@app.get("/cities", response_model=list[CityResponse])

def get_cities(
    db: Session = Depends(get_db)
):

    return db.query(City).all()