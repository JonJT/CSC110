# **********************************************
# WS ch4_7
# Use make_window(colr, ttle), make_turtle(colr, sz) & 
# draw_rectangle(t,W,H) to have
# Tess make a 100 x 50 rectangle
# Alex make a 150 x 200 rectangle at 45 deg wrt horizontal
# Dave make a 200 x 250 rectangle at 70 deg wrt horizontal
# ***********************************************

import turtle

def make_window(colr, ttle):
    '''Set up the window with the given background color and title. Returns the new window.'''
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    '''Set up a turtle with the given color and pensize. Returns the new turtle.'''
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_rectangle(t, w, h):
    '''Get turle t to draw a rectangle of width w and height h.'''
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)

wn = make_window("lightgreen", "tress, alex & dave")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

t, w, h = tess, 100, 50
draw_rectangle(t, w, h)
t, w, h = alex, 150, 200
t.lt(45)
draw_rectangle(t, w, h)
t, w, h = dave, 200, 250
t.lt(70)
draw_rectangle(t, w, h)

wn.mainloop()