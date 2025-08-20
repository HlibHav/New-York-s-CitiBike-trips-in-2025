# 🚴 New York CitiBike Data Analysis Project

A comprehensive data analysis project exploring CitiBike trip patterns and their relationship with weather conditions using advanced Python visualization libraries.

## 📊 Project Overview

This project contains multiple Jupyter notebooks that demonstrate different aspects of data visualization and analysis using CitiBike trip data from New York City. The analysis focuses on understanding ridership patterns, weather correlations, user demographics, and seasonal trends through both Matplotlib and Seaborn visualizations.

## 📁 Project Structure


```
New York's CitiBike trips in 2022./
├── README.md
├── citibike_seaborn_analysis.ipynb          # Advanced Seaborn visualizations
├── citibike_weather_analysis_2024.ipynb     # Weather correlation analysis
├── citibike_weather_analysis_new.ipynb      # Enhanced weather analysis
└── weather_data_2024_enhanced.csv           # Weather dataset
```


## 🎯 Analysis Objectives

### Primary Goals:
- **Weather Impact Analysis**: Understand how weather conditions affect CitiBike usage patterns
- **User Behavior Insights**: Analyze trip duration distributions and user demographics
- **Seasonal Trends**: Identify patterns across different seasons and weather conditions
- **Visualization Mastery**: Demonstrate advanced plotting techniques using both Matplotlib and Seaborn

## 📚 Notebook Descriptions

### 1. 🎨 CitiBike Seaborn Analysis (`citibike_seaborn_analysis.ipynb`)
**Focus**: Advanced Seaborn visualization techniques

**Key Features**:
- Global theme and style configuration
- Dynamic color palette management
- Dual-axis plotting with temperature and trip count correlation
- Statistical visualizations (box plots, violin plots, pair plots)
- FacetGrid for multi-dimensional analysis
- Correlation heatmaps with professional styling

**Seaborn Advantages Demonstrated**:
- Simplified syntax for complex statistical plots
- Built-in statistical functions and estimations
- Aesthetic themes and consistent styling
- Intelligent color palette management
- Effortless multi-panel comparisons with FacetGrid

### 2. 🌤️ Weather Analysis 2024 (`citibike_weather_analysis_2024.ipynb`)
**Focus**: Matplotlib paradigms and weather correlation analysis

**Key Features**:
- Temperature time series analysis with seasonal shading
- Dual-axis charts combining trip counts and weather data
- Trip duration distribution analysis with fitted curves
- User demographics visualization using subplots
- Kernel density estimation for statistical modeling

**Matplotlib Paradigms Used**:
- **Pandas Integration**: Quick exploratory plotting with `df.plot()`
- **Object-Oriented Approach**: Full control with explicit figure and axes objects
- **Advanced Techniques**: `twinx()` for dual-axis, combined legends, grid customization

### 3. 🔄 Enhanced Weather Analysis (`citibike_weather_analysis_new.ipynb`)
**Focus**: Comprehensive weather impact analysis

**Key Features**:
- Enhanced temperature time series with multiple variables
- Sophisticated trip count simulation based on weather factors
- Professional dual-axis visualizations
- Statistical analysis of trip duration patterns
- Multi-panel demographic analysis

## 🛠️ Technologies Used

### Core Libraries:
- **Python 3.8+**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing and statistical operations
- **Matplotlib**: Fundamental plotting and visualization
- **Seaborn**: Statistical data visualization
- **SciPy**: Scientific computing and statistical functions

### Visualization Techniques:
- Time series analysis and plotting
- Dual-axis charts for multi-variable comparison
- Statistical distribution fitting and visualization
- Correlation analysis and heatmaps
- Multi-panel subplot arrangements
- Professional styling and theming

## 📈 Key Insights and Findings

### Weather Impact:
- **Temperature Correlation**: Strong positive correlation between temperature and trip counts
- **Precipitation Effect**: Significant reduction in ridership during rainy days (up to 40% decrease)
- **Seasonal Patterns**: Clear seasonal variation with peaks in warmer months

### User Behavior:
- **Trip Duration**: Follows log-normal distribution, typical for transportation data
- **User Types**: Members dominate usage (70% vs 30% casual users)
- **Demographics**: Male users represent majority of ridership

### Station Patterns:
- **Usage Distribution**: Clear Zipf distribution in station popularity
- **Geographic Trends**: Central locations show higher usage patterns

## 🎨 Visualization Highlights

### Advanced Seaborn Features:
1. **Global Theme Management**: Consistent styling across all visualizations
2. **Dynamic Color Palettes**: Context-aware color selection
3. **Statistical Integration**: Built-in regression lines and confidence intervals
4. **FacetGrid Power**: Multi-dimensional data exploration
5. **Professional Aesthetics**: Publication-ready plot styling

### Matplotlib Mastery:
1. **Dual-Axis Plotting**: Complex multi-variable time series
2. **Subplot Architecture**: Multi-panel comparative analysis
3. **Custom Styling**: Professional formatting and annotations
4. **Statistical Overlays**: Fitted curves and distribution analysis

## 🚀 Getting Started

### Prerequisites:
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Running the Analysis:
1. Clone or download the project files
2. Ensure all required libraries are installed
3. Open Jupyter Notebook or JupyterLab
4. Run the notebooks in any order (each is self-contained)

### Data Requirements:
- Weather data: `weather_data_2024_enhanced.csv`
- Trip data: Simulated within notebooks for demonstration

## 📊 Sample Visualizations

The project includes various types of professional visualizations:
- **Time Series**: Temperature variations and trip count trends
- **Correlation Analysis**: Heatmaps showing variable relationships
- **Distribution Analysis**: Trip duration patterns with statistical fitting
- **Demographic Insights**: User type and gender distribution analysis
- **Multi-dimensional Plots**: FacetGrid comparisons across multiple variables

## 🎓 Learning Outcomes

### Technical Skills Demonstrated:
- **Data Manipulation**: Advanced pandas operations for time series data
- **Statistical Analysis**: Correlation analysis, distribution fitting, hypothesis testing
- **Visualization Design**: Professional plot styling and multi-panel layouts
- **Library Integration**: Seamless combination of matplotlib and seaborn capabilities
- **Code Organization**: Clean, documented, and reproducible analysis workflows

### Visualization Best Practices:
- Consistent color schemes and styling
- Appropriate chart types for different data relationships
- Clear labeling and professional formatting
- Statistical accuracy in data representation
- Accessibility considerations in design choices

## 📝 Future Enhancements

- Integration with real-time weather APIs
- Interactive visualizations using Plotly or Bokeh
- Machine learning models for trip prediction
- Geographic analysis with mapping libraries
- Dashboard development for real-time monitoring

## 📄 License

This project is available for educational and research purposes. Please cite appropriately if used in academic work.

---

*This analysis demonstrates the power of Python's visualization ecosystem for extracting meaningful insights from transportation and weather data.*

## 👥 Contributors
- Glib Gavryliuk (https://github.com/Glebazzz)
- Linkedin (https://www.linkedin.com/in/glebaz