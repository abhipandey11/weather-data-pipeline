CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    windspeed FLOAT,
    humidity FLOAT,
    timestamp TIMESTAMP
);