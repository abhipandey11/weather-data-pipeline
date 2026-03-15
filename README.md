# 🌦 Weather Data Pipeline & Dashboard

## Overview

This project builds an end-to-end **weather data pipeline and dashboard**.
Weather data is fetched from the Open-Meteo API, processed using Python, stored in a cloud PostgreSQL database (Supabase), and visualized through an interactive Streamlit dashboard.

The project demonstrates fundamental **data engineering and data analytics concepts**, including API ingestion, data transformation, database storage, and data visualization.

---

## Architecture
```text

Open-Meteo API
↓
Python ETL Pipeline
↓
Supabase PostgreSQL Database
↓
Streamlit Dashboard

```

---

## Features

* Collects weather data from the Open-Meteo API
* Supports multiple cities
* Stores historical weather data
* Python-based ETL pipeline
* Cloud PostgreSQL database using Supabase
* Interactive Streamlit dashboard
* Time-series visualization of temperature and wind speed

---

## Technologies Used

* Python
* PostgreSQL (Supabase)
* Streamlit
* Plotly
* Pandas
* Requests
* Psycopg2

---

## Project Structure

```text

weather-data-pipeline
│
├── dashboard
│   └── app.py
│
├── data_pipeline
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── cities.py
│   └── main.py
│
├── requirements.txt
├── render.yaml
└── README.md
```

---

## How the Pipeline Works

### Extract

Weather data is fetched from the Open-Meteo API for multiple cities.

### Transform

The API response is cleaned and structured using Python and Pandas.

### Load

The processed data is stored in a PostgreSQL database hosted on Supabase.

### Visualize

The Streamlit dashboard reads data from the database and displays weather trends and metrics.

---

## Running the Project Locally

### Install dependencies

pip install -r requirements.txt

### Set environment variable

DATABASE_URL=your_supabase_connection_string

Example:

postgresql://postgres:password@db.xxxxx.supabase.co:5432/postgres

### Run the ETL pipeline

python data_pipeline/main.py

### Start the dashboard

streamlit run dashboard/app.py

Open in browser:

http://localhost:8501

---

## Dashboard Features

* City selection filter
* Temperature trend visualization
* Wind speed trend visualization
* Latest weather metrics display

---

## Data Source

Weather data is provided by the **Open-Meteo API**
https://open-meteo.com/

---

## Deployment

The dashboard is deployed using **Render**, and the database is hosted on **Supabase**.

---

## Author

This project was developed as a **data engineering and data analytics portfolio project** demonstrating ETL pipelines, cloud databases, and data visualization.
