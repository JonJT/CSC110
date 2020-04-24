# ************************************************
# WS ch 3_6
# Initialize a product accumulator to 1, then use a for loop & a range statement to multiply the ints from 1 to 5.
# ************************************************

# def prod_a_b (a, b):
#     '''Print sum of a through b'''
#     p = 1
#     for i in range (a, b + 1):
#         p *= i
#     print(p)

# prod_a_b(1, 5)

s = 1

for i in range (1, 5 + 1):
    s *= i
    
print(s)