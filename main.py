# add it with pillow
from PIL import Image, ImageDraw, ImageFont
import json
import textwrap
import os
#from dotenv import load_dotenv
from instagrapi import Client
from datetime import datetime

def days_passed_since(date_str):
    current_date = datetime.now().date()
    target_date = datetime.strptime(date_str, '%d/%m/%Y').date()
    days_passed = (target_date - current_date).days
    return days_passed

target_date_str = '26/9/2023'
n = days_passed_since(target_date_str)

#load_dotenv()

# get quote
def get_quote(n: int) -> str:
    with open('quotes.json', 'r', encoding="utf8") as json_file:
        quotes = json.load(json_file)
    
    quote = quotes["quotes"][n]
    return quote


# add quote to template
def wrap_text(text, width):
    wrapped_text = textwrap.fill(text, width=width)
    return wrapped_text

WHITE = (255, 255, 255)
font_path = "./assets/fonts/BASKVILL.TTF"
frame_path = "./assets/images/frame.png"
quote = wrap_text(get_quote(n)["quote"], 40)
author = get_quote(n)["author"]
quote_position = (544, 554)
author_position = (544, 744)

font = ImageFont.truetype(font_path, 41)
frame = Image.open(frame_path)
draw = ImageDraw.Draw(frame)
draw.text(quote_position, quote, font=font, fill=WHITE, anchor="mm")
draw.text(author_position, author, font=font, fill=WHITE)

frame = frame.convert("RGB")

frame.save("quote.jpg", format="JPEG")


# Post to IG
username = os.getenv("IG_USERNAME")
password = os.getenv("IG_PASSWORD")


client = Client()
client.login(username=username, password=password)

client.photo_upload("quote.jpg", f"day {n}")
