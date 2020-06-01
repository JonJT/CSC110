# ws ch7_2
# Write a function, sum_of_odds_1(a,b),
# which returns the sum positive odd ints starting with
# the ath odd int & ending with the bth odd int.
# Use odd(n) as a helper function.
# Is there more than one way to do this?

def seq3np1(n):
    '''print the 3n+1 sequence from n,
    terminating when it reaches 1.'''
    while n != 1:
        print(n, end = ' ')
        if n % 2 == 0: # n is even
            n = n // 2
        else: # n is odd
            n = n * 3 + 1
    print(n, end = '.\n')

def seq3np1_list(n):
    '''return a list of the 3n + 1 sequence from n,
    terminating when it reaches 1.'''
    c = [n] # list accum, starts with n in the list
    while n != 1:
        # c.append(n)
        if n % 2 == 0: # n is even
            n = n // 2
            c.append(n)
        else: # n is odd
            n = n * 3 + 1
            c.append(n)
    return c

for n in range(1, 21):
    l = seq3np1_list(n)
    lng = len(l)
    print(l, lng)
