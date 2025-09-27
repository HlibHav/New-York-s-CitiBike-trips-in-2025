#!/usr/bin/env python3
"""
Test script for the LangChain CitiBike AI System
"""

import os
import sys
import pandas as pd
import numpy as np

def test_imports():
    """Test if all required packages can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import langchain
        print("✅ LangChain imported successfully")
    except ImportError as e:
        print(f"❌ LangChain import failed: {e}")
        return False
    
    try:
        import openai
        print("✅ OpenAI imported successfully")
    except ImportError as e:
        print(f"❌ OpenAI import failed: {e}")
        return False
    
    try:
        import fastapi
        print("✅ FastAPI imported successfully")
    except ImportError as e:
        print(f"❌ FastAPI import failed: {e}")
        return False
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    return True

def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🔑 Testing OpenAI connection...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your-openai-api-key-here":
        print("❌ OpenAI API key not set")
        print("Set it with: export OPENAI_API_KEY='your-actual-api-key'")
        return False
    
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello, this is a test."}],
            max_tokens=10
        )
        
        print("✅ OpenAI API connection successful")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API connection failed: {e}")
        return False

def test_langchain_system():
    """Test the LangChain system"""
    print("\n🤖 Testing LangChain system...")
    
    try:
        from backend.langchain_agent_system import get_citibike_system
        
        # Create test data
        test_data = pd.DataFrame({
            'started_at': pd.date_range('2024-01-01', periods=100, freq='H'),
            'start_station_name': np.random.choice(['Station A', 'Station B', 'Station C'], 100),
            'end_station_name': np.random.choice(['Station X', 'Station Y', 'Station Z'], 100),
            'temperature': np.random.normal(20, 10, 100),
            'precipitation': np.random.exponential(1, 100)
        })
        
        # Initialize system
        system = get_citibike_system()
        system.load_data(test_data)
        
        print("✅ LangChain system initialized successfully")
        print(f"✅ Data loaded: {len(test_data)} rows")
        
        return True
        
    except Exception as e:
        print(f"❌ LangChain system test failed: {e}")
        return False

def test_api_server():
    """Test if API server can be imported"""
    print("\n🌐 Testing API server...")
    
    try:
        from backend.langchain_api_server import app
        print("✅ API server imported successfully")
        return True
        
    except Exception as e:
        print(f"❌ API server import failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 LangChain CitiBike AI System Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("OpenAI Connection", test_openai_connection),
        ("LangChain System", test_langchain_system),
        ("API Server", test_api_server)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! System is ready to use.")
        print("\n🚀 To start the system:")
        print("   python start_langchain_system.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("\n💡 To install missing dependencies:")
        print("   pip install -r requirements_langchain_simple.txt")

if __name__ == "__main__":
    main()
