# Write the inverse function day_num which is given a day name, and returns its number:
# test(day_num("Friday") == 5)
# test(day_num("Sunday") == 0)
# test(day_num(day_name(3)) == 3)
# test(day_name(day_num("Thursday")) == "Thursday")
# Once again, if this function is given an invalid argument, it should return None:
# test(day_num("Halloween") == None)

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