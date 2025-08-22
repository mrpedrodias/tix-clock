# Deployment Guide for LaMetric TIX Clock

## Quick Deploy Options (Recommended)

### 1. Railway (Easiest - Free Tier Available)

1. **Sign up** at [railway.app](https://railway.app)
2. **Create new project** → "Deploy from GitHub repo"
3. **Connect your GitHub repository**
4. **Railway will automatically detect Python and deploy**
5. **Get your live URL** (e.g., `https://your-app-name.railway.app`)

### 2. Render (Free Tier Available)

1. **Sign up** at [render.com](https://render.com)
2. **Create new Web Service**
3. **Connect your GitHub repository**
4. **Configure:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python tix.py`
   - **Environment**: Python 3
5. **Deploy and get your URL**

### 3. PythonAnywhere (Free Tier Available)

1. **Sign up** at [pythonanywhere.com](https://pythonanywhere.com)
2. **Go to Files tab** and upload your files
3. **Go to Web tab** → "Add a new web app"
4. **Choose Flask** and Python 3.9
5. **Set source code** to your uploaded directory
6. **Set WSGI file** to point to your app
7. **Reload** and get your URL

## Production Considerations

### Environment Variables
Your app now uses environment variables for production:
- `PORT`: Port number (set automatically by most platforms)
- `HOST`: Host address (set automatically by most platforms)

### Security
For production, consider:
1. **HTTPS**: Most platforms provide this automatically
2. **Rate limiting**: Add if needed
3. **CORS**: Add if needed for web access

### Monitoring
Add basic health check endpoint:
```python
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'time': datetime.datetime.now().isoformat()})
```

## LaMetric Configuration

Once deployed, configure your LaMetric app with:
- **API URL**: `https://your-app-name.railway.app/tix` (or your chosen platform)
- **Update frequency**: Every minute or as needed

## Testing Your Deployment

1. **Test the endpoint**: Visit `https://your-app-name.railway.app/tix`
2. **Check JSON response**: Should return valid LaMetric format
3. **Test from LaMetric**: Configure your device to use the new URL

## Troubleshooting

### Common Issues:
- **App not starting**: Check logs for Python version compatibility
- **404 errors**: Ensure route is `/tix` not `/`
- **CORS errors**: Add CORS headers if accessing from web browser
- **Icon not showing**: Verify icon IDs are correct

### Adding CORS Support (if needed):
```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Add this line after creating Flask app
```

## Cost Comparison

| Platform | Free Tier | Paid Plans | Ease of Use |
|----------|-----------|------------|-------------|
| Railway | ✅ 500 hours/month | $5/month | ⭐⭐⭐⭐⭐ |
| Render | ✅ 750 hours/month | $7/month | ⭐⭐⭐⭐ |
| PythonAnywhere | ✅ 512MB RAM | $5/month | ⭐⭐⭐ |
| Heroku | ❌ No free tier | $7/month | ⭐⭐⭐⭐ |
| DigitalOcean | ❌ No free tier | $5/month | ⭐⭐⭐ |

## Recommended: Railway

For your TIX clock, I recommend **Railway** because:
- ✅ Generous free tier
- ✅ Automatic deployments
- ✅ Easy setup
- ✅ Good performance
- ✅ HTTPS included
