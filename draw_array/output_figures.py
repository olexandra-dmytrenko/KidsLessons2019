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
        # fillcolor("green")
    end_fill()


def draw_matrix(matrix):
    color('yellow')
    speed(100)
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1:
                fillcolor("black")
            elif cell == 2:
                fillcolor("red")
            elif cell == 3:
                fillcolor("blue")
            else:
                fillcolor("yellow")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            penup()
            goto(curX, curY)
            pendown()
            draw_shape(4, shapeSide)

def draw_anime(arrayOfMatrix):
    for matrix in arrayOfMatrix:
        draw_matrix(matrix)
        # clear()

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

matrixMidSmileGlassesOn = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 3, 3, 1, 1, 3, 3, 1],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 1, 1, 2, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0]
    ]

matrixMidSmile = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0]
    ]

matrixNoSmile = \
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 3, 3, 0, 0, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

smileAnime = [matrixNoSmile, matrixMidSmile, matrixMidSmileGlassesOn, matrixSmile]

setup(width=600, height=600, startx=0, starty=0)

# shape("turtle")
hideturtle()

draw_anime(smileAnime)

exitonclick()
