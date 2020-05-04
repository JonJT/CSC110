# *************************************************
# WS ch 4_5
# Use factorial(n) to print out a table of n! for 1 <= n <= 10.
# ************************************************

print(' n       n!')
print('------------')

def factorial(n):
    '''return n!, for n >= 0'''
    prodAcum = 1
    for i in range(1, n + 1):
        prodAcum *= i
    return prodAcum

for n in range(1, 11):
    print(n, '      ', factorial(n))