# LaMetric TIX Clock

A Flask-based API that displays the current time on a LaMetric TIX clock using custom 8x8 pixel icons.

## How It Works

1. **Get Current Time**: The application retrieves the current time
2. **Break Down Digits**: Time is broken into individual digits (e.g., 11:45 becomes 1, 1, 4, 5)
3. **Map to Icons**: Each digit is mapped to a corresponding 8x8 pixel icon
4. **JSON Response**: Constructs a JSON response for LaMetric to display

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Custom Icons

You need to create custom 8x8 pixel icons in the LaMetric Developer portal:

1. Go to [LaMetric Developer Portal](https://developer.lametric.com/)
2. Create a new app
3. Design 10 icons (0-9) where each icon represents the number of lit squares
4. Note down the icon IDs (they'll look like `i420`, `i421`, etc.)

### 3. Update Icon Mapping

Edit `tix.py` and replace the placeholder icon IDs in the `icon_map` dictionary with your actual icon IDs:

```python
icon_map = {
    '0': 'i420',  # Replace with your actual icon ID for 0
    '1': 'i421',  # Replace with your actual icon ID for 1
    # ... continue for all digits
}
```

### 4. Run the Application

```bash
python tix.py
```

The server will start on `http://127.0.0.1:5000/`

## API Endpoints

- **`/`** - Home page with API information and current time
- **`/tix`** - LaMetric-compatible JSON response (main endpoint)
- **`/time`** - Current time in readable format with debugging info

## Testing

1. Visit `http://127.0.0.1:5000/` to see the home page
2. Visit `http://127.0.0.1:5000/tix` to see the JSON response for LaMetric
3. Visit `http://127.0.0.1:5000/time` to see current time details

## LaMetric Configuration

In your LaMetric app configuration, set the API endpoint to:
```
http://your-server-ip:5000/tix
```

## Example JSON Response

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

## Icon Design Tips

For the TIX concept, design your icons so that:
- Icon for "0" has 0 lit squares
- Icon for "1" has 1 lit square
- Icon for "2" has 2 lit squares
- And so on...

This creates a visual representation where the number of lit squares matches the digit being displayed.

## Troubleshooting

- **404 Error**: Make sure you're accessing the correct endpoint (`/tix` for LaMetric, `/` for home page)
- **Icon Not Displaying**: Verify your icon IDs are correct in the `icon_map`
- **Server Won't Start**: Check that Flask is installed and port 5000 is available
