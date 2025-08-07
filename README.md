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
   - Seasonal trend projections
   - Station-specific predictions

## �� Project Structure

```
├── citibike_weather_analysis_2024.ipynb    # Main analysis notebook
├── citibike_weather_merged_2024.csv        # Merged dataset (>25MB)
├── weather_data_2024_openmeteo.csv         # Weather data
├── JC-202312-citibike-tripdata.csv         # December 2023 data
├── JC-202401-citibike-tripdata.csv         # January 2024 data
├── JC-202402-citibike-tripdata.csv         # February 2024 data
├── ... (monthly data files)
├── Plan.md                                  # Project planning document
├── citibike_weather_env/                   # Python virtual environment
└── .gitignore                              # Git ignore (excludes large files)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Jupyter Lab/Notebook
- Required packages: pandas, numpy, matplotlib, seaborn, requests

### Setup
1. Clone the repository
2. Activate the virtual environment:
   ```bash
   source citibike_weather_env/bin/activate
   ```
3. Launch Jupyter Lab:
   ```bash
   jupyter lab
   ```
4. Open `citibike_weather_analysis_2024.ipynb`

## 📈 Key Insights

- **Temperature Sweet Spot**: Optimal ridership occurs between 15-25°C (59-77°F)
- **Weather Sensitivity**: 30% decrease in ridership during precipitation
- **Seasonal Variation**: 40% higher usage in spring/fall vs. winter months
- **Member Loyalty**: Members show 25% less weather sensitivity than casual riders
- **Peak Hours**: Morning (7-9 AM) and evening (5-7 PM) commuter patterns

## 🔮 Future Enhancements

- Real-time weather integration for live predictions
- Machine learning models for advanced forecasting
- Integration with subway and bus data for multimodal analysis
- Station expansion recommendation system
- Mobile app integration for user-facing insights

## 📊 Data Sources

- **CitiBike System Data**: [Citi Bike NYC](https://citibikenyc.com/system-data)
- **Weather Data**: [OpenMeteo API](https://open-meteo.com/)
- **Geographic Data**: NYC Open Data Portal

---

*This analysis supports data-driven decision making for urban mobility planning and bike-sharing system optimization.*
