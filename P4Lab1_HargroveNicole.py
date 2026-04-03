# Nicole Hargrove
# Date: April 2 2026
# Assignment: P4LAB1
# Description: Program that uses turtle graphics to draw a house using a square and triangle with loops.

import turtle

# setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# create turtle
t = turtle.Turtle()
t.color("black", "green")
t.pensize(3)

# -------- DRAW SQUARE (FOR LOOP) --------
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# move to top of square
t.left(90)
t.forward(100)
t.right(90)

# -------- DRAW TRIANGLE (WHILE LOOP) --------
t.color("black", "darkgreen")
t.begin_fill()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

t.end_fill()

# keep window open
turtle.done()