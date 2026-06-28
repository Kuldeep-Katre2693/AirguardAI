from fastapi import APIRouter, HTTPException

from ml.predict import predict

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


@router.get("/{city}")
def forecast(city: str, days: int = 5):

    try:

        result = predict(
            city=city,
            days=days
        )

        return result.to_dict(
            orient="records"
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