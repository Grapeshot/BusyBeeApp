#!/usr/bin/env python3
"""
Test script to verify the app is ready for Railway deployment
"""

import os
import sys
import subprocess

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    try:
        import flask
        import flask_cors
        import sqlite3
        import datetime
        print("   ✅ All imports successful")
        return True
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False

def test_app_startup():
    """Test that the app can start without errors"""
    print("🧪 Testing app startup...")
    try:
        # Import the app
        from app import app, init_db
        
        # Test database initialization
        init_db()
        print("   ✅ Database initialization successful")
        
        # Test app creation
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("   ✅ App responds to requests")
                return True
            else:
                print(f"   ❌ App returned status {response.status_code}")
                return False
                
    except Exception as e:
        print(f"   ❌ App startup error: {e}")
        return False

def test_requirements():
    """Test that requirements.txt exists and is valid"""
    print("🧪 Testing requirements.txt...")
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip()
            if requirements:
                print("   ✅ requirements.txt exists and has content")
                return True
            else:
                print("   ❌ requirements.txt is empty")
                return False
    except FileNotFoundError:
        print("   ❌ requirements.txt not found")
        return False

def test_procfile():
    """Test that Procfile exists and is valid"""
    print("🧪 Testing Procfile...")
    try:
        with open('Procfile', 'r') as f:
            procfile = f.read().strip()
            if 'web:' in procfile:
                print("   ✅ Procfile exists and has web command")
                return True
            else:
                print("   ❌ Procfile missing web command")
                return False
    except FileNotFoundError:
        print("   ❌ Procfile not found")
        return False

def main():
    """Run all tests"""
    print("🚀 BusyBee Backend - Railway Deployment Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_requirements,
        test_procfile,
        test_app_startup
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready for Railway deployment.")
        return True
    else:
        print("❌ Some tests failed. Fix issues before deploying.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
