from turtle import *


# def draw_square():
#     color('black', 'red')
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)

# def draw_spiral(radius):
#     original_xcor = xcor()
#     original_ycor = ycor()
#     speed = 1
#     while True:
#         forward(speed)
#         left(10)
#         speed += 0.1
#         if distance(original_xcor, original_ycor) > radius:
#             break

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