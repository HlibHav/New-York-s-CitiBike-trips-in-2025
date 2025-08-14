# New York's CitiBike Weather Analysis 2024

A comprehensive analysis of New York City's CitiBike trip data integrated with weather information from the Open-Meteo API for the year 2024.

## 📊 Project Overview

This project combines CitiBike trip data with historical weather data to analyze patterns and correlations between weather conditions and bike-sharing usage in New York City. The analysis covers data from December 2023 through December 2024.

## 🗂️ Data Sources

### CitiBike Trip Data
- **Source**: Jersey City CitiBike trip data (JC-YYYYMM-citibike-tripdata.csv)
- **Period**: December 2023 - December 2024
- **Format**: CSV files with trip details including start/end times, stations, and user types
- **Total Records**: Over 1 million trips processed

### Weather Data
- **Source**: [Open-Meteo Historical Weather API](https://open-meteo.com/)
- **Location**: LaGuardia Airport, NYC (40.7769°N, 73.8740°W)
- **Enhanced Features**: 
  - **Basic Metrics**: Temperature (max/min/mean), precipitation, wind speed, humidity
  - **Time-Specific Data**: Morning, afternoon, and evening temperatures
  - **Precipitation Details**: Total rain, snow, hourly maximums, precipitation type
  - **Wind Analysis**: Maximum gusts, calm hours, directional patterns
  - **Comfort Indices**: Heat index, wind chill, cycling comfort index
  - **Weather Conditions**: Dominant weather codes, visibility, cloud cover
- **Period**: January 1, 2024 - December 31, 2024 (366 days including leap day)

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

## 📂 Project Structure

```text
New York's CitiBike trips in 2022./
├── .gitignore                             # Git ignore rules for large files
├── README.md                              # Project documentation
├── Plan.md                                # Project planning document
├── citibike_weather_analysis_2024.ipynb   # Main analysis notebook
├── citibike_weather_env/                  # Python virtual environment
├── logs/                                  # Analysis execution logs
│   └── citibike_analysis_20250814_131055.log
├── JC-202401-citibike-tripdata.csv        # Jan 2024 trip data
├── JC-202402-citibike-tripdata.csv        # Feb 2024 trip data
├── ... (monthly files through Dec 2024)
├── weather_data_2024_openmeteo.csv        # Basic weather data
├── weather_data_2024_enhanced.csv         # Enhanced weather features
└── citibike_weather_merged_2024.csv       # Merged trip and weather data
```

## 🚀 Usage

### Running the Analysis

1. **Open the main notebook**:
   ```bash
   jupyter lab citibike_weather_analysis_2024.ipynb
   

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

- `weather_data_2024_openmeteo.csv`: Basic daily weather data from Open-Meteo API
- `weather_data_2024_enhanced.csv`: Enhanced weather dataset with computed features:
  - Time-specific temperatures (morning/afternoon/evening)
  - Precipitation analysis (type, intensity, duration)
  - Wind patterns and comfort indices
  - Heat index, wind chill, and cycling comfort scores
- `citibike_weather_merged_2024.csv`: Combined trip and weather data for analysis
- `logs/`: Execution logs with timestamps for reproducibility

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional analysis features.

## 📄 License

This project is for educational and research purposes. Please respect the terms of service for both CitiBike data and Open-Meteo API usage.


#### Analysis Components
1. **Enhanced Weather Feature Engineering**:
   - Time-specific temperature analysis (morning, afternoon, evening)
   - Precipitation categorization (rain vs. snow vs. mixed)
   - Wind pattern analysis with gust detection
   - Comfort index calculations for cycling conditions
   
2. **Temporal Analysis**: Hourly, daily, and seasonal usage patterns
3. **Weather Impact Assessment**: Multi-dimensional weather condition effects
4. **Rider Segmentation**: Member vs. casual rider behavior analysis
5. **Station Performance**: Popular routes and station demand patterns
6. **Predictive Modeling**: Weather-based demand forecasting with enhanced features

## 📈 Key Insights

- **Optimal Temperature**: Peak ridership occurs at 20-25°C (68-77°F)
- **Weather Sensitivity**: Strong positive correlation (r=0.778) between temperature and daily trips
- **Seasonal Variation**: Summer months (June-August) show highest usage
- **Member Loyalty**: Members show less weather sensitivity than casual riders
- **Peak Hours**: Morning (7-9 AM) and evening (5-7 PM) commute times
- **Precipitation Impact**: Moderate negative correlation (r=-0.356) with daily ridership
- **Comfort Index Correlation**: Cycling comfort index shows strong predictive power for ridership
- **Wind Effect**: High wind speeds (>15 m/s) significantly reduce casual rider usage
- **Time-of-Day Weather Sensitivity**: Evening temperatures more predictive than morning for commuter patterns

## 🔮 Future Enhancements
- Real-time Weather Integration : Live weather API for current conditions
- Machine Learning Models : Advanced predictive algorithms for demand forecasting
- Interactive Dashboards : Web-based visualization platform
- Station-Level Analysis : Granular insights for individual bike stations
- Route Optimization : AI-powered bike redistribution recommendations
- Mobile App Integration : User-facing weather-aware trip planning
- Hyperlocal Weather : Integration of multiple weather stations for better geographic coverage
## 📊 Data Sources
### CitiBike Trip Data
- Source : Citi Bike System Data
- Format : Jersey City CitiBike trip data (JC-YYYYMM-citibike-tripdata.csv)
- Period : December 2023 - December 2024
- Total Records : Over 1 million trips processed
### Weather Data
- Source : Open-Meteo Historical Weather API
- Location : LaGuardia Airport, NYC (40.7769°N, 73.8740°W)
- Enhanced Features :
  - Basic Metrics : Temperature (max/min/mean), precipitation, wind speed, humidity
  - Time-Specific Data : Morning, afternoon, and evening temperatures
  - Precipitation Details : Total rain, snow, hourly maximums, precipitation type
  - Wind Analysis : Maximum gusts, calm hours, directional patterns
  - Comfort Indices : Heat index, wind chill, cycling comfort index
  - Weather Conditions : Dominant weather codes, visibility, cloud cover
- Period : January 1, 2024 - December 31, 2024 (366 days including leap day)
- Analysis Period : January 2024 - December 2024
- Geographic Scope : New York City metropolitan area
## 📊 Output Files
- weather_data_2024_openmeteo.csv : Basic daily weather data from Open-Meteo API
- weather_data_2024_enhanced.csv : Enhanced weather dataset with computed features:
  - Time-specific temperatures (morning/afternoon/evening)
  - Precipitation analysis (type, intensity, duration)
  - Wind patterns and comfort indices
  - Heat index, wind chill, and cycling comfort scores
- citibike_weather_merged_2024.csv : Combined trip and weather data for analysis
- logs/ : Execution logs with timestamps for reproducibility
## ⚠️ Limitations & Next Steps
### 📊 Data Limitations Temporal Considerations
- Leap Year Handling : 2024 is a leap year with February 29th. The analysis includes this extra day, which may slightly skew monthly averages and seasonal comparisons with non-leap years
- Data Completeness : Analysis assumes complete data coverage for all dates, but potential gaps in trip data or weather API responses could affect correlation accuracy
- Timezone Consistency : All timestamps are standardized to America/New_York timezone, but original data sources may have inconsistent timezone handling Geographic & Location Assumptions
- Single Weather Station : Weather data is sourced exclusively from LaGuardia Airport (40.7769°N, 73.8740°W), which may not represent microclimatic conditions across all NYC boroughs
- Urban Heat Island Effect : Airport weather data may not capture the urban heat island effect experienced in dense city areas where most bike stations are located
- Elevation Differences : LaGuardia Airport is at sea level, while NYC has varying elevations that could affect local weather conditions
- Distance Bias : Weather conditions at LaGuardia may differ significantly from conditions in Manhattan, Brooklyn, or other boroughs (up to 20+ miles away) Methodological Biases
- Correlation vs. Causation : Strong correlations between weather and ridership don't necessarily imply direct causation; other factors (events, holidays, infrastructure changes) may confound results
- Seasonal Confounding : Weather patterns correlate with other seasonal factors (school schedules, tourism, daylight hours) that independently affect bike usage
- Sample Bias : Jersey City CitiBike data (JC-prefix files) may not fully represent broader NYC CitiBike system patterns
- Temporal Aggregation : Daily weather averages may mask important intraday weather variations that affect commuting decisions Technical Limitations
- API Dependencies : Analysis relies on Open-Meteo API availability and rate limits, which could affect reproducibility
- Data Processing : Large dataset processing may encounter memory limitations on standard hardware
- Weather Code Interpretation : Weather condition codes from Open-Meteo may not perfectly align with user-perceived cycling conditions

## 🤝 Contributing
Feel free to fork this project and submit pull requests for improvements or additional analysis features.

## 📄 License
This project is for educational and research purposes. Please respect the terms of service for both CitiBike data and Open-Meteo API usage.

