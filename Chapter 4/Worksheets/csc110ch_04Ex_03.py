# *********************************************
# WS ch4_3
# Write a function which return 5! = 1*2*3*4*5
# ********************************************

def fiveFactorial():
    '''Returns 5!'''
    prodAcum = 1
    for i in range(1, 6):
        prodAcum *= i
    return prodAcum

print(fiveFactorial())