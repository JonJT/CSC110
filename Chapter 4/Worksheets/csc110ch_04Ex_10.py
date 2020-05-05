# **********************************************
# WS ch 4-10
# This example is about helper functions, not conditionals.
# Write code to produce the following turtle output.  Use appropriate helper functions.
# **********************************************

import turtle

def draw_square (t, sz, pc, ps):
    t.pensize(ps)
    t.color(pc)
    for i in range (4):
        t.fd(sz)
        t.lt(90)

def LnOfSqrs(t, sz, pc, ps, n_s, sep_s):
    for i in range(n_s):
        draw_square(t, sz, pc, ps)
        t.pu()
        t.fd(sz + sep_s)
        t.pd()

def SqrOfLnOfSqrs(t, sz, pc, ps, n_s, sep_s):
    for i in range(4):
        LnOfSqrs(t, sz, pc, ps, n_s, sep_s)
        t.pu()
        t.fd(sep_s)
        t.lt(90)
        t.fd(sz)
        t.pd()

def LnOfSqrOfLnOfSqrs(t, sz, pc, ps, n_s, sep_s, n_L, sep_L):
    for i in range(n_L):
        SqrOfLnOfSqrs(t, sz, pc, ps, n_s, sep_s)
        t.pu()
        t.fd((n_s + 1)*(sz) + (n_s -1)* sep_s)
        t.fd(sep_L)
        t.pd()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
alex.speed(0)

alex.pu(); alex.bk(500); alex.pd()
LnOfSqrOfLnOfSqrs(alex, 12, "cyan", 4, 5, 5, 5, 30)

wn.mainloop()