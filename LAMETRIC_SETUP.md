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

### Expected Response Format (Base64, Single Frame)
Your Flask app now returns a single frame with a Base64-encoded PNG image (32x8), which prevents scrolling and shows a static, stitched display of all four digits:
```json
{
  "frames": [
    {
      "icon": "data:image/png;base64,iVBORw0KGgoAAA..."
    }
  ]
}
```

- The server fetches the 8x8 digit icons from LaMetric, stitches them into one 32x8 image, and returns it as a Base64 data URI.
- LaMetric renders this as a static icon, so the time does not scroll.

## Step 4: Custom Icons Section (Server-side Use)

Your server needs the 10 digit icons (0–9) to compose the 32x8 image. Upload them once to the Developer Portal to obtain their IDs.

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
- `icon_0.png` → Will get an ID like `939`
- `icon_1.png` → Will get an ID like `4423`
- … continue for `2` through `9`

### Why upload icons if we return Base64?
- The Flask app downloads these icons by ID from LaMetric servers and stitches them server‑side.
- Your device receives only the final Base64 image, not the individual icon IDs.

## Step 5: Update Your Code

Once you have the real icon IDs from LaMetric:

1. **Note down all 10 icon IDs**
2. **Update the `icon_map`** in your `tix.py` file (IDs are numbers as strings)
3. **Commit and push** the changes to GitHub
4. **Railway will redeploy** automatically

## Step 6: Test Your App

### In Developer Portal
1. **Click "Test"** button
2. **Check the preview** shows your static image (no scrolling)

### From the API
- `https://your-app-name.railway.app/tix` – returns JSON with the Base64 data URI
- `https://your-app-name.railway.app/test` – HTML preview showing the stitched image (scaled up for visibility)

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
- **Image not loading**: Verify the icon IDs exist and are reachable at LaMetric’s CDN
- **API not responding**: Check Railway logs and dependency installation
- **Wrong time**: Check your server's timezone (code uses server time)

### Testing Your API
Visit these URLs to test:
- `https://your-app-name.railway.app/tix` - JSON response with Base64 data URI
- `https://your-app-name.railway.app/test` - Visual preview of the stitched image

## Example Icon IDs

After uploading, your icon IDs might look like:
```python
icon_map = {
    '0': '939',
    '1': '4423',
    '2': '9168',
    '3': '9169',
    '4': '70007',
    '5': '70008',
    '6': '70009',
    '7': '70010',
    '8': '70011',
    '9': '70012'
}
```

## Next Steps

1. **Create an Indicator app** (you're on the right track!)
2. **Upload your 10 icons** (0-9)
3. **Update your code** with the real IDs
4. **Verify `/test`** renders correctly
5. **Point the app to `/tix`**
6. **Enjoy your TIX clock!**
