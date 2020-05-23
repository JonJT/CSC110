# Write a function that helps answer questions like “‘Today is Wednesday. I leave on
# holiday in 19 days time. What day will that be?”’ So the function must take a day name
# and a delta argument — the number of days to add — and should return the resulting
# day name:
# test(day_add("Monday", 4) == "Friday")
# test(day_add("Tuesday", 0) == "Tuesday")
# test(day_add("Tuesday", 14) == "Tuesday")
# test(day_add("Sunday", 100) == "Tuesday")
# Hint: use the first two functions written above to help you write this one

def day_name(dayName):
    if dayName == 'Sunday':
        return 0
    elif dayName =='Monday':
        return 1
    elif dayName =='Tuesday':
        return 2
    elif dayName =='Wednesday':
        return 3
    elif dayName =='Thursday':
        return 4
    elif dayName =='Friday':
        return 5
    elif dayName =='Saturday':
        return 6
    else:
        return 'None'

print(day_name("Thursday") == 4)