# New York's CitiBike Weather Analysis 2024

## Project Overview

A comprehensive data analysis project examining the relationship between weather conditions and CitiBike usage patterns in New York City during 2024.

## STAR Analysis Framework

### 📍 **Situation**
New York's CitiBike system serves millions of rides annually, but usage patterns fluctuate significantly based on various factors. Understanding how weather conditions impact bike-sharing demand is crucial for:
- Operational planning and bike redistribution
- Predicting demand patterns
- Optimizing station capacity and placement
- Supporting data-driven expansion decisions

### 🎯 **Task**
Analyze the correlation between weather conditions and CitiBike usage patterns to:
1. Identify optimal weather conditions for bike-sharing
2. Understand seasonal trends and their impact on ridership
3. Compare usage patterns between different rider types (members vs. casual)
4. Provide actionable insights for operational improvements
5. Develop predictive models for demand forecasting

### ⚡ **Action**
Implemented a comprehensive data analysis pipeline:

#### Data Collection & Integration
- **CitiBike Trip Data**: Monthly trip records for 2024 (JC-202312 through JC-202412)
- **Weather Data**: Daily weather conditions from OpenMeteo API
- **Data Merging**: Combined trip and weather data for correlation analysis

#### Analysis Components
1. **Temporal Analysis**: Hourly, daily, and seasonal usage patterns
2. **Weather Impact Assessment**: Temperature, precipitation, and weather condition effects
3. **Rider Segmentation**: Member vs. casual rider behavior analysis
4. **Station Performance**: Popular routes and station demand patterns
5. **Predictive Modeling**: Weather-based demand forecasting

#### Technical Implementation
- **Python Environment**: Pandas, NumPy for data processing
- **Visualization**: Matplotlib, Seaborn for comprehensive charts
- **Data Sources**: CitiBike open data, OpenMeteo weather API
- **Analysis Tools**: Jupyter notebooks for interactive exploration

### 📊 **Results**

#### Key Findings
- **Weather Sensitivity**: Clear correlation between temperature and ridership
- **Seasonal Patterns**: Peak usage during spring and fall months
- **Rider Behavior**: Different weather sensitivity between member and casual riders
- **Operational Insights**: Station-specific demand patterns and optimization opportunities

#### Visualizations Included
1. **Time Series Analysis**
   - Daily ridership trends throughout 2024
   - Seasonal usage patterns
   - Hourly demand distribution

2. **Weather Impact Charts**
   - Temperature vs. ridership correlation
   - Precipitation impact on usage
   - Weather condition categorical analysis

3. **Rider Segmentation**
   - Member vs. casual usage patterns
   - Weather sensitivity comparison
   - Trip duration analysis by rider type

4. **Geographic Analysis**
   - Popular station heatmaps
   - Route flow visualization
   - Demand vs. supply analysis

5. **Predictive Models**
   - Weather-based demand forecasting

## 📁 Project Structure

```
New York's CitiBike trips in 2022./
├── .gitignore                             # Git ignore rules for large files
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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Lab/Notebook
- Required packages: pandas, numpy, matplotlib, requests

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "New York's CitiBike trips in 2022."
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv citibike_weather_env
   source citibike_weather_env/bin/activate  # On Windows: citibike_weather_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install pandas numpy matplotlib requests jupyter
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter lab citibike_weather_analysis_2024.ipynb
   ```

5. **Run the analysis**:
   - Execute all cells to load data, fetch weather information, and generate visualizations
   - The notebook will automatically merge trip data with weather conditions
   - All processed data will be saved as CSV files

## 📈 Key Insights

- **Optimal Temperature**: Peak ridership occurs at 20-25°C (68-77°F)
- **Weather Sensitivity**: Strong positive correlation (r=0.778) between temperature and daily trips
- **Seasonal Variation**: Summer months (June-August) show highest usage
- **Member Loyalty**: Members show less weather sensitivity than casual riders
- **Peak Hours**: Morning (7-9 AM) and evening (5-7 PM) commute times
- **Precipitation Impact**: Moderate negative correlation (r=-0.356) with daily ridership

## 🔮 Future Enhancements

- **Real-time Weather Integration**: Live weather API for current conditions
- **Machine Learning Models**: Advanced predictive algorithms for demand forecasting
- **Interactive Dashboards**: Web-based visualization platform
- **Station-Level Analysis**: Granular insights for individual bike stations
- **Route Optimization**: AI-powered bike redistribution recommendations
- **Mobile App Integration**: User-facing weather-aware trip planning

## 📊 Data Sources

- **CitiBike Trip Data**: [Citi Bike System Data](https://citibikenyc.com/system-data)
- **Weather Data**: [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)
- **Analysis Period**: January 2024 - December 2024
- **Geographic Scope**: New York City metropolitan area

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional analysis features.

## 📄 License

This project is for educational and research purposes. Please respect the terms of service for both CitiBike data and Open-Meteo API usage.
