import turtle

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
BG_COLOR = "gray"
DRAWING_COLOR2 = (255, 0, 50, 45)
DRAWING_COLOR = "#FF0032"
RIGHT_MOUSE_BUTTON = 3

# SCREEN DEFINITION
screen = turtle.Screen()
screen.title("Geoplano")
screen.bgpic("fundo.png")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

# PEN-TURTLE DEFINITION
penTurtle = turtle.Pen("circle")
penTurtle.speed(0)
penTurtle.pencolor(DRAWING_COLOR2)
penTurtle.pensize(20)

def clearAllDrawings(x, y):
    penTurtle.clear()

while True:
    screen.update()
    screen.onclick(penTurtle.setpos)
    screen.onclick(clearAllDrawings, RIGHT_MOUSE_BUTTON)