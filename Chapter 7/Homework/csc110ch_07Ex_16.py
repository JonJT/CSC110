# Write a function sum_of_squares(xs) that computes the sum of the squares of the
# numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return
# 4+9+16 which is 29:
# test(sum_of_squares([2, 3, 4]) == 29)
# test(sum_of_squares([ ]) == 0)
# test(sum_of_squares([2, -3, 4]) == 29)


def sum_of_squares(xs):
    sum_of_squares = 0 
    for i in (xs):
        squared = i * i
        sum_of_squares += squared
    return sum_of_squares

print(sum_of_squares([2, 3, 4]) == 29)
print(sum_of_squares([ ]) == 0)
print (sum_of_squares([2, -3, 4]) == 29)