import psycopg2
import os

def load_data(df):

    conn = psycopg2.connect(os.getenv("DATABASE_URL"))

    cur = conn.cursor()

    for index, row in df.iterrows():

        cur.execute("""INSERT INTO weather_data(city, latitude, longitude, temperature, windspeed, weather_time)
        VALUES (%s, %s, %s, %s, %s, %s)""", (
        row["city"],
        row["latitude"],
        row["longitude"],
        row["temperature"],
        row["windspeed"],
        row["weather_time"]
   ))

    conn.commit()

    cur.close()
    conn.close()