# Railway Deployment Guide

## Files Added for Railway Deployment

- `Procfile` - Tells Railway how to run the app
- `runtime.txt` - Specifies Python version
- `start.sh` - Startup script for Railway
- `railway.json` - Railway configuration
- `nixpacks.toml` - Nixpacks configuration for Python detection
- Updated `app.py` - Added Railway environment support

## Step-by-Step Deployment

### 1. Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub account
3. Verify your email

### 2. Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Connect your GitHub account if not already connected

### 3. Deploy Backend
1. Select your BusyBeeApp repository
2. Choose the `backend` folder as the root directory
3. Railway will automatically detect it's a Python app
4. Click "Deploy"

### 4. Configure Environment Variables
Railway will automatically set:
- `PORT` - Railway assigns this
- `RAILWAY_ENVIRONMENT` - Set to "production"

### 5. Get Your Deployment URL
1. After deployment, Railway will give you a URL like: `https://your-app-name.railway.app`
2. Copy this URL - you'll need it for the mobile app

### 6. Test Deployment
Visit your Railway URL in browser:
- `https://your-app-name.railway.app/` - Should show API info
- `https://your-app-name.railway.app/api/health` - Should show health status
- `https://your-app-name.railway.app/api/tasks` - Should show tasks (empty initially)

### 7. Update Mobile App
Update the API_BASE_URL in mobile/App.js to use your Railway URL:
```javascript
const API_BASE_URL = 'https://your-app-name.railway.app/api';
```

## Expected Deployment Time
- Initial deployment: 2-5 minutes
- Subsequent deployments: 1-2 minutes

## Troubleshooting

### Common Issues:
1. **Build Fails**: Check that all files are in the backend folder
2. **App Won't Start**: Check Railway logs for errors
3. **Database Issues**: SQLite file will be created automatically

### Railway Logs:
- Go to your project dashboard
- Click on "Deployments" tab
- Click on latest deployment
- View logs for any errors

## Cost
- **Free Tier**: 500 hours/month (should be enough for development)
- **Paid Tier**: $5/month for unlimited usage

## Next Steps After Deployment
1. Test API endpoints
2. Update mobile app with Railway URL
3. Test mobile app with deployed backend
4. Add login system (next phase)
