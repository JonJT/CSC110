# WS ch5_7
# Example of a function that returns 2 items:

# def sum_diff(x,y):
#     '''Returns sum and difference of x and y.'''
#     Sum = x + y
#     Diff = x - y
#     return Sum, Diff

# ##How to use it:

# S,D = sum_diff(5,3)

# print(S,D)

# Write a function, sumSqrs_diffSqrs(x,y), which returns x^2 + y^2  and
# x^2 - y^2.  Use sumSqrs_diffSqrs(x,y) to compute 4^2 + 2^2 and 4^2 - 2^2.


def sumSqrs_diffSqrs(x, y):
    sumSqrs = ((x**2) + (y**2))
    difSqrs = ((x**2) - (y**2))
    return sumSqrs, difSqrs

s, d = sumSqrs_diffSqrs(4, 2)

print(s, d)