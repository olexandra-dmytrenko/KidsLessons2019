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
#t.fillcolor('red')

def draw_square()
t.forward(20)
t.left(90)
t.forward(50)
t.left(80)
t.forward(50)
t.left(90)
t.color('black', 'red')
t.forward(50)
t.left(90)


t.color('yellow')
draw_square()
draw_square()

t.shape("turtle")
#t.hideturtle()

t.speed(30)

t.exitonclick()