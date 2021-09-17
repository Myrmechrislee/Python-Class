import turtle as t, numpy as n, time
from tkinter import *

screen = t.Screen()
screen.setup(1000, 1000)

board = t.Turtle()
board.speed(0)
board.hideturtle()

u = t.Turtle()
u.hideturtle()
u.penup()
u.speed(0)

points = []
square = (-200, 200, 400, 400)
circle = (0, 0, 200)
 
# draws a rectangle given top left position of a rectangle
def draw_rectangle(board,x,y,width,height,size,color):
  board.pencolor(color)
  board.pensize(size)
  board.setheading(0)
  board.up()
  board.setposition(x,y)
  board.down()
  # draw top
  board.forward(width)
  # draw right
  board.right(90)
  board.forward(height)
  # draw bottom
  board.right(90)
  board.forward(width)
  # draw left
  board.right(90)
  board.forward(height)
  board.end_fill()

def draw_point(x, y):
  board.penup()
  board.setposition(x, y)
  board.pendown()
  board.begin_fill()
  board.circle(.1)
  board.end_fill()

def draw_circle():
  board.penup()
  board.setposition(circle[0] + circle[2], circle[1])
  board.pendown()
  board.pencolor("green")
  board.circle(circle[2])

def stats_box():
    count = len(points)
    nsquare = float(len([p for p in points if square[0] < p[0] < square[0] + square[2] and - square[1] < p[1] < - square[1] + square[3]]))
    ncircle = float(len([p for p in points if n.sqrt(n.square(circle[0] - p[0]) + n.square(circle[1] - p[1])) < circle[2]]))
    (x, y) = (-400, 350)
    u.setposition(x, y)
    u.write("n(E)=" + str(count), font=("Arial", 24, "normal"))
    u.setposition(x, y-25)
    u.write("n(square)=" + str(nsquare), 
    font=("Arial", 24, "normal"))
    u.setposition(x, y-50)
    u.write("Pr(square)=" + str(nsquare / count), 
    font=("Arial", 24, "normal"))
    u.setposition(x, y-75)
    u.write("n(Circle)=" + str(ncircle), 
    font=("Arial", 24, "normal"))
    u.setposition(x, y-100)
    u.write("Pr(Circle)=" + str(ncircle / count), font=("Arial", 24, "normal"))
    u.setposition(x, y-125)
    if ncircle == 0 or nsquare == 0:
      u.write("Pr(Circle|Square)=0", font=("Arial", 24, "normal"))
    else:
      u.write("Pr(Circle|Square)=" + str(ncircle / nsquare), font=("Arial", 24, "normal"))

draw_rectangle(board, square[0], square[1], square[2], square[3], 5, "blue")
draw_circle()

# while True:
#   points.append(n.random.randint(-300, 300, (2)))
#   stats_box()
#   draw_point(points[-1][0], points[-1][1])
#   time.sleep(1/4.0)
#   for _ in range(12):
#     u.undo()

points = n.random.randint(-300, 300, (1000, 2))
board.color("red")
for p in points:
  draw_point(p[0], p[1])

stats_box()

ts = t.getscreen()
ts.getcanvas().postscript(file="random.eps")