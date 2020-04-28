# Write a program to draw a face of a clock

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
wn.bgcolor("black")
t.color("white")

def clock(h):
    t.stamp()
    mv = 30
    for i in range(h):
        t.pu()
        t.fd(50)
        t.pd()
        t.fd(15)
        t.pu()
        t.fd(20)
        t.stamp()
        t.home()
        t.rt(mv)
        mv = mv + (360 / h)

clock(12)

wn.mainloop()