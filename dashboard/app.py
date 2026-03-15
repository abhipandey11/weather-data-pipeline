import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌤 Weather Data Dashboard")

# Database connection
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

query = """
SELECT city, temperature, windspeed, weather_time
FROM weather_data
ORDER BY weather_time
"""

df = pd.read_sql(query, conn)

# Sidebar city filter
cities = df["city"].unique()

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

city_df = df[df["city"] == selected_city]

latest = city_df.iloc[-1]

# Metrics
col1, col2 = st.columns(2)

col1.metric(
    "Temperature (°C)",
    latest["temperature"]
)

col2.metric(
    "Wind Speed (km/h)",
    latest["windspeed"]
)

# Temperature trend
st.subheader(f"Temperature Trend — {selected_city}")

fig = px.line(
    city_df,
    x="weather_time",
    y="temperature",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Wind trend
st.subheader(f"Wind Speed Trend — {selected_city}")

fig2 = px.line(
    city_df,
    x="weather_time",
    y="windspeed",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)