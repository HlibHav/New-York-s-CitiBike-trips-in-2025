import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import streamlit.components.v1 as components

# Configure Streamlit page
st.set_page_config(
    page_title="CitiBike Analytics Dashboard",
    page_icon="🚴‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: bold;
}
.sub-header {
    font-size: 1.5rem;
    color: #333;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
.metric-container {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Main title and description
st.markdown('<h1 class="main-header">🚴‍♂️ CitiBike Analytics Dashboard</h1>', unsafe_allow_html=True)

st.markdown("""
### Welcome to the New York CitiBike Data Analysis Dashboard

This interactive dashboard provides comprehensive insights into CitiBike usage patterns in New York City for 2024. 
Explore bike sharing trends, popular stations, and the correlation between weather conditions and ridership.

**Key Features:**
- 📊 **Station Popularity Analysis**: Discover the most frequented CitiBike stations
- 🌡️ **Weather Impact**: Understand how temperature affects bike usage
- 🗺️ **Interactive Map**: Explore station locations and trip patterns
- 📈 **Trend Analysis**: Visualize daily ridership patterns

---
""")

# Load data with caching for better performance
@st.cache_data
def load_data():
    """Load and preprocess CitiBike data"""
    try:
        df = pd.read_csv('citibike_weather_merged_2024.csv')
        df['started_at'] = pd.to_datetime(df['started_at'])
        df['date'] = pd.to_datetime(df['date'])
        df_clean = df.dropna(subset=['start_station_name', 'end_station_name'])
        return df_clean
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'citibike_weather_merged_2024.csv' is in the current directory.")
        return None

# Load the data
df_clean = load_data()

if df_clean is not None:
    # Sidebar with data summary
    st.sidebar.header("📊 Data Overview")
    st.sidebar.metric("Total Trips", f"{len(df_clean):,}")
    st.sidebar.metric("Date Range", f"{df_clean['date'].min().strftime('%Y-%m-%d')} to {df_clean['date'].max().strftime('%Y-%m-%d')}")
    st.sidebar.metric("Unique Stations", f"{df_clean['start_station_name'].nunique():,}")
    
    # Average temperature
    avg_temp = df_clean['temperature_mean_c'].mean()
    st.sidebar.metric("Average Temperature", f"{avg_temp:.1f}°C")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Data Source:** CitiBike NYC & Open-Meteo Weather API")
    
    # Main dashboard content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">📊 Most Popular CitiBike Stations</h2>', unsafe_allow_html=True)
        
        # Calculate most popular stations
        station_counts = df_clean['start_station_name'].value_counts().head(15)
        
        # Create bar chart
        fig_bar = px.bar(
            x=station_counts.values,
            y=station_counts.index,
            orientation='h',
            title='Top 15 Most Popular CitiBike Stations in New York (2024)',
            labels={'x': 'Number of Trips', 'y': 'Station Name'},
            color=station_counts.values,
            color_continuous_scale='viridis'
        )
        
        # Customize layout
        fig_bar.update_layout(
            height=600,
            title_font_size=18,
            title_x=0.5,
            xaxis_title_font_size=14,
            yaxis_title_font_size=14,
            font=dict(size=11),
            plot_bgcolor='white',
            paper_bgcolor='white',
            showlegend=False
        )
        
        fig_bar.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig_bar.update_yaxes(showgrid=False)
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.markdown('<h3 class="sub-header">🏆 Top Station Stats</h3>', unsafe_allow_html=True)
        
        # Display top 5 stations with metrics
        for i, (station, count) in enumerate(station_counts.head(5).items()):
            st.markdown(f"**#{i+1} {station}**")
            st.metric("", f"{count:,} trips")
            st.markdown("---")
    
    # Weather correlation section
    st.markdown('<h2 class="sub-header">🌡️ Weather Impact on Bike Usage</h2>', unsafe_allow_html=True)
    
    # Aggregate daily data
    daily_data = df_clean.groupby('date').agg({
        'ride_id': 'count',
        'temperature_mean_c': 'mean'
    }).reset_index()
    
    daily_data.columns = ['date', 'trip_count', 'temp_mean']
    daily_data = daily_data.sort_values('date')
    
    # Create dual-axis line chart
    fig_dual = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add trip count line
    fig_dual.add_trace(
        go.Scatter(
            x=daily_data['date'],
            y=daily_data['trip_count'],
            mode='lines',
            name='Daily Trip Count',
            line=dict(color='#1f77b4', width=2),
            hovertemplate='<b>Date:</b> %{x}<br><b>Trips:</b> %{y:,}<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Add temperature line
    fig_dual.add_trace(
        go.Scatter(
            x=daily_data['date'],
            y=daily_data['temp_mean'],
            mode='lines',
            name='Mean Temperature (°C)',
            line=dict(color='#ff7f0e', width=2),
            hovertemplate='<b>Date:</b> %{x}<br><b>Temperature:</b> %{y:.1f}°C<extra></extra>'
        ),
        secondary_y=True
    )
    
    # Update layout
    fig_dual.update_layout(
        title='CitiBike Daily Trips vs Temperature Correlation (2024)',
        title_font_size=18,
        title_x=0.5,
        height=500,
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Set y-axes titles
    fig_dual.update_yaxes(title_text="Number of Daily Trips", secondary_y=False, showgrid=True, gridcolor='lightgray')
    fig_dual.update_yaxes(title_text="Temperature (°C)", secondary_y=True, showgrid=False)
    fig_dual.update_xaxes(title_text="Date", showgrid=True, gridcolor='lightgray')
    
    st.plotly_chart(fig_dual, use_container_width=True)
    
    # Correlation analysis
    correlation = daily_data['trip_count'].corr(daily_data['temp_mean'])
    st.info(f"📈 **Correlation Coefficient:** {correlation:.3f} - {'Strong' if abs(correlation) > 0.7 else 'Moderate' if abs(correlation) > 0.4 else 'Weak'} correlation between temperature and trip count")
    
    # Interactive Map Section
    st.markdown('<h2 class="sub-header">🗺️ Interactive Station Map</h2>', unsafe_allow_html=True)
    
    # Check if kepler.gl map exists
    try:
        with open('citibike_trips_map.html', 'r', encoding='utf-8') as f:
            map_html = f.read()
        
        st.markdown("""
        **Explore the interactive map below to see:**
        - Station locations across New York City
        - Trip flow patterns and popular routes
        - Geographic distribution of bike usage
        """)
        
        # Display the map
        components.html(map_html, height=600, scrolling=True)
        
    except FileNotFoundError:
        st.warning("Interactive map file 'citibike_trips_map.html' not found. Please ensure the file is in the current directory.")
        
        # Create a simple scatter plot as fallback
        st.markdown("**Fallback: Station Locations Scatter Plot**")
        
        # Sample of station locations
        station_locations = df_clean.groupby('start_station_name').agg({
            'start_lat': 'mean',
            'start_lng': 'mean',
            'ride_id': 'count'
        }).reset_index()
        
        station_locations.columns = ['station_name', 'lat', 'lng', 'trip_count']
        station_locations = station_locations.head(100)  # Limit for performance
        
        fig_map = px.scatter_mapbox(
            station_locations,
            lat='lat',
            lon='lng',
            size='trip_count',
            hover_name='station_name',
            hover_data={'trip_count': True},
            color='trip_count',
            color_continuous_scale='viridis',
            title='CitiBike Station Locations (Top 100 by Usage)',
            mapbox_style='open-street-map',
            height=600
        )
        
        fig_map.update_layout(title_x=0.5)
        st.plotly_chart(fig_map, use_container_width=True)
    
    # Additional insights
    st.markdown('<h2 class="sub-header">📈 Key Insights</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        peak_day = daily_data.loc[daily_data['trip_count'].idxmax()]
        st.metric(
            "Peak Usage Day",
            peak_day['date'].strftime('%Y-%m-%d'),
            f"{peak_day['trip_count']:,} trips"
        )
    
    with col2:
        avg_daily_trips = daily_data['trip_count'].mean()
        st.metric(
            "Average Daily Trips",
            f"{avg_daily_trips:,.0f}",
            "trips per day"
        )
    
    with col3:
        total_stations = df_clean['start_station_name'].nunique()
        st.metric(
            "Active Stations",
            f"{total_stations:,}",
            "unique locations"
        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>🚴‍♂️ CitiBike Analytics Dashboard | Data Analysis & Visualization</p>
        <p>Built with Streamlit & Plotly | Weather data from Open-Meteo API</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("Unable to load data. Please check if the data file exists and try again.")
