# Modify the turtle bar chart program so that the bar for any value of 200 or more is filled
# with red, values between [100 and 200) are filled with yellow, and bars representing
# values less than 100 are filled with green.

import turtle
tess = turtle.Turtle()
wn = turtle.Screen()
tess.pensize(3)
wn.bgcolor("lightgreen")

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def fillColor(t,height):
    if height >=200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    drawBar(t,height)


xs = [48,117,200,240,160,260,220]

for a in xs:
    fillColor(tess,a)

wn.exitonclick()