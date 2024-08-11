import pgzrun
from random import randint

TITLE = "PUT FIRE OUT"

WIDTH = 500
HEIGHT = 500

message = ""

fire = Actor("fire")

def draw():
    screen.clear()
    screen.fill(color = (128, 0,0))
    
    fire.draw()
    screen.draw.text(message, center = (400, 10), fontsize= 30)

def place_fire():
    fire.x = randint(50, WIDTH-50)
    fire.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
    global message
    if fire.collidepoint(pos):
        message = "Good Shot! You Put Out The Fire."
        place_fire()
    else:
        message = "You Missed"

place_fire()
pgzrun.go()


