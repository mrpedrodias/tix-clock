from flask import Flask, jsonify
import datetime
import requests
from PIL import Image
import io
import base64

# Create a new Flask web server
app = Flask(__name__)

# This is your "map" of digits to LaMetric icon IDs.
# The script will use these IDs to download the correct icon images.
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

# --- Helper Function to Create the Combined Image ---
def create_tix_image(time_string):
    """
    Fetches four 8x8 icon images from LaMetric, combines them into a single 32x8 image,
    and returns it as a Base64 encoded string.
    """
    images = []
    for digit in time_string:
        icon_id = icon_map[digit]
        # Construct the URL to download the icon
        icon_url = f"https://developer.lametric.com/content/apps/icon_thumbs/{icon_id}.png"
        try:
            # Download the image data
            response = requests.get(icon_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            img_data = io.BytesIO(response.content)
            img = Image.open(img_data).convert("RGBA")
            images.append(img)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching icon {icon_id}: {e}")
            # Return a default blank image on error
            return Image.new('RGBA', (8, 8), (0, 0, 0, 0))

    if not images:
        return None

    # Create a new blank image with a width for all four icons (32x8)
    combined_image = Image.new('RGBA', (32, 8), (0, 0, 0, 0))

    # Paste each 8x8 icon into the combined image
    for i, img in enumerate(images):
        combined_image.paste(img, (i * 8, 0))

    # Convert the final image to a Base64 string
    buffered = io.BytesIO()
    combined_image.save(buffered, format="PNG")
    base64_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    # Format as a data URI for the LaMetric API
    return f"data:image/png;base64,{base64_string}"


# --- API Routes ---

# The main endpoint for your LaMetric clock
@app.route('/tix')
def get_tix_time_base64():
    now = datetime.datetime.now()
    time_string = now.strftime("%H%M")

    # Generate the combined Base64 image
    base64_icon = create_tix_image(time_string)

    if not base64_icon:
        return jsonify({"error": "Could not generate image"}), 500

    # Create a single frame with the Base64 icon
    lametric_response = {
        'frames': [
            {
                'icon': base64_icon
            }
        ]
    }
    
    return jsonify(lametric_response)

# A new testing route to see the Base64 output
@app.route('/test')
def test_base64_output():
    now = datetime.datetime.now()
    time_string = now.strftime("%H%M")
    base64_icon = create_tix_image(time_string)
    
    # Return an HTML page that displays the generated image
    return f'''
        <h1>TIX Clock Image Test</h1>
        <p>Current Server Time (UTC): {time_string}</p>
        <p>This is the 32x8 image that will be sent to your LaMetric:</p>
        <img src="{base64_icon}" style="width: 320px; height: 80px; image-rendering: pixelated; border: 1px solid black;">
        <p>Base64 String (truncated):</p>
        <pre>{base64_icon[:100]}...</pre>
    '''

# --- Server Start ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    print(f"Running on http://{host}:{port}")
    app.run(debug=False, host=host, port=port)