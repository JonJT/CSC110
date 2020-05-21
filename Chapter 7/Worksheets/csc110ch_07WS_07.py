# ws ch7_7
# Rewrite num_digits(n) by converting
# n to a string & using the len BIF.

def num_digits(n):
    '''return the number of digits of int n > 0.'''
    # nStr = str(n)
    # num_digits = len(nStr)
    # return num_digits
    return len(str(n))

# print(num_digits(105))

from random import randint

for i in range(20):
    n = randint(10, 10000)
    print(n, 'has', num_digits(n), 'digits')