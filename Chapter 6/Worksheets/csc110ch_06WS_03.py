# WS ch6 – 3
# Write a function, quadratic(a,b,c), which returns the solutions for a quadratic equation,
# ax^2 + bx + c = 0.  Use conditionals as appropriate. Use your function to print out the  solutions for several different  quadratic equations:
# a,b,c = 1,-1,-2
# a,b,c = 1,10,25
# a,b,c = 1,-2.5,-6.25
# a,b,c = 6,1,12

import math

def quadratic(a, b, c):
    roots = []
    D = b**2 - 4*a*c
    if (D > 0):
        root1 = (-b - math.sqrt(D)) / (2*a)
        root2 = (-b + math.sqrt(D)) / (2*a)
        roots.append(root1)
        roots.append(root2)
    elif (D == 0):
        root = -b / (2*a)
        roots.append(root)
    else:
        pass
    return roots

examples = [(1,-1,-2), (1,10,25), (1,-2.5,-6.25), (6,1,12)]
for abc in examples:
    a, b, c = abc
    print(a, b, c, quadratic(a, b, c))