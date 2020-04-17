# *****************************
# WS ch2_9
# Get a user’s name, then ask the user using that name to provide
# The radius of a circle.  Then, print out the user’s name & the 
# Circumference of the circle.
# *********************************

# Asking for the users name
name = input ("What is your name?: ")
# Asking for the radius of the users circle
radius = float ( input("What is the radius of the circle?: ") )
# Calculating the circumference of the circle
circ = 2*3.14159*radius
# Giving the user the outcome of the calculation
print ( name, "the circumference of your circle is", circ)