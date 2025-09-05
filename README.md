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

## How it satisfies requirements

1. **Dev env:** Expo CLI + Python Flask installed.
2. **Sample app:** Start from Expo’s “TextInput + FlatList” example. Runs on your device.
3. **Git:** Put app and API in GitHub, track tasks/bugs in Issues or Projects.
4. **Partner work:** They add a small change (e.g., mark-complete button). You do a small API change. Both check in/pull/build/deploy.
5. **Web service:** Flask service that stores and returns tasks. ✅