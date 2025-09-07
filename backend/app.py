from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import sqlite3
import datetime
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
DATABASE = 'tasks.db'
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')  # store in env var

def init_db():
    """Initialize the database with tasks table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            done BOOLEAN DEFAULT FALSE
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        tasks = cursor.fetchall()
        
        conn.close()
        
        # Convert Row objects to dictionaries
        tasks_list = []
        for task in tasks:
            tasks_list.append({
                'id': task['id'],
                'text': task['text'],
                'created_at': task['created_at'],
                'done': bool(task['done'])
            })
        
        return jsonify(tasks_list), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'Text is required'}), 400
        
        text = data['text'].strip()
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO tasks (text) VALUES (?)',
            (text,)
        )
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({
            'id': task_id,
            'text': text,
            'created_at': datetime.datetime.now().isoformat(),
            'done': False
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update a task (mark as done/undone)"""
    try:
        data = request.get_json()
        
        if not data or 'done' not in data:
            return jsonify({'error': 'Done status is required'}), 400
        
        done = data['done']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if task exists
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        
        if not task:
            conn.close()
            return jsonify({'error': 'Task not found'}), 404
        
        # Update the task
        cursor.execute(
            'UPDATE tasks SET done = ? WHERE id = ?',
            (done, task_id)
        )
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'id': task_id,
            'text': task['text'],
            'created_at': task['created_at'],
            'done': bool(done)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Atlanta') # default to Atlanta
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            return jsonify({'error': data.get('message', 'Weather fetch failed')}), 400
        
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return jsonify(weather_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'BusyBee API is running'}), 200

@app.route('/api/tasks', methods=['DELETE'])
def clear_all_tasks():
    """Clear all tasks from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Count tasks before deletion
        cursor.execute('SELECT COUNT(*) FROM tasks')
        count = cursor.fetchone()[0]
        
        # Delete all tasks
        cursor.execute('DELETE FROM tasks')
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'message': f'Cleared {count} tasks from database',
            'deleted_count': count
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    """Root endpoint for Railway health checks"""
    return jsonify({
        'message': 'BusyBee API is running!',
        'status': 'healthy',
        'endpoints': {
            'health': '/api/health',
            'tasks': '/api/tasks',
            'weather': '/api/weather'
        }
    }), 200

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
    print("Starting BusyBee API server...")
    
    # Get port from Render environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run in production mode on Render, debug mode locally
    debug_mode = os.environ.get('RENDER') is None
    
    print(f"Starting server on port {port}")
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
