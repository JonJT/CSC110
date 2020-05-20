# You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving
# on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general
# version of the program which asks for the starting day number, and the length of your
# stay, and it will tell you the name of day of the week you will return on.

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


def returnDay(startDay, lengthOfStay):
    return_day = (startDay + lengthOfStay % 7) % 7
    return dayOfWeek(return_day)

print(returnDay(3, 137))