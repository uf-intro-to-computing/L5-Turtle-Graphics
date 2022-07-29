import time
import displayio
from adafruit_turtle import turtle, Color
from unigui.pygamedisplay import PygameDisplay

WIDTH = 640
HEIGHT = 640
SF = 2
display = PygameDisplay(WIDTH, HEIGHT)

turtle = turtle(display)

colors = [Color.YELLOW, Color.GREEN]

for _ in range(4):
    for i in range (5):
        turtle.pencolor(colors[i % 2])
        turtle.pendown()
        turtle.circle(60 - (i*10) )
        turtle.penup()
    turtle.right(90)

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click is not None:
        print(click)
    time.sleep(0.5)