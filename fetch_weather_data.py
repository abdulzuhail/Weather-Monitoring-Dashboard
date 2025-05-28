import requests
import pandas as pd
import mysql.connector
from datetime import datetime, timezone
import os
import schedule
import time

API_KEY = "key"
csv_file = "data/weather_data.csv"

district_cities = {
    "Nilgiris": [
        "Ooty", "Coonoor", "Kotagiri", "Gudalur", "Lovedale",
        "Wellington", "Ketti", "Naduvattam", "Devala"
    ],
    "Coimbatore": [
        "Coimbatore", "Pollachi", "Mettupalayam", "Valparai"
    ]
}

def fetch_and_store_weather():
    print("⏳ Running scheduled weather data fetch...")

    db = mysql.connector.connect(
        host="localhost",
        user="username",
        password="Ur pwd",
        database="weather_db"
    )
    cursor = db.cursor()

    # Ensure table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district VARCHAR(50),
        city VARCHAR(50),
        timestamp DATETIME,
        temperature FLOAT,
        humidity INT,
        wind_speed FLOAT,
        weather_desc VARCHAR(100),
        pm2_5 FLOAT,
        pm10 FLOAT,
        aqi INT
    )
    """)

    all_data = []

    for district, cities in district_cities.items():
        for city in cities:
            print(f"📍 Fetching data for {city} ({district})")
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            try:
                weather_response = requests.get(weather_url, timeout=10)
                weather_response.raise_for_status()
                weather_data = weather_response.json()

                temperature = weather_data["main"]["temp"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]
                description = weather_data["weather"][0]["description"]
                timestamp = datetime.fromtimestamp(weather_data["dt"], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                lat = weather_data["coord"]["lat"]
                lon = weather_data["coord"]["lon"]

                air_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
                air_response = requests.get(air_url, timeout=10)
                air_response.raise_for_status()
                air_data = air_response.json()

                if not air_data.get("list"):
                    pm2_5 = pm10 = aqi = None
                else:
                    air_values = air_data["list"][0]
                    pm2_5 = air_values["components"]["pm2_5"]
                    pm10 = air_values["components"]["pm10"]
                    aqi = air_values["main"]["aqi"]

                row = {
                    "district": district,
                    "city": city,
                    "timestamp": timestamp,
                    "temperature": temperature,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "weather_desc": description,
                    "pm2_5": pm2_5,
                    "pm10": pm10,
                    "aqi": aqi
                }
                all_data.append(row)

                cursor.execute("""
                    INSERT INTO weather_data (
                        district, city, timestamp, temperature, humidity, wind_speed, weather_desc, pm2_5, pm10, aqi
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (district, city, timestamp, temperature, humidity, wind_speed, description, pm2_5, pm10, aqi))
                db.commit()

            except requests.exceptions.RequestException as e:
                print(f"❌ Error fetching data for {city}: {e}")
                continue
            except Exception as e:
                print(f"⚠️ Unexpected error for {city}: {e}")
                continue

    # Save to CSV
    df = pd.DataFrame(all_data)
    write_header = not os.path.isfile(csv_file)
    df.to_csv(csv_file, mode='a', index=False, header=write_header)

    print(f"✅ Data saved to MySQL and CSV at '{csv_file}'")

    cursor.close()
    db.close()

# Schedule the job to run every hour
schedule.every(5).minutes.do(fetch_and_store_weather)

print("🔁 Scheduler started. Fetching weather data every 5 minutes...")

# Run the scheduled task
while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute
