# Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk
# pirate makes a turn, and then takes some steps forward, and repeats this. Our social
# science student now records pairs of data: the angle of each turn, and the number of
# steps taken after the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43,
# 12)]. Use a turtle to draw the path taken by our drunk friend.

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")

list = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
# list = [(160, 200), (-43, 100), (270, 80), (-43, 120)]

def drkPrt():
    for angle, movement in list:
        t.lt(angle)
        t.fd(movement)

drkPrt()

wn.mainloop()