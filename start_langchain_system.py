#!/usr/bin/env python3
"""
Startup script for the LangChain CitiBike AI System
Starts both the LangChain backend and Streamlit dashboard
"""

import os
import sys
import subprocess
import time
import signal
import threading
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        "langchain",
        "langchain-openai", 
        "fastapi",
        "streamlit",
        "phoenix",
        "openai"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements_langchain.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def check_openai_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your-openai-api-key-here":
        print("❌ OpenAI API key not set")
        print("Set it with: export OPENAI_API_KEY='your-actual-api-key'")
        return False
    
    print("✅ OpenAI API key is configured")
    return True

def start_langchain_backend():
    """Start the LangChain backend server"""
    print("🚀 Starting LangChain backend server...")
    
    try:
        # Start the backend server
        backend_process = subprocess.Popen([
            sys.executable, "backend/langchain_api_server.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a moment for startup
        time.sleep(3)
        
        # Check if server is running
        if backend_process.poll() is None:
            print("✅ LangChain backend server started successfully")
            return backend_process
        else:
            stdout, stderr = backend_process.communicate()
            print(f"❌ Failed to start backend server: {stderr.decode()}")
            return None
            
    except Exception as e:
        print(f"❌ Error starting backend server: {e}")
        return None

def start_streamlit_dashboard():
    """Start the Streamlit dashboard"""
    print("🚀 Starting Streamlit dashboard...")
    
    try:
        # Start Streamlit
        dashboard_process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", 
            "citibike_ultimate_dashboard.py", 
            "--server.port", "8505"
        ])
        
        print("✅ Streamlit dashboard started successfully")
        return dashboard_process
        
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        return None

def main():
    """Main startup function"""
    print("🤖 LangChain CitiBike AI System Startup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_dependencies():
        sys.exit(1)
    
    if not check_openai_key():
        sys.exit(1)
    
    print("\n🚀 Starting system components...")
    
    # Start backend server
    backend_process = start_langchain_backend()
    if not backend_process:
        print("❌ Cannot start system without backend server")
        sys.exit(1)
    
    # Wait a bit for backend to fully initialize
    time.sleep(2)
    
    # Start dashboard
    dashboard_process = start_streamlit_dashboard()
    if not dashboard_process:
        print("❌ Cannot start system without dashboard")
        backend_process.terminate()
        sys.exit(1)
    
    print("\n✅ LangChain CitiBike AI System is running!")
    print("=" * 50)
    print("📊 Streamlit Dashboard: http://localhost:8505")
    print("🔧 LangChain API: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("=" * 50)
    print("\nPress Ctrl+C to stop the system")
    
    def signal_handler(signum, frame):
        print("\n🛑 Shutting down system...")
        if backend_process:
            backend_process.terminate()
        if dashboard_process:
            dashboard_process.terminate()
        print("✅ System shutdown complete")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
            # Check if processes are still running
            if backend_process.poll() is not None:
                print("❌ Backend server stopped unexpectedly")
                break
            
            if dashboard_process.poll() is not None:
                print("❌ Dashboard stopped unexpectedly")
                break
                
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    main()
