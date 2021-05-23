import turtle
from turtle import Turtle
import random
import paint_colors

tim = Turtle()
turtle.colormode(255)


def shape(sides, angle):
    for side in range(sides):
        tim.forward(100)
        tim.right(angle)


for fig in range(3, 11):
    tim.color(random.choice(paint_colors.avaliable_colors()))
    angle_deg = 360 / fig
    shape(fig, angle_deg)

screen = turtle.Screen()
screen.exitonclick()
