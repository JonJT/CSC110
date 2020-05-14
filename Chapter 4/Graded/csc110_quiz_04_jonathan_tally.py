## overall grade = (19 + 19 + 12)/55 = 50/55
## Q1 and Q2  - functions not written to spec to return  sum of squares
## Q3  Sum_B not right because of range in for loop.  No explanation for cube root of cube

# CSC 110 Spring 2020  Quiz 4 Take-home                       NAME: Jonathan Tally
# YouTube Link: https://youtu.be/ldwJVTkuGZA
# Write clear, legible code, the simpler the better. Make sure your code works.   Due Monday at class start.
# Use the editor to write your code. Submit a file, Quiz_4_YourFullName.py in an email that has as subject 
# csc 110 quiz 4_YourFullName.
# Points will be deducted if submission is late.


# 1.  (20 pts) Write a function SumOfSqrOfInts_A(From,To), which returns the sum of the squares of the ints
# from From to To, inclusive, that are (divisible by 7  or divisible by 3) and divisible by 2.
# Explain how you checked that your function is working properly by doing a hand selection of
# qualifying ints  from 20 to 40, inclusive, then adding together the square of the qualifying
# ints directly using Python.  Print out the "Checked Sum"  and the "Sum from Function" -
# they should be the same.  Outputs should be of the following form – make sure to include the labels.
# The underscores are the appropriate numbers. Sum_A =   SumOfSqrOfInts_A(From,To)

# Q1 check:
# My explanation of how I selected the qualifying ints from 20 to 40:

# [I used a piece of paper to do the math to find out what numbers are 
# divisible by 7 or 3 or 2. Then I cross referenced the numbers until I 
# found only those that are divisible by 7 or 3, and 2]

# Therefore, the qualifying ints are: 24, 28, 30, 36
# Checked Sum is: checkSum = ((24**2) + (28**2) + (30**2) + (36**2))
# Sum_A is: 3556


def SumOfSqrOfInts_A(x, y):
    list = []
    for n in range(x, y):
        d7 = (n % 7 == 0)           # div by 7
        d3 = (n % 3 == 0)           # div by 3
        d2 = (n % 2 == 0)           # div by 2
        b = ((d7 or d3) and d2)
        if (b):
            list.append(n)
    return list

listA = SumOfSqrOfInts_A(20, 41)

print(listA)

# output [24, 28, 30, 36]

# checkSum = ((24**2) + (28**2) + (30**2) + (36**2))

# print(checkSum)

# output 3556

SumA = 0   
for x in listA:
    SumA += x**2

print('Sum of list A is', SumA)

# output 3556


# 2.  [20 pts] Write a function SumOfSqrOfInts_B(From,To), which returns the sum of the squares of the
# ints from From to To, inclusive, that are (divisible by 3  and divisible by 7) or (divisible by 2).
# Explain how you checked that your function is working properly by doing a hand selection of
# qualifying ints  from 20 to 40, inclusive, then  adding together the square of the qualifying
# ints directly using Python.  Print out the "Checked Sum"  and the "Sum from Function" -
# they should be the same.  Outputs should be of the following form – make sure to include the labels.
# The underscores are the appropriate numbers. Sum_B =   SumOfSqrOfInts_B(From,To)

# Q2 check:
# My explanation of how I selected the qualifying ints from 20 to 40:

# [I wrote out all the numbers div by 7 or 3 or 2. Once I had those I found the numbers div by 7 and 3. Then all the numbers div by 2]

# Therefore, the qualifying ints are: 20, 21, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40
# Checked Sum is: checkSum2 = ((20**2) + (21**2) + (22**2) + (24**2) + (26**2) + (28**2) + (30**2) + (32**2) + (34**2) + (36**2) + (38**2) + (40**2))
# Sum_B is: 10781

def SumOfSqrOfInts_B(x, y):
    list = []
    for n in range(x, y):
        d7 = (n % 7 == 0)           # div by 7
        d3 = (n % 3 == 0)           # div by 3
        d2 = (n % 2 == 0)           # div by 2
        b = ((d7 and d3) or d2)
        if (b):
            list.append(n)
    return list

# print(SumOfSqrOfInts_B(20, 41))

# output [20, 21, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# checkSum2 = ((20**2) + (21**2) + (22**2) + (24**2) + (26**2) + (28**2) + (30**2) + (32**2) + (34**2) + (36**2) + (38**2) + (40**2))

# print(checkSum2)

# output 10781

SumB = 0   
for x in SumOfSqrOfInts_B(20, 41):
    SumB += x**2

print('Sum of list B is', SumB)

# output 10781

# 3. [15 pts] If From = 1235, To = 7124, take
# Sum_A  = SumOfSqrOfInts_A(From,To)
# Sum_B  = SumOfSqrOfInts_B(From,To)
# Find Sum_A/ Sum_B, then print out the answer out to five decimal places.
# Find the cube root of the cube of Sum_A, then print the result out without rounding. Explain the result. Copy the output from the shell,
# put it below your code and comment it out.  Output should
# be of the following form.  The underscore are the appropriate numbers.  

# Q3:
# Sum_A is 25687265020
# Sum_B is 62793967725
# The ratio of Sum_A to Sum_B for From,To = 1235, 7124, to five decimals, is  0.40907
# The cube root of the cube of Sum_A is 2950.570224731659
# My explanation for the last result:
  
# [Cube root is x^1/3 so in python x**(1/3) is the cube root of x]

Sum_A = 0   
for x in SumOfSqrOfInts_A(1235, 7124):
    Sum_A += x**2

print('Sum of list A is', Sum_A)

# output 25687265020

Sum_B = 0   
for x in SumOfSqrOfInts_B(1235, 7124):
    Sum_B += x**2

print('Sum of list B is', Sum_B)

# output 62793967725

aDivB = round((Sum_A / Sum_B), 5)

print(aDivB)

# output 0.40907

cubeSum_A = Sum_A ** (1/3)

print(cubeSum_A)

# output 2950.570224731659


# To Submit:
# Your quiz .py file, csc110_Quiz_4_YourFullName.py in an email that has as subject csc110_Quiz_4_YourFullName.
# 2.  In your file, put a youtube link of a video showing and discussing Q1, paying particular attention to how you did
# a hand selection of qualifying ints  from 20 to 40, inclusive . Use https://screencast-o-matic.com/ to download a video creation application.
# I need to see Python code on the screen and to hear your voice as you explain.  Be sure to announce yourself at the beginning of the video.  
