# ws ch6 - 0
#  Write a function, circle_area(Radius),which
# returns the area of a circle of radius Radius.
# Then use the function to print out a table of
# radii and corresponding circle areas for the
# radii 1,3,7,10.  Round the circle areas to 3
# decimal points.

from math import pi

def circle_area(Radius):
    r = pi * Radius**2
    return r

print('Radius       Area')
print('------------------')

R = [1, 3, 7, 10]

for i in R:
    print(i,'           ', round(circle_area(i), 3))