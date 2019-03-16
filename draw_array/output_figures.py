from turtle import *

def draw_shape(sides, length):
    begin_fill()
    for _ in range(sides):
        forward(length)
        right(360 / sides)
        #fillcolor("green")
    end_fill()

def draw_matrix(matrix):
    print("Write here your code")

matrix = [
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0]
         ]

setup (width=600, height=600, startx=0, starty=0)
color('yellow')
# shape("turtle")
hideturtle()

speed(30)
draw_matrix(matrix)

exitonclick()