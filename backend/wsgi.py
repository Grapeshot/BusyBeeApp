import os
from app import app, init_db

# Initialize database
init_db()

if __name__ == "__main__":
    # Get port from Render environment variable
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting WSGI server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
