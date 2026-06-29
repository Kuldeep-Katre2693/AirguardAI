from fastapi import APIRouter, HTTPException

from backend.services.forecast_service import forecast_service

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


@router.get("/{city}")
def forecast(city: str, days: int = 5):

    try:
        return forecast_service(
            city=city,
            days=days
        )

    except FileNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )