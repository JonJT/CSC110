# ws ch7_4
# Write a function, stop_when_circle_xd(t,Dz,R),
# which makes the turtle t execute a random walk of size Dz
# for each step, and which stops the first time the turtle
# is >= radius of R from its start point.
# Use a separate turtle to draw a circle of radius R
# Uses the  turtle position()
# Function, which returns the x and y coordinate for the current
# Position of the turtle.
# Print out the number of steps the turtle takes before stopping.


import turtle, random, math

def draw_circle(t, R):
    '''draws a circle of a radius R centered at the origin.'''
    t.pu(); t.lt(90); t.bk(R); t.rt(90); t.pd()
    t.circle(R)


def stop_when_circle_xd(t, Dz, R):
    '''makes the turtle t execute a random walk of the size Dz for each step, and which stops the first time the turtle
    is >= radius for R from its start point.'''
    current_R, num_steps = 0, 0
    while (current_R <= R):
        ngl = random.randint(0, 359); t.lt(ngl); t.fd(Dz)
        num_steps += 1
        x, y = t.pos()
        current_R = math.sqrt(x**2 + y**2)
    print('Turtle took', num_steps, 'steps before crossing circle of R = ', R)


def make_window(colr, ttle):
    '''set up the window with the given background color and title.'''
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    '''set up a turtle with given color and pensize.Returns the new turtle.'''
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


wn = make_window("black", "turtle does a random walk")
t = make_turtle("white", 2)
t.speed(0)
d = make_turtle('blue', 3)

draw_circle(d, 300)
stop_when_circle_xd(t, 15, 300)

wn.exitonclick()