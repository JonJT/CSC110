# ws ch6_7
# Write a boolean function, isFactor(f,n), which returns True
# if f is a factor of n, where 1 < f < n, OTW it returns False.
# Use this function to print out all factors of 60 which are
# greater than 1 and smaller than n.

def isFactor(f, n):
    tv = (n % f == 0)
    return tv

# test all proper factors of 60

for f in range(2, 60):
    if isFactor(f, 60):
        print(f, end = ' ')