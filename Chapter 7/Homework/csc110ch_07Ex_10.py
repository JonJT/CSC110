# Write a function, is_prime, which takes a single integer argument and returns True
# when the argument is a prime number and False otherwise. Add tests for cases like
# this:
# test(is_prime(11))
# test(not is_prime(35))
# test(is_prime(19911121))

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

print(is_prime(11))
print(not is_prime(35))
print(is_prime(19911121))