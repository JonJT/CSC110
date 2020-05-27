# Write a function to count how many odd numbers are in a list.

xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def countOdd(xs):
    oddCount = 0
    for num in xs:
        if num % 2 == 1:
            oddCount += 1
        else:
            pass
    return oddCount

print(countOdd(xs))