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


# print('LC    UC    Value')
# print('--    --    -----')
# for Letter in lc:
#     UC = Letter.upper()
#     print(Letter, ' or ', UC, '   ', valueOf_1(Letter))
# print()

##############################

#####
# Monday
#####

punctuation = "!\"#$%&’()*+,-./:;<=>?@[\\]^_'{|}~"

def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
        return s_sans_punct

# print(remove_punctuation("Are you very, very, sure?") ==
# "Are you very very sure")

###############################

import string

def remove_punctuation_A(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
        return s_without_punct

my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake’s
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The ’extra stuff’ gets passed out as ---
you guessed it --- snake POOP! """

wds = remove_punctuation(my_story).split()
print(wds)