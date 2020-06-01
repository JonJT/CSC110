# ws ch7_2
# Write a function, sum_of_odds_1(a,b),
# which returns the sum positive odd ints starting with
# the ath odd int & ending with the bth odd int.
# Use odd(n) as a helper function.
# Is there more than one way to do this?


def sum_of_odds_1(a, b):
    sumAcum = 0
    for n in range(a, b+1):
        sumAcum += odd(n)
    return sumAcum

def odd(n):
    V = 2*n -1
    return V

# 3 + 5 + 7+ 9 + 11 + 13 = 48
print(sum_of_odds_1(2, 7) == 48)