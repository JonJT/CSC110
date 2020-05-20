# Ws ch 7-2A

# Use a while loop to sum the squares of the natural numbers,  starting with 1, 
# until the sum  first exceeds 1000. What is the largest sum < 1000 and what is the corresponding natural number n such that
# 1^2 + 2^2 + … + n^2 < 1000?

sum_acum = 0
n = 0
while sum_acum + (n + 1) ** 2 <= 1000:
    n += 1 # update, n, OTW inf loop
    sum_acum += n ** 2
print(n, sum_acum)
print()

def sumOfSqrs(n):
    '''Returns sum of squares of the first n natural numbers.'''
    sumAcum = 0
    for i in range(1, n + 1):
        sumAcum += i ** 2
    return sumAcum

print(sumOfSqrs(13))
print(sumOfSqrs(14))