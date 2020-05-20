# ws ch7_3
# randint(n1,n2) from the random module generates
# random ints from n1 to n2 inclusive.
# Write a function a function, ran_walk(t,Dz,n),
# which makes the turtle t move a distance Dz
# in a random direction n times.
# Use helper functions to set up the screen and
# set up the turtle.

import turtle
import random

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


def ran_walk(t, Dz, n):
    for i in range(n):
        ngl = random.randint(0, 359)
        t.lt(ngl)
        t.fd(Dz)


wn = make_window("black", "turtle does a random walk")
t = make_turtle("white", 2)
t.speed(0)
ran_walk(t, 5, 200)

wn.exitonclick()