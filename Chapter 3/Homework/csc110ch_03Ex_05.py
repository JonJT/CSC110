# Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99,
# 20]
# (a) Write a loop that prints each of the numbers on a new line.
# (b) Write a loop that prints each number and its square on a new line.
# (c) Write a loop that adds all the numbers from the list into a variable called total. You
# should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.
# (d) Print the product of all the numbers in the list. (product means all multiplied together)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

### start of question (a)

for i in xs:
    '''print each number in xs list on it's own line'''
    nl = i
    print(nl)

### end of question (a)

### start of question (b)

for i in xs:
    '''square and print each number in xs list on it's own line'''
    sq = i**2
    print(sq)

### end of question (b)

### start of question (c)

# total = 0

total = 0

for i in xs:
    '''add all numbers from xs up and print the total'''
    total += i
    
print(total)

### end of question (c)

### start of question (d)

pd = 1

for i in xs:
    '''product of all numbers in list, print total'''
    pd *= i

print(pd)

### end of question (d)