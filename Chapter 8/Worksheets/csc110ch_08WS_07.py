# Ws ch8_7
# Redo the 15 primes per line table for primes <= 1000 using the string format method. See ws ch6_9.  Is there a nice number of primes
# per line table that fills all the lines?  [15 per line does not fill all lines]

def isPrime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

def tableOfPrimes(From, To, numPerLine):
    primes = []
    for n in range(From, To + 1):
        if isPrime(n):
            primes.append(n)
    
    print('Primes <= 1000')
    print('--------------')
    primeCounter = 0
    for prime in primes:
        layout = '{0:>3}'
        print(layout.format(prime), end = ' ')
        primeCounter += 1
        if primeCounter % numPerLine == 0:
            print()

print()
print(tableOfPrimes(0, 1000, 15))