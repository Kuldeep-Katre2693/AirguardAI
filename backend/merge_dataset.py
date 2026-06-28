merged = weather.merge(
    aqi,
    on=[
        "city_id",
        "record_date"
    ]
)
merged["month"] = merged["record_date"].dt.month

merged["day"] = merged["record_date"].dt.day

merged["week"] = merged["record_date"].dt.isocalendar().week

merged["year"] = merged["record_date"].dt.year

merged["aqi_7day_avg"] = merged["aqi"].rolling(7).mean()

merged["aqi_30day_avg"] = merged["aqi"].rolling(30).mean()