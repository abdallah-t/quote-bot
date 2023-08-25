# add it with pillow
from PIL import Image, ImageDraw, ImageFont
import json

# get quote
def get_quote(n):
    with open('quotes.json', 'r', encoding="utf8") as json_file:
        quotes = json.load(json_file)
    
    quote = quotes["quotes"][n]
    return quote




WHITE = (255, 255, 255)
font_path = "./assets/fonts/BASKVILL.TTF"