import turtle
from turtle import Turtle, Screen
import random
import paint_colors

tim = Turtle()
angle = [0, 90, 180, 270]
tim.hideturtle()
tim.speed(0)
tim.pensize(10)
turtle.colormode(255)


def random_walks():
    for _ in range(500):
        tim.pencolor(random.choice(paint_colors.avaliable_colors()))
        tim.forward(30)
        tim.setheading(random.choice(angle))


random_walks()
screen = Screen()
screen.exitonclick()
