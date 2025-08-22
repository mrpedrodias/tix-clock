# LaMetric Developer Portal Setup Guide

## ✅ CORRECT: Choose "Indicator app"

**Select**: `Indicator app` - This is the right choice for your TIX clock!

**DO NOT** choose:
- ❌ "Button app" (for taking actions)
- ❌ "Notification app" (for smart home notifications)

## Step 1: Create Your Indicator App

1. **Go to** [https://developer.lametric.com/](https://developer.lametric.com/)
2. **Sign in** with your LaMetric account
3. **Click "Create App"** or "New App"
4. **Select "Indicator app"** from the options
5. **Click "create"** next to Indicator app

## Step 2: App Configuration

Fill in the basic details:
- **App Name**: `TIX Clock`
- **App Description**: `Displays current time using TIX format with custom 8x8 pixel icons`
- **Category**: `Clock` (if available)

## Step 3: API Configuration

### API Settings
- **API URL**: `https://your-app-name.railway.app/tix`
- **Update frequency**: `Every minute`
- **Request method**: `GET`
- **Authentication**: `None`

### Expected Response Format
Your Flask app returns exactly what LaMetric expects:
```json
{
  "frames": [
    {
      "text": "TIX",
      "icon": "i421i422i424i420"
    }
  ]
}
```

## Step 4: Custom Icons Section

### Where to Find Icon Upload
1. **Look for "Icons" section** in your app configuration
2. **Click "Add Icon"** or "Upload Icon"
3. **Upload your generated icons** from the `icons/` directory

### Icon Requirements
- **Size**: 8x8 pixels
- **Format**: PNG
- **Colors**: 2 colors maximum (recommended)
- **Transparency**: Supported

### Upload Process
Upload these 10 files:
- `icon_0.png` → Will get ID like `i420`
- `icon_1.png` → Will get ID like `i421`
- `icon_2.png` → Will get ID like `i422`
- And so on...

### Icon Naming
- **Name**: `TIX 0`, `TIX 1`, `TIX 2`, etc.
- **Description**: `TIX icon with X lit squares`

## Step 5: Update Your Code

Once you have the real icon IDs from LaMetric:

1. **Note down all 10 icon IDs** (i420, i421, i422, etc.)
2. **Update the `icon_map`** in your `tix.py` file
3. **Commit and push** the changes to GitHub
4. **Railway will redeploy** automatically

## Step 6: Test Your App

### In Developer Portal
1. **Click "Test"** button
2. **Check the preview** shows correct icons
3. **Verify API response** is working

### On Your Device
1. **Go to your LaMetric device**
2. **Add the app** from your private apps
3. **Configure** with your Railway URL

## Step 7: Publish

### Private App (Recommended for now)
- **Keep it private** - only you can use it
- **No review process** - instant availability

### Public App (Later)
- **Submit for review** - LaMetric team reviews
- **May take days** for approval
- **Appears in public store**

## Troubleshooting

### Common Issues
- **Icons not showing**: Check icon IDs are correct in `icon_map`
- **API not responding**: Verify Railway URL is working
- **Wrong time**: Check your server's timezone

### Testing Your API
Visit these URLs to test:
- `https://your-app-name.railway.app/` - Home page
- `https://your-app-name.railway.app/tix` - LaMetric endpoint
- `https://your-app-name.railway.app/time` - Debug info

## Example Icon IDs

After uploading, your icon IDs might look like:
```python
icon_map = {
    '0': 'i1234',  # Your actual icon ID for 0
    '1': 'i1235',  # Your actual icon ID for 1
    '2': 'i1236',  # Your actual icon ID for 2
    # ... continue for all digits
}
```

## Next Steps

1. **Create an Indicator app** (you're on the right track!)
2. **Upload your 10 icons** (0-9)
3. **Get the real icon IDs**
4. **Update your code** with the real IDs
5. **Test on your device**
6. **Enjoy your TIX clock!**
