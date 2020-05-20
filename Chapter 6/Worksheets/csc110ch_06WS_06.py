# ##ws ch6_6
# ##The following function has semantic errors.
# ## Find & fix the errors


# def func(n):
#     '''Returns n + 2 unless n is 3 or 4,
#     in which case it returns n - 2. n is an int.
# '''
#     if n == 3 or  4:  ## 4 is nonzero and is True
#         return n - 2
#     else:
#         return n + 2


def func(n):
    '''Returns n + 2 unless n is 3 or 4,
    in which case it returns n - 2. n is an int.
'''
    if n == 3  or  n == 4:  ## 4 is nonzero and is True
        return n - 2
    else:
        return n + 2

print(1, func(1), 'should be 3')
print(5, func(5), 'should be 7')
print(3, func(3), 'should be 1')
print(4, func(4), 'should be 2')