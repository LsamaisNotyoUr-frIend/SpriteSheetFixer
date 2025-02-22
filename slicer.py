import cv2
import numpy as np
from PIL import Image, ImageChops
import os

# ---- CONFIGURATION ----
#enter the location of the spritesheet it r"D:\outputs\spritesheets\walk.png"
SPRITE_SHEET = r"something"
SPRITE_WIDTH = 80  # Original sprite width
SPRITE_HEIGHT = 80  # Original sprite height
#enter an output folder something like r"D:\outputs\spritesheets"
OUTPUT_SPRITESHEET = r"C:\Users\thega\Games\Other\Generalassests\Unassigned\Redhood\final_atk_spritesheet.png"

# Load sprite sheet
sheet = cv2.imread(SPRITE_SHEET, cv2.IMREAD_UNCHANGED)
if sheet is None:
    raise FileNotFoundError(f"Could not load sprite sheet: {SPRITE_SHEET}")

sheet_h, sheet_w, _ = sheet.shape

# Calculate number of sprites
cols = sheet_w // SPRITE_WIDTH
rows = sheet_h // SPRITE_HEIGHT
total_sprites = rows * cols

# Define output sprite sheet size
OUTPUT_WIDTH = 2080  # Final sprite sheet width
OUTPUT_HEIGHT = 80   # Final sprite sheet height

# Create empty final sprite sheet
final_sheet = Image.new("RGBA", (OUTPUT_WIDTH, OUTPUT_HEIGHT), (0, 0, 0, 0))


def get_bounding_box(image):
    """ Get the bounding box of non-transparent pixels. """
    bbox = image.getbbox()
    return bbox if bbox else (0, 0, image.width, image.height)


# Process each sprite and place it on the final sprite sheet
x_offset = 0
for y in range(rows):
    for x in range(cols):
        if x_offset >= OUTPUT_WIDTH:  # Prevent exceeding width
            break

        sprite = sheet[
            y * SPRITE_HEIGHT:(y + 1) * SPRITE_HEIGHT,
            x * SPRITE_WIDTH:(x + 1) * SPRITE_WIDTH
        ]

        # Convert to PIL Image
        sprite_pil = Image.fromarray(cv2.cvtColor(sprite, cv2.COLOR_BGRA2RGBA))

        # Trim extra transparent pixels
        bbox = get_bounding_box(sprite_pil)
        trimmed_sprite = sprite_pil.crop(bbox)

        # Create empty canvas (160x160) and center sprite
        canvas = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        offset_x = (160 - trimmed_sprite.width) // 2
        offset_y = (160 - trimmed_sprite.height) // 2
        canvas.paste(trimmed_sprite, (offset_x, offset_y), trimmed_sprite)

        # Crop directly to 80x80 (keeping the centered part)
        final_sprite = canvas.crop((40, 40, 120, 120))

        # Paste onto final sprite sheet
        final_sheet.paste(final_sprite, (x_offset, 0), final_sprite)
        x_offset += 80

# Save final sprite sheet
final_sheet.save(OUTPUT_SPRITESHEET)
print(f"✅ Done! Final sprite sheet saved at '{OUTPUT_SPRITESHEET}'")