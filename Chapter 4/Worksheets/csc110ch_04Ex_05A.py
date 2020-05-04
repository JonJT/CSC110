# *************************************************
# WS ch 4_5A
# Write a function, f2c(fahr), that takes degrees in Fahrenheit & returns Celsius degrees.
# Write a function, f2k(fahr), that takes Fahrenheit degrees & returns Kelvin degrees.  Use f2c(fahr) as a helper function.
# 32F ~ 0C, 212F ~ 100C
# deg K = deg C + 273.15
# ************************************************

def f2c(fahr):
    '''return temperature in Celsius given temp in fahrenheit.'''
    C = (fahr - 32) * 5 / 9
    return C

# know that:        Freezing Pt         Boiling Pt
#           F           32                  212
#           C            0                  100

for fahr in [32, 212]:
    c = f2c(fahr)
    print(fahr,'Fahrenheit is', c, 'Celsius')
print()

def c2k(celsius):
    '''return temperature in Kelvin given temp in Celsius'''
    k = celsius + 273.15
    return k

def f2k(fahr):
    '''returns temp in Kelvin given temp in fahrenheit'''
    c = f2c(fahr)
    k = c2k(c)
    return k

print('Fahrenheit    Celsius    Kelvin')
print('--------------------------------')
spaces = '   '
moreSpaces = '      '
for fahr in (32, 212):
    c = round(f2c(fahr), 2)
    k = round(f2k(fahr), 2)
    print(spaces, fahr, moreSpaces, c, moreSpaces, k)
