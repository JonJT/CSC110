# WS ch5_3.py
# Write a function, tell_if_NZP(num), which prints out an appropriate message
# telling if num is negative, zero or positive.  Assume that num is an int.
# Test the function on ints from -2 to 2.

# def tell_if_NZP(num):
#     if ( num > 0):
#         print(num, 'is positive.')
#     elif (num < 0):
#         print(num, 'is negative.')
#     else:
#         print(num, 'is zero')

# for num in range(-2, 3):
#     tell_if_NZP(num)

def tellAboutTemp(temp):
    if (temp <= 0):
        print(temp, 'cold.')
    elif (temp <= 10):
        print(temp, 'cool.')
    elif (temp <= 25):
        print(temp, 'medium.')
    elif (temp <= 35):
        print(temp, 'warmer.')
    else:
        print(temp, 'is not cataloged.')

for temp in [-10, 5 , 15, 30, 50]:
    tellAboutTemp(temp)
