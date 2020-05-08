# WS Ch 5_8A
# Write a function:
# def ruler(t,N):
#         '''Draw a ruler with N ticks, making every 10th (including the 0th line) 
#         line longest, every 5th line next longest and every other line shortest.'''

import turtle
wn = turtle.Screen()
t = turtle.Turtle

def ruler(t, n):
    long, medium, short = 15, 10 ,5
    for tick_num in range(n + 1):
        if tick_num % 10 == 0:
            make_tick(t, long)
            if tick_num < n:
                t.fd(5)
        elif tick_num % 5 == 0:
            make_tick(t, medium)
            t.fd(5)
        else:
            make_tick(t, short)
            t.fd(5)

def make_tick(t, tick_length):
    t.lt(90)
    t.fd(tick_length)
    t.bk(tick_length)
    t.rt(90)

ruler (t, 50)

def ruler_square(t, n):
    for i in range(4):
        ruler(t, n)
        t.lt(90)

ruler_square(t, 70)

wn.mainloop()