#!/usr/bin/env python3
"""
Clear the remote database on Render
This script will delete all tasks from the deployed backend
"""

import requests
import json

# Your deployed backend URL
API_BASE_URL = 'https://busybeeapp.onrender.com/api'

def get_all_tasks():
    """Get all tasks from the remote database"""
    try:
        response = requests.get(f'{API_BASE_URL}/tasks')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get tasks: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error getting tasks: {e}")
        return []

def clear_remote_database():
    """Clear all tasks from the remote database"""
    print("🗑️  Clearing remote database on Render...")
    
    # Get all tasks first
    tasks = get_all_tasks()
    print(f"📋 Found {len(tasks)} tasks to delete")
    
    if not tasks:
        print("✅ Database is already empty!")
        return
    
    # Use the DELETE endpoint to clear all tasks
    try:
        response = requests.delete(f'{API_BASE_URL}/tasks')
        if response.status_code == 200:
            result = response.json()
            print(f"✅ {result['message']}")
            print(f"🗑️  Deleted {result['deleted_count']} tasks")
        else:
            print(f"❌ Failed to clear database: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Error clearing database: {e}")
    
    # Show the tasks that were deleted
    print("\n📋 Tasks that were deleted:")
    for task in tasks:
        status = "✅" if task['done'] else "⏳"
        print(f"   {status} {task['text']} (ID: {task['id']})")

if __name__ == '__main__':
    clear_remote_database()
