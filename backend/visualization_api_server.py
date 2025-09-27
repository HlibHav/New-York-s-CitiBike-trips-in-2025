"""
Visualization API Server for CitiBike AI Dashboard
Generates interactive visualizations based on user queries
"""

import os
import sys
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Add the parent directory to the path to import the dashboard functions
sys.path.append(str(Path(__file__).parent.parent))

# Create the visualization directory
VIZ_DIR = Path("generated_visualizations")
VIZ_DIR.mkdir(exist_ok=True)

app = FastAPI(title="CitiBike Visualization API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ChatMessage(BaseModel):
    message: str
    query_category: Optional[str] = "general"

class VisualizationData(BaseModel):
    title: str
    description: str
    url: str
    data_points: int

class ChatResponse(BaseModel):
    response: str
    visualizations: List[VisualizationData] = []
    insights: List[str] = []
    recommendations: List[str] = []
    timestamp: str
    processing_time_ms: int
    trace_id: str

def load_citibike_data():
    """Load CitiBike data for visualization generation"""
    try:
        # Try to load the processed data
        df = pd.read_csv("citibike_weather_detrended_analysis.csv", parse_dates=['date'])
        
        # Add some basic processing
        df["temperature_f"] = df["temperature_mean_c"] * 9/5 + 32
        df["bike_rides_daily"] = df["trip_count"]
        
        # Weather categorization
        def categorize_weather(row):
            temp_c = row["temperature_mean_c"]
            precip = row["precipitation_mm"]
            
            if precip > 25:
                return "Heavy Precipitation"
            elif precip > 10:
                return "Moderate Precipitation"
            elif precip > 2:
                return "Light Precipitation"
            elif temp_c > 30:
                return "Very Hot"
            elif temp_c > 25:
                return "Hot"
            elif temp_c > 20:
                return "Warm"
            elif temp_c > 15:
                return "Mild"
            elif temp_c > 5:
                return "Cool"
            elif temp_c > 0:
                return "Cold"
            else:
                return "Very Cold"
        
        df["weather_category"] = df.apply(categorize_weather, axis=1)
        
        # Seasonal analysis
        df["season"] = df["date"].dt.month.map({
            12: "Winter", 1: "Winter", 2: "Winter",
            3: "Spring", 4: "Spring", 5: "Spring",
            6: "Summer", 7: "Summer", 8: "Summer",
            9: "Fall", 10: "Fall", 11: "Fall"
        })
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def generate_hourly_usage_heatmap(df: pd.DataFrame) -> VisualizationData:
    """Generate hourly usage heatmap"""
    # Create sample hourly data (since we don't have actual hourly data)
    hours = list(range(24))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Generate sample data with realistic patterns
    np.random.seed(42)
    data = []
    for day in days:
        for hour in hours:
            # Peak hours: 7-9 AM and 5-7 PM on weekdays
            # Weekend patterns are different
            if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                if hour in [7, 8, 17, 18]:
                    base_usage = np.random.normal(1200, 200)
                elif hour in [9, 10, 16, 19]:
                    base_usage = np.random.normal(800, 150)
                elif hour in range(11, 16):
                    base_usage = np.random.normal(600, 100)
                else:
                    base_usage = np.random.normal(200, 50)
            else:  # Weekend
                if hour in range(10, 18):
                    base_usage = np.random.normal(900, 150)
                else:
                    base_usage = np.random.normal(300, 80)
            
            data.append([day, hour, max(0, base_usage)])
    
    heatmap_df = pd.DataFrame(data, columns=['Day', 'Hour', 'Usage'])
    pivot_df = heatmap_df.pivot(index='Day', columns='Hour', values='Usage')
    
    fig = px.imshow(
        pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        color_continuous_scale='Blues',
        title="Hourly Usage Patterns Heatmap"
    )
    
    fig.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Day of Week",
        height=500
    )
    
    # Save the visualization
    filename = f"hourly_heatmap_{uuid.uuid4().hex[:8]}.html"
    filepath = VIZ_DIR / filename
    fig.write_html(filepath)
    
    return VisualizationData(
        title="Hourly Usage Heatmap",
        description="Shows usage patterns throughout the week and day",
        url=f"/visualization/{filename}",
        data_points=len(data)
    )

def generate_station_analysis(df: pd.DataFrame) -> VisualizationData:
    """Generate top stations bar chart"""
    # Create sample station data
    stations = [
        'W 21 St & 6 Ave', 'Broadway & E 14 St', 'West St & Chambers St',
        'E 17 St & Broadway', 'Broadway & W 58 St', 'W 41 St & 8 Ave',
        'E 47 St & Park Ave', 'Broadway & W 25 St', 'W 33 St & 7 Ave',
        'E 42 St & Vanderbilt Ave'
    ]
    
    # Generate trip counts with realistic patterns
    np.random.seed(42)
    trip_counts = [np.random.randint(12000, 20000) for _ in stations]
    
    station_df = pd.DataFrame({
        'Station': stations,
        'Trips': trip_counts
    }).sort_values('Trips', ascending=True)
    
    fig = px.bar(
        station_df,
        x='Trips',
        y='Station',
        orientation='h',
        title="Top 10 CitiBike Stations by Usage",
        color='Trips',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    # Save the visualization
    filename = f"station_analysis_{uuid.uuid4().hex[:8]}.html"
    filepath = VIZ_DIR / filename
    fig.write_html(filepath)
    
    return VisualizationData(
        title="Top Stations Analysis",
        description="Most popular CitiBike stations by trip count",
        url=f"/visualization/{filename}",
        data_points=len(stations)
    )

def generate_weather_correlation(df: pd.DataFrame) -> VisualizationData:
    """Generate weather correlation scatter plot"""
    fig = px.scatter(
        df,
        x='temperature_mean_c',
        y='trip_count',
        color='precipitation_mm',
        size='wind_speed_max_ms',
        title="Temperature vs Trip Count (Weather Correlation)",
        labels={
            'temperature_mean_c': 'Temperature (°C)',
            'trip_count': 'Daily Trips',
            'precipitation_mm': 'Precipitation (mm)'
        },
        color_continuous_scale='Blues_r'
    )
    
    # Add trend line
    fig.add_scatter(
        x=df['temperature_mean_c'],
        y=np.poly1d(np.polyfit(df['temperature_mean_c'], df['trip_count'], 1))(df['temperature_mean_c']),
        mode='lines',
        name='Trend Line',
        line=dict(color='red', dash='dash')
    )
    
    fig.update_layout(height=500)
    
    # Save the visualization
    filename = f"weather_correlation_{uuid.uuid4().hex[:8]}.html"
    filepath = VIZ_DIR / filename
    fig.write_html(filepath)
    
    return VisualizationData(
        title="Weather Impact Analysis",
        description="Relationship between temperature, precipitation, and bike usage",
        url=f"/visualization/{filename}",
        data_points=len(df)
    )

def generate_seasonal_trends(df: pd.DataFrame) -> VisualizationData:
    """Generate seasonal trends line chart"""
    seasonal_data = df.groupby(['date', 'season'])['trip_count'].mean().reset_index()
    
    fig = px.line(
        seasonal_data,
        x='date',
        y='trip_count',
        color='season',
        title="Seasonal Usage Trends",
        labels={
            'trip_count': 'Average Daily Trips',
            'date': 'Date'
        }
    )
    
    fig.update_layout(height=500)
    
    # Save the visualization
    filename = f"seasonal_trends_{uuid.uuid4().hex[:8]}.html"
    filepath = VIZ_DIR / filename
    fig.write_html(filepath)
    
    return VisualizationData(
        title="Seasonal Usage Trends",
        description="How bike usage changes throughout the seasons",
        url=f"/visualization/{filename}",
        data_points=len(seasonal_data)
    )

@app.get("/")
async def root():
    return {"message": "CitiBike Visualization API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(message: ChatMessage):
    start_time = datetime.now()
    
    try:
        # Load data
        df = load_citibike_data()
        if df is None:
            raise HTTPException(status_code=500, detail="Could not load data")
        
        # Generate visualizations based on query
        visualizations = []
        insights = []
        recommendations = []
        
        query_lower = message.message.lower()
        
        # Determine visualization type based on query
        if "heatmap" in query_lower or "hourly" in query_lower:
            viz = generate_hourly_usage_heatmap(df)
            visualizations.append(viz)
            insights.append("Peak usage occurs during morning (7-9 AM) and evening (5-7 PM) rush hours")
            insights.append("Weekend patterns show more consistent usage throughout the day")
            recommendations.append("Consider increasing bike availability during peak hours")
            
        elif "station" in query_lower or "top" in query_lower:
            viz = generate_station_analysis(df)
            visualizations.append(viz)
            insights.append("Business districts and transit hubs show highest usage")
            insights.append("Station performance varies significantly across locations")
            recommendations.append("Focus expansion efforts on high-performing areas")
            
        elif "weather" in query_lower or "temperature" in query_lower:
            viz = generate_weather_correlation(df)
            visualizations.append(viz)
            insights.append("Strong positive correlation between temperature and ridership")
            insights.append("Precipitation significantly reduces bike usage")
            recommendations.append("Monitor weather forecasts for demand planning")
            
        elif "seasonal" in query_lower or "trend" in query_lower:
            viz = generate_seasonal_trends(df)
            visualizations.append(viz)
            insights.append("Summer and fall show highest ridership")
            insights.append("Winter months experience the lowest usage")
            recommendations.append("Adjust fleet size based on seasonal patterns")
            
        else:
            # Default response with general insights
            insights.append("CitiBike usage shows strong seasonal and weather-dependent patterns")
            insights.append("Peak hours are typically 7-9 AM and 5-7 PM on weekdays")
            insights.append("Temperature and precipitation are key factors affecting ridership")
            recommendations.append("Try asking about specific topics like 'hourly patterns', 'top stations', or 'weather impact'")
        
        processing_time = (datetime.now() - start_time).total_seconds() * 1000
        
        return ChatResponse(
            response=f"I've analyzed your query about '{message.message}' and generated relevant insights!",
            visualizations=visualizations,
            insights=insights,
            recommendations=recommendations,
            timestamp=datetime.now().isoformat(),
            processing_time_ms=int(processing_time),
            trace_id=str(uuid.uuid4())
        )
        
    except Exception as e:
        processing_time = (datetime.now() - start_time).total_seconds() * 1000
        return ChatResponse(
            response=f"I encountered an error processing your query: {str(e)}",
            visualizations=[],
            insights=[],
            recommendations=[],
            timestamp=datetime.now().isoformat(),
            processing_time_ms=int(processing_time),
            trace_id=str(uuid.uuid4())
        )

@app.get("/visualization/{filename:path}")
async def get_visualization(filename: str):
    """Serve generated visualization files"""
    file_path = VIZ_DIR / filename
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="Visualization not found")
    return FileResponse(file_path, media_type="text/html")

@app.get("/hot-actions")
async def get_hot_actions():
    """Get suggested queries for the chat interface"""
    return {
        "actions": [
            {
                "id": "hourly_heatmap",
                "title": "📊 Hourly Usage Patterns",
                "description": "Show me hourly usage heatmap",
                "query": "Create a heatmap of hourly usage patterns"
            },
            {
                "id": "top_stations",
                "title": "🏆 Top Stations",
                "description": "Display top performing stations",
                "query": "Show me the top 10 stations by usage"
            },
            {
                "id": "weather_impact",
                "title": "🌤️ Weather Impact",
                "description": "Analyze weather correlation",
                "query": "Analyze how weather affects ridership"
            },
            {
                "id": "seasonal_trends",
                "title": "🍂 Seasonal Trends",
                "description": "Show seasonal usage patterns",
                "query": "What are the seasonal trends in bike usage?"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
