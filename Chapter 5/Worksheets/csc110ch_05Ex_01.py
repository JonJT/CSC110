# WS ch5_1
# For ints from 1 to 20, which ints n are (n % 2 == 0)   and (n % 3 == 0) ?

# For ints from 1 to 20, which ints n are (n % 2 == 0)   or (n % 3 == 0) ?

# What ints from 1 to 20 satisfy neither condition?


for n in range(1, 21):
    if (n % 2 == 0) and (n % 3 == 0):
        print(n)

for n in range(1, 21):
    if (n % 2 == 0) or (n % 3 == 0):
        print(n)

