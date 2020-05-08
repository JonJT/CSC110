# The two spirals in this picture differ only by the turn angle. Draw both.

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.speed(0)

def drawSpiral(t, angle):
    length = 1
    for i in range(84):
        t.fd(length)
        t.right(angle)
        length = length + 2

t.pu()
t.bk(110)
t.pd()

drawSpiral(t, 90)

t.pu()
t.home()
t.fd(90)
t.pd()

drawSpiral(t, 89)

wn.exitonclick()