# ***************************************
# WS ch3_4A :
# Write a program that uses a for loop to print
#     a rectangle using a function, rectangle(t,w,h),
# Using turtle, t, width, w, and height,h.
# ***************************************


import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
wn.bgcolor("black")
bob.color("red")
bob.pensize(4)

for i in range(2):
    bob.fd(50)
    bob.lt(90)
    bob.fd(100)
    bob.lt(90)