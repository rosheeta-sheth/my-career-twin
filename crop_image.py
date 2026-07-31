from PIL import Image, ImageDraw, ImageOps
import sys

def crop_to_circle(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Make it a square first by cropping the center
    width, height = img.size
    min_dim = min(width, height)
    
    left = (width - min_dim) / 2
    # Shift the crop upwards to get more of the upper face
    top = (height - min_dim) * 0.15
    right = left + min_dim
    bottom = top + min_dim
    
    img = img.crop((left, top, right, bottom))
    
    # Create mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_dim, min_dim), fill=255)
    
    # Apply mask
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    
    # Save
    output.save(output_path, "PNG")
    print(f"Successfully saved circular profile to {output_path}")

if __name__ == "__main__":
    crop_to_circle(sys.argv[1], sys.argv[2])
