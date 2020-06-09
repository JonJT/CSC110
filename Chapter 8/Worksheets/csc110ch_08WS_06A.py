# Ws ch8_6A
# Write a function, RmvVwlsFrom(String), which returns the original string with the
# Vowels ‘a’,’e’,’i’,’o’,’u’ removed.  Write a helper function isVowel(Ltr), which returns
# True if Ltr is a vowel & which otherwise returns False.

def isVowel(ltr):
    vowels = 'aeiou'
    return ltr in vowels

def rmvVwlsFrom(String):
    sans_vowels = ''
    for Ltr in String:
        if not isVowel(Ltr): # remove not to make the commented out code work
        #     pass
        # else:
            sans_vowels += Ltr
    return sans_vowels

String = 'hello there'

print(rmvVwlsFrom(String))