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
        if a - 1 < b < a + 1:
            break
    t.end_fill()
    t.penup()


def draw_square(color, size, x, y):
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.colormode(255)
    # цвет рукчи (контура) - темносиний
    t.color((40, 80, 120))
    # t.color(color, 'red')
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


def draw_flower_squared(size, start_x, start_y, color=(40, 80, 120)):
    # поворот цветочка, чтоб рисовался по диагонали ромбиками
    t.left(-45)
    # серединка
    draw_square((255, 255, 0), size, start_x, start_y)
    draw_square(color, size, start_x + size, start_y + size)
    draw_square(color, size, start_x - size, start_y - size)
    draw_square(color, size, start_x - size, start_y + size)
    draw_square(color, size, start_x + size, start_y - size)


def draw_flower_field():
    square_size = 20
    cur_height = 40  # start position
    size_increase = 8  # flower rate of growth
    cur_color = (150, 90, 10)  # start color for the furthest flowers, dark
    for row_number in range(0, 3):
        cur_width = -width / 2
        flower_size = 3 * square_size
        for col_number in range(int(width / flower_size)):
            draw_flower_squared(square_size, cur_width + square_size + 10, cur_height, cur_color)
            cur_width = cur_width + flower_size + 10
        cur_height = cur_height - flower_size - 3 * size_increase - 20
        square_size = square_size + size_increase
        cur_color = (cur_color[0] + 50, cur_color[1] - 45, cur_color[2])


#---------- initialize screen -----------
width = 600
height = 600
t.setup(width=width, height=height, startx=450, starty=100)
t.speed(0)
t.shape("turtle")
t.hideturtle()


#---------- draw sky and sun and flowers field -----------
draw_square((0, 191, 255), 600, -300, -300)
draw_sun()
draw_flower_field()

t.exitonclick()
