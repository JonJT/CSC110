# *********************************************
# Ws ch3_5
# Initialize a sum accumulator to 0, then use a for loop 
# & a range statement to add the ints from 1 to 10.
# ********************************************


s = 0

for i in range (1, 11):
    s += i
    
print(s)

# def sum_a_to_b (a, b):
#     '''Print sum of a through b'''
#     s = 0
#     for i in range (a, b + 1):
#         s += i
#     print(s)

# sum_a_to_b(1, 10)