# Write a function slope(x1, y1, x2, y2) that returns the slope of the line through
# the points (x1, y1) and (x2, y2). Be sure your implementation of slope can pass the
# following tests:
# test(slope(5, 3, 4, 2) == 1.0)
# test(slope(1, 2, 3, 2) == 0.0)
# test(slope(1, 2, 3, 3) == 0.5)
# test(slope(2, 4, 1, 2) == 2.0)
# Then use a call to slope in a new function named intercept(x1, y1, x2, y2)
# that returns the y-intercept of the line through the points (x1, y1) and (x2, y2)
# test(intercept(1, 6, 3, 12) == 3.0)
# test(intercept(6, 1, 1, 6) == 7.0)
# test(intercept(4, 6, 12, 8) == 5.0)

def slope(x1, y1, x2, y2): 
    return (float)(y2-y1) / (x2-x1)


# print(slope(5, 3, 4, 2) == 1.0)
# print(slope(1, 2, 3, 2) == 0.0)
# print(slope(1, 2, 3, 3) == 0.5)
# print(slope(2, 4, 1, 2) == 2.0)

def intercept(x1, y1, x2, y2):
    y = y2-(slope(x1, y1, x2, y2)*x2)
    return y


print(intercept(1, 6, 3, 12) == 3.0)
print(intercept(6, 1, 1, 6) == 7.0)
print(intercept(4, 6, 12, 8) == 5.0)