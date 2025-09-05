# Render Deployment Guide

## Files Configured for Render Deployment

- `requirements.txt` - Python dependencies
- `wsgi.py` - WSGI entry point for Render
- Updated `app.py` - Added Render environment support

## Step-by-Step Deployment

### 1. Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub account
3. Verify your email

### 2. Create New Web Service
1. Click "New +" → "Web Service"
2. Select "Build and deploy from a Git repository"
3. Connect your GitHub account if not already connected

### 3. Configure Deployment
1. **Repository**: Select your BusyBeeApp repository
2. **Branch**: Select `main`
3. **Root Directory**: Set to `backend`
4. **Runtime**: Select `Python 3`
5. **Build Command**: Leave empty (Render will auto-detect)
6. **Start Command**: `python wsgi.py`

### 4. Configure Environment Variables
Render will automatically set:
- `PORT` - Render assigns this
- `RENDER` - Set to "true" in production

### 5. Deploy
1. Click "Create Web Service"
2. Wait 3-5 minutes for deployment
3. Render will give you a URL like: `https://your-app-name.onrender.com`

### 6. Test Deployment
Visit your Render URL in browser:
- `https://your-app-name.onrender.com/` - Should show API info
- `https://your-app-name.onrender.com/api/health` - Should show health status
- `https://your-app-name.onrender.com/api/tasks` - Should show tasks (empty initially)

### 7. Update Mobile App
Update the API_BASE_URL in mobile/App.js to use your Render URL:
```javascript
const API_BASE_URL = 'https://your-app-name.onrender.com/api';
```

## Expected Deployment Time
- Initial deployment: 3-5 minutes
- Subsequent deployments: 2-3 minutes

## Troubleshooting

### Common Issues:
1. **Build Fails**: Check that all files are in the backend folder
2. **App Won't Start**: Check Render logs for errors
3. **Database Issues**: SQLite file will be created automatically

### Render Logs:
- Go to your service dashboard
- Click on "Logs" tab
- View real-time logs for any errors

## Cost
- **Free Tier**: 750 hours/month (should be enough for development)
- **Paid Tier**: $7/month for always-on service

## Next Steps After Deployment
1. Test API endpoints
2. Update mobile app with Render URL
3. Test mobile app with deployed backend
4. Add login system (next phase)
