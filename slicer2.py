
import cv2
import numpy as np
from PIL import Image
import os

# ---- CONFIGURATION ----
#enter the location of the spritesheet it r"D:\outputs\spritesheets\walk.png"
SPRITE_SHEET = r"hmm"
SPRITE_WIDTH = 80  # Change this based on your actual sprite width
SPRITE_HEIGHT = 80  # Change this based on your actual sprite height
CANVAS_SIZE = (160, 160)  # Final output size (adjust as needed)
#enter an output folder something like r"D:\outputs\spritesheets"
OUTPUT_FOLDER = r"yes"

# Load sprite sheet
sheet = cv2.imread(SPRITE_SHEET, cv2.IMREAD_UNCHANGED)
sheet_h, sheet_w, _ = sheet.shape

# Calculate rows and columns
cols = sheet_w // SPRITE_WIDTH
rows = sheet_h // SPRITE_HEIGHT

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each sprite
for y in range(rows):
    for x in range(cols):
        sprite = sheet[
            y * SPRITE_HEIGHT:(y + 1) * SPRITE_HEIGHT,
            x * SPRITE_WIDTH:(x + 1) * SPRITE_WIDTH
        ]

        # Convert to PIL Image
        sprite_pil = Image.fromarray(cv2.cvtColor(sprite, cv2.COLOR_BGRA2RGBA))

        # Create empty canvas
        canvas = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))

        # Center the sprite on the canvas
        offset_x = (CANVAS_SIZE[0] - SPRITE_WIDTH) // 2
        offset_y = (CANVAS_SIZE[1] - SPRITE_HEIGHT) // 2
        canvas.paste(sprite_pil, (offset_x, offset_y), sprite_pil)

        # Save centered sprite
        output_path = os.path.join(OUTPUT_FOLDER, f"sprite_{y}_{x}.png")
        canvas.save(output_path)

print(f"✅ Done! Sprites saved in '{OUTPUT_FOLDER}'")