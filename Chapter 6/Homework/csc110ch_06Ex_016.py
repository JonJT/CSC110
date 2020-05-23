# Write a function is_factor(f, n) that passes these tests:
# test(is_factor(3, 12))
# test(not is_factor(5, 12))
# test(is_factor(7, 14))
# test(not is_factor(7, 15))
# test(is_factor(1, 15))
# test(is_factor(15, 15))
# test(not is_factor(25, 15))
# An important role of unit tests is that they can also act as unambiguous “specifications”
# of what is expected. These test cases answer the question Do we treat 1 and 15 as factors
# of 15?

def is_factor(f, n):
    if n % f == 0:
        return True
    elif n % f != 0:
        return False


print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7, 14))
print(not is_factor(7, 15))
print(is_factor(1, 15))
print(is_factor(15, 15))
print(not is_factor(25, 15))