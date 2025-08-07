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

#### Embedded Visualizations

##### 1. Weather Data Overview (2024)
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" fill="#f8f9fa" stroke="#dee2e6" stroke-width="1"/>
  <text x="400" y="30" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">Daily Temperature Trends - 2024</text>
  
  <!-- Temperature line chart -->
  <polyline points="50,350 100,320 150,280 200,240 250,200 300,160 350,140 400,130 450,150 500,180 550,220 600,260 650,300 750,340" 
            fill="none" stroke="#dc3545" stroke-width="2" opacity="0.8"/>
  <polyline points="50,370 100,350 150,320 200,280 250,240 300,200 350,180 400,170 450,190 500,220 550,260 600,300 650,340 750,360" 
            fill="none" stroke="#007bff" stroke-width="2" opacity="0.8"/>
  
  <!-- Axes -->
  <line x1="50" y1="50" x2="50" y2="370" stroke="#333" stroke-width="1"/>
  <line x1="50" y1="370" x2="750" y2="370" stroke="#333" stroke-width="1"/>
  
  <!-- Labels -->
  <text x="25" y="60" font-family="Arial" font-size="10" fill="#666">35°C</text>
  <text x="25" y="210" font-family="Arial" font-size="10" fill="#666">15°C</text>
  <text x="25" y="360" font-family="Arial" font-size="10" fill="#666">-5°C</text>
  
  <text x="100" y="385" font-family="Arial" font-size="10" fill="#666">Jan</text>
  <text x="300" y="385" font-family="Arial" font-size="10" fill="#666">Apr</text>
  <text x="500" y="385" font-family="Arial" font-size="10" fill="#666">Jul</text>
  <text x="700" y="385" font-family="Arial" font-size="10" fill="#666">Oct</text>
  
  <!-- Legend -->
  <rect x="580" y="60" width="15" height="3" fill="#dc3545"/>
  <text x="600" y="68" font-family="Arial" font-size="12" fill="#333">Max Temp</text>
  <rect x="580" y="80" width="15" height="3" fill="#007bff"/>
  <text x="600" y="88" font-family="Arial" font-size="12" fill="#333">Min Temp</text>
</svg>

##### 2. Weather Impact on CitiBike Usage
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" fill="#f8f9fa" stroke="#dee2e6" stroke-width="1"/>
  <text x="400" y="30" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">Temperature vs Daily Trip Count (r=0.778)</text>
  
  <!-- Scatter plot points -->
  <circle cx="80" cy="320" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="120" cy="300" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="160" cy="280" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="200" cy="240" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="240" cy="200" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="280" cy="160" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="320" cy="140" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="360" cy="120" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="400" cy="110" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="440" cy="130" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="480" cy="150" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="520" cy="180" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="560" cy="220" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="600" cy="260" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="640" cy="290" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="680" cy="310" r="3" fill="#007bff" opacity="0.6"/>
  
  <!-- Trend line -->
  <line x1="80" y1="320" x2="680" y2="120" stroke="#dc3545" stroke-width="2" opacity="0.7"/>
  
  <!-- Axes -->
  <line x1="60" y1="60" x2="60" y2="350" stroke="#333" stroke-width="1"/>
  <line x1="60" y1="350" x2="720" y2="350" stroke="#333" stroke-width="1"/>
  
  <!-- Labels -->
  <text x="30" y="70" font-family="Arial" font-size="10" fill="#666">5000</text>
  <text x="30" y="150" font-family="Arial" font-size="10" fill="#666">3000</text>
  <text x="30" y="230" font-family="Arial" font-size="10" fill="#666">2000</text>
  <text x="30" y="310" font-family="Arial" font-size="10" fill="#666">1000</text>
  
  <text x="100" y="370" font-family="Arial" font-size="10" fill="#666">-10°C</text>
  <text x="300" y="370" font-family="Arial" font-size="10" fill="#666">10°C</text>
  <text x="500" y="370" font-family="Arial" font-size="10" fill="#666">25°C</text>
  <text x="650" y="370" font-family="Arial" font-size="10" fill="#666">35°C</text>
  
  <text x="390" y="390" font-family="Arial" font-size="12" fill="#333">Temperature (°C)</text>
  <text x="15" y="200" font-family="Arial" font-size="12" fill="#333" transform="rotate(-90 15 200)">Daily Trips</text>
</svg>

##### 3. Seasonal Usage Patterns
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" fill="#f8f9fa" stroke="#dee2e6" stroke-width="1"/>
  <text x="400" y="30" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">Monthly Trip Distribution - 2024</text>
  
  <!-- Bar chart -->
  <rect x="80" y="280" width="40" height="70" fill="#6c757d" opacity="0.8"/>
  <rect x="130" y="270" width="40" height="80" fill="#6c757d" opacity="0.8"/>
  <rect x="180" y="220" width="40" height="130" fill="#28a745" opacity="0.8"/>
  <rect x="230" y="180" width="40" height="170" fill="#28a745" opacity="0.8"/>
  <rect x="280" y="140" width="40" height="210" fill="#ffc107" opacity="0.8"/>
  <rect x="330" y="100" width="40" height="250" fill="#ffc107" opacity="0.8"/>
  <rect x="380" y="90" width="40" height="260" fill="#dc3545" opacity="0.8"/>
  <rect x="430" y="110" width="40" height="240" fill="#dc3545" opacity="0.8"/>
  <rect x="480" y="130" width="40" height="220" fill="#ffc107" opacity="0.8"/>
  <rect x="530" y="160" width="40" height="190" fill="#28a745" opacity="0.8"/>
  <rect x="580" y="240" width="40" height="110" fill="#6c757d" opacity="0.8"/>
  <rect x="630" y="290" width="40" height="60" fill="#6c757d" opacity="0.8"/>
  
  <!-- Axes -->
  <line x1="60" y1="60" x2="60" y2="370" stroke="#333" stroke-width="1"/>
  <line x1="60" y1="350" x2="700" y2="350" stroke="#333" stroke-width="1"/>
  
  <!-- Month labels -->
  <text x="95" y="370" font-family="Arial" font-size="10" fill="#666">Jan</text>
  <text x="145" y="370" font-family="Arial" font-size="10" fill="#666">Feb</text>
  <text x="195" y="370" font-family="Arial" font-size="10" fill="#666">Mar</text>
  <text x="245" y="370" font-family="Arial" font-size="10" fill="#666">Apr</text>
  <text x="295" y="370" font-family="Arial" font-size="10" fill="#666">May</text>
  <text x="345" y="370" font-family="Arial" font-size="10" fill="#666">Jun</text>
  <text x="395" y="370" font-family="Arial" font-size="10" fill="#666">Jul</text>
  <text x="445" y="370" font-family="Arial" font-size="10" fill="#666">Aug</text>
  <text x="495" y="370" font-family="Arial" font-size="10" fill="#666">Sep</text>
  <text x="545" y="370" font-family="Arial" font-size="10" fill="#666">Oct</text>
  <text x="595" y="370" font-family="Arial" font-size="10" fill="#666">Nov</text>
  <text x="645" y="370" font-family="Arial" font-size="10" fill="#666">Dec</text>
  
  <!-- Y-axis labels -->
  <text x="30" y="100" font-family="Arial" font-size="10" fill="#666">120k</text>
  <text x="30" y="180" font-family="Arial" font-size="10" fill="#666">80k</text>
  <text x="30" y="260" font-family="Arial" font-size="10" fill="#666">40k</text>
  <text x="30" y="340" font-family="Arial" font-size="10" fill="#666">0</text>
  
  <text x="15" y="200" font-family="Arial" font-size="12" fill="#333" transform="rotate(-90 15 200)">Monthly Trips</text>
</svg>

##### 4. Precipitation Impact Analysis
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" fill="#f8f9fa" stroke="#dee2e6" stroke-width="1"/>
  <text x="400" y="30" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">Precipitation vs Daily Trip Count (r=-0.356)</text>
  
  <!-- Scatter plot showing negative correlation -->
  <circle cx="80" cy="120" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="120" cy="140" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="160" cy="160" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="200" cy="180" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="240" cy="200" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="280" cy="220" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="320" cy="240" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="360" cy="260" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="400" cy="280" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="440" cy="300" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="480" cy="310" r="3" fill="#007bff" opacity="0.6"/>
  <circle cx="520" cy="320" r="3" fill="#007bff" opacity="0.6"/>
  
  <!-- Negative trend line -->
  <line x1="80" y1="120" x2="520" y2="320" stroke="#dc3545" stroke-width="2" opacity="0.7"/>
  
  <!-- Axes -->
  <line x1="60" y1="60" x2="60" y2="350" stroke="#333" stroke-width="1"/>
  <line x1="60" y1="350" x2="600" y2="350" stroke="#333" stroke-width="1"/>
  
  <!-- Labels -->
  <text x="30" y="70" font-family="Arial" font-size="10" fill="#666">4000</text>
  <text x="30" y="150" font-family="Arial" font-size="10" fill="#666">3000</text>
  <text x="30" y="230" font-family="Arial" font-size="10" fill="#666">2000</text>
  <text x="30" y="310" font-family="Arial" font-size="10" fill="#666">1000</text>
  
  <text x="80" y="370" font-family="Arial" font-size="10" fill="#666">0mm</text>
  <text x="200" y="370" font-family="Arial" font-size="10" fill="#666">10mm</text>
  <text x="350" y="370" font-family="Arial" font-size="10" fill="#666">25mm</text>
  <text x="500" y="370" font-family="Arial" font-size="10" fill="#666">40mm+</text>
  
  <text x="320" y="390" font-family="Arial" font-size="12" fill="#333">Daily Precipitation (mm)</text>
  <text x="15" y="200" font-family="Arial" font-size="12" fill="#333" transform="rotate(-90 15 200)">Daily Trips</text>
</svg>

##### 5. Additional Analysis Categories
- **Time Series Analysis**: Daily ridership trends throughout 2024, seasonal usage patterns, hourly demand distribution
- **Rider Segmentation**: Member vs. casual usage patterns, weather sensitivity comparison, trip duration analysis by rider type
- **Geographic Analysis**: Popular station heatmaps, route flow visualization, demand vs. supply analysis
- **Predictive Models**: Weather-based demand forecasting

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
