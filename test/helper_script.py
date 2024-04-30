from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import json

######## SETUP #########
CONFIG = json.loads("conf.json")

BACKGROUND = "1.png"

ZIMA_BLUE = "#18b6f4"
RATIO = (16, 10)

######## LOADING #########
im = Image.open(BACKGROUND)
width, height = im.size

######## CROPPING #########
w_div = width/RATIO[0]
h_div = height/RATIO[1]

if w_div != h_div:
    if w_div > h_div:
        new_width = h_div * RATIO[0]

        crop_window = ( int((width - new_width)/2), 0, width - int((width - new_width)/2), height)
    else:
        new_height = w_div * RATIO[1]

        crop_window = ( 0, int((height - new_height)/2), width, height - int((height - new_height)/2))
    
    im = im.crop( crop_window )

width, height = im.size

######## RECTANGLE #########
rectangle_pos = ( int(1/4 * width), int(1/4 * height), int(3/4 * width), int(3/4 * height))
im.paste(ZIMA_BLUE, rectangle_pos)

######## FONTS #########

FACE_FONT_SIZE = int(height/7)
MIDDLE_FONT_SIZE = int(height/37)
BOTTOM_FONT_SIZE = int(height/48)

FACE_FONT = ImageFont.truetype('open-san/OpenSans-Regular.ttf', FACE_FONT_SIZE)
MIDDLE_FONT = ImageFont.truetype('open-san/OpenSans-Regular.ttf', MIDDLE_FONT_SIZE)
BOTTOM_FONT = ImageFont.truetype('open-san/OpenSans-Regular.ttf', BOTTOM_FONT_SIZE)

######## TEXT #########

face = ""
middle = ""
bottom = ""

######## Drawing #########
I = ImageDraw.Draw(im)

I.text( ( int(1/28 * width) + int(1/4 * width), int(1/4 * height)), face, "#ffffff", font=FACE_FONT)
I.text( ( int(1/48 * width) + int(1/4 * width), FACE_FONT_SIZE + MIDDLE_FONT_SIZE + int(1/48 * height) + int(1/4 * height)), middle, "#ffffff", font=MIDDLE_FONT)
I.text( ( int(1/48 * width) + int(1/4 * width), height - int(1/3 * height)), bottom, "#ffffff", font=BOTTOM_FONT)

im.save("Zima_Bluescreen.png")