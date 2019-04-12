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


def draw_sun():
    t.penup()
    t.goto(-200, 200)
    a = abs(t.pos())
    t.pendown()
    t.begin_fill()
    t.color('red', 'yellow')
    while True:
        t.forward(150)
        t.left(170)
        b = abs(t.pos())
        if (a - 1 < b < a + 1):
            break
    t.end_fill()
    t.penup()


def draw_square(color, size):
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_flower_scuared(size, start_x, start_y):
    t.penup()
    t.left(45)

    t.goto(start_x, start_y)
    t.color('blue')
    draw_square('yellow', size)
    t.goto(start_x + size, start_y + size)
    draw_square('purple', size)
    t.goto(start_x -size, start_y-size)
    draw_square('orange', size)
    t.goto(start_x -size, start_y + size)
    draw_square('pink', size)
    t.goto(start_x + size, start_y-size)
    draw_square('blue', size)



width=600
height=600
t.setup(width=width, height=height, startx=450, starty=100)
t.speed(35)

draw_sun()

flower_size = 20

cur_width = -width/2
for number in range(int(width/(3*flower_size))):
    draw_flower_scuared(flower_size, cur_width + flower_size + 10, 0)
    cur_width = cur_width + 3* flower_size + 10

t.shape("turtle")
t.hideturtle()

t.exitonclick()
