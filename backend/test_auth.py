#!/usr/bin/env python3
"""
Test authentication endpoints
"""

import requests
import json

API_BASE_URL = 'https://busybeeapp.onrender.com/api'

def test_register():
    """Test user registration"""
    print("🧪 Testing user registration...")
    
    test_user = {
        "username": "testuser123",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f'{API_BASE_URL}/register', json=test_user)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 201:
            print("✅ Registration successful!")
        else:
            print("❌ Registration failed")
            
    except Exception as e:
        print(f"❌ Network error: {e}")

def test_login():
    """Test user login"""
    print("\n🧪 Testing user login...")
    
    test_user = {
        "username": "testuser123",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f'{API_BASE_URL}/login', json=test_user)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Login successful!")
        else:
            print("❌ Login failed")
            
    except Exception as e:
        print(f"❌ Network error: {e}")

if __name__ == '__main__':
    test_register()
    test_login()
