import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw" / "aqi"
RAW_DIR.mkdir(parents=True, exist_ok=True)

LATITUDE = 21.1458
LONGITUDE = 79.0882

START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={LATITUDE}"
    f"&longitude={LONGITUDE}"
    f"&start_date={START_DATE}"
    f"&end_date={END_DATE}"
    "&hourly=pm10,pm2_5,carbon_monoxide,"
    "nitrogen_dioxide,sulphur_dioxide,ozone,"
    "european_aqi"
)
print("Connecting to Open-Meteo API...")

response = requests.get(URL)

print("Status Code:", response.status_code)
data = response.json()

print(data.keys())
print(data["hourly"].keys())
hourly = data["hourly"]

df = pd.DataFrame({
    "date": hourly["time"],
    "pm10": hourly["pm10"],
    "pm25": hourly["pm2_5"],
    "co": hourly["carbon_monoxide"],
    "no2": hourly["nitrogen_dioxide"],
    "so2": hourly["sulphur_dioxide"],
    "o3": hourly["ozone"],
    "aqi": hourly["european_aqi"]
})
print(df.head())
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Keep only the date (remove time)
df["date"] = df["date"].dt.date
daily_df = df.groupby("date").mean().reset_index()
print(daily_df.head())
csv_path = RAW_DIR / "nagpur_aqi.csv"

daily_df.to_csv(
    csv_path,
    index=False
)

print(f"\nAQI data saved successfully!")

print(csv_path)