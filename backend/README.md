# BusyBee Backend API

Flask-based REST API for the BusyBee To Do App.

## Features

- ✅ SQLite database with tasks table
- ✅ RESTful API endpoints
- ✅ CORS enabled for mobile app
- ✅ Error handling and validation
- ✅ Health check endpoint

## API Endpoints

### Health Check
- `GET /api/health` - Check if API is running

### Tasks
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `PATCH /api/tasks/{id}` - Update a task (mark as done/undone)

## Database Schema

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    done BOOLEAN DEFAULT FALSE
);
```

## Installation & Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python app.py
   ```

3. The API will be available at `http://localhost:5000`

## Testing

Run the test script to verify all endpoints:
```bash
python test_api.py
```

## Example Usage

### Create a task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"text": "Buy groceries"}'
```

### Get all tasks
```bash
curl http://localhost:5000/api/tasks
```

### Mark task as done
```bash
curl -X PATCH http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```
