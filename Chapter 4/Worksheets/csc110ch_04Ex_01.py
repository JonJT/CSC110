# ************************************************
# WS ch4_1
# Write a function, draw_triangle(t,sz), 
# which draws an equilateral triangle of size sz using Turtle t.
# *************************************************




# draw_triangle(tess,150)

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.pensize(3)

def draw_triangle(t, sz, sides):
    for i in range(sides):
        t.fd(sz)
        t.lt(360 / sides)

draw_triangle(t, 150, 3)

wn.mainloop()