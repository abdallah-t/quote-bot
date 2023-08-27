from PIL import Image, ImageDraw, ImageFont
import json
import textwrap
import os
from instagrapi import Client
from datetime import datetime

def days_passed_since(date_str):
    current_date = datetime.now().date()
    target_date = datetime.strptime(date_str, '%d/%m/%Y').date()
    days_passed = (current_date - target_date).days
    return days_passed

def load_quotes():
    with open('data.json', 'r', encoding="utf8") as json_file:
        quotes = json.load(json_file)
    return quotes["quotes"]

def load_templates():
    with open('data.json', 'r', encoding="utf8") as json_file:
        quotes = json.load(json_file)
    return quotes["templates"]
    
def get_quote(quotes, n):
    return quotes[n]

def wrap_text(text, width):
    wrapped_text = textwrap.fill(text, width=width)
    return wrapped_text

def create_quote_image(quote, author, n):
    WHITE = (255, 255, 255)
    font_path = "./assets/fonts/BASKVILL.TTF"
    frame_path = "./assets/images/frame.png"

    quote_position = (544, 554)
    author_position = (544, 744)

    font = ImageFont.truetype(font_path, 41)
    frame = Image.open(frame_path)
    draw = ImageDraw.Draw(frame)
    
    wrapped_quote = wrap_text(quote, 40)
    
    draw.text(quote_position, wrapped_quote, font=font, fill=WHITE, anchor="mm")
    draw.text(author_position, author, font=font, fill=WHITE)

    frame = frame.convert("RGB")
    image_path = f".\quotes\quote_{n}.jpg"
    frame.save(image_path, format="JPEG")
    return image_path

def post_to_instagram(image_path, caption):
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")
    
    client = Client()
    client.login(username=username, password=password)
    
    client.photo_upload(image_path, caption)

def main():
    target_date_str = '26/8/2023'
    n = days_passed_since(target_date_str)
    
    quotes = load_quotes()
    quote_data = get_quote(quotes, n)
    
    quote = quote_data["quote"]
    author = quote_data["author"]
    
    image_path = create_quote_image(quote, author, n)
    caption = f"day {n}"
    
    #post_to_instagram(image_path, caption)

if __name__ == "__main__":
    main()