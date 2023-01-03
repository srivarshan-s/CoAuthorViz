# draw_circle.py
from PIL import Image, ImageDraw, ImageFont
import math

image = Image.new("RGB", (600, 600), "white")
draw = ImageDraw.Draw(image)
x, y = 25, 50
margin = 75
line_center = 85
x_line, y_line = 175, 100
font = ImageFont.load_default()


def user_circle(num):
    increment = num * 150
    draw.ellipse((x+increment, y, x+margin, y+margin),
                 fill=(100, 100, 255, 255), outline="black", width=2)
    draw.text((x+20,y+80), "(2,1)", fill='black', font=font)


def gpt_circle(num):
    increment = num * 150
    draw.ellipse((x+increment, y, x+increment+margin, y+margin),
                 fill=(100, 255, 100, 255), outline="black", width=2)


def modified_circle(num):
    increment = num * 150
    draw.ellipse((x+increment, y, x+increment+margin, y+margin),
                 fill=(255, 100, 100, 255), outline="black", width=2)


def suggestion_open(num):
    increment = num * 150
    draw.line([(x_line+increment, line_center),
              (y_line+increment, line_center)], fill='red', width=3)


def suggestion_close(num):
    increment = num * 150
    draw.line([(x_line+increment, line_center),
              (y_line+increment, line_center)], fill='black', width=3)

# draw.line([(x_line+300, line_center), (y_line+300, line_center)], fill='red', width=3)

# 50, 150


# if _name_ == "_main_":
if __name__ == "__main__":
    count_circle = 0
    count_line = 0
    for i in range(6):
        if count_circle == 0 or count_line == 0:
            if i == 1:
                user_circle(count_circle)
                count_circle += 1
            if i == 2:
                gpt_circle(count_circle)
                count_circle += 1
            if i == 3:
                modified_circle(count_circle)
                count_circle += 1
            if i == 4:
                suggestion_open(count_line)
                count_line += 1
            if i == 5:
                suggestion_close(count_line)
                count_line += 1
        else:
            if i == 1:
                user_circle(count_circle)
                count_circle += 1
            if i==2:
                gpt_circle(count_circle)
                count_circle += 1
            if i==3:
                modified_circle(count_circle)
                count_circle += 1
            if i==4:
                suggestion_open(count_line)
                count_line += 1
            if i==5:
                suggestion_close(count_line)
                count_line += 1 
        
    image.save("graph.jpg")
    #circle("circle.jpg")