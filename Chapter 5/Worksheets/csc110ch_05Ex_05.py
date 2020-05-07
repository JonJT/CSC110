# WS ch5_5
# Write a function, tell_if_d3_and_not_d5(num),
# which prints out an appropriate message for all num
# regarding if num is divisible by 3 but
# not divisible by 5.


# Use this function to print out an appropriate message
# for each int from 2 to 20.

def tell_if_d3_and_not_d5(num):
    d3 = (num % 3 == 0)
    d5 = (num % 5 ==0 )
    b = (d3 and not d5)
    if (b):
        print(num, 'is div by 3 but not div by 5')

for n in range(2, 21):
    tell_if_d3_and_not_d5(n)
