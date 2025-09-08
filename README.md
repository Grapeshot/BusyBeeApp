# 🐝 BusyBee - Mobile Todo App

A full-stack mobile application built with React Native (Expo) and Flask, featuring real-time task synchronization between mobile devices and a cloud-hosted backend. Now includes **user authentication** (register + login) with password hashing.

## 📱 Live Demo

- **Mobile App**: Run via Expo Go (see setup instructions below)
- **Backend API**: [https://busybeeapp.onrender.com](https://busybeeapp.onrender.com)
- **API Health Check**: [https://busybeeapp.onrender.com/api/health](https://busybeeapp.onrender.com/api/health)

## 🏗️ Architecture

BusyBeeApp/
├── mobile/ # React Native (Expo) mobile application
│ ├── App.js # Main application component
│ ├── LoginScreen.js # User login
│ ├── RegisterScreen.js # User registration
│ ├── app.json # Expo configuration
│ └── package.json # Dependencies
├── backend/ # Flask REST API
│ ├── app.py # Main Flask application (with auth + tasks)
│ ├── wsgi.py # WSGI entry point
│ ├── requirements.txt # Python dependencies
│ └── tasks.db # SQLite database (stores users + tasks)
└── README.md # This file

markdown
Copy code

## ✨ Features

### Mobile App
- **📝 Task Management**: Add, view, and complete tasks
- **🔑 Authentication**: Register new accounts and log in securely
- **🔄 Real-time Sync**: Tasks sync instantly with backend
- **📱 Native Feel**: Built with React Native for smooth performance
- **🎨 Modern UI**: Clean, intuitive interface with BusyBee branding
- **📲 Cross-platform**: Runs on iOS and Android via Expo Go
- **🔄 Pull-to-refresh**: Swipe down to refresh task list
- **⚡ Offline Handling**: Graceful error handling and connection status

### Backend API
- **🌐 RESTful API**: Standard HTTP endpoints for auth + tasks
- **👥 User Accounts**: SQLite database stores registered users
- **🔒 Secure Passwords**: Hashed with Passlib (`bcrypt` or `pbkdf2_sha256`)
- **CORS Enabled**: Secure cross-origin requests for mobile app
- **☁️ Cloud Hosted**: Deployed on Render
- **📊 Health Monitoring**: Built-in health check endpoints

## 🚀 Quick Start

### Prerequisites
- **Node.js** (v16 or higher)
- **Python 3.9+**
- **Expo Go** app on your mobile device
- **Git** for version control

### Option 1: Use Deployed Backend (Recommended)
```bash
git clone https://github.com/your-username/BusyBeeApp.git
cd BusyBeeApp/mobile
npm install
npx expo start
The app is pre-configured to use the live backend at:

arduino
Copy code
https://busybeeapp.onrender.com/api
```
### Option 2: Local Development
```bash
Copy code
git clone https://github.com/your-username/BusyBeeApp.git
cd BusyBeeApp
```
# Start backend locally
cd backend
pip install -r requirements.txt

# If bcrypt gives errors, use:
# pip install bcrypt
# or switch to pbkdf2_sha256 in app.py
python wsgi.py

# In another terminal, start mobile app
```
cd mobile
npm install
npx expo start
Note: For local dev, update mobile/App.js API base URL to:

bash
Copy code
http://localhost:5000/api
Run on Device
Install Expo Go on your phone

Run npx expo start --tunnel

Scan the QR code

App loads on your device
```
🔧 Development

Backend Endpoints
Health
GET https://busybeeapp.onrender.com/api/health → Health check

Authentication
POST https://busybeeapp.onrender.com/api/register → Register new user
Body:

json
Copy code
{"username": "alice", "password": "mypassword"}
POST https://busybeeapp.onrender.com/api/login → Login with existing user
Body:

json
Copy code
{"username": "alice", "password": "mypassword"}
Tasks
GET https://busybeeapp.onrender.com/api/tasks → Retrieve all tasks

POST https://busybeeapp.onrender.com/api/tasks → Create new task

json
Copy code
{"text": "Finish BusyBee README"}
PATCH https://busybeeapp.onrender.com/api/tasks/:id → Update task status

json
Copy code
{"done": true}
🌐 Deployment
Backend (Render)
Connect repo to Render

Create Web Service

Configure:

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: python wsgi.py

Deploy → get service URL

Mobile (Expo)
Development: Expo Go QR scanning

Production: expo build → standalone iOS/Android apps

📚 Example Flows
Register a User
bash
Copy code
curl -X POST https://busybeeapp.onrender.com/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"1234"}'
Login
bash
Copy code
curl -X POST https://busybeeapp.onrender.com/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"1234"}'
Get Tasks
bash
Copy code
curl https://busybeeapp.onrender.com/api/tasks
