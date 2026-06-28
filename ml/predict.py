import os
import joblib
import pandas as pd

MODELS_DIR = "ml/artifacts/models"


def predict(city: str = "nagpur", days: int = 5):

    model_path = os.path.join(
        MODELS_DIR,
        f"{city.lower()}.pkl"
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"No trained model found for {city}"
        )

    model = joblib.load(model_path)

    future = model.make_future_dataframe(
        periods=days
    )

    forecast = model.predict(future)

    result = forecast[
        [
            "ds",
            "yhat",
            "yhat_lower",
            "yhat_upper"
        ]
    ].tail(days)

    return result