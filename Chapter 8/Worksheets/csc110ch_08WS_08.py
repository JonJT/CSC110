# Ws ch8_8
# Print out a table for the escape velocity from the earth,  where M = 5.97 x 1024 kg is the mass of the earth,
# for r varying from 6.5 x 106 m to 15x106 m in increments of 0.5 x 106 m .  Use the formula below and print
# formatting with 3 significant figures for r and 3 significant figures for the escape velocity. Re = 6.37 x 106 m is the radius of the earth.

from math import sqrt

def vEscape(r):
    G = 6.67E-11
    M = 5.97E24
    return sqrt(2*G*M/r)

layout = '{0:10}    {1:10}'
print(layout.format('Radius(m)', 'Esc Vel m/s'))

delta = 0.5E6
r = 6.5E6
endingRadius = 15E6
layout1 = '{0:10.3e}    {1:10.3e}'
while r <= endingRadius:
    print(layout1.format(r,vEscape(r)))
    r += delta
print()