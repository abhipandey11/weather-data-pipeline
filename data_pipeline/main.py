from extract import get_weather_data
from transform import transform_weather_data
from load import load_data
from cities import CITIES

def run_pipeline():

    for city in CITIES:

        print(f"Fetching data for {city['name']}")

        raw_data = get_weather_data(city["lat"], city["lon"])

        clean_data = transform_weather_data(
            raw_data,
            city["name"],
            city["lat"],
            city["lon"]
        )

        load_data(clean_data)

    print("Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()