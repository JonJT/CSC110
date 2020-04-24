# CSC 110 Spring 2020  Quiz 2 Take-home                       NAME: Jonathan Tally
# youTube Link: 
# Write clear, legible code, the simpler the better. Make sure your code works. 
# Due Monday at class start.  Use the editor to write your code.  Also, submit a file, Quiz_2_YourFullName.py 
# in an email that has as subject csc 110 quiz_YourFullName. 
# Points will be deducted if submission is late or if answers are not shown in code & commented out.


# 1. (20 pts) Use a sum accumulator, a for loop and a range statement to find the sum of the even ints
# from 110 to 518, inclusive.  Use a print statement to print out a labelled answer:
#     "The sum of even ints from 110 to 518, inclusive, is  64370 ."
# Do not use formulas to add up the ints,  just add them up please. Copy the answer from the shell into your file, 
# comment the answer out.  Make sure your code works.

s = 0
for i in range(110, 518 + 2, 2):
    s += i

print(s)

# Answer = 64370

# 2.  (20 pts) Write python code to solicit three numbers from the user and to print out the
# sum of the cubes of the 3 numbers.  For full credit, use a sum accumulator and a for loop.  Check your code and make sure it works. 
# Now have the user type in the 3 numbers
# 1950.1, 1975.2, 2000.3 when prompted and then print out the sum of the cubes of
# these number. Copy the answer from the shell into your file, comment the answer out.  Make sure your code works.

usrNm=[]

for i in range(3):
    usrNm.append(float(input("Enter number: ")))
    s = 0
    for x in (usrNm):
        s += x ** 3

print(s)


# 3.  (extra credit 5 pts) Write Python code that answers this question: How many whole gallons, quarts, pints, cups & ounces of
#  water are there in 7953 ounces of water?  You will need the following measures:
#     1 gallon = 4 quarts
#     1  quart = 2 pints
#     1   pint = 2 cups
#     1    cup = 8 ounces
# Plan on using // and %.  Use appropriate variables with appropriate names to make your code clear.
# Use a labelled print statement of print out the answer:
# " 7953 oz is ___ gallons, ____ quarts, ____ pints, ____ cups, ____ oz.“
# A great way to do this labelled print out is with string concatenation. 
# SHOW YOUR ANSWER and check your code.  Make sure you use Python code to find the answers.  If you do not show your answer, 
# points will be deducted. Copy the answer from the shell into your file, comment the answer out.  Make sure your code works.

