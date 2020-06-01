# ws ch7_1_
# Write a function, sum_of_odds(n), which returns
# the sum of the 1st n  positive odd ints.
# Is there more than 1 way to do this? Are there any useful helper functions?

def sum_of_odds(n):
    sum_accum = 0
    for i in range(1, n+1):
        sum_accum += odd(i)
    return sum_accum

def odd(n):
    V = 2*n - 1
    return V

print(sum_of_odds(5) == 25)