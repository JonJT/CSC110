# WS 8_2
# Write a function, numValMany(Chars)which takes a Chars, a combination of characters,
# and which uses , numValSngl(Char), to return the value of the characters as the sum
# of the values of the characters in Chars.

from string import ascii_lowercase as lc, ascii_uppercase as uc

def numValSngl(Char):
    return lc.find(Char.lower()) + 1

def numValMany(Chars):
    S = 0
    for n in Chars:
        S += numValSngl(n)
    return S

Chars = 'Abe'

print(Chars, "has a value of", numValMany(Chars))

# Chars = 'To be or not to be that is the question'
# P = 1
# L = Chars.split()
# for word in L:
#     P *= numValMany(word)
# print("The product of the values of", Chars, "is", P)



def summation(word): 
    return sum(lettersDict[s.upper()] for s in word)