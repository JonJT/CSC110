# Use for loops to make a turtle draw these regular polygons (regular means all sides the
# same lengths, all angles the same):
# • An equilateral triangle
# • A square
# • A hexagon (six sides)
# • An octagon (eight sides)

# use helper function

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")

def plygns(n):
    for l in range(n):
        t.fd(100)
        t.lt(360/n)

plygns(3) # equilateral triangle

plygns(4) # square

plygns(6) # hexagon

plygns(8) # octagon

wn.mainloop()