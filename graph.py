from PIL import Image, ImageDraw, ImageFont
import math


image = Image.new("RGB", (600, 600), "white")
draw = ImageDraw.Draw(image)
#x, y = 25, 50
margin = 75
y_center = 45
x1_line, x2_line = 100, 70
font = ImageFont.load_default()

circle_size = 50


def text(text, y):
    y -= 1
    y_start = 20 + (circle_size*2/5) + 80 * y
    x_start = 20
    draw.text((x_start,y_start), text, fill='black', font=font)


def user_circle(x, y):
    x -= 1
    y -= 1
    x_start = 20 + 80 * x
    y_start = 20 + 80 * y
    draw.ellipse((x_start, y_start, x_start+circle_size, y_start+circle_size), 
                 fill = "pink", outline ='black')
    #draw.text((x+20,y+80), "(2,1)", fill='black', font=font)


def gpt_circle(x, y):
    x -= 1
    y -= 1
    x_start = 20 + 80 * x
    y_start = 20 + 80 * y
    draw.ellipse((x_start, y_start, x_start+circle_size, y_start+circle_size), 
                 fill = (100, 255, 100, 255), outline ='black')


def modified_circle(x, y):
    x -= 1
    y -= 1
    x_start = 20 + 80 * x
    y_start = 20 + 80 * y
    draw.ellipse((x_start, y_start, x_start+circle_size, y_start+circle_size), 
                 fill = (255, 100, 100, 255), outline ='black')
    

def suggestion_open(x, y):
    x_increment = x * 80
    y_increment = y * 80
    draw.line([(x1_line+x_increment, y_center + y_increment),
              (x2_line+x_increment, y_center + y_increment)], fill='red', width=3)


def suggestion_close(x, y):
   x_increment = x * 80
   y_increment = y * 80
   draw.line([(x1_line+x_increment, y_center + y_increment),
              (x2_line+x_increment, y_center + y_increment)], fill='black', width=3)


if __name__ == "__main__":

#start x axis for circles from 2, since text needs to be inserted
    user_circle(2, 4)
    gpt_circle(2, 1)
    gpt_circle(2, 2)
    gpt_circle(2, 3)
    gpt_circle(3, 2)
    gpt_circle(3, 3)
    gpt_circle(4, 3)
    modified_circle(2, 1)
    modified_circle(3, 1)
    suggestion_open(1,1)
    suggestion_close(2, 2)
    text("Sentence 1", 1)

    image.save("graph.jpg")
