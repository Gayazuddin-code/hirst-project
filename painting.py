import turtle
from turtle import Turtle, Screen
import paint_colors
import random

turtle.colormode(255)
tom = Turtle()
tom.hideturtle()
tom.speed(0)
tom.penup()
tom.setpos(-400, -400)
orginal_x = tom.xcor()

for _ in range(17):
    for _ in range(17):
        rgb_color = random.choice(paint_colors.avaliable_colors())
        tom.dot(20, rgb_color)
        tom.forward(50)
    tom.setpos(orginal_x, tom.ycor() + 50)

screen = Screen()
screen.exitonclick()
