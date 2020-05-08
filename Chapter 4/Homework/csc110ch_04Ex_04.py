# Draw this pretty pattern

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.speed(0)

def square():
    for i in range(4):
        t.fd(100)
        t.lt(90)

for i in range(20):
    t.lt(18)
    square()

wn.exitonclick()