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
        data = json.load(json_file)
    return data["quotes"]

def load_templates():
    with open('data.json', 'r', encoding="utf8") as json_file:
        data = json.load(json_file)
    return data["templates"]
    
def get_quote(quotes: list, n: int) -> dict:
    return quotes[n]

def get_template(templates: list, n: int) -> dict:
    return templates[n]

def wrap_text(text: str, width: int) -> str:
    wrapped_text = textwrap.fill(text, width=width)
    return wrapped_text

def create_quote_image(quote_dict: dict, template: dict, n: int) -> str:
    WHITE = (255, 255, 255)
    quote = quote_dict["quote"]
    author = quote_dict["author"]

    quote_font_path = template["quote_font_path"]
    author_font_path = template["author_font_path"]
    frame_path = template["frame_path"]
    
    quote_font_size = template["quote_font_size"]
    author_font_size = template["author_font_size"]
    wrap_width = template["wrap_width"]

    quote_position = template["quote_position"]
    author_position = template["author_position"]

    quote_font = ImageFont.truetype(quote_font_path, quote_font_size)
    author_font = ImageFont.truetype(author_font_path, author_font_size)
    frame = Image.open(frame_path)
    draw = ImageDraw.Draw(frame)
    
    wrapped_quote = wrap_text(quote, wrap_width)
    
    draw.text(quote_position, wrapped_quote, font=quote_font, fill=WHITE, anchor="mm", align="center")
    draw.text(author_position, author, font=author_font, fill=WHITE, anchor="mm")

    image_path = f".\quotes\quote_{n}.jpg"
    frame.save(image_path)
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
    template_int = 1
    
    quotes = load_quotes()
    quote = get_quote(quotes, n)
    templates = load_templates()
    template = get_template(templates, template_int)
    
    image_path = create_quote_image(quote, template, n)
    caption = f"day {n}"
    
    post_to_instagram(image_path, caption)

if __name__ == "__main__":
    main()