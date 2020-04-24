import turtle
wn = turtle.Screen()
BC = input("Please enter a background colo: ")
wn.bgcolor(BC) # User sets the window background color
wn.title("Hello, Bob") # Set the window title

bob = turtle.Turtle()

pc = input("Please enter the turtles pen color: ")
bob.color(pc)
ps = input("Please enter the turtles pen size: ")
bob.pensize(ps)

def rect (t,W,H):
    '''turtle t draws rectangle of width W and of hight H.'''
    trn = 90
    for i in range(2):
        bob.fd(50)
        bob.lt(trn)
        bob.fd(100)
        bob.lt(trn)

rect(bob, 100, 50)