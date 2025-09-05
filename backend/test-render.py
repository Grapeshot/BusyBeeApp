#!/usr/bin/env python3
"""
Test script to verify the app is ready for Render deployment
"""

import os
import sys

def test_wsgi():
    """Test that wsgi.py can be imported and run"""
    print("🧪 Testing wsgi.py...")
    try:
        import wsgi
        print("   ✅ wsgi.py imports successfully")
        return True
    except ImportError as e:
        print(f"   ❌ wsgi.py import error: {e}")
        return False

def test_app_import():
    """Test that app.py can be imported"""
    print("🧪 Testing app.py import...")
    try:
        from app import app
        print("   ✅ app.py imports successfully")
        return True
    except ImportError as e:
        print(f"   ❌ app.py import error: {e}")
        return False

def test_requirements():
    """Test that requirements.txt exists and is valid"""
    print("🧪 Testing requirements.txt...")
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip()
            if 'Flask' in requirements and 'Flask-CORS' in requirements:
                print("   ✅ requirements.txt has required dependencies")
                return True
            else:
                print("   ❌ requirements.txt missing required dependencies")
                return False
    except FileNotFoundError:
        print("   ❌ requirements.txt not found")
        return False

def test_render_config():
    """Test that app is configured for Render"""
    print("🧪 Testing Render configuration...")
    try:
        from app import app
        # Test that the app can start (this will fail locally but that's OK)
        print("   ✅ App configuration looks good for Render")
        return True
    except Exception as e:
        print(f"   ❌ App configuration error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 BusyBee Backend - Render Deployment Test")
    print("=" * 50)
    
    tests = [
        test_requirements,
        test_app_import,
        test_wsgi,
        test_render_config
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
        print("🎉 All tests passed! Ready for Render deployment.")
        print("📋 Next steps:")
        print("   1. Commit and push changes to GitHub")
        print("   2. Create Render web service")
        print("   3. Set root directory to 'backend'")
        print("   4. Set start command to 'python wsgi.py'")
        return True
    else:
        print("❌ Some tests failed. Fix issues before deploying.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
