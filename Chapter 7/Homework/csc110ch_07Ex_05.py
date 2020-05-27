# Sum all the elements in a list up to but not including the first even number. (Write your
# unit tests. What if there is no even number?)

xs = [1, 3, 1, 4, 3, 8]

def sumOfInitialOdds(xs):
    '''sum the initial odd numbers in a list and break once it reaches the first even number'''
    sum = 0
    for num in xs:
        if num % 2 != 0:
            sum = sum + num
        else: 
            break
    return sum

print(sumOfInitialOdds(xs))