# ***********************************************
# WS ch4_4
# Write a function, factorial(n), which returns n! .  n is an int >=0.
# ***********************************************

def factorial(n):
    '''return n!, for n >= 0'''
    prodAcum = 1
    for i in range(1, n + 1):
        prodAcum *= i
    return prodAcum

for n in range(6):
    print(n,factorial(n))