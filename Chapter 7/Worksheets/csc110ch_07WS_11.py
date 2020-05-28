# Ws ch 7_11
# Use a while loop to find how many terms of this series are needed to approximate pi to within 0.001.

import math

def sum_Leibnitz(n):
    sum_acum = 0
    for i in range(n):
        odd = 2*i + 1
        Sign = (-1) ** i
        sum_acum += Sign  *1 / odd
    return sum_acum

def approx_pi_w_Leibnitz():
    n = 1
    while True:
        Sum = sum_Leibnitz(n)
        if abs(4 * Sum - math.pi) <= 0.001:
            break
        n += 1
    return 4 * Sum, n

Pi = math.pi
piApprox, numTerms = approx_pi_w_Leibnitz()
print("pi is", Pi)
print("An approximations of pi to within 0.001 is", piApprox)
print("abs (piApprox - pi is", abs(piApprox - Pi))
print("The number of terms needed is", numTerms)

