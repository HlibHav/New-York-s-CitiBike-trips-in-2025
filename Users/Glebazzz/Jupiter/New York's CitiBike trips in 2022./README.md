# New York's CitiBike Weather Analysis 2024

A comprehensive analysis of New York City's CitiBike trip data integrated with weather information from the Open-Meteo API for the year 2024.

## 📊 Project Overview

This project combines CitiBike trip data with historical weather data to analyze patterns and correlations between weather conditions and bike-sharing usage in New York City. The analysis covers data from December 2023 through December 2024.

## 🗂️ Data Sources

### CitiBike Trip Data
- **Source**: Jersey City CitiBike trip data (JC-YYYYMM-citibike-tripdata.csv)
- **Period**: December 2023 - December 2024
- **Format**: CSV files with trip details including start/end times, stations, and user types

### Weather Data
- **Source**: [Open-Meteo Historical Weather API](https://open-meteo.com/)
- **Location**: LaGuardia Airport, NYC (40.7769°N, 73.8740°W)
- **Variables**: Temperature, precipitation, wind speed, weather conditions
- **Period**: January 1, 2024 - December 31, 2024

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.12+
- Virtual environment (recommended)

### Installation

1. **Activate the virtual environment**:
   ```bash
   source citibike_weather_env/bin/activate
   ```

2. **Verify required packages** (already installed in the environment):
   - pandas (2.0.3)
   - numpy
   - requests
   - matplotlib
   - jupyter

3. **Start Jupyter Lab**:
   ```bash
   jupyter lab
   ```

## 📁 Project Structure

```
├── README.md                              # Project documentation
├── Plan.md                                # Project planning document
├── citibike_weather_analysis_2024.ipynb   # Main analysis notebook
├── citibike_weather_env/                  # Python virtual environment
├── JC-202312-citibike-tripdata.csv       # Dec 2023 trip data
├── JC-202401-citibike-tripdata.csv       # Jan 2024 trip data
├── JC-202402-citibike-tripdata.csv       # Feb 2024 trip data
├── ... (monthly files through Dec 2024)
├── weather_data_2024_openmeteo.csv       # Processed weather data
└── citibike_weather_merged_2024.csv      # Merged trip and weather data
```

## 🚀 Usage

### Running the Analysis

1. **Open the main notebook**:
   ```bash
   jupyter lab citibike_weather_analysis_2024.ipynb
   ```

2. **Run all cells** to:
   - Load and process CitiBike trip data
   - Fetch weather data from Open-Meteo API
   - Merge datasets by date
   - Generate visualizations and insights
   - Export processed data

### Key Features

- **Data Integration**: Automatically merges trip data with weather conditions
- **Weather API Integration**: Fetches real-time historical weather data
- **Comprehensive Analysis**: Trip patterns, weather correlations, seasonal trends
- **Visualizations**: Charts showing weather impact on bike usage
- **Data Export**: Saves processed datasets for further analysis

## 📈 Analysis Highlights

The notebook provides insights into:
- **Seasonal Patterns**: How bike usage varies throughout the year
- **Weather Impact**: Correlation between weather conditions and trip frequency
- **Daily Trends**: Peak usage times under different weather conditions
- **Station Analysis**: Popular stations and weather-dependent usage patterns

## 🌐 API Information

**Open-Meteo Historical Weather API**
- **Endpoint**: `https://archive-api.open-meteo.com/v1/archive`
- **Documentation**: [Open-Meteo API Docs](https://open-meteo.com/en/docs/historical-weather-api)
- **Rate Limits**: Free tier with reasonable limits for research use
- **Data Quality**: High-quality reanalysis data suitable for research

## 📊 Output Files

- `weather_data_2024_openmeteo.csv`: Daily weather data for 2024
- `citibike_weather_merged_2024.csv`: Combined trip and weather data

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional analysis features.

## 📄 License

This project is for educational and research purposes. Please respect the terms of service for both CitiBike data and Open-Meteo API usage.