# WS 8_1
# Write a function, numValSngl(Char),which takes a
# single character.  If it is a lower case or upper case letter, returns
# 1 for an ‘a’ for an ‘A’, 2 for a ‘b’ or a ‘B’, ….
# 26 for a ‘z’ or a ‘Z’.  If isn't a letter, returns 0.
# Uses the find string method. 

from string import ascii_lowercase as lc, ascii_uppercase as uc

def numValSngl(Char):
    return lc.find(Char.lower()) + 1

print(numValSngl('a'))
print(numValSngl('A'))
print(numValSngl('b'))
print(numValSngl('B'))
print(numValSngl('!'))