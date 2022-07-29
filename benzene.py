import time
import displayio
from adafruit_turtle import turtle, Color
from unigui.pygamedisplay import PygameDisplay

WIDTH = 640
HEIGHT = 640
SF = 2
display = PygameDisplay(WIDTH, HEIGHT)

turtle = turtle(display)

benzsize = round(min(display.width, display.height) * 0.5)

print("Turtle time! Lets draw a rainbow benzene")

colors = (Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PURPLE)

turtle.pendown()
start = turtle.pos()

for x in range(benzsize):
    turtle.pencolor(colors[x%6])
    turtle.forward(x)
    turtle.left(59)

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click is not None:
        print(click)
    time.sleep(0.5)
