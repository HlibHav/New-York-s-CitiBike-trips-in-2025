# 🤖 LangChain CitiBike AI System

A comprehensive multi-agent AI system for CitiBike data analysis, powered by LangChain, OpenAI GPT-4, and Phoenix observability.

## 🚀 Features

### Core AI Capabilities
- **Multi-Agent Architecture**: Orchestrator, Jupyter Code Execution, and Response agents
- **Real AI Analysis**: Powered by OpenAI GPT-4 for intelligent data insights
- **Dynamic Code Generation**: AI generates and executes Python code for data analysis
- **Natural Language Processing**: Understand complex queries in plain English
- **Real-time Visualizations**: Interactive charts and graphs generated on-demand

### Advanced Features
- **Phoenix Observability**: Complete system monitoring and tracing
- **Jupyter Integration**: Sandboxed code execution environment
- **Conversation Memory**: Maintains context across queries
- **Hot Actions**: Quick access to common analyses
- **Fallback System**: Graceful degradation when AI is unavailable

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   FastAPI        │    │   LangChain     │
│   Dashboard     │◄──►│   API Server     │◄──►│   Multi-Agent   │
│   (Frontend)    │    │   (Backend)      │    │   System        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       ▼
         │                       │              ┌─────────────────┐
         │                       │              │   Phoenix       │
         │                       │              │   Observability │
         │                       │              └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User          │    │   OpenAI         │    │   Jupyter       │
│   Interface     │    │   GPT-4 API      │    │   Kernel        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- OpenAI API key
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd citibike-ai-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements_langchain.txt
   ```

3. **Set up OpenAI API key**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

4. **Start the system**
   ```bash
   python start_langchain_system.py
   ```

5. **Access the dashboard**
   - Streamlit Dashboard: http://localhost:8505
   - API Documentation: http://localhost:8000/docs

## 📊 Usage

### Quick Actions
The dashboard provides quick action buttons for common analyses:
- **📊 Usage Patterns**: Hourly heatmaps and peak time analysis
- **🏆 Top Stations**: Most popular stations with statistics
- **🌤️ Weather Impact**: Weather correlation analysis
- **🍂 Seasonal Trends**: Seasonal pattern analysis
- **🔮 Demand Forecasting**: Predictive analysis
- **⚡ Efficiency Analysis**: Operational optimization

### Custom Queries
Ask natural language questions:
- "Show me trips on the map"
- "Identify optimal staffing periods"
- "Analyze user behavior patterns"
- "What are the revenue trends?"
- "How can we improve efficiency?"

### API Usage
```python
import requests

# Query the AI system
response = requests.post("http://localhost:8000/query", json={
    "query": "Analyze peak usage patterns",
    "user_id": "user123"
})

result = response.json()
print(result["response"])
print(result["insights"])
```

## 🔧 Configuration

Edit `config_langchain.py` to customize:
- OpenAI model settings
- Server ports and timeouts
- Phoenix observability
- Data processing limits
- Visualization settings

## 📈 Monitoring

### Phoenix Dashboard
Access Phoenix observability at: http://localhost:6006

Monitor:
- Query processing times
- Agent interactions
- Code execution metrics
- Error rates and patterns
- User interaction analytics

### Performance Metrics
- Average response time
- Success/failure rates
- Token usage and costs
- System resource utilization

## 🧪 Development

### Project Structure
```
├── backend/
│   ├── langchain_agent_system.py    # Core LangChain system
│   ├── langchain_api_server.py      # FastAPI server
│   └── phoenix_langchain_monitor.py # Observability
├── citibike_ultimate_dashboard.py   # Streamlit dashboard
├── config_langchain.py              # Configuration
├── start_langchain_system.py        # Startup script
└── requirements_langchain.txt       # Dependencies
```

### Adding New Agents
1. Create agent class in `langchain_agent_system.py`
2. Add to system initialization
3. Update API endpoints
4. Add Phoenix tracing

### Custom Analysis Functions
1. Add function to dashboard
2. Update query processing logic
3. Add visualization support
4. Test with Phoenix monitoring

## 🔍 Troubleshooting

### Common Issues

**OpenAI API Key Not Set**
```bash
export OPENAI_API_KEY="your-actual-api-key"
```

**Port Already in Use**
```bash
# Change ports in config_langchain.py
SERVER_CONFIG["backend_port"] = 8001
```

**Dependencies Missing**
```bash
pip install -r requirements_langchain.txt
```

**Phoenix Connection Issues**
```bash
# Check Phoenix is running
pip install phoenix
python -m phoenix.main
```

### Debug Mode
Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 API Reference

### Endpoints

**POST /query**
- Process natural language queries
- Returns AI-generated insights and recommendations

**POST /load-data**
- Load CitiBike data into the system
- Required for analysis

**GET /status**
- System health and status
- Agent availability

**GET /performance**
- Performance metrics
- Usage statistics

**WebSocket /ws**
- Real-time communication
- Streaming responses

### Response Format
```json
{
  "query": "user question",
  "response": "AI analysis summary",
  "insights": ["insight1", "insight2"],
  "recommendations": ["rec1", "rec2"],
  "execution_time": 2.5,
  "success": true,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## 🚀 Deployment

### Production Deployment
1. Set production OpenAI API key
2. Configure Phoenix for production
3. Set up proper logging
4. Configure security settings
5. Deploy with Docker or cloud platform

### Docker Deployment
```dockerfile
FROM python:3.9-slim
COPY requirements_langchain.txt .
RUN pip install -r requirements_langchain.txt
COPY . .
EXPOSE 8000 8505
CMD ["python", "start_langchain_system.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- GitHub Issues: Report bugs and feature requests
- Documentation: Check README files
- Community: Join our discussions

---

**Built with ❤️ using LangChain, OpenAI, and Phoenix**
