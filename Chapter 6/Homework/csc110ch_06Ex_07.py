# Write a function to_secs that converts hours, minutes and seconds to a total number
# of seconds. Here are some tests that should pass:
# test(to_secs(2, 30, 10) == 9010)
# test(to_secs(2, 0, 0) == 7200)
# test(to_secs(0, 2, 0) == 120)
# test(to_secs(0, 0, 42) == 42)
# test(to_secs(0, -10, 10) == -590)

def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print(to_secs(2, 30, 10) == 9010)
print(to_secs(2, 0, 0) == 7200)
print(to_secs(0, 2, 0) == 120)
print(to_secs(0, 0, 42) == 42)
print(to_secs(0, -10, 10) == -590)