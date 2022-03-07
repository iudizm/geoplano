import turtle

# CONFIGS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
DRAWING_COLOR = "#FF0032"
RIGHT_MOUSE_BUTTON = 3
INITIAL_POSITION = (-47, 34)
PEN_POSITIONS = []
CURSOR_SIZE = 20
FONT_SIZE = 22
FONT = ('Arial', FONT_SIZE, 'bold italic')
HORIZONTAL_UNIT = 80.0
VERTICAL_UNIT = 73.0
NOTE_POSITION = (-600, 400)
NOTE_CONTENT = "Sugestão de atividade: Desenhe um retângulo que tenha 12 quadrados de área."

def defScreen():
    screen = turtle.Screen()
    screen.title("Geoplano")
    screen.bgpic("src/fundo.png")
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

def createSuggestionNote():
    note = turtle.Turtle()
    note.ht()
    note.penup()
    note.color("white")
    note.setpos(NOTE_POSITION)
    note.write(NOTE_CONTENT, align="left", font=FONT)

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
createSuggestionNote()

while True:
    screen.update()
    screen.listen()

    screen.onclick(clearAllDrawings, RIGHT_MOUSE_BUTTON)
    screen.onclick(setPenPosition)
    
    screen.onkey(goRight, "Right")
    screen.onkey(goLeft, "Left")
    screen.onkey(goDown, "Down")
    screen.onkey(goUp, "Up")