#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t


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