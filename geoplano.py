import turtle

# CONFIGS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
DRAWING_COLOR = "#FF0032"
RIGHT_MOUSE_BUTTON = 3
INITIAL_POSITION = (-47, 34)
PEN_POSITIONS = []
CURSOR_SIZE = 20
FONT_SIZE = 16
FONT = ('Arial', FONT_SIZE, 'bold')
HORIZONTAL_UNIT = 80.0
VERTICAL_UNIT = 73.0

def defScreen():
    screen = turtle.Screen()
    screen.title("Geoplano")
    screen.bgpic("fundo.png")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)
    return screen

def defPen():
    penTurtle = turtle.Pen("circle", visible=False)
    penTurtle.penup()
    penTurtle.setpos(INITIAL_POSITION)
    PEN_POSITIONS.append(INITIAL_POSITION)
    penTurtle.pendown()
    penTurtle.showturtle()
    penTurtle.speed(0)
    penTurtle.pencolor(DRAWING_COLOR)
    penTurtle.pensize(20)
    return penTurtle

def setPenPosition(x, y):
    pen.setpos(x, y)
    PEN_POSITIONS.append((x, y))
    print(PEN_POSITIONS)

def clearAllDrawings(x, y):
    pen.clear()

def goRight():
    x = pen.xcor() + HORIZONTAL_UNIT
    setPenPosition(x, pen.ycor())

def goLeft():
    x = pen.xcor() - HORIZONTAL_UNIT
    setPenPosition(x, pen.ycor())

def goUp():
    y = pen.ycor() + VERTICAL_UNIT
    setPenPosition(pen.xcor(), y)

def goDown():
    y = pen.ycor() - VERTICAL_UNIT
    setPenPosition(pen.xcor(), y)

screen = defScreen()
pen = defPen()

while True:
    screen.update()
    screen.listen()

    screen.onclick(clearAllDrawings, RIGHT_MOUSE_BUTTON)
    screen.onclick(setPenPosition)
    
    screen.onkey(goRight, "Right")
    screen.onkey(goLeft, "Left")
    screen.onkey(goDown, "Down")
    screen.onkey(goUp, "Up")