from Constants import *
from Board import *

def setup():
    global b
    size(CANVASSIZE, CANVASSIZE)
    background(*BACKGROUND)
    b = Board()

def draw():
    b.show()
    b.checkHover(mouseX, mouseY)

def mousePressed():
    if mouseButton == LEFT:
        b.checkLeftClick(mouseX, mouseY)
    elif mouseButton == RIGHT:
        b.checkRightClick(mouseX, mouseY)

def keyPressed():
    global b
    if key == ENTER:
        b = Board()