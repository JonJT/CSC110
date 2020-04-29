# **************************************************
# WS ch4_2
# Write a function, draw_rects(t,W1,H1,W2,H2), which uses Turtle t to draw 2 rectangles with the same center.  
# Can you use draw_rectangle(t,W,H) as a helper function?  Can you write any other useful helper functions?
# **************************************************



# draw_rects(tess,200,20,25,400)

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.pensize(3)

def cntr2LwrLft(t, w, h):
    """move t from center to lower left"""
    t.pu()
    t.bk(w / 2)
    t.lt(90)
    t.bk(h / 2)
    t.rt(90)
    t.pd()

def LweLft2Cntr(t, w, h):
    """move t from lower left to center"""
    t.pu()
    t.fd(w / 2)
    t.lt(90)
    t.fd(h / 2)
    t.rt(90)
    t.pd()

def draw_rect(t, w, h):
    """turtle t draws a rect of width w & height h."""
    cntr2LwrLft(t, w, h)
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)
    LweLft2Cntr(t, w, h)

def draw_rects(t, w1, h1, w2, h2):
    draw_rect(t, w1, h1)
    draw_rect(t, w2, h2)

draw_rects(t, 200, 50, 30, 300)

wn.mainloop()