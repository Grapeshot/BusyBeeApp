import requests
import json
import time

# Base URL for the API
BASE_URL = 'http://localhost:5000/api'

def test_api():
    """Test all API endpoints"""
    print("🧪 Testing BusyBee API endpoints...")
    
    # Test health check
    print("\n1. Testing health check...")
    try:
        response = requests.get(f'{BASE_URL}/health')
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test getting tasks (should be empty initially)
    print("\n2. Testing GET /api/tasks (should be empty)...")
    try:
        response = requests.get(f'{BASE_URL}/tasks')
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test creating a task
    print("\n3. Testing POST /api/tasks...")
    try:
        task_data = {'text': 'Test task from API test'}
        response = requests.post(f'{BASE_URL}/tasks', json=task_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        
        if response.status_code == 201:
            task_id = response.json()['id']
            print(f"   Created task with ID: {task_id}")
            
            # Test updating the task
            print("\n4. Testing PATCH /api/tasks/{id}...")
            update_data = {'done': True}
            response = requests.patch(f'{BASE_URL}/tasks/{task_id}', json=update_data)
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
            
            # Test getting all tasks again
            print("\n5. Testing GET /api/tasks (should have our task)...")
            response = requests.get(f'{BASE_URL}/tasks')
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n✅ API testing complete!")

if __name__ == '__main__':
    print("Make sure the Flask server is running on http://localhost:5000")
    print("Run: python app.py")
    input("Press Enter when the server is ready...")
    test_api()
