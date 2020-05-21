# A counter is variable used to count the number of events.
# It is similar to a sum accumulator - both are initialized
# to zero. In contrast to a sum accumulator, a counter is
# increased by 1 whenever the event occurs.  Occurrence of
# the event is typically checked with a conditional.

# Ws ch7-0

# Write code to find the number of ints from 1 to 500,
# inclusive, that are divisible by 7 but not divisible
# by 5.  Write a boolean function as a helper function.

# counter = 0
# for n in range(1, 501):
#     d7 = n % 7 == 0
#     d5 = n % 5 == 0
#     B = d7 and not d5
#     if (B):
#         counter += 1

# print(counter)

################################

counter = 0
def d7andnotd5(n):
    d7 = n % 7 == 0
    d5 = n % 5 == 0
    B = d7 and not d5
    return B

for n in range(1, 501):
    if (d7andnotd5(n)):
        counter += 1

print(counter)

#########################

# L = []
# for n in range(1, 501):
#     if (d7andnotd5(n)):
#         L.append(n)