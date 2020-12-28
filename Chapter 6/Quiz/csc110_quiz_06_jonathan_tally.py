# CSC 110 Spring 2020  Quiz 6 Take-home                       NAME: Jonathan Tally
# YouTube: https://youtu.be/_En-MDj3mdg
# Write clear, legible code, the simpler the better. Make sure your code works.   
# Due next Monday before midnight.  Use the editor to write your code. Submit a file, 
# Quiz_6_YourFullName.py in an email that has as subject  csc 110 quiz 6_YourFullName.   
# Points will be deducted if submission is late.   


# 1. [10 pts] Write a function, roll2Dice(), that returns a list of 2 rolls of a fair, six-sided dice.
# Uses a list accumulator.  Uses the random module.

from random import randint

def roll2Dice():
    l = []
    for r in range(2):
        roll = randint(1, 6)
        l.append(roll)
    return l

print(roll2Dice())



# 2. [20 pts] Write a function, roll2DiceUntilSumIsPrime(), which rolls 2 dice until the
# sum of the 2 dice is prime.  Uses a while loop and the function from Q1 as a helper function.
# Returns  a list of the sums of the dice pairs rolled.  Uses a list accumulator. Two dice are 
# rolled until the sum of the dice is a prime number.  You can use isPrime(n) as a helper function, 
# but there is an alternate way to do this using in  or not in
# Hints: You can write a boolean,
# x in List
# which is True if x is in List, otherwise it is False.  For example

# >>> L,x,y = [6,4,11,2],2,7
# >>> x in L
# True
# >>> y in L
# False
# >>> y not in L
# True
# If 2 dice are rolled, what are the possible sums of the 2 dice?  And of these sums, which of them are prime?


def roll2DiceUntilSumIsPrime():
    sumPrime = [2, 3, 5, 7, 11]
    rolledDice = []
    roll = sum(roll2Dice())
    while roll not in sumPrime:
        rolledDice.append(roll)
        roll = sum(roll2Dice())
    rolledDice.append(roll)
    print(rolledDice)

roll2DiceUntilSumIsPrime()



# 3. [[10 pts]  Write a function, quadratic(a,b,c,x), which returns the value of
# a*x**2 + b*x + c.

def quadratic(a, b, c, x):
    return a*x**2 + b*x + c

# print(quadratic(2, -1, -15, -3))



# 4. [20 pts] Use a while loop and a range statement to print out a table of quadratic(2,-1,-15,x), 
# for -3 <= x <= 4 and for x in steps of 0.25. Print all values using 2 decimals.  Uses the function from Q3.
# Hint:  set x to -3.0 before the while loop.  In the while loop, update the value of x using 0.25. Write an appropriate Boolean after the while.


# x = -3
# while (-3 <= x <= 4):
#     for i in range (1):
#         print(x,'   ', round(quadratic(2,-1,-15,x), 2))
#         x += 0.25



# 5. [XC 3 pts] Write a function numTimesThruLoop(x1,x2,del_x), which returns the number
# of times a for loop needs to execute for x1 <= x <= x2, with a step size for x
# of del_x.  For example, if x1,x2,del_x = 0,2,0.25, the function should return 9, since
# the values of x in a table would have 9 rows:
#     x
# ----------
#     0.00
#     .25
#     .50
#     .75
#     1.00
#     1.25
#     1.50
#     1.75
#     2.00

def numTimesThruLoop(x1 ,x2, del_x):
    l = []
    x = x1
    while (x1 <= x <= x2):
        for i in range(1):
            l.append(x)
            x += del_x
    return len(l)


# print(numTimesThruLoop(0, 2, 0.25))




# 6. [XC 3 pts] Same as Q4, but use a for loop and a range statement instead of a while loop.
# Uses the functions from Q3 and Q5.  
# Hints: Remember, range takes only ints as  parameters, so be careful.
# If you know how many times,  n_loop, to go through the loop, then you can generate all
# the required x values from the code:
# for i in range(n_loop):
#     x = x1 + i * del_x

# x1, x2, del_x = 0, 2, 0.25

# n_loop = numTimesThruLoop(x1, x2, del_x)

# for i in range(n_loop):
#     x = x1 + i * del_x
#     return x

### This was as far as I got.




# To Submit:
# 1. Your quiz .py file, csc110_Quiz_6_YourFullName.py in an email that has as subject csc110_Quiz_6_YourFullName.
# 2.  In your file, put a youtube link of a video showing and discussing Q2. Use https://screencast-o-matic.com/ 
# to download a video creation application.   I need to see Python code on the screen and to hear your voice as you explain.  
# Be sure to announce yourself at the beginning of the video.