# WS ch6 -2

# The area of a triangle can be found from the formula
# A = sqrt(s*(s-a)*(s-b)*(s-c)),
# Where
#  a,b,c are the length of the 3 sides of the triangle, and
# s = (perimeter)/2
# Write a function, triangle_area(x1,y1,x2,y2,x3,y3),
# Which returns the area of a triangle whose vertices have the coordinates (x1,y1),(x2,y2),(x3,y3).  Use appropriate helper functions. Check the correctness
# Of your code.

from math import sqrt

def distance(x1, y1, x2, y2):
    del_x = (x2 - x1)
    del_y = (y2 - y1)
    D = sqrt(del_x**2 + del_y**2)


def Heron(a, b, c):
    s = (a + b + c) / 2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    return A


def triangle_area(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x3, y3, x2, y2)
    c = distance(x1, y1, x3, y3)
    A = Heron(a, b, c)
    return A

print('Expected area is', 0.5*(3*4))
x1, y1, x2, y2, x3, y3 = 0, 0, 3, 0, 3, 4
A = triangle_area(x1, y1, x2, y2, x3, y3)
print('Area from function is', A)