"""
Configuration file for LangChain CitiBike AI System
"""

import os
from typing import Dict, Any

# OpenAI Configuration
OPENAI_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY", "your-openai-api-key-here"),
    "model": "gpt-4",
    "temperature": 0.1,
    "max_tokens": 2000,
    "timeout": 30
}

# LangChain System Configuration
LANGCHAIN_CONFIG = {
    "project_name": "citibike-langchain-ai",
    "environment": "production",
    "max_conversation_length": 20,
    "enable_memory": True,
    "enable_streaming": True
}

# Server Configuration
SERVER_CONFIG = {
    "backend_host": "0.0.0.0",
    "backend_port": 8000,
    "streamlit_port": 8505,
    "cors_origins": ["*"],
    "request_timeout": 30,
    "max_request_size": "10MB"
}

# Phoenix Observability Configuration
PHOENIX_CONFIG = {
    "enabled": True,
    "project_name": "citibike-langchain-ai",
    "environment": "production",
    "export_traces": True,
    "trace_retention_days": 7
}

# Jupyter Kernel Configuration
JUPYTER_CONFIG = {
    "kernel_name": "python3",
    "timeout": 60,
    "max_memory_mb": 512,
    "enable_auto_restart": True
}

# Data Processing Configuration
DATA_CONFIG = {
    "max_rows_per_request": 10000,
    "sample_size_for_analysis": 1000,
    "enable_data_caching": True,
    "cache_ttl_seconds": 300
}

# Visualization Configuration
VISUALIZATION_CONFIG = {
    "default_chart_height": 500,
    "default_chart_width": 800,
    "enable_interactive_charts": True,
    "chart_theme": "plotly_white"
}

def get_config(config_type: str) -> Dict[str, Any]:
    """Get configuration by type"""
    configs = {
        "openai": OPENAI_CONFIG,
        "langchain": LANGCHAIN_CONFIG,
        "server": SERVER_CONFIG,
        "phoenix": PHOENIX_CONFIG,
        "jupyter": JUPYTER_CONFIG,
        "data": DATA_CONFIG,
        "visualization": VISUALIZATION_CONFIG
    }
    
    return configs.get(config_type, {})

def validate_config() -> bool:
    """Validate configuration settings"""
    errors = []
    
    # Check OpenAI API key
    if OPENAI_CONFIG["api_key"] == "your-openai-api-key-here":
        errors.append("OpenAI API key not configured")
    
    # Check server ports
    if SERVER_CONFIG["backend_port"] == SERVER_CONFIG["streamlit_port"]:
        errors.append("Backend and Streamlit ports cannot be the same")
    
    if errors:
        print("❌ Configuration errors:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("✅ Configuration is valid")
    return True

def print_config_summary():
    """Print configuration summary"""
    print("🤖 LangChain CitiBike AI System Configuration")
    print("=" * 50)
    print(f"OpenAI Model: {OPENAI_CONFIG['model']}")
    print(f"Backend Server: {SERVER_CONFIG['backend_host']}:{SERVER_CONFIG['backend_port']}")
    print(f"Streamlit Dashboard: localhost:{SERVER_CONFIG['streamlit_port']}")
    print(f"Phoenix Observability: {'Enabled' if PHOENIX_CONFIG['enabled'] else 'Disabled'}")
    print(f"Data Cache: {'Enabled' if DATA_CONFIG['enable_data_caching'] else 'Disabled'}")
    print("=" * 50)

if __name__ == "__main__":
    print_config_summary()
    validate_config()
