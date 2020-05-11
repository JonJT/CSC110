# def addEvens(x, y):
#     '''Return the sum of the evens from x to y, inclusive.'''
#     s = 0
#     for n in range (x, y + 1):
#         if (n % 2 == 0):
#             s += n
#     return s

# x, y = 1, 5

# print(addEvens(x, y))

#######################################

def findAll2_LtrWrds(xs):
    '''Takes a list of words, xs, and returns a list of
    all 2 letter words. If there are not 2 letter words,
    return the empty list.'''
    All_2s = []
    # counter = 0
    for wd in xs:
        if len(wd) == 2:
            # counter += 1
            All_2s.append(wd)
    return All_2s

xs = ['ab', 'abe', 'dogs', 'no', 'on', 'za']

L = findAll2_LtrWrds(xs)
print('There are', len(L), 'two letter words in', L)

