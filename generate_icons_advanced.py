from PIL import Image, ImageDraw
import os

def create_tix_icon(number, size=8, bg_color=(0, 0, 0), fg_color=(255, 255, 255)):
    """
    Create an 8x8 icon where the number of lit squares equals the digit.
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

def create_spiral_icon(number, size=8, bg_color=(0, 0, 0), fg_color=(255, 255, 255)):
    """Create icon with spiral pattern from center."""
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Spiral pattern coordinates (from center outward)
    spiral_order = [
        (3, 3), (4, 3), (4, 4), (3, 4), (2, 4), (2, 3), (2, 2), (3, 2),
        (4, 2), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5),
        (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1),
        (5, 1), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (5, 6),
        (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (0, 3),
        (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
        (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
        (7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)
    ]
    
    for i in range(min(number, len(spiral_order))):
        x, y = spiral_order[i]
        draw.rectangle([x, y, x+1, y+1], fill=fg_color)
    
    return img

def create_checkerboard_icon(number, size=8, bg_color=(0, 0, 0), fg_color=(255, 255, 255)):
    """Create icon with checkerboard pattern."""
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Create checkerboard positions
    positions = []
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:  # Checkerboard pattern
                positions.append((col, row))
    
    # Light up the first 'number' positions
    for i in range(min(number, len(positions))):
        x, y = positions[i]
        draw.rectangle([x, y, x+1, y+1], fill=fg_color)
    
    return img

def create_corner_icon(number, size=8, bg_color=(0, 0, 0), fg_color=(255, 255, 255)):
    """Create icon starting from corners."""
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Corner positions (clockwise from top-left)
    corners = [
        (0, 0), (7, 0), (7, 7), (0, 7),  # Corners
        (1, 0), (6, 0), (7, 1), (7, 6),  # Near corners
        (0, 1), (0, 6), (1, 7), (6, 7),  # Near corners
        (1, 1), (6, 1), (6, 6), (1, 6),  # Inner corners
        (2, 0), (5, 0), (7, 2), (7, 5),  # Expanding pattern
        (0, 2), (0, 5), (2, 7), (5, 7),  # Expanding pattern
        (2, 1), (5, 1), (6, 2), (6, 5),  # Inner expanding
        (1, 2), (1, 5), (2, 6), (5, 6),  # Inner expanding
        (3, 0), (4, 0), (7, 3), (7, 4),  # Center edges
        (0, 3), (0, 4), (3, 7), (4, 7),  # Center edges
        (2, 2), (5, 2), (5, 5), (2, 5),  # Inner squares
        (3, 1), (4, 1), (6, 3), (6, 4),  # More inner
        (1, 3), (1, 4), (3, 6), (4, 6),  # More inner
        (3, 2), (4, 2), (5, 3), (5, 4),  # Center area
        (2, 3), (2, 4), (3, 5), (4, 5),  # Center area
        (3, 3), (4, 3), (4, 4), (3, 4)   # Center
    ]
    
    for i in range(min(number, len(corners))):
        x, y = corners[i]
        draw.rectangle([x, y, x+1, y+1], fill=fg_color)
    
    return img

def generate_all_patterns(output_dir="icons_advanced"):
    """Generate icons with different patterns."""
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Color schemes
    schemes = {
        "classic": {"bg": (0, 0, 0), "fg": (255, 255, 255)},
        "blue": {"bg": (0, 0, 0), "fg": (0, 150, 255)},
        "green": {"bg": (0, 0, 0), "fg": (0, 255, 0)},
        "yellow": {"bg": (0, 0, 0), "fg": (255, 255, 0)},
        "cyan": {"bg": (0, 0, 0), "fg": (0, 255, 255)}
    }
    
    patterns = {
        "sequential": create_tix_icon,
        "spiral": create_spiral_icon,
        "checkerboard": create_checkerboard_icon,
        "corners": create_corner_icon
    }
    
    print("Generating icons with different patterns and colors...")
    
    for pattern_name, pattern_func in patterns.items():
        pattern_dir = f"{output_dir}/{pattern_name}"
        if not os.path.exists(pattern_dir):
            os.makedirs(pattern_dir)
        
        for scheme_name, colors in schemes.items():
            scheme_dir = f"{pattern_dir}/{scheme_name}"
            if not os.path.exists(scheme_dir):
                os.makedirs(scheme_dir)
            
            for digit in range(10):
                icon = pattern_func(digit, 8, colors["bg"], colors["fg"])
                filename = f"{scheme_dir}/icon_{digit}.png"
                icon.save(filename)
            
            print(f"Created: {scheme_dir}/ (20 icons)")
    
    print(f"\nAll icons saved to '{output_dir}/' directory")
    print("Choose your favorite pattern and color scheme!")

if __name__ == "__main__":
    generate_all_patterns()
