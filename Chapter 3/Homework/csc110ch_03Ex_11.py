# Write a program to draw a shape like this:
# star
# Hints:
# • Try this on a piece of paper, moving and turning your cellphone as if it was a turtle.
# Watch how many complete rotations your cellphone makes before you complete the
# star. Since each full rotation is 360 degrees, you can figure out the total number of
# degrees that your phone was rotated through. If you divide that by 5, because there
# are five points to the star, you’ll know how many degrees to turn the turtle at each
# point.
# • You can hide a turtle behind its invisibility cloak if you don’t want it
# shown. It will still draw its lines if its pen is down. The method is invoked as tess.hideturtle() . To make the turtle visible again, use
# tess.showturtle() .

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")

def star(s):
    for i in range(s):
        t.fd(100)
        t.lt((360 * 3) / 5)

star(5)