# **********************************************
# WS ch4_8

# Write a function, trngl_perim(x1,y1,x2,y2,x3,y3), which takes the coordinates of the 3 vertices of a triangle as 
# parameters and which returns the perimeter of the triangle. Write a helper function, distance(x1,y1,x2,y2), which 
# returns the distance between 2 points, which will be in the definition of trngl_perim(x1,y1,x2,y2,x3,y3).  
# Check that both functions are working correctly.

# Find the perimeter of the triangle whose vertices are
# (1,2),(3,4),(5,6).
# ***********************************************

from math import sqrt

def distance(x1,y1,x2,y2):
    '''return the distance between x1,y1 and x2,y2 using the pythagorean theorem'''
    h = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return h

def trngl_perim(x1,y1,x2,y2,x3,y3):
    '''which takes the coordinates of the 3 vertices of a triangle as parameters and 
    which returns the perimeter of the triangle use distance(x1,y1,x2,y2) as a helper function.'''
    a = distance(x1, y1, x2, y2)
    b = distance(x1, y1, x3, y3)
    c = distance(x3, y3, x2, y2)
    perim = a + b + c
    return perim

x1, y1 = 0, 0
x2, y2 = 4, 3

print(distance(x1, y1, x2, y2))

x3, y3 = 4, 0

print(trngl_perim(x1,y1,x2,y2,x3,y3))