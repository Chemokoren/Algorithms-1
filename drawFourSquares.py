import turtle
import tkinter as TK

# my_turtle =turtle.Turtle()
# my_turtle.shape('turtle')
# drawing_area =turtle.Screen()
# # my_turtle.penup()
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)

#
# import turtle
#
# my_turtle =turtle.Turtle()
# my_turtle.shape('turtle')
# drawing_area =turtle.Screen()
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)

# import turtle
#
# my_turtle =turtle.Turtle() # create instance of the turtle
# my_turtle.shape('turtle') #  set the shape of the turtle to that of the turtle
# drawing_area =turtle.Screen() # create the screen
# my_turtle.penup()  # lift the pen up so when the turtle moves, it will not leave a trace behind
# my_turtle.left(90) #
# for i in range(4):
#   my_turtle.forward(200)
#   my_turtle.right(90)


import turtle

def drawSquares(myTurtle, sideLength, nSquares, distanceApart):

    for n in range(nSquares):

        for _ in range(4):
            myTurtle.forward(sideLength)
            myTurtle.left(90)

        myTurtle.penup()
        x, y = myTurtle.position()
        myTurtle.goto(x + distanceApart / 2, y + distanceApart / 2)
        myTurtle.pendown()

        sideLength -= distanceApart

def drawSquares3(yourTurtle, sideLength, nSquares, distanceApart):
    myTurtle = yourTurtle.clone()  # clone turtle so we don't have to restore changes

    myTurtle.shape("square")  # modify turtle shape for stamping
    myTurtle.fillcolor(turtle.bgcolor())  # modify turtle fill color for stamping

    for _ in range(nSquares):
        myTurtle.turtlesize(sideLength / 20)  # magic number 20 is default stamp size
        myTurtle.stamp()
        sideLength -= distanceApart

def drawSquares2(myTurtle, sideLength, nSquares, distanceApart):
    if nSquares < 1:
        return

    for _ in range(4):
        myTurtle.forward(sideLength)
        myTurtle.left(90)

    myTurtle.penup()
    x, y = myTurtle.position()
    myTurtle.goto(x + distanceApart / 2, y + distanceApart / 2)
    myTurtle.pendown()

    drawSquares(myTurtle, sideLength - distanceApart, nSquares - 1, distanceApart)

def drawSquares1(myTurtle, sideLength, nSquares, distanceApart):

    myTurtle.penup()
    x, y = myTurtle.position()
    myTurtle.goto(x - sideLength/ 2, y - sideLength / 2)  # adjust so current x, y is center
    myTurtle.pendown()

    myTurtle.setheading(-45)  # by default square would be sitting on corner instead of on side

    for _ in range(nSquares):
        radius = sideLength * 2**0.5 / 2
        myTurtle.circle(radius, steps=4)
        sideLength -= 10

        myTurtle.penup()
        x, y = myTurtle.position()
        myTurtle.goto(x + distanceApart / 2, y + distanceApart / 2)
        myTurtle.pendown()

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("tuts@fosslinux: How to draw 4 Squares in Python")

# yertle = turtle.Turtle()
# yertle.penup()
# yertle.goto(60, 60)
# yertle.pendown()
# drawSquares1(yertle, 200, 4, 10)
# turtle.done()
alex = turtle.Turtle()
for some_color in ["yellow", "red", "purple", "blue"]:
    alex.color(some_color)
    alex.forward(50)
    alex.left(90)
wn.exitonclick()

help(turtle.color)
# myTurtle = turtle.Turtle()
# def _drawSquares(myTurtle,sideLength, x, y, nSquares, distanceApart):
#     if nSquares > 0:
#         myTurtle.pu()
#         myTurtle.setx(x)
#         myTurtle.sety(y)
#         myTurtle.pd()
#         for i in range(4):
#             myTurtle.forward(sideLength)
#             myTurtle.right(90)
#         drawSquares(myTurtle, sideLength - distanceApart*2, x+10, y-10, nSquares-1, distanceApart)
#
# _drawSquares(myTurtle, 200, 60, 60, 4, 10)
