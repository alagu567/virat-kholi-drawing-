import cv2
import turtle
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()  
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
)

if not image_path:
    print("No image selected!")
    exit()

SCALE = 4        
THRESHOLD = 120  

img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape
gray = cv2.resize(gray, (w // SCALE, h // SCALE))

edges = cv2.Canny(gray, 50, THRESHOLD)

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()

for y in range(edges.shape[0]):
    for x in range(edges.shape[1]):
        if edges[y][x] == 255:
            pen.goto(
                x - edges.shape[1] // 2,
                edges.shape[0] // 2 - y
            )
            pen.pendown()
            pen.dot(2)
            pen.penup()

turtle.done()
