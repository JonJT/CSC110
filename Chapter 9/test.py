#-----
# Monday class
#-----

from string import ascii_lowercase as lc, ascii_uppercase as uc

def numValSngl(Char):
    # a = char.lower()
    # if(a in lc):
    #     x = lc.find(a)
    #     return x + 1
    # else:
    #     return 0
    return lc.find(Char.lower()) + 1

print(numValSngl('a'))
print(numValSngl('A'))
print(numValSngl('b'))
print(numValSngl('B'))
print(numValSngl('!'))

#-----
#
#-----