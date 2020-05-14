# ws ch6_4
# Write a boolean function, isEven(n), which
# returns True if n is even and False if n
# is odd.  n is an int.



# Write a function, isOdd(n), which returns
# True if n is odd and False if n is even.
# n is an int.  Use isEven(n) as a helper
# function.

def isEven(n):
    tv = (n % 2 == 0)
    return tv

for n in [1, 2, 4, 5, 7]:
    if isEven(n):
        print(n, end = ' ')

def isOdd(n):
    tv = not isEven(n)
    return tv

for n in [1, 3, 5, 6, 8, 9]:
    if not isOdd(n):
        print(n, end = ' ')