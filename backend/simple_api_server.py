"""
Simplified FastAPI Server for LangChain CitiBike AI System
Works with minimal dependencies
"""

import os
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd

# FastAPI imports
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Simple LangChain system
from backend.simple_langchain_system import get_simple_system

# Initialize FastAPI app
app = FastAPI(
    title="CitiBike Simple LangChain AI API",
    description="Simplified multi-agent AI system for CitiBike data analysis",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class QueryRequest(BaseModel):
    query: str = Field(..., description="User query for data analysis")
    user_id: Optional[str] = Field(None, description="User identifier for tracking")
    session_id: Optional[str] = Field(None, description="Session identifier")

class QueryResponse(BaseModel):
    query: str
    response: str
    insights: List[str]
    recommendations: List[str]
    business_impact: str
    analysis_type: str
    execution_time: float
    success: bool
    error: Optional[str] = None
    timestamp: str

class DataLoadRequest(BaseModel):
    data: Dict[str, Any] = Field(..., description="CitiBike data to load")
    data_type: str = Field("dataframe", description="Type of data being loaded")

class SystemStatusResponse(BaseModel):
    status: str
    system_ready: bool
    data_loaded: bool
    uptime: float

# Global variables
simple_system = None
startup_time = time.time()

@app.on_event("startup")
async def startup_event():
    """Initialize the simple LangChain system on startup"""
    global simple_system
    
    try:
        # Initialize simple system
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        simple_system = get_simple_system(openai_api_key)
        
        print("✅ Simple LangChain CitiBike AI System initialized successfully")
        
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        raise

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "CitiBike Simple LangChain AI API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": time.time() - startup_time
    }

@app.get("/status", response_model=SystemStatusResponse)
async def get_system_status():
    """Get system status"""
    global simple_system
    
    return SystemStatusResponse(
        status="running",
        system_ready=simple_system is not None,
        data_loaded=len(simple_system.data_context) > 0 if simple_system else False,
        uptime=time.time() - startup_time
    )

@app.post("/load-data")
async def load_data(request: DataLoadRequest):
    """Load CitiBike data into the system"""
    global simple_system
    
    if not simple_system:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    try:
        start_time = time.time()
        
        # Convert data to DataFrame
        if request.data_type == "dataframe":
            df = pd.DataFrame(request.data)
        else:
            raise ValueError(f"Unsupported data type: {request.data_type}")
        
        # Load data into system
        simple_system.load_data(df)
        
        return {
            "message": "Data loaded successfully",
            "rows": len(df),
            "columns": len(df.columns),
            "load_time": time.time() - start_time
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to load data: {str(e)}")

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process user query through the simple LangChain system"""
    global simple_system
    
    if not simple_system:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    try:
        # Process query
        result = simple_system.analyze_query(request.query)
        
        response = QueryResponse(
            query=result["query"],
            response=result["response"],
            insights=result["insights"],
            recommendations=result["recommendations"],
            business_impact=result["business_impact"],
            analysis_type=result["analysis_type"],
            execution_time=result["execution_time"],
            success=result["success"],
            error=result.get("error"),
            timestamp=result["timestamp"]
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.get("/hot-actions")
async def get_hot_actions():
    """Get predefined hot actions for quick analysis"""
    return {
        "hot_actions": [
            {
                "id": "hourly_heatmap",
                "title": "📊 Hourly Usage Patterns",
                "query": "Analyze hourly usage patterns and peak times throughout the week",
                "description": "Understand when bikes are most and least used"
            },
            {
                "id": "top_stations",
                "title": "🏆 Top Performing Stations",
                "query": "Identify the top 10 most popular CitiBike stations with usage statistics",
                "description": "Find the busiest locations for expansion planning"
            },
            {
                "id": "weather_impact",
                "title": "🌤️ Weather Impact Analysis",
                "query": "Analyze how weather conditions affect bike ridership patterns",
                "description": "Understand weather influence on demand"
            },
            {
                "id": "seasonal_trends",
                "title": "🍂 Seasonal Trends",
                "query": "Show seasonal patterns and trends in bike usage throughout the year",
                "description": "Identify seasonal variations and planning insights"
            },
            {
                "id": "demand_forecasting",
                "title": "🔮 Demand Forecasting",
                "query": "Predict future demand based on historical patterns and provide forecasting insights",
                "description": "Generate demand predictions for operational planning"
            },
            {
                "id": "operational_efficiency",
                "title": "⚡ Operational Efficiency",
                "query": "Analyze operational efficiency metrics and identify optimization opportunities",
                "description": "Find ways to improve service efficiency"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    
    # Set environment variables
    os.environ.setdefault("OPENAI_API_KEY", "your-openai-api-key-here")
    
    # Run the server
    uvicorn.run(
        "backend.simple_api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
