import pandas as pd
import random
import json

# Simulate Wearable Data
def simulate_wearable_data():
    return {
        "heart_rate": random.randint(60, 140),
        "steps": random.randint(2000, 15000),
        "calories_burned": round(random.uniform(200, 800), 2),
        "SpO2": round(random.uniform(92, 100), 2),
        "sleep_hours": round(random.uniform(4, 8), 2)
    }

# Simulate API Data
def simulate_api_data():
    weather_data = ["Sunny", "Rainy", "High Humidity", "Polluted"]
    return {
        "weather": random.choice(weather_data),
        "air_quality": random.choice(["Good", "Moderate", "Unhealthy"])
    }

# Process Real-Time Data
def process_real_time_data(data_sources):
    data = {}
    if "Wearable Devices" in data_sources:
        data.update(simulate_wearable_data())
    if "External APIs" in data_sources:
        data.update(simulate_api_data())
    return pd.DataFrame([data])
