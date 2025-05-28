# 🌦 Weather Monitoring Dashboard

![Weather Dashboard](https://github.com/abdulzuhail/Weather-Monitoring-Dashboard/blob/main/Weather%20Dashboard.png)

🎥 **[Watch Demo Video](https://github.com/abdulzuhail/Weather-Monitoring-Dashboard/blob/main/Weather%20Monitoring.mp4)**

---

## 📌 Project Overview

This project presents a **dynamic weather monitoring dashboard** developed using **Power BI**, which visually analyzes and tracks weather conditions across various cities in Tamil Nadu, India.

It is designed to offer real-time insights into important weather parameters such as:

- **Temperature (°C)**
- **Humidity (%)**
- **Wind Speed (m/s)**
- **Air Quality Index (AQI)** — *(AQI stands for Air Quality Index, a measure used to communicate how polluted the air currently is or how polluted it is forecast to become.)*

The goal of this dashboard is to support decision-making for weather-related planning and ensure public awareness by simplifying weather patterns into an interactive format.

---

## 📂 Data Collection & Processing

- Weather data was collected using a Python-based API script.
- Data was stored in **MySQL** for structured querying and transformation.
- Key transformations and cleaning steps included:
  - Handling `NULL` values in temperature, humidity, and AQI.
  - Removing duplicate or invalid rows.
  - Calculating **average**, **maximum**, and **minimum** values across cities.

---

## 📊 Dashboard Features

### ✅ KPIs (Top Cards)
- **Average Wind Speed**
- **Average Temperature**
- **Average Humidity**
- **Average AQI (Air Quality Index)**

### 📈 Visualizations

1. **Weather by Cities (Bar Chart)**  
   Compares the highest recorded temperatures across cities.  
   Easily identifies heat-prone areas.

2. **Temperature and Humidity per City (Clustered Column Chart)**  
   Shows the contrast between average humidity and temperature.  
   Helps in analyzing correlations (e.g., high humidity with moderate temperatures).

3. **City-Wise Breakdown Table**  
   Detailed city-level stats including district, temperature, humidity, AQI, and wind speed.  
   Conditional formatting for quick interpretation (e.g., high AQI marked in red).

4. **Filters**
   - **City Filter**: Focus on a specific city.
   - **Weather-wise Filter**: Filter by weather conditions (e.g., high humidity).
   - **District Filter**: Analyze districts like Nilgiris, Coimbatore, etc.

---

## 🧠 Insights

- **Highest Temperature**: Ketti and Mettupalayam (28.8°C)
- **Lowest AQI (Better Air Quality)**: Coimbatore (AQI 1)
- **Most Humid City**: Devala (99%)
- **Windiest City**: Pollachi (10.66 m/s)

This allows quick decision-making for people in agriculture, transport, event planning, or public health.

---

## 🛠 Tools Used

- **Power BI** – Dashboard visualization
- **Python** – Data collection via weather APIs
- **MySQL** – Data storage and SQL-based cleaning
- **GitHub** – Code and dashboard hosting
