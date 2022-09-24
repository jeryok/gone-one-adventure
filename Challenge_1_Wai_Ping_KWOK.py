# -------------------------------------------------------------------------------------------
# Wai Ping KWOK
# 15 SEP 2022
# COMP 1296 Introduction to Programming Logic
# Variables and Data Types
# Assignment - Challenge 1
# Drawing a triangle with Python library turtle
# -------------------------------------------------------------------------------------------

# Importing the turtle library to be used to draw shapes on a drawing board
import turtle

# Creating a drawing board
board = turtle.Turtle()

# Setting the pen color to blue and pen size to 10
board.pencolor("blue")
board.pensize(10)

# Drawing the base of the triangle with length 150
board.forward(150)

# Drawing another side of the triangle
board.left(120)
board.forward(150)

# Drawing the other side of the triangle
board.left(120)
board.forward(150)

# END