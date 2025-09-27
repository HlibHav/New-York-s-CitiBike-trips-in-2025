"""
FastAPI Server for LangChain CitiBike AI System
Connects Streamlit dashboard with the multi-agent LangChain backend
"""

import os
import time
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd
import json

# FastAPI imports
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# LangChain system imports
from backend.langchain_agent_system import get_citibike_system, shutdown_system
from backend.phoenix_langchain_monitor import get_phoenix_monitor, shutdown_phoenix

# Initialize FastAPI app
app = FastAPI(
    title="CitiBike LangChain AI API",
    description="Multi-agent AI system for CitiBike data analysis",
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
    chart_data: Optional[Dict[str, Any]] = None
    generated_code: Optional[str] = None
    execution_time: float
    success: bool
    error: Optional[str] = None
    timestamp: str

class DataLoadRequest(BaseModel):
    data: Dict[str, Any] = Field(..., description="CitiBike data to load")
    data_type: str = Field("dataframe", description="Type of data being loaded")

class SystemStatusResponse(BaseModel):
    status: str
    agents_ready: bool
    phoenix_connected: bool
    data_loaded: bool
    uptime: float
    total_queries: int

# Global variables
citibike_system = None
phoenix_monitor = None
startup_time = time.time()
total_queries = 0

@app.on_event("startup")
async def startup_event():
    """Initialize the LangChain system on startup"""
    global citibike_system, phoenix_monitor
    
    try:
        # Initialize Phoenix monitoring
        phoenix_monitor = get_phoenix_monitor()
        
        # Initialize LangChain system
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        citibike_system = get_citibike_system(openai_api_key)
        
        print("✅ LangChain CitiBike AI System initialized successfully")
        
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Clean shutdown of the system"""
    global citibike_system, phoenix_monitor
    
    try:
        if citibike_system:
            citibike_system.shutdown()
        
        if phoenix_monitor:
            phoenix_monitor.shutdown()
        
        print("✅ System shutdown completed")
        
    except Exception as e:
        print(f"❌ Error during shutdown: {e}")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "CitiBike LangChain AI API",
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
    global citibike_system, phoenix_monitor, total_queries
    
    return SystemStatusResponse(
        status="running",
        agents_ready=citibike_system is not None,
        phoenix_connected=phoenix_monitor is not None,
        data_loaded=len(citibike_system.data_context) > 0 if citibike_system else False,
        uptime=time.time() - startup_time,
        total_queries=total_queries
    )

@app.post("/load-data")
async def load_data(request: DataLoadRequest):
    """Load CitiBike data into the system"""
    global citibike_system, phoenix_monitor
    
    if not citibike_system:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    try:
        start_time = time.time()
        
        # Convert data to DataFrame
        if request.data_type == "dataframe":
            df = pd.DataFrame(request.data)
        else:
            raise ValueError(f"Unsupported data type: {request.data_type}")
        
        # Load data into system
        citibike_system.load_data(df)
        
        # Log data loading
        if phoenix_monitor:
            phoenix_monitor.log_system_metrics({
                "data_rows": len(df),
                "data_columns": len(df.columns),
                "load_time_ms": (time.time() - start_time) * 1000
            })
        
        return {
            "message": "Data loaded successfully",
            "rows": len(df),
            "columns": len(df.columns),
            "load_time": time.time() - start_time
        }
        
    except Exception as e:
        if phoenix_monitor:
            phoenix_monitor.log_error("data_loading_error", str(e), {"data_type": request.data_type})
        
        raise HTTPException(status_code=400, detail=f"Failed to load data: {str(e)}")

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest, background_tasks: BackgroundTasks):
    """Process user query through the LangChain multi-agent system"""
    global citibike_system, phoenix_monitor, total_queries
    
    if not citibike_system:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    start_time = time.time()
    total_queries += 1
    
    try:
        # Start Phoenix tracing
        trace_span = None
        if phoenix_monitor:
            trace_span = phoenix_monitor.trace_query_processing(
                request.query, request.user_id
            )
        
        # Process query through LangChain system
        result = citibike_system.process_query(request.query)
        
        execution_time = time.time() - start_time
        
        if result["success"]:
            # Extract insights and recommendations
            insights = result.get("insights", {}).get("insights", [])
            recommendations = result.get("insights", {}).get("recommendations", [])
            summary = result.get("insights", {}).get("summary", "Analysis completed")
            
            response = QueryResponse(
                query=request.query,
                response=summary,
                insights=insights,
                recommendations=recommendations,
                generated_code=result.get("generated_code"),
                execution_time=execution_time,
                success=True,
                timestamp=datetime.now().isoformat()
            )
            
            # Log successful interaction
            if phoenix_monitor:
                phoenix_monitor.log_user_interaction(
                    request.user_id or "anonymous",
                    "query_processed",
                    request.query,
                    execution_time,
                    True
                )
            
            return response
            
        else:
            # Handle error case
            error_msg = result.get("error", "Unknown error occurred")
            
            response = QueryResponse(
                query=request.query,
                response="I encountered an error while processing your query.",
                insights=[],
                recommendations=["Please try rephrasing your question or ask about a different aspect of the data."],
                execution_time=execution_time,
                success=False,
                error=error_msg,
                timestamp=datetime.now().isoformat()
            )
            
            # Log error
            if phoenix_monitor:
                phoenix_monitor.log_error("query_processing_error", error_msg, {
                    "query": request.query,
                    "user_id": request.user_id
                })
            
            return response
            
    except Exception as e:
        execution_time = time.time() - start_time
        
        # Log system error
        if phoenix_monitor:
            phoenix_monitor.log_error("system_error", str(e), {
                "query": request.query,
                "user_id": request.user_id
            })
        
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
                "query": "Create a heatmap showing hourly usage patterns throughout the week",
                "description": "Analyze peak usage times and daily patterns"
            },
            {
                "id": "top_stations",
                "title": "🏆 Top Performing Stations",
                "query": "Show me the top 10 most popular CitiBike stations with usage statistics",
                "description": "Identify high-traffic locations for expansion planning"
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
                "query": "Predict future demand based on historical patterns and trends",
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

@app.get("/performance")
async def get_performance_metrics():
    """Get system performance metrics"""
    global phoenix_monitor
    
    if not phoenix_monitor:
        raise HTTPException(status_code=503, detail="Phoenix monitoring not available")
    
    try:
        summary = phoenix_monitor.get_performance_summary()
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get performance metrics: {str(e)}")

@app.post("/export-traces")
async def export_traces():
    """Export Phoenix traces for analysis"""
    global phoenix_monitor
    
    if not phoenix_monitor:
        raise HTTPException(status_code=503, detail="Phoenix monitoring not available")
    
    try:
        output_file = phoenix_monitor.export_traces()
        return {
            "message": "Traces exported successfully",
            "file": output_file
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to export traces: {str(e)}")

# WebSocket endpoint for real-time communication (optional)
@app.websocket("/ws")
async def websocket_endpoint(websocket):
    """WebSocket endpoint for real-time communication"""
    await websocket.accept()
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Process query
            if message.get("type") == "query":
                query_request = QueryRequest(**message.get("data", {}))
                
                # Process through the system (simplified for WebSocket)
                result = citibike_system.process_query(query_request.query)
                
                # Send response back
                await websocket.send_text(json.dumps({
                    "type": "response",
                    "data": result
                }))
            
            elif message.get("type") == "ping":
                await websocket.send_text(json.dumps({
                    "type": "pong",
                    "timestamp": datetime.now().isoformat()
                }))
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    
    # Set environment variables
    os.environ.setdefault("OPENAI_API_KEY", "your-openai-api-key-here")
    
    # Run the server
    uvicorn.run(
        "backend.langchain_api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
