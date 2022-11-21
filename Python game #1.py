import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race!")


def get_number_of_turtles():
    turtles = 0
    while True:
        turtles = input("Please enter number of Turtles (2 - 10): ")
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("The input is not valid. Try again! ")
            continue
        if 2 <= turtles <= 10:
            return turtles
        else:
            print("Sorry the number is out of range. Try again! ")


def create_turtles(colours):
    turtles = []
    spacingx = WIDTH // (len(colours) + 1)
    spacingy = -HEIGHT // 2 + 20
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacingx, spacingy)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colours):
    turtles = create_turtles(colours)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colours[turtles.index(racer)]


racers = get_number_of_turtles()
init_turtle()
random.shuffle(COLOURS)
colours = COLOURS[:racers]
winner = race(colours)
print("The", winner, "Turtle has won!")
time.sleep(5)

