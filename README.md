# 🐝 BusyBee - Mobile Todo App

A full-stack mobile application built with React Native (Expo) and Flask, featuring real-time task synchronization between mobile devices and a cloud-hosted backend.

## 📱 Live Demo

- **Mobile App**: Run via Expo Go (see setup instructions below)
- **Backend API**: [https://busybeeapp.onrender.com](https://busybeeapp.onrender.com)
- **API Health Check**: [https://busybeeapp.onrender.com/api/health](https://busybeeapp.onrender.com/api/health)

## 🏗️ Architecture

```
BusyBeeApp/
├── mobile/          # React Native (Expo) mobile application
│   ├── App.js       # Main application component
│   ├── app.json     # Expo configuration
│   └── package.json # Dependencies
├── backend/         # Flask REST API
│   ├── app.py       # Main Flask application
│   ├── wsgi.py      # WSGI entry point
│   ├── requirements.txt # Python dependencies
│   └── tasks.db     # SQLite database
└── README.md        # This file
```

## ✨ Features

### Mobile App
- **📝 Task Management**: Add, view, and complete tasks
- **🔄 Real-time Sync**: Instant synchronization with cloud backend
- **📱 Native Feel**: Built with React Native for smooth performance
- **🎨 Modern UI**: Clean, intuitive interface with BusyBee branding
- **📲 Cross-platform**: Runs on iOS and Android via Expo Go
- **🔄 Pull-to-refresh**: Swipe down to refresh task list
- **⚡ Offline Handling**: Graceful error handling and connection status

### Backend API
- **🌐 RESTful API**: Standard HTTP endpoints for task operations
- **💾 Data Persistence**: SQLite database for reliable data storage
- **🔒 CORS Enabled**: Secure cross-origin requests for mobile app
- **☁️ Cloud Hosted**: Deployed on Render for 24/7 availability
- **📊 Health Monitoring**: Built-in health check endpoints

## 🚀 Quick Start

### Prerequisites
- **Node.js** (v16 or higher)
- **Expo Go** app on your mobile device
- **Git** for version control

### Option 1: Use Deployed Backend (Recommended)
The easiest way to get started is using the live backend:

```bash
git clone https://github.com/your-username/BusyBeeApp.git
cd BusyBeeApp/mobile
npm install
npx expo start
```

The mobile app is already configured to connect to the deployed backend at `https://busybeeapp.onrender.com`.

### Option 2: Local Development
If you want to modify the backend or develop locally:

```bash
git clone https://github.com/your-username/BusyBeeApp.git
cd BusyBeeApp

# Start backend locally
cd backend
pip install -r requirements.txt
python wsgi.py

# In another terminal, start mobile app
cd mobile
npm install
npx expo start
```

**Note**: For local development, you'll need to update `mobile/App.js` to use `http://localhost:5000/api` instead of the deployed URL.

### Run on Device
1. Install **Expo Go** on your phone
2. Scan the QR code from the terminal
3. The app will load on your device

## 🔧 Development

### Backend Development
```bash
cd backend
python app.py  # Development server with hot reload
```

**API Endpoints:**
- `GET /api/health` - Health check
- `GET /api/tasks` - Retrieve all tasks
- `POST /api/tasks` - Create new task
- `PATCH /api/tasks/:id` - Update task status

### Mobile Development
```bash
cd mobile
npx expo start --tunnel  # For testing on physical device
```

**Key Components:**
- `App.js` - Main application with task management logic
- `app.json` - Expo configuration and app metadata

### Testing
```bash
# Test backend API
cd backend
python test_api.py

# Test mobile connection
cd mobile
node test-connection.js
```

## 🌐 Deployment

### Backend Deployment (Render)
1. Create account at [render.com](https://render.com)
2. Connect GitHub repository
3. Create new Web Service
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python wsgi.py`
5. Deploy and get your URL

### Mobile App Distribution
- **Development**: Use Expo Go for testing
- **Production**: Build standalone apps with `expo build`

## 🤝 Contributing

### For New Developers

1. **Fork the repository**
2. **Clone your fork**: `git clone https://github.com/your-username/BusyBeeApp.git`
3. **Create a feature branch**: `git checkout -b feature/your-feature-name`
4. **Follow the Quick Start** guide above
5. **Make your changes** and test thoroughly
6. **Commit your changes**: `git commit -m "Add your feature"`
7. **Push to your fork**: `git push origin feature/your-feature-name`
8. **Create a Pull Request**

### Development Workflow
- **Backend changes**: Test with `python test_api.py`
- **Mobile changes**: Test on physical device via Expo Go
- **Integration testing**: Verify mobile app connects to backend
- **Documentation**: Update README for significant changes

## 📚 API Documentation

### Task Object
```json
{
  "id": 1,
  "text": "Complete project documentation",
  "created_at": "2025-09-05T10:30:00Z",
  "done": false
}
```

### Endpoints

#### GET /api/tasks
Retrieve all tasks
```bash
curl https://busybeeapp.onrender.com/api/tasks
```

#### POST /api/tasks
Create a new task
```bash
curl -X POST https://busybeeapp.onrender.com/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"text": "New task"}'
```

#### PATCH /api/tasks/:id
Update task completion status
```bash
curl -X PATCH https://busybeeapp.onrender.com/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```
