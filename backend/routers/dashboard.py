from fastapi import APIRouter, HTTPException
from backend.services.dashboard_service import dashboard_service
from backend.schemas import DashboardResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/{city}",
    response_model=DashboardResponse
)
def get_dashboard(city: str):
    try:
        return dashboard_service(city)
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )