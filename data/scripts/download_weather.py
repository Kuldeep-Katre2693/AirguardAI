import requests
import pandas as pd
import os

LAT = 21.1458
LON = 79.0882

url = (
    f"https://archive-api.open-meteo.com/v1/archive"
    f"?latitude={LAT}"
    f"&longitude={LON}"
    f"&start_date=2024-01-01"
    f"&end_date=2024-12-31"
    f"&daily=temperature_2m_mean,relative_humidity_2m_mean,"
    f"precipitation_sum,wind_speed_10m_max"
    f"&timezone=Asia/Kolkata"
)

response = requests.get(url)

data = response.json()["daily"]

df = pd.DataFrame(data)

os.makedirs("../raw/weather", exist_ok=True)

print(df.head())
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "raw" / "weather"

RAW_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(RAW_DIR/"nagpur_weather.csv", index=False)

print("Weather data downloaded successfully.")