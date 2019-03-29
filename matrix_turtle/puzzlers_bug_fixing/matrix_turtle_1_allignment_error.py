#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Виправіть синтаксичні помилки у методі draw_matrix
"""

import turtle as t
# from turtle import *

def draw_shape(sides, length):
    t.begin_fill()

    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)
    t.end_fill()


def draw_matrix(matrix):
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1:
                t.color("black")
                t.fillcolor("black")
            elif cell == 2:
                t.color("red")
                t.fillcolor("red")
            elif cell == 3:
                t.color("blue")
                t.fillcolor("blue")
            else:
                t.color("yellow")
                t.fillcolor("yellow")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            t.goto(curX, curY)
            draw_shape(4, shapeSide)


matrixSmile = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 3, 3, 1, 1, 3, 3, 1],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0]
    ]

t.setup(width=600, height=600, startx=0, starty=0)
t.hideturtle()

t.color('yellow')

t.speed(30)
draw_matrix(matrixSmile)

t.exitonclick()
