# Write a void (non-fruitful) function to draw a square. Use it in a program to draw the
# image shown below. Assume each side is 20 units. (Hint: notice that the turtle has
# already moved away from the ending point of the last square when the program ends.)

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")

def drawSquare(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)

for i in range(5):
    drawSquare(t, 20)
    t.pu()
    t.fd(40)
    t.pd()

wn.exitonclick()