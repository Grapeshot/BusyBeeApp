# **Busy Bee To Do App (Expo + Flask)**

A one-screen mobile app where you add a short task and it syncs to a backend.

## Project Structure

```
BusyBeeApp/
├── mobile/          # Expo React Native app
├── backend/         # Flask API
├── README.md
└── .gitignore
```

---

## App (Expo / React Native)

* Screen has:

  * Text input: “Enter task…”
  * Button: “Add Task”
  * List showing all tasks (fetched from backend)
* Runs on your phone through **Expo Go**.

**Environmental input:** keyboard text entry (counts as “user input” ✅).
Optional: add a checkbox to mark a task as complete.

---

## Backend (Flask)

* `POST /api/tasks` → save `{ text, created_at, done }` into SQLite
* `GET /api/tasks` → return all tasks
* Optional: `PATCH /api/tasks/:id` → mark task done
* Deploy on **Render** or **Railway** (free tier).

---

## Development Status

### ✅ Completed Features

1. **Development Environment:** Expo CLI + Python Flask installed and configured
2. **Flask Backend:** 
   - SQLite database with tasks table
   - RESTful API endpoints (GET, POST, PATCH)
   - CORS enabled for mobile app
   - Health check endpoint
3. **Mobile App:**
   - Beautiful BusyBee-branded UI
   - Text input for adding tasks
   - Task list with checkboxes
   - Real-time sync with backend
   - Pull-to-refresh functionality
   - Error handling and loading states
4. **Project Structure:** Organized with separate mobile/ and backend/ folders
5. **Documentation:** README files for both frontend and backend

### 🚀 Ready for Testing

The app is ready to run on your device via Expo Go:
1. Start Flask backend: `cd backend && python app.py`
2. Start mobile app: `cd mobile && npx expo start`
3. Scan QR code with Expo Go app

### 📋 Remaining Tasks

- Deploy backend to Render/Railway
- Final integration testing
- Git repository setup for collaboration