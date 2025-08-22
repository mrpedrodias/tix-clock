from PIL import Image, ImageDraw
import os

def create_tix_icon(number, size=8, bg_color=(0, 0, 0), fg_color=(255, 255, 255)):
    """
    Create an 8x8 icon where the number of lit squares equals the digit.
    
    Args:
        number: The digit (0-9)
        size: Icon size (default 8x8)
        bg_color: Background color (RGB tuple)
        fg_color: Foreground color for lit squares (RGB tuple)
    """
    # Create image with background color
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calculate how many squares to light up
    squares_to_light = number
    
    # Light up squares in a logical pattern
    squares_lit = 0
    for row in range(size):
        for col in range(size):
            if squares_lit < squares_to_light:
                # Calculate position for this square
                x1 = col
                y1 = row
                x2 = col + 1
                y2 = row + 1
                
                # Draw the lit square
                draw.rectangle([x1, y1, x2, y2], fill=fg_color)
                squares_lit += 1
            else:
                break
        if squares_lit >= squares_to_light:
            break
    
    return img

def generate_all_icons(output_dir="icons", size=8):
    """Generate all 10 icons (0-9) and save them."""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Colors: Black background, White squares
    bg_color = (0, 0, 0)      # Black
    fg_color = (255, 255, 255) # White
    
    print(f"Generating {size}x{size} TIX icons...")
    
    for digit in range(10):
        # Create the icon
        icon = create_tix_icon(digit, size, bg_color, fg_color)
        
        # Save the icon
        filename = f"{output_dir}/icon_{digit}.png"
        icon.save(filename)
        print(f"Created: {filename} ({digit} lit squares)")
    
    print(f"\nAll icons saved to '{output_dir}/' directory")
    print("You can now upload these to the LaMetric Developer portal")

def create_alternative_patterns():
    """Create alternative icon patterns for variety."""
    
    patterns = {
        "sequential": "Left to right, top to bottom",
        "spiral": "Spiral pattern from center",
        "checkerboard": "Checkerboard pattern",
        "corners": "Start from corners"
    }
    
    print("\nAlternative patterns you could implement:")
    for name, description in patterns.items():
        print(f"- {name}: {description}")

if __name__ == "__main__":
    # Generate the standard icons
    generate_all_icons()
    
    # Show alternative patterns
    create_alternative_patterns()
    
    print("\nTo use these icons:")
    print("1. Upload each icon to LaMetric Developer portal")
    print("2. Note the icon IDs (like i420, i421, etc.)")
    print("3. Update the icon_map in tix.py with the real IDs")
