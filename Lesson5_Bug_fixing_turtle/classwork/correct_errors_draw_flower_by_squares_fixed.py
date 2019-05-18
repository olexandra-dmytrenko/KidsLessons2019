#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
Нарисовать цветочек из квадратов,
чтоб серединка была желтой,
а лепестки других цветов
"""

import turtle as t


#t.goto(curX, curY)
t.fillcolor('yellow')

def draw_square(color):
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


t.goto(60,60)
draw_square('purple')
t.goto(-60,-60)
draw_square('orange')
t.goto(-60,60)
draw_square('pink')
t.goto(60,-60)
draw_square('blue')
t.goto(0,0)
t.color('blue')
draw_square('yellow')
t.shape("turtle")
t.hideturtle()

t.speed(30)

t.exitonclick()