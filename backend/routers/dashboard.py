from fastapi import APIRouter, HTTPException

from backend.services.dashboard_service import dashboard_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/{city}")
def get_dashboard(city: str):

    try:
        return dashboard_service(city)

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )