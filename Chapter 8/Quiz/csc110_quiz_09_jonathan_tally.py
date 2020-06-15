# CSC 110 Spring 2020  Quiz 9 Take-home                       NAME: Jonathan Tally
# YouTube: https://youtu.be/1Dd6RBzGvr4
# Write clear, legible code, the simpler the better. Make sure your code works.
# Due next Monday by the start of class.  Use the editor to write your code.
# Submit a file, Quiz_9_YourFullName.py in an email that has as subject 
# csc 110 quiz 9_YourFullName.   Points will be deducted if submission is late.   

# [20 pts] Write the following function.  Test it to make sure it works as shown in the docstring.

from string import ascii_lowercase as lc

def encodeL(Letter):
    if Letter in lc:
        return lc[(25 - lc.find(Letter))]
        # ndx = lc.find(Letter) '''I though I would leave these in
        # encNdx = 25 - ndx     but I like the one liner better.'''
        # return lc[encNdx]
    else:
        return Letter



for n in lc:
    print(n, encodeL(n))

# 2. [20 pts] Write the following function.  Test it to make sure it works as shown in the docstring.

def encodeW(Word):
    '''Returns Word encoded letter by letter using the first function.
    use a string accumulator'''
    String = ''
    for Ltr in Word:
        String += encodeL(Ltr)
    return String


print(encodeW('abe') == 'zyv')
print(encodeW('zappo') == 'azkkl')
print(encodeW('meal') == 'nvzo')

# 3. [XC 5 pts] Write the following function.  Test it to make sure it works as shown in the docstring.

def undoEncode(EncodedWord):
    String = ''
    for Ltr in EncodedWord:
        String += lc[lc.find(encodeL(Ltr))]
    return String

print(undoEncode('zyv') == 'abe')
print(undoEncode('azkkl') == 'zappo')
print(undoEncode('nvzo') == 'meal')