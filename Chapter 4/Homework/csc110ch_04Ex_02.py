# Write a program to draw this. Assume the innermost square is 20 units per side, and each
# successive square is 20 units bigger, per side, than the one inside it.

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.speed(0)
sz = 20

def drawSquare(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)

for i in range(5):
    drawSquare(t, sz)
    sz = sz + 20
    t.pu()
    t.bk(10)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.pd()

wn.exitonclick()