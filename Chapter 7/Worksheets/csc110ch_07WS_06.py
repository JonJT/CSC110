# Ws ch7_6
# For what n<= 1000 is the collatz sequence the longest?  What is the sum of that sequence?  
# What is the corresponding n for this sequence? Use the function from the previous ws as a 
# helper function.  You might want some other helper functions.  This problem is somewhat easier 
# with indices or dictionaries.

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
        if n % 2 == 0: # n is even
            n = n // 2
            c.append(n)
        else: # n is odd
            n = n * 3 + 1
            c.append(n)
    return c


# for n in range(1, 1001):
#     l = seq3np1_list(n)
#     lng = len(l)
#     print(n, lng)

def longestCS(x, y):
    '''return the n's, x <= n <= y, that has the longest cs, the max length,
    the corresponding sums of these max length CS.'''
    lnOfCS = []
    for n in range(x, y + 1):
        lnOfCS.append(len(seq3np1_list(n)))
    lnMax = max(lnOfCS)
    # find the n's correspond to this max length
    seqWithMaxLen = []
    for n in range(x, y + 1):
        if len(seq3np1_list(n)) == lnMax:
            seqWithMaxLen.append(n)
    # find the sum of the cs with max length
    sumOfCSWithMaxLen = []
    for n in seqWithMaxLen:
        sumOfCSWithMaxLen.append(sum(seq3np1_list(n)))
    return seqWithMaxLen, lnMax, sumOfCSWithMaxLen

print('Output for 1 to 20:')
print(longestCS(1,20))
print()
print('Output for 1 to 1000')
print(longestCS(1, 1000))
print()