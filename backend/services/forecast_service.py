def get_forecast():
    forecast = predict(days=5)
    aqi = forecast.iloc[-1]["yhat"]
    risk = calculate_risk(aqi)
    category = get_aqi_category(aqi)
    return {
        "forecast": forecast.to_dict(),
        "category": category,
        "risk": risk,
        "recommendation": recommendation(aqi)
    }

@app.get("/forecast/{city}")

def forecast(city:str):

    return forecast_service(city)