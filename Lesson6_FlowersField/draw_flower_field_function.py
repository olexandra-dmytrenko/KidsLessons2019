#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
Нарисовать цветочек из квадратов,
чтоб серединка была желтой,
а лепестки других цветов
"""

import turtle as t


# t.goto(curX, curY)
# t.fillcolor('yellow')

def draw_sun():
    t.pendown()
    pos = t.Vec2D(-220, 120)
    abs_default = abs(pos)
    t.goto(pos)
    t.color('red', 'yellow')
    t.begin_fill()

    while True:
        t.forward(200)
        t.left(130)

        abs_current = abs(t.pos())
        if abs_current < abs_default + 1 and abs_current > abs_default - 1:
            # if int(curPos[0]) == -219 and int(curPos[1]) == 119:
            break
    t.end_fill()
    t.penup()
    # t.done()


def draw_square(x, y, size, color='red'):
    t.goto(x, y)
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


def draw_flower(pos_x, pos_y, outer_color, inner_color, scale=1):
    size = 1 * scale
    draw_square(pos_x, pos_y, size, inner_color)
    draw_square(pos_x + size, pos_y + size, size, outer_color)
    draw_square(pos_x - size, pos_y - size, size, outer_color)
    draw_square(pos_x - size, pos_y + size, size, outer_color)
    draw_square(pos_x + size, pos_y - size, size, outer_color)


# Program code
t.penup()
t.speed(50)
# draw_sun()
t.shape("turtle")
draw_flower(10, 50, "purple", "yellow", 10)
# t.hideturtle()


t.exitonclick()
