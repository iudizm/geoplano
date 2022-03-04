import turtle

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
BG_COLOR = "gray"

# SCREEN CREATION
window = turtle.Screen()
window.title("Geoplano")
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)

while True:
    window.update()
