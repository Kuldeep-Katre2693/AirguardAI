from ml.predict import predict


def forecast_service(city: str, days: int = 5):
    """
    Generate AQI forecast for a city.
    """

    forecast = predict(
        city=city,
        days=days
    )

    return forecast.to_dict(
        orient="records"
    )