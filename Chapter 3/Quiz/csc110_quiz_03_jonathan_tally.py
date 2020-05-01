# CSC 110 Spring 2020  Quiz 3 Take-home                       NAME: Jonathan Tally
# Write clear, legible code, the simpler the better. Make sure your code works.   Due Monday at class start.  
# Use the editor to write your code.  Also, submit a file, Quiz_3_YourFullName.py in an email that has as subject csc 110 quiz 3_YourFullName.   
# Points will be deducted if submission is late.


# (20 pts) Write a function, mltyClrdSqr(t ,sz,clr1, clr2, clr3, clr4), that has turtle, t, 
# draw a square of size, sz, that has sides colored clr1, clr2, clr3, clr4.  The turtle tess’s pensize has previously been set to 5.  Sample run:

# mltyClrdSqr(tess,150,'red’, 'green’, 'blue’,  'magenta')

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.pensize(5)
t.speed(0)


def mltyClrdSqr(t, sz, clr1, clr2, clr3, clr4):
    '''turtle, t, assign color clr#, draw square'''
    for i in (clr1, clr2, clr3, clr4):
        t.color(i)
        t.fd(sz)
        t.lt(90)


mltyClrdSqr(t, 50, 'red', 'green', 'blue', 'magenta')

# 2.  (10 pts)  Use the previous function as a helper function to write the function
# lineOfMltyClrdSqrs(t, sz, , clr1, clr2, clr3, clr4, spc, n), where turtle, t,  draws 
# n multicolored squares of size, sz, each with colors clr1,clr2,clr3,clr4, where spc is the 
# distance moved from the end of the square to the beginning of the next square. Sample runs:


def lineOfMltClrdSqrs(t, sz, clr1, clr2, clr3, clr4, spc, n):
    t.pu()                              # pick pen up
    t.bk(((sz * n) + (spc * n)) / 2)    # move pen to the left so that squares are centered in the graphic display
    t.pd()                              # put pen down
    for i in range(n):
        mltyClrdSqr(t, sz, clr1, clr2, clr3, clr4)
        t.pu()
        t.fd(sz + spc)
        t.pd()

lineOfMltClrdSqrs(t,50,'red','green','blue','magenta',20,6)

def lineOfMltyClrdSqrs(t, sz, clr1, clr2, clr3, clr4, spc, n):
    t.pu()                              # pick pen up
    t.bk(((sz * n) + (spc * n)) / 2)    # move pen to the left so that squares are centered in the graphic display
    t.pd()                              # put pen down
    for i in range(n):
        mltyClrdSqr(t, sz, clr1, clr2, clr3, clr4)
        t.pu()
        t.fd(sz + spc)
        t.pd()

lineOfMltyClrdSqrs(t, 30, 'red', 'green', 'blue', 'magenta', 40, 5)


wn.mainloop()