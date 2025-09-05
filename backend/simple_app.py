from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'message': 'BusyBee API is running!',
        'status': 'healthy',
        'port': os.environ.get('PORT', 'unknown')
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'BusyBee API is running'})

@app.route('/api/tasks')
def tasks():
    return jsonify([])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting simple app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
