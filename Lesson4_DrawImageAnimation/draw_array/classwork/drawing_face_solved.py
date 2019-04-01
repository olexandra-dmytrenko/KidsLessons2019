
import turtle as t

def draw_shape(sides, length):
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)
        #fillcolor("green")
    t.end_fill()

def draw_matrix(matrix):
    t.color('yellow')
    t.speed(100)
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1:
                t.fillcolor("black")
            else:
                t.fillcolor("yellow")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            t.penup()
            t.goto(curX, curY)
            t.pendown()
            draw_shape(4, shapeSide)


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

t.setup (width=600, height=600, startx=0, starty=0)

# shape("turtle")
t.hideturtle()

t.speed(30)
draw_matrix(matrix)

t.exitonclick()