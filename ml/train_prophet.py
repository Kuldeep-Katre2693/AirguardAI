import os
import joblib
import numpy as np
import pandas as pd
from prophet import Prophet
from sqlalchemy import text
from sklearn.metrics import mean_absolute_error, mean_squared_error
from backend.database import engine
import time
from backend.database import SessionLocal
from backend.models import City

CITY = "Nagpur"

db = SessionLocal()

city = db.query(City).filter(
    City.city_name == CITY
).first()

if city is None:
    raise Exception(f"{CITY} not found.")

CITY_ID = city.id

db.close()

ARTIFACTS_DIR = "ml/artifacts/models"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# -----------------------------
# Load Data
# -----------------------------
query = """
SELECT
    record_date,
    aqi
FROM merged_dataset
WHERE city_id = :city_id
ORDER BY record_date
"""

df = pd.read_sql(
    text(query),
    engine,
    params={"city_id": CITY_ID}
)

if df.empty:
    raise Exception("No training data found.")

# Prophet format
df.rename(
    columns={
        "record_date": "ds",
        "aqi": "y"
    },
    inplace=True
)

df["ds"] = pd.to_datetime(df["ds"])

print(df.head())

# -----------------------------
# Train / Test Split
# -----------------------------
split = int(len(df) * 0.8)

train = df.iloc[:split]

test = df.iloc[split:]
print("=" * 50)
print("Training Prophet Model")
print("=" * 50)
print(f"City : {CITY}")
print(f"Total Records : {len(df)}")
print(f"Train Records : {len(train)}")
print(f"Test Records : {len(test)}")
# -----------------------------
# Train
# -----------------------------
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)
start = time.time()
model.fit(train)
end = time.time()

print(f"\nTraining Time : {end-start:.2f} seconds")

# -----------------------------
# Evaluate
# -----------------------------
future = model.make_future_dataframe(
    periods=len(test)
)

forecast = model.predict(future)

pred = forecast.tail(len(test))

mae = mean_absolute_error(
    test["y"],
    pred["yhat"]
)

rmse = np.sqrt(
    mean_squared_error(
        test["y"],
        pred["yhat"]
    )
)

print("=" * 40)
print("Evaluation")
print("=" * 40)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
metrics = pd.DataFrame({
    "Metric": ["MAE", "RMSE"],
    "Value": [mae, rmse]
})

metrics.to_csv(
    "ml/artifacts/model_metrics.csv",
    index=False
)

# -----------------------------
# Retrain on Full Dataset
# -----------------------------
final_model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

final_model.fit(df)

# -----------------------------
# Save Model
# -----------------------------
model_path = os.path.join(
    ARTIFACTS_DIR,
    f"{CITY.lower()}.pkl"
)

joblib.dump(
    final_model,
    model_path
)

print(f"\nModel saved to: {model_path}")

# -----------------------------
# Forecast Next 5 Days
# -----------------------------
future = final_model.make_future_dataframe(
    periods=5
)

forecast = final_model.predict(
    future
)

print("\nNext 5-Day Forecast")

print(
    forecast[
        [
            "ds",
            "yhat",
            "yhat_lower",
            "yhat_upper"
        ]
    ].tail(5)
)
forecast.tail(5).to_csv(
    "ml/artifacts/forecast.csv",
    index=False
)