#           CSC 110 Spr 20   Quiz 1                                                               NAME: Jonathan Tally
# 10 pts per question.

# You have 153375 millimeters for a length measurement.  Given that:
#     1 centimeter = 10 millimeters
#     1 meter = 100 centimeter = 1000 millimeters
# 1. Use the assignment, integer division and remainder operators (using the remainder operator is easier but you can just use the integer 
# division operator as you like) to convert 153375 millimeters to a whole number of meters, centimeters and millimeters.

# 2. Use the print statement to print out a labelled answer to the above questions (your computed numbers are where the underscores are):

# 153375 millimeters = _______ meters, ________ centimeters, ______ millimeters.

# 3. . Check to make sure you are doing the calculations correctly with Python code by adding up all the millimeters in your answer of meters, 
# centimeters and millimeters & verifying that
# they add to 153375 millimeters.  Print out the result of the check (the underscore should be 153375):

# Check: total millimeters = __________

# 4.  Finally, put your code in a .py file named csc110quiz_1_YourName.py.  The subject of the email is csc110quiz_1_YourName.  
# Your code needs to run without any syntax errors.  And it should run correctly. Submit your code to ctwellman@gmail.com by the start of class next Monday.

# Answer to question number 1 includes the following code

begin = 153375
total_mm = begin

num_m = total_mm // 1000
total_mm %= 1000

num_cm = total_mm // 100
total_mm %= 100

# End question 1 code

print("#2: ", begin, "millimeters = ", num_m, "Meters ",num_cm, "Centimeters, ",total_mm,"Millimeters" )

print("#3: ", "Check: total millimeters =", (num_m*1000) + (num_cm*100) + total_mm)