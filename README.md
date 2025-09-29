# Main CitiBike Analytics Dashboard

## Project Structure

```
├── app.py                          # Main Streamlit dashboard
├── requirements.txt                # Main dependencies
├── backend/                        # Backend services
│   ├── langchain_agent_system.py
│   ├── langchain_api_server.py
│   └── ...
├── frontend/                       # Frontend components
│   └── chat_widget.html
├── notebooks/                      # Jupyter notebooks
│   ├── citibike_*.ipynb
│   └── ...
├── data/                          # Data files
│   ├── *.csv
│   └── *.html
├── config/                        # Configuration files
│   ├── *.json
│   ├── config_*.py
│   └── requirements_*.txt
├── scripts/                       # Utility scripts
│   ├── start_*.py
│   ├── test_*.py
│   └── st_dashboard_Part_2.py
├── docs/                          # Documentation
│   ├── README.md
│   ├── Plan.md
│   └── README_LANGCHAIN.md
└── tests/                         # Test files
```

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Features

- Interactive CitiBike analytics dashboard
- Weather correlation analysis
- Station performance mapping
- Seasonal usage patterns
- Advanced statistical visualizations

## Live Dashboard

🌟 **Live Dashboard**: [citibike2024.streamlit.app](https://citibike2024.streamlit.app/)

*🚴‍♂️ Transforming urban mobility data into actionable insights through advanced analytics and interactive visualization.*
