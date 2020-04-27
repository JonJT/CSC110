## grade = 1.0

# The formula for computing the final amount if one is earing compound interest is given on Wikipedia as
# A = P (1 + r/n)**nt
# Where,
#       P = principal amount (initial investment)
#       r = annual nominal interest rate (as a decimal)
#       n = number of times the interst is compounded per year
#       t = number of years
# Write a Python program that assigns the principal amount of $10000 to variable P, assign
# to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt
# the user for the number of year t that the money will be compounded for. Calculate and
# print the final amount after t years.

P = 10000 # principal amount in dollars
n = 12 # number of times a year interest compounds
r = float(0.08) # monthly compound interest rate
t = int(input("Enter the number of years your money will earn 8% interest for:")) # user input

A = P * ( 1 + r/n ) ** (n*t)

print("Your final savings ammount after", t, "years is:", round(A, 2), "USD")