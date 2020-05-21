# Ws ch7_6A
# Define a function f(x) that returns x**2 + 1.  Then write a loop to print out 
# a table of values of the function from 1 to 5 inclusive in step of 0.5.  Do this first 
# with a while loop, then with a for loop.

def f(x):
    '''return x**2 + 1.'''
    return x**2 + 1

x = 1
while x <= 5:
    print(x, f(x))
    x += 0.5

n = 9
for i in range(n):
    x = 1 + i * 0.5
    print(x, f(x))