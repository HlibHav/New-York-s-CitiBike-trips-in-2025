"""
Enhanced Phoenix Integration for LangChain Multi-Agent System
Provides comprehensive observability for the CitiBike AI system
"""

import os
import time
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd

# Phoenix imports
import phoenix as px
from phoenix.trace.otel import Span, SpanKind
from phoenix.trace.attributes import SpanAttributes

class PhoenixLangChainMonitor:
    """Enhanced Phoenix monitoring for LangChain multi-agent system"""
    
    def __init__(self, project_name: str = "citibike-langchain-ai"):
        self.project_name = project_name
        self.client = px.Client()
        self.session = self.client.start_session(project_name=project_name)
        
        # Initialize tracing
        self._setup_tracing()
    
    def _setup_tracing(self):
        """Setup Phoenix tracing configuration"""
        # Configure tracing for LangChain components
        os.environ["PHOENIX_PROJECT_NAME"] = self.project_name
        os.environ["PHOENIX_ENVIRONMENT"] = "production"
    
    def trace_query_processing(self, query: str, user_id: str = None) -> Span:
        """Start tracing for query processing"""
        return Span(
            name="query_processing",
            kind=SpanKind.INTERNAL,
            attributes={
                "query": query[:200],  # Truncate for logging
                "query_length": len(query),
                "user_id": user_id or "anonymous",
                "timestamp": datetime.now().isoformat(),
                "system": "langchain-citibike-ai"
            }
        )
    
    def trace_agent_interaction(self, agent_name: str, operation: str, input_data: Any = None) -> Span:
        """Trace individual agent interactions"""
        attributes = {
            "agent_name": agent_name,
            "operation": operation,
            "timestamp": datetime.now().isoformat()
        }
        
        if input_data:
            if isinstance(input_data, str):
                attributes["input_preview"] = input_data[:200]
            elif isinstance(input_data, dict):
                attributes["input_keys"] = list(input_data.keys())
        
        return Span(
            name=f"{agent_name}_{operation}",
            kind=SpanKind.TOOL,
            attributes=attributes
        )
    
    def trace_code_execution(self, code: str, execution_time: float, success: bool, 
                           output_size: int = 0, error: str = None) -> Span:
        """Trace Jupyter code execution"""
        attributes = {
            "code_length": len(code),
            "execution_time_ms": execution_time * 1000,
            "success": success,
            "output_size": output_size,
            "timestamp": datetime.now().isoformat()
        }
        
        if error:
            attributes["error"] = error[:500]
        
        return Span(
            name="jupyter_code_execution",
            kind=SpanKind.TOOL,
            attributes=attributes
        )
    
    def trace_llm_call(self, model: str, prompt: str, response: str, 
                      tokens_used: int = 0, cost: float = 0) -> Span:
        """Trace LLM API calls"""
        return Span(
            name="llm_api_call",
            kind=SpanKind.TOOL,
            attributes={
                SpanAttributes.TOOL_NAME: "openai_chat",
                "model": model,
                "prompt_length": len(prompt),
                "response_length": len(response),
                "tokens_used": tokens_used,
                "estimated_cost": cost,
                "timestamp": datetime.now().isoformat()
            }
        )
    
    def trace_data_analysis(self, analysis_type: str, data_shape: tuple, 
                           metrics_calculated: List[str], insights_generated: int) -> Span:
        """Trace data analysis operations"""
        return Span(
            name="data_analysis",
            kind=SpanKind.TOOL,
            attributes={
                "analysis_type": analysis_type,
                "data_rows": data_shape[0] if len(data_shape) > 0 else 0,
                "data_columns": data_shape[1] if len(data_shape) > 1 else 0,
                "metrics_calculated": json.dumps(metrics_calculated),
                "insights_generated": insights_generated,
                "timestamp": datetime.now().isoformat()
            }
        )
    
    def trace_visualization_generation(self, chart_type: str, data_points: int, 
                                     generation_time: float) -> Span:
        """Trace visualization generation"""
        return Span(
            name="visualization_generation",
            kind=SpanKind.TOOL,
            attributes={
                "chart_type": chart_type,
                "data_points": data_points,
                "generation_time_ms": generation_time * 1000,
                "timestamp": datetime.now().isoformat()
            }
        )
    
    def log_system_metrics(self, metrics: Dict[str, Any]):
        """Log system performance metrics"""
        span = Span(
            name="system_metrics",
            kind=SpanKind.INTERNAL,
            attributes={
                **metrics,
                "timestamp": datetime.now().isoformat()
            }
        )
        return span
    
    def log_user_interaction(self, user_id: str, action: str, query: str, 
                           response_time: float, success: bool):
        """Log user interactions for analytics"""
        span = Span(
            name="user_interaction",
            kind=SpanKind.CLIENT,
            attributes={
                "user_id": user_id,
                "action": action,
                "query_preview": query[:100],
                "response_time_ms": response_time * 1000,
                "success": success,
                "timestamp": datetime.now().isoformat()
            }
        )
        return span
    
    def log_error(self, error_type: str, error_message: str, context: Dict[str, Any] = None):
        """Log system errors"""
        attributes = {
            "error_type": error_type,
            "error_message": error_message[:500],
            "timestamp": datetime.now().isoformat()
        }
        
        if context:
            attributes.update({f"context_{k}": str(v)[:200] for k, v in context.items()})
        
        span = Span(
            name="system_error",
            kind=SpanKind.INTERNAL,
            attributes=attributes
        )
        return span
    
    def get_performance_summary(self, time_window_hours: int = 24) -> Dict[str, Any]:
        """Get performance summary from Phoenix"""
        try:
            # This would typically query Phoenix for metrics
            # For now, return a mock summary
            return {
                "total_queries": 0,
                "average_response_time": 0,
                "success_rate": 0,
                "top_queries": [],
                "error_rate": 0,
                "time_window_hours": time_window_hours
            }
        except Exception as e:
            return {"error": f"Failed to get performance summary: {str(e)}"}
    
    def export_traces(self, output_file: str = None) -> str:
        """Export traces to file for analysis"""
        if output_file is None:
            output_file = f"phoenix_traces_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            # This would export actual traces from Phoenix
            # For now, create a sample export
            sample_traces = {
                "export_timestamp": datetime.now().isoformat(),
                "project_name": self.project_name,
                "traces": []
            }
            
            with open(output_file, 'w') as f:
                json.dump(sample_traces, f, indent=2)
            
            return output_file
        except Exception as e:
            return f"Failed to export traces: {str(e)}"
    
    def shutdown(self):
        """Shutdown Phoenix monitoring"""
        try:
            if self.session:
                self.session.close()
        except Exception as e:
            print(f"Error shutting down Phoenix: {e}")

# Global monitor instance
_phoenix_monitor = None

def get_phoenix_monitor() -> PhoenixLangChainMonitor:
    """Get or create the global Phoenix monitor instance"""
    global _phoenix_monitor
    
    if _phoenix_monitor is None:
        _phoenix_monitor = PhoenixLangChainMonitor()
    
    return _phoenix_monitor

def shutdown_phoenix():
    """Shutdown the global Phoenix monitor"""
    global _phoenix_monitor
    if _phoenix_monitor:
        _phoenix_monitor.shutdown()
        _phoenix_monitor = None
