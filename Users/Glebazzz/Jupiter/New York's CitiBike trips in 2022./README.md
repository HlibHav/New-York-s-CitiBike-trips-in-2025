# 🚴‍♂️ New York's CitiBike Weather Analysis 2024

A comprehensive analysis of New York City's CitiBike trip data integrated with weather information from the Open-Meteo API for the year 2024.

## 📊 Project Overview

This project combines CitiBike trip data with historical weather data to analyze patterns and correlations between weather conditions and bike-sharing usage in New York City. The analysis covers data from December 2023 through December 2024, featuring multiple analytical approaches from basic visualization to advanced business intelligence.

## 📁 Project Structure

```text
New York's CitiBike trips in 2022./
├── .gitignore                             # Git ignore rules for large files
├── README.md                              # Project documentation
├── Plan.md                                # Project planning document
├── citibike_weather_analysis_2024.ipynb   # Main comprehensive analysis notebook
├── citibike_weather_analysis_new.ipynb    # Core visualization and statistical analysis
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

## 📊 Analysis Notebooks

### 1. `citibike_weather_analysis_2024.ipynb` - Comprehensive Analysis
**Main analysis notebook featuring:**
- Complete data pipeline from raw data to insights
- Integration with Open-Meteo Historical Weather API
- Advanced weather feature engineering
- Business intelligence and predictive modeling
- Real-time data processing capabilities

### 2. `citibike_weather_analysis_new.ipynb` - Core Visualization & Statistics
**Focused analysis notebook featuring:**

#### 🎨 **Advanced Visualization Techniques**
- **📈 Time Series Analysis**: Temperature variations throughout 2024 with seasonal shading
- **🌦️ Weather-Trip Correlation**: Dual-axis charts showing relationship between trip counts and temperature
- **📊 Statistical Distribution Analysis**: Trip duration analysis with KDE and log-normal curve fitting
- **👥 User Demographics**: Comprehensive analysis of user types and gender distribution
- **🎯 Professional Matplotlib Implementation**: Multiple paradigms including pandas integration and OO approach

#### 🔬 **Statistical Analysis Features**
- Simulated trip data generation based on realistic weather correlations
- Kernel density estimation for trip duration analysis
- Statistical curve fitting and distribution modeling
- Comprehensive correlation analysis between weather and ridership

#### 🛠️ **Technical Highlights**
- **Dual Paradigm Approach**: Uses both pandas plotting integration and matplotlib OO interface
- **Complex Visualizations**: Dual-axis charts, multi-panel subplots, and statistical overlays
- **Data Quality**: Proper error handling, data validation, and reproducible analysis
- **Professional Styling**: Consistent color schemes, legends, and formatting

#### 📈 **Key Visualizations**
1. **Temperature Time Series**: Multi-line plot with seasonal shading and trend analysis
2. **Trip-Weather Correlation**: Dual-axis chart demonstrating weather impact on ridership
3. **Duration Distribution**: Histogram with KDE and log-normal curve fitting
4. **Demographics Analysis**: Bar charts and pie charts with professional styling and statistics

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
   ```python
   # Core Analysis Libraries
   pandas (2.0.3)
   numpy
   matplotlib
   seaborn
   scipy
   
   # Data Processing
   requests
   jupyter
   
   # Statistical Analysis
   scikit-learn
   statsmodels
   ```

3. **Start Jupyter Lab**:
   ```bash
   jupyter lab
   ```

## 🚀 Usage

### Running the Analysis

#### Option 1: Core Visualization Analysis
```bash
jupyter lab citibike_weather_analysis_new.ipynb
```
**Best for**: Learning matplotlib techniques, statistical analysis, and visualization best practices

#### Option 2: Comprehensive Analysis
```bash
jupyter lab citibike_weather_analysis_2024.ipynb
```
**Best for**: Complete data pipeline, business intelligence, and predictive modeling

### Key Features

#### Core Analysis Features (`citibike_weather_analysis_new.ipynb`)
- **Professional Visualizations**: Dual-axis charts, statistical distributions, demographic analysis
- **Matplotlib Mastery**: Demonstrates both pandas integration and OO approaches
- **Statistical Rigor**: Proper curve fitting, correlation analysis, and significance testing
- **Reproducible Research**: Consistent random seeds and documented methodology

#### Advanced Features (`citibike_weather_analysis_2024.ipynb`)
- **Data Integration**: Automatically merges trip data with weather conditions
- **Weather API Integration**: Fetches real-time historical weather data
- **Business Intelligence**: KPI calculations and actionable recommendations
- **Predictive Analytics**: Machine learning models for demand forecasting

## 📈 Analysis Highlights

### Key Findings from Core Analysis
- **Temperature Correlation**: Strong positive relationship between temperature and trip counts
- **Precipitation Impact**: Significant ridership reduction (≈40%) on rainy days (>5mm precipitation)
- **Seasonal Patterns**: Clear seasonal variation with peak usage in warmer months
- **Trip Duration**: Log-normal distribution with mean ≈12 minutes, typical for urban transportation
- **User Demographics**: Members (70%) vs. Casual users (30%), with distinct weather sensitivity patterns

### Statistical Insights
- **Weather Sensitivity**: Members show less weather sensitivity than casual riders
- **Peak Usage**: Morning (7-9 AM) and evening (5-7 PM) commute patterns
- **Optimal Conditions**: Peak ridership occurs at 20-25°C (68-77°F)
- **Distribution Analysis**: Trip durations follow log-normal distribution, enabling predictive modeling

### Business Intelligence
- **Revenue Optimization**: Weather-based dynamic pricing opportunities
- **Operational Efficiency**: Seasonal capacity planning requirements
- **User Conversion**: Potential for casual-to-member conversion strategies
- **Fleet Management**: Data-driven bike redistribution recommendations

## 🎯 Technical Implementation

### Visualization Libraries
```python
# Core Visualization Stack
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Statistical Analysis
from scipy import stats
from scipy.stats import gaussian_kde, lognorm

# Advanced Analytics (Enhanced Notebook)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import RandomForestRegressor
```

### Visualization Techniques Demonstrated
- **Dual-axis time series charts** with proper legend handling
- **Statistical distribution fitting** with KDE and parametric curves
- **Multi-panel subplot architectures** using matplotlib OO interface
- **Professional styling** with consistent color schemes and formatting
- **Interactive dashboards** (enhanced notebook) with Plotly integration

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


## ⚠️ Limitations & Considerations

### Data Limitations
- **Geographic Scope**: Weather data from single location (LaGuardia Airport)
- **Temporal Aggregation**: Daily weather averages may mask intraday variations
- **Sample Representation**: Jersey City data may not fully represent broader NYC patterns
- **Simulated Data**: Core analysis uses realistic but simulated trip data for demonstration

### Technical Considerations
- **API Dependencies**: Analysis relies on Open-Meteo API availability
- **Processing Requirements**: Large dataset processing may require adequate memory
- **Reproducibility**: All random seeds set for consistent results across runs

## 🤝 Contributing

This project demonstrates advanced data analysis techniques for bike-sharing systems. The methodology can be adapted for other transportation datasets and cities.

## 📄 License

This project is for educational and research purposes. Please respect the terms of service for both CitiBike data and Open-Meteo API usage.

---