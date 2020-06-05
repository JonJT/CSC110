# Ws ch8_4
# Write a function, count_words_in(Sentence), that returns the number of words in
# Sentence that have between 3 and 7 letters and which contain at least 2 vowels,
# where vowels are taken to be the letters {‘a’,’e’,’I’,’o’,’u’}.

def count_words_in(Sentence):
    '''returns the number of words in Sentence that
    have between 3 and 7 letters and which contain at
    least 2 vowels, where vowels are taken to be the
    letters {'a', 'e', 'i', 'o', 'u'}.'''
    counter = 0
    for word in Sentence.split():
        if (has3To7Letters(word) and hasAtLeast2Vowels(word)):
            counter += 1
    return counter

def has3To7Letters(word):
    '''return True if Word as from 3 to 7 letters,
    inclusive, OTW returns False.'''
    TV = (3 <= len(word) <= 7)
    return TV

def countVowelsIn(word):
    '''return the number of vowels in word'''
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter

def hasAtLeast2Vowels(word):
    '''return True if word has at least 2 vowels, OTW
    return False'''
    TV = (countVowelsIn(word) >= 2)
    return TV

Sentence = 'This is a test of our idea'

print(count_words_in(Sentence))