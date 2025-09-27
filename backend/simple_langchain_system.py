"""
Simplified LangChain System for CitiBike Data Analysis
Works without complex dependencies like Phoenix and Jupyter
"""

import os
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd
import numpy as np

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferMemory

class SimpleLangChainSystem:
    """Simplified LangChain system for CitiBike analysis"""
    
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            model="gpt-4",
            api_key=openai_api_key,
            temperature=0.1
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.data_context = {}
        self.data_summary = {}
    
    def load_data(self, df: pd.DataFrame):
        """Load CitiBike data into the system"""
        self.data_context["df"] = df
        
        # Generate data summary - handle different date column names
        date_column = None
        for col in ['date', 'started_at', 'start_time', 'datetime']:
            if col in df.columns:
                date_column = col
                break
        
        if date_column:
            date_range = f"{df[date_column].min()} to {df[date_column].max()}"
        else:
            date_range = "No date column found"
        
        self.data_summary = {
            "total_trips": len(df),
            "date_range": date_range,
            "date_column": date_column,
            "columns": list(df.columns),
            "data_types": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "sample_size": len(df.sample(min(1000, len(df))))
        }
    
    def analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze user query and provide insights"""
        start_time = time.time()
        
        try:
            # Create analysis prompt
            prompt = f"""
            You are a CitiBike data analyst. Analyze this query and provide insights:
            
            Query: "{query}"
            
            Available data summary:
            - Total trips: {self.data_summary.get('total_trips', 0)}
            - Date range: {self.data_summary.get('date_range', 'Unknown')}
            - Columns: {self.data_summary.get('columns', [])}
            - Sample size: {self.data_summary.get('sample_size', 0)}
            
            Provide a comprehensive analysis with:
            1. Executive summary (2-3 sentences)
            2. Key insights (3-5 bullet points)
            3. Actionable recommendations (3-5 bullet points)
            4. Business impact assessment
            
            Format your response as JSON:
            {{
                "summary": "Executive summary here",
                "insights": ["insight1", "insight2", "insight3"],
                "recommendations": ["rec1", "rec2", "rec3"],
                "business_impact": "High|Medium|Low",
                "analysis_type": "descriptive|predictive|prescriptive"
            }}
            """
            
            # Get AI response
            messages = [HumanMessage(content=prompt)]
            response = self.llm.invoke(messages)
            
            # Parse response
            try:
                import json
                analysis_result = json.loads(response.content.strip())
            except:
                # Fallback if JSON parsing fails
                analysis_result = {
                    "summary": response.content[:200] + "...",
                    "insights": ["Analysis completed successfully"],
                    "recommendations": ["Review the detailed response above"],
                    "business_impact": "Medium",
                    "analysis_type": "descriptive"
                }
            
            execution_time = time.time() - start_time
            
            return {
                "query": query,
                "response": analysis_result.get("summary", "Analysis completed"),
                "insights": analysis_result.get("insights", []),
                "recommendations": analysis_result.get("recommendations", []),
                "business_impact": analysis_result.get("business_impact", "Medium"),
                "analysis_type": analysis_result.get("analysis_type", "descriptive"),
                "execution_time": execution_time,
                "success": True,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            return {
                "query": query,
                "response": f"I encountered an error while analyzing your query: {str(e)}",
                "insights": [],
                "recommendations": ["Please try rephrasing your question"],
                "business_impact": "Low",
                "analysis_type": "descriptive",
                "execution_time": execution_time,
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

# Global system instance
_simple_system = None

def get_simple_system(openai_api_key: str = None) -> SimpleLangChainSystem:
    """Get or create the global simple system instance"""
    global _simple_system
    
    if _simple_system is None:
        if openai_api_key is None:
            openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if not openai_api_key:
            raise ValueError("OpenAI API key is required")
        
        _simple_system = SimpleLangChainSystem(openai_api_key)
    
    return _simple_system
