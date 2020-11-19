import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

class game:
    def __init__(self):
        self.x, self.y = WIDTH / 2, HEIGHT / 2
        self.delay = 10
        self.tick = 0

g = game()

def draw():
    screen.clear()
    screen.draw.filled_circle((g.x, g.y), 50, "red")


def update():
    if g.tick == g.delay:
        g.x += randint(-10, 10)
        g.y += randint(-10, 10)
        g.tick = 0
    else:
        g.tick += 1


pgzrun.go()