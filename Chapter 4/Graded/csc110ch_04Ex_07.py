## grade = 1.0
# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to
# and including n. So sum_to(10) would be 1+2+3...+10 which would return the value
# 55

def sumTo(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

t = sumTo(10)
print("The sum from 1 to 10 is",t)