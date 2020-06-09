# CSC 110 Spring 2020  Quiz 8 Take-home                       NAME: Jonathan Tally
# YouTube: https://youtu.be/48tPtLK09G0
# Write clear, legible code, the simpler the better. Make sure your code works.
# Due next Monday by the start of class.  Use the editor to write your code. Submit a file,
# Quiz_8_YourFullName.py in an email that has as subject  csc 110 quiz 8_YourFullName.
# Points will be deducted if submission is late.   

# 1. [40 pts] Write a function, valueOf(Letter), which takes a letter, Letter and which returns value of the letter, as follows:

from string import ascii_lowercase as lc, ascii_uppercase as uc

def valueOf(Letter):
    letter = Letter.lower()
    if ('a' <= letter <= 'm'):
        return lc.find(letter)
    else:
        return 25 - lc.find(letter)


print('LC    UC    Value')
print('--    --    -----')
for Letter in lc:
    UC = Letter.upper()
    print(Letter, ' or ', UC, '   ', valueOf(Letter))
print()


# 2.  [5 pts] Write a function, maxValueWords(Words), which takes a string, Words,
# of letters separated by spaces, and which returns the word or words in Words that have the max value.
# The value of a word is computed as the sum of the values of the letters using the function from Q1.
# Assume that the words consist entirely of letters.
# Hints:  Write a function, wordValue(Word), which returns the value of a word, Word.
# Consider using the split() string method.  Use a list accumulator to store the value of each word.
# Use the built in function max.
#  Sample run:
#  Words = 'The quick brown foxes jump over the lazy dog pumj'
# print(maxValueWords(Words))

# ['jump', 'pumj’]

Words = 'The quick brown foxes jump over the lazy dog pumj'

def wordValue(Word):
    total = 0
    for ltr in Word:
        total += valueOf(ltr)
    return total

# print(wordValue('the'))

def maxValueWords(Words):
    listOfWords = Words.split()
    values = []
    wordsWithMaxValue = []
    for value in listOfWords:
        values.append(wordValue(value))
    for maxvalue in listOfWords:
        if (wordValue(maxvalue) == max(values)):
            wordsWithMaxValue.append(maxvalue)
    return wordsWithMaxValue

print(maxValueWords(Words))

# To Submit:
# Your quiz .py file, csc110_Quiz_8_YourFullName.py in an email that has as subject csc110_Quiz_8_YourFullName.
# 2.  In your file, put a youtube link of a video showing and discussing Q1.  You need to explain your code.
# Use https://screencast-o-matic.com/ to download a video creation application.   I need to see Python code
# on the screen and to hear your voice as you explain.  Be sure to announce yourself at the beginning of the video.  