# add it with pillow
from PIL import Image, ImageDraw, ImageFont
import json


WHITE = (255, 255, 255)
font_path = "./assets/fonts/BASKVILL.TTF"

# Open the image file
image = Image.open("./images/frame.png")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define font size and type
font = ImageFont.truetype(font_path, 32)