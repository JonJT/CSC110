# def printOutSqrd(n):
#     print(n**2)

# for i in range(1, 4):
#     printOutSqrd(i)

# WS ch4_2
# try with a helper function
import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("white")
t.pensize(4)

def draw_rect(t, w, h):
    '''turble t draws a rect of width w & height h.'''
    t.pu(); t.bk(w / 2); t.lt(90); t.bk(h / 2); t.rt(90); t.pd()
    for i in range(2):
        t.fd(w); t.lt(90)
        t.fd(h); t.lt(90)
    t.pu(); t.fd(w / 2); t.lt(90); t.fd(h /2); t.rt(90); t.pd()

def draw_rects(t, w1, h1, w2, h2):
    draw_rect(t, w1, h1)
    draw_rect(t, w2, h2)

draw_rects(t, 200, 50, 25, 400)

# end of WS