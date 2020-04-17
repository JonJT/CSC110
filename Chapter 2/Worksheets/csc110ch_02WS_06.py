# ************************************
# WS ch 2_6
# Use the // operator to convert  8911 minutes to days, hours and minutes. (Later, we will meet the modulus operator which can also
# be used.)
# ************************************

begin = 8911
total_min = begin

numdays = total_min // (60*24)
total_min %= 60*24

numhrs = total_min // 60
total_min %= 60

print(begin, "minutes = ", numdays, "days ",numhrs, "hours, ",total_min,"minutes" )