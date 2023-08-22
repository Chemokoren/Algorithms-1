import turtle
import tkinter as TK

# my_turtle =turtle.Turtle()
# my_turtle.shape('turtle')
# drawing_area =turtle.Screen()
# drawing_area.title("tuts@codeunderscored: Drawing a Square Anti-Clockwise")
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# drawing_area.exitonclick()



# import turtle
#
# my_turtle =turtle.Turtle()
# my_turtle.shape('turtle')
# drawing_area =turtle.Screen()
# drawing_area.title("tuts@codeunderscored: Drawing a Square Clockwise")
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# drawing_area.exitonclick()

# import turtle
#
# my_turtle =turtle.Turtle() # create instance of the turtle
# my_turtle.shape('turtle') #  set the shape of the turtle to that of the turtle
# drawing_area =turtle.Screen() # create the screen
# drawing_area.title("tuts@codeunderscored: Optimizing drawing a square ")
# my_turtle.pendown()  # lift the pen up so when the turtle moves, it will not leave a trace behind
# my_turtle.left(90) #
# for i in range(4):
#   my_turtle.forward(200)
#   my_turtle.right(90)
# drawing_area.exitonclick()


# """
# example 1
# """
#
# import turtle
#
# def drawSquares(my_turtle, length_of_side, count_squares, distance_apart):
#     for n in range(count_squares):
#         for _ in range(4):
#             my_turtle.forward(length_of_side)
#             my_turtle.left(90)
#
#         my_turtle.penup()
#         x, y = my_turtle.position()
#         my_turtle.goto(x + distance_apart / 2, y + distance_apart / 2)
#         my_turtle.pendown()
#         length_of_side -= distance_apart
#
# if __name__=='__main__':
#     window = turtle.Screen()        # Set up the window and its attributes
#     window.bgcolor("lightgreen")
#     window.title("tuts@codeunderscored:~ Example 1:How to draw 4 Squares in Python")
#
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.goto(60, 60)
#     new_turtle.pendown()
#     drawSquares(new_turtle, 200, 4, 10)
#     turtle.done()


# """
# Example 2
# """
# def drawSquares(my_turtle, side_length, no_of_squares, distance_apart):
#     new_turtle = my_turtle.clone()  # clone turtle so we don't have to restore changes
#
#     new_turtle.shape("square")  # modify turtle shape for stamping
#     new_turtle.fillcolor(turtle.bgcolor())  # modify turtle fill color for stamping
#
#     for _ in range(no_of_squares):
#         new_turtle.turtlesize(side_length / 20)  # magic number 20 is default stamp size
#         new_turtle.stamp()
#         side_length -= distance_apart
#
# if __name__=='__main__':
#     window = turtle.Screen()        # Set up the window and its attributes
#     window.bgcolor("grey")
#     window.title("tuts@codeunderscored:~ Example 2: How to draw 4 Squares in Python")
#
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.goto(10, 10)
#     new_turtle.pendown()
#     drawSquares(new_turtle, 200, 4, 10)
#     turtle.done()
#
# """
# Example 4
#
# """
# def drawSquares(my_turtle, side_length, no_of_squares, distance_apart):
#
#     """
#
#     :param my_turtle:    instance of the turtle
#     :param side_length:   initial length of the square e.g 200 before drawing the inner squares
#     :param no_of_squares:  determines how many squares exist e.g 5 means the count of squares is 5
#     :param distance_apart: distance from once square to the next
#     :return:
#     """
#     if no_of_squares < 1:
#         return
#     for _ in range(4):
#         my_turtle.forward(side_length)
#         my_turtle.left(90)
#
#     my_turtle.penup()
#     x, y = my_turtle.position()
#     my_turtle.goto(x + distance_apart / 2, y + distance_apart / 2)
#     my_turtle.pendown()
#
#     drawSquares(my_turtle, side_length - distance_apart, no_of_squares - 1, distance_apart)
#
# if __name__=='__main__':
#     window = turtle.Screen()        # window and attributes setup
#     window.bgcolor("yellow")
#     window.title("tuts@codeunderscored:~ Example 4: How to draw 4 Squares in Python")
#
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.goto(10, 10)
#     new_turtle.pendown()
#     drawSquares(new_turtle, 200, 4, 40)
#     turtle.done()

#
# """
# Example 3
# """
# def drawSquares(my_turtle, side_length, no_of_squares, distance_apart):
#
#     my_turtle.penup()
#     x, y = my_turtle.position()
#     my_turtle.goto(x - side_length/ 2, y - side_length / 2)  # current x, y is positioned at the center
#     my_turtle.pendown()
#
#     my_turtle.setheading(-45)  # square sits on corner instead of on side by default
#
#     for _ in range(no_of_squares):
#         radius = side_length * 2**0.5 / 2
#         my_turtle.circle(radius, steps=4) # determines the size of the shape 4 = square, 5=pentagon
#         side_length -= 50
#
#         my_turtle.penup()
#         x, y = my_turtle.position()
#         my_turtle.goto(x + distance_apart / 2, y + distance_apart / 2)
#         my_turtle.pendown()
#
# if __name__=='__main__':
#     window = turtle.Screen()        # window and attributes setup
#     window.bgcolor("blue")
#     window.title("tuts@codeunderscored:~ Example 3: How to draw 4 Squares in Python")
#
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.goto(10, 10)
#     new_turtle.pendown()
#     drawSquares(new_turtle, 200, 4, 50)
#     turtle.done()

# window = turtle.Screen()
# window.bgcolor("lightgrey")
# window.title("tuts@codeunderscored:~ Demonstrate how to draw a square with 4 colors")
# my_turtle = turtle.Turtle()
# my_turtle.pendown()
# for current_color in ["red", "green", "purple", "blue"]:
#     my_turtle.pensize(10)
#     my_turtle.color(current_color)
#     my_turtle.forward(200)
#     my_turtle.left(90)
# window.exitonclick()


# help(turtle.color)



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


import turtle

turtle.shape("turtle")

turtle.forward(25)

turtle.exitonclick()
