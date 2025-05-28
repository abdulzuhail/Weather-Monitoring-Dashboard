# 🌤️ Weather Monitoring Dashboard using Power BI

This project provides a comprehensive Power BI dashboard that visualizes **weather conditions and air quality levels** across major cities in Tamil Nadu, focusing on regions such as Nilgiris and Coimbatore.

![Weather Dashboard](https://github.com/abdulzuhail/Weather-Monitoring-Dashboard/blob/main/Weather%20Dashboard.png)

🎥 [Watch Dashboard Video](https://github.com/abdulzuhail/Weather-Monitoring-Dashboard/blob/main/Weather%20Monitoring.mp4)

---

## 📌 Project Objective

The goal of this project is to build an **interactive, insightful dashboard** that enables users to:

- Monitor temperature, humidity, Air Quality Index (AQI), and wind speed
- Compare weather parameters across cities and districts
- Identify pollution levels
- Enable city/district-specific filtering for decision-making

---

## 🧾 Data Source

- The data was collected from **local weather stations and air quality monitoring APIs**.
- Final dataset includes:
  - `City`
  - `District`
  - `Temperature (°C)`
  - `Humidity (%)`
  - `Air Quality Index (AQI)`
  - `Wind Speed (km/h)`
  - `Timestamp` (for time-based insights if needed)

---

## 🛠️ Tools Used

| Tool      | Purpose                            |
|-----------|------------------------------------|
| **Power BI** | Dashboard design and visualization |
| **MySQL**    | Data storage and filtering (local DB) |
| **SQL**      | Querying and cleaning data        |
| **Power BI Query Editor** | Data preprocessing and transformation |

---

## 📊 Key Visuals in Dashboard

### 1. **KPI Cards**
- Displays average values of:
  - 🌬️ Wind Speed
  - 🌡️ Temperature
  - 💧 Humidity
  - 🟡 Air Quality Index (AQI)

### 2. **Weather by Cities**
- A horizontal bar chart showing **maximum temperature** per city.
- Helps identify hottest areas.

### 3. **Temperature and Humidity Per Cities**
- Grouped bar chart comparing temperature vs humidity city-wise.
- Useful to detect correlation between heat and moisture.

### 4. **City-Wise Breakdown Table**
- A color-coded matrix showing:
  - City & District
  - Temperature, Humidity
  - AQI & Wind Speed
- Conditional formatting applied for quick heatmap analysis.

### 5. **Filters**
- Slicers for:
  - **City**
  - **Weather Condition**
  - **District**
- Allows tailored insights for specific regions.

---

## 🧠 Insights & Interpretation

- Cities like **Ketti** and **Mettupalayam** experience high maximum temperatures (~28.8°C).
- **Devala** shows extremely high humidity (~99%) and also a noticeable AQI (~12–14), indicating poor ventilation.
- **Coimbatore** shows varied data with good wind speed and relatively better air quality.
- The AQI distribution shows **concern in urban zones**, needing intervention.

---

## 📌 Next Steps / Enhancements

- Add **time series** data for weather trends over days.
- Integrate **forecasting** using Azure ML or Python.
- Trigger **alerts** for dangerous AQI zones.
- Embed dashboard into a website or public Power BI workspace.

---


