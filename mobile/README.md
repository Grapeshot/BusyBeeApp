# BusyBee Mobile App

React Native mobile app built with Expo for the BusyBee To Do App.

## Features

- ✅ Beautiful, modern UI with BusyBee branding
- ✅ Add new tasks with text input
- ✅ Mark tasks as complete/incomplete
- ✅ Real-time sync with Flask backend
- ✅ Pull-to-refresh functionality
- ✅ Loading states and error handling
- ✅ Empty state with helpful messaging
- ✅ Responsive design

## Screenshots

The app includes:
- **Header**: BusyBee branding with bee emoji
- **Add Task Section**: Text input with add button
- **Tasks List**: Scrollable list with checkboxes
- **Empty State**: Helpful message when no tasks exist

## Setup & Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npx expo start
   ```

3. Run on device:
   - Install Expo Go app on your phone
   - Scan the QR code from the terminal
   - Or press 'w' to open in web browser

## API Configuration

The app connects to the Flask backend at `http://localhost:5000/api`.

**Important**: Make sure the Flask backend is running before testing the mobile app.

## Testing on Device

1. Make sure your phone and computer are on the same WiFi network
2. Start the Flask backend: `python app.py` (in backend folder)
3. Start the Expo server: `npx expo start` (in mobile folder)
4. Scan the QR code with Expo Go app
5. Test adding tasks and marking them complete

## Features Implemented

- **Text Input**: Environmental input for adding tasks ✅
- **Add Button**: Creates new tasks via API ✅
- **Task List**: Displays all tasks from backend ✅
- **Checkboxes**: Mark tasks as complete/incomplete ✅
- **Real-time Sync**: Updates immediately after changes ✅
- **Error Handling**: Shows alerts for network errors ✅
- **Loading States**: Visual feedback during operations ✅
