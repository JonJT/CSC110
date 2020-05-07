# WS ch5_4
# Find all ints from 2 to 250 that are (divisible by 7) but (not (divisible by 3
# or by 5))

# for n in range (2, 251):
#     d7 = (n % 7 == 0)               # div by 7
#     d3 = (n % 3 == 0)               # div by 3
#     d5 = (n % 5 == 0)               # div by 5
#     b = (d7 and not (d3 or d5))     # whole boolean
#     if (b):
#         print(n, end = ' ')


counter = 0                         # init counter
for n in range (2, 251):
    d7 = (n % 7 == 0)               # div by 7
    d3 = (n % 3 == 0)               # div by 3
    d5 = (n % 5 == 0)               # div by 5
    b = (d7 and not (d3 or d5))     # whole boolean
    if (b):
        print(n, end = ' ')
        counter += 1

# print()
print('There are', counter, 'qualifying ints')