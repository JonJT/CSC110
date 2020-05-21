# ws ch6_8
# Write a function, listOfFactorsOf(n),
# which returns a list of the factors of int n,
# n >= 2 and where the factors are larger than
# or equal to 2 and smaller than n.
# Uses isFactor(f,n) as a helper function.
# Use your function to print a table
# of ints from 11 to 20 with their factors

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