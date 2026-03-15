import pandas as pd

def transform_weather_data(data, city, lat, lon):

    current = data["current_weather"]

    transformed = {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weather_time": current["time"]
    }

    df = pd.DataFrame([transformed])

    return df