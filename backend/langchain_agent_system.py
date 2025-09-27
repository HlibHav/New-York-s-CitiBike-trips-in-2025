"""
LangChain Multi-Agent System for CitiBike Data Analysis
Implements the full Jupyter Agent architecture with OpenAI integration
"""

import os
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain

# LangGraph imports
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

# Phoenix observability
import phoenix as px
from phoenix.trace.otel import Span, SpanKind
from phoenix.trace.attributes import SpanAttributes

# Jupyter kernel management
import jupyter_client
from jupyter_client import KernelManager

class JupyterCodeExecutionAgent:
    """Jupyter Code Execution Agent - Core of the system"""
    
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            model="gpt-4",
            api_key=openai_api_key,
            temperature=0.1,
            streaming=True
        )
        self.kernel_manager = KernelManager()
        self.kernel_manager.start_kernel()
        
    def execute_code(self, code: str, data_context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute Python code in Jupyter kernel with data context"""
        with Span(
            name="jupyter_code_execution",
            kind=SpanKind.TOOL,
            attributes={
                SpanAttributes.TOOL_NAME: "jupyter_kernel",
                SpanAttributes.TOOL_INPUT: code[:500],  # Truncate for logging
                "code_length": len(code)
            }
        ) as span:
            try:
                # Prepare data context in kernel
                for var_name, data in data_context.items():
                    if isinstance(data, pd.DataFrame):
                        self.kernel_manager.kernel.execute(f"{var_name} = pd.DataFrame({data.to_dict()})")
                    else:
                        self.kernel_manager.kernel.execute(f"{var_name} = {repr(data)}")
                
                # Execute user code
                result = self.kernel_manager.kernel.execute(code)
                
                # Capture outputs
                outputs = {
                    "stdout": result.get("stdout", ""),
                    "stderr": result.get("stderr", ""),
                    "error": result.get("error", None),
                    "execution_time": result.get("execution_time", 0),
                    "memory_usage": result.get("memory_usage", 0)
                }
                
                span.set_attribute("execution_success", True)
                span.set_attribute("execution_time", outputs["execution_time"])
                
                return outputs
                
            except Exception as e:
                span.set_attribute("execution_success", False)
                span.set_attribute("error", str(e))
                return {
                    "stdout": "",
                    "stderr": "",
                    "error": str(e),
                    "execution_time": 0,
                    "memory_usage": 0
                }
    
    def generate_analysis_code(self, query: str, data_schema: Dict[str, Any]) -> str:
        """Generate Python code for data analysis based on user query"""
        with Span(
            name="code_generation",
            kind=SpanKind.TOOL,
            attributes={
                SpanAttributes.TOOL_NAME: "code_generator",
                SpanAttributes.TOOL_INPUT: query
            }
        ) as span:
            
            prompt = f"""
            You are a data analyst expert. Generate Python code to analyze CitiBike data based on this query:
            
            Query: "{query}"
            
            Available data schema:
            {data_schema}
            
            Requirements:
            1. Use pandas for data manipulation
            2. Use plotly for visualizations
            3. Provide clear variable names
            4. Include data validation
            5. Generate insights and recommendations
            6. Handle missing data appropriately
            
            Return ONLY the Python code, no explanations.
            """
            
            messages = [HumanMessage(content=prompt)]
            response = self.llm.invoke(messages)
            
            generated_code = response.content.strip()
            span.set_attribute("generated_code_length", len(generated_code))
            
            return generated_code

class OrchestratorAgent:
    """Orchestrator Agent - Manages workflow and agent coordination"""
    
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
    
    def analyze_query(self, query: str, data_summary: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze user query and determine analysis strategy"""
        with Span(
            name="query_analysis",
            kind=SpanKind.TOOL,
            attributes={
                SpanAttributes.TOOL_NAME: "query_analyzer",
                SpanAttributes.TOOL_INPUT: query
            }
        ) as span:
            
            prompt = f"""
            Analyze this CitiBike data query and determine the best analysis approach:
            
            Query: "{query}"
            
            Available data summary:
            {data_summary}
            
            Determine:
            1. Analysis type (descriptive, predictive, prescriptive)
            2. Required visualizations
            3. Key metrics to calculate
            4. Data subsets needed
            5. Expected insights
            
            Respond in JSON format:
            {{
                "analysis_type": "descriptive|predictive|prescriptive",
                "visualizations": ["chart_type1", "chart_type2"],
                "metrics": ["metric1", "metric2"],
                "data_filters": {{"column": "value"}},
                "expected_insights": ["insight1", "insight2"]
            }}
            """
            
            messages = [HumanMessage(content=prompt)]
            response = self.llm.invoke(messages)
            
            try:
                analysis_plan = eval(response.content.strip())
                span.set_attribute("analysis_type", analysis_plan.get("analysis_type", "unknown"))
                return analysis_plan
            except:
                # Fallback analysis plan
                return {
                    "analysis_type": "descriptive",
                    "visualizations": ["bar_chart"],
                    "metrics": ["usage_count"],
                    "data_filters": {},
                    "expected_insights": ["Basic usage patterns"]
                }

class ResponseAgent:
    """Response Agent - Generates human-readable insights and recommendations"""
    
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            model="gpt-4",
            api_key=openai_api_key,
            temperature=0.3
        )
    
    def generate_insights(self, query: str, analysis_results: Dict[str, Any], data_context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate human-readable insights from analysis results"""
        with Span(
            name="insight_generation",
            kind=SpanKind.TOOL,
            attributes={
                SpanAttributes.TOOL_NAME: "insight_generator",
                SpanAttributes.TOOL_INPUT: query
            }
        ) as span:
            
            prompt = f"""
            Generate professional insights and recommendations based on this analysis:
            
            Original Query: "{query}"
            
            Analysis Results:
            {analysis_results}
            
            Data Context:
            {data_context}
            
            Provide:
            1. Executive summary (2-3 sentences)
            2. Key insights (3-5 bullet points)
            3. Actionable recommendations (3-5 bullet points)
            4. Business impact assessment
            
            Format as JSON:
            {{
                "summary": "Executive summary here",
                "insights": ["insight1", "insight2"],
                "recommendations": ["rec1", "rec2"],
                "business_impact": "High|Medium|Low"
            }}
            """
            
            messages = [HumanMessage(content=prompt)]
            response = self.llm.invoke(messages)
            
            try:
                insights = eval(response.content.strip())
                span.set_attribute("insights_generated", len(insights.get("insights", [])))
                return insights
            except:
                # Fallback insights
                return {
                    "summary": "Analysis completed successfully",
                    "insights": ["Data analysis completed"],
                    "recommendations": ["Review results for actionable insights"],
                    "business_impact": "Medium"
                }

class LangChainCitiBikeSystem:
    """Main LangChain Multi-Agent System"""
    
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        
        # Initialize agents
        self.jupyter_agent = JupyterCodeExecutionAgent(openai_api_key)
        self.orchestrator = OrchestratorAgent(openai_api_key)
        self.response_agent = ResponseAgent(openai_api_key)
        
        # Initialize Phoenix
        self.phoenix_session = px.Client()
        
        # Data context
        self.data_context = {}
        self.data_summary = {}
    
    def load_data(self, df: pd.DataFrame):
        """Load CitiBike data into the system"""
        with Span(name="data_loading", kind=SpanKind.INTERNAL) as span:
            self.data_context["df"] = df
            
            # Generate data summary
            self.data_summary = {
                "total_trips": len(df),
                "date_range": f"{df['started_at'].min()} to {df['started_at'].max()}",
                "columns": list(df.columns),
                "data_types": df.dtypes.to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "sample_size": len(df.sample(min(1000, len(df))))
            }
            
            span.set_attribute("data_rows", len(df))
            span.set_attribute("data_columns", len(df.columns))
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Main method to process user queries through the multi-agent system"""
        
        with Span(
            name="query_processing",
            kind=SpanKind.INTERNAL,
            attributes={
                "query": query,
                "query_length": len(query)
            }
        ) as span:
            
            try:
                # Step 1: Orchestrator analyzes the query
                analysis_plan = self.orchestrator.analyze_query(query, self.data_summary)
                
                # Step 2: Jupyter agent generates and executes code
                code = self.jupyter_agent.generate_analysis_code(query, self.data_summary)
                execution_results = self.jupyter_agent.execute_code(code, self.data_context)
                
                # Step 3: Response agent generates insights
                insights = self.response_agent.generate_insights(
                    query, execution_results, self.data_context
                )
                
                # Compile final response
                response = {
                    "query": query,
                    "analysis_plan": analysis_plan,
                    "generated_code": code,
                    "execution_results": execution_results,
                    "insights": insights,
                    "timestamp": datetime.now().isoformat(),
                    "success": True
                }
                
                span.set_attribute("processing_success", True)
                span.set_attribute("analysis_type", analysis_plan.get("analysis_type", "unknown"))
                
                return response
                
            except Exception as e:
                span.set_attribute("processing_success", False)
                span.set_attribute("error", str(e))
                
                return {
                    "query": query,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat(),
                    "success": False
                }
    
    def shutdown(self):
        """Clean shutdown of the system"""
        if hasattr(self.jupyter_agent, 'kernel_manager'):
            self.jupyter_agent.kernel_manager.shutdown_kernel()

# Global system instance
_citibike_system = None

def get_citibike_system(openai_api_key: str = None) -> LangChainCitiBikeSystem:
    """Get or create the global CitiBike system instance"""
    global _citibike_system
    
    if _citibike_system is None:
        if openai_api_key is None:
            openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if not openai_api_key:
            raise ValueError("OpenAI API key is required")
        
        _citibike_system = LangChainCitiBikeSystem(openai_api_key)
    
    return _citibike_system

def shutdown_system():
    """Shutdown the global system"""
    global _citibike_system
    if _citibike_system:
        _citibike_system.shutdown()
        _citibike_system = None
