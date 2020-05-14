# ws ch6_9
# Write a function, isPrime(n),
# which returns True if n is prime,
# OTW it returns False.
# Use your function to print out all primes <= 1000, 15 primes per line.
# Use listOfFactorsOf(n) and isFactor(f,n) as helper functions



# Write a function, tableOfPrimes(From,To,num_per_line),
# Which prints out the prime numbers from From to To,
# With num_per_line primes per line.

def isFactor(f, n):
    tv = (n % f == 0)
    return tv


def listOfFactorsOf(n):
    A = []
    for f in range(2, n):
        if isFactor(f, n):
            A.append(f)
    return A


factors = listOfFactorsOf(60)
print('The proper factors of 60 are:', factors)
print()

print(' n        proper factors')
print('------------------------')
for n in range(11, 21):
    print(n, listOfFactorsOf(n))


def isPrime(n):
    if n == 1:
        return False
    numberOfFactors = len(listOfFactorsOf(n))
    return numberOfFactors == 0


# counter = 0
# for n in range(1, 1001):
#     if isPrime(n):
#         counter += 1
#         print(n, end = ' ')
#         if counter % 15 == 0:
#             print()

def tableOfPrimes(From, To, num_per_line):
    counter = 0
    for n in range(From, To + 1):
        if isPrime(n):
            counter += 1
            print(n, end = ' ')
            if counter % num_per_line == 0:
                print()


tableOfPrimes(1000, 5000, 15)