# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write
# a function which is given the day number, and it returns the day name (a string).

def dayOfWeek(dayNumber):
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
        return 'Enter a number between 0 & 6, where Sunday is 0 and Saturday is 6'

print(dayOfWeek(4))