# WS ch6 -1 use print to debug this code:
# def avg_2_nums(x, y):
#     '''Returns the average of 2 numbers.'''
#     avg = x+ y/2
#     return avg

def avg_2_nums(x, y):
    '''Returns the average of 2 numbers.'''
    avg = (x + y) / 2
    return avg

x, y = 1, 2
avg = avg_2_nums(x, y)
print(avg)