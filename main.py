# add it with pillow
from PIL import Image, ImageDraw, ImageFont
import json
import textwrap

n = 7

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


frame.save("quote.png")


# Post to IG

