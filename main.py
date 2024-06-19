import turtle as jam
import random

jam.colormode(255)
jam.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


jam.speed('fastest')


def gap(size):
    for _ in range(int(360/size)):
        jam.color(random_color())
        jam.circle(100)
        jam.setheading(jam.heading() + size)


jam.hideturtle()
gap(5)

jam.exitonclick()
