#!/usr/bin/env python3
"""
Working startup script for LangChain CitiBike AI System
Uses simplified components that actually work
"""

import os
import sys
import subprocess
import time
import signal
from pathlib import Path

def check_openai_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your-openai-api-key-here":
        print("❌ OpenAI API key not set")
        print("Please set it with: export OPENAI_API_KEY='your-actual-api-key'")
        print("\nTo get an API key:")
        print("1. Go to https://platform.openai.com/api-keys")
        print("2. Create a new API key")
        print("3. Copy the key and set it as an environment variable")
        return False
    
    print("✅ OpenAI API key is configured")
    return True

def test_system_imports():
    """Test if system components can be imported"""
    print("🧪 Testing system components...")
    
    try:
        from backend.simple_langchain_system import get_simple_system
        print("✅ Simple LangChain system imported")
        
        from backend.simple_api_server import app
        print("✅ Simple API server imported")
        
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False

def start_backend_server():
    """Start the simple LangChain backend server"""
    print("🚀 Starting simple LangChain backend server...")
    
    try:
        # Start the backend server
        backend_process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "backend.simple_api_server:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for startup
        time.sleep(3)
        
        # Check if server is running
        if backend_process.poll() is None:
            print("✅ Simple LangChain backend server started successfully")
            print("   📡 API available at: http://localhost:8000")
            print("   📚 Docs available at: http://localhost:8000/docs")
            return backend_process
        else:
            stdout, stderr = backend_process.communicate()
            print(f"❌ Failed to start backend server")
            print(f"Error: {stderr.decode()}")
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
        print("   📊 Dashboard available at: http://localhost:8505")
        return dashboard_process
        
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        return None

def main():
    """Main startup function"""
    print("🤖 LangChain CitiBike AI System (Working Version)")
    print("=" * 55)
    
    # Check OpenAI API key
    if not check_openai_key():
        print("\n💡 You can still run the dashboard without AI features:")
        print("   streamlit run citibike_ultimate_dashboard.py --server.port 8505")
        sys.exit(1)
    
    # Test system components
    if not test_system_imports():
        print("\n❌ System components test failed")
        sys.exit(1)
    
    print("\n🚀 Starting system components...")
    
    # Start backend server
    backend_process = start_backend_server()
    if not backend_process:
        print("❌ Cannot start system without backend server")
        sys.exit(1)
    
    # Wait for backend to initialize
    time.sleep(2)
    
    # Start dashboard
    dashboard_process = start_streamlit_dashboard()
    if not dashboard_process:
        print("❌ Cannot start system without dashboard")
        backend_process.terminate()
        sys.exit(1)
    
    print("\n✅ LangChain CitiBike AI System is running!")
    print("=" * 55)
    print("📊 Streamlit Dashboard: http://localhost:8505")
    print("🔧 LangChain API: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("=" * 55)
    print("\n🎯 Features available:")
    print("   • Real AI analysis powered by OpenAI GPT-4")
    print("   • Natural language query processing")
    print("   • Intelligent insights and recommendations")
    print("   • Interactive dashboard with chat interface")
    print("   • Fallback system for reliability")
    print("\n💬 Try asking questions like:")
    print("   • 'Show me trips on the map'")
    print("   • 'Identify optimal staffing periods'")
    print("   • 'Analyze peak usage patterns'")
    print("   • 'What are the revenue trends?'")
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
