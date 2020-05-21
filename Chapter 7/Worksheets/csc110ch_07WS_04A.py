# Ws ch 7-4A

# Same as 7-4 but use a rectangle centered at the origin,
# stop_when_rect_xd(t,Dz,W,H), t execute a random walk of size Dz
# for each step, and which stops the first time the turtle
# is not inside the rectangle.  Print out the total distance travelled
# By the turtle. Turtle starts at rectangle center.

import turtle, random, math

def rectangle(t, w, h):
    '''Draws a rectangle of width w, height h centered at the origin.'''
    t.pu(); t.setpos(-w/2, -h/2); t.pd()
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)
    t.pu(); t.setpos(0, 0); t.pd()

def stopWhenLeaveRect(t, dz, w, h):
    '''makes the turtle t execute a random walk of size dz for each step,
    and which stops the first time the turtle is outside rectangle. t
    starts are rectangle center'''
    rectangle(t, w, h)
    x, y = t.pos()
    num_steps = 0
    while (-w/2 <= x <= w/2 and -h/2 <= y <= h/2):
        ngl = random.randint(0, 359); t.lt(ngl); t.fd(dz)
        num_steps += 1
        x, y = t.pos()
    print('Turtle travelled', num_steps*dz, 'before leaving the rectangle.')

def make_window(colr, ttle):
    '''set up the window with the given background color and title.'''
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    '''set up a turtle with given color and pensize.'''
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("black", "random walk inside rectangle")
t = make_turtle("white", 2)
t.speed(0)
stopWhenLeaveRect(t, 10, 500, 300)

wn.exitonclick()