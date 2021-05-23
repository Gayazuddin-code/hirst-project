import turtle
from turtle import Turtle, Screen
import random
import paint_colors

timmy = Turtle()
turtle.colormode(255)
timmy.pensize(2)
timmy.speed(0)
timmy.hideturtle()


def spirograph():
    for _ in range(200):
        timmy.color(random.choice(paint_colors.avaliable_colors()))
        timmy.circle(150)
        timmy.left(3)
        if timmy.heading() == 0.0:
            break


spirograph()

screen = Screen()
screen.exitonclick()
