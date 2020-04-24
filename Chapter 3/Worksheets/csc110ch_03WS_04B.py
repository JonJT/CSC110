# ***************************************

# WS ch3_4B:
# Use rectangle(t,w,h) to write a function, 
# pinwheel_1(t,w,h,n),  that uses rectangle(t,w,h) to make a pinwheel using turtle, t.  
# n is an int that tells how many rectangles to make within a turn of 360 degrees.
# ***************************************

import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
wn.bgcolor("black")
bob.color("red")
bob.pensize(4)

def rect (t,w,h):
    '''turtle t draws rectangle of width W and of hight H.'''
    trn = 90
    for i in range(2):
        bob.fd(50)
        bob.lt(trn)
        bob.fd(100)
        bob.lt(trn)

def pinwheelRect(t,w,h,n):
    '''turtle t draws n rectangle of width W and of hight H, in a circle. Ue rect (t, W, H) as a helper function.'''
    trnAngle = 360/n
    for i in range(n):
        rect(t, w, h)
        t.lt(trnAngle)

pinwheelRect(bob, 100, 50, 6)
