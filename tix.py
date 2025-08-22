from flask import Flask, jsonify
import datetime

# Create a new Flask web server
app = Flask(__name__)

# This is your "map" of digits to LaMetric icon IDs.
# You MUST replace 'iXXXX' with the actual icon IDs from your LaMetric Developer account.
# To get these IDs:
# 1. Go to https://developer.lametric.com/
# 2. Create your app and upload the 10 icons (0-9)
# 3. Note the icon IDs that LaMetric assigns
# 4. Replace the placeholder IDs below with the real ones
icon_map = {
    '0': '1489',  # Replace with your actual icon ID for 0
    '1': '4423',  # Replace with your actual icon ID for 1
    '2': '9168',  # Replace with your actual icon ID for 2
    '3': '9169',  # Replace with your actual icon ID for 3
    '4': '70007',  # Replace with your actual icon ID for 4
    '5': '70008',  # Replace with your actual icon ID for 5
    '6': '70009',  # Replace with your actual icon ID for 6
    '7': '70010',  # Replace with your actual icon ID for 7
    '8': '70011',  # Replace with your actual icon ID for 8
    '9': '70012'   # Replace with your actual icon ID for 9
}

# Root route for testing and information
@app.route('/')
def home():
    return '''
    <h1>LaMetric TIX Clock API</h1>
    <p>This is a Flask API for displaying time on a LaMetric TIX clock.</p>
    <h2>Available endpoints:</h2>
    <ul>
        <li><a href="/tix">/tix</a> - Get current time in TIX format for LaMetric</li>
        <li><a href="/time">/time</a> - Get current time in readable format</li>
    </ul>
    <h2>Current time:</h2>
    <p>{}</p>
    '''.format(datetime.datetime.now().strftime("%H:%M:%S"))

# Route to show current time in readable format
@app.route('/time')
def get_time():
    now = datetime.datetime.now()
    return jsonify({
        'current_time': now.strftime("%H:%M:%S"),
        'time_digits': list(now.strftime("%H%M")),
        'icon_ids': [icon_map[digit] for digit in now.strftime("%H%M")]
    })

# Define the API route that LaMetric will call
@app.route('/tix')
def get_tix_time():
    # 1. Get the current time
    now = datetime.datetime.now()
    
    # Format the time into a four-digit string like "1240"
    time_string = now.strftime("%H%M")

    # 2. Break down the time string into four icon IDs
    # For example, "1240" becomes ['i421', 'i422', 'i424', 'i420']
    icons = [icon_map[digit] for digit in time_string]

    # 3. Construct the JSON response
    lametric_response = {
        'frames': [
            {
                'text': 'TIX',
                # The 'icon' value is a single string of the four icon IDs joined together
                'icon': "".join(icons)
            }
        ]
    }
    
    # Return the data as a JSON object
    return jsonify(lametric_response)

# This allows you to run the server for testing
if __name__ == '__main__':
    print("Starting LaMetric TIX Clock API...")
    
    # Use environment variables for production deployment
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # If PORT is set (production), bind to 0.0.0.0, otherwise use 127.0.0.1 (development)
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    
    print(f"Running on http://{host}:{port}")
    print(f"LaMetric endpoint: http://{host}:{port}/tix")
    
    app.run(debug=False, host=host, port=port)