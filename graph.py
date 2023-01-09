import numpy as np
from PIL import Image, ImageDraw, ImageFont


def user_square(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x
    y_start = margin + y_padding * y
    draw.rectangle((x_start, y_start, x_start+circle_size, y_start+circle_size),
                   fill=(100, 255, 100, 255), outline='black')


def text(text, y):
    y -= 1
    x_start = margin
    y_start = margin + (circle_size/3) + y_padding * y
    draw.text((x_start, y_start), text, fill='black', font=font)


def gpt_triangle(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x
    y_start = margin + y_padding * y
    draw.polygon([(x_start+circle_size/2, y_start), (x_start, y_start+circle_size),
                  (x_start+circle_size, y_start+circle_size)],
                 fill="blue", outline='black')


def prompt_circle(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x
    y_start = margin + y_padding * y
    draw.ellipse((x_start, y_start, x_start+circle_size, y_start+circle_size),
                 fill="black", outline='black')


def modified_triangle(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x
    y_start = margin + y_padding * y
    draw.polygon([(x_start+circle_size/2, y_start), (x_start, y_start+circle_size),
                  (x_start+circle_size, y_start+circle_size)],
                 fill="grey", outline='black')


def empty_triangle(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x
    y_start = margin + y_padding * y
    draw.polygon([(x_start+circle_size/2, y_start), (x_start, y_start+circle_size),
                  (x_start+circle_size, y_start+circle_size)],
                 fill="white", outline='black')


def suggestion_open(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x + circle_size/2
    y_start = margin + (circle_size/2) + y_padding * y
    draw.line([(x_start, y_start),
              (x_start-line_size, y_start)], fill='red', width=3)


def user_change(x, y):
    x -= 1
    y -= 1
    x_start = sentence_margin + margin + x_padding * x + circle_size/2
    y_start = margin + (circle_size/2) + y_padding * y
    # Dotted line
    x_start = int(x_start)
    for dash in range(x_start, x_start-line_size, -4):
        draw.line([(dash, y_start), (dash-2, y_start)], fill="orange", width=3)


def draw_graph(event_seq_dict, name="graph"):

    # Define global variables
    global margin
    global circle_size
    global sentence_margin
    global x_padding
    global y_padding
    global line_size
    global draw
    global font

    # Graph config
    margin = 25
    circle_size = 20
    sentence_margin = 80
    x_padding = 50
    y_padding = 30
    line_size = x_padding

    # Compute image dimensions
    y_len = len(event_seq_dict["num_sent"]) - 1
    x_len = np.max([len(x) for x in event_seq_dict["sequence"]]) - 1
    image_height = (margin * 2) + (y_padding * y_len) + circle_size
    image_width = sentence_margin + \
        (margin * 2) + (x_padding * x_len) + circle_size

    # Initialize image canvas
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw lines
    for idx, event_seq in enumerate(event_seq_dict["sequence"]):
        image_text = "Sentence " + str(idx+1)
        text(image_text, idx+1)
        for i, op in enumerate(event_seq):
            if op == "gpt3-call" and i != 0:
                suggestion_open(i+1, idx+1)
            if op == "user" and i != 0:
                user_change(i+1, idx+1)
            if op == "modify-gpt3" and i != 0:
                user_change(i+1, idx+1)
            if op == "empty-call" and i != 0:
                suggestion_open(i+1, idx+1)

    # Draw nodes
    for idx, event_seq in enumerate(event_seq_dict["sequence"]):
        image_text = "Sentence " + str(idx+1)
        text(image_text, idx+1)
        for i, op in enumerate(event_seq):
            if op == "gpt3-call":
                gpt_triangle(i+1, idx+1)
            if op == "user":
                user_square(i+1, idx+1)
            if op == "prompt":
                prompt_circle(i+1, idx+1)
            if op == "modify-gpt3":
                modified_triangle(i+1, idx+1)
            if op == "empty-call":
                empty_triangle(i+1, idx+1)

    # Save graph
    image.save(str("./" + name + ".png"))
