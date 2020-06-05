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

# print(numValSngl('a'))
# print(numValSngl('A'))
# print(numValSngl('b'))
# print(numValSngl('B'))
# print(numValSngl('!'))

#-----
# Thursday
#-----
from string import ascii_lowercase as lc, ascii_uppercase as uc

def valueOf(Letter):
    letter = Letter.lower()
    if ('a' <= letter <= 'm'):
        return lc.find(letter)
    else:
        return -25 + lc.find(letter)


# print('LC    UC    Value')
# print('--    --    -----')
# for Letter in lc:
#     UC = Letter.upper()
#     print(Letter, ' or ', UC, '   ', valueOf(Letter))
# print()

##############################

def valueOf_1(Letter):
    letter = Letter.lower()
    if('a' <= letter <= 'k'):
        return lc.find(letter)
    elif('l' <= letter <= 'p'):
        return 10
    else: # 'q' <= letter <= 'z'
        return  25 - lc.find(letter)


print('LC    UC    Value')
print('--    --    -----')
for Letter in lc:
    UC = Letter.upper()
    print(Letter, ' or ', UC, '   ', valueOf_1(Letter))
print()

##############################