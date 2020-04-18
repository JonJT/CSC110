# *************************************
# WS ch2_12
# Use a for loop with range to sum all the  odd numbers from 11 to 91.  Use a sum accumulator.
# **************************************

start = 11
end = 91

num_list = range(start, end + 1, 2)
final_sum = sum(num_list)
print(final_sum)