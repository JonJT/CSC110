# Write a function day_name that converts an integer number 0 to 6 into the name of a
# day. Assume day 0 is “Sunday”. Once again, return None if the arguments to the function
# are not valid. Here are some tests that should pass:
# test(day_name(3) == "Wednesday")
# test(day_name(6) == "Saturday")
# test(day_name(42) == None)

def day_name(dayNumber):
    if dayNumber == 0:
        return 'Sunday'
    elif dayNumber == 1:
        return 'Monday'
    elif dayNumber == 2:
        return 'Tuesday'
    elif dayNumber == 3:
        return 'Wednesday'
    elif dayNumber == 4:
        return 'Thursday'
    elif dayNumber == 5:
        return 'Friday'
    elif dayNumber == 6:
        return 'Saturday'
    else:
        return 'None'

print(day_name(4) == "Thursday")